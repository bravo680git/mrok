@	
o	--warmup|-w	Perform warmupruns (number) before the actual benchmarking starts	v
o	--min-runs|-m	Perform at least NUM runs for each command	v
o	--max-runs|-M	Perform at most NUM runs for each command. Default: no limit	v
o	--runs|-r	Perform exactly NUM runs for each command	v
o	--setup|-s	Execute cmd once before each set of timing runs	v
o	--prepare|-p	Execute cmd before each timing run. This is useful for clearing disk caches, for example	v
o	--cleanup|-c	Execute cmd after the completion of all benchmarking runs for each individual command to be…	v
o	--parameter-scan|-P	Perform benchmark runs for each value in the range min..max	v
o	--parameter-step-size|-D	This argument requires --parameter-scan to be specified as well. Traverse the range min..max in…	v
o	--parameter-list|-L	Perform benchmark runs for each value in the comma-separated list of values	v
o	--style	Set output style type	v
o	--shell|-S	Set the shell to use for executing benchmarked commands	v
o	--ignore-failure|-i	Ignore non-zero exit codes of the benchmarked commands	
o	--time-unit|-u	Set the time unit to use for the benchmark results	v
o	--export-asciidoc	Export the timing summary statistics as an AsciiDoc table to the given file	v
o	--export-csv	Export the timing summary statistics as CSV to the given file	v
o	--export-json	Export the timing summary statistics and timings of individual runs as JSON to the given file	v
o	--export-markdown	Export the timing summary statistics as a Markdown table to the given file	v
o	--show-output	Print the stdout and stderr of the benchmark instead of suppressing it	
o	--command-name	Identify a command with the given name	v
o	--help	Prints help message	
o	--version	Shows version information	
a	1	0
=		--style
v	basic	Disable output coloring and interactive elements
v	full	Enable all effects even if no interactive terminal was detected
v	nocolor	Keep the interactive output without any colors
v	color	Keep the colors without any interactive output
v	none	Disable all the output of the tool
=		--shell
v	bash	Use bash as the shell
v	zsh	Use zsh as the shell
v	sh	Use sh as the shell
v	fish	Use fish as the shell
v	pwsh	Use pwsh as the shell
v	powershell	Use powershell as the shell
=		--time-unit
v	millisecond	
v	second	
=		--export-asciidoc
t	filepaths
=		--export-csv
t	filepaths
=		--export-json
t	filepaths
=		--export-markdown
t	filepaths
