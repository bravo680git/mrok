@	
s	diagnose	Output diagnostics to aid in debugging Valet
s	directory-listing	Determine directory-listing behavior. Default is off, which means a 404 will display
s	fetch-share-url	Get the URL to the current share tunnel (for Expose or ngrok)
s	forget	Remove the current working (or specified) directory from Valet's list of paths
s	help	Display help for a command
s	install	Install the Valet services
s	link	Link the current working directory to Valet
s	links	Display all of the registered Valet links
s	list	List commands
s	log	Tail log file
s	loopback	Get or set the loopback address used for Valet sites
s	on-latest-version|latest	Determine if this is the latest version of Valet
s	open	Open the site for the current (or specified) directory in your browser
s	park	Register the current working (or specified) directory with Valet
s	parked	Display all the current sites within parked paths
s	paths	Get all of the paths registered with Valet
s	proxies	Display all of the proxy sites
s	proxy	Create an Nginx proxy site for the specified host. Useful for docker, mailhog etc
s	restart	Restart the Valet services
s	secure	Secure the given domain with a trusted TLS certificate
s	share	Generate a publicly accessible URL for your project
s	start	Start the Valet services
s	stop	Stop the Valet services
s	tld|domain	Get or set the TLD used for Valet sites
s	trust	Add sudoers files for Brew and Valet to make Valet commands run without passwords
s	uninstall	Uninstall the Valet services
s	unlink	Remove the specified Valet link
s	unproxy	Delete an Nginx proxy config
s	unsecure	Stop serving the given domain over HTTPS and remove the trusted TLS certificate
s	use	Change the version of PHP used by valet
s	which	Determine which Valet driver serves the current working directory
s	isolate	Change the version of PHP used by Valet to serve the current working directory
s	unisolate	Stop customizing the version of PHP used by Valet to serve the current working directory
s	isolated	List all sites using isolated versions of PHP
s	php	Proxy PHP commands to the "php" executable on the isolated site
s	composer	Proxy Composer commands with the "php" executable on the isolated site
s	which-php	Get the PHP executable path for a site
s	completion	Dump the shell completion script
s	secured	Display all of the currently secured sites
s	set-ngrok-token	Set the Ngrok auth token
s	share-tool	Get the name of the current share tool (Expose or ngrok)
s	status	Output the status of Valet and its installed services and config
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=		-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	diagnose
o	-p|--print	Print diagnostics output while running	
o	--plain	Format clipboard output as plain text	
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	diagnose	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	directory-listing
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	directory-listing	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
#	directory-listing	1
v	on	
v	off	
@	fetch-share-url
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	fetch-share-url	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	forget
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	forget	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
#	forget	1
t	folders
@	help
o	--format	The output format (txt, xml, json, or md) [default: 'txt']	v=
o	--raw	To output raw command help	
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	help	--format
v	txt	
v	xml	
v	json	
v	md	
=	help	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
#	help	1
d
@	install
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	install	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	link
o	--secure	Link the site with a trusted TLS certificate	
o	--isolate	Isolate the site to the PHP version specified in the current working directory's .valetrc file	
o	--secure		
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	link	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	links
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	links	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	list
o	--raw	To output raw command list	
o	--format	The output format (txt, xml, json, or md) [default: 'txt']	v=
o	--short	To skip describing commands' arguments	
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	list	--format
v	txt	
v	xml	
v	json	
v	md	
=	list	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	log
o	-f|--follow		
o	-l|--lines		v
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	log	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	loopback
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	loopback	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	on-latest-version
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	on-latest-version	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	open
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	open	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	park
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	park	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
#	park	1
t	folders
@	parked
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	parked	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	paths
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	paths	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	proxies
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	proxies	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	proxy
o	--secure	Create a proxy with a trusted TLS certificate	
o	--secure		
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	2	0
=	proxy	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	restart
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	restart	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	secure
o	expireIn	The amount of days the self signed certificate is valid for. Default is set to 368	=
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	secure	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	share
o	--auth	Enforce basic auth on tunnel endpoint, 'user:password'	
o	--authtoken	Ngrok.com authtoken identifying a user	v
o	--bind-tls	Listen for http, https or both: true/false/both	v
o	--config	Path to config files; they are merged if multiple	v
o	--host-header	Set Host header; if 'rewrite' use local address hostname	v
o	--hostname	Host tunnel on custom hostname (requires DNS CNAME)	
o	--inspect	Enable/disable http introspection	
o	--log	Path to log file, 'stdout', 'stderr' or 'false'	v
o	--log-format	Log record format: 'term', 'logfmt', 'json'	v
o	--log-level	Logging level	v
o	--region	Ngrok server region [us, eu, au, ap, sa, jp, in] (default: us)	v
o	--subdomain	Host tunnel on a custom subdomain	
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	share	--bind-tls
v	true	
v	false	
v	both	
=	share	--config
t	filepaths
=	share	--log
v	stdout	
v	stderr	
v	false	
=	share	--log-format
v	term	
v	logfmt	
v	json	
=	share	--log-level
v	info	
=	share	--region
v	us	
v	eu	
v	au	
v	ap	
v	sa	
v	jp	
v	in	
=	share	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	start
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	start	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	stop
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	stop	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	tld
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	tld	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
#	tld	1
v	local	
v	test	
@	trust
o	--off	Remove the sudoers files so normal sudo password prompts are required	
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	trust	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	uninstall
o	--force	Do a forceful uninstall of Valet and related Homebrew pkgs	
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	uninstall	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	unlink
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	unlink	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	unproxy
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	unproxy	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	unsecure
o	--all		
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	unsecure	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	use
o	--force		
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	use	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
#	use	1
v	php@8.0	
v	php@8.1	
v	php@8.2	
@	which
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	which	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	isolate
o	--site	Name of the website you want to isolate	v=
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	isolate	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
#	isolate	1
v	php@8.0	
v	php@8.1	
v	php@8.2	
@	unisolate
o	--site	Name of the website you want to unisolate	v
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	unisolate	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	isolated
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	isolated	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	php
o	--site	Specify the site to use to get the PHP version (e.g. if the site isn't linked as its directory name)	v=
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	php	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	composer
o	--site	Specify the site to use to get the PHP version (e.g. if the site isn't linked as its directory name)	v=
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	composer	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	which-php
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	which-php	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	completion
o	--debug	Tail the completion debug log	
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	completion	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
#	completion	1
v	bash	
v	fish	
@	secured
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	secured	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	set-ngrok-token
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	set-ngrok-token	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
@	share-tool
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
a	1	0
=	share-tool	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
#	share-tool	1
v	Expose	
v	Ngrok	
@	status
o	-h|--help	Display help for the given command. When no command is given display help for the list command	
o	-q|--quiet	Do not output any message	
o	-V|--version	Display this application version	
o	--ansi	Force (or disable --no-ansi) ANSI output	
o	--no-ansi	Force (or disable --no-ansi) ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	-v|-vv|-vvv|--verbose	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	V
=	status	-v
v	1	Normal output
v	2	More verbose output
v	3	Debug output
