@	
o	--bail|-b	Exit the test suite immediately upon n number of failing test suite. Defaults to 1	v
o	--cache	Whether to use the cache	
o	--no-cache	Whether to use the cache	
o	--changedFilesWithAncestor	Runs tests related to the current changes and the changes made in the last commit	
o	--changedSince	Runs tests related to the changes since the provided branch or commit hash	v
o	--ci	Instead of the regular behavior of storing a new snapshot automatically, will fail the test and…	
o	--clearCache	Deletes the Jest cache directory and then exits without running tests	v
o	--collectCoverageFrom	A glob pattern relative to rootDir matching the files that coverage info needs to be collected from	v=
o	--colors	Forces test results output highlighting even if stdout is not a TTY	
o	--config|-c	The path to a Jest config file specifying how to find and execute tests	v=
o	--coverage	Enable or disable coverage, disabled by default	v=
o	--coverageProvider	Indicates which provider should be used to instrument code for coverage	v=
o	--debug	Print debugging info about your Jest config	
o	--detectOpenHandles	Attempt to collect and print open handles preventing Jest from exiting cleanly	
o	--env	The test environment used for all tests	v=
o	--errorOnDeprecated	Make calling deprecated APIs throw helpful error messages	
o	--expand|-e	Use this flag to show full diffs and errors instead of a patch	
o	--findRelatedTests	Find and run the tests that cover a space separated list of source files that were passed in as…	v
o	--forceExit	Force Jest to exit after all tests have completed running	
o	--help	Show the help information	
o	--init	Generate a basic configuration file	
o	--injectGlobals	Insert Jest's globals (expect, test, describe, beforeEach etc.) into the global environment	
o	--json	Prints the test results in JSON	
o	--outputFile	Write test results to a file when the --json option is also specified	v=
o	--lastCommit	Run all tests affected by file changes in the last commit made	
o	--listTests	Lists all tests as JSON that Jest will run given the arguments, and exits	
o	--logHeapUsage	Logs the heap usage after every test	
o	--maxConcurrency	Prevents Jest from executing more than the specified amount of tests at the same time	v=
o	--maxWorkers|-w	Specifies the maximum number of workers the worker-pool will spawn for running tests	v=
o	--noStackTrace	Disables stack trace in test results output	
o	--notify	Activates notifications for test results	
o	--onlyChanged|-o	Attempts to identify which tests to run based on which files have changed in the current repository	
o	--passWithNoTests	Allows the test suite to pass when no files are found	
o	--projects	Run tests from one or more projects, found in the specified paths; also takes path globs	v
o	--reporters	Run tests with specified reporters	v=
o	--roots	A list of paths to directories that Jest should use to search for files in	v
o	--runInBand|-i	Run all tests serially in the current process, rather than creating a worker pool of child…	
o	--selectProjects	Run only the tests of the specified projects	v
o	--runTestsByPath	Run only the tests that were specified with their exact paths	
o	--setupTestFrameworkScriptFile	The path to a module that runs some code to configure or set up the testing framework before each…	v=
o	--showConfig	Print your Jest config and then exits	
o	--silent	Prevent tests from printing messages through the console	
o	--testNamePattern|-t	Run only tests with a name that matches the regex	v=
o	--testLocationInResults	Adds a location field to test results	
o	--testPathPattern	A regexp pattern string that is matched against all tests paths before executing the test	v=
o	--testPathIgnorePatterns	An array of regexp pattern strings that are tested against all tests paths before executing the test	v=
o	--testRunner	Lets you specify a custom test runner	v=
o	--testSequencer	Lets you specify a custom test sequencer	v=
o	--testTimeout	Default timeout of a test in milliseconds	v=
o	--updateSnapshot|-u	Use this flag to re-record every snapshot that fails during this test run	
o	--useStderr	Divert all output to stderr	
o	--verbose	Display individual test results with the test suite hierarchy	
o	--version|-v	Print the version and exit	
o	--watch	Watch files for changes and rerun tests related to changed files	
o	--watchAll	Watch files for changes and rerun all tests when something changes	
o	--watchman	Whether to use watchman for file crawling	
o	--no-watchman	Whether to use watchman for file crawling	
a	1	0
=		--config
t	filepaths
=		--coverage
v	true	
v	false	
=		--coverageProvider
v	babel	
v	v8	
=		--env
v	jsdom	
v	node	
t	filepaths
=		--projects
t	filepaths
=		--roots
t	folders
=		--setupTestFrameworkScriptFile
t	filepaths
=		--testRunner
t	filepaths
=		--testSequencer
t	filepaths
