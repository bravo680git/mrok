@	
s	analyze	Analyze the project's Dart code
s	assemble	Assemble and build Flutter resources
s	attach	Attach to a running app
s	bash-completion	Output command line shell completion setup scripts
s	build	Build an executable app or install bundle
s	channel	List or switch Flutter channels
s	clean	Delete the build/ and .dart_tool/ directories
s	config	Configure Flutter settings
s	create	Create a new Flutter project
s	devices	List all connected devices
s	doctor	Show information about the installed tooling
s	downgrade	Downgrade Flutter to the last active version for the current channel
s	drive	Run integration tests for the project on an attached device or emulator
s	emulators	List, launch and create emulators
s	format	Format one or more Dart files
s	gen-l10n	Generate localizations for the current project
s	install	Install a Flutter app on an attached device
s	logs	Show log output for running Flutter apps
s	pub	Commands for managing Flutter packages
s	run	Run your Flutter app on an attached device
s	screenshot	Take a screenshot from a connected device
s	symbolize	Symbolize a stack trace from an AOT-compiled Flutter app
s	test	Run Flutter unit tests for the current project
s	upgrade	Upgrade your copy of Flutter
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
=		-d
d
@	analyze
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--current-package	Analyze the current project, if applicable	
o	--no-current-package	Don't analyze the current project, if applicable	
o	--watch	Run analysis continuously, watching the filesystem for changes	
o	--write	Also output the results to a file. This is useful with --watch if you want a file to always…	v
o	--pub	Run 'flutter pub get' before executing this command	
o	--no-pub	Don't run 'flutter pub get' before executing this command	
o	--congratulate	Show output even when there are no errors, warnings, hints, or lints. Ignored if --watch is…	
o	--no-congratulate	Hide output even when there are no errors, warnings, hints, or lints. Ignored if --watch is…	
o	--preamble	When analyzing the flutter repository, display the number of files that will be analyzed. Ignored…	
o	--no-preamble	When analyzing the flutter repository, don't display the number of files that will be analyzed…	
o	--fatal-infos	Treat info level issues as fatal	
o	--no-fatal-infos	Don't treat info level issues as fatal	
o	--fatal-warnings	Treat warning level issues as fatal	
o	--no-fatal-warnings	Don't treat warning level issues as fatal	
=	analyze	-d
d
=	analyze	--write
t	filepaths
@	assemble
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	-d|--define	Allows passing configuration to a target with --define=target=key=value	
o	--performance-measurement-file	Output individual target performance to a JSON file	
o	-i|--input	Treat warning level issues as fatal	
o	--depfile	A file path where a depfile will be written. This contains all build inputs and outputs in a make…	
o	--build-inputs	A file path where a newline separated file containing all inputs used will be written after a…	
o	--build-outputs	A file path where a newline separated file containing all outputs used will be written after a…	
o	-o|--output	A directory where output files will be written. Must be either absolute or relative from the root…	
o	--ExtraGenSnapshotOptions		
o	--ExtraFrontEndOptions		
o	--DartDefines		
o	--resource-pool-size	The maximum number of concurrent tasks the build system will run	
=	assemble	-d
d
@	attach
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--debug	Build a debug version of your app (default mode)	
o	--profile	Build a version of your app specialized for performance profiling	
o	-t|--target	The main entry-point file of the application, as run on the device. If the --target option is…	v
o	--observatory-port	(deprecated use host-vmservice-port instead) Listen to the given port for an observatory debugger…	
o	--device-vmservice-port	Look for vmservice connections only from the specified port. Specifying port 0 (the default) will…	
o	--host-vmservice-port	When a device-side vmservice port is forwarded to a host-side port, use this value as the host…	
o	--dart-define	Additional key-value pairs that will be available as constants from the String.fromEnvironment…	v
o	--device-user	Identifier number for a user or work profile on Android only. Run "adb shell pm list users" for…	v
o	--null-assertions	Perform additional null assertions on the boundaries of migrated and un-migrated code. This…	
o	--no-null-assertions	Not performing additional null assertions on the boundaries of migrated and un-migrated code. This…	
o	--debug-uri	The URI at which the observatory is listening	
o	--app-id	The package name (Android) or bundle identifier (iOS) for the app. This can be specified to avoid…	
o	--pid-file	Specify a file to write the process id to. You can send SIGUSR1 to trigger a hot reload and…	
o	--track-widget-creation	Track widget creation locations. This enables features such as the widget inspector. This…	
o	--no-track-widget-creation	No tracking widget creation locations. This disables features such as the widget inspector. This…	
o	--dds-port	When this value is provided, the Dart Development Service (DDS) will be bound to the provided…	
o	--devtools-server-address	When this value is provided, the Flutter tool will not spin up a new DevTools server instance, but…	
o	--device-timeout	Time in seconds to wait for devices to attach. Longer timeouts may be necessary for networked…	v
=	attach	-d
d
=	attach	-t
t	filepaths
@	bash-completion
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--overwrite	When performing operations, overwrite existing files	
o	--no-overwrite		
=	bash-completion	-d
d
@	build
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	-t|--target	The main entry-point file of the application, as run on the device.	v
a	1	0
=	build	-d
d
=	build	-t
d
#	build	1
v	aar	Build a repository containing an AAR and a POM file
v	apk	Build an Android APK file from your app
v	appbundle	Build an Android App Bundle file from your app
v	bundle	Build the Flutter assets directory from your app
v	ios	Build an iOS application bundle (Mac OS X host only)
v	ios-framework	Produces .xcframeworks for a Flutter project and its plugins for integration into existing, plain…
v	ipa	Build an iOS archive bundle (Mac OS X host only)
v	web	Build a web application bundle
@	channel
a	1	0
#	channel	1
d
@	clean
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
=	clean	-d
d
@	config
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--analytics	Enable reporting anonymously tool usage statistics and crash reports	
o	--no-analytics	Disable reporting anonymously tool usage statistics and crash reports	
o	--clear-ios-signing-cert	Clear the saved development certificate choice used to sign apps for iOS device deployment	
o	--android-sdk	The Android SDK directory	
o	--android-studio-dir	The Android Studio install directory	
o	--build-dir	The relative path to override a projects build directory	v
o	--enable-web	Enable Flutter for web. This setting will take effect on the master, dev, beta, and stable channels	
o	--no-enable-web	Disable Flutter for web. This setting will take effect on the master, dev, beta, and stable channels	
o	--enable-linux-desktop	Enable beta-quality support for desktop on Linux. This setting will take effect on the master…	
o	--no-enable-linux-desktop	Disable beta-quality support for desktop on Linux. This setting will take effect on the master…	
o	--enable-macos-desktop	Enable beta-quality support for desktop on macOS. This setting will take effect on the master…	
o	--no-enable-macos-desktop	Disable beta-quality support for desktop on macOS. This setting will take effect on the master…	
o	--enable-windows-desktop	Enable beta-quality support for desktop on Windows. This setting will take effect on the master…	
o	--no-enable-windows-desktop	Disable beta-quality support for desktop on Windows. This setting will take effect on the master…	
o	--single-widget-reload-optimization	Enable Hot reload optimization for changes to class body of a single widget. This setting will…	
o	--no-single-widget-reload-optimization	Disable Hot reload optimization for changes to class body of a single widget. This setting will…	
o	--enable-android	Enable Flutter for Android. This setting will take effect on the master, dev, beta, and stable…	
o	--no-enable-android	Disable Flutter for Android. This setting will take effect on the master, dev, beta, and stable…	
o	--enable-ios	Enable Flutter for iOS. This setting will take effect on the master, dev, beta, and stable channels	
o	--no-enable-ios	Disable Flutter for iOS. This setting will take effect on the master, dev, beta, and stable channels	
o	--enable-fuchsia	Enable Flutter for Fuchsia. This setting will take effect on the master channel	
o	--no-enable-fuchsia	Disable Flutter for Fuchsia. This setting will take effect on the master channel	
o	--experimental-invalidation-strategy	Enable Hot reload optimization that reduces incremental artifact size. This setting will take…	
o	--no-experimental-invalidation-strategy	Disable Hot reload optimization that reduces incremental artifact size. This setting will take…	
o	--clear-features	Remove all configured features and restore them to the default values	
=	config	-d
d
=	config	--build-dir
t	folders
@	create
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--pub	Run 'flutter pub get' before executing this command	
o	--no-pub	Don't run 'flutter pub get' before executing this command	
o	--offline	When "flutter pub get" is run by the create command, this indicates whether to run it in offline…	
o	--no-offline		
o	--with-driver-test	(Deprecated) Also add a flutter_driver dependency and generate a sample 'flutter drive' test. This…	
o	--no-with-driver-test		
o	--overwrite	When performing operations, overwrite existing files	
o	--no-overwrite		
o	--description	The description to use for your new Flutter project. This string ends up in the pubspec.yaml file…	
o	--org	The organization responsible for your new Flutter project, in reverse domain name notation. This…	
o	--project-name	The project name for this new Flutter project. This must be a valid dart package name	
o	-i|--ios-language	[objc, swift (default)]	v
o	-a|--android-language	[java, kotlin (default)]	v
o	--platforms	The platforms supported by this project. This argument only works when the --template is set to…	v
o	-t|--template	Specify the type of project to create. [app] (default) Generate a Flutter application. [module]…	v
o	-s|--sample	Specifies the Flutter code sample to use as the main.dart for an application. Implies…	v
o	--list-samples	Specifies a JSON output file for a listing of Flutter code samples that can be created with --sample	v
=	create	-d
d
=	create	-i
v	objc	
v	swift (default)	
=	create	-a
v	java	
v	kotlin (default)	
=	create	--platforms
v	web	
v	macos	
v	linux	
v	windows	
v	android	
v	ios	
=	create	-t
v	app (default)	
v	module	
v	package	
v	plugin	
=	create	--list-samples
t	filepaths
@	devices
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--machine	Output device information in machine readable structured JSON format	
o	-t|--timeout	(deprecated) Use --device-timeout instead	
o	--device-timeout	Time in seconds to wait for devices to attach. Longer timeouts may be necessary for networked…	v
=	devices	-d
d
@	doctor
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--android-licenses	Run the Android SDK manager tool to accept the SDK's licenses	
=	doctor	-d
d
@	downgrade
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
=	downgrade	-d
d
@	drive
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--debug	Build a debug version of your app (default mode)	
o	--profile	Build a version of your app specialized for performance profiling	
o	--release	Build a release version of your app	
o	--dart-define	Additional key-value pairs that will be available as constants from the String.fromEnvironment…	v
o	--flavor	Build a custom app flavor as defined by platform-specific build setup. Supports the use of product…	
o	--web-renderer	The renderer implementation to use when building for the web. Possible values are: html - always…	
o	--trace-startup	Trace application startup, then exit, saving the trace to a file	
o	--verbose-system-logs	Include verbose logging from the flutter engine	
o	--cache-sksl	Only cache the shader in SkSL instead of binary or GLSL	
o	--dump-skp-on-shader-compilation	Automatically dump the skp that triggers new shader compilations. This is useful for writing…	
o	--purge-persistent-cache	Removes all existing persistent caches. This allows reproducing shader compilation jank that…	
o	--route	Which route to load when running the app	
o	--vmservice-out-file	A file to write the attached vmservice uri to after an application is started. e.g…	v
o	--use-application-binary	Specify a pre-built application binary to use when running. For android applications, this must be…	v
o	--endless-trace-buffer	Enable tracing to the endless tracer. This is useful when recording huge amounts of traces. If we…	
o	--trace-systrace	Enable tracing to the system tracer. This is only useful on platforms where such a tracer is…	
o	--trace-skia	Enable tracing of Skia code. This is useful when debugging the raster thread (formerly known as…	
o	-a|--dart-entrypoint-args	Pass a list of arguments to the Dart entrypoint at application startup. By default this is…	
o	-t|--target	The main entry-point file of the application, as run on the device. If the --target option is…	v
o	--observatory-port	(deprecated use host-vmservice-port instead) Listen to the given port for an observatory debugger…	
o	--device-vmservice-port	Look for vmservice connections only from the specified port. Specifying port 0 (the default) will…	
o	--host-vmservice-port	When a device-side vmservice port is forwarded to a host-side port, use this value as the host…	
o	--pub	Run 'flutter pub get' before executing this command	
o	--no-pub	Don't run 'flutter pub get' before executing this command	
o	--track-widget-creation	Track widget creation locations. This enables features such as the widget inspector. This…	
o	--no-track-widget-creation	No tracking widget creation locations. This disables features such as the widget inspector. This…	
o	--null-assertions	Perform additional null assertions on the boundaries of migrated and un-migrated code. This…	
o	--no-null-assertions	Not performing additional null assertions on the boundaries of migrated and un-migrated code. This…	
o	--device-user	Identifier number for a user or work profile on Android only. Run "adb shell pm list users" for…	v
o	--device-timeout	Time in seconds to wait for devices to attach. Longer timeouts may be necessary for networked…	v
o	--dds-port	When this value is provided, the Dart Development Service (DDS) will be bound to the provided…	
o	--devtools-server-address	When this value is provided, the Flutter tool will not spin up a new DevTools server instance, but…	
o	--keep-app-running	Will keep the Flutter application running when done testing. By default, "flutter drive" stops the…	
o	--no-keep-app-running		
o	--use-existing-app	Connect to an already running instance via the given observatory URL. If this option is given, the…	v
o	--driver	The test file to run on the host (as opposed to the target file to run on the device). By default…	v
o	--build	(Deprecated) Build the app before running. To use an existing app, pass the…	
o	--no-build		
o	--driver-port	The port where Webdriver server is launched at. Defaults to 4444	v
o	--headless	Whether the driver browser is going to be launched in headless mode. Defaults to true	
o	--no-headless		
o	--browser-name	Name of browser where tests will be executed. Following browsers are supported: Chrome, Firefox…	
o	--browser-dimension	The dimension of browser when running Flutter Web test. This will affect screenshot and all…	
o	--android-emulator	Whether to perform Flutter Driver testing on Android Emulator.Works only if 'browser-name' is set…	
o	--no-android-emulator		
o	--chrome-binary	Location of Chrome binary. Works only if 'browser-name' is set to 'chrome'	
o	--write-sksl-on-exit	Attempts to write an SkSL file when the drive process is finished to the provided file…	
o	--test-arguments	Additional arguments to pass to the Dart VM running The test script	
=	drive	-d
d
=	drive	--vmservice-out-file
t	filepaths
=	drive	--use-application-binary
t	filepaths
=	drive	-t
t	filepaths
@	emulators
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--launch	The full or partial ID of the emulator to launch	v
o	--create	Creates a new Android emulator based on a Pixel device	
o	--name	Used with flag --create. Specifies a name for the emulator being created	
=	emulators	-d
d
=	emulators	--launch
d
@	format
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	-n|--dry-run	Show which files would be modified but make no changes	
o	--set-exit-if-changed	Return exit code 1 if there are any formatting changes	
o	-m|--machine	Produce machine-readable JSON output	
o	-l|--line-length	Wrap lines longer than this length. Defaults to 80 characters. (defaults to "80")	
=	format	-d
d
@	gen-l10n
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--arb-dir	The directory where the template and translated arb files are located. (defaults to "lib/l10n")	
o	--output-dir	The directory where the generated localization classes will be written if the synthetic-package…	
o	--template-arb-file	The template arb file that will be used as the basis for generating the Dart localization and…	
o	--output-localization-file	The filename for the output localization and localizations delegate classes. (defaults to…	
o	--untranslated-messages-file	The location of a file that describes the localization messages have not been translated yet…	
o	--output-class	The Dart class name to use for the output localization and localizations delegate classes…	
o	--preferred-supported-locales	The list of preferred supported locales for the application. By default, the tool will generate…	v
o	--header	The header to prepend to the generated Dart localizations files. This option takes in a string…	
o	--header-file	The header to prepend to the generated Dart localizations files. The value of this option is the…	
o	--use-deferred-loading	Generate the Dart localization file with locales imported as deferred, allowing for lazy loading…	
o	--no-use-deferred-loading	Don't generate the Dart localization file with locales imported as deferred	
o	--gen-inputs-and-outputs-list	When specified, the tool generates a JSON file containing the tool's inputs and outputs named…	v
o	--synthetic-package	Determines that the generated output files will be generated as a synthetic package or at a…	
o	--no-synthetic-package		
o	--project-dir	When specified, the tool uses the path passed into this option as the directory of the root…	v
o	--required-resource-attributes	Requires all resource ids to contain a corresponding resource attribute.	
o	--no-required-resource-attributes		
=	gen-l10n	-d
d
=	gen-l10n	--gen-inputs-and-outputs-list
t	filepaths
=	gen-l10n	--project-dir
t	filepaths
@	install
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--device-user	Identifier number for a user or work profile on Android only. Run "adb shell pm list users" for…	v
o	--device-timeout	Time in seconds to wait for devices to attach. Longer timeouts may be necessary for networked…	v
=	install	-d
d
@	logs
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	-c|--clear	Clear log history before reading from logs	
o	--device-timeout	Time in seconds to wait for devices to attach. Longer timeouts may be necessary for networked…	v
=	logs	-d
d
@	pub
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	add	Add a dependency to pubspec.yaml	
o	cache	Work with the Pub system cache	
o	deps	Print package dependencies	
o	downgrade	Downgrade packages in a Flutter project	
o	get	Get packages in a Flutter project	
o	global	Work with Pub global packages	
o	login	Log into pub.dev	
o	logout	Log out of pub.dev	
o	outdated	Analyze dependencies to find which ones can be upgraded	
o	pub	Pass the remaining arguments to Dart's "pub" tool	
o	publish	Publish the current package to pub.dartlang.org	
o	remove	Removes a dependency from the current package	
o	run	Run an executable from a package	
o	test	Run the "test" package	
o	upgrade	Upgrade the current package's dependencies to latest versions	
o	uploader	Manage uploaders for a package on pub.dev	
o	version	Print Pub version	
=	pub	-d
d
@	run
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--debug	Build a debug version of your app (default mode)	
o	--profile	Build a version of your app specialized for performance profiling	
o	--release	Build a release version of your app	
o	--dart-define	Additional key-value pairs that will be available as constants from the String.fromEnvironment…	v
o	--flavor	Build a custom app flavor as defined by platform-specific build setup. Supports the use of product…	
o	--web-renderer	The renderer implementation to use when building for the web. Possible values are: html - always…	
o	--trace-startup	Trace application startup, then exit, saving the trace to a file	
o	--verbose-system-logs	Include verbose logging from the flutter engine	
o	--cache-sksl	Only cache the shader in SkSL instead of binary or GLSL	
o	--dump-skp-on-shader-compilation	Automatically dump the skp that triggers new shader compilations. This is useful for writing…	
o	--purge-persistent-cache	Removes all existing persistent caches. This allows reproducing shader compilation jank that…	
o	--route	Which route to load when running the app	
o	--vmservice-out-file	A file to write the attached vmservice uri to after an application is started. e.g…	v
o	--use-application-binary	Specify a pre-built application binary to use when running. For android applications, this must be…	v
o	--endless-trace-buffer	Enable tracing to the endless tracer. This is useful when recording huge amounts of traces. If we…	
o	--trace-systrace	Enable tracing to the system tracer. This is only useful on platforms where such a tracer is…	
o	--trace-skia	Enable tracing of Skia code. This is useful when debugging the raster thread (formerly known as…	
o	-a|--dart-entrypoint-args	Pass a list of arguments to the Dart entrypoint at application startup. By default this is…	
o	-t|--target	The main entry-point file of the application, as run on the device. If the --target option is…	v
o	--observatory-port	(deprecated use host-vmservice-port instead) Listen to the given port for an observatory debugger…	
o	--device-vmservice-port	Look for vmservice connections only from the specified port. Specifying port 0 (the default) will…	
o	--host-vmservice-port	When a device-side vmservice port is forwarded to a host-side port, use this value as the host…	
o	--pub	Run 'flutter pub get' before executing this command	
o	--no-pub	Don't run 'flutter pub get' before executing this command	
o	--track-widget-creation	Track widget creation locations. This enables features such as the widget inspector. This…	
o	--no-track-widget-creation	No tracking widget creation locations. This disables features such as the widget inspector. This…	
o	--null-assertions	Perform additional null assertions on the boundaries of migrated and un-migrated code. This…	
o	--no-null-assertions	Not performing additional null assertions on the boundaries of migrated and un-migrated code. This…	
o	--device-user	Identifier number for a user or work profile on Android only. Run "adb shell pm list users" for…	v
o	--device-timeout	Time in seconds to wait for devices to attach. Longer timeouts may be necessary for networked…	v
o	--dds-port	When this value is provided, the Dart Development Service (DDS) will be bound to the provided…	
o	--devtools-server-address	When this value is provided, the Flutter tool will not spin up a new DevTools server instance, but…	
o	--enable-software-rendering	Enable rendering using the Skia software backend. This is useful when testing Flutter on…	
o	--skia-deterministic-rendering	When combined with --enable-software-rendering, provides 100% deterministic Skia rendering	
o	--await-first-frame-when-tracing	Whether to wait for the first frame when tracing startup ("--trace-startup"), or just dump the…	
o	--no-await-first-frame-when-tracing		
o	--use-test-fonts	Enable (and default to) the "Ahem" font. This is a special font used in tests to remove any…	
o	--no-use-test-fonts		
o	--build	(Deprecated) Build the app before running. To use an existing app, pass the…	
o	--no-build		
o	--pid-file	Specify a file to write the process id to. You can send SIGUSR1 to trigger a hot reload and…	
o	--fast-start	Whether to quickly bootstrap applications with a minimal app. Currently this is only supported on…	
o	--no-fast-start		
=	run	-d
d
=	run	--vmservice-out-file
t	filepaths
=	run	--use-application-binary
t	filepaths
=	run	-t
t	filepaths
@	screenshot
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	-o|--out	Location to write the screenshot	v
o	--observatory-uri	The observatory URI to connect to. This is required when --type is "skia" or "rasterizer". To find…	v
o	--type	The type of screenshot to retrieve. [device] (default) Delegate to the device's native screenshot…	v
o	--device-timeout	Time in seconds to wait for devices to attach. Longer timeouts may be necessary for networked…	v
=	screenshot	-d
d
=	screenshot	-o
t	filepaths
=	screenshot	--type
v	device (default)	
v	rasterizer	
v	skia	
@	symbolize
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	-d|--debug-info	A path to the symbols file generated with "--split-debug-info". e.g. /out/android/app.arm64.symbols	v
o	-i|--input	A file path containing a Dart stack trace. e.g. /crashes/stack_trace.err	v
o	-o|--output		v
=	symbolize	-d
d
=	symbolize	-d
t	filepaths
=	symbolize	-i
t	filepaths
=	symbolize	-o
t	filepaths
@	test
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	--pub	Run 'flutter pub get' before executing this command	
o	--no-pub	Don't run 'flutter pub get' before executing this command	
o	--null-assertions	Perform additional null assertions on the boundaries of migrated and un-migrated code. This…	
o	--no-null-assertions	Not performing additional null assertions on the boundaries of migrated and un-migrated code. This…	
o	--track-widget-creation	Track widget creation locations. This enables features such as the widget inspector. This…	
o	--no-track-widget-creation	No tracking widget creation locations. This disables features such as the widget inspector. This…	
o	--dart-define	Additional key-value pairs that will be available as constants from the String.fromEnvironment…	v
o	--web-renderer	The renderer implementation to use when building for the web. Possible values are: html - always…	
o	--name	A regular expression matching substrings of the names of tests to run	v
o	--plain-name	A plain-text substring of the names of tests to run	v
o	-t|--tags	Run only tests associated with tags	
o	-x|--exclude-tags	Run only tests WITHOUT given tags	
o	--start-paused	Start in a paused mode and wait for a debugger to connect. You must specify a single test file to…	
o	--coverage	Whether to collect coverage information	
o	--merge-coverage	Whether to merge coverage data with "coverage/lcov.base.info". Implies collecting coverage data…	
o	--coverage-path	Where to store coverage information (if coverage is enabled). (defaults to "coverage/lcov.info")	
o	--update-goldens	Whether matchesGoldenFile() calls within your test methods should update the golden files rather…	
o	--j|--concurrency	The number of concurrent test processes to run. (defaults to "6")	v
o	--test-assets	Build the assets bundle for testing. Consider using --no-test-assets if assets are not required	
o	--no-test-assets	Exclude the assets bundle for build testing	
o	--test-randomize-ordering-seed	The seed to randomize the execution order of test cases. Must be a 32bit unsigned integer or…	
o	-r|--reporter	Set how to print test results.	v
o	--timeout	The default test timeout. For example: 15s, 2x, none. Defaults to "30s"	
o	--dds-port	When this value is provided, the Dart Development Service (DDS) will be bound to the provided…	
=	test	-d
d
=	test	-r
v	compact (default)	
v	expanded	
v	json	
@	upgrade
o	-h|--help	Print this usage information	
o	-v|--verbose	Noisy logging, including all shell commands executed. If used with --help, shows hidden options	
o	-d|--device-id	Target device id or name (prefixes allowed)	v
o	--suppress-analytics	Suppress analytics reporting when this command runs	
o	-f|--force	Force upgrade the flutter branch, potentially discarding local changes	
o	--verify-only	Verifies for any new flutter update, without fetching the update	
=	upgrade	-d
d
