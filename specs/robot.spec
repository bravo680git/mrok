@	
o	-h|-?|--help	Print usage instructions	
o	--rpa	Turn on the generic automation mode. Mainly affects terminology so that "test" is replaced with…	
o	-F|--extension	Parse only files with this extension when executing a directory	v
o	-N|--name	Set a name of the top level suite	v
o	-D|--doc	Set a documentation of the top level suite	
o	-M|--metadata	Set metadata of the top level suite	v
o	-G|--settag	Sets given tag to all executed tests	v
o	-t|--test	Select tests by name or by long name containing also parent suite name like `Parent.Test`	v
o	--task	Alias to --test. Especially applicable with --rpa	v
o	-s|--suite	Select suites by name	v
o	-i|--include	Select test cases by tag	v
o	-e|--exclude	Select test cases not to run by tag	v
o	-R|--rerunfailed	Select failed tests from an earlier output file to be re-executed	v
o	-S|--rerunfailedsuites	Select failed suites from an earlier output file to be re-executed	v
o	--runemptysuite	Executes suite even if it contains no tests	
o	--skip	Tests having given tag will be skipped	v
o	--skiponfailure	Tests having given tag will be skipped if they fail	v
o	-v|--variable	Set variables in the test data	v
o	-V|--variablefile	Python or YAML file file to read variables from	v
o	-d|--outputdir	Where to create output files. The default is the directory where tests are run from	v
o	-o|--output	XML output file relative to --outputdir unless given as an absolute path. Default: output.xml	v
o	-l|--log	HTML log file. Can be disabled by giving a special value `NONE`. Default: log.html	v
o	-r|--report	HTML report file. Can be disabled with `NONE` similarly as --log. Default: report.html	v
o	-x|--xunit	XUnit compatible result file. Not created unless this option is specified	v
o	-b|--debugfile	Debug file written during execution. Not created unless this option is specified	v
o	-T|--timestampoutputs	Adds timestamp in a format `YYYYMMDD-hhmmss` to all generated output files between their basename…	
o	--splitlog	Split the log file into smaller pieces that open in browsers transparently	
o	--logtitle	Title for the generated log file. The default title is `<SuiteName> Log.`	v
o	--reporttitle	Title for the generated report file. The default title is `<SuiteName> Report`	v
o	--reportbackground	Background colors to use in the report file. Given in format `passed:failed:skipped` where the…	v
o	--maxerrorlines	Maximum number of error message lines to show in report when tests fail. Default is 40, minimum is…	v
o	--maxassignlength	Maximum number of characters to show in log when variables are assigned. Zero or negative values…	v
o	-L|--loglevel	Threshold level for logging	v
o	--suitestatlevel	How many levels to show in `Statistics by Suite` in log and report	v
o	--tagstatinclude	Include only matching tags in `Statistics by Tag` in log and report	v
o	--tagstatexclude	Exclude matching tags from `Statistics by Tag`	v
o	--tagstatcombine	Create combined statistics based on tags. These statistics are added into `Statistics by Tag`	v
o	--tagdoc	Add documentation to tags matching the given pattern	v
o	--tagstatlink	Add external links into `Statistics by Tag`. Pattern can use `*`, `?` and `[]` as wildcards	v
o	--expandkeywords	Matching keywords will be automatically expanded in the log file	v
o	--removekeywords	Remove keyword data from the generated log file	v
o	--flattenkeywords	Flattens matching keywords in the generated log file	v
o	--listener	A class for monitoring test execution. Gets notifications e.g. when tests start and end	v
o	--nostatusrc	Sets the return code to zero regardless of failures in test cases. Error codes are returned normally	
o	--dryrun	Sets the return code to zero regardless of failures in test cases. Error codes are returned normally	
o	-X|--exitonfailure	Stops test execution if any test fails	
o	--exitonerror	Stops test execution if any error occurs when parsing test data, importing libraries, and so on	
o	--skipteardownonexit	Causes teardowns to be skipped if test execution is stopped prematurely	
o	--randomize	Randomizes the test execution order	v
o	--prerunmodifier	Class to programmatically modify the suite structure before execution	v
o	--prerebotmodifier	Class to programmatically modify the result model before creating reports and logs	v
o	--console	How to report execution on the console	v
o	-.|--dotted	Shortcut for `--console dotted`	
o	--quiet	Shortcut for `--console quiet`	
o	-W|--consolewidth	Width of the console output. Default is 78	v
o	-C|--consolecolors	Use colors on console output or not	v
o	-K|--consolemarkers	Show markers on the console when top level keywords in a test case end	v
o	-P|--pythonpath	Additional locations (directories, ZIPs) where to search libraries and other extensions when they…	v
o	-A|--argumentfile	Text file to read more arguments from. Use special path `STDIN` to read contents from the standard…	v
o	--version	Print version information	
a	1	1
=		-F
v	txt	
v	robot:txt	
=		-t
d
=		--task
d
=		-i
d
=		-e
d
=		-R
d
=		-S
d
=		--skip
d
=		--skiponfailure
d
=		-v
d
=		-V
d
=		-d
t	folders
=		-o
v	output.xml	
=		-l
v	log.html	
v	NONE	
=		-r
v	report.html	
v	NONE	
=		-x
v	xunit.xml	
=		--maxerrorlines
v	40	Default number of lines
v	10	Minimum number of lines
v	NONE	Unlimited number of lines. Shows the full message
=		--maxassignlength
v	200	Default number of characters
v	0	No values at all
=		-L
v	TRACE	
v	DEBUG	
v	INFO	
v	WARN	
v	NONE	
=		--tagstatinclude
d
=		--tagstatexclude
d
=		--tagstatcombine
d
=		--tagdoc
d
=		--tagstatlink
d
=		--expandkeywords
v	name:<pattern>	
v	tag:<pattern>	
=		--removekeywords
v	all	Remove data from all keywords
v	passed	Remove data only from keywords in passed test cases and suites
v	for	Remove passed iterations from for loops
v	while	Remove passed iterations from while loops
v	wuks	Remove all but the last failing keyword inside `BuiltIn.Wait Until Keyword Succeeds`
v	name:<pattern>	
v	tag:<pattern>	
=		--flattenkeywords
v	for	Flatten FOR loops fully
v	while	Flatten WHILE loops fully
v	iteration	Flatten FOR/WHILE loop iterations
v	name:<pattern>	
v	tag:<pattern>	
=		--randomize
v	all	Randomizes both suites and tests
v	suites	Randomizes suites
v	tests	Randomizes tests
v	none	No randomization (default)
=		--console
v	verbose	Report every suite and test (default)
v	dotted	Only show `.` for passed test, `s` for skipped tests, and `F` for failed tests
v	quiet	No output except for errors and warnings
v	none	No output whatsoever
=		-W
v	78	
=		-C
v	auto	Use colors when output not redirected (default)
v	on	Always use colors
v	ansi	Like `on` but use ANSI colors also on Windows
v	off	Disable colors altogether
=		-K
v	auto	
v	on	
v	off	
=		-P
d
=		-A
t	filepaths
#		1
d
