# Records demo/demo.gif:  brew install vhs && vhs demo/demo.tape
# Run it from a git repo with a few branches and a package.json for the best result,
# with mrok installed and loaded from ~/.zshrc.

Output demo/demo.gif

Set Shell zsh
Set FontSize 18
Set Width 1100
Set Height 520
Set Padding 20
Set TypingSpeed 90ms
Set Theme "Catppuccin Mocha"

# vhs starts zsh with --no-rcs: load your rc (and with it mrok) off camera
Hide
Type "source ~/.zshrc && clear" Enter
Sleep 2s
Show

# fuzzy: chp -> cherry-pick, then branches
Type "git chp" Sleep 1.2s
Enter Sleep 1.2s
Down Sleep 400ms
Down Sleep 1s
Ctrl+C Sleep 600ms

# git checkout -> branches with their last commit
Type "git checkout " Sleep 1.5s
Type "fe" Sleep 1.5s
Ctrl+C Sleep 600ms

# docker exec -> running containers
Type "docker ex" Sleep 1s
Enter Sleep 1.5s
Ctrl+C Sleep 600ms

# a Fig spec: go mod -> subcommands with descriptions
Type "go mod " Sleep 1.5s
Type "t" Sleep 1.2s
Ctrl+C Sleep 600ms

# cd -> folders
Type "cd " Sleep 1.5s
Down Sleep 400ms
Enter Sleep 1.5s
Ctrl+C Sleep 1s
