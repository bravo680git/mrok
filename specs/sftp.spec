@	
o	--help|-h	Show help for sftp	
o	-4	Forces scp to use IPv4 addresses only	
o	-6	Forces scp to use IPv6 addresses only	
o	-A	Allows forwarding of ssh-agent(1) to the remote system. The default is not to forward an…	
o	-a	Attempt to continue interrupted transfers rather than overwriting	
o	-B	Specify the size of the buffer that sftp uses when transferring	v
o	-b	Batch mode reads a series of commands from an input batchfile	v
o	-C	Compression enable. Passes the -C flag to ssh(1) to enable compression	
o	-c	Selects the cipher to use for encrypting the data transfer. This option is directly passed to ssh(1)	v
o	-D	Connect directly to a local sftp server (rather than via ssh(1)).	v
o	-F	Specifies an alternative per-user configuration file for ssh. This option is directly passed to…	v
o	-f	Requests that files be flushed to disk immediately after transfer	
o	-i	Selects the file from which the identity (private key) for public key authentication is read. This…	v
o	-J	Connect to the target host by first making an scp connection to the	v
o	-l	Limits the used bandwidth, specified in Kbit/s	v
o	-N	Disables quiet mode, e.g. to override the implicit quiet mode set by the -b flag	
o	-o	Can be used to pass options to ssh in the format used in	v
o	-P	Specifies the port to connect to on the remote host. Note that	v
o	-p	Preserves modification times, access times, and modes from the original file	
o	-q	Quiet mode: disables the progress meter as well as warning and diagnostic messages from ssh(1)	
o	-R	Specify how many requests may be outstanding at any one time.	v
o	-r	Recursively copy entire directories. Note that scp follows symbolic links encountered in the tree…	
o	-S	Name of program to use for the encrypted connection. The program must understand ssh(1) options	v
o	-s	Specifies the SSH2 subsystem or the path for an sftp server on the	v
o	-v	Verbose mode. Causes scp and ssh(1) to print debugging messages about their progress. This is…	
a	2	0
=		-B
v	32768	
=		-b
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
=		-R
v	64	
#		1
t	history,filepaths,folders
d
#		2
t	history,filepaths,folders
d
