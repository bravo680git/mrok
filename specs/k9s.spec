@	
s	help	Help about any command
s	info	Print configuration info
s	version	Print version/build info
o	-A|--all-namespaces	Launch K9s in all namespaces	
o	--as	Username to impersonate for the operation	v
o	--as-group	Group to impersonate for the operation	v
o	--certificate-authority	Path to a cert file for the certificate authority	v
o	--client-key	Path to a client key file for TLS	v
o	-c|--command	Overrides the default resource to load when the application launches	v
o	--context	The name of the kubeconfig context to use	v
o	--crumbsless	Turn K9s crumbs off	
o	--headless	Turn K9s header off	
o	-h|--help	Show help for k9s	
o	--insecure-skip-tls-verify	If true, the server's caCertFile will not be checked for validity	
o	--kubeconfig	Path to the kubeconfig file to use for CLI requests	v
o	--logFile	Specify the log file	v
o	-l|--logLevel	Specify a log level (info, warn, debug, trace, error) (default 'info')	v
o	--logoless	Turn K9s logo off	
o	-n|--namespace	If present, the namespace scope for this CLI request	v
o	--readonly	Sets readOnly mode by overriding readOnly configuration setting	
o	-r|--refresh	Specify the default refresh rate as an integer (sec) (default 2)	v
o	--request-timeout	The length of time to wait before giving up on a single server request	v
o	--screen-dump-dir	Sets a path to a dir for a screen dumps	v
o	--token	Bearer token for authentication to the API server	v
o	--user	The name of the kubeconfig user to use	v
o	--write	Sets write mode by overriding the readOnly configuration setting	
=		--certificate-authority
t	filepaths
=		--client-key
t	filepaths
=		--kubeconfig
t	filepaths
=		--logFile
t	filepaths
=		-l
v	info	
v	warn	
v	debug	
v	trace	
v	error	
=		-n
d
@	help
a	1	0
#	help	1
t	help
@	info
o	-h|--help	Help for info	
@	version
o	-h|--help	Help for version	
o	-s|--short	Prints K9s version info in short format	
