@	
o	-v|--version	View your current mongosh version	
o	--shell	Enables the shell interface. If you invoke the mongosh command and specify a JavaScript file as an…	
o	--eval	Evaluates a JavaScript expression that is specified as an argument. mongosh does not load its own…	v
o	--help|-h	Returns information on the options and use of the MongoDB Shell	
o	--authenticationDatabase	Specifies the authentication database where the specified --username has been created. See…	v
o	--gssapiHostName	Specify the hostname of a service using GSSAPI/Kerberos. Only required if the hostname of a…	v
o	--gssapiServiceName	Specify the name of the service using GSSAPI/Kerberos. Only required if the service does not use…	v
o	--password|-p	Specifies a password with which to authenticate to a MongoDB database that uses authentication…	v
o	--username|-u	Specifies a username with which to authenticate to a MongoDB database that uses authentication…	v
o	--retryWrites	Enables retryable writes as the default for sessions in the MongoDB Shell	
o	--authenticationMechanism	Specifies the authentication mechanism the MongoDB Shell uses to authenticate to the mongod or…	v
o	--nodb	Prevents the shell from connecting to any database instances	
o	--norc	Prevents the shell from sourcing and evaluating ~/.mongoshrc.js on startup	
o	--quiet	Skips all messages during startup (such as welcome messages and startup warnings) and goes…	
o	--verbose	Increases the verbosity of the shell output during the connection process and when running commands	
o	--port	Specifies the port where the mongod or mongos instance is listening. If --port is not specified…	v
o	--tls	Enables connection to a mongod or mongos that has TLS SSL support enabled	
o	--tlsAllowInvalidHostnames	Disables the validation of the hostnames in the certificate presented by the mongod/mongos…	
o	--tlsAllowInvalidCertificates	Bypasses the validation checks for the certificates presented by the mongod/mongos instance and…	
o	--tlsDisabledProtocols	Disables the specified TLS protocols	v
o	--tlsCAFile	Specifies the .pem file that contains the root certificate chain from the Certificate Authority…	v
o	--tlsCRLFile	Specifies the .pem file that contains the root certificate chain from the Certificate Authority…	v
o	--tlsCertificateKeyFile	Enables connection to a mongod or mongos that has TLS SSL support enabled	v
a	1	0
=		--authenticationMechanism
v	SCRAM-SHA-1	RFC 5802 standard Salted Challenge Response Authentication Mechanism using the SHA-1 hash function
v	SCRAM-SHA-256	RFC 7677 standard Salted Challenge Response Authentication Mechanism using the SHA-256 hash function
v	MONGODB-X509	MongoDB TLS SSL certificate authentication
v	GSSAPI (Kerberos)	External authentication using Kerberos. This mechanism is available only in MongoDB Enterprise
v	PLAIN (LDAP SASL)	External authentication using LDAP. You can also use PLAIN for authenticating in-database users…
=		--port
v	27017	Default-port
=		--tlsDisabledProtocols
v	TLS1_0	
v	TLS1_1	
v	TLS1_2	
v	TLS1_3	(Starting in version 4.0.4, 3.6.9, 3.4.24)
=		--tlsCAFile
t	filepaths
=		--tlsCRLFile
t	filepaths
=		--tlsCertificateKeyFile
t	filepaths
#		1
v	mongodb://localhost:27017	Default Connection String; Equivalent to running mongosh without any commands
v	mongodb+srv://cluster0.example.mongodb.net/sample_geospatial	Atlas Connection String Example
