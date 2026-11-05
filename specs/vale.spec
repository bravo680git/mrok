@	
s	ls-config	Print the current configuration to stdout
s	ls-metrics	Print the given file's internal metrics to stdout
o	--help|-h	Show help for vale	
o	--version|-v	Print the current version	
o	--ignore-syntax	Lint all files line-by-line	
o	--no-exit	Don't return a nonzero exit code on errors	
o	--no-wrap	Don't wrap CLI output	
o	--ext	An extension to associate with stdin	v=
o	--glob	A glob pattern	v=
o	--minAlertLevel	The minimum level to display	v=
o	--output	The alert output style to use	v=
o	--config	A path to a .vale.ini file	v=
a	1	1
=		--ext
v	.md	
v	.rst	
v	.adoc	
v	.html	
=		--minAlertLevel
v	suggestion	
v	warning	
v	error	
=		--output
v	line	
v	JSON	
#		1
t	filepaths,folders
@	ls-config
@	ls-metrics
a	1	0
