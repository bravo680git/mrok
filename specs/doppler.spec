@	
s	activity	Get workplace activity logs
s	changelog	View the CLI's changelog
s	completion	Print shell completion script
s	configs	Manage configs
s	configure	View the config file
s	environments	Manage environments
s	feedback	Provide feedback about the Doppler CLI
s	help	Help about any command
s	import	Import projects into your Doppler workplace
s	login	Authenticate to Doppler
s	logout	Log out of the CLI
s	open	Open the Doppler dashboard
s	projects	Manage projects
s	run	Run a command with secrets injected into the environment
s	secrets	Manage secrets
s	settings	Get workplace settings
s	setup	Setup the Doppler CLI for managing secrets
s	update	Update the Doppler CLI
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for doppler	
o	-v|--version	Get the version of the Doppler CLI	
=		--configuration
t	filepaths
=		--scope
t	folders
@	activity
s	get	Get workplace activity log
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for activity	
=	activity	--configuration
t	filepaths
=	activity	--scope
t	folders
@	activity get
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for get	
o	--log	Activity log id	v
a	1	0
=	activity get	--configuration
t	filepaths
=	activity get	--scope
t	folders
@	changelog
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for changelog	
o	-n|--number	Number of versions to show changes for (default 3)	v
=	changelog	--configuration
t	filepaths
=	changelog	--scope
t	folders
@	completion
s	install	Install completions for the current shell
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for completion	
=	completion	--configuration
t	filepaths
=	completion	--scope
t	folders
@	completion install
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for install	
a	1	0
=	completion install	--configuration
t	filepaths
=	completion install	--scope
t	folders
@	configs
s	clone	Clone a config
s	create	Create a config
s	delete	Delete a config
s	get	Get info for a config
s	lock	Lock a config
s	logs	List config audit logs
s	tokens	List a config's service tokens
s	unlock	Unlock a config
s	update	Update a config
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for configs	
o	-p|--project	Project (e.g. backend)	v
=	configs	--configuration
t	filepaths
=	configs	--scope
t	folders
=	configs	-p
d
@	configs clone
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for clone	
o	-p|--project	Project (e.g. backend)	v
o	--name	New config name	v
=	configs clone	--configuration
t	filepaths
=	configs clone	--scope
t	folders
=	configs clone	-c
d
=	configs clone	-p
d
@	configs create
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for create	
o	-p|--project	Project (e.g. backend)	v
o	--name	Config name	v
o	--environment|-e	Config environment	v
=	configs create	--configuration
t	filepaths
=	configs create	--scope
t	folders
=	configs create	-p
d
@	configs delete
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for delete	
o	-p|--project	Project (e.g. backend)	v
o	--yes|-y	Proceed without confirmation	
a	1	0
=	configs delete	--configuration
t	filepaths
=	configs delete	--scope
t	folders
=	configs delete	-c
d
=	configs delete	-p
d
#	configs delete	1
d
@	configs get
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for get	
o	-p|--project	Project (e.g. backend)	v
a	1	0
=	configs get	--configuration
t	filepaths
=	configs get	--scope
t	folders
=	configs get	-c
d
=	configs get	-p
d
#	configs get	1
d
@	configs lock
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for lock	
o	-p|--project	Project (e.g. backend)	v
o	--yes|-y	Proceed without confirmation	
a	1	0
=	configs lock	--configuration
t	filepaths
=	configs lock	--scope
t	folders
=	configs lock	-c
d
=	configs lock	-p
d
#	configs lock	1
d
@	configs logs
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for logs	
o	-p|--project	Project (e.g. backend)	v
a	1	0
=	configs logs	--configuration
t	filepaths
=	configs logs	--scope
t	folders
=	configs logs	-c
d
=	configs logs	-p
d
#	configs logs	1
d
@	configs tokens
s	get	Get a config's service token
s	create	Create a service token for a config
s	revoke	Revoke a service token from a config
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for tokens	
o	-p|--project	Project (e.g. backend)	v
=	configs tokens	--configuration
t	filepaths
=	configs tokens	--scope
t	folders
=	configs tokens	-c
d
=	configs tokens	-p
d
@	configs tokens get
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	--slug	Service token slug	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for tokens	
o	-p|--project	Project (e.g. backend)	v
a	1	0
=	configs tokens get	--configuration
t	filepaths
=	configs tokens get	--scope
t	folders
=	configs tokens get	-c
d
=	configs tokens get	-p
d
@	configs tokens create
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	--access	Print only the token without formatting	v
o	-c|--config	Config (e.g. dev)	v
o	--copy	Copy the token to your clipboard	
o	--max-age	Max age of the token (e.g. '3h', '15m')	v
o	--name	Service token name	v
o	--plain	Print only the token without formatting	
o	-h|--help	Help for tokens	
o	-p|--project	Project (e.g. backend)	v
=	configs tokens create	--configuration
t	filepaths
=	configs tokens create	--scope
t	folders
=	configs tokens create	--access
v	read	
v	read/write	
=	configs tokens create	-c
d
=	configs tokens create	-p
d
@	configs tokens revoke
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for tokens	
o	-p|--project	Project (e.g. backend)	v
=	configs tokens revoke	--configuration
t	filepaths
=	configs tokens revoke	--scope
t	folders
=	configs tokens revoke	-c
d
=	configs tokens revoke	-p
d
@	configs unlock
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for unlock	
o	-p|--project	Project (e.g. backend)	v
o	--yes|-y	Proceed without confirmation	
=	configs unlock	--configuration
t	filepaths
=	configs unlock	--scope
t	folders
=	configs unlock	-c
d
=	configs unlock	-p
d
@	configs update
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for update	
o	-p|--project	Project (e.g. backend)	v
o	--yes|-y	Proceed without confirmation	
o	--name	Config name	v
=	configs update	--configuration
t	filepaths
=	configs update	--scope
t	folders
=	configs update	-c
d
=	configs update	-p
d
@	configure
s	debug	View current configuration utilizing all config sources
s	get	Get the value of one or more options in the config file
s	options	List all supported config options
s	reset	Reset local CLI configuration to a clean initial state
s	set	Set the value of one or more options in the config file
s	unset	Unset the value of one or more options in the config file
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for configure	
o	-p|--project	Project (e.g. backend)	v
=	configure	--configuration
t	filepaths
=	configure	--scope
t	folders
=	configure	-p
d
@	configure debug
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for debug	
=	configure debug	--configuration
t	filepaths
=	configure debug	--scope
t	folders
@	configure get
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for get	
o	--copy	Copy the value(s) to your clipboard	
o	--plain	Print values without formatting. values will be printed in the same order as specified	
=	configure get	--configuration
t	filepaths
=	configure get	--scope
t	folders
@	configure options
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for options	
=	configure options	--configuration
t	filepaths
=	configure options	--scope
t	folders
@	configure reset
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for reset	
o	--yes|-y	Proceed without confirmation	
=	configure reset	--configuration
t	filepaths
=	configure reset	--scope
t	folders
@	configure set
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for set	
=	configure set	--configuration
t	filepaths
=	configure set	--scope
t	folders
@	configure unset
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for environments	
=	configure unset	--configuration
t	filepaths
=	configure unset	--scope
t	folders
@	environments
s	create	Create an environment
s	delete	Delete an environment
s	get	Get info for an environment
s	rename	Rename an environment
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for environments	
o	-p|--project	Project (e.g. backend)	v
=	environments	--configuration
t	filepaths
=	environments	--scope
t	folders
=	environments	-p
d
@	environments create
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for create	
o	-p|--project	Project (e.g. backend)	v
a	2	0
=	environments create	--configuration
t	filepaths
=	environments create	--scope
t	folders
=	environments create	-p
d
@	environments delete
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for delete	
o	-p|--project	Project (e.g. backend)	v
o	--yes|-y	Proceed without confirmation	
a	1	0
=	environments delete	--configuration
t	filepaths
=	environments delete	--scope
t	folders
=	environments delete	-p
d
#	environments delete	1
d
@	environments get
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for get	
o	-p|--project	Project (e.g. backend)	v
a	1	0
=	environments get	--configuration
t	filepaths
=	environments get	--scope
t	folders
=	environments get	-p
d
#	environments get	1
d
@	environments rename
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for rename	
o	-p|--project	Project (e.g. backend)	v
o	--yes|-y	Proceed without confirmation	
o	--name	New name	v
o	--slug	New slug	v
a	1	0
=	environments rename	--configuration
t	filepaths
=	environments rename	--scope
t	folders
=	environments rename	-p
d
#	environments rename	1
d
@	feedback
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for feedback	
=	feedback	--configuration
t	filepaths
=	feedback	--scope
t	folders
@	help
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for help	
=	help	--configuration
t	filepaths
=	help	--scope
t	folders
@	import
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for Import projects into your Doppler workplace	
o	--template	Path to template file (e.g. './path/to/file.yaml') (default "doppler-template.yaml")	v
=	import	--configuration
t	filepaths
=	import	--scope
t	folders
=	import	--template
t	filepaths
@	login
s	revoke	Revoke your auth token
s	roll	Roll your auth token
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for login	
o	--no-copy	Do not copy the auth code to the clipboard	
o	--overwrite	Overwrite existing token if one exists	
o	--yes|-y	Open browser without confirmation	
=	login	--configuration
t	filepaths
=	login	--scope
t	folders
@	login revoke
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for open	
o	--no-update-config	Do not modify the config file	
o	--no-update-config-options	Do not remove configured options from the config file (i.e. project and config)	
o	--yes|-y	Proceed without confirmation	
=	login revoke	--configuration
t	filepaths
=	login revoke	--scope
t	folders
@	login roll
o	-h|--help	Help for open	
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
=	login roll	--configuration
t	filepaths
=	login roll	--scope
t	folders
@	logout
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for logout	
o	--no-update-config	Do not modify the config file	
o	--no-update-config-options	Do not remove configured options from the config file (i.e. project and config)	
o	--yes|-y	Proceed without confirmation	
=	logout	--configuration
t	filepaths
=	logout	--scope
t	folders
@	open
s	dashboard	Open the Doppler dashboard
s	docs	Open the Doppler documentation home page
s	github	Open Doppler's GitHub to help contribute
s	status	Open the Doppler status page
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for open	
=	open	--configuration
t	filepaths
=	open	--scope
t	folders
@	open dashboard
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for dashboard	
=	open dashboard	--configuration
t	filepaths
=	open dashboard	--scope
t	folders
@	open docs
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for docs	
=	open docs	--configuration
t	filepaths
=	open docs	--scope
t	folders
@	open github
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for github	
=	open github	--configuration
t	filepaths
=	open github	--scope
t	folders
@	open status
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for status	
=	open status	--configuration
t	filepaths
=	open status	--scope
t	folders
@	projects
s	create	Create a project
s	delete	Delete a project
s	get	Get info for a project
s	update	Update a project
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for projects	
=	projects	--configuration
t	filepaths
=	projects	--scope
t	folders
@	projects create
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for create	
o	--name	Project name	v
o	--description	Project description	v
=	projects create	--configuration
t	filepaths
=	projects create	--scope
t	folders
@	projects delete
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for delete	
o	-p|--project	Project (e.g. backend)	v
o	--yes|-y	Proceed without confirmation	
a	1	0
=	projects delete	--configuration
t	filepaths
=	projects delete	--scope
t	folders
=	projects delete	-p
d
#	projects delete	1
d
@	projects get
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for get	
o	-p|--project	Project (e.g. backend)	v
a	1	0
=	projects get	--configuration
t	filepaths
=	projects get	--scope
t	folders
=	projects get	-p
d
#	projects get	1
d
@	projects update
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for projects	
o	-p|--project	Project (e.g. backend)	v
o	--yes|-y	Proceed without confirmation	
o	--name	Project name	v
o	--description	Project description	v
a	1	0
=	projects update	--configuration
t	filepaths
=	projects update	--scope
t	folders
=	projects update	-p
d
#	projects update	1
d
@	run
s	clean	Delete old fallback files
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	--fallback-only	Read all secrets directly from the fallback file, without contacting Doppler. secrets will not be…	
o	f	Path to the fallback file. encrypted secrets are written to this file after each successful fetch…	v
o	--fallback-readonly	Disable modifying the fallback file. secrets can still be read from the file	
o	-h|--help	Help for run	
o	--no-cache	Disable using the fallback file to speed up fetches. the fallback file is only used when the API…	
o	--no-exit-on-write-failure	Do not exit if unable to write the fallback file	
o	--no-fallback	Disable reading and writing the fallback file	
o	--passphrase	Passphrase to use for encrypting the secrets file. the default passphrase is computed using your…	v
o	-p|--project	Project (e.g. backend)	v
o	--command	Command to execute (e.g. "echo hi")	v
o	--forward-signals	Forward signals to the child process (defaults to false when STDOUT is a TTY)	
o	--preserve-env	Ignore any Doppler secrets that are already defined in the environment. this has potential…	
a	1	0
=	run	--configuration
t	filepaths
=	run	--scope
t	folders
=	run	-c
d
=	run	f
t	filepaths
=	run	-p
d
@	run clean
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for clean	
o	--all	Delete all fallback files	
o	--dry-run	Do not delete anything, print what would have happened	
o	--max-age	Delete fallback files that exceed this age (default 336h0m0s)	v
=	run clean	--configuration
t	filepaths
=	run clean	--scope
t	folders
@	secrets
s	delete	Delete the value of one or more secrets
s	download	Download a config's secrets for later use
s	get	Get the value of one or more secrets
s	set	Set the value of one or more secrets
s	substitute	Substitute secrets into a template file
s	upload	Upload a secrets file
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for secrets	
o	-p|--project	Project (e.g. backend)	v
o	--raw	Print the raw secret value without processing variables	v
o	--only-names	Only print the secret names; omit all values	
=	secrets	--configuration
t	filepaths
=	secrets	--scope
t	folders
=	secrets	-c
d
=	secrets	-p
d
@	secrets delete
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for delete	
o	-p|--project	Project (e.g. backend)	v
o	--raw	Print the raw secret value without processing variables	v
o	--yes|-y	Proceed without confirmation	
a	1	0
=	secrets delete	--configuration
t	filepaths
=	secrets delete	--scope
t	folders
=	secrets delete	-c
d
=	secrets delete	-p
d
#	secrets delete	1
d
@	secrets download
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	--fallback-only	Read all secrets directly from the fallback file, without contacting Doppler. secrets will not be…	
o	f	Path to the fallback file. encrypted secrets are written to this file after each successful fetch…	v
o	--fallback-passphrase	Passphrase to use for encrypting the fallback file. by default the passphrase is computed using…	v
o	--fallback-readonly	Disable modifying the fallback file. secrets can still be read from the file	
o	--format	Output format. one of json, env, yaml, docker, env-no-quotes (default "json")	v
o	-h|--help	Help for download	
o	--no-cache	Disable using the fallback file to speed up fetches. the fallback file is only used when the API…	
o	--no-exit-on-write-failure	Do not exit if unable to write the fallback file	
o	--no-fallback	Disable reading and writing the fallback file	
o	--passphrase	Passphrase to use for encrypting the secrets file. the default passphrase is computed using your…	v
o	-p|--project	Project (e.g. backend)	v
o	--yes|-y	Proceed without confirmation	
o	--no-file	Print the response to stdout	
a	1	0
=	secrets download	--configuration
t	filepaths
=	secrets download	--scope
t	folders
=	secrets download	-c
d
=	secrets download	f
t	filepaths
=	secrets download	--format
v	json	
v	env	
v	yaml	
v	docker	
v	env-no-quotes	
=	secrets download	-p
d
#	secrets download	1
t	filepaths
@	secrets get
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for get	
o	-p|--project	Project (e.g. backend)	v
o	--raw	Print the raw secret value without processing variables	v
o	--copy	Copy the value(s) to your clipboard	v
o	--no-exit-on-missing-secret	Do not exit if unable to find a requested secret	
o	--plain	Print values without formatting	
a	1	0
=	secrets get	--configuration
t	filepaths
=	secrets get	--scope
t	folders
=	secrets get	-c
d
=	secrets get	-p
d
#	secrets get	1
d
@	secrets set
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for set	
o	-p|--project	Project (e.g. backend)	v
o	--raw	Print the raw secret value without processing variables	v
o	--no-interactive	Do not allow entering secret value via interactive mode	
a	1	0
=	secrets set	--configuration
t	filepaths
=	secrets set	--scope
t	folders
=	secrets set	-c
d
=	secrets set	-p
d
#	secrets set	1
d
@	secrets substitute
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for substitute	
o	-p|--project	Project (e.g. backend)	v
o	--output	Path to the output file. by default the rendered text will be written to stdout	v
a	1	0
=	secrets substitute	--configuration
t	filepaths
=	secrets substitute	--scope
t	folders
=	secrets substitute	-c
d
=	secrets substitute	-p
d
=	secrets substitute	--output
t	filepaths
#	secrets substitute	1
d
@	secrets upload
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for substitute	
o	-p|--project	Project (e.g. backend)	v
o	--raw	Print the raw secret value without processing variables	v
a	1	0
=	secrets upload	--configuration
t	filepaths
=	secrets upload	--scope
t	folders
=	secrets upload	-c
d
=	secrets upload	-p
d
#	secrets upload	1
t	filepaths
@	settings
s	update	Update workplace settings
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for settings	
=	settings	--configuration
t	filepaths
=	settings	--scope
t	folders
@	settings update
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for settings	
o	--email	Set the workplace's billing email	v
o	--name	Set the workplace's name	v
=	settings update	--configuration
t	filepaths
=	settings update	--scope
t	folders
@	setup
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-c|--config	Config (e.g. dev)	v
o	-h|--help	Help for setup	
o	-p|--project	Project (e.g. backend)	v
o	--no-interactive	Do not prompt for information. if the project or config is not specified, an error will be thrown	
o	--no-save-token	Do not save the token to the config when passed via flag or environment variable	
=	setup	--configuration
t	filepaths
=	setup	--scope
t	folders
=	setup	-c
d
=	setup	-p
d
@	update
o	--api-host	The host address for the Doppler API (default "https://api.doppler.com")	v
o	--configuration	Config file (default "~/.doppler/.doppler.yaml")	v
o	--dashboard-host	The host address for the Doppler Dashboard (default "https://dashboard.doppler.com")	v
o	--debug	Output additional information	v
o	--dns-resolver-address	Address to use for DNS resolution (default "1.1.1.1:53")	v
o	--dns-resolver-proto	Protocol to use for DNS resolution (default "udp")	v
o	--dns-resolver-timeout	Max dns lookup duration (default 5s)	v
o	--enable-dns-resolver	Bypass the OS's default DNS resolver	
o	--json	Output json	
o	--no-check-version	Disable checking for Doppler CLI updates	
o	--no-read-env	Do not read config from the environment	
o	--no-timeout	Disable http timeout	
o	--no-verify-tls	Do not verify the validity of TLS certificates on HTTP requests (not recommended)	
o	--print-config	Output active configuration	
o	--scope	The directory to scope your config to (default ".")	v
o	--silent	Disable output of info messages	
o	--timeout	Max http request duration (default 10s)	v
o	--token|-t	Doppler token	v
o	-h|--help	Help for update	
o	--force|-f	Install the latest CLI regardless of whether there's an update available	
=	update	--configuration
t	filepaths
=	update	--scope
t	folders
