@	
s	add	Add dependencies to a Scarb.toml manifest file
s	remove	Remove dependencies from a manifest file
s	build	Compile current project
s	cache	Manipulate packages cache
s	clean	Remove generated artifacts
s	commands	List installed commands
s	fetch	Fetch dependencies of packages from the network
s	fmt	Format project files
s	init	Create a new Scarb package in existing directory
s	metadata	Output the resolved dependencies of a package, the concrete used versions including overrides, in…
s	manifest-path	Print path to current Scarb.toml file to standard output
s	new	Create a new Scarb package at <PATH>
s	run	Run arbitrary package scripts
s	test	Runs test in the local project, if it has a Scarb.toml manifest. If project is a virtual…
o	-h|--help	Print help	
@	add
o	--dry-run	Do not actually write the manifest	
o	-p|--package	Packages to run this command on	v
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
o	--path	Filesystem path to local package to add	v
o	--git	Git repository location	v
o	--branch	Git branch to download the package from	v
o	--tag	Git tag to download the package from	v
o	--rev	Git reference to download the package from	v
a	1	0
=	add	-p
d
@	remove
o	--dry-run	Do not actually write the manifest	
o	-p|--package	Packages to run this command on	v
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-w|--workspace	Run for all packages in the workspace	
o	-h|--help	Print help	
a	1	1
=	remove	-p
d
@	build
o	-p|--package	Packages to run this command on	v
o	-w|--workspace	Run for all packages in the workspace	
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
=	build	-p
d
@	cache
s	clean	Remove all cached dependencies
s	path	Print the path of the cache directory
s	help	Print this message or the help of the given subcommand(s)
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
@	cache clean
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
@	cache path
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
@	cache help
@	clean
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
@	commands
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
@	fetch
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
@	fmt
o	-c|--check	Only check if files are formatted, do not write the changes to disk	
o	--no-color	Do not color output	
o	-v|--verbose	More output per occurrence	
o	-p|--package	Packages to run this command on	v
o	-q|--quiet	Less output per occurrence	
o	-w|--workspace	Run for all packages in the workspace	
o	-h|--help	Print help	
=	fmt	-p
d
@	init
o	--name	Set the resulting package name, defaults to the directory name	v
o	--no-vcs	Do not initialize a new Git repository	
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
@	metadata
o	--format-version	Format version	v
o	--no-deps	Output information only about the workspace members and don't fetch dependencies	
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
@	manifest-path
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
@	new
o	--name	Set the resulting package name, defaults to the directory name	v
o	--no-vcs	Do not initialize a new Git repository	
o	-v|--verbose	More output per occurrence	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
a	1	0
@	run
o	-p|--package	Packages to run this command on	v
o	-v|--verbose	More output per occurrence	
o	-w|--workspace	Run for all packages in the workspace	
o	-q|--quiet	Less output per occurrence	
o	-h|--help	Print help	
a	2	1
=	run	-p
d
@	test
o	--workspace|-w	Run for all packages in the workspace	
o	--filter|-f	Runs the test with a specific filter	v
o	--include-ignored	Run ignored and not ignored tests	
o	--ignored	Run only ignored tests	
o	--verbose|-v	More output per occurrence	
o	--quiet|-q	Less output per occurrence	
o	--help|-h	Print help	
o	--package|-p	Packages to run this command on	v
=	test	--package
d
