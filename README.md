# mrok

As-you-type suggestion popup for **zsh** and **bash**. Type, and a list shows up right
under the word you're typing. Pick with the arrow keys, press Enter, and the next
suggestions show up straight away: `cd` → sub-folders, `git` → `checkout` → branches,
`pnpm` → the scripts in your `package.json`.

```
~/proj $ git checkout fe
                      feature/login   add login form
                      feature/search  search by name
```

- Works inside any terminal: Terminal.app, iTerm2, WezTerm, Ghostty, VS Code, Linux terminals
- Pure shell script, nothing to compile, no account, no network calls
- Uses your shell's own completion (zsh compsys / bash-completion), plus plugins
- Plugins are a few lines of shell, and the same plugin works in zsh and bash

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/bravo680git/mrok/main/install.sh | sh
```

or with wget:

```sh
wget -qO- https://raw.githubusercontent.com/bravo680git/mrok/main/install.sh | sh
```

Then open a new terminal. The installer copies mrok to `~/.mrok` and adds one block to
`~/.zshrc` and/or `~/.bashrc`:

```sh
# >>> mrok >>>
[ -f "$HOME/.mrok/mrok.sh" ] && . "$HOME/.mrok/mrok.sh"
# <<< mrok <<<
```

Keep that block at the **end** of the file (after oh-my-zsh / bash-completion are loaded).

Requirements: zsh 5.3+, or bash 4.3+ (Linux). macOS ships bash 3.2, so on a Mac use zsh
(the default shell) or `brew install bash`.

From a clone: `git clone https://github.com/bravo680git/mrok && sh mrok/install.sh --local`

Only one shell: `... | sh -s -- --zsh` or `--bash`.

## Keys

| Key                                                                 | Action                                                |
| ------------------------------------------------------------------- | ----------------------------------------------------- |
| typing                                                              | popup appears / filters; the first row is preselected |
| `↑` `↓`                                                             | move the selection                                    |
| `Enter` / `Tab`                                                     | accept the selection, then show what comes next       |
| `Enter` with nothing selected, or when the word is already complete | run the command                                       |
| `Esc` (zsh) / `Ctrl-G` (bash)                                       | hide the popup                                        |
| `Tab` with the popup hidden                                         | open it                                               |

When the popup is hidden, the arrow keys, Enter and Tab behave exactly as before.

## Commands

```
mrok            help
mrok plugins    list commands that have a plugin
mrok update     update to the latest version
mrok uninstall  remove mrok and the block in your rc files
```

## Configuration

Set these before the mrok block in your rc file:

| Variable                      | Default       |                                 |
| ----------------------------- | ------------- | ------------------------------- |
| `MROK_ROWS`                   | `8`           | max rows in the popup           |
| `MROK_BG` / `MROK_FG`         | `236` / `252` | popup background / text         |
| `MROK_DESC_FG`                | `244`         | description text                |
| `MROK_SEL_BG` / `MROK_SEL_FG` | `88` / `231`  | selected row (burgundy)         |
| `MROK_SEL_DESC_FG`            | `224`         | description on the selected row |
| `MROK_FOOT_FG`                | `242`         | the "3/42" footer               |
| `MROK_DEBUG`                  |               | file to write a debug log to    |

Colors are numbers from the [256-color palette](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit).

## Built-in plugins

| Commands                  | Suggests                                                                                              |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| `npm` `pnpm` `yarn` `bun` | scripts from the nearest `package.json` (with the command they run), common commands                  |
| `git`                     | subcommands with descriptions, your git aliases, branches (with last commit), remotes, stash commands |
| `make`                    | Makefile targets; `target: ## text` becomes the description                                           |

Everything else comes from your shell's completion: folders for `cd`, files, options, etc.

## Writing a plugin

Put a file in `~/.config/mrok/plugins/` (any name ending in `.sh`). Example: suggest
`docker compose` services.

```sh
# ~/.config/mrok/plugins/compose.sh
mrok_register my_compose docker-compose

my_compose() {
  # "$@" = words typed before the current one ($1 is the command)
  # $MROK_CUR = the word being typed
  [ $# -eq 2 ] && [ "$2" = logs ] || return 1    # 1 = not mine, use normal completion
  docker-compose config --services 2>/dev/null | while read -r s; do
    printf '%s\t%s\n' "$s" "service"             # value<TAB>description
  done
  return 0                                       # 0 = use what I printed
}
```

The rules:

- `mrok_register <function> <command>...` attaches the function to one or more commands.
- The function receives the words **before** the one being typed: `pnpm run d` calls it
  with `pnpm run`, and `MROK_CUR=d`.
- Print one suggestion per line: `value` or `value<TAB>description`. Print everything,
  mrok does the filtering (prefix first, then substring, case-insensitive).
- A value ending with `/` or `=` is inserted without a trailing space.
- Return `0` to use your output (no output = no popup), `1` to fall back to the shell's
  completion.
- The output is cached while the user types the same word, so calling `git`, `node`,
  `docker` is fine.
- The plugin is sourced in both zsh and bash: stick to plain `sh`-style syntax
  (`[ ]`, `case`, `$#`, no arrays).

Helpers you can use: `mrok_find_up <file>` (nearest file walking up from `$PWD`),
`mrok_pkg_scripts`, `mrok_git_branches`. A plugin with the same command name as a built-in
one replaces it.

## How it works

- **zsh**: a zle widget runs after every keystroke, calls zsh's completion system with a
  wrapped `compadd` to collect matches (instead of showing zsh's menu), and draws the popup
  with `POSTDISPLAY` + `region_highlight`.
- **bash**: printable keys are bound to readline macros (insert the character, then call a
  `bind -x` hook). The popup is drawn with ANSI escape codes below the prompt. Candidates
  come from the command's `complete -F` function (bash-completion), `compgen`, and plugins.

## Limitations

- The popup is drawn with text, under the command line, not as a floating window.
- bash: emacs editing mode only; non-ASCII typing doesn't refresh the popup.
- After `Ctrl-C` a few blank lines can be left where the popup was.

## Uninstall

```sh
mrok uninstall
```

## License

MIT
