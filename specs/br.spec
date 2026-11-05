@	
o	--dates|-d	Show the last modified date of files and directories	
o	--no-dates|-D	Don't show the last modified date	
o	--only-folders|-f	Only show folders	
o	--no-only-folders|-F	Show folders and files alike	
o	--show-root-fs	Show filesystem info on top	
o	--show-git-info|-g	Show git statuses on files and stats of repository	
o	--no-show-git-info|-G	Don't show git statuses on files nor stats	
o	--git-status	Only show files having an interesting git status, including hidden ones	
o	--hidden|-h	Show hidden files	
o	--no-hidden|-H	Don't show hidden files	
o	--show-gitignored|-i	Show files which should be ignored according to git	
o	--no-show-gitignored|-I	Don't show gitignored files	
o	--permissions|-p	Show permissions with owner and group	
o	--no-permissions|-P	Don't show permissions	
o	--sizes|-s	Show the sizes of files and directories. When this mode is on, children aren't shown so that the…	
o	--no-sizes|-S	Don't show sizes	
o	--sort-by-count	Sort by count (only show one level of the tree)	
o	--sort-by-date	Sort by date (only show one level of the tree)	
o	--sort-by-size	Sort by size (only show one level of the tree)	
o	--whale-spotting|-w	Sort by size, show ignored and hidden files	
o	--no-sort	Don't sort	
o	--trim-root|-t	Trim the root: remove elements which would exceed the screen size. This removes the scrollbar	
o	--no-trim-root|-T	Don't trim the root (still trim the deeper levels). A scrollbar may be used when there are too…	
o	--install	Install or reinstall the br shell function	
o	--get-root	Ask for the current root of the remote broot	
o	--color	Controls styling of the output (default: auto). If set to auto, all styling is removed when output…	V
o	--help	Prints a help page, with more or less the same content as this man page	
o	--version|-v	Prints the version of broot	
o	--outcmd	Where to write a command if broot produces one	v
o	--cmd|-c	Semicolon separated commands to execute on start of broot	v
o	--conf	Semicolon separated paths to specific config files	v
o	--height	Height to use if you don't want to fill the screen or for file export (by default the terminal…	v
o	--out|-o	Where to write the produced path, if any	v
o	--set-install-state	Set the installation state. This is mostly useful in installation scripts to override the normal…	v
o	--print-shell-function	Print to stdout the br function for the given shell. This can be used in your own installation…	v
o	--listen	Listen for commands	v
o	--send	Send commands to a remote broot then quits	v
a	1	0
=		--color
v	yes	
v	no	
v	auto	
=		--out
t	filepaths
=		--set-install-state
v	undefined	
v	refused	
v	installed	
=		--print-shell-function
v	bash	
v	fish	
v	zsh	
