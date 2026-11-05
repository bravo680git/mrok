# mrok: its own commands, plus spec names for `mrok spec add/rm`.
mrok_register __mrok_p_mrok mrok

__mrok_p_mrok() {
  case $MROK_CUR in -*) return 1 ;; esac
  if [ $# -eq 1 ]; then
    printf '%s\t%s\n' \
      spec 'manage command specs (from Fig)' \
      plugins 'list commands that have a plugin' \
      update 'update to the latest version' \
      uninstall 'remove mrok and its rc file block' \
      version 'print the version' \
      help 'show help'
    return 0
  fi
  [ "$2" = spec ] || [ "$2" = specs ] || return 0
  if [ $# -eq 2 ]; then
    printf '%s\t%s\n' \
      list 'installed specs' \
      available 'every spec you can add' \
      add 'download specs from GitHub' \
      rm 'remove specs (kept removed across updates)' \
      refresh 'drop specs of removed commands, fetch new ones'
    return 0
  fi
  local dir="$MROK_HOME/specs" f c
  case $3 in
    add)
      [ -f "$dir/index" ] || return 0
      while IFS='	' read -r c f; do
        [ -n "$c" ] && [ ! -f "$dir/$c.spec" ] && printf '%s\t%s\n' "$c" "$f"
      done < "$dir/index" ;;
    rm|remove)
      [ -f "$dir/index" ] || return 0
      while IFS='	' read -r c f; do
        [ -f "$dir/$c.spec" ] && printf '%s\t%s\n' "$c" "$f"
      done < "$dir/index" ;;
  esac
  return 0
}
