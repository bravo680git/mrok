@	
s	doctor	[EXPERIMENTAL] Diagnose and fix common Node.js, iOS, Android & React Native issues
s	bundle	Builds the javascript bundle for offline use
s	init	Initialize a new React Native project named <projectName> in a directory of the same name
s	uninstall	Uninstall and unlink native dependencies
s	start	Starts the webserver
s	ram-bundle	Builds javascript as a "Random Access Module" bundle for offline use
s	link	Links assets and optionally native modules
s	upgrade	Upgrade your app's template files to the specified or latest npm version using `rn-diff-purge`…
s	info	Get relevant version info about OS, toolchain and libraries
s	install	Install and link native dependencies
s	config	Print CLI configuration
s	unlink	Unlink native dependency
s	log-ios	Starts iOS device syslog tail
s	profile-hermes	Pull and convert a Hermes tracing profile to Chrome tracing profile, then store it in the…
s	log-android	Starts logkitty
s	run-android	Builds your app and starts it on a connected Android emulator or device
s	run-ios	Builds your app and starts it on iOS simulator
o	--version	Print CLI version	
o	--verbose	Increase logging verbosity	
o	-h|--help	Output usage information	
@	doctor
o	--fix	Attempt to fix all diagnosed issues	
o	--contributor	Add healthchecks required to installations required for contributing to React Native	
o	-h|--help	Output usage information	
@	bundle
o	--entry-file	Path to the root JS file, either absolute or relative to JS root	v
o	--platform	Either "ios" or "android" (default: "ios")	v
o	--transformer	Specify a custom transformer to be used	v
o	--dev	If false, warnings are disabled and the bundle is minified (default: true)	V
o	--minify	Allows overriding whether bundle is minified. This defaults to false if dev is true, and true if…	V
o	--bundle-output	File name where to store the resulting bundle, ex. /tmp/groups.bundle	v
o	--bundle-encoding	Encoding the bundle should be written in (https://nodejs.org/api/buffer.html#buffer_buffer)…	v
o	--max-workers	Specifies the maximum number of workers the worker-pool will spawn for transforming files. This…	v
o	--sourcemap-output	File name where to store the sourcemap file for resulting bundle, ex. /tmp/groups.map	v
o	--sourcemap-sources-root	Path to make sourcemap's sources entries relative to, ex. /root/dir	v
o	--sourcemap-use-absolute-path	Report SourceMapURL using its full path	
o	--assets-dest	Directory name where to store assets referenced in the bundle	v
o	--unstable-transform-profile	Experimental, transform JS for a specific JS engine. Currently supported: hermes, hermes-canary…	v
o	--reset-cache	Removes cached files	
o	--read-global-cache	Try to fetch transformed JS code from the global cache, if configured	
o	--config	Path to the CLI configuration file	v
o	-h|--help	Output usage information	
=	bundle	--entry-file
d
=	bundle	--platform
v	android	
v	ios	
=	bundle	--dev
v	true	
v	false	
=	bundle	--minify
v	true	
v	false	
=	bundle	--bundle-encoding
v	utf8	
v	utf16le	
v	latin1	
=	bundle	--max-workers
d
=	bundle	--sourcemap-sources-root
t	folders
=	bundle	--assets-dest
t	folders
=	bundle	--unstable-transform-profile
v	hermes	
v	hermes-canary	
v	default	
=	bundle	--config
t	filepaths
@	init
o	--version	Shortcut for `--template react-native@version`	v
o	--template	Uses a custom template. Valid arguments are the ones supported by `yarn add [package]` or `npm…	v
o	--npm	Forces using npm for initialization	
o	--directory	Uses a custom directory instead of `<projectName>`	v
o	--title	Uses a custom app title name for application	v
o	--skip-install	Skips dependencies installation step	
o	-h|--help	Output usage information	
a	1	0
=	init	--directory
t	folders
@	uninstall
o	-h|--help	Output usage information	
a	1	0
@	start
o	--port	Port on which to listen to	v
o	--host	Change the default host	v
o	--projectRoot	Path to a custom project root	v
o	--watchFolders	Specify any additional folders to be added to the watch list	v
o	--assetPlugins	Specify any additional asset plugins to be used by the packager by full filepath	v
o	--sourceExts	Specify any additional source extensions to be used by the packager	v
o	--max-workers	Specifies the maximum number of workers the worker-pool will spawn for transforming files. This…	v
o	--transformer	Specify a custom transformer to be used	v
o	--reset-cache|--resetCache	Removes cached files	
o	--custom-log-reporter-path|--customLogReporterPath	Path to a JavaScript file that exports a log reporter as a replacement for TerminalReporter	v
o	--verbose	Enables logging	
o	--https	Enables https connections to the server	
o	--key	Path to custom SSL key	v
o	--cert	Path to custom SSL cert	v
o	--config	Path to the CLI configuration file	v
o	--no-interactive	Disables interactive mode	
o	-h|--help	Output usage information	
=	start	--projectRoot
t	folders
=	start	--watchFolders
t	folders
=	start	--assetPlugins
t	folders
=	start	--sourceExts
v	js	
v	css	
v	png	
v	xml	
=	start	--max-workers
d
=	start	--custom-log-reporter-path
d
=	start	--key
t	filepaths
=	start	--cert
t	filepaths
@	ram-bundle
o	--entry-file	Path to the root JS file, either absolute or relative to JS root	v
o	--platform	Either "ios" or "android" (default: "ios")	v
o	--transformer	Specify a custom transformer to be used	v
o	--dev	If false, warnings are disabled and the bundle is minified (default: true)	V
o	--minify	Allows overriding whether bundle is minified. This defaults to false if dev is true, and true if…	V
o	--bundle-output	File name where to store the resulting bundle, ex. /tmp/groups.bundle	v
o	--bundle-encoding	Encoding the bundle should be written in (https://nodejs.org/api/buffer.html#buffer_buffer)…	v
o	--max-workers	Specifies the maximum number of workers the worker-pool will spawn for transforming files. This…	v
o	--sourcemap-output	File name where to store the sourcemap file for resulting bundle, ex. /tmp/groups.map	v
o	--sourcemap-sources-root	Path to make sourcemap's sources entries relative to, ex. /root/dir	v
o	--sourcemap-use-absolute-path	Report SourceMapURL using its full path	
o	--assets-dest	Directory name where to store assets referenced in the bundle	v
o	--unstable-transform-profile	Experimental, transform JS for a specific JS engine. Currently supported: hermes, hermes-canary…	v
o	--reset-cache	Removes cached files	
o	--read-global-cache	Try to fetch transformed JS code from the global cache, if configured	
o	--config	Path to the CLI configuration file	v
o	--indexed-ram-bundle	Force the "Indexed RAM" bundle file format, even when building for android	
o	-h|--help	Output usage information	
=	ram-bundle	--entry-file
d
=	ram-bundle	--platform
v	android	
v	ios	
=	ram-bundle	--dev
v	true	
v	false	
=	ram-bundle	--minify
v	true	
v	false	
=	ram-bundle	--bundle-encoding
v	utf8	
v	utf16le	
v	latin1	
=	ram-bundle	--max-workers
d
=	ram-bundle	--sourcemap-sources-root
t	folders
=	ram-bundle	--assets-dest
t	folders
=	ram-bundle	--unstable-transform-profile
v	hermes	
v	hermes-canary	
v	default	
@	link
o	--platforms	Scope linking to specified platforms	V
o	--all	Link all native modules and assets	
o	-h|--help	Output usage information	
a	1	0
@	upgrade
o	-h|--help	Output usage information	
a	1	0
@	info
o	-h|--help	Output usage information	
@	install
o	-h|--help	Output usage information	
a	1	0
@	config
o	-h|--help	Output usage information	
@	unlink
o	--platforms	Scope unlinking to specified platforms	V
o	-h|--help	Output usage information	
a	1	0
@	log-ios
o	-h|--help	Output usage information	
@	profile-hermes
o	--filename	File name of the profile to be downloaded, eg. sampling-profiler-trace8593107139682635366.cpuprofile	v
o	--raw	Pulls the original Hermes tracing profile without any transformation	
o	--sourcemap-path	The local path to your source map file, eg. /tmp/sourcemap.json	v
o	--generate-sourcemap	Generates the JS bundle and source map	
o	--port	Default: "8081"	v
o	-h|--help	Output usage information	
a	1	0
=	profile-hermes	--filename
t	filepaths
=	profile-hermes	--sourcemap-path
t	filepaths
#	profile-hermes	1
t	folders
@	log-android
o	-h|--help	Output usage information	
@	run-android
o	--root	[DEPRECATED - root is discovered automatically] Override the root directory for the android build…	v
o	--variant	Specify your app's build variant (default: "debug")	v
o	--appFolder	[DEPRECATED – use "project.android.appName" in react-native.config.js] Specify a different…	v
o	--appId	Specify an applicationId to launch after build. If not specified, `package` from…	v
o	--appIdSuffix	Specify an applicationIdSuffix to launch after build. (default: "")	v
o	--main-activity	Name of the activity to start (default: "MainActivity")	v
o	--deviceId	Builds your app and starts it on a specific device/simulator with the given device id (listed by…	v
o	--no-packager	Do not launch packager while building	
o	--port	Default: 8081	v
o	--terminal	Launches the Metro Bundler in a new window using the specified terminal path. (default…	v
o	--tasks	Run custom Gradle tasks. By default it's "installDebug"	v
o	--no-jetifier	Do not run "jetifier" – the AndroidX transition tool. By default it runs before Gradle to ease…	
o	-h|--help	Output usage information	
=	run-android	--root
t	folders
=	run-android	--variant
v	debug	
v	release	
=	run-android	--appFolder
t	folders
=	run-android	--deviceId
d
=	run-android	--tasks
d
@	run-ios
o	--simulator	Explicitly set simulator to use. Optionally include iOS version between parenthesis at the end to…	v
o	--configuration	Explicitly set the scheme configuration to use (default: "Debug")	v
o	--scheme	Explicitly set Xcode scheme to use	v
o	--project-path	Path relative to project root where the Xcode project (.xcodeproj) lives. (default: "ios")	v
o	--device	Explicitly set device to use by name	V
o	--udid	Explicitly set device to use by udid	v
o	--no-packager	Do not launch packager while building	
o	--verbose	Do not use xcpretty even if installed	
o	--port	Default: 8081	v
o	--terminal	Launches the Metro Bundler in a new window using the specified terminal path. (default…	v
o	-h|--help	Output usage information	
=	run-ios	--simulator
d
=	run-ios	--configuration
d
=	run-ios	--scheme
d
=	run-ios	--project-path
t	folders
=	run-ios	--device
d
=	run-ios	--udid
d
