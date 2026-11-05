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

# ---------------------------------------------------------------- loading
__mrok_load_plugins() {
  local f dir
  for dir in "$MROK_HOME/plugins" "${XDG_CONFIG_HOME:-$HOME/.config}/mrok/plugins"; do
    [ -d "$dir" ] || continue
    for f in "$dir"/*.sh; do
      [ -f "$f" ] && . "$f"
    done
  done
}

# ---------------------------------------------------------------- `mrok` command
mrok() {
  case ${1-help} in
    update)
      sh "$MROK_HOME/install.sh" --update && echo "mrok: updated, open a new shell to use it" ;;
    uninstall)
      sh "$MROK_HOME/install.sh" --uninstall ;;
    plugins)
      __mrok_list_plugins | sort ;;
    version|-v|--version)
      echo "mrok $MROK_VERSION" ;;
    *)
      cat <<'EOF'
mrok: as-you-type suggestion popup

  mrok plugins     list commands that have a suggestion plugin
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
