@	
o	-n|--no	Do not perform any operations that modify the filesystem; merely show what would happen	
o	-d|--dir	Set the stow directory to 'DIR' instead of the current directory. This also has the effect of…	v
o	-t|--target	Set the target directory to 'DIR' instead of the parent of the stow directory	v
o	-v|--verbose	Send verbose output to standard error describing what Stow is doing. Verbosity levels are from 0…	v
o	-S|--stow	Stow the packages that follow this option into the target directory. This is the default action…	
o	-D|--delete	Unstow the packages that follow this option from the target directory rather than installing them	
o	-R|--restow	Restow packages (first unstow, then stow again). This is useful for pruning obsolete symlinks from…	
o	--adopt	This behaviour is specifically intended to alter the contents of your stow directory. If you do…	
o	--no-folding	Disable folding of newly stowed directories when stowing, and refolding of newly foldable…	
o	--ignore	Ignore files ending in this Perl regex	v
o	--defer	Don't stow files beginning with this Perl regex if the file is already stowed to another package	v
o	--override	Force stowing files beginning with this Perl regex if the file is already stowed to another package	v
o	--dotfiles	Enable special handling for 'dotfiles' (files or folders whose name begins with a period) in the…	
o	-V|--version	Show Stow version, and exit	
o	-h|--help	Show Stow command syntax, and exit	
=		-d
t	folders
=		-t
t	folders
=		-v
v	0	
v	1	
v	2	
v	3	
v	4	
v	5	
