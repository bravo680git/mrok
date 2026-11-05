@	
s	read	Reads data from Vault at the given path
s	write	Writes data from Vault at the given path
s	delete	Deletes secrets and configuration from Vault at the given path
s	list	Lists data from Vault at the given path
s	login	Authenticates users or machines to Vault using the provided arguments
s	agent	This command starts a Vault agent that can perform automatic authentication in certain environments
s	server	This command starts a Vault server that responds to API requests. By default, Vault will start in…
s	status	Prints the current state of Vault including whether it is sealed and if HA mode is enabled. This…
s	unwrap	Unwraps a wrapped secret from Vault by the given token. The result is the same as the 'vault read'…
s	audit	This command groups subcommands for interacting with Vault's audit devices. Users can list…
s	debug	Probes a specific Vault server node for a specified period of time, recording information about…
s	kv	This command has subcommands for interacting with Vault's key-value store. Here are some simple…
s	lease	This command groups subcommands for interacting with leases. Users can revoke or renew leases
s	monitor	Stream log messages of a Vault server. The monitor command lets you listen for log levels that may…
s	namespace	This command groups subcommands for interacting with Vault namespaces. These subcommands operate…
s	operator	This command groups subcommands for operators interacting with Vault. Most users will not need to…
s	path-help	Retrieves API help for paths. All endpoints in Vault provide built-in help in markdown format…
s	plugin	This command groups subcommands for interacting with Vault's plugins and the plugin catalog. The…
s	policy	
s	print	This command groups subcommands for interacting with Vault's runtime values
s	secrets	This command groups subcommands for interacting with Vault's secrets engines. Each secret engine…
s	ssh	Establishes an SSH connection with the target machine
s	token	This command groups subcommands for interacting with tokens. Users can create, lookup, renew, and…
s	version-history	Prints the version history of the target Vault server
o	--help|-h	Show help for vault	V
@	read
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	read	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	read	1
v	secret/foo	
@	write
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-force|-f	Allow the operation to continue with no key=value pairs. This allows writing to keys that do not…	
a	2	1
=	write	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	write	1
v	secret/foo	
#	write	2
v	bar=buz	
v	bar=@buz.json	
@	delete
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	delete	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	delete	1
v	secret/foo	
@	list
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	list	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	list	1
v	secret/foo	
@	login
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-method	Type of authentication to use such as 'userpass' or 'ldap'. Note this corresponds to the TYPE, not…	v=
o	-no-print	Do not display the token. The token will be still be stored to the configured token helper. The…	v=
o	-no-store	Do not persist the token to the token helper (usually the local filesystem) after authentication…	v=
o	-path	Remote path in Vault where the auth method is enabled. This defaults to the TYPE of method (e.g…	v=
o	-token-only	Output only the token with no verification. This flag is a shortcut for '-field=token -no-store'…	v=
a	1	0
=	login	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	login	-method
v	userpass	
v	ldap	
v	token	
=	login	-no-print
v	false	
v	true	
=	login	-no-store
v	false	
v	true	
=	login	-path
v	userpass/	
=	login	-token-only
v	false	
v	true	
#	login	1
v	secret/foo	
@	agent
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-config	Path to a configuration file. This configuration file should contain only agent directives	v=
o	-exit-after-auth	If set to true, the agent will exit with code 0 after a single successful auth, where success…	v=
o	-log-level	Log verbosity level. Supported values (in order of detail) are 'trace', 'debug', 'info', 'warn'…	v=
=	agent	-config
t	filepaths
=	agent	-exit-after-auth
v	false	
v	true	
=	agent	-log-level
v	trace	
v	debug	
v	info	
v	warn	
v	err	
@	server
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-config	Path to a configuration file or directory of configuration files. This flag can be specified…	v=
o	-exit-on-core-shutdown	Exit the vault server if the vault core is shutdown. The default is false	v=
o	-log-format	Log format. Supported values are 'standard' and 'json'. The default is (not set)	v=
o	-log-level	Log verbosity level. Supported values (in order of detail) are 'trace', 'debug', 'info', 'warn'…	v=
o	-recovery	Enable recovery mode. In this mode, Vault is used to perform recovery actions.Using a recovery…	v=
o	-dev	Enable development mode. In this mode, Vault runs in-memory and starts unsealed. As the name…	v=
o	-dev-listen-address	Address to bind to in 'dev' mode. The default is 127.0.0.1:8200. This can also be specified via…	v=
o	-dev-no-store-token	Do not persist the dev root token to the token helper (usually the local filesystem) for use in…	v=
o	-dev-root-token-id	Initial root token. This only applies when running in 'dev' mode. This can also be specified via…	v=
=	server	-config
t	filepaths
=	server	-exit-on-core-shutdown
v	false	
v	true	
=	server	-log-format
v	standard	
v	json	
=	server	-log-level
v	trace	
v	debug	
v	info	
v	warn	
v	err	
=	server	-recovery
v	false	
v	true	
=	server	-dev
v	false	
v	true	
=	server	-dev-listen-address
v	127.0.0.1:8200	
=	server	-dev-no-store-token
v	false	
v	true	
@	status
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
=	status	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	unwrap
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	unwrap	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	audit
s	list	Lists the enabled audit devices in the Vault server. The output lists the enabled audit devices…
s	disable	Disables an audit device. Once an audit device is disabled, no future audit logs are dispatched to…
s	enable	Enables an audit device at a given path
@	audit list
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-detailed	Print detailed information such as options and replication status about each auth device. The…	v=
=	audit list	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	audit list	-detailed
v	false	
v	true	
@	audit disable
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	1	0
@	audit enable
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	2	1
#	audit enable	1
v	file	
#	audit enable	2
v	file_path=/var/log/audit.log	
@	debug
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-compress	Toggles whether to compress output package The default is true	v=
o	-duration	Duration to run the command. The default is 2m0s	v=
o	-interval	The polling interval at which to collect profiling data and server state. The default is 30s	v=
o	-metrics-interval	The polling interval at which to collect metrics data. The default is 10s	v=
o	-output	Specifies the output path for the debug package	v=
o	-target	Target to capture, defaulting to all if none specified. This can be specified multiple times to…	v=
=	debug	-compress
v	true	
v	true	
=	debug	-duration
v	2m0s	
=	debug	-interval
v	30s	
=	debug	-metrics-interval
v	10s	
=	debug	-target
v	config	
v	host	
v	metrics	
v	pprof	
v	replication-status	
v	server-stauts	
v	log	
@	kv
s	delete	Deletes the data for the provided version and path in the key-value store. The versioned data will…
s	destroy	Permanently removes the specified versions' data from the key-value store. If no key exists at the…
s	enable-versioning	This command turns on versioning for the backend at the provided path
s	get	Retrieves the value from Vault's key-value store at the given key name. If no key exists with that…
s	list	Lists data from Vault's key-value store at the given path
s	metadata	This command has subcommands for interacting with the metadata endpoint in Vault's key-value…
s	patch	Writes the data to the given path in the key-value store. The data can be of any type
s	put	Writes the data to the given path in the key-value store. The data can be of any type
s	rollback	Restores a given previous version to the current version at the given path. The value is written…
s	undelete	Undeletes the data for the provided version and path in the key-value store. This restores the…
o	--help|-h	Display help	
@	kv delete
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-versions	Specifies the version numbers	v=
a	1	0
=	kv delete	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	kv delete	-versions
v	false	
v	true	
#	kv delete	1
v	secret/foo	
@	kv destroy
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-versions	Specifies the version numbers	v=
a	1	0
=	kv destroy	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	kv destroy	-versions
v	false	
v	true	
#	kv destroy	1
v	secret/foo	
@	kv enable-versioning
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	kv enable-versioning	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	kv enable-versioning	1
v	secret	
@	kv get
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	kv get	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	kv get	1
v	secret/foo	
@	kv list
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-versions	Specifies the version numbers	v=
a	1	0
=	kv list	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	kv list	-versions
v	false	
v	true	
#	kv list	1
v	secret/foo	
@	kv metadata
s	delete	Deletes all versions and metadata for the provided key
s	get	Retrieves the metadata from Vault's key-value store at the given key name. If no key exists with…
s	patch	This command can be used to create a blank key in the key-value store or to update key…
s	put	This command can be used to create a blank key in the key-value store or to update key…
o	--help|-h	Display help	
@	kv metadata delete
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	1	0
#	kv metadata delete	1
v	secret/foo	
@	kv metadata get
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	kv metadata get	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	kv metadata get	1
v	secret	
@	kv metadata patch
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-cas-required	If true the key will require the cas parameter to be set on all write requests. If false, the…	v=
o	-custom-metadata	Specifies arbitrary version-agnostic key=value metadata meant to describe a secret. This can be…	v=
o	-delete-version-after	Specifies the length of time before a version is deleted. If not set, the backend's configured…	v=
o	-max-versions	The number of versions to keep. If not set, the backend’s configured max version is used. The…	v=
a	1	0
=	kv metadata patch	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	kv metadata patch	-delete-version-after
v	30s	
v	3h25m19s	
=	kv metadata patch	-max-versions
v	-1	
#	kv metadata patch	1
v	secret	
@	kv metadata put
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-cas-required	If true the key will require the cas parameter to be set on all write requests. If false, the…	v=
o	-custom-metadata	Specifies arbitrary version-agnostic key=value metadata meant to describe a secret. This can be…	v=
o	-delete-version-after	Specifies the length of time before a version is deleted. If not set, the backend's configured…	v=
o	-max-versions	The number of versions to keep. If not set, the backend’s configured max version is used. The…	v=
a	1	0
=	kv metadata put	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	kv metadata put	-delete-version-after
v	30s	
v	3h25m19s	
=	kv metadata put	-max-versions
v	-1	
#	kv metadata put	1
v	secret	
@	kv patch
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-cas	Specifies to use a Check-And-Set operation. If set to 0 or not set, the patch will be allowed. If…	v=
o	-method	Specifies which method of patching to use. If set to 'patch', then an HTTP PATCH request will be…	v=
a	2	1
=	kv patch	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	kv patch	-cas
v	-1	
v	0	
v	1	
=	kv patch	-method
v	patch	
v	rw	
#	kv patch	1
v	secret	
#	kv patch	2
v	bar=buz	
v	bar=@buz.json	
@	kv put
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-cas	Specifies to use a Check-And-Set operation. If set to 0 or not set, the patch will be allowed. If…	v=
a	2	1
=	kv put	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	kv put	-cas
v	-1	
v	0	
v	1	
#	kv put	1
v	secret	
#	kv put	2
v	bar=buz	
v	bar=@buz.json	
@	kv rollback
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-versions	Specifies the version numbers	v=
a	1	0
=	kv rollback	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	kv rollback	-versions
v	false	
v	true	
#	kv rollback	1
v	secret	
@	kv undelete
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-versions	Specifies the version numbers	v=
a	1	0
=	kv undelete	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	kv undelete	-versions
v	false	
v	true	
#	kv undelete	1
v	secret	
@	lease
s	lookup	Lookup the lease information of a secret
s	renew	Renews the lease on a secret, extending the time that it can be used before it is revoked by Vault
s	revoke	Revokes secrets by their lease ID. This command can revoke a single secret or multiple secrets…
o	--help|-h	Display help	
@	lease lookup
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	lease lookup	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	lease lookup	1
v	database/creds/readonly/2f6a614c...	
@	lease renew
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-increment	Request a specific increment in seconds. Vault is not required to honor this request	v=
a	1	0
=	lease renew	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	lease renew	1
v	database/creds/readonly/2f6a614c...	
@	lease revoke
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-force	Delete the lease from Vault even if the secret engine revocation fails. This is meant for recovery…	v=
o	-prefix	Treat the ID as a prefix instead of an exact lease ID. This can revoke multiple leases…	v=
o	-sync	Force a synchronous operation; on failure it is up to the client to retry. The default is false	v=
a	1	0
=	lease revoke	-force
v	false	
v	true	
=	lease revoke	-prefix
v	false	
v	true	
=	lease revoke	-sync
v	false	
v	true	
#	lease revoke	1
v	database/creds/readonly/2f6a614c...	
@	monitor
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-log-level	If passed, the log level to monitor logs. Supported values(in order of detail) are 'trace'…	v=
=	monitor	-log-level
v	info	
v	trace	
v	debug	
v	warn	
v	error	
@	namespace
s	create	Create a child namespace. The namespace created will be relative to the namespace provided in…
s	delete	Delete an existing namespace. The namespace deleted will be relative to the namespace provided in…
s	list	Lists the enabled child namespaces
s	lock	Lock the current namespace, and all descendants
s	lookup	Get information about the namespace of the locally authenticated token
s	unlock	Unlock the current namespace, and all descendants, with unlock key
o	--help|-h	Display help	
@	namespace create
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	namespace create	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	namespace create	1
v	secret/foo	
@	namespace delete
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	1	0
#	namespace delete	1
v	secret/foo	
@	namespace list
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
=	namespace list	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	namespace lock
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	namespace lock	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	namespace lock	1
v	secret/foo	
@	namespace lookup
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	namespace lookup	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	namespace lookup	1
v	secret/foo	
@	namespace unlock
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	namespace unlock	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	namespace unlock	1
v	secret/foo	
@	operator
s	diagnose	This command troubleshoots Vault startup issues, such as TLS configuration or auto-unseal. It…
s	generate-root	Generates a new root token by combining a quorum of share holders. Must provide either '-otp' or…
s	init	Initializes a Vault server. Initialization is the process by which Vault's storage backend is…
s	key-status	Provides information about the active encryption key. Specifically, the current key term and the…
s	members	Provides the details of all the nodes in the cluster
s	migrate	This command starts a storage backend migration process to copy all data from one backend to…
s	raft	This command groups subcommands for operators interacting with the Vault raft storage backend…
s	rekey	Generates a new set of unseal keys. This can optionally change the total number of key shares or…
s	rotate	Rotates the underlying encryption key which is used to secure data written to the storage backend…
s	seal	Seals the Vault server. Sealing tells the Vault server to stop responding to any operations until…
s	step-down	Forces the Vault server at the given address to step down from active duty. While the affected…
s	unseal	Provide a portion of the root key to unseal a Vault server. Vault starts in a sealed state. It…
s	usage	List the client counts for the default reporting period
o	--help|-h	Display help	
@	operator diagnose
o	--help|-h	Display help	
o	-config	Path to a Vault configuration file or directory of configuration files. This flag can be specified…	v=
o	-debug	Dump all information collected by Diagnose	
o	-format	The output format	v=
o	-skip	Skip the health checks named as arguments	v=
=	operator diagnose	-config
t	filepaths
=	operator diagnose	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	operator diagnose	-skip
v	listen	
v	storage	
v	autounseal	
@	operator generate-root
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-cancel	Reset the root token generation progress. This will discard any submitted unseal keys or…	
o	-decode	The value to decode; setting this triggers a decode operation. If the value is '-' then read the…	v=
o	-dr-token	Set this flag to do generate root operations on DR Operational tokens. The default is false	
o	-generate-otp	Generate and print a high-entropy one-time-password (OTP) suitable for use with the '-init' flag…	
o	-init	Start a root token generation. This can only be done if there is not currently one in progress…	
o	-nonce	Nonce value provided at initialization. The same nonce value must be provided with each unseal key	v=
o	-otp	OTP code to use with '-decode' or '-init'	v=
o	-pgp-key	Path to a file on disk containing a binary or base64-encoded public PGP key. This can also be…	v=
o	-recovery-token	Set this flag to do generate root operations on Recovery Operational tokens. The default is false	
o	-status	Print the status of the current attempt without providing an unseal key. The default is false	
=	operator generate-root	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	operator generate-root	-decode
v	-	
=	operator generate-root	-pgp-key
t	filepaths
@	operator init
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-key-shares|-n	Number of key shares to split the generated root key into. This is the number of 'unseal keys' to…	v=
o	-key-threshold|-t	Number of key shares required to reconstruct the root key. This must be less than or equal to…	v=
o	-pgp-keys	Comma-separated list of paths to files on disk containing public PGP keys OR a comma-separated…	v=
o	-root-token-pgp-key	Path to a file on disk containing a binary or base64-encoded public PGP key. This can also be…	v=
o	-status	Print the current initialization status. An exit code of 0 means the Vault is already initialized…	
o	-stored-shares	DEPRECATED: This flag does nothing. It will be removed in Vault 1.3. The default is -1	v=
o	-consul-auto	Perform automatic service discovery using Consul in HA mode. When all nodes in a Vault HA cluster…	
o	-consul-service	Name of the service in Consul under which the Vault servers are registered. The default is vault	v=
=	operator init	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	operator init	-key-shares
v	5	
=	operator init	-key-threshold
v	5	
=	operator init	-pgp-keys
v	keybase:user1	
v	/path/to/pgp/key1,/path/to/pgp/key2	
t	filepaths
=	operator init	-root-token-pgp-key
v	keybase:user1	
v	/path/to/pgp/key	
t	filepaths
=	operator init	-stored-shares
v	-1	
=	operator init	-consul-service
v	vault	
@	operator key-status
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
=	operator key-status	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	operator members
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
=	operator members	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	operator migrate
o	-config	Path to a configuration file. This configuration file should contain only migrator directives	v=
o	-reset	Reset the migration lock. No migration will occur. The default is false	
o	-start	Only copy keys lexicographically at or after this value	v=
=	operator migrate	-config
t	filepaths
@	operator raft
s	autopilot	Raft auto pilot
s	join	Joins a node to the Raft cluster
s	list-peers	Returns the Raft peer set
s	remove-peer	Removes a node from the Raft cluster
s	snapshot	Restores and saves snapshots from the Raft cluster
@	operator raft autopilot
s	get-config	Returns the configuration of the autopilot subsystem under integrated storage
s	set-config	Modify the configuration of the autopilot subsystem under integrated storage
s	state	Displays the state of the raft cluster under integrated storage as seen by autopilot
@	operator raft autopilot get-config
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
=	operator raft autopilot get-config	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	operator raft autopilot set-config
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-cleanup-dead-servers	Clean up dead servers	v=
o	-dead-server-last-contact-threshold	Dead server last contact threshold	v=
o	-last-contact-threshold	Last contact threshold	v=
o	-max-trailing-logs	Max trailing logs	v=
o	-min-quorum	Min quorum	v=
o	-server-stabilization-time	Server stabilization time	v=
=	operator raft autopilot set-config	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	operator raft autopilot set-config	-cleanup-dead-servers
v	false	
v	true	
@	operator raft autopilot state
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
=	operator raft autopilot state	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	operator raft join
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-auto-join-port	An optional port used for addresses discovered via auto-join. The default is 8200	v=
o	-auto-join-scheme	An optional URI protocol scheme used for addresses discovered via auto-join. The default is https	v=
o	-leader-ca-cert	CA cert to use when verifying the Raft leader certificate	v=
o	-leader-client-cert	Client cert to use when authenticating with the Raft leader	v=
o	-leader-client-key	Client key to use when authenticating with the Raft leader	v=
o	-non-voter	(Enterprise-only) This flag is used to make the server not participate in the Raft quorum, and…	
o	-retry	Continuously retry joining the Raft cluster upon failures. The default is false	
a	1	0
=	operator raft join	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	operator raft join	-auto-join-port
v	8200	
=	operator raft join	-auto-join-scheme
v	https	
v	http	
=	operator raft join	-leader-ca-cert
v	@/path/to/leader_ca.crt	
t	filepaths
=	operator raft join	-leader-client-cert
v	@/path/to/client.crt	
t	filepaths
=	operator raft join	-leader-client-key
v	@/path/to/client.key	
t	filepaths
#	operator raft join	1
v	http://127.0.0.2:8200	
v	provider=aws region=eu-west-1 ...	
@	operator raft list-peers
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-dr-token	DR operation token used to authorize this request (if a DR secondary node)	v=
=	operator raft list-peers	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	operator raft remove-peer
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-dr-token	DR operation token used to authorize this request (if a DR secondary node)	v=
a	1	0
=	operator raft remove-peer	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	operator raft snapshot
s	restore	Installs the provided snapshot, returning the cluster to the state defined in it
s	save	Saves a snapshot of the current state of the Raft cluster into a file
@	operator raft snapshot restore
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-force	This bypasses checks ensuring the Autounseal or shamir keys are consistent with the snapshot data…	=
a	1	0
=	operator raft snapshot restore	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	operator raft snapshot restore	1
t	filepaths
@	operator raft snapshot save
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	operator raft snapshot save	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	operator raft snapshot save	1
t	filepaths
@	operator rekey
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-cancel	Reset the rekeying progress. This will discard any submitted unseal keys or configuration. The…	
o	-init	Initialize the rekeying operation. This can only be done if no rekeying operation is in progress…	
o	-key-shares|-n	Number of key shares to split the generated root key into. This is the number of 'unseal keys' to…	v=
o	-key-threshold|-t	Number of key shares required to reconstruct the root key. This must be less than or equal to…	v=
o	-nonce	Nonce value provided at initialization. The same nonce value must be provided with each unseal key	v=
o	-pgp-keys	Comma-separated list of paths to files on disk containing public PGP keys OR a comma-separated…	v=
o	-status	Print the status of the current attempt without providing an unseal key. The default is false	=
o	-target	Target for rekeying. 'recovery' only applies when HSM support is enabled. The default is barrier	v=
o	-verify	Indicates that the action (-status, -cancel, or providing a key share) will be affecting…	=
o	-backup	Store a backup of the current PGP encrypted unseal keys in Vault's core. The encrypted values can…	=
o	-backup-delete	Delete any stored backup unseal keys. The default is false	=
o	-backup-retries	Retrieve the backed-up unseal keys. This option is only available if the PGP keys were provided…	=
a	1	0
=	operator rekey	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	operator rekey	-key-shares
v	5	
=	operator rekey	-key-threshold
v	5	
=	operator rekey	-pgp-keys
v	keybase:user1	
v	/path/to/pgp/key1,/path/to/pgp/key2	
t	filepaths
=	operator rekey	-target
v	barrier	
#	operator rekey	1
v	-	
@	operator rotate
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
=	operator rotate	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	operator seal
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
@	operator step-down
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
@	operator unseal
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-migrate	Indicate that this share is provided with the intent that it is part of a seal migration process…	=
o	-reset	Discard any previously entered keys to the unseal process. The default is false	=
a	1	0
=	operator unseal	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	operator usage
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-end-time	End of report period. Defaults to end of last month	v=
o	-start-time	Start of report period. Defaults to 'default_reporting_period' before end time	v=
=	operator usage	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	path-help
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	path-help	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	path-help	1
v	secret/foo	
@	plugin
s	deregister	Deregister an existing plugin in the catalog. If the plugin does not exist, no action is taken…
s	info	Displays information about a plugin in the catalog with the given name. If the plugin does not…
s	list	Lists available plugins registered in the catalog. This does not list whether plugins are in use…
s	register	Registers a new plugin in the catalog. The plugin binary must exist in Vault's configured plugin…
s	reload	Reloads mounted plugins. Either the plugin name or the desired plugin mount(s) must be provided…
s	reload-status	Retrieves the status of a recent cluster plugin reload. The reload id must be provided
@	plugin deregister
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	2	0
#	plugin deregister	1
v	auth	
v	database	
v	secret	
@	plugin info
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
a	2	0
=	plugin info	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	plugin info	1
v	auth	
v	database	
v	secret	
@	plugin list
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	plugin list	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	plugin list	1
v	auth	
v	database	
v	secret	
@	plugin register
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-args	Arguments to pass to the plugin when starting. Separate multiple arguments with a comma	v=
o	-command	Command to spawn the plugin. This defaults to the name of the plugin if unspecified	v=
o	-sha256	SHA256 of the plugin binary. This is required for all plugins	v=
a	2	0
#	plugin register	1
v	auth	
v	database	
v	secret	
@	plugin reload
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-mounts	Array or comma-separated string mount paths of the plugin backends to reload	v=
o	-plugin	The name of the plugin to reload, as registered in the plugin catalog	v=
o	-scope	The scope of the reload, omitted for local, 'global', for replicated reloads	v=
@	plugin reload-status
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	1	0
@	policy
s	delete	Deletes the policy named NAME in the Vault server. Once the policy is deleted, all tokens…
s	fmt	Formats a local policy file to the policy specification. This command will overwrite the file at…
s	list	Lists the names of the policies that are installed on the Vault server
s	read	Prints the contents and metadata of the Vault policy named NAME. If the policy does not exist, an…
s	write	Uploads a policy with name NAME from the contents of a local file PATH or stdin. If PATH is '-'…
@	policy delete
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	1	0
@	policy fmt
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	1	0
#	policy fmt	1
t	filepaths
@	policy list
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
=	policy list	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	policy read
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	1	0
=	policy read	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	policy write
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	2	0
#	policy write	2
t	filepaths
@	print
s	token	Prints the value of the Vault token that will be used for commands, after taking into account the…
@	print token
@	secrets
s	disable	Disables a secrets engine at the given PATH. The argument corresponds to the enabled PATH of the…
s	enable	Enables a secrets engine. By default, secrets engines are enabled at the path corresponding to…
s	list	Lists the enabled secret engines on the Vault server. This command also outputs information about…
s	move	Moves an existing secrets engine to a new path. Any leases from the old secrets engine are…
s	tune	Tunes the configuration options for the secrets engine at the given PATH. The argument corresponds…
@	secrets disable
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	1	0
#	secrets disable	1
v	secret/foo	
@	secrets enable
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-allowed-managed-keys	Managed key name(s) that the mount in question is allowed to access. Note that multiple keys may…	v=
o	-allowed-response-headers	Comma-separated string or list of response header values that plugins will be allowed to set	v=
o	-audit-non-hmac-request-keys	Comma-separated string or list of keys that will not be HMAC'd by audit devices in the request…	v=
o	-audit-non-hmac-response-keys	Comma-separated string or list of keys that will not be HMAC'd by audit devices in the response…	v=
o	-default-lease-ttl	The default lease TTL for this secrets engine. If unspecified, this defaults to the Vault server's…	v=
o	-description	Human-friendly description for the purpose of this engine	v=
o	-external-entropy-access	Enable secrets engine to access Vault's external entropy source. The default is false	=
o	-force-no-cache	Force the secrets engine to disable caching. If unspecified, this defaults to the Vault server's…	=
o	-listing-visibility	Determines the visibility of the mount in the UI-specific listing endpoint	v=
o	-local	Mark the secrets engine as local-only. Local engines are not replicated or removed by replication…	=
o	-max-lease-ttl	The maximum lease TTL for this secrets engine. If unspecified, this defaults to the Vault server's…	v
o	-options	Key-value pair provided as key=value for the mount options. This can be specified multiple times	v=
o	-passthrough-request-headers	Comma-separated string or list of request header values that will be sent to the plugins	v=
o	-path	Place where the secrets engine will be accessible. This must be unique cross all secrets engines…	v=
o	-plugin-name	Name of the secrets engine plugin. This plugin name must already exist in Vault's plugin catalog	v=
o	-seal-wrap	Enable seal wrapping of critical values in the secrets engine. The default is false	
o	-version	Select the version of the engine to run. Not supported by all engines	v=
a	1	0
#	secrets enable	1
v	secret/foo	
@	secrets list
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-details	Print detailed information such as TTLs and replication status about each secrets engine. The…	=
=	secrets list	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	secrets move
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	2	0
@	secrets tune
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
a	1	0
#	secrets tune	1
v	secret/foo	
@	ssh
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-mode	Name of the authentication mode (ca, dynamic, otp)	v=
o	-mount-point	Mount point to the SSH secrets engine. The default is ssh/	v=
o	-no-exec	Print the generated credentials, but do not establish a connection. The default is false	=
o	-role	Name of the role to use to generate the key	v=
o	-strict-host-key-checking	Value to use for the SSH configuration option 'StrictHostKeyChecking'. The default is ask. This…	v=
o	-user-known-hosts-file	Value to use for the SSH configuration option 'UserKnownHostsFile'. This can also be specified via…	v=
o	-host-key-hostnames	List of hostnames to delegate for the CA. The default value allows all domains and IPs. This is…	v=
o	-host-key-mount-point	Mount point to the SSH secrets engine where host keys are signed. When given a value, Vault will…	v=
o	-private-key-path	Path to the SSH private key to use for authentication. This must be the corresponding private key…	v
o	-public-key-path	Path to the SSH public key to send to Vault for signing. The default is ~/.ssh/id_rsa.pub	v
o	-ssh-executable	Path to the SSH executable to use when connecting to the host The default is ssh. This can also be…	v
o	-valid-principals	List of valid principal names to include in the generated user certificate. This is specified as a…	v
a	1	0
=	ssh	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	ssh	-mode
v	ca	
v	dynamic	
v	otp	
=	ssh	-mount-point
v	ssh/	
=	ssh	-user-known-hosts-file
v	~/.ssh/known_hosts	
t	filepaths
=	ssh	-host-key-hostnames
v	*	
=	ssh	-host-key-mount-point
t	folders
=	ssh	-private-key-path
v	~/.ssh/id_rsa	
t	filepaths
=	ssh	-public-key-path
v	~/.ssh/id_rsa.pub	
t	filepaths
=	ssh	-ssh-executable
v	ssh	
v	/usr/bin/ssh	
t	filepaths
@	token
s	capabilities	Fetches the capabilities of a token for a given path. If a TOKEN is provided as an argument, the…
s	create	Creates a new token that can be used for authentication. This token will be created as a child of…
s	lookup	Displays information about a token or accessor. If a TOKEN is not provided, the locally…
s	renew	Renews a token's lease, extending the amount of time it can be used. If a TOKEN is not provided…
s	revoke	Revokes authentication tokens and their children. If a TOKEN is not provided, the locally…
@	token capabilities
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
a	2	0
=	token capabilities	-format
v	table	
v	json	
v	yaml	
v	pretty	
#	token capabilities	2
v	secret/foo	
@	token create
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-field	Print only the field with the given name. Specifying this option will take precedence over other…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-display-name	Name to associate with this token. This is a non-sensitive value that can be used to help identify…	v=
o	-empty-alias	Name of the entity alias to associate with during token creation. Only works in combination with…	v=
o	-explicit-max-ttl	Explicit maximum lifetime for the token. Unlike normal TTLs, the maximum TTL is a hard limit and…	v=
o	-id	Value for the token. By default, this is an auto-generated string. Specifying this value requires…	v=
o	-metadata	Arbitrary key=value metadata to associate with the token. This metadata will show in the audit log…	v=
o	-no-default-policy	Detach the 'default' policy from the policy set for this token. The default is false	
o	-orphan	Create the token with no parent. This prevents the token from being revoked when the token which…	=
o	-period	If specified, every renewal will use the given period. Periodic tokens do not expire (unless…	v=
o	-policy	Name of a policy to associate with this token. This can be specified multiple times to attach…	v=
o	-renewable	Allow the token to be renewed up to it's maximum TTL. The default is true	
o	-role	Name of the role to create the token against. Specifying -role may override other arguments. The…	v=
o	-ttl	Initial TTL to associate with the token. Token renewals may be able to extend beyond this value…	v=
o	-type	The type of token to create. Can be 'service' or 'batch'. The default is service	v=
o	-use-limit	Number of times this token can be used. After the last use, the token is automatically revoked. By…	v=
=	token create	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	token create	-explicit-max-ttl
v	30s	
v	1m	
v	5m	
=	token create	-period
v	30s	
v	1m	
v	5m	
=	token create	-ttl
v	30s	
v	1m	
v	5m	
=	token create	-type
v	service	
v	batch	
@	token lookup
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-accessor	Treat the argument as an accessor instead of a token. When this option is selected, the output…	
a	1	0
=	token lookup	-format
v	table	
v	json	
v	yaml	
v	pretty	
@	token renew
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
o	-accessor	Treat the argument as an accessor instead of a token. When this option is selected, the output…	
o	-increment|-i	Request a specific increment for renewal. This increment may not be honored, for instance in the…	v=
a	1	0
=	token renew	-format
v	table	
v	json	
v	yaml	
v	pretty	
=	token renew	-increment
v	30s	
v	1m	
v	5m	
@	token revoke
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-accessor	Treat the argument as an accessor instead of a token. When this option is selected, the output…	
o	-mode	Type of revocation to perform. If unspecified, Vault will revoke the token and all of the token's…	v=
o	-self	Perform the revocation on the currently authenticated token. The default is false	
a	1	0
=	token revoke	-mode
v	orphan	
v	path	
@	version-history
o	--help|-h	Display help	
o	-address	Address of the Vault server. The default is https://127.0.0.1:8200. This can also be specified via…	v=
o	-agent-address	Address of the Agent. This can also be specified via the VAULT_AGENT_ADDR environment variable	v=
o	-ca-cert	Path on the local disk to a single PEM-encoded CA certificate to verify the Vault server's SSL…	v=
o	-ca-path	Path on the local disk to a directory of PEM-encoded CA certificates to verify the Vault server's…	v=
o	-client-cert	Path on the local disk to a single PEM-encoded CA certificate to use for TLS authentication to the…	v=
o	-client-key	Path on the local disk to a single PEM-encoded private key matching the client certificate from…	v=
o	-header-key	Key-value pair provided as key=value to provide http header added to any request done by the…	v=
o	-mfa	Supply MFA credentials as part of X-Vault-MFA header. This can also be specified via the VAULT_MFA…	v=
o	-namespace	The namespace to use for the command. Setting this is not necessary but allows using relative…	v=
o	-non-interactive	When set true, prevents asking the user for input via the terminal. The default is false	v=
o	-output-curl-string	Instead of executing the request, print an equivalent cURL command string and exit. The default is…	v=
o	-policy-override	Override a Sentinel policy that has a soft-mandatory enforcement_level specified The default is…	v=
o	-tls-server-name	Name to use as the SNI host when connecting to the Vault server via TLS. This can also be…	v=
o	-tls-skip-verify	Disable verification of TLS certificates. Using this option is highly discouraged as it decreases…	v=
o	-unlock-key	Key to unlock a namespace API lock. The default is (not set)	v=
o	-wrap-ttl	Wraps the response in a cubbyhole token with the requested TTL. The response is available via the…	v=
o	-format	Print the output in the given format. Valid formats are 'table', 'json', 'yaml', or 'pretty'. The…	v=
=	version-history	-format
v	table	
v	json	
v	yaml	
v	pretty	
