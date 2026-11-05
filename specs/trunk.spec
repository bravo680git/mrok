@	
s	init	Setup trunk in this repo
s	check	Universal code checker
s	fmt	Universal code formatter
s	upgrade	Upgrade trunk to the latest release
s	git-hooks	Git hooks
s	cache	Cache management
s	print-config	Print the resolved trunk config
s	daemon	Daemon management
o	-h|--help	Usage information	p
o	--version	The version	p
o	-m|--monitor	Enable the trunk daemon to monitor file changes in your repo	vp
o	--ci	Run in continuous integration mode	p
o	-o|--output	Output format	vp
o	--no-progress	Don't show progress updates	p
o	--ci-progress	Show updates every 30 seconds without clearing terminal screen (implicit with --ci)	p
o	--action_timeout	How long actions (downloads, lint runs, etc.) have to time out, with units (s, ms, etc)	vp
o	-v|--verbose	Output details about what's happening under the hood	p
=		-m
v	true	
v	false	
=		-o
v	text	
v	json	
@	init
o	--lock	Add sha256s to trunk.yaml for additional verification	
o	--check-sample	Run `trunk check sample` without prompting	
o	--nocheck-sample	Do not run `trunk check sample` post-init	
o	--force	Overwrite existing trunk.yaml	
@	check
s	upgrade	Upgrade all linters to latest versions
s	download	Download all files needed for trunk to work offline
s	enable	Enable linters
s	disable	Disable linters
o	-y|--fix	Automatically apply all fixes without prompting	
o	-a|--all	Run on all files instead of only changed files	
o	-n|--no-fix	Don't automatically apply fixes	
o	--include-existing-autofixes	Show autofixes for existing issues	
o	--force	Run on all files, even if ignored	
o	--diff	Diff printing mode	v
o	--filter	Filter the set of executed linters and/or the returned codes; use a leading '-' to exclude a…	v
o	--exclude	Shorthand for an inverse --filter	v
o	-j|--jobs	Number of concurrent jobs (does not affect background linting)	v
o	--sample	Run each linter on N files (implies --no-fix and --all if no paths are given)	v
o	--upstream	Upstream branch used to compute changed files (autodetected by default)	v
a	1	1
=	check	--diff
v	none	
v	compact	
v	full	
#	check	1
t	filepaths
@	check upgrade
a	1	1
@	check download
a	1	1
@	check enable
a	1	1
@	check disable
a	1	1
@	fmt
o	-a|--all	Run on all files instead of only changed files	
o	-n|--no-fix	Don't automatically apply fixes	
o	--include-existing-autofixes	Show autofixes for existing issues	
o	--force	Run on all files, even if ignored	
o	--diff	Diff printing mode	v
o	--filter	Filter the set of executed linters and/or the returned codes; use a leading '-' to exclude a…	v
o	--exclude	Shorthand for an inverse --filter	v
o	-j|--jobs	Number of concurrent jobs (does not affect background linting)	v
o	--sample	Run each linter on N files (implies --no-fix and --all if no paths are given)	v
o	--upstream	Upstream branch used to compute changed files (autodetected by default)	v
a	1	1
=	fmt	--diff
v	none	
v	compact	
v	full	
#	fmt	1
t	filepaths
@	upgrade
@	git-hooks
s	install	Install trunk git hooks
@	git-hooks install
@	cache
s	clean	Clean the cache
@	cache clean
o	--all	Delete all files (including results cache)	
o	-n|--dry-run	Print all directories that would be cleaned out without running deletion	
@	print-config
@	daemon
s	launch	Start the trunk daemon if its not already running
s	shutdown	Shutdown the trunk daemon if it is running
s	status	Report daemon status
@	daemon launch
@	daemon shutdown
@	daemon status
