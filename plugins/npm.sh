# npm / pnpm / yarn / bun: package.json scripts + common commands.
mrok_register __mrok_p_pkg npm pnpm yarn bun

__mrok_p_pkg() {
  # Typing an option -> let the shell's own completion handle it
  case $MROK_CUR in -*) return 1 ;; esac

  if [ $# -eq 1 ]; then
    # pnpm / yarn / bun can run a script directly: `pnpm dev`
    [ "$1" != npm ] && mrok_pkg_scripts
    __mrok_p_pkg_commands "$1"
    return 0
  fi
  if [ $# -eq 2 ]; then
    case $2 in
      run|run-script) mrok_pkg_scripts; return 0 ;;
    esac
  fi
  # after a script name / most commands: nothing useful to suggest
  case $2 in
    add|install|i|remove|rm|uninstall|un|update|up|upgrade|link|exec|x|dlx|create|init) return 1 ;;
  esac
  return 0
}

__mrok_p_pkg_commands() {
  case $1 in
    npm)
      printf '%s\t%s\n' \
        run 'run a package script' \
        install 'install dependencies' \
        ci 'clean install from the lockfile' \
        uninstall 'remove a dependency' \
        update 'update dependencies' \
        test 'run the test script' \
        start 'run the start script' \
        exec 'run a command from a package' \
        init 'create a package.json' \
        outdated 'list outdated dependencies' \
        ls 'list installed packages' \
        publish 'publish the package' \
        version 'bump the package version' \
        audit 'check for vulnerabilities' ;;
    pnpm)
      printf '%s\t%s\n' \
        install 'install dependencies' \
        add 'add a dependency' \
        remove 'remove a dependency' \
        update 'update dependencies' \
        run 'run a package script' \
        exec 'run a command in the project' \
        dlx 'run a package without installing it' \
        test 'run the test script' \
        outdated 'list outdated dependencies' \
        list 'list installed packages' \
        why 'show why a package is installed' \
        store 'manage the package store' \
        publish 'publish the package' ;;
    yarn)
      printf '%s\t%s\n' \
        install 'install dependencies' \
        add 'add a dependency' \
        remove 'remove a dependency' \
        upgrade 'upgrade dependencies' \
        run 'run a package script' \
        dlx 'run a package without installing it' \
        why 'show why a package is installed' \
        info 'show package information' ;;
    bun)
      printf '%s\t%s\n' \
        install 'install dependencies' \
        add 'add a dependency' \
        remove 'remove a dependency' \
        update 'update dependencies' \
        run 'run a script or file' \
        x 'run a package without installing it' \
        test 'run tests' \
        build 'bundle files' ;;
  esac
}
