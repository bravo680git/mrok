@	
o	-V|--version	Display the version of Wget and exit	
o	-h|--help	Print this help	
o	-b|--background	Go to background after startup	
o	-e|--execute=COMMAND	Execute a `.wgetrc'-style command	
o	-o|--output-file=FILE	Log messages to FILE	
o	-a|--append-output=FILE	Append messages to FILE	
o	-q|--quiet	Quiet (no output)	
o	-v|--verbose	Be verbose (this is the default)	
o	-nv|--no-verbose	Turn off verboseness, without being quiet	
o	--report-speed=TYPE	Output bandwidth as TYPE. TYPE can be bits	
o	-i|--input-file=FILE	Download URLs found in local or external FILE	
o	-F|--force-html	Treat input file as HTML	
o	-B|--base=URL	Resolves HTML input-file links (-i -F) relative to URL	
o	--config=FILE	Specify config file to use	
o	--no-config	Do not read any config file	
o	--rejected-log=FILE	Log reasons for URL rejection to FILE	
o	-t|--tries=NUMBER	Set number of retries to NUMBER (0 unlimits)	
o	--retry-connrefused	Retry even if connection is refused	
o	--retry-on-http-error	Comma-separated list of HTTP errors to retry	
o	-O|--output-document=FILE	Write documents to FILE	
o	-nc|--no-clobber	Skip downloads that would download to existing files (overwriting them)	
o	--no-netrc	Don't try to obtain credentials from .netrc	
o	-c|--continue	Resume getting a partially-downloaded file	
o	--start-pos=OFFSET	Start downloading from zero-based position OFFSET	
o	--progress=TYPE	Select progress gauge type	
o	--show-progress	Display the progress bar in any verbosity mode	
o	-N|--timestamping	Don't re-retrieve files unless newer than local	
o	-S|--server-response	Print server response	
o	--spider	Don't download anything	
o	-T|--timeout=SECONDS	Set all timeout values to SECONDS	
o	--dns-timeout=SECS	Set the DNS lookup timeout to SECS	
o	--connect-timeout=SECS	Set the connect timeout to SECS	
o	--read-timeout=SECS	Set the read timeout to SECS	
o	-w|--wait=SECONDS	Wait SECONDS between retrievals	
o	--waitretry=SECONDS	Wait 1..SECONDS between retries of a retrieval	
o	--random-wait	Wait from 0.5*WAIT...1.5*WAIT secs between retrievals	
o	--no-proxy	Explicitly turn off proxy	
o	-Q|--quota=NUMBER	Set retrieval quota to NUMBER	
o	--bind-address=ADDRESS	Bind to ADDRESS (hostname or IP) on local host	
o	--limit-rate=RATE	Limit download rate to RATE	
o	--no-dns-cache	Disable caching DNS lookups	
o	--restrict-file-names=OS	Restrict chars in file names to ones OS allows	
o	--ignore-case	Ignore case when matching files/directories	
o	-4|--inet4-only	Connect only to IPv4 addresses	
o	-6|--inet6-only	Connect only to IPv6 addresses	
o	--user=USER	Set both ftp and http user to USER	
o	--password=PASS	Set both ftp and http password to PASS	
o	--ask-password	Prompt for passwords	
o	--no-iri	Turn off IRI support	
o	--local-encoding=ENC	Use ENC as the local encoding for IRIs	
o	--remote-encoding=ENC	Use ENC as the default remote encoding	
o	--unlink	Remove file before clobber	
o	--xattr	Turn on storage of metadata in extended file attributes	
o	-nd|--no-directories	Don't create directories	
o	-x|--force-directories	Force creation of directories	
o	-nH|--no-host-directories	Don't create host directories	
o	--protocol-directories	Use protocol name in directories	
o	-P|--directory-prefix=PREFIX	Save files to PREFIX/	
o	--cut-dirs=NUMBER	Ignore NUMBER remote directory components	
o	--http-user=USER	Set http user to USER	
o	--http-password=PASS	Set http password to PASS	
o	--no-cache	Disallow server-cached data	
o	-E|--adjust-extension	Save HTML/CSS documents with proper extensions	
o	--ignore-length	Ignore 'Content-Length' header field	
o	--header=STRING	Insert STRING among the headers	
o	--compression=TYPE	Choose compression, one of auto, gzip and none. (default: none)	
o	--max-redirect	Maximum redirections allowed per page	
o	--proxy-user=USER	Set USER as proxy username	
o	--proxy-password=PASS	Set PASS as proxy password	
o	--referer=URL	Include 'Referer: URL' header in HTTP request	
o	--save-headers	Save the HTTP headers to file	
o	-U|--user-agent=AGENT	Identify as AGENT instead of Wget/VERSION	
o	--no-http-keep-alive	Disable HTTP keep-alive (persistent connections)	
o	--no-cookies	Don't use cookies	
o	--load-cookies=FILE	Load cookies from FILE before session	
o	--save-cookies=FILE	Save cookies to FILE after session	
o	--keep-session-cookies	Load and save session (non-permanent) cookies	
o	--post-data=STRING	Use the POST method; send STRING as the data	
o	--post-file=FILE	Use the POST method; send contents of FILE	
o	--method=HTTPMethod	Use method "HTTPMethod" in the request	
o	--body-data=STRING	Send STRING as data. --method MUST be set	
o	--body-file=FILE	Send contents of FILE. --method MUST be set	
o	--content-on-error	Output the received content on server errors	
o	--secure-protocol=PR	Choose secure protocol, one of auto, SSLv2,	
o	--https-only	Only follow secure HTTPS links	
o	--no-check-certificate	Don't validate the server's certificate	
o	--certificate=FILE	Client certificate file	
o	--certificate-type=TYPE	Client certificate type, PEM or DER	
o	--private-key=FILE	Private key file	
o	--private-key-type=TYPE	Private key type, PEM or DER	
o	--ca-certificate=FILE	File with the bundle of CAs	
o	--ca-directory=DIR	Directory where hash list of CAs is stored	
o	--crl-file=FILE	File with bundle of CRLs	
o	--ciphers=STR	Set the priority string (GnuTLS) or cipher list string (OpenSSL) directly	
o	-r|--recursive	Specify recursive download	
o	-l|--level=NUMBER	Maximum recursion depth (inf or 0 for infinite)	
o	--delete-after	Delete files locally after downloading them	
o	-k|--convert-links	Make links in downloaded HTML or CSS point to local files	
o	-K|--backup-converted	Before converting file X, back up as X.orig	
o	-m|--mirror	Shortcut for -N -r -l inf --no-remove-listing	
o	-p|--page-requisites	Get all images, etc. needed to display HTML page	
o	-A|--accept=LIST	Comma-separated list of accepted extensions	
o	-R|--reject=LIST	Comma-separated list of rejected extensions	
o	--accept-regex=REGEX	Regex matching accepted URLs	
o	--reject-regex=REGEX	Regex matching rejected URLs	
o	--regex-type=TYPE	Regex type (posix)	
o	-D|--domains=LIST	Comma-separated list of accepted domains	
o	--exclude-domains=LIST	Comma-separated list of rejected domains	
o	--follow-ftp	Follow FTP links from HTML documents	
o	--follow-tags=LIST	Comma-separated list of followed HTML tags	
o	--ignore-tags=LIST	Comma-separated list of ignored HTML tags	
o	-H|--span-hosts	Go to foreign hosts when recursive	
o	-L|--relative	Follow relative links only	
o	-I|--include-directories=LIST	List of allowed directories	
o	-X|--exclude-directories=LIST	List of excluded directories	
o	-np|--no-parent	Don't ascend to the parent directory	
a	1	1
