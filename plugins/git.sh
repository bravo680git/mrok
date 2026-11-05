# git: subcommands (+ your git aliases), branches, remotes.
mrok_register __mrok_p_git git

__mrok_p_git() {
  case $MROK_CUR in -*) return 1 ;; esac

  if [ $# -eq 1 ]; then
    printf '%s\t%s\n' \
      status 'show the working tree status' \
      add 'add file contents to the index' \
      commit 'record changes to the repository' \
      checkout 'switch branches or restore files' \
      switch 'switch branches' \
      branch 'list, create, or delete branches' \
      pull 'fetch and integrate with another branch' \
      push 'update remote refs' \
      fetch 'download objects and refs' \
      merge 'join two or more histories' \
      rebase 'reapply commits on top of another base' \
      log 'show commit logs' \
      diff 'show changes' \
      stash 'stash away changes' \
      restore 'restore working tree files' \
      reset 'reset HEAD to a state' \
      cherry-pick 'apply changes of existing commits' \
      tag 'create, list, or delete tags' \
      remote 'manage remotes' \
      clone 'clone a repository' \
      init 'create an empty repository' \
      show 'show objects' \
      blame 'show who changed each line' \
      revert 'revert existing commits' \
      worktree 'manage multiple working trees'
    git config --get-regexp '^alias\.' 2>/dev/null | sed 's/^alias\.\([^ ]*\) \(.*\)/\1	alias: \2/'
    return 0
  fi

  case $2 in
    checkout|switch|merge|rebase|cherry-pick|log|diff|reset|show)
      # only the first argument is a branch; after it let the shell complete (files...)
      [ $# -eq 2 ] || return 1
      mrok_git_branches; return 0 ;;
    branch)
      [ $# -eq 2 ] || return 1
      mrok_git_branches | grep -v '^[^	]*/'; return 0 ;;
    push|pull|fetch)
      if [ $# -eq 2 ]; then
        git remote -v 2>/dev/null | awk '$3 == "(fetch)" { print $1 "\t" $2 }'
      else
        mrok_git_branches | grep -v '^[^	]*/'
      fi
      return 0 ;;
    stash)
      if [ $# -eq 2 ]; then
        printf '%s\t%s\n' list 'list stashes' pop 'apply and drop a stash' \
          apply 'apply a stash' drop 'drop a stash' push 'stash changes' show 'show a stash'
        return 0
      fi ;;
    remote)
      if [ $# -eq 2 ]; then
        printf '%s\t%s\n' -v 'list remotes with URLs' add 'add a remote' \
          remove 'remove a remote' rename 'rename a remote' set-url 'change a remote URL'
        return 0
      fi ;;
  esac
  return 1
}
