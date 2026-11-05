@	
s	update	Update the agent if a new version exists
s	version	Print the version
s	proxy-dns	Run a DNS over HTTPS proxy server
s	service	Manages the cloudflared launch agent
s	help	Shows a list of commands or help for one command
s	access	Cloudflare Access protects internal resources by securing, authenticating and monitoring access…
s	tunnel	Use Cloudflare Tunnel to expose private services to the Internet or to Cloudflare connected…
o	--credentials-file|--cred-file	Filepath at which to read/write the tunnel credentials [$TUNNEL_CRED_FILE]	v
o	--region	Cloudflare Edge region to connect to. Omit or set to empty to connect to the global region…	v
o	--overwrite-dns|-f	Overwrites existing DNS records with this hostname (default: false) [$TUNNEL_FORCE_PROVISIONING_DNS]	
o	--help|-h	Show help for cloudflared	p
=		--credentials-file
t	filepaths
@	update
o	--beta	Specify if you wish to update to the latest beta version (default: false)	
o	--version	Specify a version you wish to upgrade or downgrade to	v
a	1	1
@	version
a	1	1
@	proxy-dns
o	--metrics	Listen address for metrics reporting. (default: "localhost:") [$TUNNEL_METRICS]	v
o	--address	Listen address for the DNS over HTTPS proxy server. (default: "localhost") [$TUNNEL_DNS_ADDRESS]	v
o	--port	Listen on given port for the DNS over HTTPS proxy server. (default: 53) [$TUNNEL_DNS_PORT]	v
o	--upstream	Upstream endpoint URL, you can specify multiple endpoints for redundancy. (default…	v
o	--bootstrap	Bootstrap endpoint URL, you can specify multiple endpoints for redundancy. (default…	v
o	--max-upstream-conns	Maximum concurrent connections to upstream. Setting to 0 means unlimited. (default: 5)…	v
a	1	0
@	service
s	install	Install cloudflared as an user launch agent
s	uninstall	Uninstall the cloudflared launch agent
s	help|h	Shows a list of commands or help for one command
a	2	1
@	service install
@	service uninstall
@	service help
@	help
@	access
s	login	The login subcommand initiates an authentication flow with your identity provider. The subcommand…
s	curl	Uninstall the cloudflared launch agent
s	token	The token subcommand produces a JWT which can be used to authenticate requests
s	tcp	The tcp subcommand sends data over a proxy to the Cloudflare edge
s	rdp	The rdp subcommand sends data over a proxy to the Cloudflare edge
s	ssh	The ssh subcommand sends data over a proxy to the Cloudflare edge
s	smb	The smb subcommand sends data over a proxy to the Cloudflare edge
s	ssh-config	Prints an example configuration ~/.ssh/config
s	ssh-gen	Generates a short lived certificate for given hostname
s	help|h	Shows a list of commands or help for one command
a	2	1
@	access login
a	1	0
@	access curl
o	--allow-request|--ar		
a	2	1
@	access token
o	--app		v=
@	access tcp
o	--hostname|--tunnel-host|-T	Specify the hostname of your application	v
o	--destination	Specify the destination address of your SSH server	v
o	--url|--listener|-L	Specify the host:port to forward data to Cloudflare edge	v
o	--service-token-id|--id	Specify an Access service token ID you wish to use. [$TUNNEL_SERVICE_TOKEN_ID]	v
o	--service-token-secret|--secret	Specify an Access service token secret you wish to use. [$TUNNEL_SERVICE_TOKEN_SECRET]	v
o	--log-directory|--logfile	Save application log to this directory for reporting issues	v
o	--log-level|--loglevel	Application logging level {debug, info, warn, error, fatal}	v
=	access tcp	--log-directory
t	folders
=	access tcp	--log-level
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
@	access rdp
o	--hostname|--tunnel-host|-T	Specify the hostname of your application	v
o	--destination	Specify the destination address of your SSH server	v
o	--url|--listener|-L	Specify the host:port to forward data to Cloudflare edge	v
o	--service-token-id|--id	Specify an Access service token ID you wish to use. [$TUNNEL_SERVICE_TOKEN_ID]	v
o	--service-token-secret|--secret	Specify an Access service token secret you wish to use. [$TUNNEL_SERVICE_TOKEN_SECRET]	v
o	--log-directory|--logfile	Save application log to this directory for reporting issues	v
o	--log-level|--loglevel	Application logging level {debug, info, warn, error, fatal}	v
=	access rdp	--log-directory
t	folders
=	access rdp	--log-level
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
@	access ssh
o	--hostname|--tunnel-host|-T	Specify the hostname of your application	v
o	--destination	Specify the destination address of your SSH server	v
o	--url|--listener|-L	Specify the host:port to forward data to Cloudflare edge	v
o	--service-token-id|--id	Specify an Access service token ID you wish to use. [$TUNNEL_SERVICE_TOKEN_ID]	v
o	--service-token-secret|--secret	Specify an Access service token secret you wish to use. [$TUNNEL_SERVICE_TOKEN_SECRET]	v
o	--log-directory|--logfile	Save application log to this directory for reporting issues	v
o	--log-level|--loglevel	Application logging level {debug, info, warn, error, fatal}	v
=	access ssh	--log-directory
t	folders
=	access ssh	--log-level
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
@	access smb
o	--hostname|--tunnel-host|-T	Specify the hostname of your application	v
o	--destination	Specify the destination address of your SSH server	v
o	--url|--listener|-L	Specify the host:port to forward data to Cloudflare edge	v
o	--service-token-id|--id	Specify an Access service token ID you wish to use. [$TUNNEL_SERVICE_TOKEN_ID]	v
o	--service-token-secret|--secret	Specify an Access service token secret you wish to use. [$TUNNEL_SERVICE_TOKEN_SECRET]	v
o	--log-directory|--logfile	Save application log to this directory for reporting issues	v
o	--log-level|--loglevel	Application logging level {debug, info, warn, error, fatal}	v
=	access smb	--log-directory
t	folders
=	access smb	--log-level
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
@	access ssh-config
o	--hostname	Specify the hostname of your application	v
o	--short-lived-cert	Specify if you wish to generate short lived certs. (default: false)	
a	2	1
@	access ssh-gen
o	--hostname	Specify the hostname of your application	v
a	2	1
@	access help
@	tunnel
s	login	Generate a configuration file with your login details
s	create	Creates a tunnel, registers it with Cloudflare edge and generates credential file used to run this…
s	route	The route command defines how Cloudflare will proxy requests to this tunnel
s	vnet	Configure and query virtual networks to manage private IP routes with overlapping IPs
s	run	Proxy a local web server by running the given tunnel
s	list	Cloudflared tunnel list will display all active tunnels, their created time and associated…
s	info	Cloudflared tunnel info displays details about the active connectors for a given tunnel…
s	delete	Cloudflared tunnel delete will delete tunnels with the given tunnel UUIDs or names. A tunnel…
s	cleanup	Delete connections for tunnels with the given UUIDs or names
s	token	Fetch the credentials token for an existing tunnel (by name or UUID) that allows to run it
s	help|h	Shows a list of commands or help for one command
o	--config	Specifies a config file in YAML format. (default: "/usr/local/etc/cloudflared/config.yml")	v
o	--origincert	Path to the certificate generated for your origin when you run cloudflared login…	v
o	--autoupdate-freq	Autoupdate frequency. Default is 24h0m0s. (default: 24h0m0s)	v
o	--no-autoupdate	Disable periodic check for updates, restarting the server with the new version. (default: false)…	
o	--metrics	Listen address for metrics reporting. (default: "localhost:") [$TUNNEL_METRICS]	v
o	--pidfile	Write the application's PID to this file after first successful connection. [$TUNNEL_PIDFILE]	v
o	--url	Connect to the local webserver at URL. (default: "http://localhost:8080") [$TUNNEL_URL]	v
o	--hello-world	Run Hello World Server (default: false) [$TUNNEL_HELLO_WORLD]	
o	--socks5	Specify if this tunnel is running as a SOCK5 Server This flag only takes effect if you define your…	
o	--proxy-connect-timeout	HTTP proxy timeout for establishing a new connection This flag only takes effect if you define…	
o	--proxy-tls-timeout	HTTP proxy timeout for completing a TLS handshake This flag only takes effect if you define your…	
o	--proxy-tcp-keepalive	HTTP proxy TCP keepalive duration This flag only takes effect if you define your origin with --url…	
o	--proxy-no-happy-eyeballs	HTTP proxy should disable "happy eyeballs" for IPv4/v6 fallback This flag only takes effect if you…	
o	--proxy-keepalive-connections	HTTP proxy maximum keepalive connection pool size This flag only takes effect if you define your…	
o	--proxy-keepalive-timeout	HTTP proxy timeout for closing an idle connection This flag only takes effect if you define your…	
o	--proxy-connection-timeout	DEPRECATED. No longer has any effect. (default: 1m30s)	
o	--proxy-expect-continue-timeout	DEPRECATED. No longer has any effect. (default: 1m30s)	
o	--http-host-header	Sets the HTTP Host header for the local webserver. This flag only takes effect if you define your…	
o	--origin-server-name	Hostname on the origin server certificate. This flag only takes effect if you define your origin…	
o	--unix-socket	Path to unix socket to use instead of --url [$TUNNEL_UNIX_SOCKET]	v
o	--origin-ca-pool	Path to the CA for the certificate of your origin. This option should be used only if your…	
o	--no-tls-verify	Disables TLS verification of the certificate presented by your origin. Will allow any certificate…	
o	--no-chunked-encoding	Disables chunked transfer encoding; useful if you are running a WSGI server. This flag only takes…	
o	--bastion	Runs as jump host (default: false) [$TUNNEL_BASTION]	
o	--proxy-address	Listen address for the proxy. (default: "127.0.0.1") [$TUNNEL_PROXY_ADDRESS]	v
o	--proxy-port	Listen port for the proxy. (default: 0) [$TUNNEL_PROXY_PORT]	v
o	--loglevel	Application logging level { value: debug, info, warn, error, fatal}. At debug level cloudflared…	v
o	--transport-loglevel|--proto-loglevel	Transport logging level(previously called protocol logging level) { value: debug, info, warn…	v
o	--logfile	Save application log to this file for reporting issues. [$TUNNEL_LOGFILE]	v
o	--log-directory	Save application log to this directory for reporting issues. [$TUNNEL_LOGDIRECTORY]	v
o	--trace-output	Name of trace output file, generated when cloudflared stops. [$TUNNEL_TRACE_OUTPUT]	v
o	--proxy-dns	Run a DNS over HTTPS proxy server. (default: false) [$TUNNEL_DNS]	
o	--proxy-dns-port	Listen on given port for the DNS over HTTPS proxy server. (default: 53) [$TUNNEL_DNS_PORT]	v
o	--proxy-dns-address	Listen address for the DNS over HTTPS proxy server. (default: "localhost") [$TUNNEL_DNS_ADDRESS]	v
o	--proxy-dns-upstream	Upstream endpoint URL, you can specify multiple endpoints for redundancy. (default…	v
o	--proxy-dns-max-upstream-conns	Maximum concurrent connections to upstream. Setting to 0 means unlimited. (default: 5)…	v
o	--proxy-dns-bootstrap	Bootstrap endpoint URL, you can specify multiple endpoints for redundancy. (default…	v
o	--credentials-file|--cred-file	Filepath at which to read/write the tunnel credentials [$TUNNEL_CRED_FILE]	v
o	--region	Cloudflare Edge region to connect to. Omit or set to empty to connect to the global region…	v
o	--hostname	Set a hostname on a Cloudflare zone to route traffic through this tunnel. [$TUNNEL_HOSTNAME]	v
o	--lb-pool	The name of a (new/existing) load balancing pool to add this origin to. [$TUNNEL_LB_POOL]	v
o	--metrics-update-freq	Frequency to update tunnel metrics (default: 5s) [$TUNNEL_METRICS_UPDATE_FREQ]	v
o	--tag	Custom tags used to identify this tunnel, in format KEY=VALUE. Multiple tags may be specified…	v
o	--retries	Maximum number of retries for connection/protocol errors. (default: 5) [$TUNNEL_RETRIES]	v
o	--grace-period	When cloudflared receives SIGINT/SIGTERM it will stop accepting new requests, wait for in-progress…	v
o	--compression-quality	(beta) Use cross-stream compression instead HTTP compression. 0-off, 1-low, 2-medium, >=3-high…	v
o	--name|-n	Stable name to identify the tunnel. Using this flag will create, route and run a tunnel. For…	v
o	--ui	Launch tunnel UI. Tunnel logs are scrollable via 'j', 'k', or arrow keys. (default: false)	
o	--overwrite-dns|-f	Overwrites existing DNS records with this hostname (default: false) [$TUNNEL_FORCE_PROVISIONING_DNS]	
a	1	0
=	tunnel	--config
d
=	tunnel	--origincert
t	filepaths
=	tunnel	--unix-socket
t	filepaths
=	tunnel	--loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel	--transport-loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel	--logfile
t	filepaths
=	tunnel	--log-directory
t	folders
=	tunnel	--credentials-file
t	filepaths
=	tunnel	--compression-quality
v	0	Off
v	1	Low
v	3	High
@	tunnel login
@	tunnel create
o	--config	Specifies a config file in YAML format. (default: "/usr/local/etc/cloudflared/config.yml")	v
o	--origincert	Path to the certificate generated for your origin when you run cloudflared login…	v
o	--autoupdate-freq	Autoupdate frequency. Default is 24h0m0s. (default: 24h0m0s)	v
o	--no-autoupdate	Disable periodic check for updates, restarting the server with the new version. (default: false)…	
o	--metrics	Listen address for metrics reporting. (default: "localhost:") [$TUNNEL_METRICS]	v
o	--pidfile	Write the application's PID to this file after first successful connection. [$TUNNEL_PIDFILE]	v
o	--loglevel	Application logging level {debug, info, warn, error, fatal}. At debug level cloudflared will log…	v
o	--transport-loglevel|--proto-loglevel	Transport logging level(previously called protocol logging level) {debug, info, warn, error…	v
o	--logfile	Save application log to this file for reporting issues. [$TUNNEL_LOGFILE]	v
o	--log-directory	Save application log to this directory for reporting issues. [$TUNNEL_LOGDIRECTORY]	v
o	--trace-output	Name of trace output file, generated when cloudflared stops. [$TUNNEL_TRACE_OUTPUT]	v
o	--output|-o	Render output using given FORMAT. Valid options are 'json' or 'yaml'	v
o	--credentials-file|--cred-file	Filepath at which to read/write the tunnel credentials [$TUNNEL_CRED_FILE]	v
o	--secret|-s	Base64 encoded secret to set for the tunnel. The decoded secret must be at least 32 bytes long. If…	v
a	1	0
=	tunnel create	--config
d
=	tunnel create	--loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel create	--transport-loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel create	--logfile
t	filepaths
=	tunnel create	--log-directory
t	folders
=	tunnel create	--output
v	json	
v	yaml	
=	tunnel create	--credentials-file
t	filepaths,folders
@	tunnel route
s	dns	Creates a DNS CNAME record hostname that points to the tunnel
s	lb	Creates Load Balancer with an origin pool that points to the tunnel
s	ip	Configure and query Cloudflare WARP routing to private IP networks made available through…
a	2	1
@	tunnel route dns
o	--overwrite-dns|-f	Overwrites existing DNS records with this hostname (default: false) [$TUNNEL_FORCE_PROVISIONING_DNS]	
a	2	0
@	tunnel route lb
a	3	0
@	tunnel route ip
s	add	Add a new network to the routing table reachable via a Tunnel
s	show|list	Shows your organization private routing table. You can use flags to filter the results
s	delete	Delete a row from your organization's private routing table
s	get	Check which row of the routing table matches a given IP
@	tunnel route ip add
o	--vnet|--vn	The ID or name of the virtual network to which the route is associated to	v
a	2	1
@	tunnel route ip show
o	--filter-is-deleted	If false (default), only show non-deleted routes. If true, only show deleted routes. (default…	v
o	--filter-tunnel-id	Show only routes with the given tunnel ID	v
o	--filter-network-is-subset-of|--nsub	Show only routes whose network is a subset of the given network	v
o	--filter-network-is-superset-of|--nsup	Show only routes whose network is a superset of the given network	v
o	--filter-comment-is	Show only routes with this comment	v
o	--filter-vnet-id	Show only routes that are attached to the given virtual network ID	v
o	--output|-o	Render output using given FORMAT. Valid options are 'json' or 'yaml'	v
a	1	1
=	tunnel route ip show	--output
v	json	
v	yaml	
@	tunnel route ip delete
o	--vnet|--vn	The ID or name of the virtual network to which the route is associated to	v
a	2	0
@	tunnel route ip get
o	--vnet|--vn	The ID or name of the virtual network to which the route is associated to	v
a	2	0
@	tunnel vnet
s	add	Add a new virtual network to which IP routes can be attached
s	list	Lists the virtual networks based on the given filter flags
s	delete	Delete a virtual network
s	update	Update a virtual network
a	2	1
@	tunnel vnet add
o	--default|-d	The virtual network becomes the default one for the account. This means that all operations that…	
@	tunnel vnet list
o	--id	List virtual networks with the given ID	v
o	--name	List virtual networks with the given NAME	v
o	--is-default	If true, lists the virtual network that is the default one. If false, lists all non-default…	
o	--show-deleted	If false (default), only show non-deleted virtual networks. If true, only show deleted virtual…	
o	--output|-o	Render output using given FORMAT. Valid options are 'json' or 'yaml'	v
=	tunnel vnet list	--output
v	json	
v	yaml	
@	tunnel vnet delete
@	tunnel vnet update
o	--name|-n	The new name for the virtual network	v
o	--comment|-c	A new comment describing the purpose of the virtual network	v
o	--default|-d	The virtual network becomes the default one for the account. This means that all operations that…	
@	tunnel run
o	--config	Specifies a config file in YAML format. (default: "/usr/local/etc/cloudflared/config.yml")	v
o	--origincert	Path to the certificate generated for your origin when you run cloudflared login…	v
o	--autoupdate-freq	Autoupdate frequency. Default is 24h0m0s. (default: 24h0m0s)	v
o	--no-autoupdate	Disable periodic check for updates, restarting the server with the new version. (default: false)…	
o	--metrics	Listen address for metrics reporting. (default: "localhost:") [$TUNNEL_METRICS]	v
o	--pidfile	Write the application's PID to this file after first successful connection. [$TUNNEL_PIDFILE]	v
o	--loglevel	Application logging level {debug, info, warn, error, fatal}. At debug level cloudflared will log…	v
o	--transport-loglevel|--proto-loglevel	Transport logging level(previously called protocol logging level) {debug, info, warn, error…	v
o	--logfile	Save application log to this file for reporting issues. [$TUNNEL_LOGFILE]	v
o	--log-directory	Save application log to this directory for reporting issues. [$TUNNEL_LOGDIRECTORY]	v
o	--trace-output	Name of trace output file, generated when cloudflared stops. [$TUNNEL_TRACE_OUTPUT]	v
o	--force|-f	By default, if a tunnel is currently being run from a cloudflared, you can't simultaneously rerun…	
o	--credentials-file|--cred-file	Filepath at which to read/write the tunnel credentials [$TUNNEL_CRED_FILE]	v
o	--credentials-contents	Contents of the tunnel credentials JSON file to use. When provided along with credentials-file…	v
o	--features|-F	Opt into various features that are still being developed or tested. (accepts multiple inputs)	v
o	--token	The Tunnel token. When provided along with credentials, this will take precedence. [$TUNNEL_TOKEN]	v
o	--url	Connect to the local webserver at URL. (default: "http://localhost:8080") [$TUNNEL_URL]	v
o	--hello-world	Run Hello World Server (default: false) [$TUNNEL_HELLO_WORLD]	
o	--socks5	Specify if this tunnel is running as a SOCK5 Server This flag only takes effect if you define your…	
o	--proxy-connect-timeout	HTTP proxy timeout for establishing a new connection This flag only takes effect if you define…	
o	--proxy-tls-timeout	HTTP proxy timeout for completing a TLS handshake This flag only takes effect if you define your…	
o	--proxy-tcp-keepalive	HTTP proxy TCP keepalive duration This flag only takes effect if you define your origin with --url…	
o	--proxy-no-happy-eyeballs	HTTP proxy should disable "happy eyeballs" for IPv4/v6 fallback This flag only takes effect if you…	
o	--proxy-keepalive-connections	HTTP proxy maximum keepalive connection pool size This flag only takes effect if you define your…	
o	--proxy-keepalive-timeout	HTTP proxy timeout for closing an idle connection This flag only takes effect if you define your…	
o	--proxy-connection-timeout	DEPRECATED. No longer has any effect. (default: 1m30s)	
o	--proxy-expect-continue-timeout	DEPRECATED. No longer has any effect. (default: 1m30s)	
o	--http-host-header	Sets the HTTP Host header for the local webserver. This flag only takes effect if you define your…	
o	--origin-server-name	Hostname on the origin server certificate. This flag only takes effect if you define your origin…	
o	--unix-socket	Path to unix socket to use instead of --url [$TUNNEL_UNIX_SOCKET]	v
o	--origin-ca-pool	Path to the CA for the certificate of your origin. This option should be used only if your…	
o	--no-tls-verify	Disables TLS verification of the certificate presented by your origin. Will allow any certificate…	
o	--no-chunked-encoding	Disables chunked transfer encoding; useful if you are running a WSGI server. This flag only takes…	
o	--bastion	Runs as jump host (default: false) [$TUNNEL_BASTION]	
o	--proxy-address	Listen address for the proxy. (default: "127.0.0.1") [$TUNNEL_PROXY_ADDRESS]	v
o	--proxy-port	Listen port for the proxy. (default: 0) [$TUNNEL_PROXY_PORT]	v
=	tunnel run	--config
d
=	tunnel run	--origincert
t	filepaths
=	tunnel run	--loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel run	--transport-loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel run	--logfile
t	filepaths
=	tunnel run	--log-directory
t	filepaths
=	tunnel run	--trace-output
t	filepaths
=	tunnel run	--credentials-file
t	filepaths
=	tunnel run	--unix-socket
t	filepaths
@	tunnel list
o	--config	Specifies a config file in YAML format. (default: "/usr/local/etc/cloudflared/config.yml")	v
o	--origincert	Path to the certificate generated for your origin when you run cloudflared login…	v
o	--autoupdate-freq	Autoupdate frequency. Default is 24h0m0s. (default: 24h0m0s)	v
o	--no-autoupdate	Disable periodic check for updates, restarting the server with the new version. (default: false)…	
o	--metrics	Listen address for metrics reporting. (default: "localhost:") [$TUNNEL_METRICS]	v
o	--pidfile	Write the application's PID to this file after first successful connection. [$TUNNEL_PIDFILE]	v
o	--loglevel	Application logging level { value: debug, info, warn, error, fatal}. At debug level cloudflared…	v
o	--transport-loglevel|--proto-loglevel	Transport logging level(previously called protocol logging level) { value: debug, info, warn…	v
o	--logfile	Save application log to this file for reporting issues. [$TUNNEL_LOGFILE]	v
o	--log-directory	Save application log to this directory for reporting issues. [$TUNNEL_LOGDIRECTORY]	v
o	--trace-output	Name of trace output file, generated when cloudflared stops. [$TUNNEL_TRACE_OUTPUT]	v
o	--output|-o	Render output using given FORMAT. Valid options are 'json' or 'yaml'	v
o	--show-deleted|-d	Include deleted tunnels in the list (default: false)	
o	--name|-n	List tunnels with the given NAME	v
o	--name-prefix|--np	List tunnels that start with the give NAME prefix	v
o	--exclude-name-prefix|--enp	List tunnels whose NAME does not start with the given prefix	v
o	--when|-w	List tunnels that are active at the given TIME in RFC3339 format (default: current time…	v
o	--id|-i	List tunnel by ID	v
o	--show-recently-disconnected|--rd	Include connections that have recently disconnected in the list (default: false)	
o	--sort-by	Sorts the list of tunnels by the given field. Valid options are { value: name, id, createdAt…	v
o	--invert-sort	Inverts the sort order of the tunnel list. (default: false) [$TUNNEL_LIST_INVERT_SORT]	
=	tunnel list	--config
d
=	tunnel list	--origincert
t	filepaths
=	tunnel list	--loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel list	--transport-loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel list	--logfile
t	filepaths
=	tunnel list	--log-directory
t	folders
=	tunnel list	--output
v	json	
v	yaml	
=	tunnel list	--sort-by
v	name	
v	id	
v	createdAt	
v	deletedAt	
v	numConnections	
@	tunnel info
o	--config	Specifies a config file in YAML format. (default: "/usr/local/etc/cloudflared/config.yml")	v
o	--origincert	Path to the certificate generated for your origin when you run cloudflared login…	v
o	--autoupdate-freq	Autoupdate frequency. Default is 24h0m0s. (default: 24h0m0s)	v
o	--no-autoupdate	Disable periodic check for updates, restarting the server with the new version. (default: false)…	
o	--metrics	Listen address for metrics reporting. (default: "localhost:") [$TUNNEL_METRICS]	v
o	--pidfile	Write the application's PID to this file after first successful connection. [$TUNNEL_PIDFILE]	v
o	--loglevel	Application logging level { value: debug, info, warn, error, fatal}. At debug level cloudflared…	v
o	--transport-loglevel|--proto-loglevel	Transport logging level(previously called protocol logging level) { value: debug, info, warn…	v
o	--logfile	Save application log to this file for reporting issues. [$TUNNEL_LOGFILE]	v
o	--log-directory	Save application log to this directory for reporting issues. [$TUNNEL_LOGDIRECTORY]	v
o	--trace-output	Name of trace output file, generated when cloudflared stops. [$TUNNEL_TRACE_OUTPUT]	v
o	--output|-o	Render output using given FORMAT. Valid options are 'json' or 'yaml'	v
o	--show-recently-disconnected|--rd	Include connections that have recently disconnected in the list (default: false)	
o	--sort-by	Sorts the list of tunnels by the given field. Valid options are { value: name, id, createdAt…	v
o	--invert-sort	Inverts the sort order of the tunnel list. (default: false) [$TUNNEL_LIST_INVERT_SORT]	
=	tunnel info	--config
d
=	tunnel info	--origincert
t	filepaths
=	tunnel info	--loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel info	--transport-loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel info	--logfile
t	filepaths
=	tunnel info	--log-directory
t	folders
=	tunnel info	--output
v	json	
v	yaml	
=	tunnel info	--sort-by
v	name	
v	id	
v	createdAt	
v	deletedAt	
v	numConnections	
@	tunnel delete
o	--config	Specifies a config file in YAML format. (default: "/usr/local/etc/cloudflared/config.yml")	v
o	--origincert	Path to the certificate generated for your origin when you run cloudflared login…	v
o	--autoupdate-freq	Autoupdate frequency. Default is 24h0m0s. (default: 24h0m0s)	v
o	--no-autoupdate	Disable periodic check for updates, restarting the server with the new version. (default: false)…	
o	--metrics	Listen address for metrics reporting. (default: "localhost:") [$TUNNEL_METRICS]	v
o	--pidfile	Write the application's PID to this file after first successful connection. [$TUNNEL_PIDFILE]	v
o	--loglevel	Application logging level { value: debug, info, warn, error, fatal}. At debug level cloudflared…	v
o	--transport-loglevel|--proto-loglevel	Transport logging level(previously called protocol logging level) { value: debug, info, warn…	v
o	--logfile	Save application log to this file for reporting issues. [$TUNNEL_LOGFILE]	v
o	--log-directory	Save application log to this directory for reporting issues. [$TUNNEL_LOGDIRECTORY]	v
o	--trace-output	Name of trace output file, generated when cloudflared stops. [$TUNNEL_TRACE_OUTPUT]	v
o	--credentials-file|--cred-file	Filepath at which to read/write the tunnel credentials [$TUNNEL_CRED_FILE]	v
o	--force|-f	Cleans up any stale connections before the tunnel is deleted. cloudflared will not delete a tunnel…	
a	1	0
=	tunnel delete	--config
d
=	tunnel delete	--origincert
t	filepaths
=	tunnel delete	--loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel delete	--transport-loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel delete	--logfile
t	filepaths
=	tunnel delete	--log-directory
t	folders
=	tunnel delete	--credentials-file
t	filepaths
@	tunnel cleanup
o	--config	Specifies a config file in YAML format. (default: "/usr/local/etc/cloudflared/config.yml")	v
o	--origincert	Path to the certificate generated for your origin when you run cloudflared login…	v
o	--autoupdate-freq	Autoupdate frequency. Default is 24h0m0s. (default: 24h0m0s)	v
o	--no-autoupdate	Disable periodic check for updates, restarting the server with the new version. (default: false)…	
o	--metrics	Listen address for metrics reporting. (default: "localhost:") [$TUNNEL_METRICS]	v
o	--pidfile	Write the application's PID to this file after first successful connection. [$TUNNEL_PIDFILE]	v
o	--loglevel	Application logging level { value: debug, info, warn, error, fatal}. At debug level cloudflared…	v
o	--transport-loglevel|--proto-loglevel	Transport logging level(previously called protocol logging level) { value: debug, info, warn…	v
o	--logfile	Save application log to this file for reporting issues. [$TUNNEL_LOGFILE]	v
o	--log-directory	Save application log to this directory for reporting issues. [$TUNNEL_LOGDIRECTORY]	v
o	--trace-output	Name of trace output file, generated when cloudflared stops. [$TUNNEL_TRACE_OUTPUT]	v
o	--credentials-file|--cred-file	Filepath at which to read/write the tunnel credentials [$TUNNEL_CRED_FILE]	v
o	--force|-f	Cleans up any stale connections before the tunnel is deleted. cloudflared will not delete a tunnel…	
a	1	0
=	tunnel cleanup	--config
d
=	tunnel cleanup	--origincert
t	filepaths
=	tunnel cleanup	--loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel cleanup	--transport-loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel cleanup	--logfile
t	filepaths
=	tunnel cleanup	--log-directory
t	folders
=	tunnel cleanup	--credentials-file
t	filepaths
@	tunnel token
o	--config	Specifies a config file in YAML format. (default: "/usr/local/etc/cloudflared/config.yml")	v
o	--origincert	Path to the certificate generated for your origin when you run cloudflared login…	v
o	--autoupdate-freq	Autoupdate frequency. Default is 24h0m0s. (default: 24h0m0s)	v
o	--no-autoupdate	Disable periodic check for updates, restarting the server with the new version. (default: false)…	
o	--metrics	Listen address for metrics reporting. (default: "localhost:") [$TUNNEL_METRICS]	v
o	--pidfile	Write the application's PID to this file after first successful connection. [$TUNNEL_PIDFILE]	v
o	--loglevel	Application logging level { value: debug, info, warn, error, fatal}. At debug level cloudflared…	v
o	--transport-loglevel|--proto-loglevel	Transport logging level(previously called protocol logging level) { value: debug, info, warn…	v
o	--logfile	Save application log to this file for reporting issues. [$TUNNEL_LOGFILE]	v
o	--log-directory	Save application log to this directory for reporting issues. [$TUNNEL_LOGDIRECTORY]	v
o	--trace-output	Name of trace output file, generated when cloudflared stops. [$TUNNEL_TRACE_OUTPUT]	v
o	--credentials-file|--cred-file	Filepath at which to read/write the tunnel credentials [$TUNNEL_CRED_FILE]	v
o	--force|-f	Cleans up any stale connections before the tunnel is deleted. cloudflared will not delete a tunnel…	
a	1	0
=	tunnel token	--config
d
=	tunnel token	--origincert
t	filepaths
=	tunnel token	--loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel token	--transport-loglevel
v	debug	
v	info	
v	warn	
v	error	
v	fatal	
=	tunnel token	--logfile
t	filepaths
=	tunnel token	--log-directory
t	folders
=	tunnel token	--credentials-file
t	filepaths
@	tunnel help
