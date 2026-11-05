@	
s	bug	Start a bug report
s	build	Compile packages and dependencies
s	clean	Remove object files and cached files
s	doc	Show documentation for package or symbol
s	env	Print Go environment information
s	fix	Update packages to use new APIs
s	fmt	Gofmt (reformat) package sources
s	generate	Generate Go files by processing source
s	get	Add dependencies to current module and install them
s	install	Compile and install packages and dependencies
s	list	List packages or modules
s	mod	Module maintenance
s	work	Workspace maintenance
s	run	Compile and run Go program
s	test	Test packages
s	tool	Run specified go tool
s	version	Print Go version
s	vet	Report likely mistakes in packages
@	bug
@	build
o	-n	Print the commands but do not run them	
o	-v	Print the names of packages as they are compiled	
o	-x	Print the commands	
o	-tags	A comma-separated list of build tags to consider satisfied during the build	v
o	-toolexec	A program to use to invoke toolchain programs like vet and asm	v
o	-a	Force rebuilding of packages that are already up-to-date	
o	-p	The number of programs, such as build commands or	v
o	-race	Enable data race detection.	
o	-msan	Enable interoperation with memory sanitizer.	
o	-work	Print the name of the temporary work directory and	
o	-asmflags	Arguments to pass on each go tool asm invocation	v
o	-buildmode	Build mode to use. See 'go help buildmode' for more	v
o	-compiler	Name of compiler to use, as in runtime.Compiler (gccgo or gc)	v
o	-gccgoflags	Arguments to pass on each gccgo compiler/linker invocation	v
o	-gcflags	Arguments to pass on each go tool compile invocation	v
o	-installsuffix	A suffix to use in the name of the package installation directory,	v
o	-ldflags	Arguments to pass on each go tool link invocation	v
o	-linkshared	Build code that will be linked against shared libraries previously	
o	-mod	Module download mode to use: readonly, vendor, or mod	v
o	-modcacherw	Leave newly-created directories in the module cache read-write	
o	-modfile	In module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the…	v
o	-overlay	Read a JSON config file that provides an overlay for build operations	v
o	-pkgdir	Install and load all packages from dir instead of the usual locations	v
o	-trimpath	Remove all file system paths from the resulting executable	
o	-o	Write the resulting executable or object to the named output file or directory	v
o	-i	Install the packages that are dependencies of the target	
a	1	1
=	build	-buildmode
v	archive	Build the listed non-main packages into .a files
v	c-archive	Build the listed main package, plus all packages it imports, into a C archive file
v	c-shared	Build the listed main package, plus all packages it imports, into a C shared library
v	default	Listed main packages are built into executables and listed non-main packages are built into .a files
v	shared	Combine all the listed non-main packages into a single shared library that will be used when…
v	exe	Build the listed main packages and everything they import into executables
v	pie	Build the listed main packages and everything they import into position independent executables…
v	plugin	Build the listed main packages, plus all packages that they import, into a Go plugin
=	build	-mod
v	readonly	
v	vendor	
v	mod	
=	build	-o
t	filepaths,folders
#	build	1
t	filepaths
@	clean
o	-n	Print the commands but do not run them	
o	-v	Print the names of packages as they are compiled	
o	-x	Print the commands	
o	-tags	A comma-separated list of build tags to consider satisfied during the build	v
o	-toolexec	A program to use to invoke toolchain programs like vet and asm	v
o	-a	Force rebuilding of packages that are already up-to-date	
o	-p	The number of programs, such as build commands or	v
o	-race	Enable data race detection.	
o	-msan	Enable interoperation with memory sanitizer.	
o	-work	Print the name of the temporary work directory and	
o	-asmflags	Arguments to pass on each go tool asm invocation	v
o	-buildmode	Build mode to use. See 'go help buildmode' for more	v
o	-compiler	Name of compiler to use, as in runtime.Compiler (gccgo or gc)	v
o	-gccgoflags	Arguments to pass on each gccgo compiler/linker invocation	v
o	-gcflags	Arguments to pass on each go tool compile invocation	v
o	-installsuffix	A suffix to use in the name of the package installation directory,	v
o	-ldflags	Arguments to pass on each go tool link invocation	v
o	-linkshared	Build code that will be linked against shared libraries previously	
o	-mod	Module download mode to use: readonly, vendor, or mod	v
o	-modcacherw	Leave newly-created directories in the module cache read-write	
o	-modfile	In module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the…	v
o	-overlay	Read a JSON config file that provides an overlay for build operations	v
o	-pkgdir	Install and load all packages from dir instead of the usual locations	v
o	-trimpath	Remove all file system paths from the resulting executable	
o	-i	Remove the corresponding installed archive or binary	
o	-r	Apply recursively to all the dependencies of the packages named by the import paths	
o	-cache	Remove the entire go build cache	
o	-testcache	Expire all test results in the go build cache	
o	-modcache	Remove the entire module download cache, including unpacked source code of versioned dependencies	
=	clean	-buildmode
v	archive	Build the listed non-main packages into .a files
v	c-archive	Build the listed main package, plus all packages it imports, into a C archive file
v	c-shared	Build the listed main package, plus all packages it imports, into a C shared library
v	default	Listed main packages are built into executables and listed non-main packages are built into .a files
v	shared	Combine all the listed non-main packages into a single shared library that will be used when…
v	exe	Build the listed main packages and everything they import into executables
v	pie	Build the listed main packages and everything they import into position independent executables…
v	plugin	Build the listed main packages, plus all packages that they import, into a Go plugin
=	clean	-mod
v	readonly	
v	vendor	
v	mod	
@	doc
o	-all	Show all the documentation for the package	
o	-c	Respect case when matching symbols	
o	-cmd	Treat a command (package main) like a regular package. Otherwise package main's exported symbols…	
o	-short	One-line representation for each symbol	
o	-src	Show the full source code for the symbol	
o	-u	Show documentation for unexported as well as exported symbols, methods, and fields	
a	1	0
@	env
o	-json	Prints the environment in JSON format instead of as a shell script	
o	-u	Unset the default setting for the named environment variables	v
o	-w	Change the default settings of the named environment variables to the given values	v
@	fix
a	1	1
#	fix	1
t	filepaths
@	fmt
o	-n	Print the commands that would be executed	
o	-x	Print the commands as they are executed	
o	-mod	Which module download mode to use	v
a	1	1
=	fmt	-mod
v	readonly	
v	vendor	
#	fmt	1
t	filepaths
@	generate
o	-n	Print the commands but do not run them	
o	-v	Print the names of packages as they are compiled	
o	-x	Print the commands	
o	-tags	A comma-separated list of build tags to consider satisfied during the build	v
o	-toolexec	A program to use to invoke toolchain programs like vet and asm	v
o	-a	Force rebuilding of packages that are already up-to-date	
o	-p	The number of programs, such as build commands or	v
o	-race	Enable data race detection.	
o	-msan	Enable interoperation with memory sanitizer.	
o	-work	Print the name of the temporary work directory and	
o	-asmflags	Arguments to pass on each go tool asm invocation	v
o	-buildmode	Build mode to use. See 'go help buildmode' for more	v
o	-compiler	Name of compiler to use, as in runtime.Compiler (gccgo or gc)	v
o	-gccgoflags	Arguments to pass on each gccgo compiler/linker invocation	v
o	-gcflags	Arguments to pass on each go tool compile invocation	v
o	-installsuffix	A suffix to use in the name of the package installation directory,	v
o	-ldflags	Arguments to pass on each go tool link invocation	v
o	-linkshared	Build code that will be linked against shared libraries previously	
o	-mod	Module download mode to use: readonly, vendor, or mod	v
o	-modcacherw	Leave newly-created directories in the module cache read-write	
o	-modfile	In module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the…	v
o	-overlay	Read a JSON config file that provides an overlay for build operations	v
o	-pkgdir	Install and load all packages from dir instead of the usual locations	v
o	-trimpath	Remove all file system paths from the resulting executable	
o	-run	Specifies a regular expression to select directives whose full original source text matches the…	
=	generate	-buildmode
v	archive	Build the listed non-main packages into .a files
v	c-archive	Build the listed main package, plus all packages it imports, into a C archive file
v	c-shared	Build the listed main package, plus all packages it imports, into a C shared library
v	default	Listed main packages are built into executables and listed non-main packages are built into .a files
v	shared	Combine all the listed non-main packages into a single shared library that will be used when…
v	exe	Build the listed main packages and everything they import into executables
v	pie	Build the listed main packages and everything they import into position independent executables…
v	plugin	Build the listed main packages, plus all packages that they import, into a Go plugin
=	generate	-mod
v	readonly	
v	vendor	
v	mod	
@	get
o	-n	Print the commands but do not run them	
o	-v	Print the names of packages as they are compiled	
o	-x	Print the commands	
o	-tags	A comma-separated list of build tags to consider satisfied during the build	v
o	-toolexec	A program to use to invoke toolchain programs like vet and asm	v
o	-a	Force rebuilding of packages that are already up-to-date	
o	-p	The number of programs, such as build commands or	v
o	-race	Enable data race detection.	
o	-msan	Enable interoperation with memory sanitizer.	
o	-work	Print the name of the temporary work directory and	
o	-asmflags	Arguments to pass on each go tool asm invocation	v
o	-buildmode	Build mode to use. See 'go help buildmode' for more	v
o	-compiler	Name of compiler to use, as in runtime.Compiler (gccgo or gc)	v
o	-gccgoflags	Arguments to pass on each gccgo compiler/linker invocation	v
o	-gcflags	Arguments to pass on each go tool compile invocation	v
o	-installsuffix	A suffix to use in the name of the package installation directory,	v
o	-ldflags	Arguments to pass on each go tool link invocation	v
o	-linkshared	Build code that will be linked against shared libraries previously	
o	-mod	Module download mode to use: readonly, vendor, or mod	v
o	-modcacherw	Leave newly-created directories in the module cache read-write	
o	-modfile	In module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the…	v
o	-overlay	Read a JSON config file that provides an overlay for build operations	v
o	-pkgdir	Install and load all packages from dir instead of the usual locations	v
o	-trimpath	Remove all file system paths from the resulting executable	
o	-t	Modules needed to build tests of packages specified on the command line	
o	-u	Update to newer minor or patch releases when available	V
o	-insecure	Permit fetching from insecure origins	
o	-d	Only update go.mod and download source code needed to build packages	
a	1	0
=	get	-buildmode
v	archive	Build the listed non-main packages into .a files
v	c-archive	Build the listed main package, plus all packages it imports, into a C archive file
v	c-shared	Build the listed main package, plus all packages it imports, into a C shared library
v	default	Listed main packages are built into executables and listed non-main packages are built into .a files
v	shared	Combine all the listed non-main packages into a single shared library that will be used when…
v	exe	Build the listed main packages and everything they import into executables
v	pie	Build the listed main packages and everything they import into position independent executables…
v	plugin	Build the listed main packages, plus all packages that they import, into a Go plugin
=	get	-mod
v	readonly	
v	vendor	
v	mod	
=	get	-u
v	patch	Update to newer patch releases
@	install
o	-n	Print the commands but do not run them	
o	-v	Print the names of packages as they are compiled	
o	-x	Print the commands	
o	-tags	A comma-separated list of build tags to consider satisfied during the build	v
o	-toolexec	A program to use to invoke toolchain programs like vet and asm	v
o	-a	Force rebuilding of packages that are already up-to-date	
o	-p	The number of programs, such as build commands or	v
o	-race	Enable data race detection.	
o	-msan	Enable interoperation with memory sanitizer.	
o	-work	Print the name of the temporary work directory and	
o	-asmflags	Arguments to pass on each go tool asm invocation	v
o	-buildmode	Build mode to use. See 'go help buildmode' for more	v
o	-compiler	Name of compiler to use, as in runtime.Compiler (gccgo or gc)	v
o	-gccgoflags	Arguments to pass on each gccgo compiler/linker invocation	v
o	-gcflags	Arguments to pass on each go tool compile invocation	v
o	-installsuffix	A suffix to use in the name of the package installation directory,	v
o	-ldflags	Arguments to pass on each go tool link invocation	v
o	-linkshared	Build code that will be linked against shared libraries previously	
o	-mod	Module download mode to use: readonly, vendor, or mod	v
o	-modcacherw	Leave newly-created directories in the module cache read-write	
o	-modfile	In module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the…	v
o	-overlay	Read a JSON config file that provides an overlay for build operations	v
o	-pkgdir	Install and load all packages from dir instead of the usual locations	v
o	-trimpath	Remove all file system paths from the resulting executable	
a	1	1
=	install	-buildmode
v	archive	Build the listed non-main packages into .a files
v	c-archive	Build the listed main package, plus all packages it imports, into a C archive file
v	c-shared	Build the listed main package, plus all packages it imports, into a C shared library
v	default	Listed main packages are built into executables and listed non-main packages are built into .a files
v	shared	Combine all the listed non-main packages into a single shared library that will be used when…
v	exe	Build the listed main packages and everything they import into executables
v	pie	Build the listed main packages and everything they import into position independent executables…
v	plugin	Build the listed main packages, plus all packages that they import, into a Go plugin
=	install	-mod
v	readonly	
v	vendor	
v	mod	
@	list
o	-n	Print the commands but do not run them	
o	-v	Print the names of packages as they are compiled	
o	-x	Print the commands	
o	-tags	A comma-separated list of build tags to consider satisfied during the build	v
o	-toolexec	A program to use to invoke toolchain programs like vet and asm	v
o	-a	Force rebuilding of packages that are already up-to-date	
o	-p	The number of programs, such as build commands or	v
o	-race	Enable data race detection.	
o	-msan	Enable interoperation with memory sanitizer.	
o	-work	Print the name of the temporary work directory and	
o	-asmflags	Arguments to pass on each go tool asm invocation	v
o	-buildmode	Build mode to use. See 'go help buildmode' for more	v
o	-compiler	Name of compiler to use, as in runtime.Compiler (gccgo or gc)	v
o	-gccgoflags	Arguments to pass on each gccgo compiler/linker invocation	v
o	-gcflags	Arguments to pass on each go tool compile invocation	v
o	-installsuffix	A suffix to use in the name of the package installation directory,	v
o	-ldflags	Arguments to pass on each go tool link invocation	v
o	-linkshared	Build code that will be linked against shared libraries previously	
o	-mod	Module download mode to use: readonly, vendor, or mod	v
o	-modcacherw	Leave newly-created directories in the module cache read-write	
o	-modfile	In module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the…	v
o	-overlay	Read a JSON config file that provides an overlay for build operations	v
o	-pkgdir	Install and load all packages from dir instead of the usual locations	v
o	-trimpath	Remove all file system paths from the resulting executable	
o	-compiled	Set CompiledGoFiles to the Go source files	
o	-deps	Terate over not just the named packages but also all their dependencies	
o	-f	Specify an alternate format for the list	v
o	-e	Processes the erroneous packages with the usual printing	
o	-export	Set the Export field to the name of a file containing up-to-date export information for the given…	
o	-find	Identify the named packages but not resolve their dependencies	
o	-test	Report test binaries	
o	-m	List modules instead of packages	
o	-u	Add information about available upgrades	
o	-versions	Set the Module's Versions field to a list of all known versions of that module	
o	-retracted	Eport information about retracted module versions	
a	1	0
=	list	-buildmode
v	archive	Build the listed non-main packages into .a files
v	c-archive	Build the listed main package, plus all packages it imports, into a C archive file
v	c-shared	Build the listed main package, plus all packages it imports, into a C shared library
v	default	Listed main packages are built into executables and listed non-main packages are built into .a files
v	shared	Combine all the listed non-main packages into a single shared library that will be used when…
v	exe	Build the listed main packages and everything they import into executables
v	pie	Build the listed main packages and everything they import into position independent executables…
v	plugin	Build the listed main packages, plus all packages that they import, into a Go plugin
=	list	-mod
v	readonly	
v	vendor	
v	mod	
@	mod
s	download	Download the named modules into the module cache
s	edit	Edit and format go.mod files
s	graph	Print the module requirement graph
s	init	Initialize and write a new go.mod file in the current directory
s	tidy	Ensure that the go.mod file matches the source code in the module
s	vendor	Construct a directory named vendor in the main module's root directory
s	verify	Check that dependencies of the main module stored in the module cache have not been modified since…
s	why	Show a shortest path in the import graph from the main module to each of the listed packages
@	mod download
o	-json	Print a sequence of JSON objects to standard output, describing each downloaded module (or failure)	
o	-x	Print the commands download executes to standard error	
a	1	1
@	mod edit
o	-module	Change the module's path	
o	-go	Set the expected Go language version	v=
o	-require	Add a requirement on the given module	v=
o	-droprequire	Drop a requirement on the given module	v=
o	-exclude	Add an exclusion on the given module	v=
o	-dropexclude	Drop an exclusion on the given module	v=
o	-replace	Add a replacement of the given module path and version pair	v=
o	-dropreplace	Drops a replacement of the given module path and version pair	v=
o	-retract	Add a retraction for the given version	v=
o	-dropretract	Drop a retraction for the given version	v=
o	-fmt	Format the go.mod file without making other changes	
o	-print	Print the final go.mod in its text format instead of writing it back to disk	
o	-json	Print the final go.mod in JSON format instead of writing it back to disk in text forma	
@	mod graph
@	mod init
a	1	0
@	mod tidy
o	-e	Attempt to proceed despite errors encountered while loading packages	
o	-v	Print information about removed modules	
@	mod vendor
o	-e	Attempt to proceed despite errors encountered while loading packages	
o	-v	Print information about removed modules	
@	mod verify
@	mod why
o	-m	Treat its arguments as a list of modules	
o	-vendor	Ignore imports in tests of packages outside the main module	
a	1	1
@	work
s	edit	Edit go.work from tools or scripts
s	init	Initialize workspace file
s	sync	Sync workspace build list to modules
s	use	Add modules to workspace file
@	work edit
o	-fmt	The -fmt flag reformats the go.work file without making other changes. This reformatting is also…	
o	-use	The -use=path and -dropuse=path flags add and drop a use directive from the go.work file's set of…	v=
o	-dropuse	The -use=path and -dropuse=path flags add and drop a use directive from the go.work file's set of…	v=
o	-replace	The -replace=old[@v]=new[@v] flag adds a replacement of the given module path and version pair. If…	v=
o	-dropreplace	The -dropreplace=old[@v] flag drops a replacement of the given module path and version pair. If…	v=
o	-go	Set the expected Go language version	v=
o	-print	The -print flag prints the final go.work in its text format instead of writing it back to go.mod	
o	-json	The -json flag prints the final go.work file in JSON format instead of writing it back to go.mod	
@	work init
a	1	1
@	work sync
@	work use
o	-r	The -r flag searches recursively for modules in the argument directories, and the use command…	
a	1	1
@	run
o	-n	Print the commands but do not run them	
o	-v	Print the names of packages as they are compiled	
o	-x	Print the commands	
o	-tags	A comma-separated list of build tags to consider satisfied during the build	v
o	-toolexec	A program to use to invoke toolchain programs like vet and asm	v
o	-a	Force rebuilding of packages that are already up-to-date	
o	-p	The number of programs, such as build commands or	v
o	-race	Enable data race detection.	
o	-msan	Enable interoperation with memory sanitizer.	
o	-work	Print the name of the temporary work directory and	
o	-asmflags	Arguments to pass on each go tool asm invocation	v
o	-buildmode	Build mode to use. See 'go help buildmode' for more	v
o	-compiler	Name of compiler to use, as in runtime.Compiler (gccgo or gc)	v
o	-gccgoflags	Arguments to pass on each gccgo compiler/linker invocation	v
o	-gcflags	Arguments to pass on each go tool compile invocation	v
o	-installsuffix	A suffix to use in the name of the package installation directory,	v
o	-ldflags	Arguments to pass on each go tool link invocation	v
o	-linkshared	Build code that will be linked against shared libraries previously	
o	-mod	Module download mode to use: readonly, vendor, or mod	v
o	-modcacherw	Leave newly-created directories in the module cache read-write	
o	-modfile	In module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the…	v
o	-overlay	Read a JSON config file that provides an overlay for build operations	v
o	-pkgdir	Install and load all packages from dir instead of the usual locations	v
o	-trimpath	Remove all file system paths from the resulting executable	
o	-exec	Invoke the binary using xprog	v
a	1	0
=	run	-buildmode
v	archive	Build the listed non-main packages into .a files
v	c-archive	Build the listed main package, plus all packages it imports, into a C archive file
v	c-shared	Build the listed main package, plus all packages it imports, into a C shared library
v	default	Listed main packages are built into executables and listed non-main packages are built into .a files
v	shared	Combine all the listed non-main packages into a single shared library that will be used when…
v	exe	Build the listed main packages and everything they import into executables
v	pie	Build the listed main packages and everything they import into position independent executables…
v	plugin	Build the listed main packages, plus all packages that they import, into a Go plugin
=	run	-mod
v	readonly	
v	vendor	
v	mod	
@	test
o	-n	Print the commands but do not run them	
o	-v	Print the names of packages as they are compiled	
o	-x	Print the commands	
o	-tags	A comma-separated list of build tags to consider satisfied during the build	v
o	-toolexec	A program to use to invoke toolchain programs like vet and asm	v
o	-a	Force rebuilding of packages that are already up-to-date	
o	-p	The number of programs, such as build commands or	v
o	-race	Enable data race detection.	
o	-msan	Enable interoperation with memory sanitizer.	
o	-work	Print the name of the temporary work directory and	
o	-asmflags	Arguments to pass on each go tool asm invocation	v
o	-buildmode	Build mode to use. See 'go help buildmode' for more	v
o	-compiler	Name of compiler to use, as in runtime.Compiler (gccgo or gc)	v
o	-gccgoflags	Arguments to pass on each gccgo compiler/linker invocation	v
o	-gcflags	Arguments to pass on each go tool compile invocation	v
o	-installsuffix	A suffix to use in the name of the package installation directory,	v
o	-ldflags	Arguments to pass on each go tool link invocation	v
o	-linkshared	Build code that will be linked against shared libraries previously	
o	-mod	Module download mode to use: readonly, vendor, or mod	v
o	-modcacherw	Leave newly-created directories in the module cache read-write	
o	-modfile	In module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the…	v
o	-overlay	Read a JSON config file that provides an overlay for build operations	v
o	-pkgdir	Install and load all packages from dir instead of the usual locations	v
o	-trimpath	Remove all file system paths from the resulting executable	
o	-args	Pass the remainder of the command line to the test binary	v
o	-c	Compile the test binary to pkg.test but do not run it	
o	-exec	Invoke the binary using xprog	v
o	-i	Install packages that are dependencies of the test	
o	-json	Convert test output to JSON suitable	
o	-o	Compile the test binary to the named file	v
=	test	-buildmode
v	archive	Build the listed non-main packages into .a files
v	c-archive	Build the listed main package, plus all packages it imports, into a C archive file
v	c-shared	Build the listed main package, plus all packages it imports, into a C shared library
v	default	Listed main packages are built into executables and listed non-main packages are built into .a files
v	shared	Combine all the listed non-main packages into a single shared library that will be used when…
v	exe	Build the listed main packages and everything they import into executables
v	pie	Build the listed main packages and everything they import into position independent executables…
v	plugin	Build the listed main packages, plus all packages that they import, into a Go plugin
=	test	-mod
v	readonly	
v	vendor	
v	mod	
=	test	-o
t	filepaths
@	tool
o	-n	Print the command that would be executed but not execute it	
a	1	0
#	tool	1
g	go tool	\n
@	version
o	-m	Print each executable's embedded module version information	
o	-v	Report unrecognized files	
a	1	0
@	vet
o	-n	Print the commands but do not run them	
o	-v	Print the names of packages as they are compiled	
o	-x	Print the commands	
o	-tags	A comma-separated list of build tags to consider satisfied during the build	v
o	-toolexec	A program to use to invoke toolchain programs like vet and asm	v
o	-vettool	Select a different analysis tool with alternative or additional checks	v=
a	1	0
