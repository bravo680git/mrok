# make: targets from the Makefile ("target: ## description" comments become descriptions).
mrok_register __mrok_p_make make

__mrok_p_make() {
  case $MROK_CUR in -*) return 1 ;; esac
  local f
  for f in GNUmakefile makefile Makefile; do
    [ -f "$f" ] && break
  done
  [ -f "$f" ] || return 0
  sed -n 's/^\([a-zA-Z0-9][a-zA-Z0-9_.\/-]*\):[^=]*$/&/p' "$f" |
    sed 's/^\([^:]*\):[^#]*\(##[[:space:]]*\(.*\)\)\{0,1\}$/\1	\3/' |
    awk -F '\t' '!seen[$1]++'
  return 0
}
