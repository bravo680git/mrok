@	
s	-certreq	Generates a certificate request
s	-changealias	Changes an entry's alias
s	-delete	Deletes an entry
s	-exportcert	Exports certificate
s	-genkeypair	Generate a key pair
s	-genseckey	Generates a secret key
s	-gencert	Generates certificate from a certificate request
s	-importcert	Imports a certificate or a certificate chain
s	-importpass	Imports a password
s	-importkeystore	Imports one or all entries from another keystore
s	-keypasswd	Changes the key password of an entry
s	-list	Lists entries in a keystore
s	-printcert	Prints the content of a certificate
s	-printcertreq	Prints the content of a certificate request
s	-printcrl	Prints the content of a CRL file
s	-storepasswd	Changes the store password of a keystore
o	-h|-?|--help|-help	Show help message	
o	-conf	Specify pre-configured options file	v
@	-certreq
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-sigalg	Signature algorithm name	v
o	-file	Output file name	v
o	-keypass	Key password	v
o	-dname	Distinguished name	v
o	-ext	X.509 extension	v
=	-certreq	-file
t	filepaths
@	-changealias
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-destalias	Destination alias	v
o	-keypass	Key password	v
o	-cacerts	Access the cacerts keystore	
@	-delete
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-cacerts	Access the cacerts keystore	
@	-exportcert
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-rfc	Output in RFC style	
o	-file	Output file name	v
o	-cacerts	Access the cacerts keystore	
=	-exportcert	-file
t	filepaths
@	-genkeypair
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-keyalg	Key algorithm name	v
o	-keysize	Key bit size	v
o	-groupname	Group name. For example, an Elliptic Curve name	v
o	-sigalg	Signature algorithm name	v
o	-destalias	Destination alias	v
o	-dname	Distinguished name	v
o	-startdate	Certificate validity start date/time	v
o	-ext	X.509 extension name	v
o	-validity	Validity number of days	v
o	-keypass	Key password	v
@	-genseckey
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-keypass	Key password	v
o	-keyalg	Key algorithm name	v
o	-keysize	Key bit size	v
@	-gencert
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-rfc	Output in RFC style	
o	-infile	Input file name	v
o	-outfile	Output file name	v
o	-sigalg	Signature algorithm name	v
o	-dname	Distinguished name	v
o	-startdate	Certificate validity start date/time	v
o	-ext	X.509 extension name	v
o	-validity	Validity number of days	v
o	-keypass	Key password	v
=	-gencert	-infile
t	filepaths
=	-gencert	-outfile
t	filepaths
@	-importcert
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-noprompt	Do not prompt	
o	-trustcacerts	Trust certificates from cacerts	
o	-file	Output file name	v
o	-keypass	Key password	v
o	-cacerts	Access the cacerts keystore	
=	-importcert	-file
t	filepaths
@	-importpass
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-keypass	Key password	v
o	-keyalg	Key algorithm name	v
o	-keysize	Key bit size	v
@	-importkeystore
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-srckeystore	Source keystore name	v
o	-destkeystore	Destination keystore name	v
o	-srcstoretype	Source keystore type	v
o	-deststoretype	Destination keystore type	v
o	-srcstorepass	Source keystore password	v
o	-deststorepass	Destination keystore password	v
o	-srcprotected	Source keystore password protected	
o	-destprotected	Destination keystore password protected	
o	-srcprovidername	Source keystore provider name	v
o	-destprovidername	Destination keystore provider name	v
o	-srcalias	Source alias	v
o	-destalias	Destination alias	v
o	-srckeypass	Source key password	v
o	-destkeypass	Destination key password	v
o	-noprompt	Do not prompt	
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
@	-keypasswd
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-keypass	Key password	v
o	-new	New password	v
@	-list
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-protected	Password through protected mechanism	
o	-rfc	Output in RFC style	
o	-cacerts	Access the cacerts keystore	
@	-printcert
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-rfc	Output in RFC style	
o	-file	Input file name	v
o	-sslserver	SSL server host and port	v
o	-jarfile	Signed jar file	v
=	-printcert	-file
t	filepaths
=	-printcert	-jarfile
t	filepaths
@	-printcertreq
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-file	Input file name	v
=	-printcertreq	-file
t	filepaths
@	-printcrl
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-file	Input file name	v
=	-printcrl	-file
t	filepaths
@	-storepasswd
o	-h|-?|--help|-help	Show help message	
o	-v	Verbose output	
o	-alias	Alias name of the entry to process	v
o	-keystore	Keystore name	v
o	-storepass	Keystore password	v
o	-storetype	Keystore type	v
o	-providername	Provider name	v
o	-addprovider	Add security provider by name (e.g. SunPKCS11)	v
o	-providerclass	Add security provider by fully-qualified class name	v
o	-providerarg	Configure argument for -addprovider or -providerclass	v
o	-providerpath	Provider classpath	v
o	-new	New password	v
o	-cacerts	Access the cacerts keystore	
