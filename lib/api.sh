# mrok shared code: plugin API, helpers for plugins, and the `mrok` command.
# Sourced by both lib/mrok.zsh and lib/mrok.bash, so keep it bash/zsh compatible.

MROK_VERSION=0.1.0

typeset -gA __mrok_plugins 2>/dev/null

# ---------------------------------------------------------------- plugin API
#
#   mrok_register <function> <command>...
#
# When the user is typing an argument of <command>, mrok calls
#
#   <function> <word1> <word2> ...      (all words BEFORE the current one, $1 = command)
#
# with $MROK_CUR set to the word being typed. The function prints one suggestion per
# line:  value<TAB>description  (description optional). mrok filters by $MROK_CUR itself,
# so plugins can print everything. A value ending in "/" or "=" is inserted without the
# trailing space, so the next suggestions show up right after it.
#
# Return status:
#   0  -> use the printed suggestions (print nothing = no suggestions)
#   1  -> let the shell's own completion handle this position
#
# Output is cached while the user types the same word, so it's fine to call git/node.
mrok_register() {
  local fn=$1 cmd
  shift
  for cmd in "$@"; do
    __mrok_plugins[$cmd]=$fn
  done
}

# Print the path of the nearest <file>, searching from $PWD upwards.
mrok_find_up() {
  local d=$PWD
  while :; do
    if [ -e "$d/$1" ]; then
      printf '%s\n' "$d/$1"
      return 0
    fi
    [ "$d" = / ] && return 1
    d=$(dirname "$d")
  done
}

# Print "name<TAB>command" for every script in the nearest package.json.
mrok_pkg_scripts() {
  local pkg
  pkg=$(mrok_find_up package.json) || return 0
  if command -v node >/dev/null 2>&1; then
    node -e '
      try {
        const s = JSON.parse(require("fs").readFileSync(process.argv[1], "utf8")).scripts || {};
        for (const [k, v] of Object.entries(s)) console.log(k + "\t" + String(v).replace(/\s+/g, " "));
      } catch {}' "$pkg" 2>/dev/null
  elif command -v python3 >/dev/null 2>&1; then
    python3 -c '
import json, sys
try:
    for k, v in (json.load(open(sys.argv[1])).get("scripts") or {}).items():
        print(k + "\t" + " ".join(str(v).split()))
except Exception:
    pass' "$pkg" 2>/dev/null
  else
    # crude fallback: "name": "command" lines inside the "scripts" block
    sed -n '/"scripts"[[:space:]]*:/,/}/s/^[[:space:]]*"\([^"]*\)"[[:space:]]*:[[:space:]]*"\(.*\)",\{0,1\}[[:space:]]*$/\1	\2/p' "$pkg"
  fi
}

# Print "branch<TAB>last commit subject": local branches first, then remote ones.
mrok_git_branches() {
  git rev-parse --git-dir >/dev/null 2>&1 || return 0
  git for-each-ref --sort=-committerdate --count=200 \
    --format='%(refname:short)	%(subject)' refs/heads 2>/dev/null
  git for-each-ref --sort=-committerdate --count=200 \
    --format='%(refname:short)	%(subject)' refs/remotes 2>/dev/null | grep -v '/HEAD	'
}

# ---------------------------------------------------------------- Fig specs
# specs/<cmd>.spec are converted from github.com/withfig/autocomplete (MIT, see
# specs/LICENSE). __mrok_spec is the plugin for every command that has one.

__mrok_spec_off="${XDG_CONFIG_HOME:-$HOME/.config}/mrok/specs.off"

__mrok_spec() {
  local f="$MROK_HOME/specs/$1.spec" out line nat=0 any=0 IFS
  [ -f "$f" ] || return 1
  shift
  IFS=$(printf '\037')
  out=$(MROK_W="$*" MROK_CUR="$MROK_CUR" awk -f "$MROK_HOME/lib/spec.awk" "$f" 2>/dev/null)
  IFS=
  while read -r line; do
    case $line in
      '') ;;
      '!native') nat=1 ;;
      '!gen	'*) any=1; (unset IFS; eval "${line#*	}") 2>/dev/null | sed '/^[[:space:]]*$/d' ;;
      *) any=1; printf '%s\n' "$line" ;;
    esac
  done <<EOF
$out
EOF
  [ "$any" = 1 ] || [ "$nat" = 0 ]
}

# Seconds since the epoch, without starting a process.
__mrok_now() {
  if [ -n "${ZSH_VERSION-}" ]; then
    zmodload -F zsh/datetime p:EPOCHSECONDS 2>/dev/null
    REPLY=$EPOCHSECONDS
  else
    printf -v REPLY '%(%s)T' -1
  fi
}

# Download specs/<file> from GitHub (a spec, or the index).
__mrok_spec_get() {
  local dir="$MROK_HOME/specs" f
  local url="https://raw.githubusercontent.com/${MROK_REPO:-bravo680git/mrok}/${MROK_REF:-main}/specs/$1"
  f="$dir/$1.tmp"
  mkdir -p "$dir"
  if command -v curl >/dev/null 2>&1; then curl -fsSL "$url" -o "$f"
  elif command -v wget >/dev/null 2>&1; then wget -qO "$f" "$url"
  else return 1
  fi && mv "$f" "$dir/$1" && return 0
  rm -f "$f"
  return 1
}
__mrok_spec_fetch() { __mrok_spec_get "$1.spec"; }

# Download several specs: one curl run, parallel when curl supports it.
__mrok_spec_fetch_many() {
  local dir="$MROK_HOME/specs" c
  local base="https://raw.githubusercontent.com/${MROK_REPO:-bravo680git/mrok}/${MROK_REF:-main}/specs"
  local n=$# par=''
  [ -n "${ZSH_VERSION-}" ] && setopt localoptions nullglob shwordsplit
  if command -v curl >/dev/null 2>&1; then
    for c in "$@"; do set -- "$@" -o "$dir/$c.spec.tmp" "$base/$c.spec"; done
    shift "$n"
    curl -Z -V >/dev/null 2>&1 && par='-Z --parallel-max 8'
    curl -fsSL $par "$@" 2>/dev/null
    for c in "$dir"/*.spec.tmp; do
      [ -s "$c" ] && mv "$c" "${c%.tmp}" || rm -f "$c"
    done
  else
    for c in "$@"; do __mrok_spec_fetch "$c"; done
  fi
  return 0
}

# Make sure specs/index exists (an install from an old installer has no specs/ at all).
__mrok_spec_index() {
  [ -f "$MROK_HOME/specs/index" ] && return 0
  __mrok_spec_get index && return 0
  echo "mrok: can't download the spec index" >&2
  return 1
}

# Keep the specs in line with what's installed: delete the ones of commands that are gone
# (or that the user removed with `mrok spec rm`), download the ones of new commands.
# $1 = 1: print what happened.
__mrok_spec_refresh() {
  local dir="$MROK_HOME/specs" f c d off='' nrm=0 nadd=0
  [ -n "${ZSH_VERSION-}" ] && setopt localoptions nullglob shwordsplit
  if [ "${1-0}" = 1 ]; then __mrok_spec_index || return 1
  else [ -d "$dir" ] || return 0
  fi
  __mrok_now; printf '%s\n' "$REPLY" > "$dir/.refreshed"
  [ -f "$__mrok_spec_off" ] && off="
$(cat "$__mrok_spec_off")
"
  for f in "$dir"/*.spec; do
    [ -f "$f" ] || continue
    c=${f##*/}; c=${c%.spec}
    case $off in *"
$c
"*) rm -f "$f"; nrm=$((nrm + 1)); continue ;; esac
    command -v "$c" >/dev/null 2>&1 || { rm -f "$f"; nrm=$((nrm + 1)); }
  done
  if [ -f "$dir/index" ]; then
    local new=''
    while IFS='	' read -r c d; do
      [ -n "$c" ] && [ ! -f "$dir/$c.spec" ] || continue
      case $off in *"
$c
"*) continue ;; esac
      command -v "$c" >/dev/null 2>&1 && new="$new $c"
    done < "$dir/index"
    [ -n "$new" ] && __mrok_spec_fetch_many $new
    for c in $new; do
      if [ -f "$dir/$c.spec" ]; then
        nadd=$((nadd + 1)); [ "${1-0}" = 1 ] && echo "mrok: added $c"
      elif [ "${1-0}" = 1 ]; then
        echo "mrok: download failed: $c" >&2
      fi
    done
  fi
  [ "${1-0}" = 1 ] && echo "mrok: removed $nrm, added $nadd specs"
  return 0
}

# At shell start: refresh in the background every MROK_SPEC_REFRESH_DAYS days (default 3).
__mrok_spec_auto_refresh() {
  local dir="$MROK_HOME/specs" last=0
  [ -d "$dir" ] && [ ! -e "$MROK_HOME/.git" ] || return 0
  [ -f "$dir/.refreshed" ] && read -r last < "$dir/.refreshed"
  __mrok_now
  [ $((REPLY - ${last:-0})) -ge $(( ${MROK_SPEC_REFRESH_DAYS:-3} * 86400 )) ] || return 0
  ( __mrok_spec_refresh >/dev/null 2>&1 & )
}

__mrok_load_specs() {
  local f c
  [ -n "${ZSH_VERSION-}" ] && setopt localoptions nullglob
  [ -d "$MROK_HOME/specs" ] || return 0
  __mrok_spec_auto_refresh
  for f in "$MROK_HOME/specs"/*.spec; do
    [ -f "$f" ] || continue
    c=${f##*/}; c=${c%.spec}
    __mrok_plugins[$c]=__mrok_spec
  done
}

__mrok_spec_cmd() {
  local dir="$MROK_HOME/specs" c f n
  [ -n "${ZSH_VERSION-}" ] && setopt localoptions nullglob
  case ${1-} in
    add)
      shift
      [ $# -gt 0 ] || { echo "usage: mrok spec add <command>..." >&2; return 2; }
      command -v curl >/dev/null 2>&1 || command -v wget >/dev/null 2>&1 || { echo "mrok: need curl or wget" >&2; return 1; }
      __mrok_spec_index || return 1
      for c in "$@"; do
        if ! cut -f1 "$dir/index" | grep -qxF "$c"; then
          echo "mrok: no spec for '$c' (see: mrok spec available)" >&2; continue
        fi
        __mrok_spec_fetch "$c" || { echo "mrok: download failed: $c" >&2; continue; }
        [ -f "$__mrok_spec_off" ] && { grep -vxF "$c" "$__mrok_spec_off" > "$__mrok_spec_off.tmp"; mv "$__mrok_spec_off.tmp" "$__mrok_spec_off"; }
        [ -n "${__mrok_plugins[$c]-}" ] || __mrok_plugins[$c]=__mrok_spec
        echo "mrok: added $c"
      done ;;
    rm|remove)
      shift
      [ $# -gt 0 ] || { echo "usage: mrok spec rm <command>..." >&2; return 2; }
      mkdir -p "${__mrok_spec_off%/*}"
      for c in "$@"; do
        rm -f "$dir/$c.spec"
        grep -qxF "$c" "$__mrok_spec_off" 2>/dev/null || printf '%s\n' "$c" >> "$__mrok_spec_off"
        [ "${__mrok_plugins[$c]-}" = __mrok_spec ] && unset "__mrok_plugins[$c]"
        echo "mrok: removed $c"
      done ;;
    list|'')
      n=0
      for f in "$dir"/*.spec; do
        [ -f "$f" ] || continue
        c=${f##*/}; echo "${c%.spec}"; n=$((n + 1))
      done
      [ "$n" -gt 0 ] || echo "no specs installed (mrok spec available / mrok spec add <command>)" ;;
    available)
      __mrok_spec_index || return 1
      if command -v column >/dev/null 2>&1; then cut -f1 "$dir/index" | column
      else cut -f1 "$dir/index"
      fi ;;
    refresh)
      __mrok_spec_refresh 1
      __mrok_load_specs ;;
    *)
      echo "usage: mrok spec [list|available|add <cmd>...|rm <cmd>...|refresh]" >&2; return 2 ;;
  esac
}

# ---------------------------------------------------------------- loading
__mrok_load_plugins() {
  local f dir
  __mrok_load_specs
  for dir in "$MROK_HOME/plugins" "${XDG_CONFIG_HOME:-$HOME/.config}/mrok/plugins"; do
    [ -d "$dir" ] || continue
    for f in "$dir"/*.sh; do
      [ -f "$f" ] && . "$f"
    done
  done
}

# Run the latest installer, not the installed one: a new version may install new files.
__mrok_self_update() {
  local tmp url="https://raw.githubusercontent.com/${MROK_REPO:-bravo680git/mrok}/${MROK_REF:-main}/install.sh"
  tmp=$(mktemp 2>/dev/null || mktemp -t mrok) || return 1
  if { command -v curl >/dev/null 2>&1 && curl -fsSL "$url" -o "$tmp"; } ||
     { command -v wget >/dev/null 2>&1 && wget -qO "$tmp" "$url"; }; then
    sh "$tmp" --update
  else
    sh "$MROK_HOME/install.sh" --update
  fi
  local rc=$?
  rm -f "$tmp"
  return $rc
}

# ---------------------------------------------------------------- `mrok` command
mrok() {
  case ${1-help} in
    update)
      __mrok_self_update && echo "mrok: updated, open a new shell to use it" ;;
    uninstall)
      sh "$MROK_HOME/install.sh" --uninstall ;;
    plugins)
      __mrok_list_plugins | grep -v '	__mrok_spec$' | sort ;;
    spec|specs)
      shift; __mrok_spec_cmd "$@" ;;
    version|-v|--version)
      echo "mrok $MROK_VERSION" ;;
    *)
      cat <<'EOF'
mrok: as-you-type suggestion popup

  mrok plugins     list commands that have a suggestion plugin
  mrok spec        list the commands with a Fig spec (also: available, add, rm, refresh)
  mrok update      update to the latest version
  mrok uninstall   remove mrok and its line in your shell rc file
  mrok version     print the version

Keys:  type -> popup,  Up/Down select,  Enter/Tab accept,
       Enter with nothing selected runs the command,  Esc (or Ctrl-G in bash) hides.
Write your own plugins in ~/.config/mrok/plugins/*.sh (see README).
EOF
      ;;
  esac
}
