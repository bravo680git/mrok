@	
o	-a|--append	Append to target file when uploading	
o	-E|--cert	Client certificate file and password	v
o	-K|--config	Read config from a file	v
o	-C|--continue-at	Resumed transfer offset	v
o	-b|--cookie	Send cookies from string/file	v
o	-c|--cookie-jar	Write cookies to <filename> after operation	v
o	-d|--data	HTTP POST data	v
o	-q|--disable	Disable .curlrc	
o	-D|--dump-header	Write the received headers to <filename>	v
o	-f|--fail	Fail silently (no output at all) on HTTP errors	
o	-F|--form	Specify multipart MIME data	v
o	-P|--ftp-port	Use PORT instead of PASV	v
o	-G|--get	Put the post data in the URL and use GET	
o	-g|--globoff	Disable URL sequences and ranges using {} and []	
o	-I|--head	Show document info only	
o	-H|--header	Pass custom header(s) to server	v
o	-h|--help	This help text	
o	-0|--http1.0	Use HTTP 1.0	
o	-i|--include	Include protocol response headers in the output	
o	-k|--insecure	Allow insecure server connections when using SSL	
o	-4|--ipv4	Resolve names to IPv4 addresses	
o	-6|--ipv6	Resolve names to IPv6 addresses	
o	-j|--junk-session-cookies	Ignore session cookies read from file	
o	-l|--list-only	List only mode	
o	-L|--location	Follow redirects	
o	-M|--manual	Display the full manual	
o	-m|--max-time	Maximum time allowed for the transfer	v
o	-n|--netrc	Must read .netrc for user name and password	
o	-:|--next	Make next URL use its separate set of options	
o	-N|--no-buffer	Disable buffering of the output stream	
o	-o|--output	Write to file instead of stdout	v
o	-#|--progress-bar	Display transfer progress as a bar	
o	-x|--proxy	[protocol://]host[:port] Use this proxy	
o	-U|--proxy-user	Proxy user and password	v
o	-p|--proxytunnel	Operate through an HTTP proxy tunnel (using CONNECT)	
o	-Q|--quote	Send command(s) to server before transfer	
o	-r|--range	Retrieve only the bytes within RANGE	v
o	-e|--referer	Referrer URL	v
o	-J|--remote-header-name	Use the header-provided filename	
o	-O|--remote-name	Write output to a file named as the remote file	
o	-R|--remote-time	Set the remote file's time on the local output	
o	-X|--request	Specify request command to use	v
o	-S|--show-error	Show error even when -s is used	
o	-s|--silent	Silent mode	
o	-Y|--speed-limit	Stop transfers slower than this	v
o	-y|--speed-time	Trigger 'speed-limit' abort after this time	v
o	-2|--sslv2	Use SSLv2	
o	-3|--sslv3	Use SSLv3	
o	-t|--telnet-option	Set telnet option	v
o	-z|--time-cond	Transfer based on a time condition	v
o	-1|--tlsv1	Use TLSv1.0 or greater	
o	-T|--upload-file	Transfer local FILE to destination	v
o	-B|--use-ascii	Use ASCII/text transfer	
o	-u|--user	Server user and password	v
o	-A|--user-agent	Send User-Agent <name> to server	v
o	-v|--verbose	Make the operation more talkative	
o	-V|--version	Show version number and quit	
o	-w|--write-out	Use output FORMAT after completion	v
o	--abstract-unix-socket	Connect via abstract Unix domain socket	v
o	--alt-svc	Name> Enable alt-svc with this cache file	v
o	--anyauth	Pick any authentication method	
o	--basic	Use HTTP Basic Authentication	
o	--cacert	CA certificate to verify peer against	v
o	--capath	CA directory to verify peer against	v
o	--cert-status	Verify the status of the server certificate	
o	--cert-type	Certificate file type	v
o	--ciphers	Of ciphers> SSL ciphers to use	v
o	--compressed	Request compressed response	
o	--compressed-ssh	Enable SSH compression	
o	--connect-timeout	Maximum time allowed for connection	v
o	--connect-to	Connect to host	v
o	--create-dirs	Create necessary local directory hierarchy	
o	--crlf	Convert LF to CRLF in upload	
o	--crlfile	Get a CRL list in PEM format from the given file	v
o	--data-ascii	HTTP POST ASCII data	v
o	--data-binary	HTTP POST binary data	v
o	--data-raw	HTTP POST data, '@' allowed	v
o	--data-urlencode	HTTP POST data url encoded	v
o	--delegation	GSS-API delegation permission	v
o	--digest	Use HTTP Digest Authentication	
o	--disable-eprt	Inhibit using EPRT or LPRT	
o	--disable-epsv	Inhibit using EPSV	
o	--disallow-username-in-url	Disallow username in url	
o	--dns-interface	Interface to use for DNS requests	v
o	--dns-ipv4-addr	IPv4 address to use for DNS requests	v
o	--dns-ipv6-addr	IPv6 address to use for DNS requests	v
o	--dns-servers	DNS server addrs to use	v
o	--doh-url	Resolve host names over DOH	v
o	--egd-file	EGD socket path for random data	v
o	--engine	Crypto engine to use	v
o	--etag-compare	Make a conditional HTTP request for the ETag read from the given file	v
o	--etag-save	Save an HTTP ETag to the specified file	v
o	--expect100-timeout	How long to wait for 100-continue	v
o	--fail-early	Fail on first transfer error, do not continue	
o	--fail-with-body	On HTTP errors, return an error and also output any HTML response	
o	--false-start	Enable TLS False Start	
o	--form-string	Specify multipart MIME data	v
o	--ftp-account	Account data string	v
o	--ftp-alternative-to-user	String to replace USER [name]	v
o	--ftp-create-dirs	Create the remote dirs if not present	
o	--ftp-method	Control CWD usage	v
o	--ftp-pasv	Use PASV/EPSV instead of PORT	
o	--ftp-pret	Send PRET before PASV	
o	--ftp-skip-pasv-ip	Skip the IP address for PASV	
o	--ftp-ssl-ccc	Send CCC after authenticating	
o	--ftp-ssl-ccc-mode	Set CCC mode	v
o	--ftp-ssl-control	Require SSL/TLS for FTP login, clear for transfer	
o	--happy-eyeballs-timeout-ms	How long to wait in milliseconds for IPv6 before trying IPv4	v
o	--haproxy-protocol	Send HAProxy PROXY protocol v1 header	
o	--hostpubmd5	Acceptable MD5 hash of the host public key	v
o	--http0.9	Allow HTTP 0.9 responses	
o	--http1.1	Use HTTP 1.1	
o	--http2	Use HTTP 2	
o	--http2-prior-knowledge	Use HTTP 2 without HTTP/1.1 Upgrade	
o	--ignore-content-length	Ignore the size of the remote resource	
o	--interface	Use network INTERFACE (or address)	v
o	--keepalive-time	Interval time for keepalive probes	v
o	--key	Private key file name	v
o	--key-type	Private key file type	v
o	--krb	Enable Kerberos with security <level>	v
o	--libcurl	Dump libcurl equivalent code of this command line	v
o	--limit-rate	Limit transfer speed to RATE	v
o	--local-port	Force use of RANGE for local port numbers	v
o	--location-trusted	Like --location, and send auth to other hosts	
o	--login-options	Server login options	v
o	--mail-auth	Originator address of the original email	v
o	--mail-from	Mail from this address	v
o	--mail-rcpt	Mail to this address	v
o	--max-filesize	Maximum file size to download	v
o	--max-redirs	Maximum number of redirects allowed	v
o	--metalink	Process given URLs as metalink XML file	
o	--negotiate	Use HTTP Negotiate (SPNEGO) authentication	
o	--netrc-file	Specify FILE for netrc	v
o	--netrc-optional	Use either .netrc or URL	
o	--no-alpn	Disable the ALPN TLS extension	
o	--no-keepalive	Disable TCP keepalive on the connection	
o	--no-npn	Disable the NPN TLS extension	
o	--no-sessionid	Disable SSL session-ID reusing	
o	--noproxy	List of hosts which do not use proxy	v
o	--ntlm	Use HTTP NTLM authentication	
o	--ntlm-wb	Use HTTP NTLM authentication with winbind	
o	--oauth2-bearer	OAuth 2 Bearer Token	v
o	--pass	Pass phrase for the private key	v
o	--path-as-is	Do not squash .. sequences in URL path	
o	--pinnedpubkey	FILE/HASHES Public key to verify peer against	v
o	--post301	Do not switch to GET after following a 301	
o	--post302	Do not switch to GET after following a 302	
o	--post303	Do not switch to GET after following a 303	
o	--preproxy	[protocol://]host[:port] Use this proxy first	
o	--proto	Enable/disable PROTOCOLS	v
o	--proto-default	Use PROTOCOL for any URL missing a scheme	v
o	--proto-redir	Enable/disable PROTOCOLS on redirect	v
o	--proxy-anyauth	Pick any proxy authentication method	
o	--proxy-basic	Use Basic authentication on the proxy	
o	--proxy-cacert	CA certificate to verify peer against for proxy	v
o	--proxy-capath	CA directory to verify peer against for proxy	v
o	--proxy-cert	Set client certificate for proxy	v
o	--proxy-cert-type	Client certificate type for HTTPS proxy	v
o	--proxy-ciphers	SSL ciphers to use for proxy	v
o	--proxy-crlfile	Set a CRL list for proxy	v
o	--proxy-digest	Use Digest authentication on the proxy	
o	--proxy-header	Pass custom header(s) to proxy	v
o	--proxy-insecure	Do HTTPS proxy connections without verifying the proxy	
o	--proxy-key	Private key for HTTPS proxy	v
o	--proxy-key-type	Private key file type for proxy	v
o	--proxy-negotiate	Use HTTP Negotiate (SPNEGO) authentication on the proxy	
o	--proxy-ntlm	Use NTLM authentication on the proxy	
o	--proxy-pass	Pass phrase for the private key for HTTPS proxy	v
o	--proxy-pinnedpubkey	FILE/HASHES public key to verify proxy with	v
o	--proxy-service-name	SPNEGO proxy service name	v
o	--proxy-ssl-allow-beast	Allow security flaw for interop for HTTPS proxy	
o	--proxy-tls13-ciphers	List> TLS 1.3 proxy cipher suites	v
o	--proxy-tlsauthtype	TLS authentication type for HTTPS proxy	v
o	--proxy-tlspassword	TLS password for HTTPS proxy	v
o	--proxy-tlsuser	TLS username for HTTPS proxy	v
o	--proxy-tlsv1	Use TLSv1 for HTTPS proxy	
o	--proxy1.0	Use HTTP/1.0 proxy on given port	v
o	--pubkey	SSH Public key file name	v
o	--random-file	File for reading random data from	v
o	--raw	Do HTTP "raw"; no transfer decoding	
o	--remote-name-all	Use the remote file name for all URLs	
o	--request-target	Specify the target for this request	
o	--resolve	Resolve the host+port to this address	v
o	--retry	Retry request if transient problems occur	v
o	--retry-connrefused	Retry on connection refused (use with --retry)	
o	--retry-delay	Wait time between retries	v
o	--retry-max-time	Retry only within this period	v
o	--sasl-ir	Enable initial response in SASL authentication	
o	--service-name	SPNEGO service name	v
o	--socks4	SOCKS4 proxy on given host + port	v
o	--socks4a	SOCKS4a proxy on given host + port	v
o	--socks5	SOCKS5 proxy on given host + port	v
o	--socks5-basic	Enable username/password auth for SOCKS5 proxies	
o	--socks5-gssapi	Enable GSS-API auth for SOCKS5 proxies	
o	--socks5-gssapi-nec	Compatibility with NEC SOCKS5 server	
o	--socks5-gssapi-service	SOCKS5 proxy service name for GSS-API	v
o	--socks5-hostname	SOCKS5 proxy, pass host name to proxy	v
o	--ssl	Try SSL/TLS	
o	--ssl-auto-client-cert	Obtain and use a client certificate automatically	
o	--ssl-allow-beast	Allow security flaw to improve interop	
o	--ssl-no-revoke	Disable cert revocation checks (Schannel)	
o	--ssl-reqd	Require SSL/TLS	
o	--stderr	Where to redirect stderr	
o	--styled-output	Enable styled output for HTTP headers	
o	--suppress-connect-headers	Suppress proxy CONNECT response headers	
o	--tcp-fastopen	Use TCP Fast Open	
o	--tcp-nodelay	Use the TCP_NODELAY option	
o	--tftp-blksize	Set TFTP BLKSIZE option	v
o	--tftp-no-options	Do not send any TFTP options	
o	--tls-max	Set maximum allowed TLS version	v
o	--tls13-ciphers	Of TLS 1.3 ciphersuites> TLS 1.3 cipher suites to use	v
o	--tlsauthtype	TLS authentication type	v
o	--tlspassword	TLS password	
o	--tlsuser	TLS user name	v
o	--tlsv1.0	Use TLSv1.0 or greater	
o	--tlsv1.1	Use TLSv1.1 or greater	
o	--tlsv1.2	Use TLSv1.2 or greater	
o	--tlsv1.3	Use TLSv1.3 or greater	
o	--tr-encoding	Request compressed transfer encoding	
o	--trace	Write a debug trace to FILE	v
o	--trace-ascii	Like --trace, but without hex output	v
o	--trace-time	Add time stamps to trace/verbose output	
o	--unix-socket	Connect through this Unix domain socket	v
o	--url	URL to work with	v
o	--xattr	Store metadata in extended file attributes	
a	1	0
=		-K
t	filepaths
=		-b
t	filepaths
=		-c
t	filepaths
=		-D
t	filepaths
=		-H
v	Content-Type: application/json	
v	Content-Type: application/x-www-form-urlencoded	
=		-o
t	filepaths
=		-X
v	GET	
v	HEAD	
v	POST	
v	PUT	
v	DELETE	
v	CONNECT	
v	OPTIONS	
v	TRACE	
v	PATCH	
=		-T
t	filepaths
=		--alt-svc
t	filepaths
=		--cacert
t	filepaths
=		--capath
t	folders
=		--cert-type
v	DER	
v	PEM	
v	ENG	
=		--crlfile
t	filepaths
=		--egd-file
t	filepaths
=		--ftp-ssl-ccc-mode
v	active	
v	passive	
=		--key-type
v	DER	
v	PEM	
v	ENG	
=		--libcurl
t	filepaths
=		--netrc-file
t	filepaths
=		--proxy-cacert
t	filepaths
=		--proxy-capath
t	folders
=		--proxy-crlfile
t	filepaths
=		--proxy-header
v	Content-Type: application/json	
v	Content-Type: application/x-www-form-urlencoded	
=		--pubkey
t	filepaths
=		--random-file
t	filepaths
=		--trace
t	filepaths
=		--trace-ascii
t	filepaths
#		1
t	history
