# mrok for zsh: as-you-type suggestion popup.
#
# Suggestions come from mrok plugins first (plugins/*.sh, ~/.config/mrok/plugins/*.sh),
# then from zsh's own completion system (directories, git, options, ...).
# The popup is drawn under the command line with POSTDISPLAY + region_highlight.

[[ -o interactive ]] || return 0
(( ${+__mrok_loaded} )) && return 0
typeset -g __mrok_loaded=1
zmodload zsh/datetime 2>/dev/null

# Needs the completion system; load it if the user's config didn't.
if (( ! $+functions[compdef] )); then
  autoload -Uz compinit && compinit -i
fi

source "$MROK_HOME/lib/api.sh"

: ${MROK_ROWS:=8}
# Colors: 256-color palette numbers
: ${MROK_BG:=236} ${MROK_FG:=252} ${MROK_DESC_FG:=244}
: ${MROK_SEL_BG:=88} ${MROK_SEL_FG:=231} ${MROK_SEL_DESC_FG:=224} ${MROK_FOOT_FG:=242}

typeset -g __MROK_ST_ROW="bg=$MROK_BG,fg=$MROK_FG"
typeset -g __MROK_ST_DESC="bg=$MROK_BG,fg=$MROK_DESC_FG"
typeset -g __MROK_ST_SEL="bg=$MROK_SEL_BG,fg=$MROK_SEL_FG,bold"
typeset -g __MROK_ST_SELDESC="bg=$MROK_SEL_BG,fg=$MROK_SEL_DESC_FG"
typeset -g __MROK_ST_FOOT="bg=$MROK_BG,fg=$MROK_FOOT_FG"

# Case-insensitive matching for mrok's own completion calls only; fall back to
# partial-word, substring, then fuzzy (chars in order) matching when nothing matches.
zstyle ':completion:__mrok-complete:*' matcher-list \
  'm:{a-z}={A-Za-z}' \
  'm:{a-z}={A-Za-z} r:|[._-]=* r:|=*' \
  'm:{a-z}={A-Za-z} l:|=* r:|=*' \
  'm:{a-z}={A-Za-z} r:|?=**'

# ---------------------------------------------------------------- state
# Each suggestion: __mrok_c display text, __mrok_i text that replaces the current word,
#                  __mrok_s suffix ('/' dir, ' ' normal, '' none), __mrok_d description
typeset -ga __mrok_c __mrok_i __mrok_s __mrok_d
typeset -gi __mrok_sel=0 __mrok_top=1 __mrok_visible=0 __mrok_busy=0 __mrok_promptw=0
typeset -g  __mrok_last=''
typeset -gA __mrok_orig_keys __mrok_pcache __mrok_pstat
# Keys bound while the popup is shown. Esc then Enter typed within KEYTIMEOUT arrives as
# one key, ^[^M, which zsh binds to inserting a newline: make it "hide and run" instead.
typeset -ga __MROK_KEYS=( '^[[A' '^[OA' '^[[B' '^[OB' '^M' '^[' '^[^M' '^[^J' )

__mrok_log() { [[ -n $MROK_DEBUG ]] && print -r -- "${EPOCHREALTIME:-} $*" >> $MROK_DEBUG }

__mrok_list_plugins() {
  local k
  for k in ${(k)__mrok_plugins}; do print -r -- "$k	${__mrok_plugins[$k]}"; done
}

# ---------------------------------------------------------------- native completion capture
# Replacement for compadd, active only while __mrok_complete runs: collect matches into
# our arrays together with the prefixes/suffixes zsh would insert.
__mrok_compadd() {
  local -a args; args=( "$@" )
  local P='' p='' s='' S='' W='' ip='' dvar='' val opt rest
  local -i Q=0 f=0 hasS=0 query=0 i=1
  while (( i <= $#args )); do
    rest=${args[i]}
    [[ $rest == (-|--) ]] && break
    [[ $rest != -* ]] && break
    rest=${rest#-}
    while [[ -n $rest ]]; do
      opt=${rest[1]}; rest=${rest[2,-1]}
      case $opt in
        [PpSsiIWJVXxrRMFOADdE])
          if [[ -n $rest ]]; then val=$rest; rest=''; else (( i++ )); val=${args[i]}; fi
          case $opt in
            P) P=$val ;; p) p=$val ;; s) s=$val ;; S) S=$val; hasS=1 ;;
            W) W=$val ;; i) ip=$val ;; d) dvar=$val ;; [OAD]) query=1 ;;
          esac ;;
        o) # -o [order]: value is glued or the next argument
           if [[ -z $rest && ${args[i+1]} == [a-z]* ]]; then (( i++ )); fi
           rest='' ;;
        Q) Q=1 ;;
        f) f=1 ;;
      esac
    done
    (( i++ ))
  done
  # compadd used only to query (-O/-A/-D): run it untouched
  if (( query )); then builtin compadd "$@"; return; fi

  local -a __hits __dscr
  [[ -n $dvar ]] && __dscr=( "${(@P)dvar}" )
  builtin compadd -A __hits -D __dscr "$@"
  (( $#__hits )) || return 1
  # Really add them so zsh stops trying looser matchers; the zsh menu itself is
  # disabled in __mrok_complete, so nothing is displayed.
  builtin compadd "$@"

  local h disp ins suf fp k
  for (( k = 1; k <= $#__hits; k++ )); do
    h=${__hits[k]}
    if (( Q )); then disp=${(Q)h}; ins="$IPREFIX$ip$P$p$h$s"
    else disp=$h; ins="$IPREFIX$ip$P$p${(q)h}$s"
    fi
    while [[ $disp == *' ' ]]; do disp=${disp% }; done
    if (( f )); then
      if [[ -n $W ]]; then fp=${W%/}/$h; else fp=$p$h; fi
      [[ $fp == '~'* ]] && fp=$HOME${fp#\~}
      if [[ -d $fp ]]; then suf='/'; disp+='/'; else suf=' '; fi
    elif (( hasS )); then suf=$S
    else suf=' '
    fi
    __mrok_c+=( "$disp" ); __mrok_i+=( "$ins" ); __mrok_s+=( "$suf" )
    __mrok_d+=( "${__dscr[k]}" )
  done
  return 0
}

__mrok_complete() {
  setopt localoptions nobeep nolistbeep
  __mrok_c=() __mrok_i=() __mrok_s=() __mrok_d=()
  functions[compadd]=$functions[__mrok_compadd]
  {
    _main_complete 2>/dev/null
  } always {
    unfunction compadd 2>/dev/null
  }
  compstate[insert]=''
  compstate[list]=''
}
zle -C __mrok-complete complete-word __mrok_complete

# ---------------------------------------------------------------- plugins
# $1 = current word, $2.. = words before it. Fills the arrays and returns 0 when a
# plugin handled this position.
__mrok_from_plugin() {
  local word=$1; shift
  local -a seg; seg=( "$@" )
  local i
  for (( i = $#seg; i >= 1; i-- )); do
    [[ ${seg[i]} == (';'|'|'|'||'|'&&'|'&'|'|&'|'('|'{'|'!'|then|do|else) ]] && break
  done
  seg=( "${(@)seg[i+1,-1]}" )
  while (( $#seg )) && [[ ${seg[1]} == (sudo|time|nohup|command|noglob|exec) ]]; do
    shift seg
  done
  (( $#seg )) || return 1
  local fn=${__mrok_plugins[${seg[1]}]}
  [[ -n $fn ]] || return 1
  seg=( "${(@Q)seg}" )
  local cur=${(Q)word}
  local key="$PWD|${(pj:\0:)seg}|${cur[1]}"
  if (( ! ${+__mrok_pstat[$key]} )); then
    __mrok_pcache[$key]="$(MROK_CUR=$cur "$fn" "${seg[@]}" 2>/dev/null)"
    __mrok_pstat[$key]=$?
  fi
  (( __mrok_pstat[$key] == 0 )) || return 1

  __mrok_c=() __mrok_i=() __mrok_s=() __mrok_d=()
  local line v
  for line in "${(@f)__mrok_pcache[$key]}"; do
    v=${line%%$'\t'*}
    [[ -z $v ]] && continue
    __mrok_c+=( "$v" )
    if [[ $v == '~'* ]]; then __mrok_i+=( "~${(q)v#\~}" ); else __mrok_i+=( "${(q)v}" ); fi
    if [[ $v == *[/=] ]]; then __mrok_s+=( '' ); else __mrok_s+=( ' ' ); fi
    if [[ $line == *$'\t'* ]]; then __mrok_d+=( "${line#*$'\t'}" ); else __mrok_d+=( '' ); fi
  done
  return 0
}

# ---------------------------------------------------------------- helpers
# REPLY = length of the word right before the cursor
__mrok_wordlen() {
  if [[ -z $LBUFFER || $LBUFFER == *[[:space:]] ]]; then REPLY=0; return; fi
  local -a w; w=( ${(z)LBUFFER} )
  REPLY=${#w[-1]}
}

# Succeeds when the word being typed is in command position
__mrok_cmdpos() {
  local wl=$1
  local -a w; w=( ${(z)LBUFFER} )
  local n=$#w
  (( wl > 0 )) && (( n-- ))
  (( n < 1 )) && return 0
  [[ ${w[n]} == (';'|'|'|'||'|'&&'|'&'|'|&'|'('|'{'|'!'|sudo|then|do|else|time|nohup|exec|command|noglob|xargs) ]]
}

__mrok_bind() {
  local k
  if (( $1 )); then
    bindkey '^[[A' mrok-up;   bindkey '^[OA' mrok-up
    bindkey '^[[B' mrok-down; bindkey '^[OB' mrok-down
    bindkey '^M'   mrok-enter
    bindkey '^['   mrok-esc
    bindkey '^[^M' mrok-run; bindkey '^[^J' mrok-run
  else
    for k in $__MROK_KEYS; do
      if [[ -z ${__mrok_orig_keys[$k]} || ${__mrok_orig_keys[$k]} == undefined-key ]]; then
        bindkey -r "$k"
      else
        bindkey "$k" ${__mrok_orig_keys[$k]}
      fi
    done
  fi
}

__mrok_hide() {
  if (( __mrok_visible )); then
    __mrok_visible=0
    __mrok_bind 0
  fi
  __mrok_c=() __mrok_i=() __mrok_s=() __mrok_d=()
  __mrok_sel=0
}

# Width of the last prompt line, to put the popup right under the word being typed.
# Computed when the popup opens: themes like oh-my-zsh update git info asynchronously.
__mrok_prompt_width() {
  setopt localoptions extendedglob
  local p
  if [[ -o promptsubst ]]; then p=${(%)${(e)PS1}}; else p=${(%)PS1}; fi
  p=${p##*$'\n'}
  p=${(S)p//$'\e'\][^$'\a']#$'\a'/}
  p=${(S)p//$'\e'\[[0-9;?]#[a-zA-Z]/}
  __mrok_promptw=${(m)#p}
}

__mrok_show() {
  __mrok_top=1
  if (( ! __mrok_visible )); then
    __mrok_visible=1
    __mrok_bind 1
    __mrok_prompt_width 2>/dev/null
  fi
}

# ---------------------------------------------------------------- compute
# $1 = 1: forced (Tab), show even for an empty command name
# $2 = 1: preselect the first row when a word is being typed
__mrok_compute() {
  local force=${1:-0} autosel=${2:-1} t0=$EPOCHREALTIME
  __mrok_wordlen; local wl=$REPLY
  local cmdpos=0
  __mrok_cmdpos $wl && cmdpos=1

  if (( ! force && cmdpos && wl == 0 )); then __mrok_hide; return; fi
  if [[ $BUFFER == *$'\n'* ]]; then __mrok_hide; return; fi

  local word=''
  (( wl > 0 )) && word=${LBUFFER[-wl,-1]}

  local plugin=0
  if (( ! cmdpos )); then
    local -a before; before=( ${(z)LBUFFER} )
    (( wl > 0 )) && before[-1]=()
    __mrok_from_plugin "$word" "${before[@]}" && plugin=1
  fi
  (( plugin )) || zle __mrok-complete 2>/dev/null

  local -a c ii ss d
  local -A seen
  local i x desc
  # Keep the best tier that has any match: prefix > substring > fuzzy (the typed
  # characters in order, e.g. "chp" -> cherry-pick). Native completion is already
  # filtered by zsh's matcher-list, so tiers 2/3 only narrow plugin output.
  local lw=${(L)word#[\"\']} tier=0 fz='*' ch
  if [[ -n $lw ]]; then
    for ch in ${(s::)lw}; do fz+="${(b)ch}*"; done
    for (( i = 1; i <= $#__mrok_c; i++ )); do
      if [[ ${(L)__mrok_i[i]} == ${lw}* ]]; then tier=1; break
      elif (( plugin )) && [[ ${(L)__mrok_c[i]} == *${lw}* ]]; then tier=2
      elif (( plugin && tier != 2 )) && [[ ${(L)__mrok_c[i]} == $~fz ]]; then tier=3
      fi
    done
  fi
  for (( i = 1; i <= $#__mrok_c; i++ )); do
    x=${__mrok_c[i]}
    [[ -z $x ]] && continue
    desc=${__mrok_d[i]}
    if [[ $desc == *' -- '* ]]; then desc=${desc#* -- }; desc=${desc##[[:space:]]#}
    elif [[ ${desc%%[[:space:]]#} == ${x%/} ]]; then desc=''
    fi
    # Same suggestion from several groups: keep the first, borrow a description
    if (( ${+seen[${__mrok_i[i]}]} )); then
      [[ -n $desc && -z ${d[${seen[${__mrok_i[i]}]}]} ]] && d[${seen[${__mrok_i[i]}]}]=$desc
      continue
    fi
    case $tier in
      1) [[ ${(L)__mrok_i[i]} == ${lw}* ]] || continue ;;
      2) [[ ${(L)x} == *${lw}* ]] || continue ;;
      3) [[ ${(L)x} == $~fz ]] || continue ;;
      0) (( plugin )) && [[ -n $lw ]] && continue ;;
    esac
    # Command position: hide internal functions (_xxx, .xxx) and parameters
    if (( cmdpos )); then
      [[ $x == [_.]* && $word != [_.]* ]] && continue
      [[ ${__mrok_s[i]} == '=' ]] && continue
    fi
    seen[${__mrok_i[i]}]=$(( $#c + 1 ))
    c+=( "$x" ); ii+=( "${__mrok_i[i]}" ); ss+=( "${__mrok_s[i]}" ); d+=( "$desc" )
    (( $#c >= 300 )) && break
  done

  # Command position: exact match first, then shorter names first
  if (( cmdpos && $#c > 1 )); then
    local -a keyed c2 i2 s2 d2
    local exact
    for (( i = 1; i <= $#c; i++ )); do
      exact=1; [[ ${c[i]} == $word ]] && exact=0
      keyed+=( "${exact}$(( 1000 + ${#c[i]} ))${c[i]}"$'\0'"$i" )
    done
    for x in ${(o)keyed}; do
      i=${x##*$'\0'}
      c2+=( "${c[i]}" ); i2+=( "${ii[i]}" ); s2+=( "${ss[i]}" ); d2+=( "${d[i]}" )
    done
    c=( "${c2[@]}" ) ii=( "${i2[@]}" ) ss=( "${s2[@]}" ) d=( "${d2[@]}" )
  fi

  __mrok_c=( "${c[@]}" ) __mrok_i=( "${ii[@]}" ) __mrok_s=( "${ss[@]}" ) __mrok_d=( "${d[@]}" )
  __mrok_log "COMPUTE $(( (EPOCHREALTIME - t0) * 1000 ))ms plugin=$plugin buf=[$BUFFER] word=[$word] n=$#__mrok_c c=[${(j:|:)__mrok_c[1,40]}] i1=[${__mrok_i[1]}] s1=[${__mrok_s[1]}] d1=[${__mrok_d[1][1,60]}]"

  if (( $#__mrok_c == 0 )); then __mrok_hide; return; fi
  # A single suggestion equal to what's typed: no popup needed (except dirs: can go deeper)
  if (( $#__mrok_c == 1 )) && [[ ${__mrok_i[1]} == $word && ${__mrok_s[1]} != '/' ]]; then
    __mrok_hide; return
  fi
  __mrok_show
  if (( autosel && wl > 0 )); then __mrok_sel=1; else __mrok_sel=0; fi
}

# ---------------------------------------------------------------- render
__mrok_render() {
  region_highlight=( "${(@)region_highlight:#*memo=mrok*}" )
  if (( ! __mrok_visible || $#__mrok_c == 0 )); then
    POSTDISPLAY=''
    return
  fi
  local n=$#__mrok_c rows=$MROK_ROWS
  (( rows > n )) && rows=$n
  if (( __mrok_sel > 0 )); then
    (( __mrok_sel < __mrok_top )) && __mrok_top=$__mrok_sel
    (( __mrok_sel >= __mrok_top + rows )) && __mrok_top=$(( __mrok_sel - rows + 1 ))
  fi
  (( __mrok_top > n - rows + 1 )) && __mrok_top=$(( n - rows + 1 ))
  (( __mrok_top < 1 )) && __mrok_top=1

  local i namew=0 descw=0 last=$(( __mrok_top + rows - 1 ))
  for (( i = __mrok_top; i <= last; i++ )); do
    (( ${#__mrok_c[i]} > namew )) && namew=${#__mrok_c[i]}
    (( ${#__mrok_d[i]} > descw )) && descw=${#__mrok_d[i]}
  done
  (( namew > 40 )) && namew=40
  (( namew < 12 )) && namew=12
  (( descw > 60 )) && descw=60

  local foot=''
  if (( n > rows )); then
    foot="  $__mrok_sel/$n"
    (( __mrok_sel == 0 )) && foot="  $n matches · ↓ to select"
  fi
  # width = 2 (margin) + name + (2 + description) + 1
  local maxw=$(( COLUMNS - 2 ))
  local width=$(( 2 + namew + (descw ? 2 + descw : 0) + 1 ))
  (( width < ${#foot} + 1 )) && { namew=$(( namew + ${#foot} + 1 - width )); width=$(( ${#foot} + 1 )) }
  if (( width > maxw )); then
    descw=$(( descw - (width - maxw) ))
    (( descw < 0 )) && { namew=$(( namew + descw )); descw=0 }
    width=$maxw
  fi

  # Indent so the popup sits right under the word being typed
  __mrok_wordlen; local wl=$REPLY
  local indent=$(( __mrok_promptw + ${#LBUFFER} - wl - 2 ))
  (( indent + width > COLUMNS - 1 )) && indent=$(( COLUMNS - 1 - width ))
  (( indent < 0 )) && indent=0
  local pad=${(l:indent:: :)}

  local out='' line name desc start base=${#BUFFER} rowst descst descoff
  for (( i = __mrok_top; i <= last; i++ )); do
    name=${__mrok_c[i]}
    (( ${#name} > namew )) && name="${name[1,namew-1]}…"
    desc=${__mrok_d[i]}
    (( ${#desc} > descw )) && desc="${desc[1,descw-1]}…"
    if (( i == __mrok_sel )); then rowst=$__MROK_ST_SEL; descst=$__MROK_ST_SELDESC
    else rowst=$__MROK_ST_ROW; descst=$__MROK_ST_DESC; fi
    line="  ${(r:namew:: :)name}"
    descoff=${#line}
    (( descw )) && line+="  ${(r:descw:: :)desc}"
    line+=' '
    out+=$'\n'$pad
    start=$(( base + ${#out} ))
    out+=$line
    region_highlight+=( "$start $(( start + ${#line} )) $rowst memo=mrok" )
    (( descw && ${#desc} )) && region_highlight+=( "$(( start + descoff )) $(( start + ${#line} )) $descst memo=mrok" )
  done
  if [[ -n $foot ]]; then
    foot=${(r:width:: :)foot}
    out+=$'\n'$pad
    start=$(( base + ${#out} ))
    out+=$foot
    region_highlight+=( "$start $(( start + ${#foot} )) $__MROK_ST_FOOT memo=mrok" )
  fi
  POSTDISPLAY=$out
}

__mrok_clear_display() {
  POSTDISPLAY=''
  region_highlight=( "${(@)region_highlight:#*memo=mrok*}" )
}

# ---------------------------------------------------------------- widgets
__mrok_up() {
  (( $#__mrok_c )) || return
  (( __mrok_sel = __mrok_sel <= 1 ? $#__mrok_c : __mrok_sel - 1 ))
  __mrok_render
}
__mrok_down() {
  (( $#__mrok_c )) || return
  (( __mrok_sel = __mrok_sel >= $#__mrok_c ? 1 : __mrok_sel + 1 ))
  __mrok_render
}

__mrok_esc() {
  __mrok_hide
  __mrok_last="$BUFFER"$'\0'"$CURSOR"
  __mrok_render
}

__mrok_run() {
  __mrok_hide
  __mrok_clear_display
  zle -R
  zle accept-line
}

# Accept suggestion $1, then show suggestions for what comes next
__mrok_accept_idx() {
  local idx=$1
  local ins=${__mrok_i[idx]} suf=${__mrok_s[idx]}
  __mrok_wordlen; local wl=$REPLY
  __mrok_log "ACCEPT ins=[$ins] suf=[$suf]"
  if (( wl > 0 )); then LBUFFER="${LBUFFER[1,-wl-1]}${ins}${suf}"
  else LBUFFER+="${ins}${suf}"
  fi
  __mrok_busy=1
  __mrok_compute 0 0
  __mrok_busy=0
  __mrok_last="$BUFFER"$'\0'"$CURSOR"
  __mrok_render
}

__mrok_enter() {
  if (( ! __mrok_visible || __mrok_sel == 0 )); then __mrok_run; return; fi
  __mrok_wordlen; local wl=$REPLY
  local word=''
  (( wl > 0 )) && word=${LBUFFER[-wl,-1]}
  # Already typed exactly this (and it's not a directory): run it
  if [[ -n $word && ${__mrok_i[__mrok_sel]} == $word && ${__mrok_s[__mrok_sel]} != '/' ]]; then
    __mrok_run; return
  fi
  __mrok_accept_idx $__mrok_sel
}

__mrok_tab() {
  if (( __mrok_visible )); then
    __mrok_accept_idx $(( __mrok_sel ? __mrok_sel : 1 ))
    return
  fi
  __mrok_busy=1
  __mrok_compute 1 1
  __mrok_busy=0
  __mrok_last="$BUFFER"$'\0'"$CURSOR"
  if (( ! __mrok_visible )); then
    zle expand-or-complete
    return
  fi
  (( __mrok_sel == 0 )) && __mrok_sel=1
  __mrok_render
}

zle -N mrok-up __mrok_up
zle -N mrok-down __mrok_down
zle -N mrok-esc __mrok_esc
zle -N mrok-enter __mrok_enter
zle -N mrok-run __mrok_run
zle -N mrok-tab __mrok_tab

# ---------------------------------------------------------------- hooks
__mrok_pre_redraw() {
  (( __mrok_busy )) && return
  local state="$BUFFER"$'\0'"$CURSOR"
  if [[ $state != $__mrok_last ]]; then
    __mrok_last=$state
    case $LASTWIDGET in
      self-insert|backward-delete-char|vi-backward-delete-char|delete-char|delete-char-or-list|\
      backward-kill-word|backward-delete-word|kill-word|kill-line|backward-kill-line|magic-space|\
      undo|redo|mrok-*)
        __mrok_busy=1; __mrok_compute 0 1; __mrok_busy=0 ;;
      *)
        __mrok_hide ;;
    esac
  fi
  __mrok_render
}

__mrok_line_init() {
  __mrok_last="$BUFFER"$'\0'"$CURSOR"
  __mrok_pcache=() __mrok_pstat=()
  __mrok_hide
}

__mrok_line_finish() {
  __mrok_hide
  __mrok_clear_display
}

# Ctrl+C with the popup open: wipe it before zsh drops the line
if (( $+functions[TRAPINT] )) && [[ $functions[TRAPINT] != *__mrok* ]]; then
  functions[__mrok_orig_trapint]=$functions[TRAPINT]
fi
TRAPINT() {
  if (( __mrok_visible )); then
    __mrok_hide
    # POSTDISPLAY can't be changed from a trap: clear the screen below the cursor
    print -n -- $'\e[J' 2>/dev/null >/dev/tty
  fi
  if (( $+functions[__mrok_orig_trapint] )); then __mrok_orig_trapint "$@"; return; fi
  return $(( 128 + $1 ))
}

# Remember the original bindings, restored while the popup is hidden
() {
  local k b
  for k in $__MROK_KEYS; do
    b=$(bindkey -M main "$k" 2>/dev/null)
    __mrok_orig_keys[$k]=${${(z)b}[2]}
  done
}

__mrok_load_plugins

autoload -Uz add-zle-hook-widget
add-zle-hook-widget line-pre-redraw __mrok_pre_redraw
add-zle-hook-widget line-init __mrok_line_init
add-zle-hook-widget line-finish __mrok_line_finish
bindkey '^I' mrok-tab
