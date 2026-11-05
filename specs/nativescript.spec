@	
s	help	Open the CLI's documentation in your web browser
s	info	Displays version information about the NativeScript CLI, core modules, and runtimes
s	update	Updates the project with the latest versions of platform runtimes, cross-platform modules and…
s	package-manager	Prints the value of the current package manager
s	doctor	Checks your system for configuration problems which might prevent the NativeScript CLI from…
s	migrate	Migrates the app dependencies to a form compatible with NativeScript 6.0
s	usage-reporting	Configures anonymous usage reporting for the NativeScript CLI. All data gathered is used strictly…
s	error-reporting	Configures anonymous error reporting for the NativeScript CLI. All data gathered is used strictly…
s	proxy	Displays the current proxy settings of the NativeScript CLI
s	create	Create a new Nativescript project. Press Enter for an interactive walkthrough
s	clean	Clean your Nativescript project
s	preview	Produces a QR code which can be used to preview the app on a device
s	platform	Lists all platforms that the project currently targets. You can build and deploy your project only…
s	run	Runs your project on all connected devices or in native emulators for the selected platform
s	debug	Initiates a debugging session for your project on a connected device or native emulator
s	test	Runs unit tests on the selected mobile platform
s	plugin	Manage the plugins for your project
s	resources	Manage the plugins for your project
s	prepare	Starts a Webpack compilation and prepares the app's App_Resources and the plugins platforms…
s	build	Builds the project for iOS and produces an APP or IPA that you can manually deploy in the iOS…
s	deploy	Prepares, builds and deploys the project to a connected device or native emulator. You must…
s	install	Installs all dependencies described in a valid package.json or installs a selected NativeScript…
s	appstore	Lists all application records in iTunes Connect. The list contains name, version and bundle ID for…
s	device|devices	Lists all recognized connected Android or iOS devices with serial number and index, grouped by…
o	-v|--version	View your current Nativescript CLI version	
@	help
o	--help|-h	Show help for the help subcommand	
@	info
o	--help|-h	Show help for the info subcommand	
@	update
s	next	The latest development release
o	--help|-h	Show help for the update subcommand	
a	1	0
@	update next
@	package-manager
s	get	Prints the value of the current package manager
s	set	Enables the specified package manager for the NativeScript CLI. Supported values are npm, yarn and…
o	--help|-h	Show help for the package-manager subcommand	
@	package-manager get
@	package-manager set
@	doctor
s	android	Check your system configuration for android
s	ios	Check your system configuration for ios
o	--help|-h	Show help for the doctor subcommand	
@	doctor android
@	doctor ios
@	migrate
o	--help|-h	Show help for the migrate subcommand	
@	usage-reporting
s	status	Shows the current configuration for anonymous usage reporting for the NativeScript CLI
s	enable	Enables anonymous usage reporting
s	disable	Disables anonymous usage reporting
o	--help|-h	Show help for the usage-reporting subcommand	
@	usage-reporting status
@	usage-reporting enable
@	usage-reporting disable
@	error-reporting
s	status	Shows the current configuration for anonymous error reporting for the NativeScript CLI
s	enable	Enables anonymous error reporting
s	disable	Disables anonymous error reporting
o	--help|-h	Show help for the error-reporting subcommand	
@	error-reporting status
@	error-reporting enable
@	error-reporting disable
@	proxy
s	clear	Clears the currently configured proxy settings of the NativeScript CLI
s	set	Sets the proxy settings of the NativeScript CLI
o	--help|-h	Show help for the proxy subcommand	
@	proxy clear
@	proxy set
o	--insecure	Allows insecure SSL connections and transfers to be performed. In case your proxy doesn't have a…	
a	3	0
@	create
o	--template	Create a project using a predefined template	v
o	--angular|--ng	Create a project using the Angular template	
o	--react	Create a project using the React template	
o	--vue|--vuejs	Create a project using the Vue template	
o	--svelte	Create a project using the Svelte template	
o	--typescript|--tsc|--ts	Create a project using plain TypeScript	
o	--javascript|--js	Create a project using plain JavaScript	
o	--path	Specifies the directory where you want to create the project, if different from the current…	v
o	--appid	Sets the application identifier of your project. <appid> is the value of the application…	v
o	--help|-h	Show help for the create subcommand	
a	1	0
=	create	--template
d
=	create	--path
t	folders
@	clean
o	--help|-h	Show help for the clean subcommand	
@	preview
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--no-hmr	Disables Hot Module Replacement (HMR)	
o	--help|-h	Show help for the preview subcommand	
@	platform
s	list	Lists all platforms that the project currently targets. You can build and deploy your project only…
s	add	Configures the current project to target the selected platform
s	remove	Removes the selected platform from the platforms that the project currently targets
s	update	Updates the NativeScript runtime for the specified platform
o	--help|-h	Show help for the platform subcommand	
@	platform list
@	platform add
s	android	The latest android platform
s	android@[Version]	The defined android platform eg. 1.0.0
s	ios	The latest ios platform
s	ios@[Version]	The defined ios platform eg. 1.0.0
@	platform add android
o	--framework-path	Sets the path to a NativeScript runtime for the specified platform that you want to use instead of…	v
=	platform add android	--framework-path
t	filepaths
@	platform add android@[Version]
o	--framework-path	Sets the path to a NativeScript runtime for the specified platform that you want to use instead of…	v
=	platform add android@[Version]	--framework-path
t	filepaths
@	platform add ios
o	--framework-path	Sets the path to a NativeScript runtime for the specified platform that you want to use instead of…	v
=	platform add ios	--framework-path
t	filepaths
@	platform add ios@[Version]
o	--framework-path	Sets the path to a NativeScript runtime for the specified platform that you want to use instead of…	v
=	platform add ios@[Version]	--framework-path
t	filepaths
@	platform remove
s	android	The latest android platform
s	ios	The latest ios platform
@	platform remove android
@	platform remove ios
@	platform update
s	android	The latest android platform
s	ios	The latest ios platform
@	platform update android
@	platform update ios
@	run
s	android	The latest android platform
s	ios	The latest ios platform
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
o	--no-hmr	Disables Hot Module Replacement (HMR)	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--clean	Forces rebuilding the native application	
o	--emulator	Specifies that you want to debug the app in an emulator	
o	--timeout	Sets the number of seconds that the NativeScript CLI will wait for the debugger to boot. If not…	v
o	--justlaunch	Does not print the application output in the console	
o	--release	Produces a release build by running webpack in production mode and native build in release mode…	
o	--bundle	Bundle the application	
o	--help|-h	Show help for the run subcommand	
@	run android
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
o	--no-hmr	Disables Hot Module Replacement (HMR)	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--clean	Forces rebuilding the native application	
o	--emulator	Specifies that you want to debug the app in an emulator	
o	--timeout	Sets the number of seconds that the NativeScript CLI will wait for the debugger to boot. If not…	v
o	--justlaunch	Does not print the application output in the console	
o	--release	Produces a release build by running webpack in production mode and native build in release mode…	
o	--bundle	Bundle the application	
o	--aab	Specifies that the command will produce and deploy an Android App Bundle	
o	--env.snapshot	Creates a V8 Snapshot decreasing the app start time (only for release builds for Android)	
o	--env.compileSnapshot	Compiles the static assets produced by --env.snapshot into .so files allowing the native build to…	
o	--env.appComponents	Allows passing additional App Components for android	
o	--key-store-path	Specifies the file path to the keystore file (P12) which you want to use to code sign your APK	v
o	--key-store-password	Provides the password for the keystore file specified with --key-store-path	v
o	--key-store-alias	Provides the alias for the keystore file specified with --key-store-path	v
o	--key-store-alias-password	Provides the password for the alias specified with --key-store-alias-password	v
=	run android	--key-store-path
t	filepaths
@	run ios
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
o	--no-hmr	Disables Hot Module Replacement (HMR)	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--clean	Forces rebuilding the native application	
o	--emulator	Specifies that you want to debug the app in an emulator	
o	--timeout	Sets the number of seconds that the NativeScript CLI will wait for the debugger to boot. If not…	v
o	--justlaunch	Does not print the application output in the console	
o	--release	Produces a release build by running webpack in production mode and native build in release mode…	
o	--bundle	Bundle the application	
o	--sdk	Specifies the target simulator's sdk	v
@	debug
s	android	Start a debugging session for your project on a connected Android device or Android emulator
s	ios	Start a debugging session for your project on a connected iOS device or in the native iOS simulator
o	--help|-h	Show help for the debug subcommand	
@	debug android
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
o	--no-hmr	Disables Hot Module Replacement (HMR)	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--clean	Forces rebuilding the native application	
o	--emulator	Specifies that you want to debug the app in an emulator	
o	--timeout	Sets the number of seconds that the NativeScript CLI will wait for the debugger to boot. If not…	v
o	--debug-brk	Prepares, builds and deploys the application package on a device or in an emulator, and stops at…	
o	--start	Attaches the debug tools to a deployed and running app	
o	--no-watch	Changes in your code will not be livesynced	
o	--aab	Specifies that the command will produce and deploy an Android App Bundle	
o	--env.snapshot	Creates a V8 Snapshot decreasing the app start time (only for release builds for Android)	
o	--env.compileSnapshot	Compiles the static assets produced by --env.snapshot into .so files allowing the native build to…	
o	--env.appComponents	Allows passing additional App Components for android	
@	debug ios
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
o	--no-hmr	Disables Hot Module Replacement (HMR)	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--clean	Forces rebuilding the native application	
o	--emulator	Specifies that you want to debug the app in an emulator	
o	--timeout	Sets the number of seconds that the NativeScript CLI will wait for the debugger to boot. If not…	v
o	--debug-brk	Prepares, builds and deploys the application package on a device or in an emulator, and stops at…	
o	--start	Attaches the debug tools to a deployed and running app	
o	--no-watch	Changes in your code will not be livesynced	
o	--no-client	The NativeScript CLI attaches the debug tools but does not launch the developer tools in Safari…	
o	--inspector	The developer tools in the Safari Web Inspector are used for debugging the application	
@	test
s	init	Configure your project for unit testing
s	android	Run unit tests on all connected android devices or native emulators
s	ios	Run unit tests on all connected ios devices or native emulators
o	--help|-h	Show help for the test subcommand	
@	test init
o	--framework	Sets the unit testing framework to install	v
=	test init	--framework
v	mocha	
v	jasmine	
v	qunit	
@	test android
o	--watch	When you save changes to the project, changes are automatically synchronized to the connected…	
o	--debug-brk	Runs the tests under the debugger. The debugger will break just before your tests are executed, so…	
o	--justlaunch	Does not print the application output in the console	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--emulator	Specifies that you want to debug the app in an emulator	
o	--aab	Specifies that the command will produce and deploy an Android App Bundle	
o	--env.snapshot	Creates a V8 Snapshot decreasing the app start time (only for release builds for Android)	
o	--env.compileSnapshot	Compiles the static assets produced by --env.snapshot into .so files allowing the native build to…	
o	--env.appComponents	Allows passing additional App Components for android	
@	test ios
o	--watch	When you save changes to the project, changes are automatically synchronized to the connected…	
o	--debug-brk	Runs the tests under the debugger. The debugger will break just before your tests are executed, so…	
o	--justlaunch	Does not print the application output in the console	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--emulator	Specifies that you want to debug the app in an emulator	
@	plugin
s	add	Installs the specified plugin and its dependencies
s	remove	Uninstalls the specified plugin and its dependencies
s	update	Uninstalls and installs the specified plugin(s) and its dependencies
s	build	Builds the Android parts of a NativeScript plugin
s	create	Creates a project for building a new NativeScript plugin
o	--help|-h	Show help for the plugin subcommand	
@	plugin add
a	1	0
@	plugin remove
a	1	0
@	plugin update
a	1	0
@	plugin build
@	plugin create
o	--path	Specifies the directory where you want to create the project, if different from the current…	v
o	--username	Specifies the GitHub username, which will be used to build the URLs in the plugin's package.json…	v
o	--pluginName	Used to set the default file and class names in the plugin source	v
o	--includeTypeScriptDemo	Specifies if a TypeScript demo should be created	
o	--includeTypeScriptDemo=n	Specifies if TypeScript demo should NOT be created	
o	--includeAngularDemo	Specifies if an Angular demo should be created	
o	--includeAngularDemo=n	Specifies if Angular demo should NOT be created	
o	--template	Specifies the custom seed archive, which you want to use to create your plugin	v
a	1	0
=	plugin create	--path
t	folders
@	resources
s	update	Updates the App_Resources's internal folder structure to conform to that of an Android Studio…
s	generate	
o	--help|-h	Show help for the plugin subcommand	
@	resources update
@	resources generate
s	splashes	
s	icons	
@	resources generate splashes
o	--background	Sets the background color of the splashscreen	v
a	1	0
#	resources generate splashes	1
t	filepaths
@	resources generate icons
a	1	0
#	resources generate icons	1
t	filepaths
@	prepare
s	android	Prepares your project for an Android build
s	ios	Prepares your project for an iOS build
o	--hmr	Enables the hot module replacement (HMR) feature	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--help|-h	Show help for the prepare subcommand	
@	prepare android
o	--hmr	Enables the hot module replacement (HMR) feature	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
@	prepare ios
o	--hmr	Enables the hot module replacement (HMR) feature	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
@	build
s	android	
s	ios	
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
o	--release	Produces a release build by running webpack in production mode and native build in release mode…	
o	--copy-to	Specifies the file path where the built .ipa|.apk will be copied. If it points to a non-existent…	v
o	--path	Specifies the directory where you want to create the project, if different from the current…	v
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--clean	Forces rebuilding the native application	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--hmr	Enables the hot module replacement (HMR) feature	
o	--justlaunch	Does not print the application output in the console	
o	--help|-h	Show help for the build subcommand	
=	build	--copy-to
t	folders
=	build	--path
t	folders
@	build android
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
o	--release	Produces a release build by running webpack in production mode and native build in release mode…	
o	--copy-to	Specifies the file path where the built .ipa|.apk will be copied. If it points to a non-existent…	v
o	--path	Specifies the directory where you want to create the project, if different from the current…	v
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--clean	Forces rebuilding the native application	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--aab	Specifies that the command will produce and deploy an Android App Bundle	
o	--env.snapshot	Creates a V8 Snapshot decreasing the app start time (only for release builds for Android)	
o	--env.compileSnapshot	Compiles the static assets produced by --env.snapshot into .so files allowing the native build to…	
o	--env.appComponents	Allows passing additional App Components for android	
o	--compileSdk	Sets the Android SDK that will be used to build the project	v
o	--key-store-path	Specifies the file path to the keystore file (P12) which you want to use to code sign your APK	v
o	--key-store-password	Provides the password for the keystore file specified with --key-store-path	v
o	--key-store-alias	Provides the alias for the keystore file specified with --key-store-path	v
o	--key-store-alias-password	Provides the password for the alias specified with --key-store-alias-password	v
=	build android	--copy-to
t	folders
=	build android	--path
t	folders
=	build android	--key-store-path
t	filepaths
@	build ios
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
o	--release	Produces a release build by running webpack in production mode and native build in release mode…	
o	--copy-to	Specifies the file path where the built .ipa|.apk will be copied. If it points to a non-existent…	v
o	--path	Specifies the directory where you want to create the project, if different from the current…	v
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--clean	Forces rebuilding the native application	
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--for-device	Produces an application package that you can deploy on device. Otherwise, produces a build that…	
o	--i-cloud-container-environment	Adds the passed iCloudContainerEnvironment when exporting an application package with the…	
o	--team-id	If used without parameter, lists all team names and ids. If used with team name or id, it will…	V
o	--provision	If used without parameter, lists all eligible provisioning profiles. If used with UUID or name of…	V
=	build ios	--copy-to
t	folders
=	build ios	--path
t	folders
@	deploy
s	android	
s	ios	
o	--help|-h	Show help for the deploy subcommand	
@	deploy android
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--clean	Forces rebuilding the native application	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--release	Produces a release build by running webpack in production mode and native build in release mode…	
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
o	--aab	Specifies that the command will produce and deploy an Android App Bundle	
o	--env.snapshot	Creates a V8 Snapshot decreasing the app start time (only for release builds for Android)	
o	--env.compileSnapshot	Compiles the static assets produced by --env.snapshot into .so files allowing the native build to…	
o	--env.appComponents	Allows passing additional App Components for android	
o	--key-store-path	Specifies the file path to the keystore file (P12) which you want to use to code sign your APK	v
o	--key-store-password	Provides the password for the keystore file specified with --key-store-path	v
o	--key-store-alias	Provides the alias for the keystore file specified with --key-store-path	v
o	--key-store-alias-password	Provides the password for the alias specified with --key-store-alias-password	v
=	deploy android	--key-store-path
t	filepaths
@	deploy ios
o	--device	Specifies a connected device/emulator to start and run the app	v
o	--clean	Forces rebuilding the native application	
o	--force	Skips the application compatibility checks and forces npm i to ensure all dependencies are installed	
o	--release	Produces a release build by running webpack in production mode and native build in release mode…	
o	--env.aot	Creates an Ahead-Of-Time build (Angular only)	
o	--env.uglify	Provides basic obfuscation and smaller app size	
o	--env.report	Creates a Webpack report inside a /report folder in the root folder	
o	--env.sourceMap	Creates inline source maps	
o	--env.hiddenSourceMap	Creates sources maps in the root folder (useful for Crashlytics usage with bundled app in release)	
o	--env.verbose	Prints verbose logs and the internal config before building	
o	--env.production	Enable production mode (will minify the code)	
o	--env.replace=from:to	Add file replacement rules. For source files (.js and .ts) this will add a new alias to the…	=
@	install
s	typescript	Enable TypeScript support
o	--path	Specifies the directory which contains the package.json file, if different from the current…	v
o	--help|-h	Show help for the install subcommand	
a	1	0
=	install	--path
t	folders
@	install typescript
@	appstore
s	upload	Uploads project to iTunes Connect. The command either issues a production build and uploads it to…
o	--team-id	Specifies the team id for which Xcode will try to find distribution certificate and provisioning…	v
o	--help|-h	Show help for the appstore subcommand	
a	2	0
@	appstore upload
o	--ipa	Use the provided .ipa file instead of building the project	v
o	--appleApplicationSpecificPassword	Specifies the password for accessing the information you store in iTunes Transporter application	v
o	--appleSessionBase64	The session that will be used instead of triggering a new login each time NativeScript CLI…	v
a	4	0
=	appstore upload	--ipa
t	filepaths
@	device
s	android	Lists all recognized connected Android physical and running Android virtual devices
s	ios	Lists all recognized connected iOS devices with serial number and index
s	log	Opens the device log stream for a selected connected device
s	list-applications	Lists the installed applications on all connected Android or iOS devices
s	run	Runs the selected application on a connected Android or iOS device
o	--available-devices	Lists all available devices	
o	--json	Show the output of the command in JSON format	
o	--help|-h	Show help for the device subcommand	
@	device android
o	--timeout	Sets the number of seconds that the NativeScript CLI will wait for the debugger to boot. If not…	v
o	--available-devices	Lists all available Android devices	
o	--json	Show the output of the command in JSON format	
@	device ios
o	--timeout	Sets the number of seconds that the NativeScript CLI will wait for the debugger to boot. If not…	v
o	--available-devices	Lists all available iOS devices	
o	--json	Show the output of the command in JSON format	
@	device log
o	--device	Specifies a connected device/emulator to start and run the app	v
@	device list-applications
o	--device	Specifies a connected device/emulator to start and run the app	v
@	device run
o	--device	Specifies a connected device/emulator to start and run the app	v
a	1	0
