@	
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
=		-F
t	filepaths
=		-i
t	filepaths
=		-o
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
=		-S
t	filepaths
#		1
t	history
d
