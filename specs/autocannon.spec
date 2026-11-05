@	
o	-c|--connections	The number of concurrent connections to use	v
o	-p|--pipelining	The number of pipelined requests to use	v
o	-d|--duration	The number of seconds to run the autocannon	v
o	-a|--amount	The number of requests to make before exiting the benchmark	v
o	-L	The number of milliseconds to elapse between taking samples. This controls the sample interval, &…	v
o	-S|--socketPath	A path to a Unix Domain Socket or a Windows Named Pipe. A URL is still required to send the…	v
o	-w|--workers	Number of worker threads to use to fire requests	v
o	-W|--warmup	Use a warm up interval before starting sampling. This enables startup processes to finish and…	v
o	--on-port	Start the command listed after -- on the command line. When it starts listening on a port, start…	v
o	-m|--method	The HTTP method to use	v
o	-t|--timeout	The number of seconds before timing out and resetting a connection	v
o	-T|--title	The title to place in the results for identification	v
o	-b|--body	The body of the request	v
o	-F|--form		v
o	-i|--input	The body of the request	v
o	-H|--headers	The request headers	v
o	--har	When provided, Autocannon will use requests from the HAR file	v
o	-B|--bailout	The number of failures before initiating a bailout	v
o	-M|--maxConnectionRequests	The max number of requests to make per connection to the server	v
o	-O|--maxOverallRequests	The max number of requests to make overall to the server	v
o	-r|--connectionRate	The max number of requests to make per second from an individual connection	v
o	-R|--overallRate	The max number of requests to make per second from all connections	v
o	-C|--ignoreCoordinatedOmission	Ignore the coordinated omission issue when requests should be sent at a fixed rate using…	
o	-D|--reconnectRate	The number of requests to make before resetting a connections connection to the server	v
o	-n|--no-progress	Don't render the progress bar. default: false	
o	-l|--latency	Print all the latency data. default: false	
o	-I|--idReplacement	Enable replacement of [<id>] with a randomly generated ID within the request body. default: false	
o	-j|--jsonPath	Print the output as newline delimited JSON. This will cause the progress bar and results not to be…	
o	-f|--forever	Run the benchmark forever. Efficiently restarts the benchmark on completion	
o	-s|--servername	Server name for the SNI (Server Name Indication) TLS extension. Defaults to the hostname of the…	
o	-x|--excludeErrorStats	Exclude error statistics (non-2xx HTTP responses) from the final latency and bytes per second…	
o	-E|--expectBody	Ensure the body matches this value. If enabled, mismatches count towards bailout. Enabling this…	v
o	--renderStatusCodes	Print status codes and their respective statistics	
o	--cert	Path to cert chain in pem format	v
o	--key	Path to private key for specified cert in pem format	v
o	--ca	Path to trusted ca certificates for the test. This argument accepts both a single file as well as…	v
o	--debug	Print connection errors to stderr	
o	-v|--version	Print the version number	
o	-V|--verbose	Print the table with results (default: true)	
o	-h|--help	Print help	
a	1	0
=		-m
v	GET	
v	POST	
v	PUT	
v	DELETE	
v	PATCH	
v	HEAD	
v	OPTIONS	
v	TRACE	
=		-i
t	filepaths
=		--har
t	filepaths
=		--cert
t	filepaths
=		--key
t	filepaths
=		--ca
t	filepaths
