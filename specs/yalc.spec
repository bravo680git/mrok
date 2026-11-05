@	
s	publish	Copy all the files that should be published in remote NPM registry
s	push	Publish your package to the store and propagate all changes to existing yalc package installations
s	add	Copy the current version from the store to your project
s	link	Alterative to 'add', instead using local '.yalc' as symlink source
s	update	Update package(s)
s	remove	Remove package info from 'package.json' & 'yalc.lock'
s	installations	
s	dir	Show yalc system directory
s	check	Check 'package.json' for yalc packages
s	restore	Restore retreated packages
s	retreat	Remove packages from project, but leave in lock file (to be restored later)
o	--help	Show help for yalc	
o	--no-colors	Disable colors	
o	--quiet	Fully disable output (except errors)	
@	publish
o	--push	Publish package to the store and propagate all changes to existing yalc package installations	
o	--no-scripts	Publish without running scripts	
o	--no-sig	Disable adding hash signature of all files when copying package content	
o	--content	Show included files in the published package	
o	--no-workspace-resolve	Do not resolve 'workspace:' protocol in dependencies	
o	--private	Force publishing of private package	
@	push
@	add
o	--link	Add a 'link:' dependency instead of 'file:'	
o	--dev	Add yalc package to dev dependencies	
o	--pure	Do not touch 'package.json' or 'node_modules'	
o	--workspace|-W	Add dependency with 'workspace:' protocol	
a	1	0
#	add	1
d
@	link
@	update
o	--update|--upgrade|--up	Run package manager's update command for packages	
a	1	0
#	update	1
d
@	remove
o	--all	Remove all packages from project	
a	1	0
#	remove	1
d
@	installations
s	clean	Unpublish a package published with yalc publish
s	show	Show all packages to which chosen package has been added
@	installations clean
a	1	0
#	installations clean	1
d
@	installations show
a	1	0
#	installations show	1
d
@	dir
@	check
@	restore
@	retreat
