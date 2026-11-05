@	
s	deintegrate	Deintegrate CocoaPods from your project
s	cache	Manipulate the CocoaPods cache
s	list	List pods
s	setup	Setup the CocoaPods environment
s	spec	Manage pod specs
s	install	Install project dependencies according to versions from a Podfile.lock
s	env	Display pod environment
s	outdated	Show outdated project dependencies
s	init	Generate a Podfile for the current directory
s	ipc	Inter-process communication
s	plugins	Show available CocoaPods plugins
s	lib	Develop pods
s	search	Search for pods
s	repo	Manage spec-repositories
s	trunk	Interact with the CocoaPods API (e.g. publishing new specs)
s	update	Update outdated project dependencies and create new Podfile.lock
s	try	Try a Pod!
o	--silent	Show nothing	
o	--verbose	Show more debugging information	
o	--no-ansi	Show output without ANSI codes	
o	--help	Show help banner of specified command	
@	deintegrate
o	--project-directory	The path to the root of the project directory	v
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
=	deintegrate	--project-directory
t	folders
@	cache
s	clean	Remove the cache for pods
s	list	List the paths of pod caches for each known pod
o	--allow-root	Allows CocoaPods to run as root	
@	cache clean
o	--all	Remove all the cached pods without asking	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	cache list
o	--short	Only print the path relative to the cache root	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	list
o	--update	Run `pod repo update` before listing	
o	--stats	Show additional stats (like GitHub watchers and forks)	
o	--allow-root	Allows CocoaPods to run as root	
@	setup
o	--allow-root	Allows CocoaPods to run as root	
@	spec
s	edit	Edit a spec file
s	create	Create spec file stub
s	cat	Prints a spec file
s	which	Prints the path of the given spec
s	lint	Validates a spec file
o	--allow-root	Allows CocoaPods to run as root	
@	spec edit
o	--regex	Interpret the `QUERY` as a regular expression	
o	--show-all	Pick from all versions of the given podspec	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	spec create
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	spec cat
o	--regex	Interpret the `QUERY` as a regular expression	
o	--show-all	Pick from all versions of the given podspec	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	spec which
o	--regex	Interpret the `QUERY` as a regular expression	
o	--show-all	Print all versions of the given podspec	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	spec lint
o	--quick	Lint skips checks that would require to download and build the spec	
o	--allow-warnings	Lint validates even if warnings are present	
o	--subspec	Lint validates only the given subspec	v
o	--no-subspecs	Lint skips validation of subspecs	
o	--no-clean	Lint leaves the build directory intact for inspection	
o	--fail-fast	Lint stops on the first failing platform or subspec	
o	--use-libraries	Lint uses static libraries to install the spec	
o	--use-modular-headers	Lint uses modular headers during installation	
o	--use-static-frameworks	Lint uses static frameworks during installation	
o	--sources	The sources from which to pull dependent pods (defaults to https://cdn.cocoapods.org/). Multiple…	v
o	--platforms	Lint against specific platforms (defaults to all platforms supported by the podspec). Multiple…	v
o	--private	Lint skips checks that apply only to public specs	
o	--swift-version	The `SWIFT_VERSION` that should be used to lint the spec. This takes precedence over the Swift…	v
o	--skip-import-validation	Lint skips validating that the pod can be imported	
o	--skip-tests	Lint skips building and running tests during validation	
o	--test-specs	List of test specs to run	v
o	--analyze	Validate with the Xcode Static Analysis tool	
o	--configuration	Build using the given configuration (defaults to Release)	v
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
=	spec lint	--sources
v	https://cdn.cocoapods.org/	
=	spec lint	--platforms
v	ios	
v	macos	
v	ios,macos	
#	spec lint	1
d
@	install
o	--repo-update	Force running `pod repo update` before install	
o	--deployment	Disallow any changes to the Podfile or the Podfile.lock during installation	
o	--clean-install	Ignore the contents of the project cache and force a full pod installation. This only applies to…	
o	--project-directory	The path to the root of the project directory	v
o	--allow-root	Allows CocoaPods to run as root	
=	install	--project-directory
t	folders
@	env
o	--allow-root	Allows CocoaPods to run as root	
@	outdated
o	--project-directory	The path to the root of the project directory	v
o	--no-repo-update	Skip running `pod repo update` before install	
o	--allow-root	Allows CocoaPods to run as root	
=	outdated	--project-directory
t	folders
@	init
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	ipc
s	list	Lists the specifications known to CocoaPods
s	update-search-index	Updates the search index
s	podfile-json	Converts a Podfile to JSON
s	spec	Converts a podspec to JSON
s	podfile	Converts a Podfile to YAML
s	repl	The repl listens to commands on standard input
o	--allow-root	Allows CocoaPods to run as root	
@	ipc list
o	--allow-root	Allows CocoaPods to run as root	
@	ipc update-search-index
o	--allow-root	Allows CocoaPods to run as root	
@	ipc podfile-json
o	--project-directory	The path to the root of the project directory	v
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
=	ipc podfile-json	--project-directory
t	folders
#	ipc podfile-json	1
t	filepaths
@	ipc spec
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	ipc podfile
o	--project-directory	The path to the root of the project directory	v
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
=	ipc podfile	--project-directory
t	folders
#	ipc podfile	1
t	filepaths
@	ipc repl
o	--project-directory	The path to the root of the project directory	v
o	--allow-root	Allows CocoaPods to run as root	
=	ipc repl	--project-directory
t	folders
@	plugins
s	search	Search for known plugins
s	installed	List plugins installed on your machine
s	create	Creates a new plugin
s	publish	Request to add the plugin to the official plugins list
o	--allow-root	Allows CocoaPods to run as root	
@	plugins search
o	--full	Search by name author, and description	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	plugins installed
o	--allow-root	Allows CocoaPods to run as root	
@	plugins create
o	--allow-root	Allows CocoaPods to run as root	
a	2	0
@	plugins publish
o	--allow-root	Allows CocoaPods to run as root	
@	lib
s	create	Creates a new Pod
s	lint	Validates a Pod
o	--allow-root	Allows CocoaPods to run as root	
@	lib create
o	--template-url	The URL of the git repo containing a compatible template	v
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	lib lint
o	--quick	Lint skips checks that would require to download and build the spec	
o	--allow-warnings	Lint validates even if warnings are present	
o	--subspec	Lint validates only the given subspec	v
o	--no-subspecs	Lint skips validation of subspecs	
o	--no-clean	Lint leaves the build directory intact for inspection	
o	--fail-fast	Lint stops on the first failing platform or subspec	
o	--use-libraries	Lint uses static libraries to install the spec	
o	--use-modular-headers	Lint uses modular headers during installation	
o	--use-static-frameworks	Lint uses static frameworks during installation	
o	--sources	The sources from which to pull dependent pods (defaults to https://cdn.cocoapods.org/)…	v
o	--platforms	Lint against specific platforms (defaults to all platforms supported by the podspec). Multiple…	v
o	--private	Lint skips checks that apply only to public specs	
o	--swift-version	The `SWIFT_VERSION` that should be used to lint the spec. This takes precedence over the Swift…	v
o	--include-podspecs	Additional ancillary podspecs which are used for linting via :path	v
o	--external-podspecs	Additional ancillary podspecs which are used for linting via :podspec. If there are…	v
o	--skip-import-validation	Lint skips validating that the pod can be imported	
o	--skip-tests	Lint skips building and running tests during validation	
o	--test-specs	List of test specs to run	v
o	--analyze	Validate with the Xcode Static Analysis tool	
o	--configuration	Build using the given configuration (defaults to Release)	v
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
=	lib lint	--sources
v	https://cdn.cocoapods.org/	
=	lib lint	--platforms
v	ios	
v	macos	
v	ios,macos	
=	lib lint	--include-podspecs
d
=	lib lint	--external-podspecs
d
#	lib lint	1
d
@	search
o	--regex	Interpret the `QUERY` as a regular expression	
o	--simple	Search only by name	
o	--stats	Show additional stats (like GitHub watchers and forks)	
o	--web	Searches on cocoapods.org	
o	--ios	Restricts the search to Pods supported on iOS	
o	--osx	Restricts the search to Pods supported on macOS	
o	--watchos	Restricts the search to Pods supported on watchOS	
o	--tvos	Restricts the search to Pods supported on tvOS	
o	--no-pager	Do not pipe search results into a pager	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	repo
s	push	Push new specifications to a spec-repo
s	add	Add a spec repo
s	remove	Remove a spec repo
s	add-cdn	Add a spec repo backed by a CDN
s	lint	Validates all specs in a repo list
s	update	Update a spec repo
o	--allow-root	Allows CocoaPods to run as root	
@	repo push
o	--allow-warnings	Allows pushing even if there are warnings	
o	--use-libraries	Linter uses static libraries to install the spec	
o	--use-modular-headers	Lint uses modular headers during installation	
o	--sources	The sources from which to pull dependent pods (defaults to all available repos). Multiple sources…	v
o	--local-only	Does not perform the step of pushing REPO to its remote	
o	--no-private	Lint includes checks that apply only to public repos	
o	--skip-import-validation	Lint skips validating that the pod can be imported	
o	--skip-tests	Lint skips building and running tests during validation	
o	--commit-message	Add custom commit message. Opens default editor if no commit message is specified	v
o	--use-json	Convert the podspec to JSON before pushing it to the repo	
o	--swift-version	The `SWIFT_VERSION` that should be used when linting the spec. This takes precedence over the…	v
o	--no-overwrite	Disallow pushing that would overwrite an existing spec	
o	--allow-root	Allows CocoaPods to run as root	
a	2	0
=	repo push	--sources
v	https://cdn.cocoapods.org/	
#	repo push	2
d
@	repo add
o	--progress	Show the progress of cloning the spec repository	
o	--allow-root	Allows CocoaPods to run as root	
a	3	0
@	repo remove
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	repo add-cdn
o	--allow-root	Allows CocoaPods to run as root	
a	2	0
@	repo lint
o	--only-errors	Lint presents only the errors	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	repo update
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	trunk
s	push	Publish a podspec
s	deprecate	Deprecates a pod
s	delete	Deletes a version of a pod
s	add-owner	Add an owner to a pod
s	remove-owner	Remove an owner from a pod
s	me	Display information about your sessions
s	register	Manage sessions
s	info	Returns information about a Pod
o	--allow-root	Allows CocoaPods to run as root	
@	trunk push
o	--allow-warnings	Allows push even if there are lint warnings	
o	--use-libraries	Linter uses static libraries to install the spec	
o	--use-modular-headers	Lint uses modular headers during installation	
o	--swift-version	The SWIFT_VERSION that should be used to lint the spec. This takes precedence over a…	v
o	--skip-import-validation	Lint skips validating that the pod can be imported	
o	--skip-tests	Lint skips building and running tests during validation	
o	--synchronous	If validation depends on other recently pushed pods ,synchronize	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	trunk deprecate
o	--in-favor-of	The pod to deprecate this pod in favor of	v
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	trunk delete
o	--allow-root	Allows CocoaPods to run as root	
a	2	0
@	trunk add-owner
o	--allow-root	Allows CocoaPods to run as root	
a	2	0
@	trunk remove-owner
o	--allow-root	Allows CocoaPods to run as root	
a	2	0
@	trunk me
s	clean-sessions	Remove sessions
o	--allow-root	Allows CocoaPods to run as root	
@	trunk me clean-sessions
o	--all	Removes all your sessions except for the current one	
o	--allow-root	Allows CocoaPods to run as root	
@	trunk register
o	--description	An arbitrary description to easily identify your session later on	v
o	--allow-root	Allows CocoaPods to run as root	
a	2	0
@	trunk info
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
@	update
o	--sources	The sources from which to update dependent pods. Multiple sources must be comma-delimited	v
o	--exclude-pods	Pods to exclude during update. Multiple pods must be comma-delimited	v
o	--clean-install	Ignore the contents of the project cache and force a full pod installation. This only applies to…	
o	--project-directory	The path to the root of the project directory	v
o	--no-repo-update	Skip running `pod repo update` before install	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
=	update	--project-directory
t	folders
@	try
o	--podspec_name		v
o	--no-repo-update	Skip running `pod repo update` before install	
o	--allow-root	Allows CocoaPods to run as root	
a	1	0
