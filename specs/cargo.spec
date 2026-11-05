@	
s	bench	Execute all benchmarks of a local package
s	build|b	Compile a local package and all of its dependencies
s	check|c	Check a local package and all of its dependencies for errors
s	clean	Remove artifacts that cargo has generated in the past
s	config	Inspect configuration values
s	doc|d	Build a package's documentation
s	fetch	Fetch dependencies of a package from the network
s	fix	Automatically fix lint warnings reported by rustc
s	generate-lockfile	Generate the lockfile for a package
s	init	Create a new cargo package in an existing directory
s	install	Install a Rust binary. Default location is $HOME/.cargo/bin
s	locate-project	Print a JSON representation of a Cargo.toml file's location
s	login	Save an api token from the registry locally. If token is not specified, it will be read from stdin
s	logout	Remove an API token from the registry locally
s	metadata	Output the resolved dependencies of a package, the concrete used versions including overrides, in…
s	new	Create a new cargo package at <path>
s	owner	Manage the owners of a crate on the registry
s	package	Assemble the local package into a distributable tarball
s	pkgid	Print a fully qualified package specification
s	publish	Upload a package to the registry
s	report	Generate and display various kinds of reports
s	run|r	Run a binary or example of the local package
s	rustc	Compile a package, and pass extra options to the compiler
s	rustdoc	Build a package's documentation, using specified custom flags
s	search	Search packages in crates.io
s	test|t	Execute all unit and integration tests and build examples of a local package
s	tree	Display a tree visualization of a dependency graph
s	uninstall	Remove a Rust binary
s	update	Update dependencies as recorded in the local lock file
s	vendor	Vendor all dependencies for a project locally
s	verify-project	Check correctness of crate manifest
s	version	Show version information
s	yank	Remove a pushed crate from the index
s	help	Print this message or the help of the given subcommand(s)
s	add	Add dependencies to a Cargo.toml manifest file
s	remove|rm	Remove dependencies from a Cargo.toml manifest file
o	--explain	Run `rustc --explain CODE`	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-h|--help	Print help information	
o	-V|--version	Print version info and exit	
o	--list	List installed commands	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	-q|--quiet	Do not print cargo log messages	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=		--color
v	always	
v	never	
v	auto	
=		--config
d
@	bench
o	--bin	Benchmark only the specified binary	v
o	--example	Benchmark only the specified example	v
o	--test	Benchmark only the specified test target	v
o	--bench	Benchmark only the specified bench target	v
o	-p|--package	Package to run benchmarks for	v
o	--exclude	Exclude packages from the benchmark	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--profile	Build artifacts with the specified profile	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Build for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--lib	Benchmark only this package's library	
o	--bins	Benchmark all binaries	
o	--examples	Benchmark all examples	
o	--tests	Benchmark all tests	
o	--benches	Benchmark all benches	
o	--all-targets	Benchmark all targets	
o	--no-run	Compile, but don't run benchmarks	
o	--workspace	Benchmark all packages in the workspace	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--ignore-rust-version	Ignore `rust-version` specification in packages	
o	--no-fail-fast	Run all benchmarks regardless of failure	
o	--unit-graph	Output build graph in JSON (unstable)	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
a	2	1
=	bench	--bin
d
=	bench	--example
d
=	bench	--test
d
=	bench	--bench
d
=	bench	-p
d
=	bench	--exclude
d
=	bench	--features
d
=	bench	--target
d
=	bench	--manifest-path
d
=	bench	--color
v	auto	
v	always	
v	never	
=	bench	--config
d
@	build
o	-p|--package	Package to build (see `cargo help pkgid`)	v
o	--exclude	Exclude packages from the build	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--bin	Build only the specified binary	v
o	--example	Build only the specified example	v
o	--test	Build only the specified test target	v
o	--bench	Build only the specified bench target	v
o	--profile	Build artifacts with the specified profile	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Build for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--out-dir	Copy final artifacts to this directory (unstable)	v
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--workspace	Build all packages in the workspace	
o	--lib	Build only this package's library	
o	--bins	Build all binaries	
o	--examples	Build all examples	
o	--tests	Build all tests	
o	--benches	Build all benches	
o	--all-targets	Build all targets	
o	-r|--release	Build artifacts in release mode, with optimizations	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--ignore-rust-version	Ignore `rust-version` specification in packages	
o	--build-plan	Output the build plan in JSON (unstable)	
o	--unit-graph	Output build graph in JSON (unstable)	
o	--future-incompat-report	Outputs a future incompatibility report at the end of the build	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
=	build	-p
d
=	build	--exclude
d
=	build	--bin
d
=	build	--example
d
=	build	--test
d
=	build	--bench
d
=	build	--features
d
=	build	--target
d
=	build	--manifest-path
d
=	build	--color
v	auto	
v	always	
v	never	
=	build	--config
d
@	check
o	-p|--package	Package(s) to check	v
o	--exclude	Exclude packages from the check	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--bin	Check only the specified binary	v
o	--example	Check only the specified example	v
o	--test	Check only the specified test target	v
o	--bench	Check only the specified bench target	v
o	--profile	Check artifacts with the specified profile	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Check for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--workspace	Check all packages in the workspace	
o	--lib	Check only this package's library	
o	--bins	Check all binaries	
o	--examples	Check all examples	
o	--tests	Check all tests	
o	--benches	Check all benches	
o	--all-targets	Check all targets	
o	-r|--release	Check artifacts in release mode, with optimizations	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--ignore-rust-version	Ignore `rust-version` specification in packages	
o	--unit-graph	Output build graph in JSON (unstable)	
o	--future-incompat-report	Outputs a future incompatibility report at the end of the build	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
=	check	-p
d
=	check	--exclude
d
=	check	--bin
d
=	check	--example
d
=	check	--test
d
=	check	--bench
d
=	check	--features
d
=	check	--target
d
=	check	--manifest-path
d
=	check	--color
v	auto	
v	always	
v	never	
=	check	--config
d
@	clean
o	-p|--package	Package to clean artifacts for	v
o	--manifest-path	Path to Cargo.toml	v
o	--target	Target triple to clean output for	v
o	--target-dir	Directory for all generated artifacts	v
o	--profile	Clean artifacts of the specified profile	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-r|--release	Whether or not to clean release artifacts	
o	--doc	Whether or not to clean just the documentation directory	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	clean	-p
d
=	clean	--manifest-path
d
=	clean	--target
d
=	clean	--color
v	auto	
v	always	
v	never	
=	clean	--config
d
@	config
s	get	
s	help	Print this message or the help of the given subcommand(s)
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	config	--color
v	auto	
v	always	
v	never	
=	config	--config
d
@	config get
o	--format	Display format	v
o	--merged	Whether or not to merge config values	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	--version	Print version information	
o	--show-origin	Display where the config value is defined	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	config get	--format
v	toml	
v	json	
v	json-value	
=	config get	--merged
v	yes	
v	no	
=	config get	--color
v	auto	
v	always	
v	never	
=	config get	--config
d
@	config help
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	--version	Print version information	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	config help	--color
v	auto	
v	always	
v	never	
=	config help	--config
d
@	doc
o	-p|--package	Package to document	v
o	--exclude	Exclude packages from the build	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--bin	Document only the specified binary	v
o	--example	Document only the specified example	v
o	--profile	Build artifacts with the specified profile	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Build for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--open	Opens the docs in a browser after the operation	
o	--workspace	Document all packages in the workspace	
o	--no-deps	Don't build documentation for dependencies	
o	--document-private-items	Document private items	
o	--lib	Document only this package's library	
o	--bins	Document all binaries	
o	--examples	Document all examples	
o	-r|--release	Build artifacts in release mode, with optimizations	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--ignore-rust-version	Ignore `rust-version` specification in packages	
o	--unit-graph	Output build graph in JSON (unstable)	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
=	doc	-p
d
=	doc	--exclude
d
=	doc	--bin
d
=	doc	--example
d
=	doc	--features
d
=	doc	--target
d
=	doc	--manifest-path
d
=	doc	--config
d
@	fetch
o	--manifest-path	Path to Cargo.toml	v
o	--target	Fetch dependencies for the target triple	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	fetch	--manifest-path
d
=	fetch	--target
d
=	fetch	--color
v	always	
v	never	
v	auto	
=	fetch	--config
d
@	fix
o	-p|--package	Package(s) to fix	v
o	--exclude	Exclude packages from the fixes	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--bin	Fix only the specified binary	v
o	--example	Fix only the specified example	v
o	--test	Fix only the specified test target	v
o	--bench	Fix only the specified bench target	v
o	--profile	Build artifacts with the specified profile	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Fix for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--workspace	Fix all packages in the workspace	
o	--lib	Fix only this package's library	
o	--bins	Fix all binaries	
o	--examples	Fix all examples	
o	--tests	Fix all tests	
o	--benches	Fix all benches	
o	--all-targets	Fix all targets (default)	
o	-r|--release	Fix artifacts in release mode, with optimizations	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--broken-code	Fix code even if it already has compiler errors	
o	--edition	Fix in preparation for the next edition	
o	--edition-idioms	Fix warnings to migrate to the idioms of an edition	
o	--allow-no-vcs	Fix code even if a VCS was not detected	
o	--allow-dirty	Fix code even if the working directory is dirty	
o	--allow-staged	Fix code even if the working directory has staged changes	
o	--ignore-rust-version	Ignore `rust-version` specification in packages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
=	fix	-p
d
=	fix	--exclude
d
=	fix	--bin
d
=	fix	--example
d
=	fix	--test
d
=	fix	--bench
d
=	fix	--features
d
=	fix	--target
d
=	fix	--manifest-path
d
=	fix	--color
v	always	
v	never	
v	auto	
=	fix	--config
d
@	generate-lockfile
o	--manifest-path	Path to Cargo.toml	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	generate-lockfile	--manifest-path
d
=	generate-lockfile	--color
v	always	
v	never	
v	auto	
=	generate-lockfile	--config
d
@	init
o	--registry	Registry to use	v
o	--vcs	Initialize a new repository for the given version control system (git, hg, pijul, or fossil) or do…	v
o	--edition	Edition to set for the crate generated	v
o	--name	Set the resulting package name, defaults to the directory name	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--bin	Use a binary (application) template [default]	
o	--lib	Use a library template	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	init	--vcs
v	git	Initialize with Git
v	hg	Initialize with Mercurial
v	pijul	Initialize with Pijul
v	fossil	Initialize with Fossil
v	none	Initialize with no VCS
=	init	--edition
v	2015	2015 edition
v	2018	2018 edition
v	2021	2021 edition
=	init	--color
v	always	
v	never	
v	auto	
=	init	--config
d
@	install
o	--version	Specify a version to install	v
o	--git	Git URL to install the specified crate from	v
o	--branch	Branch to use when installing from git	v
o	--tag	Tag to use when installing from git	v
o	--rev	Specific commit to use when installing from git	v
o	--path	Filesystem path to local crate to install	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--features	Space or comma separated list of features to activate	v
o	--profile	Install artifacts with the specified profile	v
o	--bin	Install only the specified binary	v
o	--example	Install only the specified example	v
o	--target	Build for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--root	Directory to install packages into	v
o	--index	Registry index to install from	v
o	--registry	Registry to use	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--list	List all installed packages and their versions	
o	-f|--force	Force overwriting existing crates or binaries	
o	--no-track	Do not save tracking information	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--debug	Build in debug mode instead of release mode	
o	--bins	Install all binaries	
o	--examples	Install all examples	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
a	1	1
=	install	--path
t	folders
=	install	--features
d
=	install	--bin
d
=	install	--example
d
=	install	--target
d
=	install	--color
v	always	
v	never	
v	auto	
=	install	--config
d
#	install	1
d
@	locate-project
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Output representation [possible values: json, plain]	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--workspace	Locate Cargo.toml of the workspace root	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	locate-project	--manifest-path
d
=	locate-project	--color
v	always	
v	never	
v	auto	
=	locate-project	--config
d
@	login
o	--registry	Registry to use	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	login	--color
v	always	
v	never	
v	auto	
=	login	--config
d
@	logout
o	--registry	Registry to use	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	logout	--color
v	always	
v	never	
v	auto	
=	logout	--config
d
@	metadata
o	--features	Space or comma separated list of features to activate	v
o	--filter-platform	Only include resolve dependencies matching the given target-triple	v
o	--manifest-path	Path to Cargo.toml	v
o	--format-version	Format version	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--no-deps	Output information only about the workspace members and don't fetch dependencies	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	metadata	--features
d
=	metadata	--manifest-path
d
=	metadata	--format-version
v	1	
=	metadata	--color
v	always	
v	never	
v	auto	
=	metadata	--config
d
@	new
o	--registry	Registry to use	v
o	--vcs	Initialize a new repository for the given version control system (git, hg, pijul, or fossil) or do…	v
o	--edition	Edition to set for the crate generated	v
o	--name	Set the resulting package name, defaults to the directory name	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--bin	Use a binary (application) template [default]	
o	--lib	Use a library template	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	new	--vcs
v	git	Initialize with Git
v	hg	Initialize with Mercurial
v	pijul	Initialize with Pijul
v	fossil	Initialize with Fossil
v	none	Initialize with no VCS
=	new	--edition
v	2015	2015 edition
v	2018	2018 edition
v	2021	2021 edition
=	new	--color
v	always	
v	never	
v	auto	
=	new	--config
d
#	new	1
t	folders
@	owner
o	-a|--add	Name of a user or team to invite as an owner	v
o	-r|--remove	Name of a user or team to remove as an owner	v
o	--index	Registry index to modify owners for	v
o	--token	API token to use when authenticating	v
o	--registry	Registry to use	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-l|--list	List owners of a crate	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	owner	--color
v	always	
v	never	
v	auto	
=	owner	--config
d
@	package
o	--target	Build for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--features	Space or comma separated list of features to activate	v
o	-p|--package	Package(s) to assemble	v
o	--exclude	Don't assemble specified packages	v
o	--manifest-path	Path to Cargo.toml	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-l|--list	Print files included in a package without making one	
o	--no-verify	Don't verify the contents by building them	
o	--no-metadata	Ignore warnings about a lack of human-usable metadata	
o	--allow-dirty	Allow dirty working directories to be packaged	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--workspace	Assemble all packages in the workspace	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	package	--target
d
=	package	--features
d
=	package	-p
d
=	package	--exclude
d
=	package	--manifest-path
d
=	package	--color
v	always	
v	never	
v	auto	
=	package	--config
d
@	pkgid
o	-p|--package	Argument to get the package ID specifier for	v
o	--manifest-path	Path to Cargo.toml	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	pkgid	-p
d
=	pkgid	--manifest-path
d
=	pkgid	--color
v	always	
v	never	
v	auto	
=	pkgid	--config
d
#	pkgid	1
d
@	publish
o	--index	Registry index URL to upload the package to	v
o	--token	Token to use when uploading	v
o	--target	Build for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	-p|--package	Package to publish	v
o	--manifest-path	Path to Cargo.toml	v
o	--features	Space or comma separated list of features to activate	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--registry	Registry to publish to	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--no-verify	Don't verify the contents by building them	
o	--allow-dirty	Allow dirty working directories to be packaged	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--dry-run	Perform all checks without uploading	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	publish	--target
d
=	publish	-p
d
=	publish	--manifest-path
d
=	publish	--features
d
=	publish	--color
v	always	
v	never	
v	auto	
=	publish	--config
d
@	report
s	future-incompatibilities	Reports any crates which will eventually stop compiling
s	help	Print this message or the help of the given subcommand(s)
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	report	--color
v	always	
v	never	
v	auto	
=	report	--config
d
@	report future-incompatibilities
o	--id	Identifier of the report generated by a Cargo command invocation	v
o	-p|--package	Package to display a report for	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	--version	Print version information	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	report future-incompatibilities	-p
d
=	report future-incompatibilities	--color
v	always	
v	never	
v	auto	
=	report future-incompatibilities	--config
d
@	report help
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	--version	Print version information	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	report help	--color
v	always	
v	never	
v	auto	
=	report help	--config
d
@	run
o	--bin	Name of the bin target to run	v
o	--example	Name of the example target to run	v
o	-p|--package	Package with the target to run	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--profile	Build artifacts with the specified profile	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Build for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-r|--release	Build artifacts in release mode, with optimizations	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--unit-graph	Output build graph in JSON (unstable)	
o	--ignore-rust-version	Ignore `rust-version` specification in packages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
a	1	1
=	run	--bin
d
=	run	--example
d
=	run	-p
d
=	run	--features
d
=	run	--target
d
=	run	--manifest-path
d
=	run	--color
v	always	
v	never	
v	auto	
=	run	--config
d
@	rustc
o	-p|--package	Package to build	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--bin	Build only the specified binary	v
o	--example	Build only the specified example	v
o	--test	Build only the specified test target	v
o	--bench	Build only the specified bench target	v
o	--profile	Build artifacts with the specified profile	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Target triple which compiles will be for	v
o	--print	Output compiler information without compiling	v
o	--crate-type	Comma separated list of types of crates for the compiler to emit	v
o	--target-dir	Directory for all generated artifacts	v
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--lib	Build only this package's library	
o	--bins	Build all binaries	
o	--examples	Build all examples	
o	--tests	Build all tests	
o	--benches	Build all benches	
o	--all-targets	Build all targets	
o	-r|--release	Build artifacts in release mode, with optimizations	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--unit-graph	Output build graph in JSON (unstable)	
o	--ignore-rust-version	Ignore `rust-version` specification in packages	
o	--future-incompat-report	Outputs a future incompatibility report at the end of the build	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
a	1	1
=	rustc	-p
d
=	rustc	--bin
d
=	rustc	--example
d
=	rustc	--test
d
=	rustc	--bench
d
=	rustc	--features
d
=	rustc	--target
d
=	rustc	--manifest-path
d
=	rustc	--color
v	always	
v	never	
v	auto	
=	rustc	--config
d
@	rustdoc
o	-p|--package	Package to document	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--bin	Build only the specified binary	v
o	--example	Build only the specified example	v
o	--test	Build only the specified test target	v
o	--bench	Build only the specified bench target	v
o	--profile	Build artifacts with the specified profile	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Build for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--open	Opens the docs in a browser after the operation	
o	--lib	Build only this package's library	
o	--bins	Build all binaries	
o	--examples	Build all examples	
o	--tests	Build all tests	
o	--benches	Build all benches	
o	--all-targets	Build all targets	
o	-r|--release	Build artifacts in release mode, with optimizations	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--unit-graph	Output build graph in JSON (unstable)	
o	--ignore-rust-version	Ignore `rust-version` specification in packages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
a	1	1
=	rustdoc	-p
d
=	rustdoc	--bin
d
=	rustdoc	--example
d
=	rustdoc	--test
d
=	rustdoc	--bench
d
=	rustdoc	--features
d
=	rustdoc	--target
d
=	rustdoc	--manifest-path
d
=	rustdoc	--color
v	always	
v	never	
v	auto	
=	rustdoc	--config
d
@	search
o	--index	Registry index URL to upload the package to	v
o	--limit	Limit the number of results (default: 10, max: 100)	v
o	--registry	Registry to use	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	1
=	search	--config
d
#	search	1
d
@	test
o	--bin	Test only the specified binary	v
o	--example	Test only the specified example	v
o	--test	Test only the specified test target	v
o	--bench	Test only the specified bench target	v
o	-p|--package	Package to run tests for	v
o	--exclude	Exclude packages from the test	v
o	-j|--jobs	Number of parallel jobs, defaults to # of CPUs	v
o	--profile	Build artifacts with the specified profile	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Build for the target triple	v
o	--target-dir	Directory for all generated artifacts	v
o	--manifest-path	Path to Cargo.toml	v
o	--message-format	Error format	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Display one character per test instead of one line	
o	--lib	Test only this package's library unit tests	
o	--bins	Test all binaries	
o	--examples	Test all examples	
o	--tests	Test all tests	
o	--benches	Test all benches	
o	--all-targets	Test all targets	
o	--doc	Test only this library's documentation	
o	--no-run	Compile, but don't run tests	
o	--no-fail-fast	Run all tests regardless of failure	
o	--workspace	Test all packages in the workspace	
o	-r|--release	Build artifacts in release mode, with optimizations	
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--ignore-rust-version	Ignore `rust-version` specification in packages	
o	--unit-graph	Output build graph in JSON (unstable)	
o	--future-incompat-report	Outputs a future incompatibility report at the end of the build	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	--timings	Timing output formats (unstable)	
a	2	1
=	test	--bin
d
=	test	--example
d
=	test	--test
d
=	test	--bench
d
=	test	-p
d
=	test	--exclude
d
=	test	--features
d
=	test	--target
d
=	test	--manifest-path
d
=	test	--color
v	auto	
v	always	
v	never	
=	test	--config
d
@	tree
o	--manifest-path	Path to Cargo.toml	v
o	-p|--package	Package to be used as the root of the tree	v
o	--exclude	Exclude specific workspace members	v
o	--features	Space or comma separated list of features to activate	v
o	--target	Filter dependencies matching the given target-triple (default host platform). Pass `all` to…	v
o	-e|--edges	The kinds of dependencies to display (features, normal, build, dev, all, no-normal, no-build…	v
o	-i|--invert	Invert the tree direction and focus on the given package	v
o	--prune	Prune the given package from the display of the dependency tree	v
o	--depth	Maximum display depth of the dependency tree	v
o	--prefix	Change the prefix (indentation) of how each entry is displayed	v
o	--charset	Character set to use in output: utf8, ascii	v
o	-f|--format	Format string used for printing dependencies	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--workspace	Display the tree for all packages in the workspace	
o	-a|--all		
o	--all-targets		
o	--all-features	Activate all available features	
o	--no-default-features	Do not activate the `default` feature	
o	--no-dev-dependencies		
o	--no-indent		
o	--prefix-depth		
o	--no-dedupe	Do not de-duplicate (repeats all shared dependencies)	
o	-d|--duplicates	Show only dependencies which come in multiple versions (implies -i)	
o	-V|--version		
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	tree	--manifest-path
d
=	tree	-p
d
=	tree	--exclude
d
=	tree	--features
d
=	tree	--target
v	all	
d
=	tree	-e
v	features	
v	normal	
v	build	
v	dev	
v	all	
v	no-normal	
v	no-build	
v	no-dev	
v	no-proc-macro	
=	tree	-i
d
=	tree	--prune
d
=	tree	--prefix
v	depth	
v	indent	
v	none	
=	tree	--charset
v	utf8	
v	ascii	
=	tree	--color
v	auto	
v	always	
v	never	
=	tree	--config
d
@	uninstall
o	-p|--package	Package to uninstall	v
o	--bin	Only uninstall the binary NAME	v
o	--root	Directory to uninstall packages from	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	1
=	uninstall	--color
v	auto	
v	always	
v	never	
=	uninstall	--config
d
#	uninstall	1
g	bash -c 'cargo install --list | \grep -E "^[a-zA-Z\-]+\sv" | cut -d '\'' '\'' -f 1'	\n
@	update
o	-p|--package	Package to update	v
o	--precise	Update a single dependency to exactly PRECISE when used with -p	v
o	--manifest-path	Path to Cargo.toml	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-w|--workspace	Only update the workspace packages	
o	--aggressive	Force updating all dependencies of SPEC as well when used with -p	
o	--dry-run	Don't actually write the lockfile	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	update	-p
d
=	update	--manifest-path
d
=	update	--color
v	always	
v	never	
v	auto	
=	update	--config
d
@	vendor
o	--manifest-path	Path to Cargo.toml	v
o	-s|--sync	Additional `Cargo.toml` to sync and vendor	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--no-delete	Don't delete older crates in the vendor directory	
o	--respect-source-config	Respect `[source]` config in `.cargo/config`	
o	--versioned-dirs	Always include version in subdir name	
o	--no-merge-sources		
o	--relative-path		
o	--only-git-deps		
o	--disallow-duplicates		
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	vendor	--manifest-path
d
=	vendor	--color
v	always	
v	never	
v	auto	
=	vendor	--config
d
@	verify-project
o	--manifest-path	Path to Cargo.toml	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	verify-project	--manifest-path
d
=	verify-project	--color
v	always	
v	never	
v	auto	
=	verify-project	--config
d
@	version
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
=	version	--color
v	always	
v	never	
v	auto	
=	version	--config
d
@	yank
o	--vers	The version to yank or un-yank	v
o	--index	Registry index to yank from	v
o	--token	API token to use when authenticating	v
o	--registry	Registry to use	v
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-q|--quiet	Do not print cargo log messages	
o	--undo	Undo a yank, putting a version back into the index	
o	-h|--help	Print help information	
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	yank	--color
v	always	
v	never	
v	auto	
=	yank	--config
d
@	help
o	--color	Coloring: auto, always, never	v
o	--config	Override a configuration value	v
o	-Z	Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for details	v
o	-v|--verbose	Use verbose output (-vv very verbose/build.rs output)	
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
a	1	0
=	help	--color
v	always	
v	never	
v	auto	
=	help	--config
d
@	add
o	--no-default-features	Disable the default features	
o	--default-features	Re-enable the default features	
o	-F|--features	Space or comma separated list of features to activate	
o	--optional	Mark the dependency as optional	
o	-v|--verbose	Use verbose output	
o	--no-optional	Mark the dependency as required	
o	--color		v
o	--rename	Rename the dependency	v
o	--frozen	Require Cargo.lock and cache are up to date	
o	--manifest-path	Path to Cargo.toml	
o	--locked	Require Cargo.lock is up to date	
o	-p|--package	Package to modify	v
o	--offline	Run without accessing the network	
o	-q|--quiet	Do not print cargo log messages	
o	--dry-run	Don't actually write the manifest	
o	-h|--help	Print help information	
o	--path	Filesystem path to local crate to add	v
o	--git	Git repository location	v
o	--branch	Git branch to download the crate from	v
o	--tag	Git tag to download the crate from	v
o	--rev	Git reference to download the crate from	v
o	--registry	Package registry for this dependency	v
o	--dev	Add as development dependency	
o	--build	Add as build dependency	
o	--target	Add as dependency to the given target platform	v
a	1	1
=	add	--color
v	auto	
v	always	
v	never	
=	add	-p
d
=	add	--path
t	folders
=	add	--target
d
#	add	1
d
@	remove
o	--dev	Remove as development dependency	
o	--build	Remove as build dependency	
o	--target	Remove as dependency to the given target platform	v
o	-p|--package	Package to remove from	v
o	--manifest-path	Path to Cargo.toml	
o	-q|--quiet	Do not print cargo log messages	
o	--dry-run	Don't actually write the manifest	
o	-v|--verbose	Use verbose output	
o	--color		v
o	--frozen	Require Cargo.lock and cache are up to date	
o	--locked	Require Cargo.lock is up to date	
o	--offline	Run without accessing the network	
o	-h|--help	Print help information	
a	1	1
=	remove	--target
d
=	remove	-p
d
=	remove	--color
v	auto	
v	always	
v	never	
#	remove	1
d
