@	
s	cache	Run the build and use commands
s	shortcuts	Set of base commands combinations
s	build	Build targets from Pods project
s	use	Use already built binaries instead of sources
s	delete	Delete targets from the project
s	warmup	Download remote binaries for targets from Pods project
s	rollback	Restore projects state before the last Rugby usage
s	plan	Run sequence of Rugby commands
s	clear	Clear modules cache
s	update	Update Rugby version
s	doctor	Heal your wounds after using Rugby (or not)
s	shell	Run shell command from Rugby
s	env	Print Rugby environment
o	--version	Show the version	
o	--help|-h	Show help information	
a	1	0
@	cache
o	--ignore-cache	Ignore shared cache	
o	--delete-sources	Delete target groups from project	
o	--rollback|-r	Restore projects state before the last Rugby usage	
o	--sdk|-s	Build SDK: sim or ios	v
o	--arch|-a	Build architecture: auto, x86_64 or arm64	v
o	--config|-c	Build configuration	v
o	--strip	Build without debug symbols	
o	--targets|-t	Targets for building. Empty means all targets	v
o	--targets-as-regex|-g	Targets for building as a RegEx pattern	v
o	--except|-e	Exclude targets from building	v
o	--except-as-regex|-x	Exclude targets from building as a RegEx pattern	v
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--warmup	Warmup cache with this endpoint	v
o	--help|-h	Show help information	
@	shortcuts
s	umbrella	Run the plan command if plans file exists or run the cache command
s	cache	Run the build and use commands
o	--help|-h	Show help information	
@	shortcuts umbrella
o	--help|-h	Show help information	
a	1	1
@	shortcuts cache
o	--ignore-cache	Ignore shared cache	
o	--delete-sources	Delete target groups from project	
o	--rollback|-r	Restore projects state before the last Rugby usage	
o	--sdk|-s	Build SDK: sim or ios	v
o	--arch|-a	Build architecture: auto, x86_64 or arm64	v
o	--config|-c	Build configuration	v
o	--strip	Build without debug symbols	
o	--targets|-t	Targets for building. Empty means all targets	v
o	--targets-as-regex|-g	Targets for building as a RegEx pattern	v
o	--except|-e	Exclude targets from building	v
o	--except-as-regex|-x	Exclude targets from building as a RegEx pattern	v
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--warmup	Warmup cache with this endpoint	v
o	--help|-h	Show help information	
@	build
o	--ignore-cache	Ignore shared cache	
o	--sdk|-s	Build SDK: sim or ios	v
o	--arch|-a	Build architecture: auto, x86_64 or arm64	v
o	--config|-c	Build configuration	v
o	--strip	Build without debug symbols	
o	--targets|-t	Targets for building. Empty means all targets	v
o	--targets-as-regex|-g	Targets for building as a RegEx pattern	v
o	--except|-e	Exclude targets from building	v
o	--except-as-regex|-x	Exclude targets from building as a RegEx pattern	v
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
@	use
o	--delete-sources	Delete target groups from project	
o	--targets|-t	Targets for building. Empty means all targets	v
o	--targets-as-regex|-g	Targets for building as a RegEx pattern	v
o	--except|-e	Exclude targets from building	v
o	--except-as-regex|-x	Exclude targets from building as a RegEx pattern	v
o	--strip	Build without debug symbols	
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
@	delete
o	--path|-p	Project location	v
o	--safe	Keep dependencies of excepted targets	
o	--delete-sources	Delete target groups from project	
o	--targets|-t	Targets for building. Empty means all targets	v
o	--targets-as-regex|-g	Targets for building as a RegEx pattern	v
o	--except|-e	Exclude targets from building	v
o	--except-as-regex|-x	Exclude targets from building as a RegEx pattern	v
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
@	warmup
o	--analyse	Run only in analyse mode without downloading. The endpoint is optional	
o	--sdk|-s	Build SDK: sim or ios	v
o	--arch|-a	Build architecture: auto, x86_64 or arm64	v
o	--config|-c	Build configuration	v
o	--strip	Build without debug symbols	
o	--targets|-t	Targets for building. Empty means all targets	v
o	--targets-as-regex|-g	Targets for building as a RegEx pattern	v
o	--except|-e	Exclude targets from building	v
o	--except-as-regex|-x	Exclude targets from building as a RegEx pattern	v
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--timeout	Timeout for requests in seconds	v
o	--max-connections	The maximum number of simultaneous connections	v
o	--help|-h	Show help information	
a	1	0
@	rollback
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
@	plan
o	--path|-p	Path to plans yaml	v
o	--rollback|-r	Restore projects state before the last Rugby usage	
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
a	1	0
#	plan	1
d
@	clear
s	build	Delete .rugby/build folder
s	shared	Delete .rugby/bin folder
o	--modules|-m	List of modules for deletion	v
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
@	clear build
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
@	clear shared
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
@	update
s	list	List of available versions
o	--version	Version, like 2.0.0	v
o	--arch|-a	Binary architecture: x86_64 or arm64	v
o	--beta	Allow install the latest pre-release version	
o	--force|-f	Force an install even if Rugby is already installed	
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
@	update list
o	--count	Maximum versions count	v
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
@	doctor
o	--help|-h	Show help information	
@	shell
o	--output|-o	Output mode: fold, multiline, quiet	v
o	--verbose|-v	Log level	
o	--help|-h	Show help information	
a	1	0
@	env
o	--help|-h	Show help information	
