@	
s	build	Build web assets and prepare your app for any platform targets
s	completion	Enables tab-completion for Ionic CLI commands
s	docs	Open the Ionic documentation website
s	info	Print project, system, and environment information
s	init	Initialize existing projects with Ionic
s	link	Connect local apps to Ionic
s	login	Log in to Ionic
s	logout	Log out of Ionic
s	repair	Remove and recreate dependencies and generated files
s	serve	Start a local dev server for app dev/testing
s	signup	Create an Ionic account
s	start	Create a new project
s	config	Config commands for Ionic
s	capacitor	Capacitor commands Ionic
s	deploy	AppFlow deploy commands for Ionic
s	git	Git commands for Ionic
s	package	Package commands for Ionic
s	ssl	SSL commands for Ionic
s	ssh	SSH commands for Ionic
s	doctor	Doctor commands for Ionic
s	integrations	Integration commands for Ionic
s	enterprise	Enterprise commands for Ionic
s	cordova	Cordova commands for Ionic
@	build
o	--engine	Target engine (e.g. browser, cordova)	v
o	--platform	Target platform on chosen engine (e.g. ios, android)	v
o	--prod	Flag to use the production configuration	
o	--configuration|-c	Specify the configuration to use	v
o	--source-map	Output source maps	
o	--watch	Rebuild when files change	
=	build	--engine
v	browser	
v	cordova	
=	build	--platform
v	ios	
v	android	
=	build	--configuration
t	filepaths,folders
@	completion
@	docs
o	--browser|-w	Specifies the browser to use (safari, firefox, google chrome)	v
=	docs	--browser
v	safari	
v	firefox	
v	google chrome	
@	info
o	--json	Print system/environment info in JSON format	
@	init
o	--type	Type of project (e.g. angular, react, vue, custom)	v
o	--force|-f	Initialize even if a project already exists	
o	--multi-app	Initialize a multi-app project	
o	--project-id	Specify a slug for your app	v
o	--default	Mark the initialized app as the default project	
a	1	0
=	init	--type
v	angular	
v	react	
v	vue	
v	custom	
@	link
a	1	0
@	login
a	2	0
@	logout
@	repair
o	--cordova	Only perform the repair steps for Cordova platforms and plugins	
@	serve
o	--external	Host dev server on all network interfaces (i.e. --host=0.0.0.0)	
o	--host	Use specific host for the dev server	v
o	--port|-p	Use specific port for the dev server	v
o	--public-host	The host used for the browser or web view	v
o	--no-livereload	Do not spin up dev server--just serve files	
o	--lab-host	Use specific host for Ionic Lab server	v
o	--lab-port	Use specific port for Ionic Lab server	v
o	--no-open	Do not open a browser window	
o	--browser|-w	Specifies the browser to use (safari, firefox, google chrome)	v
o	--browseroption|-o	Specifies a path to open to (/#/tab/dash)	v
o	--lab|-l	Test your apps on multiple platform types in the browser	
o	--ssl	Use HTTPS for the dev server	
o	--prod	Flag to use the production configuration	
o	--consolelogs	Print app console logs to the terminal	
o	--consolelogs-port	Use specific port for console logs server	v
o	--configuration|-c	Specify the configuration to use	v
o	--source-map	Output sourcemaps	
=	serve	--browser
v	safari	
v	firefox	
v	google chrome	
=	serve	--configuration
t	filepaths,folders
@	signup
@	start
o	--list|-l	List available starter templates	
o	--type	Type of project to start (e.g. vue, angular, react, ionic-angular, ionic1)	v
o	--cordova	Include Cordova integration	
o	--capacitor	Include Capacitor integration	
o	--no-deps	Do not install npm/yarn dependencies	
o	--no-git	Do not initialize a git repo	
o	--link	Connect your new app to Ionic	
o	--id	Specify an Ionic App ID to link	v
o	--project-id	Specify a slug for your app (used for the directory name and package name)	v
o	--package-id	Specify the bundle ID/application ID for your app (reverse-DNS notation)	v
a	2	0
=	start	--type
v	vue	
v	angular	
v	react	
v	ionic-angular	
v	ionic1	
@	config
s	get	Print config values
s	set	Set config values
s	unset	Delete config values
@	config get
o	--global|-g	Use global CLI config	
o	--json	Output config values in JSON	
o	--root	Operate on root of ionic.config.json	
a	1	0
@	config set
o	--global|-g	Use global CLI config	
o	--json	Always interpret value as JSON	
o	--force	Always overwrite existing values	
o	--root	Operate on root of ./ionic.config.json	
a	2	0
@	config unset
o	--global|-g	Use global CLI config	
o	--root	Operate on root of ./ionic.config.json	
a	1	0
@	capacitor
s	add	Add a native platform to your Ionic project
s	build	Build an Ionic project for a given platform
s	copy	Copy web assets to native platforms
s	open	Open the IDE for a given native platform project
s	run	Run an Ionic project on a connected device
s	sync	Sync (copy + update) an Ionic project
s	update	Update Capacitor native platforms, install Capacitor/Cordova plugins
@	capacitor add
a	1	0
#	capacitor add	1
v	ios	
v	android	
@	capacitor build
o	--no-build	Do not invoke Ionic build	
o	--no-open	Do not invoke Capacitor open	
o	--prod	Flag to use the production configuration	
o	configuration|-c	Specify the configuration to use	
o	--source-map	Output source maps	
o	--watch	Rebuild when files change	
a	1	0
#	capacitor build	1
v	ios	
v	android	
@	capacitor copy
o	--no-build	Do not invoke an Ionic build	
o	--prod	Flag to use the production configuration	
o	configuration|-c	Specify the configuration to use	
o	--source-map	Output source maps	
o	--watch	Rebuild when files change	
a	1	0
@	capacitor open
a	1	0
#	capacitor open	1
v	ios	
v	android	
@	capacitor run
o	--list	List all available targets	
o	--target	Deploy to a specific device by its ID (use --list to see all)	v
o	--open	Open native IDE instead of using capacitor run	
o	--no-build	Do not invoke Ionic build	
o	--external	Host dev server on all network interfaces (i.e. --host=0.0.0.0)	
o	--host	Use specific host for the dev server	v
o	--port|-p	Use specific port for the dev server	v
o	--public-host	The host used for the browser or web view	v
o	--livereload|-l	Spin up dev server to live-reload www files	
o	--livereload-url	Provide a custom URL to the dev server	v
o	--prod	Flag to use the production configuration	
o	--configuration|-c	Specify the configuration to use	v
o	--source-map	Output source maps	
o	--watch	Rebuild when files change	
a	1	0
=	capacitor run	--configuration
t	filepaths,folders
#	capacitor run	1
v	ios	
v	android	
@	capacitor sync
o	--no-build	Do not invoke an Ionic build	
o	--prod	Flag to use the production configuration	
o	--configuration|-c	Specify the configuration to use	v
o	--source-map	Output source maps	
o	--watch	Rebuild when files change	
a	1	0
=	capacitor sync	--configuration
t	filepaths,folders
#	capacitor sync	1
v	ios	
v	android	
@	capacitor update
a	1	0
#	capacitor update	1
v	ios	
v	android	
@	deploy
s	add	Adds Appflow Deploy to the project
s	build	Create a deploy build on Appflow
s	configure	Overrides Appflow Deploy configuration
s	manifest	Generates a manifest file for the deploy service from a built app directory
@	deploy add
o	--app-id	Your Appflow app ID	v
o	--channel-name	The channel to check for updates from	v
o	--update-method	The update method that dictates the behavior of the plugin	v
o	--max-store	The maximum number of downloaded versions to store on the device	v
o	--min-background-duration	The minimum duration after which the app checks for an update in the background	v
@	deploy build
o	--environment	The group of environment variables exposed to your build	v
o	--channel	The channel you want to auto deploy the build to. This can be repeated multiple times if multiple…	v
o	--commit	Commit (defaults to HEAD)	v
o	--skip-download	Skip downloading build artifacts after command succeeds	
@	deploy configure
o	--app-id	Your Appflow app ID	v
o	--channel-name	The channel to check for updates from	v
o	--update-method	The update method that dictates the behavior of the plugin	v
o	--max-store	The maximum number of downloaded versions to store on the device	v
o	--min-background-duration	The minimum duration after which the app checks for an update in the background	v
a	1	0
@	deploy manifest
@	git
s	remote	Adds/updates the Appflow git remote to your local Ionic app
@	git remote
@	package
s	build	Create a package build on Appflow
s	deploy	Deploys a binary to a destination, such as an app store using Appflow
@	package build
o	--signing-certificate	Signing certificate	v
o	--environment	The group of environment variables exposed to your build	v
o	--native-config	The group of native config variables exposed to your build	v
o	--destination	The configuration to deploy the build artifact to the app store	v
o	--commit	Commit (defaults to HEAD)	v
o	--build-stack	Target platform ("Android", "iOS - Xcode 11 (Preferred)", "iOS - Xcode 10")	v
o	--build-file-name	The name for the downloaded build file	v
o	--ipa-name	The name for the downloaded ipa file	v
o	--dsym-name	The name for the downloaded dsym file	v
o	--apk-name	The name for the downloaded apk file	v
o	--aab-name	The name for the downloaded aab file	v
o	--artifact-type	The artifact type (aab, apk, ipa, dsym)	v
o	--skip-download	Skip downloading build artifacts after command succeeds	
a	2	0
=	package build	--build-stack
v	Android	
v	iOS - Xcode 11 (Preferred)	
v	iOS - Xcode 10	
=	package build	--artifact-type
v	aab	
v	apl	
v	ipa	
v	dysm	
#	package build	1
v	ios	
v	android	
#	package build	2
v	debug	
v	release	
v	development	
v	ad-hoc	
v	app-stpre	
v	enterprise	
@	package deploy
a	2	0
@	ssl
s	generate	Generates an SSL key & certificate
@	ssl generate
o	--key-path	Destination of private key file	v
o	--cert-path	Destination of certificate file	v
o	--country-name	The country name (C) of the SSL certificate	v
o	--state-or-province-name	The state or province name (ST) of the SSL certificate	v
o	--locality-name	The locality name (L) of the SSL certificate	v
o	--organization-name	The organization name (O) of the SSL certificate	v
o	--common-name	The common name (CN) of the SSL certificate	v
o	--bits|-b	Number of bits in the key	v
@	ssh
s	add	Add an SSH public key to Ionic
s	delete	Delete an SSH public key from Ionic
s	generate	Generates a private and public SSH key pair
s	list	List your SSH public keys on Ionic
s	setup	Setup your Ionic SSH keys automatically
s	use	Set your active Ionic SSH key
@	ssh add
o	--use	Use the newly added key as your default SSH key for Ionic	
a	1	0
@	ssh delete
a	1	0
@	ssh generate
o	--type|-t	The type of key to generate: ecdsa, ed25519, rsa	v
o	--bits|-b	Number of bits in the key	v
o	--annotation|-C	Annotation (comment) in public key. Your Ionic email address will be used	v
a	1	0
=	ssh generate	--type
v	ecdsa	
v	ed25519	
v	rsa	
@	ssh list
o	--json	Output SSH keys in JSON	
@	ssh setup
@	ssh use
a	1	0
@	doctor
s	check	Check the health of your Ionic project
s	list	List all issues and their identifiers
s	treat	Attempt to fix issues in your Ionic project
@	doctor check
a	1	0
@	doctor list
@	doctor treat
a	1	0
@	integrations
s	disable	Disable an integration
s	enable	Add & enable integrations to your app
s	list	List available and active integrations in your app
@	integrations disable
a	1	0
#	integrations disable	1
v	capacitor	
v	cordova	
v	enterprise	
@	integrations enable
o	--add	Download and add the integration even if enabled	
o	--root	Specify an alternative destination to download into when adding	v
o	--quiet	Less verbose output, ignore integration errors	
a	1	0
#	integrations enable	1
v	capacitor	
v	cordova	
v	enterprise	
@	integrations list
@	enterprise
s	register	Register your Product Key with this app
@	enterprise register
o	--app-id	The Ionic App ID	v
o	--key	The Product Key	v
@	cordova
s	build	Use Cordova to build for Android and iOS platform targets
s	compile	Compile native platform code
s	emulate	Emulate an Ionic project on a simulator/emulator
s	platform	Manage Cordova platform targets
s	plugin	Manage Cordova plugins
s	prepare	Copies assets to Cordova platforms, preparing them for native builds
s	requirements	Checks and print out all the requirements for platforms
s	resources	Automatically create icon and splash screen resources
s	run	Run an Ionic project on a connected device
@	cordova build
o	--no-build	Do not invoke an Ionic build	
o	--debug	Mark as a debug build	
o	--release	Mark as a release build	
o	--device	Deploy build to a device	
o	--emulator	Deploy build to an emulator	
o	--buildConfig	Use the specified build configuration	v
o	--prod	Flag to use the production configuration	
o	--configuration|-c	Specify the configuration to use	v
o	--source-map	Output source maps	
a	1	0
=	cordova build	--buildConfig
t	filepaths,folders
=	cordova build	--configuration
t	filepaths,folders
#	cordova build	1
v	ios	
v	android	
@	cordova compile
o	--debug	Mark as a debug build	
o	--release	Mark as a release build	
o	--device	Deploy build to a device	
o	--emulator	Deploy build to an emulator	
o	--buildConfig	Use the specified build configuration	v
a	1	0
=	cordova compile	--buildConfig
t	filepaths,folders
#	cordova compile	1
v	ios	
v	android	
@	cordova emulate
o	--list	List all available targets	
o	--no-build	Do not invoke Ionic build	
o	--external	Host dev server on all network interfaces (i.e. --host=0.0.0.0)	
o	--host	Use specific host for the dev server	v
o	--port|-p	Use specific port for the dev server	v
o	--public-host	The host used for the browser or web view	v
o	--livereload|-l	Spin up dev server to live-reload www files	
o	--livereload-url	Provide a custom URL to the dev server	v
o	--debug	Mark as a debug build	
o	--release	Mark as a release build	
o	--device	Deploy build to a device	
o	--emulator	Deploy build to an emulator	
o	--buildConfig	Use the specified build configuration	v
o	--target	Deploy build to a device (use --list to see all)	v
o	--no-native-run	Do not use native-run to run the app; use Cordova instead	
o	--connect	Tie the running app to the process	
o	--json	Output targets in JSON	
o	--ssl	Use HTTPS for the dev serve	
o	--prod	Flag to use the production configuration	
o	--consolelogs	Print app console logs to the terminal	
o	--consolelogs-port	Use specific port for console logs server	v
o	--configuration|-c	Specify the configuration to use	v
o	--source-map	Output source maps	
o	--buildconfig	Use the specified build configuration	v
a	1	0
=	cordova emulate	--buildConfig
t	filepaths,folders
=	cordova emulate	--configuration
t	filepaths,folders
=	cordova emulate	--buildconfig
t	filepaths,folders
#	cordova emulate	1
v	ios	
v	android	
@	cordova platform
o	--no-resources	Do not pregenerate icons and splash screen resources (corresponds to add)	
a	2	0
#	cordova platform	1
v	add	
v	remove	
v	update	
v	ls	
v	check	
v	save	
#	cordova platform	2
v	ios	
v	android	
@	cordova plugin
o	--force	Force overwrite the plugin if it exists (corresponds to add)	
o	--variable	Specify plugin variables	v
a	2	0
#	cordova plugin	1
v	add	
v	remove	
v	ls	
v	save	
@	cordova prepare
o	--no-build	Do not invoke an Ionic build	
o	--prod	Flag to use the production configuration	
o	--configuration|-c	Specify the configuration to use	v
o	--source-map	Output source maps	
o	--watch	Rebuild when files change	
a	1	0
=	cordova prepare	--configuration
t	filepaths,folders
#	cordova prepare	1
v	ios	
v	android	
@	cordova requirements
a	1	0
#	cordova requirements	1
v	ios	
v	android	
@	cordova resources
o	--icon|-i	Generate icon resources	
o	--splash|-s	Generate splash screen resources	
a	1	0
#	cordova resources	1
v	ios	
v	android	
@	cordova run
o	--list	List all available targets	
o	--no-build	Do not invoke Ionic build	
o	--external	Host dev server on all network interfaces (i.e. --host=0.0.0.0)	
o	--host	Use specific host for the dev server	v
o	--port|-p	Use specific port for the dev server	v
o	--public-host	The host used for the browser or web view	v
o	--livereload|-l	Spin up dev server to live-reload www files	
o	--livereload-url	Provide a custom URL to the dev server	v
o	--debug	Mark as a debug build	
o	--release	Mark as a release build	
o	--device	Deploy build to a device	
o	--emulator	Deploy build to an emulator	
o	--buildConfig	Use the specified build configuration	v
o	--target	Deploy build to a device (use --list to see all)	v
o	--no-native-run	Do not use native-run to run the app; use Cordova instead	
o	--connect	Tie the running app to the process	
o	--json	Output targets in JSON	
o	--ssl	Use HTTPS for the dev server	
o	--prod	Flag to use the production configuration	
o	--consolelogs	Print app console logs to the terminal	
o	--consolelogs-port	Use specific port for console logs server	v
o	--configuration|-c	Specify the configuration to use	v
a	1	0
=	cordova run	--buildConfig
t	filepaths,folders
=	cordova run	--configuration
t	filepaths,folders
#	cordova run	1
v	ios	
v	android	
