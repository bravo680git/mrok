@	
s	build	Build the package(s) in the current directory/configuration
s	install	Builds the package in current directory and copies it as an executable for system wide usage…
s	test	Shortcut for 'build --test'
s	bench	Shortcut for 'build --bench'
s	haddock	Shortcut for 'build --haddock'
s	new	Create a new project from a template. Run `stack templates' to see available templates. Note: you…
s	templates	Show how to find templates available for `stack new'. `stack new' can accept a template from a…
s	init	Create stack project config from cabal or hpack package specifications'
s	setup	Get the appropriate GHC for your project
s	path	Print out handy path information
s	ls	List command. Supports snapshots, dependencies and stack's styles
s	unpack	Unpack one or more packages locally
s	update	Update the package index
s	upgrade	Upgrade to the latest stack version
s	upload	Upload a package to Hackage
s	sdist	Create source distribution tarballs
s	dot	Visualize your project's dependency graph using Graphviz dot
s	hoogle	Run hoogle, the Haskell API search engine. Use the '-- ARGUMENT(S)' syntax to pass Hoogle…
s	exec	Execute a command. If the command is absent, the first of any arguments is taken as the command
s	run	Build and run an executable. Defaults to the first available executable if none is provided as the…
s	repl	Load a REPL
o	--help|-h	Show help for stack	
o	--version	Show version for stack	
o	--numeric-version	Show only the numeric version for stack	
o	--hpack-numeric-version	Show only hpack's version number	
o	--verbosity	Verbosity: silent, error, warn, info, debug	
o	--verbose|-v	Enable verbose mode: verbosity level "debug"	
o	--silent	Enable silent mode: verbosity level "silent"	
o	--stack-root	Absolute path to the global stack root directory (Overrides any STACK_ROOT environment variable)	
o	--work-dir	Relative path of work directory (Overrides any STACK_WORK environment variable, default is…	
o	--system-ghc	Enable using the system installed GHC (on the PATH) if it is available and its version matches…	
o	--no-system-ghc	Disable using the system installed GHC (on the PATH) if it is available and its version matches…	
o	--install-ghc	Enable downloading and installing GHC if necessary (can be done manually with stack setup)…	
o	--no-install-ghc	Disable downloading and installing GHC if necessary (can be done manually with stack setup)…	
o	--ghc-variant	Specialized GHC variant, e.g. integersimple (incompatible with --system-ghc)	
o	--ghc-build	Specialized GHC build, e.g. 'gmp4' or 'standard' (usually auto-detected)	
o	--jobs|-j	Number of concurrent jobs to run. Should be provied as ARGS	
o	--extra-include-dirs	Extra directories to check for C header files	
o	--extra-lib-dir	Extra directories to check for libraries	
o	--custom-preprocessor-extensions	Extensions used for custom preprocessors	
o	--color|--colour	Specify when to use color in output	v
o	--compiler	Use the specified compiler	v
o	--terminal	Enable overriding terminal detection in the case of running in a false terminal	
o	--no-terminal	Disable overriding terminal detection in the case of running in a false terminal	
o	--stack-colors|--stack-colours	Specify stack's output styles	v
o	--terminal-width	Specify the width of the terminal, used for pretty-print messages	v
o	--stack-yaml	Override project stack.yaml file (overrides any STACK_YAML environment variable)	v
o	--lock-file	Specify how to interact with lock files	v
=		--color
v	always	
v	never	
v	auto	
@	build
o	--resolver	Override resolver in project file	v
o	--bench	Override resolver in project file	
o	--test	Run complete test suite	
o	--copy-bins	Enable copying any generated executables to the local bin path (default: disabled)	
o	--no-copy-bins	Disable copying any generated executables to the local bin path (default: disabled)	
o	--haddock	Enable generating Haddocks the package(s) in this directory/configuration (default: disabled)	
o	--no-haddock	Disable generating Haddocks the package(s) in this directory/configuration (default: disabled)	
o	--open	Enable opening the local Haddock	
o	--no-open	Disable opening the local Haddock	
o	--haddock-deps	Enable building Haddocks for dependencies (default: true if building Haddocks, false otherwise)	
o	--no-haddock-deps	Disable building Haddocks for dependencies (default: true if building Haddocks, false otherwise)	
o	--pedantic	Turn on all warnings(-Wall) and errors(-Werror)	
o	--only-locals	Only build packages in the local database, fail if the build plan includes the snapshot database	
o	--file-watch	Watch for changes in the files used to build the project, and kick off a new build when new…	
o	--watch-all	Watch all local files not taking targets into account	
o	-file-watch-poll	Like --file-watch, but polling the filesystem instead of using events	
o	--only-snapshot	Only build packages for the snapshot database, not the local database	
o	--only-configure	Only perform the configure step, not any builds. Intended for tool usage, may break when used on…	
o	--trace	Enable profiling in libraries, executables, etc. for all expressions and generate a backtrace on…	
o	--profile	Runs profiling in libraries, executables, etc. for all expressions and generate a profiling report…	
o	--no-strip	Disable DWARF debugging symbol stripping in libraries, executables, etc. for all expressions…	
o	--library-profiling	Enable library profiling for TARGETs and all its dependencies (default: disabled)	
o	--no-library-profiling	Disable library profiling for TARGETs and all its dependencies (default: disabled)	
o	--executable-profiling	Enable executable profiling for TARGETs and all its dependencies (default: disabled)	
o	--no-executable-profiling	Disable executable profiling for TARGETs and all its dependencies (default: disabled)	
o	--library-stripping	Enable library stripping for TARGETs and all its dependencies (default: enabled	
o	--no-library-stripping	Disable library stripping for TARGETs and all its dependencies (default: enabled	
o	--executable-stripping	Enable executable stripping for TARGETs and all its dependencies (default: enabled)	
o	--no-executable-stripping	Disable executable stripping for TARGETs and all its dependencies (default: enabled)	
o	--ghc-options	Specify additional options passed to GHC for all local targets. Does not affect extra-dep and…	v
@	install
@	test
@	bench
@	haddock
@	new
@	templates
@	init
@	setup
@	path
@	ls
@	unpack
@	update
@	upgrade
@	upload
@	sdist
@	dot
@	hoogle
@	exec
o	--snapshot-location-base	The base location of LTS/Nightly snapshots	v
o	--cwd	Sets the working directory before executing the command	v
o	--setup-info-yaml	Alternate URL or relative / absolute path for stack dependencies	v
o	--ghc-package-path	Enable setting the GHC_PACKAGE_PATH variable for the subprocess (default: enabled)	
o	--no-ghc-package-path	Disable setting the GHC_PACKAGE_PATH variable for the subprocess (default: enabled)	
o	--package	Additional package(s) that must be installed	v
o	--stack-exe	Enable setting the STACK_EXE environment variable to the path for the stack executable (default…	
o	--no-stack-exe	Disable setting the STACK_EXE environment variable to the path for the stack executable (default…	
@	run
@	repl
