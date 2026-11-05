@	
s	acl	Manipulate Fastly ACLs (Access Control Lists)
s	acl-entry	Manipulate Fastly ACL (Access Control List) entries
s	auth-token	Manage API tokens for Fastly service users
s	backend	Manipulate Fastly service version backends
s	compute	Manage Compute@Edge packages
s	config	Display the Fastly CLI configuration
s	dictionary	Manipulate Fastly edge dictionaries
s	dictionary-item	Manipulate Fastly edge dictionary items
s	domain	Manipulate Fastly service version domains
s	healthcheck	Manipulate Fastly service version healthchecks
s	ip-list	List Fastly's public IPs
s	log-tail	Tail Compute@Edge logs
s	logging	Manipulate Fastly service version logging endpoints
s	pops	List Fastly datacenters
s	profile	Manage user profiles
s	purge	Invalidate objects in the Fastly cache
s	service	Manipulate Fastly services
s	service-version	Manipulate Fastly service versions
s	stats	View historical and realtime statistics for a Fastly service
s	update	Update the CLI to the latest version
s	user	Manipulate users of the Fastly API and web interface
s	vcl	Manipulate Fastly service version VCL
s	version	Display version information for the Fastly CLI
s	whoami	Get information about the currently authenticated account
o	--help	Show context-sensitive help	
o	--accept-defaults	Accept default options for all interactive prompts apart from Yes/No confirmations	
o	--auto-yes	Answer yes automatically to all Yes/No confirmations. This may suppress security warnings	
o	--non-interactive	Do not prompt for user input - suitable for CI processes. Equivalent to --accept-defaults and…	
o	--profile	Switch account profile for single command execution (see also: 'fastly profile switch')	v
o	--token	Fastly API token (or via FASTLY_API_TOKEN)	v
o	--verbose	Verbose logging	
@	acl
s	create	Create a new ACL attached to the specified service version
s	delete	Delete an ACL from the specified service version
s	describe	Retrieve a single ACL by name for the version and service
s	list	List ACLs
s	update	Update an ACL for a particular service and version
@	acl create
o	--name	Name for the ACL. Must start with an alphanumeric character and contain only alphanumeric…	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	acl delete
o	--name	The name of the ACL to delete	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	acl describe
o	--name	The name of the ACL	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	acl list
o	--version	'latest', 'active', or the number of a specific version	v
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	acl update
o	--name	The name of the ACL to update	v
o	--new-name	The new name of the ACL	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	acl-entry
s	create	Add an ACL entry to an ACL
s	delete	Delete an ACL entry from a specified ACL
s	describe	Retrieve a single ACL entry
s	list	List ACLs
s	update	Update an ACL entry for a specified ACL
@	acl-entry create
o	--acl-id	Alphanumeric string identifying a ACL	v
o	--ip	An IP address	v
o	--comment	A freeform descriptive note	v
o	--negated	Whether to negate the match	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--subnet	Number of bits for the subnet mask applied to the IP address	v
@	acl-entry delete
o	--acl-id	Alphanumeric string identifying a ACL	v
o	--id	Alphanumeric string identifying an ACL Entry	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	acl-entry describe
o	--acl-id	Alphanumeric string identifying a ACL	v
o	--id	Alphanumeric string identifying an ACL Entry	v
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	acl-entry list
o	--acl-id	Alphanumeric string identifying a ACL	v
o	--direction	Direction in which to sort results	v
o	--json	Render output as JSON	
o	--page	Page number of data set to fetch	v
o	--per-page	Number of records per page	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--sort	Field on which to sort	v
@	acl-entry update
o	--acl-id	Alphanumeric string identifying a ACL	v
o	--comment	A freeform descriptive note	v
o	--file	Batch update json passed as file path or content, e.g. $(< batch.json)	v
o	--id	Alphanumeric string identifying an ACL Entry	v
o	--ip	An IP address	v
o	--negated	Whether to negate the match	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--subnet	Number of bits for the subnet mask applied to the IP address	v
@	auth-token
s	create	Create an API token
s	delete	Revoke an API token
s	describe	Get the current API token
s	list	List API tokens
@	auth-token create
o	--password	User password corresponding with --token or $FASTLY_API_TOKEN	v
o	--expires	Time-stamp (UTC) of when the token will expire	v
o	--name	Name of the token	v
o	--scope	Authorization scope (repeat flag per scope)	v
o	--services	A comma-separated list of alphanumeric strings identifying services (default: access to all…	v
@	auth-token delete
o	--current	Revoke the token used to authenticate the request	
o	--file	Revoke tokens in bulk from a newline delimited list of tokens	v
o	--id	Alphanumeric string identifying a token	v
@	auth-token describe
o	--json	Render output as JSON	
@	auth-token list
o	--customer-id	Alphanumeric string identifying the customer (falls back to FASTLY_CUSTOMER_ID)	v
o	--json	Render output as JSON	
@	backend
s	create	Create a backend on a Fastly service version
s	delete	Delete a backend on a Fastly service version
s	describe	Show detailed information about a backend on a Fastly service version
s	list	List backends on a Fastly service version
s	update	Update a backend on a Fastly service version
@	backend create
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Backend name	v
o	--address	A hostname, IPv4, or IPv6 address for the backend	v
o	--comment	A descriptive note	v
o	--port	Port number of the address	v
o	--override-host	The hostname to override the Host header	v
o	--connect-timeout	How long to wait for a timeout in milliseconds	v
o	--max-conn	Maximum number of connections	v
o	--first-byte-timeout	How long to wait for the first bytes in milliseconds	v
o	--between-bytes-timeout	How long to wait between bytes in milliseconds	v
o	--auto-loadbalance	Whether or not this backend should be automatically load balanced	
o	--weight	Weight used to load balance this backend against others	v
o	--request-condition	Condition, which if met, will select this backend during a request	v
o	--healthcheck	The name of the healthcheck to use with this backend	v
o	--shield	The shield POP designated to reduce inbound load on this origin by serving the cached data to the…	v
o	--use-ssl	Whether or not to use SSL to reach the backend	
o	--ssl-check-cert	Be strict on checking SSL certs	
o	--ssl-ca-cert	CA certificate attached to origin	v
o	--ssl-client-cert	Client certificate attached to origin	v
o	--ssl-client-key	Client key attached to origin	v
o	--ssl-cert-hostname	Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all	v
o	--ssl-sni-hostname	Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all	v
o	--min-tls-version	Minimum allowed TLS version on SSL connections to this backend	v
o	--max-tls-version	Maximum allowed TLS version on SSL connections to this backend	v
o	--ssl-ciphers	Colon delimited list of OpenSSL ciphers (see https://www.openssl.org/docs/man1.0.2/man1/ciphers…	v
@	backend delete
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Backend name	v
@	backend describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	Name of backend	v
@	backend list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	backend update
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Backend name	v
o	--new-name	New backend name	v
o	--comment	A descriptive note	v
o	--address	A hostname, IPv4, or IPv6 address for the backend	v
o	--port	Port number of the address	v
o	--override-host	The hostname to override the Host header	v
o	--connect-timeout	How long to wait for a timeout in milliseconds	v
o	--max-conn	Maximum number of connections	v
o	--first-byte-timeout	How long to wait for the first bytes in milliseconds	v
o	--between-bytes-timeout	How long to wait between bytes in milliseconds	v
o	--auto-loadbalance	Whether or not this backend should be automatically load balanced	
o	--weight	Weight used to load balance this backend against others	v
o	--request-condition	Condition, which if met, will select this backend during a request	v
o	--healthcheck	The name of the healthcheck to use with this backend	v
o	--shield	The shield POP designated to reduce inbound load on this origin by serving the cached data to the…	v
o	--use-ssl	Whether or not to use SSL to reach the backend	
o	--ssl-check-cert	Be strict on checking SSL certs	
o	--ssl-ca-cert	CA certificate attached to origin	v
o	--ssl-client-cert	Client certificate attached to origin	v
o	--ssl-client-key	Client key attached to origin	v
o	--ssl-cert-hostname	Overrides ssl_hostname, but only for cert verification. Does not affect SNI at all	v
o	--ssl-sni-hostname	Overrides ssl_hostname, but only for SNI in the handshake. Does not affect cert validation at all	v
o	--min-tls-version	Minimum allowed TLS version on SSL connections to this backend	v
o	--max-tls-version	Maximum allowed TLS version on SSL connections to this backend	v
o	--ssl-ciphers	Colon delimited list of OpenSSL ciphers (see https://www.openssl.org/docs/man1.0.2/man1/ciphers…	v
@	compute
s	build	Build a Compute@Edge package locally
s	deploy	Deploy a package to a Fastly Compute@Edge service
s	init	Initialize a new Compute@Edge package locally
s	pack	Package a pre-compiled Wasm binary for a Fastly Compute@Edge service
s	publish	Build and deploy a Compute@Edge package to a Fastly service
s	serve	Build and run a Compute@Edge package locally
s	update	Update a package on a Fastly Compute@Edge service version
s	validate	Validate a Compute@Edge package
@	compute build
o	--include-source	Include source code in built package	
o	--language	Language type	v
o	--name	Package name	v
o	--skip-verification	Skip verification steps and force build	
o	--timeout	Timeout, in seconds, for the build compilation step	v
@	compute deploy
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--comment	Human-readable comment	v
o	--domain	The name of the domain associated to the package	v
o	--name	Package name	v
o	--package	Path to a package tar.gz	v
@	compute init
o	--name	Name of package, falls back to --directory	v
o	--description	Description of the package	v
o	--directory	Destination to write the new package, defaulting to the current directory	v
o	--author	Author(s) of the package	v
o	--language	Language of the package	v
o	--from	Local project directory, or Git repository URL, or URL referencing a .zip/.tar.gz file, containing…	v
o	--force	Skip non-empty directory verification step and force new project creation	
@	compute pack
o	--wasm-binary	Path to a pre-compiled Wasm binary	v
@	compute publish
o	--comment	Human-readable comment	v
o	--domain	The name of the domain associated to the package	v
o	--include-source	Include source code in built package	
o	--language	Language type	v
o	--name	Package name	v
o	--package	Path to a package tar.gz	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--skip-verification	Skip verification steps and force build	
o	--timeout	Timeout, in seconds, for the build compilation step	v
@	compute serve
o	--addr	The IPv4 address and port to listen on	v
o	--env	The environment configuration to use (e.g. stage)	v
o	--file	The Wasm file to run	v
o	--include-source	Include source code in built package	
o	--language	Language type	v
o	--name	Package name	v
o	--skip-build	Skip the build step	
o	--skip-verification	Skip verification steps and force build	
o	--timeout	Timeout, in seconds, for the build compilation step	v
o	--watch	Watch for file changes, then rebuild project and restart local server	
@	compute update
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--package	Path to a package tar.gz	v
@	compute validate
o	--package	Path to a package tar.gz	v
@	config
o	--location	Print the location of the CLI configuration file	
@	dictionary
s	create	Create a Fastly edge dictionary on a Fastly service version
s	delete	Delete a Fastly edge dictionary from a Fastly service version
s	describe	Show detailed information about a Fastly edge dictionary
s	list	List all dictionaries on a Fastly service version
s	update	Update name of dictionary on a Fastly service version
@	dictionary create
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Name of Dictionary	v
o	--write-only	Whether to mark this dictionary as write-only. Can be true or false (defaults to false)	v
@	dictionary delete
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Name of Dictionary	v
@	dictionary describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	Name of Dictionary	v
@	dictionary list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	dictionary update
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Old name of Dictionary	v
o	--new-name	New name of Dictionary	v
o	--write-only	Whether to mark this dictionary as write-only. Can be true or false (defaults to false)	v
@	dictionary-item
s	create	Create a new item on a Fastly edge dictionary
s	delete	Delete an item from a Fastly edge dictionary
s	describe	Show detailed information about a Fastly edge dictionary item
s	list	List items in a Fastly edge dictionary
s	update	Update or insert an item on a Fastly edge dictionary
@	dictionary-item create
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--dictionary-id	Dictionary ID	v
o	--key	Dictionary item key	v
o	--value	Dictionary item value	v
@	dictionary-item delete
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--dictionary-id	Dictionary ID	v
o	--key	Dictionary item key	v
@	dictionary-item describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--dictionary-id	Dictionary ID	v
o	--key	Dictionary item key	v
@	dictionary-item list
o	--dictionary-id	Dictionary ID	v
o	--direction	Direction in which to sort results	v
o	--json	Render output as JSON	
o	--page	Page number of data set to fetch	v
o	--per-page	Number of records per page	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--sort	Field on which to sort	v
@	dictionary-item update
o	--dictionary-id	Dictionary ID	v
o	--file	Batch update json file	v
o	--key	Dictionary item key	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--value	Dictionary item value	v
@	domain
s	create	Create a domain on a Fastly service version
s	delete	Delete a domain on a Fastly service version
s	describe	Show detailed information about a domain on a Fastly service version
s	list	List domains on a Fastly service version
s	update	Update a domain on a Fastly service version
s	validate	Checks the status of a specific domain's DNS record for a Service Version
@	domain create
o	--name	Domain name	v
o	--comment	A descriptive note	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
@	domain delete
o	--name	Domain name	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
@	domain describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	Name of domain	v
@	domain list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	domain update
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Domain name	v
o	--new-name	New domain name	v
o	--comment	A descriptive note	v
@	domain validate
o	--version	'latest', 'active', or the number of a specific version	v
o	--all	Checks the status of all domains' DNS records for a Service Version	
o	--name	The name of the domain associated with this service	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	healthcheck
s	create	Create a healthcheck on a Fastly service version
s	delete	Delete a healthcheck on a Fastly service version
s	describe	Show detailed information about a healthcheck on a Fastly service version
s	list	List healthchecks on a Fastly service version
s	update	Update a healthcheck on a Fastly service version
@	healthcheck create
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Healthcheck name	v
o	--comment	A descriptive note	v
o	--method	Which HTTP method to use	v
o	--host	Which host to check	v
o	--path	The path to check	v
o	--http-version	Whether to use version 1.0 or 1.1 HTTP	v
o	--timeout	Timeout in milliseconds	v
o	--check-interval	How often to run the healthcheck in milliseconds	v
o	--expected-response	The status code expected from the host	v
o	--window	The number of most recent healthcheck queries to keep for this healthcheck	v
o	--threshold	How many healthchecks must succeed to be considered healthy	v
o	--initial	When loading a config, the initial number of probes to be seen as OK	v
@	healthcheck delete
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Healthcheck name	v
@	healthcheck describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	Name of healthcheck	v
@	healthcheck list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	healthcheck update
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	Healthcheck name	v
o	--new-name	Healthcheck name	v
o	--comment	A descriptive note	v
o	--method	Which HTTP method to use	v
o	--host	Which host to check	v
o	--path	The path to check	v
o	--http-version	Whether to use version 1.0 or 1.1 HTTP	v
o	--timeout	Timeout in milliseconds	v
o	--check-interval	How often to run the healthcheck in milliseconds	v
o	--expected-response	The status code expected from the host	v
o	--window	The number of most recent healthcheck queries to keep for this healthcheck	v
o	--threshold	How many healthchecks must succeed to be considered healthy	v
o	--initial	When loading a config, the initial number of probes to be seen as OK	v
@	ip-list
@	log-tail
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--from	From time, in Unix seconds	v
o	--to	To time, in Unix seconds	v
o	--sort-buffer	Duration of sort buffer for received logs	v
o	--search-padding	Time beyond from/to to consider in searches	v
o	--stream	Output: stdout, stderr, both (default)	v
@	logging
s	azureblob	Manipulate Fastly service version Azure Blob Storage logging endpoints
s	bigquery	Manipulate Fastly service version BigQuery logging endpoints
s	cloudfiles	Manipulate Fastly service version Cloudfiles logging endpoints
s	datadog	Manipulate Fastly service version Datadog logging endpoints
s	digitalocean	Manipulate Fastly service version DigitalOcean Spaces logging endpoints
s	elasticsearch	Manipulate Fastly service version Elasticsearch logging endpoints
s	ftp	Manipulate Fastly service version FTP logging endpoints
s	gcs	Manipulate Fastly service version GCS logging endpoints
s	googlepubsub	Manipulate Fastly service version Google Cloud Pub/Sub logging endpoints
s	heroku	Manipulate Fastly service version Heroku logging endpoints
s	honeycomb	Manipulate Fastly service version Honeycomb logging endpoints
s	https	Manipulate Fastly service version HTTPS logging endpoints
s	kafka	Manipulate Fastly service version Kafka logging endpoints
s	kinesis	Manipulate a Kinesis logging endpoint for a specific Fastly service version
s	logentries	Manipulate Fastly service version Logentries logging endpoints
s	loggly	Manipulate Fastly service version Loggly logging endpoints
s	logshuttle	Manipulate Fastly service version Logshuttle logging endpoints
s	newrelic	Manipulate a NewRelic logging endpoint for a specific Fastly service version
s	openstack	Manipulate Fastly service version OpenStack logging endpoints
s	papertrail	Manipulate Fastly service version Papertrail logging endpoints
s	s3	Manipulate Fastly service version S3 logging endpoints
s	scalyr	Manipulate Fastly service version Scalyr logging endpoints
s	sftp	Manipulate Fastly service version SFTP logging endpoints
s	splunk	Manipulate Fastly service version Splunk logging endpoints
s	sumologic	Manipulate Fastly service version Sumologic logging endpoints
s	syslog	Manipulate Fastly service version Syslog logging endpoints
@	logging azureblob
s	create	Create an Azure Blob Storage logging endpoint on a Fastly service version
s	delete	Delete an Azure Blob Storage logging endpoint on a Fastly service version
s	describe	Show detailed information about an Azure Blob Storage logging endpoint on a Fastly service version
s	list	List Azure Blob Storage logging endpoints on a Fastly service version
s	update	Update an Azure Blob Storage logging endpoint on a Fastly service version
@	logging azureblob create
o	--name	The name of the Azure Blob Storage logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--container	The name of the Azure Blob Storage container in which to store logs	v
o	--account-name	The unique Azure Blob Storage namespace in which your data objects are stored	v
o	--sas-token	The Azure shared access signature providing write access to the blob service objects. Be sure to…	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--path	The path to upload logs to	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--file-max-bytes	The maximum size of a log file in bytes	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging azureblob delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Azure Blob Storage logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging azureblob describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Azure Blob Storage logging object	v
@	logging azureblob list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging azureblob update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Azure Blob Storage logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Azure Blob Storage logging object	v
o	--container	The name of the Azure Blob Storage container in which to store logs	v
o	--account-name	The unique Azure Blob Storage namespace in which your data objects are stored	v
o	--sas-token	The Azure shared access signature providing write access to the blob service objects. Be sure to…	v
o	--path	The path to upload logs to	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--file-max-bytes	The maximum size of a log file in bytes	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging bigquery
s	create	Create a BigQuery logging endpoint on a Fastly service version
s	delete	Delete a BigQuery logging endpoint on a Fastly service version
s	describe	Show detailed information about a BigQuery logging endpoint on a Fastly service version
s	list	List BigQuery endpoints on a Fastly service version
s	update	Update a BigQuery logging endpoint on a Fastly service version
@	logging bigquery create
o	--name	The name of the BigQuery logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--project-id	Your Google Cloud Platform project ID	v
o	--dataset	Your BigQuery dataset	v
o	--table	Your BigQuery table	v
o	--user	Your Google Cloud Platform service account email address. The client_email field in your service…	v
o	--secret-key	Your Google Cloud Platform account secret key. The private_key field in your service account…	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--template-suffix	BigQuery table name suffix template	v
o	--format	Apache style log formatting. Must produce JSON that matches the schema of your BigQuery table	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
@	logging bigquery delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the BigQuery logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging bigquery describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the BigQuery logging object	v
@	logging bigquery list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging bigquery update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the BigQuery logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the BigQuery logging object	v
o	--project-id	Your Google Cloud Platform project ID	v
o	--dataset	Your BigQuery dataset	v
o	--table	Your BigQuery table	v
o	--user	Your Google Cloud Platform service account email address. The client_email field in your service…	v
o	--secret-key	Your Google Cloud Platform account secret key. The private_key field in your service account…	v
o	--template-suffix	BigQuery table name suffix template	v
o	--format	Apache style log formatting. Must produce JSON that matches the schema of your BigQuery table	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
@	logging cloudfiles
s	create	Create a Cloudfiles logging endpoint on a Fastly service version
s	delete	Delete a Cloudfiles logging endpoint on a Fastly service version
s	describe	Show detailed information about a Cloudfiles logging endpoint on a Fastly service version
s	list	List Cloudfiles endpoints on a Fastly service version
s	update	Update a Cloudfiles logging endpoint on a Fastly service version
@	logging cloudfiles create
o	--name	The name of the Cloudfiles logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--user	The username for your Cloudfile account	v
o	--access-key	Your Cloudfile account access key	v
o	--bucket	The name of your Cloudfiles container	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--path	The path to upload logs to	v
o	--region	The region to stream logs to. One of: DFW-Dallas, ORD-Chicago, IAD-Northern Virginia, LON-London…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging cloudfiles delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Cloudfiles logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging cloudfiles describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Cloudfiles logging object	v
@	logging cloudfiles list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging cloudfiles update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Cloudfiles logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Cloudfiles logging object	v
o	--user	The username for your Cloudfile account	v
o	--access-key	Your Cloudfile account access key	v
o	--bucket	The name of your Cloudfiles container	v
o	--path	The path to upload logs to	v
o	--region	The region to stream logs to. One of: DFW-Dallas, ORD-Chicago, IAD-Northern Virginia, LON-London…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging datadog
s	create	Create a Datadog logging endpoint on a Fastly service version
s	delete	Delete a Datadog logging endpoint on a Fastly service version
s	describe	Show detailed information about a Datadog logging endpoint on a Fastly service version
s	list	List Datadog endpoints on a Fastly service version
s	update	Update a Datadog logging endpoint on a Fastly service version
@	logging datadog create
o	--name	The name of the Datadog logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--auth-token	The API key from your Datadog account	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--region	The region that log data will be sent to. One of US or EU. Defaults to US if undefined	v
o	--format	Apache style log formatting. For details on the default value refer to the documentation…	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging datadog delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Datadog logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging datadog describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Datadog logging object	v
@	logging datadog list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging datadog update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Datadog logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Datadog logging object	v
o	--auth-token	The API key from your Datadog account	v
o	--region	The region that log data will be sent to. One of US or EU. Defaults to US if undefined	v
o	--format	Apache style log formatting. For details on the default value refer to the documentation…	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging digitalocean
s	create	Create a DigitalOcean Spaces logging endpoint on a Fastly service version
s	delete	Delete a DigitalOcean Spaces logging endpoint on a Fastly service version
s	describe	Show detailed information about a DigitalOcean Spaces logging endpoint on a Fastly service version
s	list	List DigitalOcean Spaces logging endpoints on a Fastly service version
s	update	Update a DigitalOcean Spaces logging endpoint on a Fastly service version
@	logging digitalocean create
o	--name	The name of the DigitalOcean Spaces logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--bucket	The name of the DigitalOcean Space	v
o	--access-key	Your DigitalOcean Spaces account access key	v
o	--secret-key	Your DigitalOcean Spaces account secret key	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--domain	The domain of the DigitalOcean Spaces endpoint (default 'nyc3.digitaloceanspaces.com')	v
o	--path	The path to upload logs to	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging digitalocean delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the DigitalOcean Spaces logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging digitalocean describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the DigitalOcean Spaces logging object	v
@	logging digitalocean list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging digitalocean update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the DigitalOcean Spaces logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the DigitalOcean Spaces logging object	v
o	--bucket	The name of the DigitalOcean Space	v
o	--domain	The domain of the DigitalOcean Spaces endpoint (default 'nyc3.digitaloceanspaces.com')	v
o	--access-key	Your DigitalOcean Spaces account access key	v
o	--secret-key	Your DigitalOcean Spaces account secret key	v
o	--path	The path to upload logs to	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging elasticsearch
s	create	Create an Elasticsearch logging endpoint on a Fastly service version
s	delete	Delete an Elasticsearch logging endpoint on a Fastly service version
s	describe	Show detailed information about an Elasticsearch logging endpoint on a Fastly service version
s	list	List Elasticsearch endpoints on a Fastly service version
s	update	Update an Elasticsearch logging endpoint on a Fastly service version
@	logging elasticsearch create
o	--name	The name of the Elasticsearch logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--index	The name of the Elasticsearch index to send documents (logs) to. The index must follow the…	v
o	--url	The URL to stream logs to. Must use HTTPS	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--pipeline	The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before…	v
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--tls-hostname	The hostname used to verify the server's certificate. It can either be the Common Name or a…	v
o	--format	Apache style log formatting. Your log must produce valid JSON that Elasticsearch can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--request-max-entries	Maximum number of logs to append to a batch, if non-zero. Defaults to 10k	v
o	--request-max-bytes	Maximum size of log batch, if non-zero. Defaults to 100MB	v
@	logging elasticsearch delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Elasticsearch logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging elasticsearch describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Elasticsearch logging object	v
@	logging elasticsearch list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging elasticsearch update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Elasticsearch logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Elasticsearch logging object	v
o	--index	The name of the Elasticsearch index to send documents (logs) to. The index must follow the…	v
o	--url	The URL to stream logs to. Must use HTTPS	v
o	--pipeline	The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before…	v
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--tls-hostname	The hostname used to verify the server's certificate. It can either be the Common Name or a…	v
o	--format	Apache style log formatting. Your log must produce valid JSON that Elasticsearch can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--request-max-entries	Maximum number of logs to append to a batch, if non-zero. Defaults to 10k	v
o	--request-max-bytes	Maximum size of log batch, if non-zero. Defaults to 100MB	v
@	logging ftp
s	create	Create an FTP logging endpoint on a Fastly service version
s	delete	Delete an FTP logging endpoint on a Fastly service version
s	describe	Show detailed information about an FTP logging endpoint on a Fastly service version
s	list	List FTP endpoints on a Fastly service version
s	update	Update an FTP logging endpoint on a Fastly service version
@	logging ftp create
o	--name	The name of the FTP logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--address	An hostname or IPv4 address	v
o	--user	The username for the server (can be anonymous)	v
o	--password	The password for the server (for anonymous use an email address)	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--port	The port number	v
o	--path	The path to upload log files to. If the path ends in / then it is treated as a directory	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging ftp delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the FTP logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging ftp describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the FTP logging object	v
@	logging ftp list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging ftp update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the FTP logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the FTP logging object	v
o	--address	An hostname or IPv4 address	v
o	--port	The port number	v
o	--username	The username for the server (can be anonymous)	v
o	--password	The password for the server (for anonymous use an email address)	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--path	The path to upload log files to. If the path ends in / then it is treated as a directory	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging gcs
s	create	Create a GCS logging endpoint on a Fastly service version
s	delete	Delete a GCS logging endpoint on a Fastly service version
s	describe	Show detailed information about a GCS logging endpoint on a Fastly service version
s	list	List GCS endpoints on a Fastly service version
s	update	Update a GCS logging endpoint on a Fastly service version
@	logging gcs create
o	--name	The name of the GCS logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--user	Your GCS service account email address. The client_email field in your service account…	v
o	--bucket	The bucket of the GCS bucket	v
o	--secret-key	Your GCS account secret key. The private_key field in your service account authentication JSON	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--path	The path to upload logs to (default '/')	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging gcs delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the GCS logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging gcs describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the GCS logging object	v
@	logging gcs list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging gcs update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the GCS logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the GCS logging object	v
o	--bucket	The bucket of the GCS bucket	v
o	--user	Your GCS service account email address. The client_email field in your service account…	v
o	--secret-key	Your GCS account secret key. The private_key field in your service account authentication JSON	v
o	--path	The path to upload logs to (default '/')	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging googlepubsub
s	create	Create a Google Cloud Pub/Sub logging endpoint on a Fastly service version
s	delete	Delete a Google Cloud Pub/Sub logging endpoint on a Fastly service version
s	describe	Show detailed information about a Google Cloud Pub/Sub logging endpoint on a Fastly service version
s	list	List Google Cloud Pub/Sub endpoints on a Fastly service version
s	update	Update a Google Cloud Pub/Sub logging endpoint on a Fastly service version
@	logging googlepubsub create
o	--name	The name of the Google Cloud Pub/Sub logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--user	Your Google Cloud Platform service account email address. The client_email field in your service…	v
o	--secret-key	Your Google Cloud Platform account secret key. The private_key field in your service account…	v
o	--topic	The Google Cloud Pub/Sub topic to which logs will be published	v
o	--project-id	The ID of your Google Cloud Platform project	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
@	logging googlepubsub delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Google Cloud Pub/Sub logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging googlepubsub describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Google Cloud Pub/Sub logging object	v
@	logging googlepubsub list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging googlepubsub update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Google Cloud Pub/Sub logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Google Cloud Pub/Sub logging object	v
o	--user	Your Google Cloud Platform service account email address. The client_email field in your service…	v
o	--secret-key	Your Google Cloud Platform account secret key. The private_key field in your service account…	v
o	--topic	The Google Cloud Pub/Sub topic to which logs will be published	v
o	--project-id	The ID of your Google Cloud Platform project	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
@	logging heroku
s	create	Create a Heroku logging endpoint on a Fastly service version
s	delete	Delete a Heroku logging endpoint on a Fastly service version
s	describe	Show detailed information about a Heroku logging endpoint on a Fastly service version
s	list	List Heroku endpoints on a Fastly service version
s	update	Update a Heroku logging endpoint on a Fastly service version
@	logging heroku create
o	--name	The name of the Heroku logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--url	The url to stream logs to	v
o	--auth-token	The token to use for authentication (https://devcenter.heroku.com/articles/add-on-partner-log-integ…	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging heroku delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Heroku logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging heroku describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Heroku logging object	v
@	logging heroku list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging heroku update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Heroku logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Heroku logging object	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--url	The url to stream logs to	v
o	--auth-token	The token to use for authentication (https://devcenter.heroku.com/articles/add-on-partner-log-integ…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging honeycomb
s	create	Create a Honeycomb logging endpoint on a Fastly service version
s	delete	Delete a Honeycomb logging endpoint on a Fastly service version
s	describe	Show detailed information about a Honeycomb logging endpoint on a Fastly service version
s	list	List Honeycomb endpoints on a Fastly service version
s	update	Update a Honeycomb logging endpoint on a Fastly service version
@	logging honeycomb create
o	--name	The name of the Honeycomb logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--dataset	The Honeycomb Dataset you want to log to	v
o	--auth-token	The Write Key from the Account page of your Honeycomb account	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--format	Apache style log formatting. Your log must produce valid JSON that Honeycomb can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging honeycomb delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Honeycomb logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging honeycomb describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Honeycomb logging object	v
@	logging honeycomb list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging honeycomb update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Honeycomb logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Honeycomb logging object	v
o	--format	Apache style log formatting. Your log must produce valid JSON that Honeycomb can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--dataset	The Honeycomb Dataset you want to log to	v
o	--auth-token	The Write Key from the Account page of your Honeycomb account	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging https
s	create	Create an HTTPS logging endpoint on a Fastly service version
s	delete	Delete an HTTPS logging endpoint on a Fastly service version
s	describe	Show detailed information about an HTTPS logging endpoint on a Fastly service version
s	list	List HTTPS endpoints on a Fastly service version
s	update	Update an HTTPS logging endpoint on a Fastly service version
@	logging https create
o	--name	The name of the HTTPS logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--url	URL that log data will be sent to. Must use the https protocol	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--content-type	Content type of the header sent with the request	v
o	--header-name	Name of the custom header sent with the request	v
o	--header-value	Value of the custom header sent with the request	v
o	--method	HTTP method used for request. Can be POST or PUT. Defaults to POST if not specified	v
o	--json-format	Enforces valid JSON formatting for log entries. Can be disabled 0, array of json (wraps JSON log…	v
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--tls-hostname	The hostname used to verify the server's certificate. It can either be the Common Name or a…	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--format	Apache style log formatting. Your log must produce valid JSON that HTTPS can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--request-max-entries	Maximum number of logs to append to a batch, if non-zero. Defaults to 10k	v
o	--request-max-bytes	Maximum size of log batch, if non-zero. Defaults to 100MB	v
@	logging https delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the HTTPS logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging https describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the HTTPS logging object	v
@	logging https list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging https update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the HTTPS logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the HTTPS logging object	v
o	--url	URL that log data will be sent to. Must use the https protocol	v
o	--content-type	Content type of the header sent with the request	v
o	--header-name	Name of the custom header sent with the request	v
o	--header-value	Value of the custom header sent with the request	v
o	--method	HTTP method used for request. Can be POST or PUT. Defaults to POST if not specified	v
o	--json-format	Enforces valid JSON formatting for log entries. Can be disabled 0, array of json (wraps JSON log…	v
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--tls-hostname	The hostname used to verify the server's certificate. It can either be the Common Name or a…	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--format	Apache style log formatting. Your log must produce valid JSON that HTTPS can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--request-max-entries	Maximum number of logs to append to a batch, if non-zero. Defaults to 10k	v
o	--request-max-bytes	Maximum size of log batch, if non-zero. Defaults to 100MB	v
@	logging kafka
s	create	Create a Kafka logging endpoint on a Fastly service version
s	delete	Delete a Kafka logging endpoint on a Fastly service version
s	describe	Show detailed information about a Kafka logging endpoint on a Fastly service version
s	list	List Kafka endpoints on a Fastly service version
s	update	Update a Kafka logging endpoint on a Fastly service version
@	logging kafka create
o	--name	The name of the Kafka logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--topic	The Kafka topic to send logs to	v
o	--brokers	A comma-separated list of IP addresses or hostnames of Kafka brokers	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--compression-codec	The codec used for compression of your logs. One of: gzip, snappy, lz4	v
o	--required-acks	The Number of acknowledgements a leader must receive before a write is considered successful. One…	v
o	--use-tls	Whether to use TLS for secure logging. Can be either true or false	
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--tls-hostname	The hostname used to verify the server's certificate. It can either be the Common Name or a…	v
o	--format	Apache style log formatting. Your log must produce valid JSON that Kafka can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--parse-log-keyvals	Parse key-value pairs within the log format	
o	--max-batch-size	The maximum size of the log batch in bytes	v
o	--use-sasl	Enable SASL authentication. Requires --auth-method, --username, and --password to be specified	
o	--auth-method	SASL authentication method. Valid values are: plain, scram-sha-256, scram-sha-512	v
o	--username	SASL authentication username. Required if --auth-method is specified	v
o	--password	SASL authentication password. Required if --auth-method is specified	v
@	logging kafka delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Kafka logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging kafka describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Kafka logging object	v
@	logging kafka list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging kafka update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Kafka logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Kafka logging object	v
o	--topic	The Kafka topic to send logs to	v
o	--brokers	A comma-separated list of IP addresses or hostnames of Kafka brokers	v
o	--compression-codec	The codec used for compression of your logs. One of: gzip, snappy, lz4	v
o	--required-acks	The Number of acknowledgements a leader must receive before a write is considered successful. One…	v
o	--use-tls	Whether to use TLS for secure logging. Can be either true or false	
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--tls-hostname	The hostname used to verify the server's certificate. It can either be the Common Name or a…	v
o	--format	Apache style log formatting. Your log must produce valid JSON that Kafka can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--parse-log-keyvals	Parse key-value pairs within the log format	
o	--max-batch-size	The maximum size of the log batch in bytes	v
o	--use-sasl	Enable SASL authentication. Requires --auth-method, --username, and --password to be specified	
o	--auth-method	SASL authentication method. Valid values are: plain, scram-sha-256, scram-sha-512	v
o	--username	SASL authentication username. Required if --auth-method is specified	v
o	--password	SASL authentication password. Required if --auth-method is specified	v
@	logging kinesis
s	create	Create an Amazon Kinesis logging endpoint on a Fastly service version
s	delete	Delete a Kinesis logging endpoint on a Fastly service version
s	describe	Show detailed information about a Kinesis logging endpoint on a Fastly service version
s	list	List Kinesis endpoints on a Fastly service version
s	update	Update a Kinesis logging endpoint on a Fastly service version
@	logging kinesis create
o	--name	The name of the Kinesis logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--stream-name	The Amazon Kinesis stream to send logs to	v
o	--region	The AWS region where the Kinesis stream exists	v
o	--access-key	The access key associated with the target Amazon Kinesis stream	v
o	--secret-key	The secret key associated with the target Amazon Kinesis stream	v
o	--iam-role	The IAM role ARN for logging	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging kinesis delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Kinesis logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging kinesis describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Kinesis logging object	v
@	logging kinesis list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging kinesis update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Kinesis logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Kinesis logging object	v
o	--stream-name	Your Kinesis stream name	v
o	--access-key	Your Kinesis account access key	v
o	--secret-key	Your Kinesis account secret key	v
o	--iam-role	The IAM role ARN for logging	v
o	--region	The AWS region where the Kinesis stream exists	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging logentries
s	create	Create a Logentries logging endpoint on a Fastly service version
s	delete	Delete a Logentries logging endpoint on a Fastly service version
s	describe	Show detailed information about a Logentries logging endpoint on a Fastly service version
s	list	List Logentries endpoints on a Fastly service version
s	update	Update a Logentries logging endpoint on a Fastly service version
@	logging logentries create
o	--name	The name of the Logentries logging object. Used as a primary key for API access	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--port	The port number	v
o	--use-tls	Whether to use TLS for secure logging. Can be either true or false	
o	--auth-token	Use token based authentication (https://logentries.com/doc/input-token/)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--region	The region to which to stream logs	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
@	logging logentries delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Logentries logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging logentries describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Logentries logging object	v
@	logging logentries list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging logentries update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Logentries logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Logentries logging object	v
o	--port	The port number	v
o	--use-tls	Whether to use TLS for secure logging. Can be either true or false	
o	--auth-token	Use token based authentication (https://logentries.com/doc/input-token/)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--region	The region to which to stream logs	v
@	logging loggly
s	create	Create a Loggly logging endpoint on a Fastly service version
s	delete	Delete a Loggly logging endpoint on a Fastly service version
s	describe	Show detailed information about a Loggly logging endpoint on a Fastly service version
s	list	List Loggly endpoints on a Fastly service version
s	update	Update a Loggly logging endpoint on a Fastly service version
@	logging loggly create
o	--name	The name of the Loggly logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--auth-token	The token to use for authentication (https://www.loggly.com/docs/customer-token-authentication-toke…	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging loggly delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Loggly logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging loggly describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Loggly logging object	v
@	logging loggly list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging loggly update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Loggly logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Loggly logging object	v
o	--auth-token	The token to use for authentication (https://www.loggly.com/docs/customer-token-authentication-toke…	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging logshuttle
s	create	Create a Logshuttle logging endpoint on a Fastly service version
s	delete	Delete a Logshuttle logging endpoint on a Fastly service version
s	describe	Show detailed information about a Logshuttle logging endpoint on a Fastly service version
s	list	List Logshuttle endpoints on a Fastly service version
s	update	Update a Logshuttle logging endpoint on a Fastly service version
@	logging logshuttle create
o	--name	The name of the Logshuttle logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--url	Your Log Shuttle endpoint url	v
o	--auth-token	The data authentication token associated with this endpoint	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging logshuttle delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Logshuttle logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging logshuttle describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Logshuttle logging object	v
@	logging logshuttle list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging logshuttle update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Logshuttle logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Logshuttle logging object	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--url	Your Log Shuttle endpoint url	v
o	--auth-token	The data authentication token associated with this endpoint	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging newrelic
s	create	Create an New Relic logging endpoint attached to the specified service version
s	delete	Delete the New Relic Logs logging object for a particular service and version
s	describe	Get the details of a New Relic Logs logging object for a particular service and version
s	list	List all of the New Relic Logs logging objects for a particular service and version
s	update	Update a New Relic Logs logging object for a particular service and version
@	logging newrelic create
o	--key	The Insert API key from the Account page of your New Relic account	v
o	--name	The name for the real-time logging configuration	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--format	A Fastly log format string. Must produce valid JSON that New Relic Logs can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint	v
o	--placement	Where in the generated VCL the logging call should be placed	v
o	--region	The region to which to stream logs	v
o	--response-condition	The name of an existing condition in the configured endpoint	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging newrelic delete
o	--name	The name for the real-time logging configuration to delete	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging newrelic describe
o	--name	The name for the real-time logging configuration	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging newrelic list
o	--version	'latest', 'active', or the number of a specific version	v
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging newrelic update
o	--name	The name for the real-time logging configuration to update	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--format	A Fastly log format string. Must produce valid JSON that New Relic Logs can ingest	v
o	--format-version	The version of the custom logging format used for the configured endpoint	v
o	--key	The Insert API key from the Account page of your New Relic account	v
o	--new-name	The name for the real-time logging configuration	v
o	--placement	Where in the generated VCL the logging call should be placed	v
o	--region	The region to which to stream logs	v
o	--response-condition	The name of an existing condition in the configured endpoint	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging openstack
s	create	Create an OpenStack logging endpoint on a Fastly service version
s	delete	Delete an OpenStack logging endpoint on a Fastly service version
s	describe	Show detailed information about an OpenStack logging endpoint on a Fastly service version
s	list	List OpenStack logging endpoints on a Fastly service version
s	update	Update an OpenStack logging endpoint on a Fastly service version
@	logging openstack create
o	--name	The name of the OpenStack logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--bucket	The name of your OpenStack container	v
o	--access-key	Your OpenStack account access key	v
o	--user	The username for your OpenStack account	v
o	--url	Your OpenStack auth url	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--path	The path to upload logs to	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging openstack delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the OpenStack logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging openstack describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the OpenStack logging object	v
@	logging openstack list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging openstack update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the OpenStack logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the OpenStack logging object	v
o	--bucket	The name of the Openstack Space	v
o	--access-key	Your OpenStack account access key	v
o	--user	The username for your OpenStack account	v
o	--url	Your OpenStack auth url	v
o	--path	The path to upload logs to	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging papertrail
s	create	Create a Papertrail logging endpoint on a Fastly service version
s	delete	Delete a Papertrail logging endpoint on a Fastly service version
s	describe	Show detailed information about a Papertrail logging endpoint on a Fastly service version
s	list	List Papertrail endpoints on a Fastly service version
s	update	Update a Papertrail logging endpoint on a Fastly service version
@	logging papertrail create
o	--name	The name of the Papertrail logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--address	A hostname or IPv4 address	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--port	The port number	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--format	Apache style log formatting	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging papertrail delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Papertrail logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging papertrail describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Papertrail logging object	v
@	logging papertrail list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging papertrail update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Papertrail logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Papertrail logging object	v
o	--address	A hostname or IPv4 address	v
o	--port	The port number	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--format	Apache style log formatting	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging s3
s	create	Create an Amazon S3 logging endpoint on a Fastly service version
s	delete	Delete a S3 logging endpoint on a Fastly service version
s	describe	Show detailed information about a S3 logging endpoint on a Fastly service version
s	list	List S3 endpoints on a Fastly service version
s	update	Update a S3 logging endpoint on a Fastly service version
@	logging s3 create
o	--name	The name of the S3 logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--bucket	Your S3 bucket name	v
o	--access-key	Your S3 account access key	v
o	--secret-key	Your S3 account secret key	v
o	--iam-role	The IAM role ARN for logging	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--domain	The domain of the S3 endpoint	v
o	--path	The path to upload logs to	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--redundancy	The S3 redundancy level. Can be either standard or reduced_redundancy	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--server-side-encryption	Set to enable S3 Server Side Encryption. Can be either AES256 or aws:kms	v
o	--server-side-encryption-kms-key-id	Server-side KMS Key ID. Must be set if server-side-encryption is set to aws:kms	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging s3 delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the S3 logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging s3 describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the S3 logging object	v
@	logging s3 list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging s3 update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the S3 logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the S3 logging object	v
o	--bucket	Your S3 bucket name	v
o	--access-key	Your S3 account access key	v
o	--secret-key	Your S3 account secret key	v
o	--iam-role	The IAM role ARN for logging	v
o	--domain	The domain of the S3 endpoint	v
o	--path	The path to upload logs to	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--redundancy	The S3 redundancy level. Can be either standard or reduced_redundancy	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--server-side-encryption	Set to enable S3 Server Side Encryption. Can be either AES256 or aws:kms	v
o	--server-side-encryption-kms-key-id	Server-side KMS Key ID. Must be set if server-side-encryption is set to aws:kms	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging scalyr
s	create	Create a Scalyr logging endpoint on a Fastly service version
s	delete	Delete a Scalyr logging endpoint on a Fastly service version
s	describe	Show detailed information about a Scalyr logging endpoint on a Fastly service version
s	list	List Scalyr endpoints on a Fastly service version
s	update	Update a Scalyr logging endpoint on a Fastly service version
@	logging scalyr create
o	--name	The name of the Scalyr logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--auth-token	The token to use for authentication (https://www.scalyr.com/keys)	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--region	The region that log data will be sent to. One of US or EU. Defaults to US if undefined	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging scalyr delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Scalyr logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging scalyr describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Scalyr logging object	v
@	logging scalyr list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging scalyr update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Scalyr logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Scalyr logging object	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--auth-token	The token to use for authentication (https://www.scalyr.com/keys)	v
o	--region	The region that log data will be sent to. One of US or EU. Defaults to US if undefined	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging sftp
s	create	Create an SFTP logging endpoint on a Fastly service version
s	delete	Delete an SFTP logging endpoint on a Fastly service version
s	describe	Show detailed information about an SFTP logging endpoint on a Fastly service version
s	list	List SFTP endpoints on a Fastly service version
s	update	Update an SFTP logging endpoint on a Fastly service version
@	logging sftp create
o	--name	The name of the SFTP logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--address	The hostname or IPv4 address	v
o	--user	The username for the server	v
o	--ssh-known-hosts	A list of host keys for all hosts we can connect to over SFTP	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--port	The port number	v
o	--password	The password for the server. If both password and secret_key are passed, secret_key will be used…	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--secret-key	The SSH private key for the server. If both password and secret_key are passed, secret_key will be…	v
o	--path	The path to upload logs to. The directory must exist on the SFTP server before logs can be saved…	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging sftp delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the SFTP logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging sftp describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the SFTP logging object	v
@	logging sftp list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging sftp update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the SFTP logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the SFTP logging object	v
o	--address	The hostname or IPv4 address	v
o	--port	The port number	v
o	--public-key	A PGP public key that Fastly will use to encrypt your log files before writing them to disk	v
o	--secret-key	The SSH private key for the server. If both password and secret_key are passed, secret_key will be…	v
o	--ssh-known-hosts	A list of host keys for all hosts we can connect to over SFTP	v
o	--user	The username for the server	v
o	--password	The password for the server. If both password and secret_key are passed, secret_key will be used…	v
o	--path	The path to upload logs to. The directory must exist on the SFTP server before logs can be saved…	v
o	--period	How frequently log files are finalized so they can be available for reading (in seconds, default…	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--gzip-level	What level of GZIP encoding to have when dumping logs (default 0, no compression)	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--timestamp-format	Strftime specified timestamp formatting (default "%Y-%m-%dT%H:%M:%S.000")	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--compression-codec	The codec used for compression of your logs. Valid values are zstd, snappy, and gzip. If the…	v
@	logging splunk
s	create	Create a Splunk logging endpoint on a Fastly service version
s	delete	Delete a Splunk logging endpoint on a Fastly service version
s	describe	Show detailed information about a Splunk logging endpoint on a Fastly service version
s	list	List Splunk endpoints on a Fastly service version
s	update	Update a Splunk logging endpoint on a Fastly service version
@	logging splunk create
o	--name	The name of the Splunk logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--url	The URL to POST to	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-hostname	The hostname used to verify the server's certificate. It can either be the Common Name or a…	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--auth-token	A Splunk token for use in posting logs over HTTP to your collector	v
@	logging splunk delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Splunk logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging splunk describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Splunk logging object	v
@	logging splunk list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging splunk update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Splunk logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Splunk logging object	v
o	--url	The URL to POST to	v
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-hostname	The hostname used to verify the server's certificate. It can either be the Common Name or a…	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
o	--auth-token		v
@	logging sumologic
s	create	Create a Sumologic logging endpoint on a Fastly service version
s	delete	Delete a Sumologic logging endpoint on a Fastly service version
s	describe	Show detailed information about a Sumologic logging endpoint on a Fastly service version
s	list	List Sumologic endpoints on a Fastly service version
s	update	Update a Sumologic logging endpoint on a Fastly service version
@	logging sumologic create
o	--name	The name of the Sumologic logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--url	The URL to POST to	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging sumologic delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Sumologic logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging sumologic describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Sumologic logging object	v
@	logging sumologic list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging sumologic update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Sumologic logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Sumologic logging object	v
o	--url	The URL to POST to	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2 (the…	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging syslog
s	create	Create a Syslog logging endpoint on a Fastly service version
s	delete	Delete a Syslog logging endpoint on a Fastly service version
s	describe	Show detailed information about a Syslog logging endpoint on a Fastly service version
s	list	List Syslog endpoints on a Fastly service version
s	update	Update a Syslog logging endpoint on a Fastly service version
@	logging syslog create
o	--name	The name of the Syslog logging object. Used as a primary key for API access	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--address	A hostname or IPv4 address	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--port	The port number	v
o	--use-tls	Whether to use TLS for secure logging. Can be either true or false	
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-hostname	Used during the TLS handshake to validate the certificate	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--auth-token	Whether to prepend each message with a specific token	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	logging syslog delete
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Syslog logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	logging syslog describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--name	The name of the Syslog logging object	v
@	logging syslog list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	logging syslog update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--name	The name of the Syslog logging object	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--new-name	New name of the Syslog logging object	v
o	--address	A hostname or IPv4 address	v
o	--port	The port number	v
o	--use-tls	Whether to use TLS for secure logging. Can be either true or false	
o	--tls-ca-cert	A secure certificate to authenticate the server with. Must be in PEM format	v
o	--tls-hostname	Used during the TLS handshake to validate the certificate	v
o	--tls-client-cert	The client certificate used to make authenticated requests. Must be in PEM format	v
o	--tls-client-key	The client private key used to make authenticated requests. Must be in PEM format	v
o	--auth-token	Whether to prepend each message with a specific token	v
o	--format	Apache style log formatting	v
o	--format-version	The version of the custom logging format used for the configured endpoint. Can be either 2…	v
o	--message-type	How the message should be formatted. One of: classic (default), loggly, logplex or blank	v
o	--response-condition	The name of an existing condition in the configured endpoint, or leave blank to always execute	v
o	--placement	Where in the generated VCL the logging call should be placed, overriding any format_version…	v
@	pops
@	profile
s	create	Create user profile
s	delete	Delete user profile
s	list	List user profiles
s	switch	Switch user profile
s	token	Print access token
s	update	Update user profile
@	profile create
@	profile delete
@	profile list
@	profile switch
@	profile token
o	--name	Print access token for the named profile	v
@	profile update
@	purge
o	--all	Purge everything from a service	
o	--file	Purge a service of a newline delimited list of Surrogate Keys	v
o	--key	Purge a service of objects tagged with a Surrogate Key	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--soft	A 'soft' purge marks affected objects as stale rather than making them inaccessible	
o	--url	Purge an individual URL	v
@	service
s	create	Create a Fastly service
s	delete	Delete a Fastly service
s	describe	Show detailed information about a Fastly service
s	list	List Fastly services
s	search	Search for a Fastly service by name
s	update	Update a Fastly service
@	service create
o	--name	Service name	v
o	--type	Service type. Can be one of "wasm" or "vcl", defaults to "vcl"	v
o	--comment	Human-readable comment	v
@	service delete
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--force	Force deletion of an active service	
@	service describe
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	service list
o	--direction	Direction in which to sort results	v
o	--json	Render output as JSON	
o	--page	Page number of data set to fetch	v
o	--per-page	Number of records per page	v
o	--sort	Field on which to sort	v
@	service search
o	--name	Service name	v
@	service update
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--name	Service name	v
o	--comment	Human-readable comment	v
@	service-version
s	activate	Activate a Fastly service version
s	clone	Clone a Fastly service version
s	deactivate	Deactivate a Fastly service version
s	list	List Fastly service versions
s	lock	Lock a Fastly service version
s	update	Update a Fastly service version
@	service-version activate
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
@	service-version clone
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	service-version deactivate
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	service-version list
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	service-version lock
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
@	service-version update
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--comment	Human-readable comment	v
@	stats
s	historical	View historical stats for a Fastly service
s	realtime	View realtime stats for a Fastly service
s	regions	List stats regions
@	stats historical
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--from	From time, accepted formats at https://fastly.dev/reference/api/metrics-stats/historical-stats	v
o	--to	To time	v
o	--by	Aggregation period (minute/hour/day)	v
o	--region	Filter by region ('stats regions' to list)	v
o	--format	Output format (json)	v
@	stats realtime
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--format	Output format (json)	v
@	stats regions
@	update
@	user
s	create	Create a user of the Fastly API and web interface
s	delete	Delete a user of the Fastly API and web interface
s	describe	Get a specific user of the Fastly API and web interface
s	list	List all users from a specified customer id
s	update	Update a user of the Fastly API and web interface
@	user create
o	--login	The login associated with the user (typically, an email address)	v
o	--name	The real life name of the user	v
o	--role	The permissions role assigned to the user. Can be user, billing, engineer, or superuser	v
@	user delete
o	--id	Alphanumeric string identifying the user	v
@	user describe
o	--current	Get the logged in user	
o	--id	Alphanumeric string identifying the user	v
o	--json	Render output as JSON	
@	user list
o	--customer-id	Alphanumeric string identifying the customer (falls back to FASTLY_CUSTOMER_ID)	v
o	--json	Render output as JSON	
@	user update
o	--id	Alphanumeric string identifying the user	v
o	--login	The login associated with the user (typically, an email address)	v
o	--name	The real life name of the user	v
o	--password-reset	Requests a password reset for the specified user	
o	--role	The permissions role assigned to the user. Can be user, billing, engineer, or superuser	v
@	vcl
s	custom	Manipulate Fastly service version custom VCL
s	snippet	Manipulate Fastly VCL snippets (blocks of VCL logic inserted into your service's configuration…
@	vcl custom
s	create	Upload a VCL for a particular service and version
s	delete	Delete the uploaded VCL for a particular service and version
s	describe	Get the uploaded VCL for a particular service and version
s	list	List the uploaded VCLs for a particular service and version
s	update	Update the uploaded VCL for a particular service and version
@	vcl custom create
o	--content	VCL passed as file path or content, e.g. $(< main.vcl)	v
o	--name	The name of the VCL	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--main	Whether the VCL is the 'main' entrypoint	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	vcl custom delete
o	--name	The name of the VCL to delete	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	vcl custom describe
o	--name	The name of the VCL	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	vcl custom list
o	--version	'latest', 'active', or the number of a specific version	v
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	vcl custom update
o	--name	The name of the VCL to update	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--new-name	New name for the VCL	v
o	--content	VCL passed as file path or content, e.g. $(< main.vcl)	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	vcl snippet
s	create	Create a snippet for a particular service and version
s	delete	Delete a specific snippet for a particular service and version
s	describe	Get the uploaded VCL snippet for a particular service and version
s	list	List the uploaded VCL snippets for a particular service and version
s	update	Update a VCL snippet for a particular service and version
@	vcl snippet create
o	--content	VCL snippet passed as file path or content, e.g. $(< snippet.vcl)	v
o	--name	The name of the VCL snippet	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--type	The location in generated VCL where the snippet should be placed	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--dynamic	Whether the VCL snippet is dynamic or versioned	
o	--priority	Priority determines execution order. Lower numbers execute first	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	vcl snippet delete
o	--name	The name of the VCL snippet to delete	v
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	vcl snippet describe
o	--version	'latest', 'active', or the number of a specific version	v
o	--dynamic	Whether the VCL snippet is dynamic or versioned	
o	--json	Render output as JSON	
o	--name	The name of the VCL snippet	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--snippet-id	Alphanumeric string identifying a VCL Snippet	v
@	vcl snippet list
o	--version	'latest', 'active', or the number of a specific version	v
o	--json	Render output as JSON	
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
@	vcl snippet update
o	--version	'latest', 'active', or the number of a specific version	v
o	--autoclone	If the selected service version is not editable, clone it and use the clone	
o	--content	VCL snippet passed as file path or content, e.g. $(< snippet.vcl)	v
o	--dynamic	Whether the VCL snippet is dynamic or versioned	
o	--name	The name of the VCL snippet to update	v
o	--new-name	New name for the VCL snippet	v
o	--priority	Priority determines execution order. Lower numbers execute first	v
o	--service-id	Service ID (falls back to FASTLY_SERVICE_ID, then fastly.toml)	v
o	--service-name	The name of the service	v
o	--snippet-id	Alphanumeric string identifying a VCL Snippet	v
o	--type	The location in generated VCL where the snippet should be placed	v
@	version
@	whoami
