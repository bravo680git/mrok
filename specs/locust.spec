@	
o	-v|--version	Show program's version number and exit	
o	-h|--help	Show this help message and exit	
o	-f|--locustfile	Show program's version number and exit	v
o	--config	Config file path	v
o	-H|--host	Host to load test in the following format: http://10.21.32.33	
o	-u|--users	Peak number of concurrent Locust users. Primarily used together with --headless or --autostart	
o	-r|--spawn-rate	Rate to spawn users at (users per second). Primarily used together with --headless or --autostart	
o	-t|--run-time	Stop after the specified amount of time, e.g. (300s, 20m, 3h, 1h30m, etc.)	
o	-l|--list	Show list of possible User classes and exit	
o	--web-host	Host to bind the web interface to. Defaults to '*' (all interfaces)	
o	-P|--web-port	Port on which to run web host	
o	--headless	Disable the web interface, and start the test immediately	
o	--autostart	Starts the test immediately (without disabling the web UI)	
o	--autoquit	Quits Locust entirely, X seconds after the run is finished	
o	--web-auth	Turn on Basic Auth for the web interface. e.g. username:password	
o	--tls-cert	Optional path to TLS certificate to use to serve over HTTPS	v
o	--tls-key	Optional path to TLS private key to use to serve over HTTPS	v
o	--class-picker	Enable select boxes in the web interface to choose from all available User classes and Shape classes	
o	--master	Set locust to run in distributed mode with this process as master	
o	--master-bind-host	Interfaces (hostname, ip) that locust master should bind to	
o	--master-bind-port	Port that locust master should bind to	
o	--expect-workers	How many workers master should expect to connect before starting the test (only when…	
o	--expect-workers-max-wait	How long should the master wait for workers to connect before giving up. Defaults to wait forever	
o	--worker	Set locust to run in distributed mode with this process as worker	
o	--master-host	Host or IP address of locust master for distributed load testing. Only used when running with…	
o	--master-port	Show list of possible User classes and exit	
o	--csv	Store current request stats to files in CSV format	
o	--csv-full-history	Store each stats entry in CSV format to _stats_history.csv file. You must also specify the '--csv'…	
o	--print-stats	Print stats in the console	
o	--only-summary	Only print the summary stats	
o	--reset-stats	Reset statistics once spawning has been completed. Should be set on both master and workers when…	
o	--html	Store HTML report to file path specified	
o	--skip-log-setup	Disable Locust's logging setup. Instead, the configuration is provided by the Locust test or…	
o	--loglevel	Choose between DEBUG/INFO/WARNING/ERROR/CRITICAL. Default is INFO	v
o	--logfile	Path to log file. If not set, log will go to stderr	v
o	--show-task-ratio	Print table of the User classes' task execution ratio. Use this with non-zero --user option if…	
o	--show-task-ratio-json	Print json data of the User classes' task execution ratio. Use this with non-zero --user option if…	
o	--exit-code-on-error	Sets the process exit code to use when a test result contain any failure or error	
o	--equal-weights	Use equally distributed task weights, overriding the weights specified in the locustfile	
o	--enable-rebalancing	Allow to automatically rebalance users if new workers are added or removed during a test run	
o	-T|--tags	List of tags to include in the test, so only tasks with any matching tags will be executed	
o	--E|--exclude-tags	List of tags to exclude from the test, so only tasks with no matching tags will be executed	
=		-f
t	filepaths
=		--config
t	filepaths
=		--tls-cert
t	filepaths
=		--tls-key
t	filepaths
=		--loglevel
v	INFO	
v	WARNING	
v	DEBUG	
v	ERROR	
v	CRITICAL	
=		--logfile
t	filepaths
