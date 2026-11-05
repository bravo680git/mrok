# mrok: as-you-type suggestion popup for zsh and bash.
# Source this file from ~/.zshrc or ~/.bashrc (install.sh does it for you).

if [ -z "${MROK_HOME-}" ]; then
  MROK_HOME="$HOME/.mrok"
fi

if [ -n "${ZSH_VERSION-}" ]; then
  . "$MROK_HOME/lib/mrok.zsh"
elif [ -n "${BASH_VERSION-}" ]; then
  . "$MROK_HOME/lib/mrok.bash"
fi
