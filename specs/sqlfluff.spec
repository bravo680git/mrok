@	
s	lint	Lint SQL files via passing a list of files or using stdin
s	fix	Fix SQL files
s	parse	Parse SQL files and just spit out the result
s	dialects	Show the current dialects available
s	version	Show the version of sqlfluff
s	rules	Show the current rules in use
o	--version	Show the version and exit	p
o	--help|-h	Show help for sqlfluff	p
@	lint
o	--nocolor|-n	No color - output will be without ANSI color codes	
o	--ignore|-i	Ignore particular families of errors so that they don’t cause a failed run. -–ignore behaves…	v
o	--verbose|-v	Verbosity, how detailed should the output be. This is stackable, so -vv is more verbose than -v…	
o	--exclude-rules|-e	Exclude specific rules. This could either be the allowlist, or the general set if there is no…	v
o	--rules|-r	Narrow the search to only specific rules	v
o	--templater|-t	The templater to use (default=jinja)	v
o	--dialect|-d	The dialect of SQL to lint	v
o	--format|-f	What format to return the lint result in (default=human)	v
o	--processes|-p	The number of parallel processes to run. Positive numbers work as expected. Zero and negative…	v
o	--disable-noqa	Set this flag to ignore inline noqa comments	
o	--bench	Set this flag to engage the benchmarking tool output	
o	--logger	Choose to limit the logging to one of the loggers	v
o	--encoding	Specify encoding to use when reading and writing files. Defaults to autodetect	v
o	--ignore-local-config	Ignore config files in default search path locations. This option allows the user to lint with the…	
o	--config	Include additional config file. By default the config is generated from the standard configuration…	v
o	--write-output	Optionally provide a filename to write the results to, mostly used in tandem with –format. NB…	v
o	--annotation-level	When format is set to github-annotation or github-annotation-native, default annotation level…	v
o	--disregard-sqlfluffignores	Perform the operation regardless of .sqlfluffignore configurations	
o	--disable-progress-bar	Disables progress bars	
o	--nofail	If set, the exit code will always be zero, regardless of violations found. This is potentially…	
o	--help|-h	Show help for sqlfluff	
a	1	1
=	lint	--templater
v	raw	
v	jinja	
v	python	
v	placeholders	
=	lint	--dialect
v	ansi	
v	bigquery	
v	exasol	
v	hive	
v	mysql	
v	oracle	
v	postgres	
v	redshift	
v	snowflake	
v	spark3	
v	sqllite	
v	teradata	
v	tsql	
=	lint	--format
v	human	
v	json	
v	yaml	
v	github-annotation	
v	github-annotation-native	
=	lint	--logger
v	templater	
v	lexer	
v	parser	
v	linter	
v	rules	
=	lint	--config
t	filepaths
=	lint	--write-output
t	filepaths
=	lint	--annotation-level
v	notice	
v	warning	
v	failure	
v	error	
#	lint	1
t	filepaths
@	fix
o	--nocolor|-n	No color - output will be without ANSI color codes	
o	--ignore|-i	Ignore particular families of errors so that they don’t cause a failed run. -–ignore behaves…	v
o	--verbose|-v	Verbosity, how detailed should the output be. This is stackable, so -vv is more verbose than -v…	
o	--exclude-rules|-e	Exclude specific rules. This could either be the allowlist, or the general set if there is no…	v
o	--rules|-r	Narrow the search to only specific rules	v
o	--templater|-t	The templater to use (default=jinja)	v
o	--dialect|-d	The dialect of SQL to lint	v
o	--format|-f	What format to return the lint result in (default=human)	v
o	--processes|-p	The number of parallel processes to run. Positive numbers work as expected. Zero and negative…	v
o	--fixed-suffix|-x	An optional suffix to add to fixed files	v
o	--disable-noqa	Set this flag to ignore inline noqa comments	
o	--bench	Set this flag to engage the benchmarking tool output	
o	--logger	Choose to limit the logging to one of the loggers	v
o	--encoding	Specify encoding to use when reading and writing files. Defaults to autodetect	v
o	--ignore-local-config	Ignore config files in default search path locations. This option allows the user to lint with the…	
o	--config	Include additional config file. By default the config is generated from the standard configuration…	v
o	--write-output	Optionally provide a filename to write the results to, mostly used in tandem with –format. NB…	v
o	--disable-progress-bar	Disables progress bars	
o	--FIX-EVEN-UNPARSABLE	Enables fixing of files that have templating or parse errors	
o	--show-lint-violations	Show lint violations	
a	1	1
=	fix	--templater
v	raw	
v	jinja	
v	python	
v	placeholders	
=	fix	--dialect
v	ansi	
v	bigquery	
v	exasol	
v	hive	
v	mysql	
v	oracle	
v	postgres	
v	redshift	
v	snowflake	
v	spark3	
v	sqllite	
v	teradata	
v	tsql	
=	fix	--format
v	human	
v	json	
v	yaml	
v	github-annotation	
v	github-annotation-native	
=	fix	--logger
v	templater	
v	lexer	
v	parser	
v	linter	
v	rules	
=	fix	--config
t	filepaths
=	fix	--write-output
t	filepaths
#	fix	1
t	filepaths
@	parse
o	--nocolor|-n	No color - output will be without ANSI color codes	
o	--ignore|-i	Ignore particular families of errors so that they don’t cause a failed run. -–ignore behaves…	v
o	--verbose|-v	Verbosity, how detailed should the output be. This is stackable, so -vv is more verbose than -v…	
o	--exclude-rules|-e	Exclude specific rules. This could either be the allowlist, or the general set if there is no…	v
o	--rules|-r	Narrow the search to only specific rules	v
o	--templater|-t	The templater to use (default=jinja)	v
o	--dialect|-d	The dialect of SQL to lint	v
o	--code-only|-c	Output only the code elements of the parse tree	
o	--include-meta|-m	Include meta segments (indents, dedents and placeholders) in the output. This only applies when…	
o	--format|-f	What format to return the lint result in (default=human)	v
o	--disable-noqa	Set this flag to ignore inline noqa comments	
o	--bench	Set this flag to engage the benchmarking tool output	
o	--recurse	The depth to recursively parse to (0 for unlimited)	v
o	--logger	Choose to limit the logging to one of the loggers	v
o	--encoding	Specify encoding to use when reading and writing files. Defaults to autodetect	v
o	--ignore-local-config	Ignore config files in default search path locations. This option allows the user to lint with the…	
o	--config	Include additional config file. By default the config is generated from the standard configuration…	v
o	--write-output	Optionally provide a filename to write the results to, mostly used in tandem with –format. NB…	v
o	--profiler	Set this flag to engage the python profiler	
o	--nofail	If set, the exit code will always be zero, regardless of violations found. This is potentially…	
a	1	0
=	parse	--templater
v	raw	
v	jinja	
v	python	
v	placeholders	
=	parse	--dialect
v	ansi	
v	bigquery	
v	exasol	
v	hive	
v	mysql	
v	oracle	
v	postgres	
v	redshift	
v	snowflake	
v	spark3	
v	sqllite	
v	teradata	
v	tsql	
=	parse	--format
v	human	
v	json	
v	yaml	
v	github-annotation	
v	github-annotation-native	
=	parse	--logger
v	templater	
v	lexer	
v	parser	
v	linter	
v	rules	
=	parse	--config
t	filepaths
=	parse	--write-output
t	filepaths
#	parse	1
t	filepaths
@	dialects
o	--nocolor|-n	No color - output will be without ANSI color codes	
o	--verbose|-v	Verbosity, how detailed should the output be. This is stackable, so -vv is more verbose than -v…	
@	version
o	--nocolor|-n	No color - output will be without ANSI color codes	
o	--verbose|-v	Verbosity, how detailed should the output be. This is stackable, so -vv is more verbose than -v…	
@	rules
o	--nocolor|-n	No color - output will be without ANSI color codes	
o	--verbose|-v	Verbosity, how detailed should the output be. This is stackable, so -vv is more verbose than -v…	
