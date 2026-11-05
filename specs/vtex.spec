@	
s	add	Adds the specified app(s) to the manifest's dependencies
s	autoupdate	Automatically updates VTEX IO's CLI
s	browse	Opens the URL relative to your current workspace and account in a new browser window
s	config	Env Configuration
s	debug dotnet	Debug .NET applications (IDEs only)
s	deploy	Publishes an app as a stable version. Only works for apps previously published as a release…
s	deprecate	Deprecates the specified app, uninstalling and downgrading it to the latest stable version in…
s	deps	Displays the differences between the dependencies of two distinct workspaces. If a single…
s	edition	Displays the Edition App version installed on the current account
s	help	Displays help for VTEX CLI commands
s	infra	Infra service
s	init	Copies starting files and folders from VTEX boilerplates into your local directories
s	install	Installs an app on the current workspace. If not specified which one, it defaults to the app in…
s	lighthouse	Runs a Lighthouse audit over the specified URL
s	lh	Runs a Lighthouse audit over the specified URL
s	link	Syncs the app in the current directory with the development workspace in use
s	list	Lists the apps installed on the current workspace and account
s	local token	Prints the user's auth token and copies it to the clipboard
s	login	Login to a VTEX account
s	logout	Logs out of the current VTEX account
s	logs	Shows logs of an app. (Only apps in production.)
s	publish	Publishes the app in the current directory as a release candidate version
s	redirects	Redirects from the current account and workspace
s	release	(Only for git users.) Bumps the app version, commits, and pushes to remote the app in the current…
s	settings	VTEX CLI Settings
s	setup	Sets up typings and tools for the current development environment
s	submit	Submits the current app, or an specified one, to validation from VTEX App Store team
s	support	Logs in as support to another VTEX account
s	switch	Switches to another VTEX account
s	test	Runs unit tests for the app in the current directory
s	undeprecate	Reestablishes a deprecated version of an app as a stable version
s	uninstall	Uninstalls an app from the current workspace. If not specified which app to uninstall, it defaults…
s	unlink	Unlinks an app from the current workspace. If not specified which app to unlink, it defaults to…
s	update	Updates all installed apps to the latest (minor or patch) version. Does not upgrade to another…
s	url	Prints base URL for the current account and workspace
s	whoami	Prints the current account, workspace, environment, and login details
s	workspace	Workspace from the current account
o	--help|-h	Show help for command	
@	add
o	--help|-h	Show help for command	
a	2	0
@	autoupdate
o	--help|-h	Show help for command	
a	1	0
@	browse
o	--help|-h	Show help for command	
o	--qr|-q	Prints a QR Code on the terminal	
a	1	0
@	config
s	get	Prints the value of the requested configuration key
s	reset	Resets the specified configuration to its default value
s	set	Sets the value of a configuration key
o	--help|-h	Show help for command	
@	config get
o	--help|-h	Show help for command	
a	1	0
@	config reset
o	--help|-h	Show help for command	
a	1	0
@	config set
o	--help|-h	Show help for command	
a	2	0
@	debug dotnet
o	--help|-h	Show help for command	
a	1	0
@	deploy
o	--help|-h	Show help for command	
o	--yes|-y	Answers yes to all prompts	
o	--force|-f	(Use with caution.) Ignores the testing period of 7 minutes after publishing an app	
a	1	0
@	deprecate
o	--help|-h	Show help for command	
o	--yes|-y	Answers yes to all prompts	
a	2	0
@	deps
s	diff	Displays the differences between the dependencies of two distinct workspaces. If a single…
s	list	Displays the complete dependency tree of the current workspace
s	update	Updates a dependency of the current workspace. If not specified which dependency, it updates all…
@	deps diff
o	--help|-h	Show help for command	
a	2	0
@	deps list
o	--help|-h	Show help for command	
o	--keys|-k	Shows only key dependencies	
o	--npm|-n	Includes dependencies from the npm registry	
@	deps update
o	--help|-h	Show help for command	
a	2	0
@	edition
s	get	Displays the Edition App version installed on the current account
s	set	Sets the Edition App version for the current account
o	--help|-h	Show help for command	
@	edition get
o	--help|-h	Show help for command	
@	edition set
o	--help|-h	Show help for command	
a	1	0
@	help
o	--help|-h	Show help for command	
o	--all	Displays all commands available in the CLI	
a	1	0
@	infra
s	install	Installs an infra service
s	list	Lists installed infra services
s	update	Updates all installed infra services
o	--help|-h	Show help for command	
@	infra install
o	--help|-h	Show help for command	
a	1	0
@	infra list
o	--help|-h	Show help for command	
o	--available|-a	Lists services that are available to install	
o	--filter=filter|-f	Lists services that contain the specified word	
a	1	0
@	infra update
o	--help|-h	Show help for command	
@	init
o	--help|-h	Show help for command	
@	install
o	--help|-h	Show help for command	
o	--force|-f	Installs the specified app without checking for route conflicts	
a	2	0
@	lighthouse
s	audit	Runs a Lighthouse audit over the specified URL
s	show	Shows a previous audit report, filtering by app and/or URL
o	--help|-h	Show help for command	
@	lighthouse audit
o	--help|-h	Show help for command	
o	--json|-j	Returns the report as a json on stdout	
a	1	0
@	lighthouse show
o	--help|-h	Show help for command	
o	--app=app|-a	Filters by app name	
o	--url=url|-u	Filters by URL	
@	lh
s	audit	Runs a Lighthouse audit over the specified URL
s	show	Shows a previous audit report, filtering by app and/or URL
o	--help|-h	Show help for command	
@	lh audit
o	--help|-h	Show help for command	
o	--json|-j	Returns the report as a json on stdout	
a	1	0
@	lh show
o	--help|-h	Show help for command	
o	--app=app|-a	Filters by app name	
o	--url=url|-u	Filters by URL	
@	link
o	--help|-h	Show help for command	
o	--account=account|-a	Starts a development session in the specified account. Must be paired with the '--workspace' flag	
o	--clean|-c	Cleans builder cache	
o	--setup|-s	Sets up typing definitions before linking the app [see vtex setup --help]	
o	--unsafe|-u	Allows linking the app despite Typescript errors	
o	--workspace=workspace|-w	Starts a development session in the specified workspace. Can be paired with the '--account' flag…	
o	--no-watch	Doesn't watch for file changes after the initial link	
@	list
o	--help|-h	Show help for command	
@	local token
o	--help|-h	Show help for command	
@	login
o	--help|-h	Show help for command	
o	--workspace=workspace|-w	Logs in the specified workspace	
a	1	0
@	logout
o	--help|-h	Show help for command	
@	logs
o	--help|-h	Show help for command	
o	--all|-a	Shows logs of every app installed on the current account	
o	--past|-p	Shows previous logs of the specified app	
a	1	0
@	publish
o	--help|-h	Show help for command	
o	--force|-f	Publishes the app independently of SemVer rules	
o	--tag=tag|-t	Adds the specified tag to the release	
o	--workspace=workspace|-w	Uses the specified workspace in the app registry	
o	--yes|-y	Answers yes to all prompts	
@	redirects
s	delete	Deletes redirects from the current account and workspace
s	export	Exports all redirects defined in the current account and workspace to a CSV file
s	import	Imports redirects from a CSV file to the current account and workspace
o	--help|-h	Show help for command	
@	redirects delete
o	--help|-h	Show help for command	
a	1	0
@	redirects export
o	--help|-h	Show help for command	
a	1	0
@	redirects import
o	--help|-h	Show help for command	
o	--reset|-r	Removes all redirects previously defined	
@	release
o	--help|-h	Show help for command	
a	2	0
@	settings
s	get	
s	set	Sets value to the specified setting of an app
s	unset	Disables the specified setting of an app
o	--help|-h	Show help for command	
@	settings get
o	--help|-h	Show help for command	
a	2	0
@	settings set
o	--help|-h	Show help for command	
a	3	0
@	settings unset
o	--help|-h	Show help for command	
a	2	0
@	setup
o	--help|-h	Show help for command	
o	--ignore-linked|-i	Sets up types from published apps, and ignores types from linked apps	
o	--all	Sets up all available typings, configs, and tools	
o	--tooling	Sets up Prettier, Husky, and ESLint	
o	--tsconfig	Sets up React and Node TSconfig, if applicable	
o	--typings	Sets up GraphQL and React typings	
@	submit
o	--help|-h	Show help for command	
a	1	0
@	support
o	--help|-h	Show help for command	
a	1	0
@	switch
o	--help|-h	Show help for command	
o	--workspace=workspace|-w	Moves to the specified workspace	
a	1	0
@	test
s	e2e	Runs E2E integration tests for the app in the current directory
s	unit	Runs unit tests for the app in the current directory
o	--help|-h	Show help for command	
@	test e2e
o	--help|-h	Show help for command	
o	--report=report|-r	Displays the results and state of the specified test ID	
o	--token|-t	(Not recommended.) Sends your personal authorization token to your testing session, making it…	
o	--workspace|-w	Runs tests for the apps installed on the specified workspace	
@	test unit
o	--help|-h	Show help for command	
o	--unsafe|-u	Ignores Typescript errors	
@	undeprecate
o	--help|-h	Show help for command	
o	--yes|-y	Answers yes to all prompts	
a	2	0
@	uninstall
o	--help|-h	Show help for command	
o	--yes|-y	Answers yes to all prompts	
a	2	0
@	unlink
o	--help|-h	Show help for command	
o	--all|-a	Unlinks all apps	
a	2	0
@	update
o	--help|-h	Show help for command	
@	url
o	--help|-h	Show help for command	
@	whoami
o	--help|-h	Show help for command	
@	workspace
s	abtest	A/B tests from running on the current account
s	delete	Deletes one or many workspaces from the current account
s	list	Lists all workspaces of the current account
s	promote	Promotes the current workspace to master. Only works for production workspaces
s	reset	Cleans all configurations of the specified workspace and recreates it with the configurations from…
s	status	Displays information about the specified workspace
s	use	Creates and switches to a new workspace or simply switches to an existing one
o	--help|-h	Show help for command	
@	workspace abtest
s	finish	Stops all A/B tests from running on the current account
s	start	Starts a new A/B test on the current workspace
s	status	Displays the results of the active A/B tests
o	--help|-h	Show help for command	
@	workspace abtest finish
o	--help|-h	Show help for command	
@	workspace abtest start
o	--help|-h	Show help for command	
@	workspace abtest status
o	--help|-h	Show help for command	
@	workspace delete
o	--help|-h	Show help for command	
o	--force|-f	Deletes the specified workspace even if it is currently in use	
o	--yes|-y	Answers yes to all prompts	
a	2	0
@	workspace list
o	--help|-h	Show help for command	
@	workspace promote
o	--help|-h	Show help for command	
@	workspace reset
o	--help|-h	Show help for command	
o	--production|-p	Recreates the workspace as a production one	
o	--yes|-y	Answers yes to all prompts	
a	1	0
@	workspace status
o	--help|-h	Show help for command	
a	1	0
@	workspace use
o	--help|-h	Show help for command	
o	--production|-p	Creates and/or switches to a production workspace	
o	--reset|-r	Resets the workspace before switching to it	
a	1	0
