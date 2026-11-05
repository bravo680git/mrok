@	
s	init	Create or reinitialize an empty workspace
s	new	Create a new workspace from a template
s	config	Global config management
s	scope-config	Scope config management
s	login	Log in to Bit cloud
s	logout	Log the CLI out of Bit
s	doctor	Diagnose a bit workspace
s	completion	Enable bash/zsh-completion shortcuts for commands and options
s	cli	EXPERIMENTAL: Enters bit cli program and generates commands list
s	help|$0	Shows help
s	clear-cache|cc	Clears Bit's cache from current working machine
s	remote	Manage set of tracked bit scope(s)
s	remove|rm	Remove component(s) from the local workspace
s	import	Import components from their remote scopes to the local workspace
s	pack	Create tar for npm publish
s	deprecate|d	Deprecate a component
s	undeprecate	Undeprecate a deprecated component (local/remote).
s	rename	Rename a component
s	fork	Create a new component forked from an existing one (copies source files and configs)
s	export|e	Export components from the workspace to remote scopes
s	dependents	Show dependents of the given component
s	show	Display the component's essential information
s	deps|dependencies	Manage dependencies
s	log	Show components(s) version history
s	add	Add any subset of files to be tracked as a component(s)
s	move|mv	Move a component to a different filesystem path
s	diff	Show the diff between the components' current source files and config, and their latest snapshot…
s	envs|env	List all components maintained by the workspace and their corresponding envs
s	start|c	Run the UI/development server
s	ui-build	Build production assets for deployment
s	checkout|U	Switch between component versions or remove local changes
s	install|in	Installs workspace dependencies
s	uninstall|un	Uninstall dependencies.
s	update|up	Update dependencies.
s	link	Create links in the node_modules directory, to core aspects and to components in the workspace
s	component-issues	List available component-issues
s	tag|t	Create an immutable and exportable component snapshot, tagged with a release version.
s	reset	Revert tagged or snapped versions for component(s)
s	merge	Merge changes of the remote head into local and creates snaps for merged components
s	create	Create a new component using a template
s	templates	List available templates for "bit create" and "bit new"
s	build	Run set of tasks for build. By default, only new and modified components are built
s	artifacts	List and download component artifacts
s	refactor	Source code refactoring / codemod
s	status|s	Present the current status of components in the workspace, including indication of detected issues
s	compile	Compile components in the workspace
s	test|at	Test components in the workspace. By default only runs tests for new and modified components.
s	schema	Shows the API schema of the specified component/s
s	check-types	Check typescript types
s	aspect	EXPERIMENTAL. Manage aspects
s	eject|E	Remove component from the workspace and install it instead as a regular npm package. By default…
s	format	Format components in the development workspace
s	lint	Lint components in the development workspace
s	graph	Generate an image file with the workspace components' dependencies graph
s	list|ls	List components on a workspace or a remote scope
s	globals	List all globals
s	run	Locally run an app component (independent of bit's dev server)
s	app	Manages apps
s	capsule	Manage capsules
s	delete	Mark components as deleted on the remote
s	eject-conf	Eject components configuration (create a component.json file). Note this can be reversed at any…
s	git	Perform git operations
s	lane|l	Manage lanes - if no sub-command is used, runs 'bit lane list'
s	log-file	EXPERIMENTAL: Show file history
s	mini-status|ms	EXPERIMENTAL. Basic status for fast execution
s	pattern	List the component ids matching the given pattern
s	recover	EXPERIMENTAL. Recover component(s) soft-deleted from the workspace, or a remote scope
s	revert	Replace the current component files by the specified version, leave the version intact
s	scope	Manage the scope-name for components
s	server	EXPERIMENTAL. Communicate with bit CLI program via HTTP requests
s	system	System operations
s	snap	Create an immutable and exportable component snapshot (non-release version)
s	watch	Automatically recompile modified components (on save). By default, the watcher doesn't use…
s	use	Set aspects in the workspace/scope config to make them loadable by the workspace/scope.
s	ws-config|workspace-config	Manage workspace config files.
o	--version|-v	Show version	
o	--help|-h	Show help for bit	
@	init
o	--bare|-b		v
o	--shared|-s		v
o	--standalone	Do not nest component store within .git	
o	--reset|-r	Write missing or damaged Bit files	
o	--reset-new	Reset .bitmap file as if components were newly added	
o	--reset-lane-new	Reset only components belonging to lanes	
o	--reset-hard	Delete all Bit files and directories	
o	--reset-scope	Removes local scope	
o	--default-directory|-d		v
o	--default-scope		v
o	--package-manager|-p		v
o	--force	Force workspace initialization without clearing local objects	
o	--harmony	DEPRECATED: Harmony is the default now	
o	--interactive|-I	Start an interactive process	
a	1	0
@	new
o	--aspect|-a	ID of the aspect that registered the template	
o	--template|-t	Env-ID of the template's owner. Alias for --env	
o	--env	Env-ID of the template. Alias for -t	
o	--default-scope|-d	Set defaultScope in the new workspace's workspace.jsonc	
o	--skip-git	Skip generation of Git repository in the new workspace	
o	--empty	Skip template's default component creation	
o	--load-from	Local path to the workspace containing the template	
a	2	0
@	config
s	set	Set a global configuration
s	del	Delete given key from global configuration
s	get	Get a value from global configuration
s	list	List all configuration(s)
@	config set
a	2	0
@	config del
a	1	0
@	config get
a	1	0
@	config list
@	scope-config
s	set	Set a scope configuration.
s	del	Delete given key from global configuration.
s	get	Get a scope configuration.
s	list	List all scope configuration(s).
@	scope-config set
a	2	0
@	scope-config del
a	1	0
@	scope-config get
a	1	0
@	scope-config list
@	login
o	--cloud-domain	Login cloud domain (default bit.cloud)	
o	--port|-p	Port number to open for localhost server	
o	--suppress-browser-launch	Do not open a browser for authentication	
o	--npmrc-path	Path to npmrc file to configure bit.cloud registry	
o	--skip-registry-config	Don't configure bit.cloud registry	
o	--machine-name	Specify machine-name to pair with the token	
@	logout
@	doctor
o	--json|-j	Return diagnoses in json format	
o	--list	List all available diagnoses	
o	--save|-s		v
o	--archive|-a		v
a	1	0
@	completion
@	cli
s	generate	Generate an .md file with all commands details
@	cli generate
o	--metadata	Metadata/front-matter to place at the top of the .md file	
o	--docs	Generate the cli-reference.docs.mdx file	
o	--json|-j	Output the commands info as JSON	
@	help
o	--internal	Show internal commands	
@	clear-cache
o	--remote|-r	Clear memory cache from a remote scope	
@	remote
s	add	Add a bare-scope as a remote, usage: remote add <url>
s	del	Remove a tracked bit remote: usage: remote del <name>
@	remote add
o	--global|-g	Configure a remote bit scope	
a	1	0
@	remote del
o	--global|-g	Remove a globally configured remote scope	
a	1	0
@	remove
o	--track|-t	Keep tracking component in .bitmap	
o	--keep-files	Keep component files	
o	--force|-f	Removes the component even if used as a dependency	
o	--silent|-s	Skip confirmation	
a	1	0
@	import
o	--path|-p		v
o	--objects	Import components objects without checkout	
o	--override|-O	Override local changes	
o	--verbose|-v	Show verbose output for inspection	
o	--json|-j	Return the output as JSON	
o	--skip-dependency-installation	Do not auto-install dependencies	
o	--merge		v
o	--dependencies	Import all dependencies of imported components	
o	--dependents	Import components found while traversing from imported components	
o	--save-in-lane	Save in the lane when checked out to a lane	
o	--all-history	Fetch all history versions, always	
o	--fetch-deps	Fetch dependencies objects without adding to the workspace	
o	--track-only	Create bitmap entries without writing component files	
o	--include-deprecated	Include deprecated components when importing with patterns	
a	1	0
@	pack
@	deprecate
o	--new-id	If replaced by another component, enter the new component id	
a	1	0
@	undeprecate
@	rename
o	--scope|-s	Define the scope for the newly created component	
o	--path|-p	Relative path in the workspace to place new component in	
o	--refactor|-r	Update the import/require statements in all dependent components	
o	--preserve	Avoid renaming files and variables according to the new component name	
o	--ast	EXPERIMENTAL. Use AST to transform files instead of regex	
a	2	0
@	fork
o	--scope|-s		v
o	--path|-p		v
o	--refactor|-r	Update the import/require statements in all dependent components	
o	--skip-dependency-installation	Do not install packages of the imported components	
o	--env		v
o	--skip-config	Do not copy the config to the new component	
o	--preserve	Avoid refactoring file and variable/class names according to the new component name	
o	--no-link	Avoid saving a reference to the original component	
o	--ast	Use ast to transform files instead of regex	
a	2	0
@	export
o	--eject|-e	Remove component from the workspace and install it as a regular npm package	
o	--all	Export all components, including non-staged	
o	--all-versions	Export not only staged versions but all of them	
o	--origin-directly	Avoid export to the central hub, export directly to the original scopes	
o	--resume		v
o	--ignore-missing-artifacts	Don't throw an error when artifact files are missing	
o	--fork-lane-new-scope	Allow exporting a forked lane into a different scope than the original scope	
o	--json|-j	Show output in json format	
a	1	0
@	dependents
a	1	0
@	show
o	--json|-j	Return the component data in JSON format	
o	--legacy	Use the legacy bit show	
o	--remote|-r	Show data for a remote component	
o	--compare|-c	Legacy-only. Compare current file system component to its latest tagged version	
a	1	0
@	deps
s	get	Show direct and indirect dependencies of the given component
s	remove	Remove a dependency to component(s)
s	unset	Unset a dependency to component(s) that was previously set by 'bit deps set'
s	debug	Show the immediate dependencies and how their versions were determined
s	set	Set a dependency to component(s)
s	reset	Reset dependencies to the default values (revert any previously 'bit deps set')
s	eject	Write dependencies that were previously set via 'bit deps set' into .bitmap
s	blame	EXPERIMENTAL: Find out which snap/tag changed a dependency version
s	usage	EXPERIMENTAL: Find components that use the specified dependency
@	deps get
o	--tree|-t	EXPERIMENTAL: Render dependencies as a tree, similar to 'npm ls'	
a	1	0
@	deps remove
o	--dev|-d	Remove from devDependencies	
o	--peer|-p	Remove from peerDependencies	
a	2	0
@	deps unset
o	--dev|-d	Unset from devDependencies	
o	--peer|-p	Unset from peerDependencies	
a	2	0
@	deps debug
a	1	0
@	deps set
o	--dev|-d	Add to the devDependencies	
o	--peer|-p	Add to the peerDependencies	
a	2	0
@	deps reset
a	1	0
@	deps eject
a	1	0
@	deps blame
a	2	0
@	deps usage
a	1	0
@	log
o	--remote|-r	Show log of a remote component	
o	--parents	Show parents and lanes data	
o	--one-line|-o	Show each log entry in one line	
o	--json|-j	JSON format	
a	1	0
@	add
o	--id|-i	Manually set component id	
o	--main|-m	Define component entry point	
o	--namespace|-n	Organize component in a namespace	
o	--override|-o	Override existing component if exists (default = false)	
o	--scope|-s	Sets the component's scope. If not entered, the default-scope from workspace.jsonc will be used	
o	--env|-e	Set the component's environment. (overrides the env from variants if exists)	
o	--json|-j	Output as json format	
@	move
a	2	0
@	diff
o	--verbose|-v	Show a more verbose output where possible	
o	--table|-t	Show tables instead of plain text for dependencies diff	
a	1	0
@	envs
s	list	List all envs currently used in the workspace
s	get	Show config information from a component's env
s	set	Assigns one or more components a development environment (env)
s	unset	Un-sets an env from components
s	replace	Replace an existing env with another env for all components using the old env
s	update	Update a version of an env for all components using that env
@	envs list
@	envs get
o	--services		v
a	1	0
@	envs set
a	2	0
@	envs unset
a	1	0
@	envs replace
a	2	0
@	envs update
a	2	0
@	start
o	--dev|-d	Start UI server in dev mode	
o	--port|-p	Port of the UI server	
o	--rebuild|-r	Rebuild the UI (useful e.g. when updating the workspace UI - can use the dev flag for HMR in this…	
o	--skip-ui-build	Skip building UI	
o	--verbose	Show verbose output for inspection and prints stack trace	
o	--no-browser|-n	Do not automatically open browser when ready	
o	--skip-compilation	Skip the auto-compilation before starting the web-server	
o	--ui-root-name	Name of the UI root to use, e.g. "teambit.scope/scope" or "teambit.workspace/workspace"	
a	1	0
@	ui-build
@	checkout
o	--interactive-merge	Display options to resolve conflicts when found during merge	
o	--ours	DEPRECATED	
o	--theirs	DEPRECATED	
o	--manual	DEPRECATED	
o	--auto-merge-resolve	Resolve merge conflicts according to the provided strategy: [ours, theirs, manual]	
o	--reset|-r	Revert changes that were not snapped/tagged	
o	--all|-a	All components	
o	--workspace-only	Only relevant for 'bit checkout head' when on a lane	
o	--verbose|-v	Verbose output for inspection	
o	--skip-dependency-installation	Do not auto-install dependencies of the imported components	
a	2	0
@	install
o	--type		v
o	--update|-u	Update all dependencies to the latest version	
o	--update-existing	DEPRECATED: Update existing dependencies version and types	
o	--save-prefix		v
o	--skip-dedupe	Do not dedupe dependencies on installation	
o	--skip-import	Do not import bit objects post installation	
o	--skip-compile	Do not compile components	
o	--add-missing-deps	Install all missing dependencies	
o	--add-missing-peers	Install all missing peer dependencies	
o	--recurring-install	Automatically run install again if there are old envs	
o	--no-optional	Do not install optional dependencies (pnpm only)	
a	1	0
@	uninstall
@	update
o	--yes|-y	Automatically update all outdated versions for packages specified in pattern (all if no pattern…	
o	--patch	Update to the latest patch version. Semver rules are ignored	
o	--minor	Update to the latest minor version. Semver rules are ignored	
o	--major	Update to the latest major version. Semver rules are ignored	
a	1	0
@	link
o	--json|-j	Return the output as JSON	
o	--verbose	Verbose output	
o	--rewire|-r	Replace relative paths with module paths in code (e.g. "../foo" => "@bit/foo")	
o	--target	Link to an external directory (similar to npm-link) so other projects could use these components	
o	--skip-fetching-objects	Skip fetch missing objects from remotes before linking	
a	1	0
@	component-issues
@	tag
o	--message|-m	A log message describing the latest changes	
o	--unmodified|-u	Include unmodified components (by default, only new and modified components are tagged)	
o	--editor	Open an editor to write a tag message for each component. Optionally, specify the editor-name…	
o	--ver|-v	Tag with the given version	
o	--increment|-l	Options are: [major, premajor, minor, preminor, patch, prepatch, prerelease], default to patch	
o	--prerelease-id	Prerelease identifier (e.g. "dev" to get "1.0.0-dev.1")	
o	--patch|-p	Syntactic sugar for "--increment patch"	
o	--minor	Syntactic sugar for "--increment minor"	
o	--major	Syntactic sugar for "--increment major"	
o	--pre-release	Syntactic sugar for "--increment prerelease" and --prerelease-id <identifier>	
o	--snapped	Tag only components whose head is a snap (not a tag)	
o	--unmerged	Complete a merge process by tagging the unmerged components	
o	--skip-tests	Skip running component tests during tag process	
o	--skip-auto-tag	Skip auto tagging dependents	
o	--soft	Do not persist. Only keep note of the changes to be made	
o	--persist	Persist the changes generated by --soft tag	
o	--disable-tag-pipeline	Skip the tag pipeline to avoid publishing the components	
o	--ignore-build-errors	Proceed to tag pipeline even when build pipeline fails	
o	--increment-by	(default to 1) increment semver flag (patch/minor/major) by. e.g. incrementing patch by 2: 0.0.1…	
o	--ignore-issues|-i	Ignore component issues (shown in "bit status" as "issues found"), issues to ignore…	
o	--ignore-newest-version|-I	Allow tagging even when the component has newer versions e.g. for hotfixes (default = false)	
o	--fail-fast	Stop pipeline execution on the first failed task (by default a task is skipped only when its…	
o	--build|-b	Not needed for now. Run the pipeline build and complete the tag	
o	--all|-a	DEPRECATED (not needed anymore, it is the default now). Tag all new and modified components	
o	--scope|-s	DEPRECATED (use "--unmodified" instead). Tag all components of the local scope	
o	--force	DEPRECATED (use "--skip-tests", "--ignore-build-errors" or "--unmodified" instead). Force-tag even…	
o	--disable-deploy-pipeline	DEPRECATED. Use --disable-tag-pipeline instead	
a	1	0
@	reset
o	--all|-a	Revert all unexported tags/snaps for all components	
o	--head	Revert the head tag/snap only	
o	--soft	Revert only soft-tags	
o	--force|-f	Revert the tag even if it's used as a dependency	
a	1	0
@	merge
o	--ours	DEPRECATED. In case of a conflict, keep the local modification	
o	--theirs	DEPRECATED. In case of a conflict, override the local modification with the specified version	
o	--manual	DEPRECATED. Use --auto-merge-resolve	
o	--auto-merge-resolve	In case of a conflict, resolve according to the strategy: [ours, theirs, manual]	
o	--abort	In case of an unresolved merge, revert to pre-merge state	
o	--resolve	Mark an unresolved merge as resolved and create a new snap with the changes	
o	--no-snap	Do not auto snap even if the merge completed without conflicts	
o	--build	In case of snap during the merge, run the build-pipeline	
o	--verbose	Show details of components that were not merged successfully	
o	--skip-dependency-installation|-x	Do not install new dependencies resulting from the merge	
o	--message|-m	Override the default message for the auto snap	
a	1	0
@	create
o	--namespace|-n	Sets the component's namespace and nested dirs inside the scope	
o	--scope|-s	Sets the component's scope-name	
o	--aspect|-a	Aspect-id of the template	
o	--template	Env-id of the template, alias for --aspect	
o	--path	Relative path in the workspace	
o	--env	Set the component's environment	
a	2	0
@	templates
o	--show-all|-s	Show hidden templates	
o	--aspect|-a	Show templates provided by the aspect-id	
@	build
o	--all|-a	DEPRECATED. Use --unmodified	
o	--unmodified|-u	Include unmodified components	
o	--dev|-d	Run the pipeline in dev mode	
o	--install	Install core aspects in capsules	
o	--reuse-capsules	Avoid deleting the capsules root-dir before starting the build	
o	--tasks	Build the specified task(s) only	
o	--cache-packages-on-capsule-root	Set the package-manager cache on the capsule root	
o	--list-tasks	List tasks of an env or a component-id for each one of the pipelines	
o	--skip-tests	Skip running component tests during build process	
o	--fail-fast	Stop pipeline execution on the first failed task	
a	1	0
@	artifacts
o	--aspect	Show/download only artifacts generated by this aspect-id	
o	--task	Show/download only artifacts generated by this task-id	
o	--files	Show/download only artifacts matching the given files or the glob pattern (wrap glob patterns in…	
o	--out-dir	Download the files to the specified dir	
a	1	0
@	refactor
s	dependency-name	Replace the dependency's old package-name with a new one in the code, usage: refactor…
@	refactor dependency-name
a	2	0
@	status
o	--json|-j	Return a JSON version of the component	
o	--verbose	Show extra data: full snap hashes for staged components, and divergence point for lanes	
o	--lanes|-l	When on a lane, show updates from main and updates from forked lanes	
o	--strict	In case issues found, exit with code 1	
@	compile
o	--changed|-c	Compile only new and modified components	
o	--verbose|-v	Show more data, such as, dist paths	
o	--json|-j	Return the compile results in json format	
o	--delete-dist-dir	Delete existing dist folder before writing new compiled files	
a	1	0
@	test
o	--watch|-w	Start the tester in watch mode	
o	--debug|-d	Start the tester in debug mode	
o	--all|-a	Test all components, not only new and modified	
o	--junit	Write tests results as JUnit XML format into the specified file path	
o	--coverage	Show code coverage data	
o	--env|-e	Test only components assigned the given env	
o	--scope|-s	DEPRECATED. (use the pattern instead, e.g. "scopeName/**"). Name of the scope to test	
a	1	0
@	schema
o	--json|-j	Return the component schema in json format	
a	1	0
@	check-types
o	--all|-a	Check-types for all components, not only modified and new	
o	--strict	In case issues found, exit with code 1	
a	1	0
@	aspect
@	eject
o	--force|-f	Ignore local changes/versions, eject component/s even when they are staged or modified. Note…	
o	--json|-j	Print the results in JSON format	
o	--keep-files	Keep the component files in the workspace intact	
a	1	0
@	format
o	--changed	Format only new and modified components	
o	--check	Will output a message and a list of unformatted files, if any	
o	--json|-j	Return the format results in json format	
@	lint
o	--changed|-c	Lint only new and modified components	
o	--fix|-f	Automatically fix problems	
o	--fix-type	Specify the types of fixes to apply (problem, suggestion, layout)	
o	--json|-j	Return the lint results in json format	
a	1	0
@	graph
o	--image|-i		v
o	--remote		v
o	--all-versions	Enter all components versions into the graph, not only latest	
o	--layout		v
o	--json|-j	Json format	
a	1	0
@	list
o	--ids|-i	Show only component ids, unformatted	
o	--scope|-s	Show only components stored in the local scope	
o	--outdated|-o	Highlight outdated components	
o	--json|-j	Show the output in JSON format	
o	--namespace	Show only components in the specified namespace	
a	1	0
@	globals
o	--json|-j	Json format	
@	run
o	--dev|-d	Start the application in dev mode	
o	--port|-p	Port to run the app on	
o	--verbose|-v	Show verbose output for inspection and print stack trace	
o	--skip-watch	Avoid running the watch process that compiles components in the background	
o	--ssr	Run app in server side rendering mode	
a	1	0
@	app
s	list	List all registered apps
s	run	Locally run an app component (independent of bit's dev server)
@	app list
o	--json|-j	Return the component data in json format	
@	app run
o	--dev|-d	Start the application in dev mode	
o	--port|-p	Port to run the app on	
o	--verbose|-v	Show verbose output for inspection and print stack trace	
o	--skip-watch	Avoid running the watch process that compiles components in the background	
o	--ssr	Run app in server side rendering mode	
a	1	0
@	capsule
s	list	List the capsules generated for this workspace
s	create	Create capsules for components
s	delete	Delete capsules
@	capsule list
o	--json|-j	JSON format	
@	capsule create
o	--base-dir|-b	Set base dir of all capsules	
o	--root-base-dir|-r	Set root base dir of all capsules	
o	--always-new|-a	Create new environment for capsule	
o	--seeders-only	Create capsules for the seeders only	
o	--id|-i	Reuse capsule of certain name	
o	--use-hash	Whether to use hash function as capsules root dir name	
o	--json|-j	JSON format	
o	--install-packages	Install packages by the package-manager	
o	--package-manager|-p	Npm, yarn or pnpm, default to npm	
@	capsule delete
o	--scope-aspects	Delete scope-aspects capsules	
o	--all|-a	Delete all capsules for all workspaces and scopes	
o	--json|-j	JSON format	
@	delete
o	--lane	When on a lane, delete the component from this lane only	
o	--update-main	EXPERIMENTAL: Delete component/s on the main lane after merging this lane into main	
o	--force|-f	Removes the component from the scope, even if used as a dependency	
o	--silent|-s	Skip confirmation	
o	--hard	NOT-RECOMMENDED: Delete a component completely from a remote scope	
a	1	0
@	eject-conf
o	--propagate|-p	Mark propagate true in the config file, so that component.json configs will be merge with…	
o	--override|-o	Override file if exist	
a	1	0
@	git
s	set-merge-driver	Setup bit's git merge driver for bitmap files
s	merge-bitmaps	Merge conflicting bitmap files during git merge
@	git set-merge-driver
o	--global|-g	Set the git merge driver globally	
@	git merge-bitmaps
a	3	0
@	lane
s	list	List local lanes
s	switch	Switch to the specified lane
s	show	Show lane details. If no lane specified, show the current lane
s	create	Creates a new lane and switches to it
s	remove	Remove or delete lanes
s	change-scope	Changes the remote scope of a lane
s	alias	Adds an alias to a lane
s	rename	EXPERIMENTAL. Change the lane-name locally and on the remote (if exported)
s	diff	Show diff between lanes
s	merge-abort	Abort the recent lane-merge. Revert the lane object and checkout accordingly
s	merge	Merge a local or a remote lane to the current lane. By default, the provided lane will be fetched…
s	add-readme	EXPERIMENTAL. Sets an existing component as the readme of a lane
s	remove-readme	EXPERIMENTAL. Remove lane readme component
s	import	Import a remote lane to your workspace and switch to that lane
s	remove-comp	DEPRECATED. Remove components when on a lane
@	lane list
o	--details|-d	Show more details on the state of each component in each lane	
o	--json|-j	Show lanes' details in a json format	
o	--remote|-r	Show all remote lanes from the specified scope	v
o	--merged	List only merged lanes	
o	--not-merged	List only lanes that haven't been merged	
@	lane switch
o	--alias|-n	Relevant when the specified lane is a remote lane. Create a local alias for the lane	v
o	--merge|-m	Merge local changes with the checked out version. Strategy should be 'theirs', 'ours', or 'manual'	v
o	--get-all	Checkout all components in a lane, including those not currently in the workspace	
o	--skip-dependency-installation	Do not install packages of the imported components	
o	--pattern|-p	Switch only the lane components matching the specified component-pattern	v
o	--json|-j	Return the output as JSON	
a	1	0
@	lane show
o	--json|-j	Show the lane details in json format	
o	--remote	Show details of the remote head of the provided lane	
@	lane create
o	--scope|-s	Remote scope to which this lane will be exported, default to the workspace.json's defaultScope	v
o	--remote-scope	DEPRECATED. Use --scope	
o	--alias	A local alias to refer to this lane, defaults to the <lane-name>	v
o	--fork-lane-new-scope	Create the new lane in a different scope than its parent lane (if created from another lane)	
a	1	0
@	lane remove
o	--remote|-r	Delete a remote lane. Use remote/lane-id syntax e.g. bit lane remove owner.org/my-lane --remote…	
o	--force|-f	Removes/deletes the lane even when the lane is not yet merged to main	
o	--silent|-s	Skip confirmation	
a	1	0
@	lane change-scope
o	--lane-name|-l	The name of the lane to change its remote scope. If not specified, the current lane is used	v
a	1	0
@	lane alias
a	1	0
@	lane rename
o	--lane-name|-l	The name of the lane to rename. If not specified, the current lane is used	v
a	1	0
@	lane diff
o	--pattern|-p	Show lane-diff for components conforming to the specified component-pattern only	v
o	--workspace-only	Do not mark the components as removed from the lane. Instead, remove them from the workspace only	
o	--update-main	EXPERIMENTAL. Remove, i.e. delete, component/s on the main lane after merging this lane into main	
a	1	0
@	lane merge-abort
o	--verbose	Show details of components that didn't need to be merged	
o	--silent|-s	Skip confirmation	
o	--skip-dependency-installation	Do not install packages of the imported components	
@	lane merge
o	--ours	DEPRECATED. Use --auto-merge-resolve. In case of a conflict, keep local modifications	
o	--theirs	DEPRECATED. Use --auto-merge-resolve. In case of a conflict, override local with incoming changes	
o	--manual	DEPRECATED. Use --auto-merge-resolve. Requires manual resolution of conflicts	
o	--auto-merge-resolve	In case of a merge conflict, resolve according to the provided strategy. Options include: [ours…	
o	--workspace	Merge only lane components that are in the current workspace	
o	--no-snap	Do not auto snap after merge completed without conflicts	
o	--tag	Auto-tag all lane components after merging into main (or tag-merge in case of snap-merge)	
o	--build	In case of snap during the merge, run the build-pipeline (similar to bit snap --build)	
o	--message|-m	Override the default message for the auto snap	
o	--keep-readme	Skip deleting the lane readme component after merging	
o	--no-squash	Relevant for merging lanes into main, which by default squashes all lane snaps	
o	--squash	EXPERIMENTAL. Relevant for merging a lane into another non-main lane, which by default does not…	
o	--ignore-config-changes	Allow merging when components are modified due to config changes (such as dependencies) only and…	
o	--verbose	Show details of components that were not merged successfully	
o	--skip-dependency-installation|-x	Do not install dependencies of the imported components	
o	--skip-fetch	Use the local state of target-lane if exits locally, without updating it from the remote	
o	--include-deps	Relevant for "--pattern" and "--workspace". Merge also dependencies of the specified components	
o	--resolve-unrelated	Relevant when a component on a lane and the component on main have nothing in common…	
o	--include-non-lane-comps	When merging main, include workspace components that are not on the lane (by default only lane…	
a	2	0
@	lane add-readme
a	2	0
@	lane remove-readme
a	1	0
@	lane import
o	--skip-dependency-installation|-x	Do not install dependencies of the imported components	
o	--pattern|-p	Import only components from the lane that fit the specified component-pattern to the workspace…	
a	1	0
@	lane remove-comp
o	--workspace-only	Do not mark the components as removed from the lane. Instead, remove them from the workspace only	
o	--update-main	EXPERIMENTAL. Remove, i.e., delete, component/s on the main lane after merging this lane into the…	
a	1	0
@	log-file
o	--one-line|-o	Show each log entry in one line	
a	1	0
@	mini-status
o	--show-issues	Show component issues	
o	--json|-j	Output in JSON format	
a	1	0
@	pattern
o	--json|-j	Return the output as JSON	
a	1	0
@	recover
o	--skip-dependency-installation|-x	Do not install packages in case of importing components	
a	1	0
@	revert
o	--verbose|-v	Showing verbose output for inspection	
o	--skip-dependency-installation|-x	Do not install packages of the imported components	
a	2	0
@	scope
s	set	Sets the scope for specified component/s. If no component is specified, sets the default scope of…
s	rename	Renames the scope name for all components with the specified 'current scope name' - only available…
s	rename-owner	Renames the owner part of the scope-name for all components with the specified 'current owner name'.
s	fork	Fork all components of the original-scope and refactor the source-code to use the new scope name.
@	scope set
a	2	0
@	scope rename
o	--refactor|-r	Update the import statements in all dependent components	
a	2	0
@	scope rename-owner
o	--refactor|-r	Update the import statements in all dependent components	
o	--ast	EXPERIMENTAL. Use AST to transform files instead of regex	
a	2	0
@	scope fork
o	--ast	EXPERIMENTAL. Use AST to transform files instead of regex	
@	server
o	--port|-p	Port to run the server on	
@	system
s	log	Print debug.log to the screen
@	system log
@	snap
o	--message|-m	Snap message describing the latest changes - will appear in component history log	
o	--unmodified	Include unmodified components (by default, only new and modified components are snapped)	
o	--unmerged	Complete a merge process by snapping the unmerged components	
o	--build|-b	Not needed for now. Run the build pipeline locally in case the feature-flag build-on-ci is enabled	
o	--editor	Open an editor to write a snap message per component. Optionally specify the editor-name (defaults…	
o	--skip-tests	Skip running component tests during snap process	
o	--skip-auto-snap	Skip auto snapping dependents	
o	--disable-snap-pipeline	Skip the snap pipeline. This will for instance skip packing and publishing component version for…	
o	--ignore-build-errors	Proceed to snap pipeline even when build pipeline fails	
o	--ignore-issues|-i	Ignore component issues (shown in "bit status" as "issues found"), issues to ignore…	
o	--all|-a	DEPRECATED (not needed anymore, now the default). Snap all new and modified components	
o	--fail-fast	Stop pipeline execution on the first failed task (by default a task is skipped only when its…	
o	--force|-f	DEPRECATED (use "--skip-tests" or "--unmodified" instead). Force-snap even if tests are failing…	
a	1	0
@	watch
o	--verbose|-v	Show all watch events and compiler verbose output	
o	--skip-pre-compilation	Skip compilation step before starting to watch	
o	--check-types|-t	EXPERIMENTAL. Show errors/warnings for types. Options are [file, project] to investigate only…	
@	use
a	1	0
@	ws-config
s	ws-config write	EXPERIMENTAL. Write config files in the workspace. Useful for IDEs.
s	ws-config clean	EXPERIMENTAL. Clean (delete) written config files in the workspace. Useful for IDEs.
s	ws-config list	EXPERIMENTAL. List config writers.
@	ws-config ws-config write
o	--clean|-c	Delete existing config files from the workspace. Highly recommended to run it with "--dry-run" first	
o	--writers|-w	Only write config files for the given writers. Use comma to separate multiple writers. Use…	
o	--silent|-s	Do not prompt for confirmation	
o	--no-dedupe	Write configs inside each one of the component's dir, avoid deduping	
o	--dry-run	Show the paths that configs will be written per env	
o	--dry-run-with-content	Use with --json flag. Show the config content and the paths that will be written per env	
o	--verbose|-v	Showing verbose output for writing	
o	--json|-j	JSON format	
@	ws-config ws-config clean
o	--silent|-s	Do not prompt for confirmation	
o	--writers|-w	Only clean config files for the given writers. Use comma to separate multiple writers. Use…	
o	--dry-run	Show the paths of configs that will be cleaned	
o	--json|-j	JSON format	
@	ws-config ws-config list
o	--json|-j	JSON format	
