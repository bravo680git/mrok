# mrok: suggestions from a converted Fig spec (see tools/fig/convert.mjs for the format).
#
#   MROK_W=<words after the command, joined by \037>  MROK_CUR=<word being typed>  awk -f spec.awk <cmd>.spec
#
# Prints "value<TAB>description" lines, plus control lines:
#   !native          let the shell complete this position (files, ...)
#   !gen<TAB>cmd     run cmd, one suggestion per output line
# With MROK_WHERE=1 it prints one line instead: <subcommand path><TAB><argument index,
# 0 = an option's value><TAB><that option>
# POSIX awk only (macOS awk, mawk, gawk).

# Only blocks whose path is made of typed words are kept (big specs stay fast). Parents
# come before their children in the file, so a typed alias can add its canonical name.
BEGIN {
  FS = "\t"; key = ""
  nw = split(ENVIRON["MROK_W"], w, "\037")
  for (i = 1; i <= nw; i++) typed[w[i]] = 1
}
function relevant(p,    n, i, pw) {
  n = split(p, pw, " ")
  for (i = 1; i <= n; i++) if (!(pw[i] in typed)) return 0
  return 1
}
$1 == "@" { key = relevant($2) ? "N" SUBSEP $2 : ""; next }
$1 == "=" { key = relevant($2) ? "O" SUBSEP $2 SUBSEP $3 : ""; next }
$1 == "#" { key = relevant($2) ? "P" SUBSEP $2 SUBSEP $3 : ""; next }
key == "" { next }
$1 == "s" && index($2, "|") {
  na = split($2, al, "|")
  for (i = 2; i <= na; i++) if (al[i] in typed) typed[al[1]] = 1
}
{ blk[key] = blk[key] $0 "\n" }

# Load subcommands/options/args of node path p into sub[], opt*[], nargs[].
function load(p,    n, i, ln, f, k, nm, j) {
  if (p in loaded) return
  loaded[p] = 1
  n = split(blk["N" SUBSEP p], ln, "\n")
  for (i = 1; i <= n; i++) {
    split(ln[i], f, "\t")
    if (f[1] == "s") {
      k = split(f[2], nm, "|")
      for (j = 1; j <= k; j++) sub_[p SUBSEP nm[j]] = nm[1]
      subs[p] = subs[p] nm[1] "\t" f[3] "\n"
    } else if (f[1] == "o") {
      k = split(f[2], nm, "|")
      for (j = 1; j <= k; j++) { oflag[p SUBSEP nm[j]] = f[4]; ocanon[p SUBSEP nm[j]] = nm[1] }
      opts[p] = opts[p] ln[i] "\n"
    } else if (f[1] == "a") {
      nargs[p] = f[2] + 0; nvar[p] = f[3] + 0
    }
  }
}

function parent(p) { return sub(/ ?[^ ]*$/, "", p) ? p : "" }

# Find option name for node p (or an ancestor's persistent one). Sets fnode, fcanon.
function findopt(p, name,    q, first) {
  q = p; first = 1
  while (1) {
    load(q)
    if ((q SUBSEP name) in oflag && (first || oflag[q SUBSEP name] ~ /p/)) {
      fnode = q; fcanon = ocanon[q SUBSEP name]; return oflag[q SUBSEP name]
    }
    if (q == "") return ""
    q = parent(q); first = 0
  }
}

# Print the values of a slot with prefix pre. Returns 1 if it asked for native completion.
function slot(k, pre,    n, i, ln, f, nat) {
  if (!(k in blk)) return 0
  n = split(blk[k], ln, "\n")
  for (i = 1; i <= n; i++) {
    split(ln[i], f, "\t")
    if (f[1] == "v") print pre f[2] "\t" f[3]
    else if (f[1] == "g") print "!gen\t" f[2]
    else if (f[1] == "t" || f[1] == "d") nat = 1
  }
  return nat
}

# Options of p and persistent ones of its ancestors.
function listopts(p,    q, first, n, i, ln, f, k, nm, j, any) {
  q = p; first = 1
  while (1) {
    load(q)
    n = split(opts[q], ln, "\n")
    for (i = 1; i <= n; i++) {
      split(ln[i], f, "\t")
      if (!first && f[4] !~ /p/) continue
      k = split(f[2], nm, "|")
      for (j = 1; j <= k; j++) {
        if (nm[j] in seenopt) continue
        seenopt[nm[j]] = 1; any = 1
        print nm[j] (f[4] ~ /=/ ? "=" : "") "\t" f[3]
      }
    }
    if (q == "") return any
    q = parent(q); first = 0
  }
}

END {
  cur = ENVIRON["MROK_CUR"]
  node = ""; pos = 0; pend = ""; ddash = 0
  load(node)
  for (i = 1; i <= nw; i++) {
    x = w[i]
    if (x == "") continue
    if (pend != "") { pend = ""; continue }
    if (x == "--") { ddash = 1; continue }
    if (!ddash && x ~ /^-./) {
      eq = index(x, "=")
      fl = findopt(node, eq ? substr(x, 1, eq - 1) : x)
      if (fl ~ /v/ && !eq && fl !~ /=/) { pend = "O" SUBSEP fnode SUBSEP fcanon; pendopt = fcanon }
      continue
    }
    if (pos == 0 && (node SUBSEP x) in sub_) {
      node = (node == "" ? "" : node " ") sub_[node SUBSEP x]
      load(node)
      continue
    }
    pos++
  }

  # MROK_WHERE=1: only say where the cursor is, for plugins (see __mrok_spec_where)
  if (ENVIRON["MROK_WHERE"] != "") {
    print node "\t" (pend != "" ? 0 : pos + 1) "\t" (pend != "" ? pendopt : "")
    exit
  }

  # Value of an option given as the previous word
  if (pend != "") {
    if (slot(pend, "") || !(pend in blk)) print "!native"
    exit
  }
  # --option=value
  if (!ddash && cur ~ /^-.*=/) {
    eq = index(cur, "=")
    fl = findopt(node, substr(cur, 1, eq - 1))
    if (fl ~ /[vV]/) { if (slot("O" SUBSEP fnode SUBSEP fcanon, substr(cur, 1, eq))) print "!native" }
    else print "!native"
    exit
  }
  if (!ddash && cur ~ /^-/) {
    if (!listopts(node)) print "!native"
    exit
  }

  # Subcommands + values of the next positional argument
  any = 0
  if (pos == 0 && subs[node] != "") { printf "%s", subs[node]; any = 1 }
  a = pos + 1
  if (a > nargs[node] && nvar[node]) a = nargs[node]
  if (a <= nargs[node]) {
    k = "P" SUBSEP node SUBSEP a
    if (slot(k, "")) { if (!any) print "!native" }
    else if (!(k in blk) && !any) print "!native"
    exit
  }
  if (!any && cur == "" && !listopts(node)) print "!native"
  else if (!any && cur != "") print "!native"
}
