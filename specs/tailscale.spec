@	
s	up	Connect to Tailscale, logging in if needed
s	down	Disconnect from Tailscale
s	logout	Disconnect from Tailscale and expire current node key
s	netcheck	Print an analysis of local network conditions
s	ip	Show Tailscale IP addresses
s	status	Show state of tailscaled and its connections
s	ping	Ping a host at the Tailscale layer, see how it routed
s	nc	Connect to a port on a host, connected to stdin/stdout
s	ssh	SSH to a Tailscale machine
s	version	Print Tailscale version
s	web	Run a web server for controlling Tailscale
s	file	Send or receive files
s	bugreport	Print a shareable identifier to help diagnose issues
s	cert	Get TLS certs
s	help	Print help message
o	--socket	Path to tailscaled's unix socket	v
@	up
o	--accept-dns	Accept DNS configuration from the admin panel	
o	--accept-routes	Accept routes advertised by other Tailscale nodes	
o	--advertise-exit-node	Offer to be an exit node for internet traffic for the tailnet	
o	--advertise-routes	Routes to advertise to other nodes (comma-separated, e.g. "10.0.0.0/8,192.168.0.0/24") or empty…	v
o	--advertise-tags	Comma-separated ACL tags to request; each must start with "tag:" (e.g…	v
o	--auth-key	Node authorization key; if it begins with "file:", then it's a path to a file containing the authkey	v
o	--exit-node	Tailscale exit node (IP or base name) for internet traffic, or empty string to not use an exit node	v
o	--exit-node-allow-lan-access	Allow direct access to the local network when routing traffic via an exit node	
o	--force-reauth	Force reauthentication	
o	--host-routes	Install host routes to other Tailscale nodes	
o	--hostname	Hostname to use instead of the one provided by the OS	
o	--json	Output in JSON format	
o	--login-server	Login server to use	
o	--operator	Unix username to allow to operate on tailscaled without sudo	v
o	--qr	Show QR code for login URLs	
o	--reset	Reset unspecified settings to their default values	
o	--shields-up	Don't allow incoming connections	
o	--ssh	Run an SSH server, permitting access per tailnet admin's declared policy	
o	--help	Show help message	
=	up	--operator
v	$USER	
@	down
o	--help	Show help message	
@	logout
o	--help	Show help message	
@	netcheck
o	--every	If non-zero, do an incremental report with the given frequency	
o	--format	Output format	v
o	--verbose	Verbose logs	
o	--help	Show help message	
=	netcheck	--format
v	json	
v	json-line	
v	human-readable	
@	ip
o	--1	Only print one IP address	
o	--4	Only print IPv4 address	
o	--6	Only print IPv6 address	
o	--help	Show help message	
a	1	0
#	ip	1
d
@	status
o	--active	Filter output to only peers with active sessions	
o	--browser	Open a browser in web mode	
o	--json	Output in JSON format	
o	--listen	Listen address for web mode; use port 0 for automatic (default 127.0.0.1:8384)	v
o	--peers	Show status of peers	
o	--self	Show status of local machine	
o	--web	Run webserver with HTML showing status	
o	--help	Show help message	
@	ping
o	--c	Max number of pings to send	v
o	--timeout	Timeout before giving up on a ping	v
o	--tsmp	Do a TSMP-level ping (through IP + wireguard, but not involving host OS stack)	
o	--until-direct	Stop once a direct path is established	
o	--verbose	Verbose logs	
o	--help	Show help message	
@	nc
o	--help	Show help message	
a	2	0
@	ssh
o	--help	Show help message	
a	1	0
@	version
o	--daemon	Also print local node's daemon version	
o	--help	Show help message	
@	web
o	--cgi	Run as CGI script	
o	--listen	Listen address; use port 0 for automatic (default localhost:8088)	v
o	--help	Show help message	
@	file
s	cp	Copy file(s) to a host
s	get	Move files out of the Tailscale file inbox
o	--help	Show help message	
@	file cp
a	2	1
#	file cp	1
t	filepaths
#	file cp	2
t	filepaths
d
@	file get
a	1	0
#	file get	1
t	folders
@	bugreport
o	--help	Show help message	
a	1	1
@	cert
o	--cert-file	Output cert file or "-" for stdout	v
o	--key-file	Output cert file or "-" for stdout	v
o	--serve-demo	Serve on port :443 using the cert as a demo, instead of writing out the files to disk	
o	--help	Show help message	
=	cert	--cert-file
v	-	Stdout
t	filepaths
=	cert	--key-file
v	-	Stdout
t	filepaths
@	help
