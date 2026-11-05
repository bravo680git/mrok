@	
s	archive	Create an archive
s	cloud	Run a test on the cloud
s	completion	Generate the autocompletion script for the specified shell
s	convert	Convert a HAR file to a k6 script
s	help	Help about any command
s	inspect	Inspect a script or archive
s	login	Inspect a script or archive
s	pause	Pause a running test
s	resume	Resume a running test
s	run	Start a load test
s	scale	Scale a running test
s	stats	Show test metrics
s	status	Show test status
s	version	Show the application version and exit
o	-v|--verbose	Enable verbose logging	
o	-q|--quiet	Disable progress updates	
o	-h|--help	Help for k6	
o	-a|--address	Address for the REST API server (default "localhost:6565")	v
o	--config|-c	JSON config file	v
o	--log-format	Log output format	v
o	--log-output	Change the output for k6 logs	v
o	--no-color	Disable colored output	v
@	archive
a	1	0
@	cloud
a	1	0
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
a	1	0
@	completion bash
@	completion fish
@	completion powershell
@	completion zsh
@	convert
a	1	0
@	help
a	1	0
@	inspect
a	1	0
@	login
s	cloud	Authenticate with Load Impact
s	influxdb	Authenticate with InfluxDB
a	1	0
@	login cloud
@	login influxdb
@	pause
@	resume
@	run
o	--address	Address of the API server	v
o	--batch	Max parallel batch reqs (default 20)	v
o	--batch-per-host	Max parallel batch reqs per host (default 6)	v
o	--vus|-u	Number of virtual users (default 1)	v
o	--duration|-d	Test duration limit	v
o	--iterations|-i	Script total iteration limit (among all VUs)	v
o	--stage|-s	Add a stage, as `[duration]:[target]`	v
o	--execution-segment	Add a stage, as `[duration]:[target]`	v
o	--execution-segment-sequence	The execution segment sequence	v
o	--paused|-p	Start the test in a paused state	v
o	--no-setup	Don't run setup()	v
o	--no-teardown	Don't run teardown()	v
o	--max-redirects	Follow at most n redirects (default 10)	v
o	--rps	Limit requests per second	v
o	--user-agent	User agent for http requests (default "k6/0.39.0 (https://k6.io/)")	v
o	--http-debug	Log all HTTP requests and responses. Excludes body by default. To include body use…	v
o	--insecure-skip-tls-verify	Skip verification of TLS certificates	v
o	--no-connection-reuse	Disable keep-alive connections	v
o	--no-vu-connection-reuse	Don't reuse connections between iterations	v
o	--min-iteration-duration	Minimum amount of time k6 will take executing a single iteration	v
o	--throw	Throw warnings (like failed http requests) as errors	v
o	--blacklist-ip	Blacklist an ip range from being called	v
o	--block-hostnames	Block a case-insensitive hostname pattern, with optional leading wildcard, from being called	v
o	--summary-trend-stats	Define stats for trend metrics (response times), one or more as 'avg,p(95),...' (default…	v
o	--summary-time-unit	Define the time unit used to display the trend stats. Possible units are: 's', 'ms' and 'us'	v
o	--system-tags	Only include these system tags in metrics (default "proto,subproto,status,method,url,name,group,che…	v
o	--tag	Add a tag to be applied to all samples, as `[name]=[value]`	v
o	--console-output	Redirects the console logging to the provided output file	v
o	--discard-response-bodies	Read but don't process or save HTTP response bodies	v
o	--local-ips	Client IP Ranges and/or CIDRs from which each VU will be making requests, e.g…	v
o	--dns	DNS resolver configuration	v
o	--include-system-env-vars	Pass the real system environment variables to the runtime (default true)	v
o	--compatibility-mode	JavaScript compiler compatibility mode, "extended" or "base"	v
o	--type|-t	Override test type, "js" or "archive"	v
o	--env|-e	Add/override environment variable with VAR=value	v
o	--no-thresholds	Don't run thresholds	v
o	--no-summary	Don't show the summary at the end of the test	v
o	--summary-export	Output the end-of-test summary report to JSON file	v
o	--out|-o	Uri for an external metrics database	v
o	--linger|-l	Keep the API server alive past test end	v
o	--no-usage-report	Don't send anonymous stats to the developers	v
a	1	0
@	scale
o	-h|--help	Help for scale	
o	-m|--max	Max available virtual users	v
o	-u|--vus	Number of virtual users (default 1)	v
@	stats
o	-h|--help	Help for stats	
@	status
o	-h|--help	Help for status	
@	version
o	-h|--help	Help for version	
