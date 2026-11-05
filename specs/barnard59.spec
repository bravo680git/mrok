@	
s	run	
s	cube	
s	graph-store	
s	shacl	
s	help	Display help for command
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-q|--quiet	Disable all logging	
o	--enable-buffer-monitor	Enable histogram of buffer usage	
o	--otel-debug	Enable OpenTelemetry console diagnostic output	v
o	--otel-metrics-exporter	OpenTelemetry Metrics exporter to use	v
o	--otel-metrics-interval	Export Metrics interval	v
o	--otel-traces-exporter	OpenTelemetry Traces exporter to use	v
o	-h|--help	Display help for command	
=		--otel-debug
v	NONE	
v	ERROR	
v	WARN	
v	INFO	
v	DEBUG	
v	VERBOSE	
v	ALL	
=		--otel-metrics-exporter
v	otlp	
v	none	
=		--otel-traces-exporter
v	otlp	
v	none	
@	run
o	--output	Output file	V
o	--pipeline	IRI of the pipeline description	V
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-q|--quiet	Disable all logging	
o	-h|--help	Display help for command	
a	1	0
@	cube
s	fetch-metadata	Retrieves cube and its constraint shape from SPARQL endpoint
s	check-metadata	Validate input cube and its constraint against profile shapes
s	fetch-observations	Retrieves cube observations from SPARQL endpoint
s	check-observations	Validate input observations against cube constraint
s	fetch-constraint	Retrieves cube constraint from SPARQL endpoint
s	fetch-cube	Retrieves cube with observations from SPARQL endpoint
s	help	Display help for command
o	-V|--version	Output the version number	
o	-h|--help	Display help for command	
@	cube fetch-metadata
o	--endpoint	SPARQL endpoint	v
o	--cube	Cube URI	v
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-h|--help	Display help for command	
@	cube check-metadata
o	--profile	Cube constraint profile URL	v
o	--profileFormat	Override the profile format	v
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-h|--help	Display help for command	
@	cube fetch-observations
o	--endpoint	SPARQL endpoint	v
o	--cube	Cube URI	v
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-h|--help	Display help for command	
@	cube check-observations
o	--constraint	Cube constraint file	v
o	--batchSize	Batch size	v
o	--maxViolations	Max number of violations	v
o	--sortChunkSize	Sort chunk size	v
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-h|--help	Display help for command	
@	cube fetch-constraint
o	--endpoint	SPARQL endpoint	v
o	--cube	Cube URI	v
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-h|--help	Display help for command	
@	cube fetch-cube
o	--endpoint	SPARQL endpoint	v
o	--cube	Cube URI	v
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-h|--help	Display help for command	
@	cube help
a	1	0
#	cube help	1
t	help
@	graph-store
s	put	Upload RDF documents using SPARQL Graph Store Protocol
s	help	Display help for command
o	-V|--version	Output the version number	
o	-h|--help	Display help for command	
@	graph-store put
o	--source	Glob of RDF documents to upload	v
o	--graph		v
o	--endpoint		v
o	--user		v
o	--password		v
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-h|--help	Display help for command	
@	graph-store help
a	1	0
#	graph-store help	1
t	help
@	shacl
s	validate	Validates the RDF in standard input against a SHACL document
s	report-summary	Human-readable summary of SHACL validation report
s	help	Display help for command
o	-V|--version	Output the version number	
o	-h|--help	Display help for command	
@	shacl validate
o	--shapes	URL or path of the shapes graph	v
o	--shapesMediaType	Override the shapes graph format	v
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-h|--help	Display help for command	
@	shacl report-summary
o	--variable	Variable key/value pairs	v
o	--variable-all	Import all environment variables	
o	-v|--verbose	Enable diagnostic console output	
o	-h|--help	Display help for command	
@	shacl help
a	1	0
#	shacl help	1
t	help
@	help
a	1	0
#	help	1
t	help
