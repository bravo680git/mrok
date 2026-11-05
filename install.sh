#!/bin/sh
# mrok installer
#
#   curl -fsSL https://raw.githubusercontent.com/bravo680git/mrok/main/install.sh | sh
#   wget -qO-  https://raw.githubusercontent.com/bravo680git/mrok/main/install.sh | sh
#
# Options:
#   --zsh / --bash   only set up this shell (default: every shell found)
#   --update         download the latest version (keeps your rc files as they are)
#   --uninstall      remove mrok and the lines it added to your rc files
#   --local          install from the directory this script is in (a git clone)
#
# Environment:
#   MROK_HOME   install directory (default ~/.mrok)
#   MROK_REPO   GitHub repo (default bravo680git/mrok)
#   MROK_REF    branch or tag (default main)
#   MROK_URL    tarball URL (overrides MROK_REPO/MROK_REF)

set -eu

REPO=${MROK_REPO:-bravo680git/mrok}
REF=${MROK_REF:-main}
URL=${MROK_URL:-https://github.com/$REPO/archive/refs/heads/$REF.tar.gz}
DEST=${MROK_HOME:-$HOME/.mrok}
BEGIN='# >>> mrok >>>'
END='# <<< mrok <<<'

say() { printf '\033[1;35mmrok\033[0m %s\n' "$*"; }
die() { printf '\033[1;31mmrok\033[0m %s\n' "$*" >&2; exit 1; }

action=install
from_local=0
shells=''
for arg in "$@"; do
  case $arg in
    --zsh) shells="$shells zsh" ;;
    --bash) shells="$shells bash" ;;
    --update) action=update ;;
    --uninstall) action=uninstall ;;
    --local) from_local=1 ;;
    -h|--help) sed -n '2,18p' "$0" 2>/dev/null | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) die "unknown option: $arg" ;;
  esac
done

# ---------------------------------------------------------------- files
fetch() {  # url file
  if command -v curl >/dev/null 2>&1; then curl -fsSL "$1" -o "$2"
  elif command -v wget >/dev/null 2>&1; then wget -qO "$2" "$1"
  else die "need curl or wget"
  fi
}

copy_tree() {  # src_dir
  [ -f "$1/mrok.sh" ] && [ -f "$1/lib/mrok.zsh" ] || die "not a mrok directory: $1"
  rm -rf "$DEST.new"
  mkdir -p "$DEST.new"
  cp -R "$1/mrok.sh" "$1/install.sh" "$1/lib" "$1/plugins" "$DEST.new/"
  [ -d "$1/specs" ] && cp -R "$1/specs" "$DEST.new/"
  for f in README.md LICENSE; do
    [ -f "$1/$f" ] && cp "$1/$f" "$DEST.new/"
  done
  rm -rf "$DEST"
  mv "$DEST.new" "$DEST"
}

install_files() {
  if [ "$from_local" = 1 ]; then
    here=$(cd "$(dirname "$0")" && pwd)
    if [ "$here" = "$DEST" ]; then
      say "already installed at $DEST"
      return
    fi
    say "installing from $here"
    copy_tree "$here"
    return
  fi
  command -v tar >/dev/null 2>&1 || die "need tar"
  tmp=$(mktemp -d 2>/dev/null || mktemp -d -t mrok)
  trap 'rm -rf "$tmp"' EXIT
  say "downloading $URL"
  fetch "$URL" "$tmp/mrok.tar.gz" || die "download failed"
  tar -xzf "$tmp/mrok.tar.gz" -C "$tmp" || die "can't extract the archive"
  src=$(find "$tmp" -name mrok.sh -type f | head -1)
  [ -n "$src" ] || die "mrok.sh not found in the archive"
  copy_tree "$(dirname "$src")"
}

# ---------------------------------------------------------------- rc files
rc_lines() {
  if [ "$DEST" = "$HOME/.mrok" ]; then
    printf '%s\n' '[ -f "$HOME/.mrok/mrok.sh" ] && . "$HOME/.mrok/mrok.sh"'
  else
    printf 'export MROK_HOME="%s"\n' "$DEST"
    printf '%s\n' '[ -f "$MROK_HOME/mrok.sh" ] && . "$MROK_HOME/mrok.sh"'
  fi
}

add_block() {  # rc_file
  [ -f "$1" ] || : > "$1"
  if grep -qF "$BEGIN" "$1"; then
    say "$1 already loads mrok"
    return
  fi
  { printf '\n%s\n' "$BEGIN"; rc_lines; printf '%s\n' "$END"; } >> "$1"
  say "added mrok to $1"
}

remove_block() {  # rc_file
  [ -f "$1" ] || return 0
  grep -qF "$BEGIN" "$1" || return 0
  tmp_rc=$(mktemp 2>/dev/null || mktemp -t mrok)
  awk -v b="$BEGIN" -v e="$END" '$0 == b { skip = 1; next } $0 == e { skip = 0; next } !skip' "$1" > "$tmp_rc"
  cat "$tmp_rc" > "$1"   # write in place: keeps permissions and symlinks
  rm -f "$tmp_rc"
  say "removed mrok from $1"
}

bash_ok() {
  command -v bash >/dev/null 2>&1 || return 1
  bash -c '(( BASH_VERSINFO[0] > 4 || (BASH_VERSINFO[0] == 4 && BASH_VERSINFO[1] >= 3) ))' 2>/dev/null
}

pick_shells() {
  [ -n "$shells" ] && return
  if command -v zsh >/dev/null 2>&1; then
    if [ -f "$HOME/.zshrc" ] || [ "${SHELL##*/}" = zsh ]; then shells="$shells zsh"; fi
  fi
  if [ -f "$HOME/.bashrc" ] || [ "${SHELL##*/}" = bash ]; then
    if bash_ok; then shells="$shells bash"
    else say "skipping bash: mrok needs bash >= 4.3 (macOS ships 3.2; try: brew install bash)"
    fi
  fi
  [ -n "$shells" ] || die "no supported shell found (zsh, or bash >= 4.3)"
}

# ---------------------------------------------------------------- main
case $action in
  uninstall)
    remove_block "$HOME/.zshrc"
    remove_block "$HOME/.bashrc"
    rm -rf "$DEST"
    say "uninstalled. Open a new shell to finish."
    ;;
  update)
    install_files
    say "updated $DEST. Open a new shell to use it."
    ;;
  install)
    install_files
    pick_shells
    for sh in $shells; do
      case $sh in
        zsh) add_block "$HOME/.zshrc" ;;
        bash) add_block "$HOME/.bashrc" ;;
      esac
    done
    say "done! Open a new terminal (or run: exec \$SHELL) and start typing."
    say "your own plugins go in ~/.config/mrok/plugins/*.sh - run 'mrok' for help"
    ;;
esac
