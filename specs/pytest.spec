@	
o	--assert	Control assertion debugging tools. 'plain' performs no assertion debugging. 'rewrite' (the…	v
o	--basetemp	Base temporary directory for this test run.(warning: this directory is removed if it exists)	v
o	-c	Load configuration from `file` instead of trying to locate one of the implicit configuration files	v
o	--cache-clear	Remove all cache contents at start of test run	
o	--cache-show	Show cache contents, don't perform collection or tests. Optional argument: glob (default: '*')	V
o	--capture	Per-test capturing method	v
o	--code-highlight	Whether code should be highlighted (only if --color is also enabled)	v
o	--co|--collect-only	Only collect tests, don't execute them	
o	--collect-in-virtualenv	Don't ignore tests in a local virtualenv directory	
o	--color	Color terminal output	v
o	--confcutdir	Only load conftest.py's relative to specified dir	v
o	--continue-on-collection-errors	Force test execution even if collection errors occur	
o	--debug	Store internal tracing debug information in this log file. This file is opened with 'w' and…	V
o	--durations	Show N slowest setup/test durations (N=0 for all)	v
o	--durations-min	Minimal duration in seconds for inclusion in slowest list	v
o	--deselect	Deselect item (via node id prefix) during collection (multi-allowed)	v
o	--disable-warnings|--disable-pytest-warnings	Disable warnings summary	
o	--doctest-continue-on-failure	For a given doctest, continue to run after the first failure	
o	--doctest-ignore-import-errors	Ignore doctest ImportErrors	
o	--doctest-modules	Run doctests in all .py modules	
o	--doctest-report	Choose another output format for diffs on doctest failure	v
o	--doctest-glob	Doctests file matching pattern, default: test*.txt	v
o	--exitfirst|-x	Exit instantly on first error or failed test	
o	--failed-first|--ff	Run all tests, but run the last failures first	
o	--fixtures	Shows builtin and custom fixtures. Note that this command omits fixtures with leading _ unless the…	
o	--fixtures-per-test	Show fixtures per test	
o	--full-trace	Don't cut any tracebacks (default is to cut)	
o	--help|-h	This shows help on command line and config-line options	
o	--ignore	Ignore path during collection (multi-allowed)	v
o	--ignore-glob	Ignore path pattern during collection (multi-allowed)	v
o	--import-mode	Prepend/append to sys.path when importing test modules and conftest files, default is to prepend	v
o	--junit-xml	Create junit-xml style report file at given path	v
o	--junit-prefix	Prepend prefix to classnames in junit-xml output	v
o	-k	Only run tests which match the given substring expression. An expression is a python evaluatable…	v
o	--keep-duplicates	Keep duplicate tests	
o	--showlocals|-l	Show locals in tracebacks (disabled by default)	
o	--last-failed-no-failures|--lfnf	Which tests to run with no previously (known) failures	v
o	--last-failed|--lf	Rerun only the tests that failed at the last run (or all if none failed)	
o	--log-auto-indent	Auto-indent multiline messages passed to the logging module. Accepts true|on, false|off or an…	v
o	--log-cli-level	Cli logging level	v
o	--log-cli-format	Log format as used by the logging module	v
o	--log-cli-date-format	Log date format as used by the logging module	v
o	--log-date-format	Log date format as used by the logging module	v
o	--log-format	Log format as used by the logging module	v
o	--log-file	Path to a file where logging will be written to	v
o	--log-file-level	Log file logging level	v
o	--log-file-date-format	Log date format as used by the logging module	v
o	--log-file-format	Log format as used by the logging module	v
o	--log-level	Level of messages to catch/display. Not set by default, so it depends on the root/parent log…	v
o	-m	Only run tests matching given mark expression	v
o	--markers	Show markers (builtin, plugin and per-project ones)	
o	--maxfail	Exit after first num failures or errors	v
o	--new-first|--nf	Run tests from new files first, then the rest of the tests sorted by file mtime	
o	--noconftest	Don't load any conftest.py files	
o	--no-header	Disable header	
o	--no-summary	Disable summary	
o	--override-ini|-o	Override ini option with `option=value` style`	v
o	-p	Early-load given plugin module name or entry point (multi-allowed)	v
o	--pastebin	Send failed|all info to bpaste.net pastebin service	v
o	--pdb	Start the interactive Python debugger on errors or KeyboardInterrupt	
o	--pdbcls	Specify a custom interactive Python debugger for use with --pdb	v
o	--pyargs	Try to interpret all arguments as python packages	
o	--quiet|-q	Decrease verbosity	
o	-r	Show extra test summary info as specified by chars: (f)ailed, (E)rror, (s)kipped, (x)failed…	v
o	--rootdir	Define root directory for tests. Can be relative path: 'root_dir', './root_dir'…	v
o	--runxfail	Report the results of xfail tests as if they were not marked	
o	-s	Shortcut for --capture=no	
o	--setup-only	Only setup fixtures, do not execute tests	
o	--setup-show	Show setup of fixtures while executing tests	
o	--setup-plan	Show what fixtures and tests would be executed but don't execute anything	
o	--show-capture	Controls how captured stdout/stderr/log is shown on failed tests	v
o	--stepwise|--sw	Exit on test failure and continue from last failing test next time	
o	--stepwise-skip|--sw-skip	Ignore the first failing test but stop on the next failing test	
o	--strict	Alias to --strict-markers	
o	--strict-config	Any warnings encountered while parsing the `pytest` section of the configuration file raise errors	
o	--strict-markers	Markers not registered in the `markers` section of the configuration file raise errors	
o	--tb	Traceback print mode	v
o	--trace	Immediately break when running each test	
o	--trace-config	Trace considerations of conftest.py files	
o	--verbose|-v	Increase verbosity	
o	--verbosity	Set verbosity. Default is 0	v
o	--version|-V	Display pytest version and information about plugins. When given twice, also display information…	
o	--pythonwarnings|-W	Set which warnings to report, see -W option of python itself	v
a	1	0
=		--assert
v	plain	
v	rewrite	
=		--basetemp
t	folders
=		-c
t	filepaths
=		--capture
v	fd	
v	sys	
v	no	
v	tee-sys	
=		--code-highlight
v	yes	
v	no	
=		--color
v	yes	
v	no	
v	auto	
=		--confcutdir
t	folders
=		--doctest-report
v	none	
v	cdiff	
v	ndiff	
v	udiff	
v	only_first_failure	
=		--ignore
t	filepaths
=		--ignore-glob
t	filepaths
=		--import-mode
v	prepend	
v	append	
v	importlib	
=		--junit-xml
t	filepaths,folders
=		--last-failed-no-failures
v	all	
v	none	
=		--log-auto-indent
v	true	
v	false	
=		--log-cli-level
v	CRITICAL	
v	ERROR	
v	WARNING	
v	INFO	
v	DEBUG	
=		--log-file
t	filepaths
=		--log-file-level
v	CRITICAL	
v	ERROR	
v	WARNING	
v	INFO	
v	DEBUG	
=		--log-level
v	CRITICAL	
v	ERROR	
v	WARNING	
v	INFO	
v	DEBUG	
=		--pastebin
v	failed	
v	all	
=		-r
v	a	
v	A	
v	E	
v	f	
v	N	
v	p	
v	P	
v	s	
v	w	
v	x	
v	X	
=		--rootdir
t	folders
=		--show-capture
v	no	
v	stdout	
v	stderr	
v	log	
v	all	
=		--tb
v	auto	
v	long	
v	short	
v	line	
v	native	
v	no	
#		1
t	filepaths,folders
