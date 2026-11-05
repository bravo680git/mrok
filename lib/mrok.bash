# mrok for bash (>= 4.3, emacs editing mode): as-you-type suggestion popup.
#
# How it works:
#  - every printable key is bound to a readline macro: insert the char natively, then
#    run __mrok_update through a hidden `bind -x` key sequence;
#  - Enter / Up / Down / Tab / Ctrl-G are macros "<hidden -x handler><hidden dynamic key>":
#    the handler rebinds the dynamic key to the original readline command (accept-line,
#    previous-history, ...) or to nothing, depending on whether the popup used the key;
#  - the popup is drawn with ANSI escapes on the lines below the prompt.
# Suggestions come from mrok plugins first, then from bash programmable completion
# (bash-completion if installed), then from compgen.

[[ $- == *i* ]] || return 0
[[ -n ${__mrok_loaded-} ]] && return 0
if (( BASH_VERSINFO[0] < 4 || (BASH_VERSINFO[0] == 4 && BASH_VERSINFO[1] < 3) )); then
  echo "mrok: bash >= 4.3 is required (this is $BASH_VERSION)" >&2
  return 0
fi
__mrok_loaded=1

source "$MROK_HOME/lib/api.sh"

: "${MROK_ROWS:=8}"
: "${MROK_BG:=236}" "${MROK_FG:=252}" "${MROK_DESC_FG:=244}"
: "${MROK_SEL_BG:=88}" "${MROK_SEL_FG:=231}" "${MROK_SEL_DESC_FG:=224}" "${MROK_FOOT_FG:=242}"

__MROK_SGR_ROW=$'\e[0;48;5;'"$MROK_BG"';38;5;'"$MROK_FG"'m'
__MROK_SGR_DESC=$'\e[0;48;5;'"$MROK_BG"';38;5;'"$MROK_DESC_FG"'m'
__MROK_SGR_SEL=$'\e[0;1;48;5;'"$MROK_SEL_BG"';38;5;'"$MROK_SEL_FG"'m'
__MROK_SGR_SELDESC=$'\e[0;48;5;'"$MROK_SEL_BG"';38;5;'"$MROK_SEL_DESC_FG"'m'
__MROK_SGR_FOOT=$'\e[0;48;5;'"$MROK_BG"';38;5;'"$MROK_FOOT_FG"'m'
__MROK_SGR_OFF=$'\e[0m'

# Suggestions (0-based): display, inserted text, suffix, description
__mrok_c=() __mrok_i=() __mrok_s=() __mrok_d=()
__mrok_sel=0          # 1-based selected row, 0 = nothing selected
__mrok_top=1
__mrok_visible=0
__mrok_drawn=0        # rows currently drawn under the prompt
__mrok_promptw=0
__mrok_pline=''
__mrok_pdone=0        # prompt measured for the current prompt
__mrok_lastout=''     # last popup output, to skip identical redraws
declare -gA __mrok_pcache=() __mrok_pstat=()

__mrok_log() { [[ -n ${MROK_DEBUG-} ]] && printf '%s %s\n' "${EPOCHREALTIME-}" "$*" >> "$MROK_DEBUG"; }

__mrok_list_plugins() {
  local k
  for k in "${!__mrok_plugins[@]}"; do printf '%s\t%s\n' "$k" "${__mrok_plugins[$k]}"; done
}

# ---------------------------------------------------------------- parsing
# Sets: __mrok_left (line before cursor), __mrok_cur (word being typed),
#       __mrok_seg (words of the current command before __mrok_cur), __mrok_cmdpos
__mrok_parse() {
  __mrok_left=${READLINE_LINE:0:READLINE_POINT}
  local -a w
  read -r -a w <<< "$__mrok_left"
  if [[ -z $__mrok_left || $__mrok_left == *[[:space:]] ]]; then
    __mrok_cur=''
  else
    __mrok_cur=${w[${#w[@]}-1]}
    unset "w[${#w[@]}-1]"
  fi
  local i start=0
  for (( i = 0; i < ${#w[@]}; i++ )); do
    case ${w[i]} in
      ';'|'|'|'||'|'&&'|'&'|'|&'|'('|'{'|'!'|then|do|else|sudo|time|nohup|exec|command|xargs)
        start=$(( i + 1 )) ;;
    esac
  done
  __mrok_seg=( "${w[@]:start}" )
  if (( ${#__mrok_seg[@]} == 0 )); then __mrok_cmdpos=1; else __mrok_cmdpos=0; fi
}

# ---------------------------------------------------------------- candidates
__mrok_add() {  # value insert suffix description
  __mrok_c+=( "$1" ); __mrok_i+=( "$2" ); __mrok_s+=( "$3" ); __mrok_d+=( "$4" )
}

# Quote a word for the command line, keeping a leading ~ expandable
__mrok_quote() {
  if [[ $1 == '~'* ]]; then
    local rest=${1#\~}
    if [[ -n $rest ]]; then printf -v REPLY '~%q' "$rest"; else REPLY='~'; fi
  else
    printf -v REPLY '%q' "$1"
  fi
}

__mrok_from_plugin() {
  local cmd=${__mrok_seg[0]}
  local fn=${__mrok_plugins[$cmd]-}
  [[ -n $fn ]] || return 1
  local key="$PWD|${__mrok_seg[*]}|${__mrok_cur:0:1}"
  if [[ -z ${__mrok_pstat[$key]+x} ]]; then
    __mrok_pcache[$key]=$(MROK_CUR=$__mrok_cur "$fn" "${__mrok_seg[@]}" 2>/dev/null)
    __mrok_pstat[$key]=$?
  fi
  (( __mrok_pstat[$key] == 0 )) || return 1
  local line v d suf
  while IFS= read -r line; do
    v=${line%%$'\t'*}
    [[ -z $v ]] && continue
    d=''; [[ $line == *$'\t'* ]] && d=${line#*$'\t'}
    suf=' '; [[ $v == *[/=] ]] && suf=''
    __mrok_quote "$v"
    __mrok_add "$v" "$REPLY" "$suf" "$d"
  done <<< "${__mrok_pcache[$key]}"
  return 0
}

# Results of a path-like completion: directories get a '/' and show their last part
__mrok_add_paths() {
  local p full disp
  for p in "$@"; do
    p=${p%/}
    full=$p; [[ $full == '~'* ]] && full=$HOME${full#\~}
    disp=$p
    [[ $__mrok_cur == */* && $p == */* ]] && disp=${p##*/}
    __mrok_quote "$p"
    if [[ -d $full ]]; then __mrok_add "$disp/" "$REPLY" '/' ''
    else __mrok_add "$disp" "$REPLY" ' ' ''
    fi
  done
}

__mrok_from_native() {
  local cmd=${__mrok_seg[0]} cur=$__mrok_cur
  local -a res=()
  case $cmd in
    cd|pushd|rmdir)
      mapfile -t res < <(compgen -d -- "$cur" 2>/dev/null | head -300)
      __mrok_add_paths "${res[@]}"
      return ;;
  esac
  local spec
  spec=$(complete -p -- "$cmd" 2>/dev/null)
  if [[ -z $spec ]] && declare -F _completion_loader >/dev/null; then
    _completion_loader "$cmd" >/dev/null 2>&1
    spec=$(complete -p -- "$cmd" 2>/dev/null)
  fi
  [[ -z $spec ]] && spec=$(complete -p -D 2>/dev/null)

  local fn=''
  [[ $spec =~ (^|[[:space:]])-F[[:space:]]+([^[:space:]]+) ]] && fn=${BASH_REMATCH[2]}
  if [[ -n $fn ]] && declare -F "$fn" >/dev/null; then
    local COMP_WORDS=( "${__mrok_seg[@]}" "$cur" )
    local COMP_CWORD=${#__mrok_seg[@]}
    local COMP_LINE="${__mrok_seg[*]} $cur"
    local COMP_POINT=${#COMP_LINE}
    local COMP_TYPE=9 COMP_KEY=9
    local prev=${__mrok_seg[${#__mrok_seg[@]}-1]}
    COMPREPLY=()
    "$fn" "$cmd" "$cur" "$prev" >/dev/null 2>&1
    res=( "${COMPREPLY[@]}" )
    COMPREPLY=()
    # bash-completion asks for the default (file) completion with an empty reply
    (( ${#res[@]} )) || mapfile -t res < <(compgen -f -- "$cur" 2>/dev/null | head -300)
  elif [[ -n $spec ]]; then
    local opts=${spec#complete }
    opts=${opts% *}
    opts=$(sed -E 's/(^| )-o [a-z]+//g; s/(^| )-F [^ ]+//g' <<< "$opts")
    mapfile -t res < <(eval "compgen $opts -- \"\$cur\"" 2>/dev/null | head -300)
  else
    mapfile -t res < <(compgen -f -- "$cur" 2>/dev/null | head -300)
  fi

  local r v full
  local -a paths=()
  for r in "${res[@]}"; do
    [[ -z $r ]] && continue
    v=${r%% }
    full=$v; [[ $full == '~'* ]] && full=$HOME${full#\~}
    if [[ -e $full || $v == */* ]]; then
      paths+=( "$v" )
    else
      __mrok_quote "$v"
      if [[ $r == *' ' || $v != *[/=] ]]; then __mrok_add "$v" "$REPLY" ' ' ''
      else __mrok_add "$v" "$REPLY" '' ''
      fi
    fi
  done
  (( ${#paths[@]} )) && __mrok_add_paths "${paths[@]}"
}

__mrok_from_commands() {
  local cur=$__mrok_cur
  local name
  while IFS= read -r name; do
    [[ -z $name ]] && continue
    [[ $name == [_.]* && $cur != [_.]* ]] && continue
    __mrok_add "$name" "$name" ' ' ''
  done < <(compgen -c -- "$cur" 2>/dev/null | awk -v w="$cur" '!seen[$0]++ { printf "%d %05d %s\n", ($0 != w), length($0), $0 }' | sort | head -300 | cut -d' ' -f3-)
}

# Keep the best tier that has any match: prefix > substring > fuzzy (the typed
# characters in order, e.g. "chp" -> cherry-pick); dedupe.
__mrok_filter() {
  local cur=${__mrok_cur#[\"\']} lw i tier=0 ch q fz='*'
  lw=${cur,,}
  local -a c=() ii=() ss=() d=()
  local -A seen=()
  if [[ -n $lw ]]; then
    for (( i = 0; i < ${#lw}; i++ )); do
      ch=${lw:i:1}; printf -v q '%q' "$ch"; fz+="$q*"
    done
    for (( i = 0; i < ${#__mrok_c[@]}; i++ )); do
      if [[ ${__mrok_i[i],,} == "$lw"* || ${__mrok_c[i],,} == "$lw"* ]]; then tier=1; break
      elif [[ ${__mrok_c[i],,} == *"$lw"* ]]; then tier=2
      elif (( tier != 2 )) && [[ ${__mrok_c[i],,} == $fz ]]; then tier=3
      fi
    done
    (( tier )) || { __mrok_c=() __mrok_i=() __mrok_s=() __mrok_d=(); return; }
  fi
  for (( i = 0; i < ${#__mrok_c[@]}; i++ )); do
    [[ -n ${seen[${__mrok_i[i]}]+x} ]] && continue
    case $tier in
      1) [[ ${__mrok_i[i],,} == "$lw"* || ${__mrok_c[i],,} == "$lw"* ]] || continue ;;
      2) [[ ${__mrok_c[i],,} == *"$lw"* ]] || continue ;;
      3) [[ ${__mrok_c[i],,} == $fz ]] || continue ;;
    esac
    seen[${__mrok_i[i]}]=1
    c+=( "${__mrok_c[i]}" ); ii+=( "${__mrok_i[i]}" ); ss+=( "${__mrok_s[i]}" ); d+=( "${__mrok_d[i]}" )
    (( ${#c[@]} >= 300 )) && break
  done
  __mrok_c=( "${c[@]}" ) __mrok_i=( "${ii[@]}" ) __mrok_s=( "${ss[@]}" ) __mrok_d=( "${d[@]}" )
}

# $1 = 1: forced (Tab);  $2 = 1: preselect first row while typing a word
__mrok_compute() {
  local force=${1:-0} autosel=${2:-1}
  __mrok_c=() __mrok_i=() __mrok_s=() __mrok_d=()
  __mrok_parse
  if (( __mrok_cmdpos )); then
    if [[ -z $__mrok_cur ]] && (( ! force )); then __mrok_visible=0; return; fi
    __mrok_from_commands
  else
    __mrok_from_plugin || __mrok_from_native
  fi
  __mrok_filter
  __mrok_log "COMPUTE line=[$READLINE_LINE] cur=[$__mrok_cur] n=${#__mrok_c[@]} c=[${__mrok_c[*]:0:12}] i0=[${__mrok_i[0]-}] d0=[${__mrok_d[0]-}]"

  local n=${#__mrok_c[@]}
  if (( n == 0 )); then __mrok_visible=0; return; fi
  if (( n == 1 )) && [[ ${__mrok_i[0]} == "$__mrok_cur" && ${__mrok_s[0]} != / ]]; then
    __mrok_visible=0; return
  fi
  __mrok_visible=1
  __mrok_top=1
  if (( autosel )) && [[ -n $__mrok_cur ]]; then __mrok_sel=1; else __mrok_sel=0; fi
}

# ---------------------------------------------------------------- drawing
# Once per prompt (PS1 can run commands): __mrok_promptw = width of the prompt's last
# line, __mrok_pline = that line as printed (colors kept), '' on bash 4.3.
__mrok_prompt_width() {
  (( __mrok_pdone )) && return
  __mrok_pdone=1
  local p=''
  if (( BASH_VERSINFO[0] > 4 || BASH_VERSINFO[1] >= 4 )); then
    p=${PS1@P}
  fi
  p=${p##*$'\n'}
  __mrok_pline=${p//[$'\001\002']/}
  # drop \[ \] markers (\001 \002) and what's between them, then ANSI sequences
  while [[ $p == *$'\001'*$'\002'* ]]; do
    p=${p%%$'\001'*}${p#*$'\002'}
  done
  local re=$'\e''\[[0-9;?]*[a-zA-Z]'
  while [[ $p =~ $re ]]; do p=${p/"${BASH_REMATCH[0]}"/}; done
  __mrok_promptw=${#p}
}

# bash clears the prompt line before running a `bind -x` handler and redraws it only
# after the handler returns: over ssh the terminal shows the blank line in between
# (flicker on every key). Put the line back right away; bash's redraw then writes the
# same text over it. Only when the line fits on one screen line.
__mrok_restore_line() {
  __mrok_prompt_width
  [[ -n $__mrok_pline ]] || return 0
  (( __mrok_promptw + ${#READLINE_LINE} < ${COLUMNS:-80} )) || return 0
  printf '%s%s\r' "$__mrok_pline" "$READLINE_LINE" > /dev/tty
}

__mrok_pad() {  # printf -v REPLY a string padded/truncated to width $2
  local s=$1 w=$2
  if (( ${#s} > w )); then
    if (( w > 0 )); then s="${s:0:w-1}…"; else s=''; fi
  fi
  printf -v REPLY '%-*s' "$w" "$s"
}

__mrok_draw() {
  local out='' cols=${COLUMNS:-80}
  local n=0 rows=0
  (( __mrok_visible )) && n=${#__mrok_c[@]}
  if (( n > 0 )); then
    rows=$MROK_ROWS; (( rows > n )) && rows=$n
    if (( __mrok_sel > 0 )); then
      (( __mrok_sel < __mrok_top )) && __mrok_top=$__mrok_sel
      (( __mrok_sel >= __mrok_top + rows )) && __mrok_top=$(( __mrok_sel - rows + 1 ))
    fi
    (( __mrok_top > n - rows + 1 )) && __mrok_top=$(( n - rows + 1 ))
    (( __mrok_top < 1 )) && __mrok_top=1
  fi
  local foot=''
  if (( n > rows )); then
    foot="  $__mrok_sel/$n"
    (( __mrok_sel == 0 )) && foot="  $n matches · ↓ to select"
  fi
  local total=$rows
  [[ -n $foot ]] && (( total++ ))

  # Nothing drawn and nothing to draw
  (( total == 0 && __mrok_drawn == 0 )) && return

  if (( total > 0 )); then
    # Make room below (scrolls when at the bottom) without losing the cursor column
    local k
    for (( k = 0; k < total; k++ )); do out+=$'\eD'; done
    out+=$'\e['"$total"'A'
  fi
  # Save the cursor once (restored once at the end), go to the next line, clear the
  # old popup; rows are then drawn one line further down each time.
  out+=$'\e7\e[1B\r\e[J'

  if (( total > 0 )); then
    local i namew=0 descw=0 last=$(( __mrok_top + rows - 1 ))
    for (( i = __mrok_top; i <= last; i++ )); do
      (( ${#__mrok_c[i-1]} > namew )) && namew=${#__mrok_c[i-1]}
      (( ${#__mrok_d[i-1]} > descw )) && descw=${#__mrok_d[i-1]}
    done
    (( namew > 40 )) && namew=40
    (( namew < 12 )) && namew=12
    (( descw > 60 )) && descw=60
    local maxw=$(( cols - 2 ))
    local width=$(( 2 + namew + (descw ? 2 + descw : 0) + 1 ))
    if (( width < ${#foot} + 1 )); then namew=$(( namew + ${#foot} + 1 - width )); width=$(( ${#foot} + 1 )); fi
    if (( width > maxw )); then
      descw=$(( descw - (width - maxw) ))
      if (( descw < 0 )); then namew=$(( namew + descw )); descw=0; fi
      width=$maxw
    fi
    local indent=$(( __mrok_promptw + ${#__mrok_left} - ${#__mrok_cur} - 2 ))
    (( indent + width > cols - 1 )) && indent=$(( cols - 1 - width ))
    (( indent < 0 )) && indent=0

    local r=1 name desc sgr dsgr
    for (( i = __mrok_top; i <= last; i++, r++ )); do
      if (( i == __mrok_sel )); then sgr=$__MROK_SGR_SEL; dsgr=$__MROK_SGR_SELDESC
      else sgr=$__MROK_SGR_ROW; dsgr=$__MROK_SGR_DESC; fi
      __mrok_pad "${__mrok_c[i-1]}" "$namew"; name=$REPLY
      (( r > 1 )) && out+=$'\e[1B\r'
      (( indent )) && out+=$'\e['"$indent"'C'
      out+="$sgr  $name"
      if (( descw )); then
        __mrok_pad "${__mrok_d[i-1]}" "$descw"; desc=$REPLY
        out+="  $dsgr$desc"
      fi
      out+=" $__MROK_SGR_OFF"
    done
    if [[ -n $foot ]]; then
      __mrok_pad "$foot" "$width"
      out+=$'\e[1B\r'
      (( indent )) && out+=$'\e['"$indent"'C'
      out+="$__MROK_SGR_FOOT$REPLY$__MROK_SGR_OFF"
    fi
  fi
  out+=$'\e8'
  # Same popup as on screen already (typing within a word that doesn't change it)
  [[ $out == "$__mrok_lastout" ]] && return
  printf '%s' "$out" > /dev/tty
  __mrok_lastout=$out
  __mrok_drawn=$total
}

# ---------------------------------------------------------------- key handlers
# Hidden key sequences (prefix \C-x\C-_ is unbound by default)
__MROK_K=$'\\C-x\\C-_'

__mrok_dyn() {  # __mrok_dyn <id> <readline-command or "">
  if [[ -n $2 ]]; then bind "\"${__MROK_K}$1\": $2"
  else bind "\"${__MROK_K}$1\": \"\""
  fi
}

__mrok_update() {   # after a character was inserted / deleted
  __mrok_restore_line
  __mrok_compute 0 1
  __mrok_draw
}

__mrok_hide() {
  __mrok_visible=0
  __mrok_sel=0
  __mrok_c=() __mrok_i=() __mrok_s=() __mrok_d=()
  __mrok_draw
}

__mrok_accept() {   # accept row $1 (1-based)
  local idx=$(( $1 - 1 ))
  local ins=${__mrok_i[idx]} suf=${__mrok_s[idx]}
  __mrok_parse
  local left=${__mrok_left:0:${#__mrok_left}-${#__mrok_cur}}$ins$suf
  READLINE_LINE=$left${READLINE_LINE:READLINE_POINT}
  READLINE_POINT=${#left}
  __mrok_log "ACCEPT ins=[$ins] suf=[$suf] line=[$READLINE_LINE]"
  __mrok_compute 0 0
  __mrok_draw
}

__mrok_key_enter() {
  __mrok_restore_line
  if (( __mrok_visible && __mrok_sel > 0 )); then
    __mrok_parse
    if [[ -n $__mrok_cur && ${__mrok_i[__mrok_sel-1]} == "$__mrok_cur" && ${__mrok_s[__mrok_sel-1]} != / ]]; then
      __mrok_hide; __mrok_dyn E accept-line; return
    fi
    __mrok_dyn E ''
    __mrok_accept "$__mrok_sel"
    return
  fi
  (( __mrok_drawn )) && __mrok_hide
  __mrok_dyn E accept-line
}

__mrok_key_tab() {
  __mrok_restore_line
  if (( __mrok_visible )); then
    __mrok_dyn T ''
    __mrok_accept $(( __mrok_sel ? __mrok_sel : 1 ))
    return
  fi
  __mrok_compute 1 1
  if (( __mrok_visible )); then
    (( __mrok_sel == 0 )) && __mrok_sel=1
    __mrok_prompt_width
    __mrok_draw
    __mrok_dyn T ''
  else
    __mrok_dyn T complete
  fi
}

__mrok_key_up() {
  __mrok_restore_line
  if (( __mrok_visible )); then
    (( __mrok_sel = __mrok_sel <= 1 ? ${#__mrok_c[@]} : __mrok_sel - 1 ))
    __mrok_draw
    __mrok_dyn K ''
  else
    __mrok_dyn K "$__mrok_up_cmd"
  fi
}

__mrok_key_down() {
  __mrok_restore_line
  if (( __mrok_visible )); then
    (( __mrok_sel = __mrok_sel >= ${#__mrok_c[@]} ? 1 : __mrok_sel + 1 ))
    __mrok_draw
    __mrok_dyn J ''
  else
    __mrok_dyn J "$__mrok_down_cmd"
  fi
}

__mrok_key_cancel() {   # Ctrl-G
  __mrok_restore_line
  if (( __mrok_visible )); then
    __mrok_hide
    __mrok_dyn G ''
  else
    __mrok_dyn G abort
  fi
}

__mrok_key_esc() {      # Esc: hide the popup, otherwise keep Esc's own binding
  __mrok_restore_line
  if (( __mrok_visible )); then
    __mrok_hide
    __mrok_dyn X ''
  else
    __mrok_dyn X "$__mrok_esc_cmd"
  fi
}

# A popup left on screen by Ctrl-C: the new prompt starts where it was drawn
__mrok_precmd() {
  if (( __mrok_drawn )); then
    printf '\e[J' > /dev/tty
    __mrok_drawn=0
  fi
  __mrok_visible=0
  __mrok_sel=0
  __mrok_pcache=() __mrok_pstat=()
  __mrok_pdone=0
  __mrok_lastout=''
}

# ---------------------------------------------------------------- bindings
__mrok_orig() {  # current readline command bound to key $1 (in `bind -p` notation)
  local line
  line=$(bind -p 2>/dev/null | grep -F "\"$1\": " | head -1)
  REPLY=${line##*: }
  [[ -z $REPLY ]] && REPLY=$2
}

__mrok_setup_bindings() {
  local K=$__MROK_K
  # hidden helpers
  bind -x "\"${K}u\": __mrok_update"
  bind "\"${K}q\": quoted-insert"
  bind "\"${K}b\": backward-delete-char"
  bind "\"${K}w\": unix-word-rubout"
  bind -x "\"${K}e\": __mrok_key_enter"
  bind -x "\"${K}t\": __mrok_key_tab"
  bind -x "\"${K}k\": __mrok_key_up"
  bind -x "\"${K}j\": __mrok_key_down"
  bind -x "\"${K}g\": __mrok_key_cancel"
  bind -x "\"${K}x\": __mrok_key_esc"
  __mrok_dyn E accept-line
  __mrok_dyn T complete
  __mrok_orig '\e[A' previous-history; __mrok_up_cmd=$REPLY
  __mrok_orig '\e[B' next-history;     __mrok_down_cmd=$REPLY
  __mrok_dyn K "$__mrok_up_cmd"
  __mrok_dyn J "$__mrok_down_cmd"
  __mrok_dyn G abort
  # Esc alone: vi-movement-mode in vi mode, nothing in emacs mode (it's only a prefix)
  __mrok_orig '\e' ''
  [[ -z $REPLY && -o vi ]] && REPLY=vi-movement-mode   # bind -p lists it as "\e\000"
  __mrok_esc_cmd=$REPLY
  __mrok_dyn X "$__mrok_esc_cmd"

  # printable characters: native insert, then update
  local code ch ks
  for (( code = 32; code < 127; code++ )); do
    printf -v ch "\\$(printf '%03o' "$code")"
    case $ch in
      '"')  ks='\"' ;;
      '\')  ks='\\' ;;
      *)    ks=$ch ;;
    esac
    bind "\"$ks\": \"${K}q$ks${K}u\""
  done
  bind "\"\\C-?\": \"${K}b${K}u\""
  bind "\"\\C-h\": \"${K}b${K}u\""
  bind "\"\\C-w\": \"${K}w${K}u\""

  bind "\"\\C-m\": \"${K}e${K}E\""
  bind "\"\\C-j\": \"${K}e${K}E\""
  bind "\"\\C-i\": \"${K}t${K}T\""
  bind "\"\\e[A\": \"${K}k${K}K\""
  bind "\"\\eOA\": \"${K}k${K}K\""
  bind "\"\\e[B\": \"${K}j${K}J\""
  bind "\"\\eOB\": \"${K}j${K}J\""
  bind "\"\\C-g\": \"${K}g${K}G\""
  # Readline tells a lone Esc from Esc-prefixed keys (arrows, Alt-x) by waiting keyseq-timeout
  bind "\"\\e\": \"${K}x${K}X\""
}

__mrok_load_plugins
__mrok_setup_bindings

if [[ ${PROMPT_COMMAND-} != *__mrok_precmd* ]]; then
  PROMPT_COMMAND="__mrok_precmd${PROMPT_COMMAND:+;$PROMPT_COMMAND}"
fi
