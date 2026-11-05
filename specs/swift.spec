@	
s	build	Build sources into binary products
s	run	Build and run an executable product
s	test	Build and run tests
s	package	Perform operations on Swift packages
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	-access-notes-path	Specify YAML file to override attributes on Swift declarations in this module	v
o	-assert-config	Specify the assert_configuration replacement	v
o	-async-main	Resolve main function as if it were called from an asynchronous context	
o	-clang-target	Separately set the target we should use for internal Clang instance	v
o	-color-diagnostics	Print diagnostics in color	
o	-continue-building-after-errors	Continue building, even after errors are encountered	
o	-coverage-prefix-map	Remap source paths in coverage info	v
o	-debug-info-format	Specify the debug info format type	v=
o	-debug-info-store-invocation	Emit the compiler invocation in the debug info	
o	-debug-prefix-map	Remap source paths in debug info	v
o	-diagnostic-style	The formatting style used when printing diagnostics	v
o	-disable-actor-data-race-checks	Disable runtime checks for actor data races	
o	-disable-autolinking-runtime-compatibility-concurrency	Do not use autolinking for the concurrency runtime compatibility library	
o	-disable-autolinking-runtime-compatibility-dynamic-replacements	Do not use autolinking for the dynamic replacement runtime compatibility library	
o	-disable-autolinking-runtime-compatibility	Do not use autolinking for runtime compatibility libraries	
o	-disable-clang-target	Disable a separately specified target triple for Clang instance to use	
o	-disable-incremental-imports	Disable cross-module incremental build metadata and driver scheduling for Swift modules	
o	-disable-only-one-dependency-file	Disables incremental build optimization that only produces one dependencies file	
o	-disallow-use-new-driver	Disable using new swift-driver	
o	-D	Marks a conditional compilation flag as true	v
o	-embed-tbd-for-module	Embed symbols from the module in the emitted tbd file	v
o	-enable-actor-data-race-checks	Emit runtime checks for actor data races	
o	-enable-bare-slash-regex	Enable the use of forward slash regular-expression literal syntax	
o	-enable-experimental-additive-arithmetic-derivation	Enable experimental 'AdditiveArithmetic' derived conformances	
o	-enable-experimental-concise-pound-file	Enable experimental concise '#file' identifier	
o	-enable-experimental-cxx-interop	Allow importing C++ modules into Swift (experimental feature)	
o	-enable-experimental-forward-mode-differentiation	Enable experimental forward mode differentiation	
o	-enable-incremental-imports	Enable cross-module incremental build metadata and driver scheduling for Swift modules	
o	-enable-library-evolution	Build the module to allow binary-compatible library evolution	
o	-enable-only-one-dependency-file	Enables incremental build optimization that only produces one dependencies file	
o	-enforce-exclusivity	Enforce law of exclusivity	v=
o	-experimental-cxx-stdlib	C++ standard library to use; forwarded to Clang's -std lib flag	v
o	-file-compilation-dir	The compilation directory to embed in the debug info. Coverage mapping is not supported yet	v
o	-file-prefix-map	Remap source paths in debug, coverage, and index info	v
o	-framework	Specifies a framework which should be linked against	v
o	-Fsystem	Add directory to system framework search path	v
o	-F	Add directory to framework search path	v
o	-gdwarf-types	Emit full DWARF type info	
o	-gline-tables-only	Emit minimal debug info for backtraces only	
o	-gnone	Don't emit debug info	
o	-g	Emit debug info. This is the preferred setting for debugging with LLDB	
o	-index-ignore-clang-modules	Avoid indexing clang modules (pcms)	
o	-index-store-path	Store indexing data to path	v
o	-index-unit-output-path	Use the specified path as the output path in the produced index data	v
o	-I	Add directory to the import search path	v
o	-j	Number of commands to execute in parallel	v
o	-libc	The libc runtime library to use	v
o	-locale	Choose a language for diagnostic messages	v
o	-localization-path	Path to localized diagnostic messages directory	v
o	-L	Add directory to library link search path	v
o	-l	Specifies a library which should be linked against	v
o	-module-abi-name	ABI name to use for the contents of this module	v
o	-module-alias	If a source file imports or references module <alias_name>, the <underlying_name> is used for the…	v
o	-module-cache-path	Specifies the Clang module cache path	v
o	-module-link-name	Library to link against when using this module	v
o	-module-name	Name of the module to build	v
o	-no-color-diagnostics	Do not print diagnostics in color	
o	-no-warnings-as-errors	Don't treat warnings as error	
o	-nostdimport	Don't search the standard library import path for modules	
o	-num-threads	Enable multi-threading and specify number of threads	v
o	-Onone	Compile without any optimization	
o	-Osize	Compile with optimizations and target small code size	
o	-Ounchecked	Compile with optimizations and remove runtime safety checks	
o	-O	Compile with optimizations	
o	-prefix-serialized-debugging-options	Apply debug prefix mappings to serialized debug info in Swiftmodule files	
o	-pretty-print	Pretty-print the output JSON	
o	-print-educational-notes	Include educational notes in printed diagnostic output, if available	
o	-print-target-info	Print target information for the given target <triple>, such as x86_64-apple-macos10.9	
o	-Rcross-import	Emit a remark if a cross-import of a module is triggered	
o	-remove-runtime-asserts	Remove runtime safety checks	
o	-requirement-machine-abstract-signatures	Control usage of experimental generic signature minimization	v=
o	-requirement-machine-inferred-signatures	Control usage of experimental generic signature minimization	v=
o	-requirement-machine-protocol-signatures	Control usage of experimental protocol requirement signature minimization	v=
o	-Rmodule-loading	Emit a remark and file path of each loaded module	
o	-Rpass-missed	Report missed transformations by optimization passes whose name matches the given POSIX regular…	v=
o	-Rpass	Report performed transformations by optimization passes whose name matches the given POSIX regular…	v=
o	-runtime-compatibility-version	Link compatibility library for Swift runtime version, or 'none'	v
o	-save-optimization-record-passes	Only include passes which match a specified regular expression in the generated optimization…	v
o	-save-optimization-record-path	Specify the file name of any generated optimization record	v
o	-save-optimization-record	Generate an optimization record file in a specific format	v=
o	-save-optimization-record	Generate a YAML optimization record file	
o	-sdk	Compile against a specific SDK	v
o	-serialize-diagnostics-path	Emit a serialized diagnostics file	v
o	-static-executable	Statically link the executable	
o	-static-stdlib	Statically link the Swift standard library	
o	-strict-concurrency	Specify the how strict concurrency checking will be	v=
o	-suppress-warnings	Suppress all warnings	
o	-swift-isa-ptrauth-mode	Mode for staging isa/super signing	v
o	-swift-ptrauth-mode	Mode for staging pointer authentication	v
o	-swift-version	Interpret input according to a specific Swift language version number	v
o	-target-cpu	Generate code for a particular CPU variant	v
o	-target-min-inlining-version	Require inlinable code with no '@available' attribute to back-deploy to this version of the…	v
o	-target-variant	Generate 'zippered' code for macCatalyst that can run on the specified variant target triple in…	v
o	-target	Generate code for the given target <triple>, such as x86_64-apple-macos10.9	v
o	-use-ld	Specifies the linker to be used	v=
o	-user-module-version	Module version specified from Swift module authors	v
o	-vfsoverlay	Add directory to VFS overlay file	v
o	-v	Show commands to run and use verbose output	
o	-warn-concurrency	Warn about code that is unsafe according to the Swift Concurrency model and will become ill-formed…	
o	-warn-implicit-overrides	Warn about implicit overrides of protocol members	
o	-warn-swift3-objc-inference-complete	Warn about deprecated @objc inference in Swift 3 for every declaration that will no longer be…	
o	-warn-swift3-objc-inference-minimal	Warn about deprecated @objc inference in Swift 3 based on direct uses of the Objective-C entrypoint	
o	-warnings-as-errors	Treat warnings as errors	
o	-working-directory	Resolve file paths relative to the specified directory	v
o	-Xcc	Pass <arg> to the C/C++/Objective-C compiler	v
o	-Xlinker	Specifies an option which should be passed to the linker	v
=		-assert-config
v	Debug	
v	Release	
v	Unchecked	
v	DisableReplacement	
=		-coverage-prefix-map
d
=		-debug-info-format
v	dwarf	
v	codeview	
=		-debug-prefix-map
d
=		-diagnostic-style
v	swift	
v	llvm	
=		-file-prefix-map
d
=		-module-alias
d
=		-requirement-machine-abstract-signatures
v	on	
v	off	
v	verify	
v	check	
=		-requirement-machine-inferred-signatures
v	on	
v	off	
v	verify	
v	check	
=		-requirement-machine-protocol-signatures
v	on	
v	off	
v	verify	
v	check	
=		-strict-concurrency
v	minimal	
v	targeted	
v	complete	
=		-swift-isa-ptrauth-mode
v	LegacyAndStrip	
v	NewAndStrip	
v	NewAndAuth	
=		-swift-ptrauth-mode
v	LegacyAndStrip	
v	NewAndStrip	
v	NewAndAuth	
@	build
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--build-tests	Build both source and test targets	
o	--show-bin-path	Print the binary output path	
o	--target	Build the specified target	v
o	--product	Build the specified product	v
@	run
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--skip-build	Skip building the executable product	
o	--build-tests	Build both source and test targets	
o	--repl	Launch Swift REPL for the package	
a	2	0
@	test
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--skip-build	Skip building the test target	
o	--parallel	Run the tests in parallel	
o	--num-workers	Number of tests to execute in parallel	v
o	-l|--list-tests	Lists test methods in specifier format	
o	--show-codecov-path	Print the path of the exported code coverage JSON file	
o	-s|--specifier		
o	--filter	Run test cases matching regular expression	v
o	--skip	Skip test cases matching regular expression	v
o	--xunit-output	Path where the xUnit xml file should be generated	v
o	--test-product	Test the specified product	v
@	package
s	clean	Delete build artifacts
s	purge-cache	Purge the global repository cache
s	reset	Reset the complete cache/build directory
s	update	Update package dependencies
s	describe	Describe the current package
s	init	Initialize a new package
s	experimental-api-diff	Diagnose API-breaking changes to Swift modules in a package
s	dump-symbol-graph	Dump Symbol Graph
s	dump-pif	Dump PIF
s	dump-package	Print parsed Package.swift as JSON
s	edit	Put a package in editable mode
s	unedit	Remove a package from editable mode
s	config	Manipulate configuration of the package
s	resolve	Resolve package dependencies
s	show-dependencies	Print the resolved dependency graph
s	tools-version	Manipulate tools version of the current package
s	generate-xcodeproj	Generates an Xcode project (this command will be deprecated soon)
s	compute-checksum	Compute the checksum for a binary artifact
s	archive-source	Create a source archive for the package
s	completion-tool	Completion tool (for shell completions)
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	-Xcc	Pass a flag through to all C compiler invocations	v
o	-Xswiftc	Pass a flag through to all Swift compiler invocations	v
o	-Xlinker	Pass a flag through to all linker invocations	v
o	-c|--configuration	Build with configuration (default: debug)	v
o	--build-path	Specify build/cache directory	v
o	--cache-path	Specify the shared cache directory	v
o	--enable-repository-cache	Enable the use of a shared cache when fetching repositories (default: enabled)	
o	--disable-repository-cache	Disable the use of a shared cache when fetching repositories (default: enabled)	
o	-C|--chdir	The custom working directory that the tool should operate in	v
o	--package-path	Change working directory before any other operation	v
o	--multiroot-data-file	The path to the file containing multiroot package data. This is currently Xcode's workspace file	v
o	--enable-prefetching	Enable prefetching in resolver which will kick off parallel git cloning (default: enabled)	
o	--disable-prefetching	Disable prefetching in resolver which will kick off parallel git cloning (default: enabled)	
o	-v|--verbose	Increase verbosity of informational output	
o	--disable-sandbox	Disable using the sandbox when executing subprocesses	
o	--manifest-cache	Caching mode of Package.swift manifests	v
o	--destination	Path to the compilation destination describing JSON file	v
o	--triple	The compilation destination's target triple	v
o	--sdk	Path to the compilation destination's SDK	v
o	--toolchain	Path to the compilation destination's toolchain	v
o	--static-swift-stdlib	Link Swift stdlib statically (default: false)	
o	--no-static-swift-stdlib	Don't link Swift stdlib statically (default: false)	
o	--skip-update	Skip updating dependencies from their remote during a resolution	
o	--sanitize	Turn on runtime checks for erroneous behavior	v
o	--enable-code-coverage	Enable code coverage (default: disabled)	
o	--disable-code-coverage	Disable code coverage (default: disabled)	
o	--force-resolved-versions|--disable-automatic-resolution|--only-use-versions-from-resolved-file	Only use versions from the Package.resolved file and fail resolution if it is out-of-date	
o	--auto-index-store	Enable or disable indexing-while-building feature (default: auto)	
o	--enable-index-store	Enable indexing-while-building feature (default: auto)	
o	--disable-index-store	Disable indexing-while-building feature (default: auto)	
o	--enable-parseable-module-interfaces	Whether to enable generation of `.swiftinterface`s alongside `.swiftmodule`s	
o	--trace-resolver	Write dependency resolver trace to a file	
o	-j|--jobs	The number of jobs to spawn in parallel during the build process	v
o	--enable-build-manifest-caching	Whether to enable llbuild manifest caching (default: enabled)	
o	--disable-build-manifest-caching	Whether to disable llbuild manifest caching (default: enabled)	
o	--emit-swift-module-separately	Emit the Swift module separately from the object files	
o	--use-integrated-swift-driver	Whether to use the integrated Swift driver rather than shelling out to a separate process	
o	--experimental-explicit-module-build	Whether to use the explicit module build flow (with the integrated driver)	
o	--print-manifest-job-graph	Write the command graph for the build manifest as a graphviz file	
o	--build-system	The build system to use (default: native)	v
o	--netrc	Whether to load .netrc files for authenticating with remote servers when downloading binary…	v
o	--netrc-file	The path to the .netrc file used when `netrc` is `true`	v
=	package	-c
v	debug	
v	release	
=	package	--manifest-cache
v	shared	
v	local	
v	none	
=	package	--sanitize
v	address	
v	thread	
v	undefined	
v	scudo	
=	package	--build-system
v	native	
v	xcode	
@	package clean
o	--help|-h|-help	Show help information	
o	--version	Show the version	
@	package purge-cache
o	--help|-h|-help	Show help information	
o	--version	Show the version	
@	package reset
o	--help|-h|-help	Show help information	
o	--version	Show the version	
@	package update
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	-n|-dry-run	Display the list of dependencies that can be updated	
@	package describe
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--type	The output type	v
=	package describe	--type
v	json	
v	text	
@	package init
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--type	The package type	v
o	--name	Provide custom package name	v
=	package init	--type
v	empty	
v	library	
v	executable	
v	system-module	
v	manifest	
@	package experimental-api-diff
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--invert-baseline	Invert the baseline which is helpful for determining API additions	
a	1	0
@	package dump-symbol-graph
o	--help|-h|-help	Show help information	
o	--version	Show the version	
@	package dump-pif
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--preserve-structure	Preserve the internal structure of PIF	
@	package dump-package
o	--help|-h|-help	Show help information	
o	--version	Show the version	
@	package edit
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--revision	The revision to edit	v
o	--branch	The branch to create	v
o	--path	Create or use the checkout at this path	v
@	package unedit
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--force	Unedit the package even if it has uncommitted and unpushed changes	
a	1	0
@	package config
s	set-mirror	Set a mirror for a dependency
s	unset-mirror	Remove an existing mirror
s	get-mirror	Print mirror configuration for the given package dependency
o	--help|-h|-help	Show help information	
o	--version	Show the version	
@	package config set-mirror
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--package-url	The package dependency url	v
o	--original-url	The original url	v
o	--mirror-url	The mirror url	v
@	package config unset-mirror
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--package-url	The package dependency url	v
o	--original-url	The original url	v
o	--mirror-url	The mirror url	v
@	package config get-mirror
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--package-url	The package dependency url	v
o	--original-url	The original url	v
@	package resolve
o	--help|-h|-help	Show help information	
o	--version	Show the version	V
o	--branch	The branch to resolve at	v
o	--revision	The revision to resolve at	v
a	1	0
@	package show-dependencies
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--format	The format type	v
=	package show-dependencies	--format
v	text	
v	dot	
v	json	
v	flatlist	
@	package tools-version
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--format	The format type	v
o	--set-current	Set tools version of package to the current tools version in use	
o	--set	Set tools version of package to the given value	v
=	package tools-version	--format
v	text	
v	dot	
v	json	
v	flatlist	
@	package generate-xcodeproj
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	--xcconfig-overrides	Path to xcconfig file	v
o	--output	Path where the Xcode project should be generated	v
o	--legacy-scheme-generator	Use the legacy scheme generator	
o	--watch	Watch for changes to the Package manifest to regenerate the Xcode project	
o	--skip-extra-files	Do not add file references for extra files to the generated Xcode project	
@	package compute-checksum
o	--help|-h|-help	Show help information	
o	--version	Show the version	
@	package archive-source
o	--help|-h|-help	Show help information	
o	--version	Show the version	
o	-o|--output	The absolute or relative path for the generated source archive	v
@	package completion-tool
o	--help|-h|-help	Show help information	
o	--version	Show the version	
a	1	0
#	package completion-tool	1
v	generate-bash-script	
v	generate-zsh-script	
v	generate-fish-script	
v	list-dependencies	
v	list-executables	
