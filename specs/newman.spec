@	
s	run	Initiate a Postman Collection run from a given URL or path
s	help	Display help for command
o	-v|--version	Output the version number	
o	-h|--help	Display help for command	
@	run
o	-e|--environment	Specify a URL or path to a Postman Environment	v
o	-g|--globals	Specify a URL or path to a file containing Postman Globals	v
o	-r|--reporters	Specify the reporters to use for this run	V
o	-n|--iteration-count	Define the number of iterations to run	v
o	-d|--iteration-data	Specify a data file to use for iterations (either JSON or CSV)	v
o	--folder	Specify the folder to run from a collection. Can be specified multiple times to run multiple folders	v
o	--global-var	Allows the specification of global variables via the command line, in a key=value format	v
o	--env-var	Allows the specification of environment variables via the command line, in a key=value format	v
o	--export-environment	Exports the final environment to a file after completing the run	v
o	--export-globals	Exports the final globals to a file after completing the run	v
o	--export-collection	Exports the executed collection to a file after completing the run	v
o	--postman-api-key	API Key used to load the resources from the Postman API	v
o	--bail	Specify whether or not to gracefully stop a collection run on encountering an error and whether to…	V
o	--ignore-redirects	Prevents Newman from automatically following 3XX redirect responses	
o	-x|--suppress-exit-code	Specify whether or not to override the default exit code for the current run	
o	--silent	Prevents Newman from showing output to CLI	
o	--disable-unicode	Forces Unicode compliant symbols to be replaced by their plain text equivalents	
o	--color	Enable/Disable colored output (auto|on|off)	v
o	--delay-request	Specify the extent of delay between requests (milliseconds)	V
o	--timeout	Specify a timeout for collection run (milliseconds)	V
o	--timeout-request	Specify a timeout for requests (milliseconds)	V
o	--timeout-script	Specify a timeout for scripts (milliseconds)	V
o	--working-dir	Specify the path to the working directory	v
o	--no-insecure-file-read	Prevents reading the files situated outside of the working directory	
o	-k|--insecure	Disables SSL validations	
o	--ssl-client-cert-list	Specify the path to a client certificates configurations (JSON)	v
o	--ssl-client-cert	Specify the path to a client certificate (PEM)	v
o	--ssl-client-key	Specify the path to a client certificate private key	v
o	--ssl-client-passphrase	Specify the client certificate passphrase (for protected key)	v
o	--ssl-extra-ca-certs	Specify additionally trusted CA certificates (PEM)	v
o	--cookie-jar	Specify the path to a custom cookie jar (serialized tough-cookie JSON)	v
o	--export-cookie-jar	Exports the cookie jar to a file after completing the run	v
o	--verbose	Show detailed information of collection run and each request sent	
o	-h|--help	Display help for command	
a	1	0
=	run	-e
t	filepaths
=	run	-g
t	filepaths
=	run	-d
v	JSON	
v	CSV	
t	filepaths
=	run	--folder
t	filepaths
=	run	--export-environment
t	filepaths
=	run	--export-globals
t	filepaths
=	run	--export-collection
t	filepaths
=	run	--color
v	auto	
v	on	
v	off	
=	run	--working-dir
t	filepaths
=	run	--ssl-client-cert-list
t	filepaths
=	run	--ssl-client-cert
t	filepaths
=	run	--ssl-client-key
t	filepaths
=	run	--ssl-extra-ca-certs
t	filepaths
=	run	--cookie-jar
t	filepaths
=	run	--export-cookie-jar
t	filepaths
#	run	1
t	filepaths
@	help
a	1	0
#	help	1
t	help
