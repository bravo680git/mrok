@	
o	-usage	Print brief usage	
o	-help	Print complete usage	
o	-verbose	Provide additional status output	
o	-license	Show the Xcode and SDK license agreements	
o	-checkFirstLaunchStatus	Check if any First Launch tasks need to be performed	
o	-runFirstLaunch	Install packages and agree to the license	
o	-project	Build the project NAME	v
o	-target	Build the target NAME	v
o	-alltargets	Build all targets	
o	-workspace	Build the workspace NAME	v
o	-scheme	Build the scheme NAME	v
o	-configuration	Use the build configuration NAME for building each target	v
o	-xcconfig	Apply the build settings defined in the file at PATH as overrides	v
o	-arch	Build each target for the architecture ARCH; this will override architectures defined in the project	v
o	-sdk	Use SDK as the name or path of the base SDK when building the project	v
o	-toolchain	Use the toolchain with identifier or name NAME	v
o	-destination	Use the destination described by DESTINATIONSPECIFIER (a comma-separated set of key=value pairs…	v
o	-destination-timeout	Wait for TIMEOUT seconds while searching for the destination device	v
o	-parallelizeTargets	Build independent targets in parallel	
o	-jobs	Specify the maximum number of concurrent build operations	v
o	-maximum-concurrent-test-device-destinations	The maximum number of device destinations to test on concurrently	v
o	-maximum-concurrent-test-simulator-destinations	The maximum number of simulator destinations to test on concurrently	v
o	-parallel-testing-enabled	Overrides the per-target setting in the scheme	v
o	-parallel-testing-worker-count	The exact number of test runners that will be spawned during parallel testing	v
o	-maximum-parallel-testing-workers	The maximum number of test runners that will be spawned during parallel testing	v
o	-dry-run	Do everything except actually running the commands	
o	-quiet	Do not print any output except for warnings and errors	
o	-hideShellScriptEnvironment	Don't show shell script environment variables in build log	
o	-showsdks	Display a compact list of the installed SDKs	
o	-showdestinations	Display a list of destinations	
o	-showTestPlans	Display a list of test plans	
o	-showBuildSettings	Display a list of build settings and values	
o	-showBuildSettingsForIndex	Display build settings for the index service	
o	-list	Lists the targets and configurations in a project, or the schemes in a workspace	
o	-find-executable	Display the full path to executable NAME in the provided SDK and toolchain	v
o	-find-library	Display the full path to library NAME in the provided SDK and toolchain	v
o	-version	Display the version of Xcode; with -sdk will display info about one or all installed SDKs	
o	-enableAddressSanitizer	Turn the address sanitizer on or off	v
o	-enableThreadSanitizer	Turn the thread sanitizer on or off	v
o	-enableUndefinedBehaviorSanitizer	Turn the undefined behavior sanitizer on or off	v
o	-resultBundlePath	Specifies the directory where a result bundle describing what occurred will be placed	v
o	-resultStreamPath	Specifies the file where a result stream will be written to (the file must already exist)	v
o	-resultBundleVersion	Specifies which result bundle version should be used	v
o	-clonedSourcePackagesDirPath	Specifies the directory to which remote source packages are fetch or expected to be found	v
o	-derivedDataPath	Specifies the directory where build products and other derived data will go	v
o	-archivePath	Specifies the directory where any created archives will be placed, or the archive that should be…	v
o	-exportArchive	Specifies that an archive should be exported	
o	-exportNotarizedApp	Export an archive that has been notarized by Apple	
o	-exportOptionsPlist	Specifies a path to a plist file that configures archive exporting	v
o	-enableCodeCoverage	Turn code coverage on or off when testing	v
o	-exportPath	Specifies the destination for the product exported from an archive	v
o	-skipUnavailableActions	Specifies that scheme actions that cannot be performed should be skipped instead of causing a…	
o	-exportLocalizations	Exports completed and outstanding project localizations	
o	-importLocalizations	Imports localizations for a project, assuming any necessary localized resources have been created…	
o	-localizationPath	Specifies a path to XLIFF localization file	v
o	-exportLanguage	Specifies multiple optional ISO 639-1 languages included in a localization export	v
o	-xcroot	Specifies a path to a .xcroot to use for building and/or testing	v
o	-xctestrun	Specifies a path to a test run specification	v
o	-testPlan	Specifies the name of the test plan associated with the scheme to use for testing	v
o	-only-testing	Constrains testing by specifying tests to include, and excluding other tests	
o	-only-testing:	Constrains testing by specifying tests to include, and excluding other tests	v
o	-skip-testing	Constrains testing by specifying tests to exclude, but including other tests	
o	-skip-testing:	Constrains testing by specifying tests to exclude, but including other tests	v
o	-test-timeouts-enabled	Enable or disable test timeout behavior	v
o	-default-test-execution-time-allowance	The default execution time an individual test is given to execute, if test timeouts are enabled	v
o	-maximum-test-execution-time-allowance	The maximum execution time an individual test is given to execute, regardless of the test's…	v
o	-only-test-configuration	Constrains testing by specifying test configurations to include, and excluding other test…	
o	-skip-test-configuration	Constrains testing by specifying test configurations to exclude, but including other test…	
o	-testLanguage	Constrains testing by specifying ISO 639-1 language in which to run the tests	
o	-testRegion	Constrains testing by specifying ISO 3166-1 region in which to run the tests	
o	-resolvePackageDependencies	Resolves any Swift package dependencies referenced by the project or workspace	
o	-disableAutomaticPackageResolution	Prevents packages from automatically being resolved to versions other than those recorded in the…	
o	-json	Output as JSON	
o	-allowProvisioningUpdates	Allow xcodebuild to communicate with the Apple Developer website. For automatically signed…	
o	-allowProvisioningDeviceRegistration	Allow xcodebuild to register your destination device on the developer portal if necessary. This…	
o	-scmProvider	Which implementation to use for Git operations (system/xcode)	v
o	-showBuildTimingSummary	Display a report of the timings of all the commands invoked during the build	
o	-create-xcframework	Create an xcframework from prebuilt libraries; -help for more information	
o	build	Build the target in the build root (SYMROOT). This is the default build action	
o	installsrc	Copy the source of the project to the source root (SRCROOT)	
o	install	Build the target and install it into the target's installation directory in the distribution root…	
o	clean	Remove build products and intermediate files from the build root (SYMROOT)	
=		-workspace
t	filepaths
=		-xcconfig
t	filepaths
=		-arch
v	x86_64	
v	arm64	
v	armv7	
=		-sdk
t	folders
=		-destination
t	folders
=		-parallel-testing-enabled
v	YES	
v	NO	
=		-enableAddressSanitizer
v	YES	
v	NO	
=		-enableThreadSanitizer
v	YES	
v	NO	
=		-enableUndefinedBehaviorSanitizer
v	YES	
v	NO	
=		-resultBundlePath
t	folders
=		-resultStreamPath
t	filepaths
=		-clonedSourcePackagesDirPath
t	folders
=		-derivedDataPath
t	folders
=		-archivePath
t	folders
=		-exportOptionsPlist
t	filepaths
=		-enableCodeCoverage
v	YES	
v	NO	
=		-exportPath
t	folders
=		-localizationPath
t	filepaths
=		-xcroot
t	folders
=		-xctestrun
t	folders
=		-test-timeouts-enabled
v	YES	
v	NO	
=		-scmProvider
v	system	
v	xcode	
