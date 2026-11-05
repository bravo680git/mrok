@	
s	analyze	Analyze Dart code in a directory
s	compile	Compile Dart to various formats
s	create	Create a new Dart project
s	fix	Apply automated fixes to Dart source code
s	format	Idiomatically format Dart source code
s	migrate	Perform null safety migration on a project
s	pub	Work with packages
s	run	Run a Dart program
s	test	Run tests for a project
o	-h|--help	Print this usage information	
o	-v|--verbose	Print verbose output	
o	--version	Current Dart version	
o	--enable-analytics	Enables analytics	
o	--disable-analytics	Disables analytics	
@	analyze
o	-h|--help	Print this usage information	
o	--fatal-infos	Treat info level issues as fatal	
o	--fatal-warnings	Treat warning level issues as fatal (defaults to on)	
o	--no-fatal-warnings	Do not treat warning level issues as fatal (defaults to on)	
a	1	0
#	analyze	1
t	folders
@	compile
s	aot-snapshot	Compile Dart to an AOT snapshot
s	exe	Compile Dart to a self-contained executable
s	jit-snapshot	Compile Dart to a JIT snapshot
s	js	Compile Dart to JavaScript
s	kernel	Compile Dart to a kernel snapshot
o	-h|--help	Print this usage information	
@	compile aot-snapshot
o	-h|--help	Print this usage information	
o	-o|--output	Write the output to <file-name>	v
o	--verbosity	Sets the verbosity level of the compilation	v
o	-D|--define	Define an environment declaration. To specify multiple declarations, use multiple options or use…	v
o	--enable-asserts	Enable assert statements	
o	-p|--packages	Get package locations from the specified file instead of .packages. <path> can be relative or…	v
o	--no-sound-null-safety|--sound-null-safety	Respect the nullability of types at runtime	
o	-S|--save-debugging-info	Remove debugging information from the output and save it separately to the specified file.. <path>…	v
a	1	0
=	compile aot-snapshot	-o
t	filepaths
=	compile aot-snapshot	--verbosity
v	all	Show all messages
v	error	Show only error messages
v	info	Show error, warning, and info messages
v	warning	Show only error and warning messages
=	compile aot-snapshot	-p
t	filepaths
=	compile aot-snapshot	-S
t	filepaths
@	compile exe
o	-h|--help	Print this usage information	
o	-o|--output	Write the output to <file-name>	v
o	--verbosity	Sets the verbosity level of the compilation	v
o	-D|--define	Define an environment declaration. To specify multiple declarations, use multiple options or use…	v
o	--enable-asserts	Enable assert statements	
o	-p|--packages	Get package locations from the specified file instead of .packages. <path> can be relative or…	v
o	--no-sound-null-safety|--sound-null-safety	Respect the nullability of types at runtime	
o	-S|--save-debugging-info	Remove debugging information from the output and save it separately to the specified file.. <path>…	v
a	1	0
=	compile exe	-o
t	filepaths
=	compile exe	--verbosity
v	all	Show all messages
v	error	Show only error messages
v	info	Show error, warning, and info messages
v	warning	Show only error and warning messages
=	compile exe	-p
t	filepaths
=	compile exe	-S
t	filepaths
@	compile jit-snapshot
o	-h|--help	Print this usage information	
o	-o|--output	Write the output to <file-name>	v
o	--verbosity	Sets the verbosity level of the compilation	v
a	1	0
=	compile jit-snapshot	-o
t	filepaths
=	compile jit-snapshot	--verbosity
v	all	Show all messages
v	error	Show only error messages
v	info	Show error, warning, and info messages
v	warning	Show only error and warning messages
@	compile js
o	-h|--help	Print this usage information	
o	-o|--output	Write the output to <file-name>	v
o	--verbosity	Sets the verbosity level of the compilation	v
o	-m|--minified	Generate minified output	
o	-D|--define	Define an environment declaration. To specify multiple declarations, use multiple options or use…	v
a	1	0
=	compile js	-o
t	filepaths
=	compile js	--verbosity
v	all	Show all messages
v	error	Show only error messages
v	info	Show error, warning, and info messages
v	warning	Show only error and warning messages
@	compile kernel
o	-h|--help	Print this usage information	
o	-o|--output	Write the output to <file-name>	v
o	--verbosity	Sets the verbosity level of the compilation	v
a	1	0
=	compile kernel	-o
t	filepaths
=	compile kernel	--verbosity
v	all	Show all messages
v	error	Show only error messages
v	info	Show error, warning, and info messages
v	warning	Show only error and warning messages
@	create
o	-h|--help	Print this usage information	
o	-t|--template	The project template to use	v
o	--pub	Run 'pub get' after the project has been created. Default to on	
o	--no-pub	Do not run 'pub get' after the project has been created. Default to on	
o	--force	Force project generation, even if the target directory already exists	
=	create	-t
v	console	A simple command-line application
v	package	A starting point for Dart libraries or applications
v	server-shelf	A web server built using package:shelf
v	web	A web app that uses only core Dart libraries
@	fix
o	-h|--help	Print this usage information	
o	-n|--dry-run	Preview the proposed changes but make no changes	
o	--apply	Apply the proposed changes	
@	format
o	-h|--help	Print this usage information	
o	-v|--verbose	Show all options and flags with --help	
o	-o|--output	Set where to write formatted output	v
o	--set-exit-if-changed	Return exist code 1 if there are any formatting changes	
o	--fix	Apply all style fixes	
o	--fix-doc-comments	Use triple slash for documentation comments	
o	--fix-function-typedefs	Use new syntax for function type typedefs	
o	--fix-named-default-separator	Use '=' as the separator before named parameter default values	
o	--fix-optional-const	Remove 'const' keyword inside constant context	
o	--fix-optional-new	Remove 'new' keyword	
o	--fix-single-cascade-statements	Remove unnecessary single cascades from expression statements	
o	-l|--line-length	Wrap lines longer than this. Defaults to 80	v
o	-i|--indent	Add this many spaces of leading indentation	v
o	--follow-links	Follow links to files and directories. If unset, links will be ignored	
o	--version	Show dart_style version	
o	--selection	Track selection (given as 'start:length') through formatting	
o	--stdin-name	Use this path in error messages when input is read from stdin. (defaults to 'stdin')	v
a	1	0
=	format	-l
v	80	
v	120	
#	format	1
t	filepaths,folders
@	migrate
o	-h|--help	Print this usage information	
o	-v|--verbose	Show additional command output	
o	--apply-changes	Apply the proposed null safety changes to the files on disk	
o	--ignore-errors	Attempt to perform null safety analysis even if the project has analysis errors	
o	--skip-import-check	Go ahead with migration even if some imported files have not yet been migrated	
o	--web-preview	Show and interactive preview of the proposed null safety changes in a browser window. (defaults to…	
o	--no-web-preview	Do not show and interactive preview of the proposed null safety changes in a browser window…	
o	--preview-hostname	Run the preview server on the specified hostname. If not specified, 'localhost' is used. Use 'any'…	v
o	--preview-port	Run the preview server on the specified port. If not specified, dynamically allocate a port	v
o	--summary	Output a machine-readable summary of migration changes	v
o	--ignore-exceptions	Attempt to perform null safety analysis even if exceptions occur	
o	--sdk-path	The path to the Dart SDK	v
=	migrate	--summary
t	filepaths
@	pub
s	add	Add a dependency to pubspec.yaml
s	cache	Work with the Pub system cache
s	deps	Print package dependencies
s	downgrade	Downgrade packages in a Flutter project
s	get	Get packages in a Flutter project
s	global	Work with Pub global packages
s	login	Log into pub.dev
s	logout	Log out of pub.dev
s	outdated	Analyze dependencies to find which ones can be upgraded
s	publish	Publish the current package to pub.dartlang.org
s	remove	Removes a dependency from the current package
s	upgrade	Upgrade the current package's dependencies to latest versions
s	uploader	Manage uploaders for a package on pub.dev
o	-h|--help	Print this usage information	
o	--trace	Print debugging information when an error occurs	
o	--no-trace	Do not print debugging information when an error occurs	
o	-v|--verbose	Shortcut for '--verbose=all	
@	pub add
o	-h|--help	Print this usage information	
o	-d|--dev	Adds package to the development dependencies instead	
o	--git-url	Git URL of the package	
o	--git-ref	Git branch or commit to be retrieved	
o	--git-path	Path of git package in repository	
o	--hosted-url	URL of package host server	
o	--path	Local path	
o	--sdk	SDK source for package	
o	--offline	Use cached packages instead of accessing the network	
o	--no-offline	Do not use cached packages instead of accessing the network	
o	-n|--dry-run	Report what dependencies would change but don't change any	
o	--precompile	Precompile executables in immediate dependencies	
o	--no-precompile	Do not precompile executables in immediate dependencies	
a	1	0
@	pub cache
s	add	Install a package
s	repair	Reinstall a cached package
o	-h|--help	Print this usage information	
@	pub cache add
o	-h|--help	Print this usage information	
o	--all	Install all matching versions	
o	-v|--version	Version constraint	
a	1	0
@	pub cache repair
o	-h|--help	Print this usage information	
@	pub deps
o	-h|--help	Print this usage information	
o	-s|--style	How output should be displayed	v
o	--dev	Include dev dependencies. (defaults to on)	
o	--no-dev	Do not include dev dependencies. (defaults to off)	
o	--executables	List all available executables	
=	pub deps	-s
v	compact	
v	tree	
v	list	
@	pub downgrade
o	-h|--help	Print this usage information	
o	--offline	Use cached packages instead of accessing the network	
o	--no-offline	Do not use cached packages instead of accessing the network	
o	-n|--dry-run	Report what dependencies would change but don't change any	
@	pub get
o	-h|--help	Print this usage information	
o	--offline	Use cached packages instead of accessing the network	
o	--no-offline	Do not use cached packages instead of accessing the network	
o	-n|--dry-run	Report what dependencies would change but don't change any	
o	--precompile	Precompile executables in immediate dependencies	
o	--no-precompile	Do not precompile executables in immediate dependencies	
@	pub global
s	activate	Make a package's executables globally available
s	deactivate	Remove a previously activated package
s	list	List globally activated packages
s	run	Run an executable from a globally activated package
o	-h|--help	Print this usage information	
@	pub global activate
o	-h|--help	Print this usage information	
o	-s|--source	The source used to find the package	v
o	--no-executables	Do not put executables on PATH	
o	-x|--executable	Executable(s) to place on PATH	
o	--overwrite	Overwrite executables from other packages with the same name	
o	-u|--hosted-url	A custom pub server URL for the package. Only applies when using the 'hosted' source	v
=	pub global activate	-s
v	git	
v	hosted	
v	path	
@	pub global deactivate
o	-h|--help	Print this usage information	
@	pub global list
o	-h|--help	Print this usage information	
@	pub global run
o	-h|--help	Print this usage information	
o	--enable-asserts	Enable assert statements	
o	--no-enable-asserts	Do not enable assert statements	
o	--enable-experiment	Runs the executable in a VM with the given experiments enabled. (Will disable snapshotting…	v
o	--sound-null-safety	Override the default null safety execution mode	
o	--no-sound-null-safety	Do not override the default null safety execution mode	
@	pub login
o	-h|--help	Print this usage information	
@	pub logout
o	-h|--help	Print this usage information	
@	pub outdated
o	-h|--help	Print this usage information	
o	--color	Color the the output. Defaults to color when connected to a terminal, and no-color otherwise	
o	--no-color	Do not color the output. Defaults to color when connected to a terminal, and no-color otherwise	
o	--dependency-overrides	Show resolutions with 'dependency_overrides'. (defaults to on)	
o	--no-dependency-overrides	Do not show resolutions with 'dependency_overrides'. (defaults to on)	
o	--json	Output the results sing a JSON format	
o	--mode	Highlight versions with PROPERTY. Only packages missing the PROPERTY will be included unless…	v
o	--prereleases	Include prereleases in latest version. (defaults to on in --mode=null-safety)	
o	--no-prereleases	Do not include prereleases in latest version. (defaults to off in --mode=null-safety)	
o	--show-all	Include dependencies that are already fulfilling --mode	
o	--no-show-all	Do not include dependencies that are already fulfilling --mode	
o	--transitive|--no-transitive	Show transitive dependencies. (defaults to off in --mode=null-safety	
=	pub outdated	--mode
v	outdated	
v	null-safety	
@	pub publish
o	-h|--help	Print this usage information	
o	-n|--dry-run	Report what dependencies would change but don't change any	
o	-f|--force	Publish without confirmation if there are no errors	
@	pub remove
o	-h|--help	Print this usage information	
o	--offline	Use cached packages instead of accessing the network	
o	--no-offline	Do not use cached packages instead of accessing the network	
o	-n|--dry-run	Report what dependencies would change but don't change any	
o	--precompile	Precompile executables in immediate dependencies	
o	--no-precompile	Do not precompile executables in immediate dependencies	
@	pub upgrade
o	-h|--help	Print this usage information	
o	--offline	Use cached packages instead of accessing the network	
o	--no-offline	Do not use cached packages instead of accessing the network	
o	-n|--dry-run	Report what dependencies would change but don't change any	
o	--precompile	Precompile executables in immediate dependencies	
o	--no-precompile	Do not precompile executables in immediate dependencies	
o	--null-safety	Upgrade constraints in pubspec.yaml to null-safety versions	
o	--major-versions	Upgrades packages to their latest resolvable versions, and updates pubspec.yaml	
@	pub uploader
o	-h|--help	Print this usage information	
o	--package	The package whose uploaders will be modified. (defaults to the current package)	
@	run
o	-h|--help	Print this usage information	
o	--observe	The observe flag is a convenience flag used to run a program with a set of common options. Useful…	v
o	--enable-vm-service	Enables the VM service and listens on the specified port for connections (default port number is…	v
o	--pause-isolates-on-exit|--no-pause-isolates-on-exit	Pause isolates on exit when running with --enable-vm-service	
o	--pause-isolates-on-unhandled-exceptions	Pause isolates when an unhandled exception is encountered when running with --enable-vm-service	
o	--no-pause-isolates-on-unhandled-exceptions	Do not pause isolates when an unhandled exception is encountered when running with…	
o	--warn-on-pause-with-no-debugger	Print a warning when an isolate pauses with no attahed debugger when running with…	
o	--no-warn-on-pause-with-no-debugger	Do not print a warning when an isolate pauses with no attahed debugger when running with…	
o	--pause-isolates-on-start	Pause isolates on start when running with --enable-vm-service	
o	--no-pause-isolates-on-start	Do not pause isolates on start when running with --enable-vm-service	
o	--enable-asserts	Enable assert statements	
o	--no-enable-asserts	Do not enable assert statements	
o	--verbosity	Sets the verbosity level of the compilation	v
o	-D|--define	Define an environment declaration. To specify multiple declarations, use multiple options or use…	v
o	--disable-service-auth-codes	Disables the requirement for an authentication code to communicate with the VM service…	
o	--enable-service-port-fallback	When the VM service is told to bind to a particular port, fallback to 0 if it fails to bind…	
o	--namespace	The path to a directory that dart:io calls will treat as the root of the filesystem	v
o	--root-certs-file	The The path to a file containing the trusted root certificates to use for secure socket connections	v
o	--root-certs-cache	The path to a cache directory containing the trusted root certificates to use for secure socket…	v
o	--trace-loading	Enables tracing of library and script loading	
o	--enable-experiment	Enable one or more experimental features (see dart.dev/go/experiments	v
=	run	--verbosity
v	all	Show all messages
v	error	Show only error messages
v	info	Show error, warning, and info messages
v	warning	Show only error and warning messages
=	run	--namespace
t	folders
=	run	--root-certs-file
t	filepaths
=	run	--root-certs-cache
t	folders
=	run	--enable-experiment
v	const-functions	Allow more of the Dart language to be executed in const expressions
v	extension-methods	Extension methods (no-op - enabled by default)
v	extension-types	Extension types
v	generic-metadata	Allow annotations to accept type arguments; also allow generic function types as type arguments
v	non-nullable	Non-nullable by default. (no-op - on by default)
v	nonfunction-type-aliases	Type aliases define a <type>, not just <functionType>. (no-op - enabled by default)
v	triple-shift	Triple-shift operator
v	value-class	Value classes
v	variance	Sound variance
@	test
o	-h|--help	Print this usage information	
