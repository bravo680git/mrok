@	
o	--help	Returns information on the options and use of mongoimport	
o	--verbose|-v	Increases the amount of internal reporting returned on standard output or in log files	
o	--quiet	Runs mongoimport in a quiet mode that attempts to limit the amount of output	
o	--version	Returns the mongoimport release number	
o	--config	Specifies the full path to a YAML configuration file containing sensitive values for the following…	v
o	--uri	Specifies the resolvable URI connection string of the MongoDB deployment	v
o	--host|-h	Specifies the resolvable hostname of the MongoDB deployment	v
o	--port	Specifies the TCP port on which the MongoDB instance listens for client connections	v
o	--ssl	Enables connection to a mongod or mongos that has TLS/SSL support enabled	
o	--sslCAFile	Specifies the .pem file that contains the root certificate chain from the Certificate Authority	v
o	--sslPEMKeyFile	Specifies the .pem file that contains both the TLS/SSL certificate and key	v
o	--sslPEMKeyPassword	Specifies the password to de-crypt the certificate-key file (i.e. --sslPEMKeyFile)	v
o	--sslCRLFile	Specifies the .pem file that contains the Certificate Revocation List	v
o	--sslAllowInvalidCertificates	Bypasses the validation checks for server certificates and allows the use of invalid certificates	
o	--sslAllowInvalidHostnames	Disables the validation of the hostnames in TLS/SSL certificates	
o	--username|-u	Specifies a username with which to authenticate to a MongoDB database that uses authentication	v
o	--password|-p	Specifies a password with which to authenticate to a MongoDB database that uses authentication	v
o	--awsSessionToken	Specifies the session token for MONGODB-AWS authentication mechanism	v
o	--authenticationDatabase	Specifies the authentication database where the specified --username has been created	v
o	--authenticationMechanism	Specifies the authentication mechanism the mongoimport instance uses to authenticate to the mongod…	v
o	--gssapiServiceName	Specify the name of the service using GSSAPI/Kerberos. This option is available only in MongoDB…	v
o	--gssapiHostName	Specify the hostname of the service using GSSAPI/Kerberos. This option is available only in…	v
o	--db|-d	Specifies the name of the database on which to run the mongoimport	v
o	--collection|-c	Specifies the name of the collection to import	v
o	--fields|-f	Specify a comma separated list of field names when importing CSV or TSV files that do not have…	v
o	--fieldFile	Specify a file containing a comma separated list of field names when importing CSV or TSV files…	v
o	--ignoreBlanks	Ignores empty fields in CSV and TSV exports	
o	--type	Specifies the file type to import	v
o	--file	Specifies the location and name of a file containing the data to import	v
o	--drop	Modifies the import process so that the target instance drops the collection before importing the…	
o	--headerline	Treats the first line of the input file as a header line	
o	--useArrayIndexFields	Interpret natural numbers in fields as array indexes when importing CSV or TSV files	
o	--mode	Specifies how the import process should handle existing documents in the database that match…	v
o	--upsertFields	Specifies a list of fields for the query portion of the import process	v
o	--stopOnError	Forces mongoimport to halt the insert operation at the first error rather than continuing the…	
o	jsonArray	Accepts the import of data expressed with multiple MongoDB documents within a single JSON array	
o	--legacy	Indicates that the import data is in Extended JSON v1 format	
o	--maintainInsertionOrder	Maintains the order of documents in the import file when inserting documents into the database	
o	--numInsertionWorkers	Specifies the number of insertion workers to run concurrently	v
o	--writeConcern	Specifies the write concern for each write operation that mongoimport performs	v
o	--bypassDocumentValidation	Enables mongoimport to bypass document validation during the operation	
o	--columnsHaveTypes	Instructs mongoimport that the field list specified in --fields, --fieldFile, or --headerline…	
o	--parseGrace	Specifies how mongoimport handles type coercion failures when importing CSV or TSV files with…	v
=		--config
d
=		--uri
v	mongodb://localhost:27017	Default Connection String
v	mongodb+srv://username:password@cluster0.example.mongodb.net/database	Atlas Connection String Example
=		--host
v	localhost:27017	Default host
=		--port
v	27017	Default port
=		--sslCAFile
d
=		--sslPEMKeyFile
d
=		--sslCRLFile
d
=		--authenticationMechanism
v	SCRAM-SHA-1	Default
v	SCRAM-SHA-256	
v	MONGODB-X509	
v	MONGODB-AWS	
v	GSSAPI	
v	PLAIN	
=		--fieldFile
d
=		--type
v	json	JSON
v	csv	Comma-separated values
v	tsv	Tab-separated values
=		--file
d
=		--mode
v	insert	Insert the documents in the import file
v	upsert	Replace existing documents in the database with matching documents from the import file
v	merge	Merge existing documents that match a document in the import file with the new document
v	delete	Delete existing documents in the database that match a document in the import file
=		--parseGrace
v	autoCast	
v	skipField	
v	skipRow	
v	stop	
