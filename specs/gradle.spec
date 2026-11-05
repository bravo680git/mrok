@	
s	build	Compute all outputs
s	run	Run applications
s	check	Run all checks
s	clean	Clear the contents of the build directory
s	projects	List of all sub-projects
s	tasks	List of main tasks of the selected project
s	help	Display task usage information
s	dependencies	Gives you a list of the dependencies of the selected project, broken down by configuration
s	buildEnvironment	Visualises the buildscript dependencies of the selected project
s	dependencyInsight	Gives you an insight into a particular dependency (or dependencies) that match specified input
s	properties	Gives you a list of the properties of the selected project
s	--status	(Standalone command) List running and recently stopped Gradle daemons. Only displays daemons of…
s	--stop	(Standalone command) Stop all Gradle Daemons of the same version
s	init	Create new Gradle builds, with new or existing projects
s	wrapper	Generates a script, gradlew, that invokes a declared version of Gradle, downloading it beforehand…
s	test	Run a test task
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
a	1	1
=		--priority
v	normal	
v	low	
=		-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=		-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=		--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=		-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=		--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=		-b
t	filepaths
=		-c
t	filepaths
=		-g
t	folders
=		-p
t	folders
=		--project-cache-dir
t	folders
=		-Dorg.gradle.java.home
t	folders
@	build
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	build	--priority
v	normal	
v	low	
=	build	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	build	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	build	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	build	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	build	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	build	-b
t	filepaths
=	build	-c
t	filepaths
=	build	-g
t	folders
=	build	-p
t	folders
=	build	--project-cache-dir
t	folders
=	build	-Dorg.gradle.java.home
t	folders
@	run
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	run	--priority
v	normal	
v	low	
=	run	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	run	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	run	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	run	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	run	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	run	-b
t	filepaths
=	run	-c
t	filepaths
=	run	-g
t	folders
=	run	-p
t	folders
=	run	--project-cache-dir
t	folders
=	run	-Dorg.gradle.java.home
t	folders
@	check
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	check	--priority
v	normal	
v	low	
=	check	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	check	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	check	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	check	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	check	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	check	-b
t	filepaths
=	check	-c
t	filepaths
=	check	-g
t	folders
=	check	-p
t	folders
=	check	--project-cache-dir
t	folders
=	check	-Dorg.gradle.java.home
t	folders
@	clean
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	clean	--priority
v	normal	
v	low	
=	clean	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	clean	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	clean	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	clean	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	clean	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	clean	-b
t	filepaths
=	clean	-c
t	filepaths
=	clean	-g
t	folders
=	clean	-p
t	folders
=	clean	--project-cache-dir
t	folders
=	clean	-Dorg.gradle.java.home
t	folders
@	projects
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	projects	--priority
v	normal	
v	low	
=	projects	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	projects	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	projects	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	projects	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	projects	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	projects	-b
t	filepaths
=	projects	-c
t	filepaths
=	projects	-g
t	folders
=	projects	-p
t	folders
=	projects	--project-cache-dir
t	folders
=	projects	-Dorg.gradle.java.home
t	folders
@	tasks
o	--all	By default, this report shows only those tasks which have been assigned to a task group. You can…	
o	--group	If you need to be more precise, you can display only the tasks from a specific group	v
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	tasks	--priority
v	normal	
v	low	
=	tasks	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	tasks	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	tasks	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	tasks	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	tasks	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	tasks	-b
t	filepaths
=	tasks	-c
t	filepaths
=	tasks	-g
t	folders
=	tasks	-p
t	folders
=	tasks	--project-cache-dir
t	folders
=	tasks	-Dorg.gradle.java.home
t	folders
@	help
o	--task		v
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	help	--priority
v	normal	
v	low	
=	help	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	help	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	help	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	help	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	help	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	help	-b
t	filepaths
=	help	-c
t	filepaths
=	help	-g
t	folders
=	help	-p
t	folders
=	help	--project-cache-dir
t	folders
=	help	-Dorg.gradle.java.home
t	folders
@	dependencies
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	dependencies	--priority
v	normal	
v	low	
=	dependencies	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	dependencies	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	dependencies	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	dependencies	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	dependencies	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	dependencies	-b
t	filepaths
=	dependencies	-c
t	filepaths
=	dependencies	-g
t	folders
=	dependencies	-p
t	folders
=	dependencies	--project-cache-dir
t	folders
=	dependencies	-Dorg.gradle.java.home
t	folders
@	buildEnvironment
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	buildEnvironment	--priority
v	normal	
v	low	
=	buildEnvironment	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	buildEnvironment	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	buildEnvironment	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	buildEnvironment	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	buildEnvironment	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	buildEnvironment	-b
t	filepaths
=	buildEnvironment	-c
t	filepaths
=	buildEnvironment	-g
t	folders
=	buildEnvironment	-p
t	folders
=	buildEnvironment	--project-cache-dir
t	folders
=	buildEnvironment	-Dorg.gradle.java.home
t	folders
@	dependencyInsight
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	dependencyInsight	--priority
v	normal	
v	low	
=	dependencyInsight	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	dependencyInsight	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	dependencyInsight	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	dependencyInsight	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	dependencyInsight	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	dependencyInsight	-b
t	filepaths
=	dependencyInsight	-c
t	filepaths
=	dependencyInsight	-g
t	folders
=	dependencyInsight	-p
t	folders
=	dependencyInsight	--project-cache-dir
t	folders
=	dependencyInsight	-Dorg.gradle.java.home
t	folders
@	properties
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	properties	--priority
v	normal	
v	low	
=	properties	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	properties	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	properties	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	properties	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	properties	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	properties	-b
t	filepaths
=	properties	-c
t	filepaths
=	properties	-g
t	folders
=	properties	-p
t	folders
=	properties	--project-cache-dir
t	folders
=	properties	-Dorg.gradle.java.home
t	folders
@	--status
@	--stop
@	init
o	--type	Specify project type	v
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	init	--type
v	basic	
v	java-library	
v	java-application	
=	init	--priority
v	normal	
v	low	
=	init	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	init	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	init	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	init	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	init	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	init	-b
t	filepaths
=	init	-c
t	filepaths
=	init	-g
t	folders
=	init	-p
t	folders
=	init	--project-cache-dir
t	folders
=	init	-Dorg.gradle.java.home
t	folders
@	wrapper
o	--gradle-version	The Gradle version used for downloading and executing the Wrapper	v
o	--distribution-type	The Gradle distribution type used for the Wrapper	v
o	--gradle-distribution-url	The full URL pointing to Gradle distribution ZIP file	v
o	--gradle-distribution-sha256-sum	The SHA256 hash sum used for verifying the downloaded Gradle distribution	v
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	wrapper	--distribution-type
v	bin	
v	all	
=	wrapper	--priority
v	normal	
v	low	
=	wrapper	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	wrapper	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	wrapper	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	wrapper	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	wrapper	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	wrapper	-b
t	filepaths
=	wrapper	-c
t	filepaths
=	wrapper	-g
t	folders
=	wrapper	-p
t	folders
=	wrapper	--project-cache-dir
t	folders
=	wrapper	-Dorg.gradle.java.home
t	folders
@	test
o	--continuous	Allows you to automatically re-execute the requested tasks when task inputs change	
o	--rerun-tasks	This will force test and all task dependencies of test to execute	
o	--continue	Gradle will execute every task to be executed where all of the dependencies for that task…	
o	-?|-h|--help	Shows a help message with all available CLI options	
o	-v|--version	Prints Gradle, Groovy, Ant, JVM, and operating system version information	
o	-S|--full-stacktrace	Print out the full (very verbose) stacktrace for any exceptions	
o	-s|--stacktrace	Print out the stacktrace also for user exceptions (e.g. compile error)	
o	--scan	Create a build scan with fine-grained information about all aspects of your Gradle build	
o	-Dorg.gradle.debug	Debug Gradle client (non-Daemon) process. Gradle will wait for you to attach a debugger at…	
o	-Dorg.gradle.daemon.debug	Debug Gradle Daemon process	
o	--build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--no-build-cache	Toggles the Gradle build cache. Gradle will try to reuse outputs from previous builds. Default is…	
o	--configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--no-configure-on-demand	Toggles Configure-on-demand. Only relevant projects are configured in this build run. Default is off	
o	--max-workers	Sets maximum number of workers that Gradle may use. Default is number of processors	v
o	--parallel	Build projects in parallel. For limitations of this option, see Parallel Project Execution…	
o	--no-parallel	Disables --parallel	
o	--priority	Specifies the scheduling priority for the Gradle daemon and all processes launched by it	v
o	--profile	Generates a high-level performance report in the $buildDir/reports/profile directory. --scan is…	
o	--scan	Generate a build scan with detailed performance diagnostics	
o	--watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--no-watch-fs	Toggles watching the file system. When enabled Gradle re-uses information it collects about the…	
o	--daemon	Use the Gradle Daemon to run the build. Starts the daemon if not running or existing daemon busy…	
o	--no-daemon	Disables --daemon	
o	--foreground	Starts the Gradle Daemon in a foreground process	
o	-Dorg.gradle.daemon.idletimeout	Gradle Daemon will stop itself after this number of milliseconds of idle time	v
o	-Dorg.gradle.logging.level	Set logging level via Gradle properties	v
o	-q|--quiet	Log errors only	
o	-w|--warn	Set log level to warn	
o	-i|--info	Set log level to info	
o	-d|--debug	Log in debug mode (includes normal stacktrace)	
o	-Dorg.gradle.console	Specify console mode via Gradle properties	v
o	--console	Specifies which type of console output to generate	v
o	-Dorg.gradle.warning.mode	Specify warning mode via Gradle properties	v
o	--warning-mode	Specifies how to log warning	v
o	--include-build	Run the build as a composite, including the specified build	
o	--offline	Specifies that the build should operate without accessing network resources	
o	--refresh-dependencies	Refresh the state of dependencies	
o	--dry-run	Run Gradle with all task actions disabled. Use this to show which task would have executed	
o	--write-locks	Indicates that all resolved configurations that are lockable should have their lock state persisted	
o	--update-locks	Indicates that versions for the specified modules have to be updated in the lock file	v
o	--no-rebuild	Do not rebuild project dependencies. Useful for debugging and fine-tuning buildSrc, but can lead…	
o	-b|--build-file	Specifies the build file. For example: gradle --build-file=foo.gradle	v
o	-c|--settings-file	Specifies the settings file. For example: gradle --settings-file=somewhere/else/settings.gradle	v
o	-g|--gradle-user-home	Specifies the Gradle user home directory. The default is the .gradle directory in the user’s home…	v
o	-p|--project-dir	Specifies the start directory for Gradle	v
o	--project-cache-dir	Specifies the project-specific cache directory. Default value is .gradle in the root project…	v
o	-D|--system-prop	Sets a system property of the JVM, for example -Dmyprop=myvalue	v
o	-I|--init-script	Specifies an initialization script	
o	-P|--project-prop	Sets a project property of the root project, for example -Pmyprop=myvalue	v
o	-Dorg.gradle.jvmargs	Set JVM arguments	v
o	-Dorg.gradle.java.home	Set JDK home dir	v
=	test	--priority
v	normal	
v	low	
=	test	-Dorg.gradle.logging.level
v	quiet	
v	warn	
v	lifecycle	
v	info	
v	debug	
=	test	-Dorg.gradle.console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	test	--console
v	auto	Enables color and other rich output in the console output when the build process is attached to a…
v	plain	Disables all color and other rich output in the console output. This is the default when Gradle is…
v	rich	Enables color and other rich output in the console output, regardless of whether the build process…
v	verbose	Enables color and other rich output like the rich, but output task names and outcomes at the…
=	test	-Dorg.gradle.warning.mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	test	--warning-mode
v	all	Log all warnings
v	fail	Log all warnings and fail the build if there are any warnings
v	summary	Suppress all warnings and log a summary at the end of the build
v	none	Suppress all warnings, including the summary at the end of the build
=	test	-b
t	filepaths
=	test	-c
t	filepaths
=	test	-g
t	folders
=	test	-p
t	folders
=	test	--project-cache-dir
t	folders
=	test	-Dorg.gradle.java.home
t	folders
