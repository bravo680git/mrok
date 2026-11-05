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
Sleep 5s
Show

# git checkout -> branches with their last commit
Sleep 500ms
Type "git checkout " Sleep 400ms
Type "fe" Sleep 1.5s
Enter Sleep 600ms
Enter Sleep 600ms

# docker log -> log containers
Type "docker lgs" Sleep 1s
Enter Sleep 1s
Down Sleep 400ms
Down Sleep 400ms
Down Sleep 400ms
Enter Sleep 500ms
Enter Sleep 2s

# cd -> folders
Type "cd " Sleep 1.5s
Down Sleep 400ms
Enter Sleep 1.5s
