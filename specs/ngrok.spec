@	
s	help	Shows a list of commands or help for one command
s	http	Start an HTTP tunnel
s	authtoken	Save authtoken to configuration file
s	credits	Prints author and licensing information
s	start	Start tunnels by name from the configuration file
s	tcp	Start a TCP tunnel
s	tls	Start a TLS tunnel
s	update	Update ngrok to the latest version
s	version	Print the version string
@	help
a	1	0
#	help	1
v	authtoken	Save authtoken to configuration file
v	credits	Prints author and licensing information
v	http	Start an HTTP tunnel
v	start	Start tunnels by name from the configuration file
v	tcp	Start a TCP tunnel
v	tls	Start a TLS tunnel
v	update	Update ngrok to the latest version
v	version	Print the version string
v	help	Shows a list of commands or help for one command
@	http
o	--log|-log	Path to log file, 'stdout', 'stderr' or 'false'	v
o	--log-format|-log-format	Log record format: 'term', 'logfmt', 'json'	v
o	--log-level|-log-level	Logging level	v
o	--config|-config	Path to config files; they are merged if multiple	v
o	--region|-region	Ngrok server region [us, eu, au, ap, sa, jp, in] (default: us)	v
o	--authtoken|-authtoken	Ngrok.com authtoken identifying a user	v
o	--hostname|-hostname	Host tunnel on custom hostname (requires DNS CNAME)	v
o	--subdomain|-subdomain	Host tunnel on a custom subdomain	v
o	--auth|-auth	Enforce basic auth on tunnel endpoint, 'user:password'	v
o	--bind-tls|-bind-tls	Listen for http, https or both: true/false/both	v
o	--host-header|-host-header	Set Host header; if 'rewrite' use local address hostname	v
o	--introspection|-introspection	Enable/disable http introspection	v
a	1	0
=	http	--log
v	stdout	
v	stderr	
v	false	
t	filepaths
=	http	--log-format
v	term	
v	logfmt	
v	json	
=	http	--log-level
v	crit	
v	warn	
v	error	
v	info	
v	debug	
=	http	--config
t	filepaths
=	http	--region
v	us	
v	eu	
v	au	
v	ap	
v	sa	
v	jp	
v	in	
=	http	--bind-tls
v	true	
v	false	
v	both	
=	http	--host-header
v	rewrite	
=	http	--introspection
v	true	
v	false	
#	http	1
v	8080	Port
@	authtoken
o	--log|-log	Path to log file, 'stdout', 'stderr' or 'false'	v
o	--log-format|-log-format	Log record format: 'term', 'logfmt', 'json'	v
o	--log-level|-log-level	Logging level	v
o	--config|-config	Path to config files; they are merged if multiple	v
a	1	0
=	authtoken	--log
v	stdout	
v	stderr	
v	false	
t	filepaths
=	authtoken	--log-format
v	term	
v	logfmt	
v	json	
=	authtoken	--log-level
v	crit	
v	warn	
v	error	
v	info	
v	debug	
=	authtoken	--config
t	filepaths
@	credits
@	start
o	--log|-log	Path to log file, 'stdout', 'stderr' or 'false'	v
o	--log-format|-log-format	Log record format: 'term', 'logfmt', 'json'	v
o	--log-level|-log-level	Logging level	v
o	--config|-config	Path to config files; they are merged if multiple	v
o	--region|-region	Ngrok server region [us, eu, au, ap, sa, jp, in] (default: us)	v
o	--authtoken|-authtoken	Ngrok.com authtoken identifying a user	v
o	--all|-all	Start all tunnels in the configuration file	
o	--none|-none	Start running no tunnels	
a	1	1
=	start	--log
v	stdout	
v	stderr	
v	false	
t	filepaths
=	start	--log-format
v	term	
v	logfmt	
v	json	
=	start	--log-level
v	crit	
v	warn	
v	error	
v	info	
v	debug	
=	start	--config
t	filepaths
=	start	--region
v	us	
v	eu	
v	au	
v	ap	
v	sa	
v	jp	
v	in	
#	start	1
v	dev	
v	web	
v	blog	
@	tcp
o	--log|-log	Path to log file, 'stdout', 'stderr' or 'false'	v
o	--log-format|-log-format	Log record format: 'term', 'logfmt', 'json'	v
o	--log-level|-log-level	Logging level	v
o	--config|-config	Path to config files; they are merged if multiple	v
o	--authtoken|-authtoken	Ngrok.com authtoken identifying a user	v
o	--region|-region	Ngrok server region [us, eu, au, ap, sa, jp, in] (default: us)	v
o	--remote-addr|-remote-addr	Bind remote address (requires you reserve an address)	v
a	1	0
=	tcp	--log
v	stdout	
v	stderr	
v	false	
t	filepaths
=	tcp	--log-format
v	term	
v	logfmt	
v	json	
=	tcp	--log-level
v	crit	
v	warn	
v	error	
v	info	
v	debug	
=	tcp	--config
t	filepaths
=	tcp	--region
v	us	
v	eu	
v	au	
v	ap	
v	sa	
v	jp	
v	in	
#	tcp	1
v	22	
@	tls
o	--log|-log	Path to log file, 'stdout', 'stderr' or 'false'	v
o	--log-format|-log-format	Log record format: 'term', 'logfmt', 'json'	v
o	--log-level|-log-level	Logging level	v
o	--config|-config	Path to config files; they are merged if multiple	v
o	--authtoken|-authtoken	Ngrok.com authtoken identifying a user	v
o	--region|-region	Ngrok server region [us, eu, au, ap, sa, jp, in] (default: us)	v
o	--hostname|-hostname	Host tunnel on custom hostname (requires DNS CNAME)	v
o	--subdomain|-subdomain	Host tunnel on a custom subdomain	v
o	--client-cas|-client-cas		v
o	--crt|-crt		v
o	--key|-key		v
a	1	0
=	tls	--log
v	stdout	
v	stderr	
v	false	
t	filepaths
=	tls	--log-format
v	term	
v	logfmt	
v	json	
=	tls	--log-level
v	crit	
v	warn	
v	error	
v	info	
v	debug	
=	tls	--config
t	filepaths
=	tls	--region
v	us	
v	eu	
v	au	
v	ap	
v	sa	
v	jp	
v	in	
=	tls	--client-cas
t	filepaths
=	tls	--crt
t	filepaths
=	tls	--key
t	filepaths
@	update
o	--log|-log	Path to log file, 'stdout', 'stderr' or 'false'	v
o	--log-format|-log-format	Log record format: 'term', 'logfmt', 'json'	v
o	--log-level|-log-level	Logging level	v
o	--channel|-channel	Update channel (stable, beta)	v
=	update	--log
v	stdout	
v	stderr	
v	false	
t	filepaths
=	update	--log-format
v	term	
v	logfmt	
v	json	
=	update	--log-level
v	crit	
v	warn	
v	error	
v	info	
v	debug	
=	update	--channel
v	stable	
v	beta	
@	version
