@	
s	version	Print the version
s	ssh	Run shell or execute a command on a remote SSH node
s	aws	Access AWS API
s	apps	View and control proxied applications
s	proxy	Run local TLS proxy allowing connecting to Teleport in single-port mode
s	db	View and control proxied databases
s	join	Join the active SSH session
s	play	Replay the recorded SSH session
s	scp	Secure file copy
s	ls	List remote SSH nodes
s	clusters	List available Teleport clusters
s	login	Log in to a cluster and retrieve the session certificate
s	logout	Delete a cluster certificate
s	status	Display the list of proxy servers and retrieved certificates
s	env	Print commands to set Teleport session environment variables
s	request	Manage access requests
s	kube	Manage available kubernetes clusters
s	mfa	Manage multi-factor authentication (MFA) devices
s	config	Print OpenSSH configuration details
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
=		--proxy
d
=		--user
d
=		-i
t	filepaths
@	version
@	ssh
o	-1	Forces ssh to try protocol version 1 only	
o	-2	Forces ssh to try protocol version 2 only	
o	-4	Forces ssh to use IPv4 addresses only	
o	-6	Forces ssh to use IPv6 addresses only	
o	-A	Enables forwarding of the authentication agent connection	
o	-a	Disables forwarding of the authentication agent connection	
o	-b	Use bind_address on the local machine as the source address of the connection	v
o	-C	Requests compression of all data (including stdin, stdout, stderr, and data for forwarded X11 and…	
o	-c	Selects the cipher specification for encrypting the session	v
o	-D	Specifies a local 'dynamic' application-level port forwarding	v
o	-e	Sets the escape character for sessions with a pty (default: '~')	v
o	-F	Specifies an alternative per-user configuration file	v
o	-f	Requests ssh to go to background just before command execution	
o	-g	Allows remote hosts to connect to local forwarded ports	
o	-I	Specify the PKCS#11 shared library ssh should use to communicate with a PKCS#11 token providing…	v
o	-i	Selects a file from which the identity (private key) for public key authentication is read	v
o	-K	Enables GSSAPI-based authentication and forwarding (delegation) of GSSAPI credentials to the server	
o	-k	Disables forwarding (delegation) of GSSAPI credentials to the server	
o	-L	Specifies that the given port on the local (client) host is to be forwarded to the given host and…	v
o	-l	Specifies the user to log in as on the remote machine	v
o	-M	Places the ssh client into ``master'' mode for connection sharing	
o	-m	Additionally, for protocol version 2 a comma-separated list of MAC (message authentication code)…	v
o	-N	Do not execute a remote command	
o	-n	Redirects stdin from /dev/null (actually, prevents reading from stdin)	
o	-O	Control an active connection multiplexing master process	v
o	-o	Can be used to give options in the format used in the configuration file	v
o	-p	Port to connect to on the remote host	v
o	-q	Quiet mode. Causes most warning and diagnostic messages to be suppressed	
o	-R	Specifies that the given port on the remote (server) host is to be forwarded to the given host and…	v
o	-S	Specifies the location of a control socket for connection sharing, or the string 'none' to disable…	v
o	-s	May be used to request invocation of a subsystem on the remote system	
o	-T	Disable pseudo-tty allocation	
o	-t	Force pseudo-tty allocation	
o	-V	Display the version number and exit	
o	-v	Verbose mode. Causes ssh to print debugging messages about its progress	
o	-W	Requests that standard input and output on the client be forwarded to host on port over the secure…	v
o	-w	Requests tunnel device forwarding with the specified tun(4) devices between the client (local_tun)…	v
o	-X	Enables X11 forwarding	
o	-x	Disables X11 forwarding	
o	-Y	Enables trusted X11 forwarding	
o	-y	Send log information using the syslog(3) system module	
a	1	0
=	ssh	-F
t	filepaths
=	ssh	-i
t	filepaths
=	ssh	-o
v	AddressFamily	
v	BatchMode	
v	BindAddress	
v	ChallengeResponseAuthentication	
v	CheckHostIP	
v	Cipher	
v	Ciphers	
v	ClearAllForwardings	
v	Compression	
v	CompressionLevel	
v	ConnectionAttempts	
v	ConnectTimeout	
v	ControlMaster	
v	ControlPath	
v	ControlPersist	
v	DynamicForward	
v	EscapeChar	
v	ExitOnForwardFailure	
v	ForwardAgent	
v	ForwardX11	
v	ForwardX11Timeout	
v	ForwardX11Trusted	
v	GatewayPorts	
v	GlobalKnownHostsFile	
v	GSSAPIAuthentication	
v	GSSAPIDelegateCredentials	
v	HashKnownHosts	
v	Host	
v	HostbasedAuthentication	
v	HostKeyAlgorithms	
v	HostKeyAlias	
v	HostName	
v	IdentityFile	
v	IdentitiesOnly	
v	IPQoS	
v	KbdInteractiveAuthentication	
v	KbdInteractiveDevices	
v	KexAlgorithms	
v	LocalCommand	
v	LocalForward	
v	LogLevel	
v	MACs	
v	NoHostAuthenticationForLocalhost	
v	NumberOfPasswordPrompts	
v	PasswordAuthentication	
v	PermitLocalCommand	
v	PKCS11Provider	
v	Port	
v	PreferredAuthentications	
v	Protocol	
v	ProxyCommand	
v	PubkeyAuthentication	
v	RekeyLimit	
v	RequestTTY	
v	RhostsRSAAuthentication	
v	RSAAuthentication	
v	SendEnv	
v	ServerAliveInterval	
v	ServerAliveCountMax	
v	StrictHostKeyChecking	
v	TCPKeepAlive	
v	Tunnel	
v	TunnelDevice	
v	UsePrivilegedPort	
v	User	
v	UserKnownHostsFile	
v	VerifyHostKeyDNS	
v	VisualHostKey	
v	XAuthLocation	
=	ssh	-S
t	filepaths
#	ssh	1
d
@	aws
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	aws	--proxy
d
=	aws	--user
d
=	aws	-i
t	filepaths
=	aws	-f
v	text	
v	json	
v	yaml	
@	apps
s	ls	List available applications
s	login	Retrieve short-lived certificate for an app
s	logout	Remove app certificate
s	config	Print app connection information
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	apps	--proxy
d
=	apps	--user
d
=	apps	-i
t	filepaths
=	apps	-f
v	text	
v	json	
v	yaml	
@	apps ls
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	apps ls	--proxy
d
=	apps ls	--user
d
=	apps ls	-i
t	filepaths
=	apps ls	-f
v	text	
v	json	
v	yaml	
@	apps login
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	apps login	--proxy
d
=	apps login	--user
d
=	apps login	-i
t	filepaths
=	apps login	-f
v	text	
v	json	
v	yaml	
@	apps logout
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	apps logout	--proxy
d
=	apps logout	--user
d
=	apps logout	-i
t	filepaths
=	apps logout	-f
v	text	
v	json	
v	yaml	
@	apps config
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	apps config	--proxy
d
=	apps config	--user
d
=	apps config	-i
t	filepaths
=	apps config	-f
v	text	
v	json	
v	yaml	
@	proxy
s	ssh	Start local TLS proxy for ssh connections when using Teleport in single-port mode
s	db	Start local TLS proxy for database connections when using Teleport in single-port mode
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	proxy	--proxy
d
=	proxy	--user
d
=	proxy	-i
t	filepaths
=	proxy	-f
v	text	
v	json	
v	yaml	
@	proxy ssh
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	proxy ssh	--proxy
d
=	proxy ssh	--user
d
=	proxy ssh	-i
t	filepaths
=	proxy ssh	-f
v	text	
v	json	
v	yaml	
@	proxy db
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	proxy db	--proxy
d
=	proxy db	--user
d
=	proxy db	-i
t	filepaths
=	proxy db	-f
v	text	
v	json	
v	yaml	
@	db
s	ls	List all available databases
s	login	Retrieve credentials for a database
s	logout	Remove database credentials
s	env	Print environment variables for the configured database
s	config	Print database connection information. Useful when configuring GUI clients
s	connect	Connect Connect to a database
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	db	--proxy
d
=	db	--user
d
=	db	-i
t	filepaths
=	db	-f
v	text	
v	json	
v	yaml	
@	db ls
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	db ls	--proxy
d
=	db ls	--user
d
=	db ls	-i
t	filepaths
=	db ls	-f
v	text	
v	json	
v	yaml	
@	db login
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	db login	--proxy
d
=	db login	--user
d
=	db login	-i
t	filepaths
=	db login	-f
v	text	
v	json	
v	yaml	
@	db logout
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	db logout	--proxy
d
=	db logout	--user
d
=	db logout	-i
t	filepaths
=	db logout	-f
v	text	
v	json	
v	yaml	
@	db env
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	db env	--proxy
d
=	db env	--user
d
=	db env	-i
t	filepaths
=	db env	-f
v	text	
v	json	
v	yaml	
@	db config
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	db config	--proxy
d
=	db config	--user
d
=	db config	-i
t	filepaths
=	db config	-f
v	text	
v	json	
v	yaml	
@	db connect
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	db connect	--proxy
d
=	db connect	--user
d
=	db connect	-i
t	filepaths
=	db connect	-f
v	text	
v	json	
v	yaml	
@	join
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	join	--proxy
d
=	join	--user
d
=	join	-i
t	filepaths
=	join	-f
v	text	
v	json	
v	yaml	
@	play
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	play	--proxy
d
=	play	--user
d
=	play	-i
t	filepaths
=	play	-f
v	text	
v	json	
v	yaml	
@	scp
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	scp	--proxy
d
=	scp	--user
d
=	scp	-i
t	filepaths
=	scp	-f
v	text	
v	json	
v	yaml	
@	ls
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	ls	--proxy
d
=	ls	--user
d
=	ls	-i
t	filepaths
=	ls	-f
v	text	
v	json	
v	yaml	
@	clusters
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	clusters	--proxy
d
=	clusters	--user
d
=	clusters	-i
t	filepaths
=	clusters	-f
v	text	
v	json	
v	yaml	
@	login
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	login	--proxy
d
=	login	--user
d
=	login	-i
t	filepaths
=	login	-f
v	text	
v	json	
v	yaml	
@	logout
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	logout	--proxy
d
=	logout	--user
d
=	logout	-i
t	filepaths
=	logout	-f
v	text	
v	json	
v	yaml	
@	status
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	status	--proxy
d
=	status	--user
d
=	status	-i
t	filepaths
=	status	-f
v	text	
v	json	
v	yaml	
@	env
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	env	--proxy
d
=	env	--user
d
=	env	-i
t	filepaths
=	env	-f
v	text	
v	json	
v	yaml	
@	request
s	ls	List access requests
s	show	Show request details
s	new	Create a new access request
s	review	Review an access request
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	request	--proxy
d
=	request	--user
d
=	request	-i
t	filepaths
=	request	-f
v	text	
v	json	
v	yaml	
@	request ls
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	request ls	--proxy
d
=	request ls	--user
d
=	request ls	-i
t	filepaths
=	request ls	-f
v	text	
v	json	
v	yaml	
@	request show
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	request show	--proxy
d
=	request show	--user
d
=	request show	-i
t	filepaths
=	request show	-f
v	text	
v	json	
v	yaml	
@	request new
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	request new	--proxy
d
=	request new	--user
d
=	request new	-i
t	filepaths
=	request new	-f
v	text	
v	json	
v	yaml	
@	request review
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	request review	--proxy
d
=	request review	--user
d
=	request review	-i
t	filepaths
=	request review	-f
v	text	
v	json	
v	yaml	
@	kube
s	ls	Get a list of kubernetes clusters
s	login	Login to a kubernetes cluster
s	sessions	Get a list of active kubernetes sessions
s	exec	Execute a command in a kubernetes pod
s	join	Join an active Kubernetes session
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	kube	--proxy
d
=	kube	--user
d
=	kube	-i
t	filepaths
=	kube	-f
v	text	
v	json	
v	yaml	
@	kube ls
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	kube ls	--proxy
d
=	kube ls	--user
d
=	kube ls	-i
t	filepaths
=	kube ls	-f
v	text	
v	json	
v	yaml	
@	kube login
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	kube login	--proxy
d
=	kube login	--user
d
=	kube login	-i
t	filepaths
=	kube login	-f
v	text	
v	json	
v	yaml	
@	kube sessions
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	kube sessions	--proxy
d
=	kube sessions	--user
d
=	kube sessions	-i
t	filepaths
=	kube sessions	-f
v	text	
v	json	
v	yaml	
@	kube exec
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	kube exec	--proxy
d
=	kube exec	--user
d
=	kube exec	-i
t	filepaths
=	kube exec	-f
v	text	
v	json	
v	yaml	
@	kube join
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	kube join	--proxy
d
=	kube join	--user
d
=	kube join	-i
t	filepaths
=	kube join	-f
v	text	
v	json	
v	yaml	
@	mfa
s	ls	Get a list of registered MFA devices
s	add	Add a new MFA device
s	rm	Remove a MFA device
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	mfa	--proxy
d
=	mfa	--user
d
=	mfa	-i
t	filepaths
=	mfa	-f
v	text	
v	json	
v	yaml	
@	mfa ls
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	mfa ls	--proxy
d
=	mfa ls	--user
d
=	mfa ls	-i
t	filepaths
=	mfa ls	-f
v	text	
v	json	
v	yaml	
@	mfa add
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	mfa add	--proxy
d
=	mfa add	--user
d
=	mfa add	-i
t	filepaths
=	mfa add	-f
v	text	
v	json	
v	yaml	
@	mfa rm
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	mfa rm	--proxy
d
=	mfa rm	--user
d
=	mfa rm	-i
t	filepaths
=	mfa rm	-f
v	text	
v	json	
v	yaml	
@	config
o	-l|--login	Remote host login	
o	--proxy	SSH proxy address	v
o	--user	SSH proxy user	v
o	--ttl	Minutes to live for a SSH session	v
o	-i|--identity	Identity file	v
o	--cert-format	SSH certificate format	v
o	--insecure	Do not verify server's certificate and host name. Use only in test environments	
o	--auth	Specify the name of authentication connector to use	v
o	--skip-version-check	Skip version checking between server and client	
o	-d|--debug	Verbose logging to stdout	
o	-k|--add-keys-to-agent	Controls how keys are handled. Valid values are [auto no yes only]	
o	--enable-escape-sequences	Enable support for SSH escape sequences. Type '~?' during an SSH session to list supported…	
o	--bind-addr	Override host:port used when opening a browser for cluster logins	
o	-J|--jumphost	SSH jumphost	
o	-f|--format	Format output	v
o	-q|--quiet	Quiet mode	
=	config	--proxy
d
=	config	--user
d
=	config	-i
t	filepaths
=	config	-f
v	text	
v	json	
v	yaml	
