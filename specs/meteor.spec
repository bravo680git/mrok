@	
s	npm	
s	help	Get help on meteor command line usage
s	run	Run a meteor development server in the current project. Searches upward from the current directory…
s	debug	DEPRECATED. The 'meteor debug' command is deprecated in favor of 'meteor --inspect-brk'
s	create	Create a new Meteor project. By default, it uses React and makes a subdirectory named name and…
s	update	Attempts to bring you to the latest version of Meteor, and then to upgrade your packages to their…
s	add	Add packages to your Meteor project. You can add multiple packages with one command
s	remove	Removes a package previously added to your Meteor project. You can remove multiple packages with…
s	list	Lists the packages that you have explicitly added to your project
s	add-platform	Adds platforms to your Meteor project. You can add multiple platforms with one command
s	remove-platform	Removes a platform previously added to your Meteor project
s	list-platforms	Lists all of the platforms added to your project
s	ensure-cordova-dependencies	Check if the dependencies are installed, otherwise install them
s	build	Package this project up for deployment. The command outputs a directory with builds for all…
s	lint	Run through the whole build process for the app and run all linters the app uses
s	shell	When `meteor shell` is executed in an application directory where a server is already running, it…
s	mongo	Opens a Mongo shell to view or manipulate collections. Can only be used when developing locally
s	reset	Reset the current project to a fresh state. Removes all local data
s	deploy	Deploys the project in your current directory to Meteor's servers
s	authorized	Manage authorized users and organizations
s	login	Prompts for your username and password and logs you in to your Meteor developer account
s	logout	Log out of your Meteor developer account
s	whoami	Prints the username of the currently logged-in Meteor developer
s	test-packages	Runs unit tests for one or more packages. The results are shown in a browser dashboard that…
s	test	Runs tests against the application
s	admin	Rarely used commands for administering official Meteor services
s	list-sites	List the sites that you have deployed with `meteor deploy`, and sites for which other users have…
s	publish-release	Publishes a new release to the package server, as determined by a JSON configuration file
s	publish	Publishes a new version of a local package to the package server. Must be runfrom the directory…
s	publish-for-arch	Publish a package for the same architecture that you are currently on
s	search	Searches through the Meteor package and release database for items whose names match the regular…
s	show	Searches through the Meteor package and release database for items whose names match the regular…
@	npm
@	help
s	admin	
a	1	0
#	help	1
t	help
@	help admin
s	maintainers	
s	recommend-release	
s	change-homepage	
s	list-organizations	
s	members	
@	help admin maintainers
@	help admin recommend-release
@	help admin change-homepage
@	help admin list-organizations
@	help admin members
@	run
o	target	If you have added a platform to your app with 'meteor add-platform', you can pass one of the…	
o	--port|-p	Port to listen on (instead of the default 3000)	V
o	--inspect	Enable server-side debugging via debugging clients like the Node.js command-line debugger, Chrome…	V
o	--inspect-brk	Enable server-side debugging via debugging clients like the Node.js command-line debugger, Chrome…	V
o	--mobile-server	Location where mobile builds connect to the Meteor server. Defaults to your local IP and the port…	
o	--cordova-server-port	Local port where Cordova will serve the content. It's important when multiple Cordova apps are…	v
o	--production	Simulate production mode. Minify and bundle CSS and JS files	
o	--raw-logs	Run without parsing logs from stdout and stderr	
o	--settings|-s	Set optional data for Meteor.settings on the server	v
o	--release	Specify the release of Meteor to use	v
o	--verbose	Print all output from builds logs	
o	--no-lint	Don't run linters used by the app on every rebuild	
o	--no-release-check	Don't run the release updater to check for new releases	
o	--allow-incompatible-update	Allow packages in your project to be upgraded or downgraded to versions that are potentially…	
o	--extra-packages	Run with additional packages (comma separated, for example: --extra-packages "package-name1…	v
o	--exclude-archs	Don't create bundles for certain web architectures (comma separated, for example: --exclude-archs…	v
=	run	--settings
d
@	debug
@	create
o	--release	Specify the release of Meteor to use	v
o	--package	Create a new meteor package instead of an app	v
o	--example	Example template to use	v
o	--list	Show list of available examples	
o	--bare	Create an empty app	
o	--minimal	Create an app with as few Meteor packages as possible	
o	--full	Create a fully scaffolded app	
o	--react	Create a basic react-based app, same as default	
o	--vue	Create a basic vue-based app	
o	--apollo	Create a basic apollo-based app	
o	--svelte	Create a basic svelte-based app	
o	--typescript	Create a basic Typescript React-based app	
o	--blaze	Create a basic blaze-based app	
o	--tailwind	Create a basic react-based app, with tailwind configured	
a	1	0
=	create	--example
d
@	update
o	--packages-only	Update the package versions only. Do not update the release	
o	--patch	Update the release to a patch release only	
o	--release	Update to a specific release of meteor	v
o	--allow-incompatible-update	Allow packages in your project to be upgraded or downgraded to versions that are potentially…	
o	--all-packages	Update all packages including indirect dependencies	
a	1	0
#	update	1
d
@	add
o	--allow-incompatible-update	Allow packages in your project to be upgraded or downgraded to versions that are potentially…	
a	1	0
@	remove
a	1	0
#	remove	1
d
@	list
o	--tree	Outputs a tree showing how packages are referenced	
o	--json	Outputs the tree in JSON format	
o	--weak	Show weakly referenced dependencies in the tree	
o	--details	Adds more package details to the JSON output	
@	add-platform
a	1	0
#	add-platform	1
v	server	
v	browser	
v	android	
v	ios	
@	remove-platform
a	1	0
#	remove-platform	1
d
@	list-platforms
@	ensure-cordova-dependencies
@	build
o	--debug	Build in debug mode (don't minify, etc)	
o	--directory	Output a directory (rather than a tarball) for the application server bundle. If the output…	
o	--server-only	Skip building mobile apps even if mobile platforms have been added	
o	--mobile-settings	Set optional data for the initial value of Meteor.settings in your mobile application	
o	--server	Location where mobile builds connect to the Meteor server. Defaults to localhost:3000. Can include…	
o	--architecture	Builds the server for a different architecture than your developer machine's architecture. Note…	v
o	--allow-incompatible-update	Allow packages in your project to be upgraded or downgraded to versions that are potentially…	
o	--platforms	Builds only the specified platforms (when available)	V
o	--packageType	Choose between apk/bundle for android builds	V
a	1	0
=	build	--architecture
v	os.osx.x86_64	
v	os.linux.x86_64	
v	os.linux.x86_32	
v	os.windows.x86_32	
v	os.windows.x86_64	
=	build	--platforms
d
=	build	--packageType
v	apk	
v	bundle	
#	build	1
t	folders
@	lint
o	--allow-incompatible-update	Allow packages in your project to be upgraded or downgraded to versions that are potentially…	
@	shell
@	mongo
o	--url|-U	Mongo database URL	v
@	reset
@	deploy
o	--delete|-D	Permanently delete this deployment	
o	--debug	Deploy in debug mode (don't minify, etc)	
o	--settings|-s	Set optional data for Meteor.settings	v
o	--allow-incompatible-update	Allow packages in your project to be upgraded or downgraded to versions that are potentially…	
o	--deploy-polling-timeout	The number of milliseconds to wait for build/deploy success or failure after a successful upload…	v
o	--no-wait	Exits when Meteor has uploaded the app's code instead of waiting for the deploy to conclude	
o	--cache-build	Reuses the build already created if the git commit hash is the same	
o	--free	When deploying an app for the first time, you can pass this option to deploy your app in the…	
o	--plan	You can change the app plan by providing this argument with one of the following values…	
o	--mongo	If this flag is true and it's not provided a mongo url in the settings…	v
o	--container-size	Change your app's container size using the deploy command	v
a	1	0
=	deploy	--settings
d
=	deploy	--mongo
v	true	
v	false	
=	deploy	--container-size
v	tiny	
v	compact	
v	standard	
v	double	
v	quad	
v	octa	
v	dozen	
@	authorized
o	--add	Add an authorized user or organization	
o	--remove	Remove an authorized user or organization	
o	--transfer	Transfer the (Galaxy) app to a new user or organization	
o	--list	List authorized users and organizations	
a	1	0
@	login
o	--email	Add an authorized user or organization	v
@	logout
@	whoami
@	test-packages
o	--release	Specify the release of Meteor to use	v
o	--port|-p	Port to listen on (instead of the default 3000). Also uses port N+1 and N+2	v
o	--inspect	Enable server-side debugging via debugging clients like the Node.js command-line debugger, Chrome…	V
o	--inspect-brk	Enable server-side debugging via debugging clients like the Node.js command-line debugger, Chrome…	V
o	--mobile-server	Location where mobile builds connect to the Meteor server. Defaults to your local IP and the port…	
o	--cordova-server-port	Local port where Cordova will serve the content. It's important when multiple Cordova apps are…	v
o	--production	Simulate production mode. Minify and bundle CSS and JS files	
o	--settings|-s	Set optional data for Meteor.settings on the server	v
o	--ios	Run tests in an iOS emulator. All of the tests for client and server will run in addition to…	
o	--android	Run tests in an Android emulator. All of the tests for client and server will run in addition to…	
o	--ios-device	Run tests on iOS mobile device. All of the tests for client and server will run in addition to…	
o	--android-device	Run tests on Android emulator or on a mobile device. All of the tests for client and server will…	
o	--test-app-path	Set the directory in which to create a temporary app used for tests. Defaults to the system's…	V
o	--verbose	Print all output from builds logs	
o	--no-lint	Don't run linters used by the app on every rebuild	
o	--extra-packages	Run with additional packages (comma separated, for example: --extra-packages "package-name1…	v
o	--driver-package	Test driver package to use to run tests and display results. For example: --driver-package…	v
o	package	Package name	
=	test-packages	--settings
d
=	test-packages	--test-app-path
t	folders
@	test
o	--full-app	Your app is loaded as usual, then hidden, so that your tests can inspect and interact with the…	v
o	--port|-p	Port to listen on (instead of the default 3000). Also uses port N+1 and N+2	v
o	--inspect	Enable server-side debugging via debugging clients like the Node.js command-line debugger, Chrome…	V
o	--inspect-brk	Enable server-side debugging via debugging clients like the Node.js command-line debugger, Chrome…	V
o	--mobile-server	Location where mobile builds connect to the Meteor server. Defaults to your local IP and the port…	
o	--cordova-server-port	Local port where Cordova will serve the content. It's important when multiple Cordova apps are…	v
o	--raw-logs	Run without parsing logs from stdout and stderr	
o	--settings|-s	Set optional data for Meteor.settings on the server	v
o	--ios	Run tests in an iOS emulator. All of the tests for client and server will run in addition to…	
o	--android	Run tests in an Android emulator. All of the tests for client and server will run in addition to…	
o	--ios-device	Run tests on iOS mobile device. All of the tests for client and server will run in addition to…	
o	--android-device	Run tests on Android emulator or on a mobile device. All of the tests for client and server will…	
o	--test-app-path	Set the directory in which to create a temporary app used for tests. Defaults to the system's…	V
o	--verbose	Print all output from builds logs	
o	--extra-packages	Run with additional packages (comma separated, for example: --extra-packages "package-name1…	v
o	--driver-package	Test driver package to use to run tests and display results. For example: --driver-package…	v
o	--exclude-archs	Don't create bundles for certain web architectures (comma separated, for example: --exclude-archs…	v
=	test	--settings
d
=	test	--test-app-path
t	folders
@	admin
s	maintainers	Manage users and organizations that are maintainers for a particular package
s	recommend-release	Recommend a version of a meteor release
s	change-homepage	Change the homepage containing package information
s	list-organizations	List the organizations of which you are a member
s	members	Manage members of an organization
a	1	0
@	admin maintainers
o	--add	Add an authorized maintainer to a package	v
o	--remove	Remove an authorized maintainer from a package. You cannot remove yourself if you are the last…	v
o	--list	List authorized maintainers	
a	1	0
@	admin recommend-release
a	1	0
@	admin change-homepage
a	2	0
@	admin list-organizations
@	admin members
o	--add	Add a member to the organization	v
o	--remove	Remove a member to the organization	v
o	--list	List members of the organization	
a	1	0
@	list-sites
@	publish-release
o	--create-track	Publish a new release track	
a	1	0
#	publish-release	1
d
@	publish
o	--create	Publish a new package	
o	--update	Publish a new package	
o	--allow-incompatible-update	Allow packages in your project to be upgraded or downgraded to versions that are potentially…	
o	--no-lint	Don't run linters used by the app on every rebuild	
@	publish-for-arch
a	1	0
@	search
o	--maintainer	Filter by authorized maintainer	v
o	--show-all	Show all matches, even prereleases	
o	--ejson	Show more detailed output in EJSON format	
a	1	0
@	show
o	--show-all	Show all matches, even prereleases	
o	--ejson	Show more detailed output in EJSON format	
a	1	0
