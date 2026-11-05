@	
o	--json|-j	Data items from the command line are serialized as a JSON object. The Content-Type and Accept…	
o	--form|-f	FData items from the command line are serialized as form fields.	
o	--multipart	Similar to --form, but always sends a multipart/form-data request (i.e., even without files)	
o	--boundary	Specify a custom boundary string for multipart/form-data requests. Has effect only together with…	
o	--compress|-x	Content compressed (encoded) with Deflate algorithm. The Content-Encoding header is set to deflate	
o	--pretty	Controls output processing. The value can be "none" to not prettify	v
o	--style|-s		v
o	--unsorted	Disables all sorting while formatting output	
o	--sorted	Re-enables all sorting options while formatting output	
o	--format-options	Controls output formatting	v
o	--print|-p	String specifying what the output should contain	v
o	--headers|-h	Print only the response headers. Shortcut for --print=h	
o	--body|-b	Print only the response body. Shortcut for --print=b	
o	--verbose|-v	Verbose output. Print the whole request as well as the response. Also print	
o	--all	By default, only the final request/response is shown. Use this flag to show	
o	--history-print|-P	The same as --print, -p but applies only to intermediary requests/responses	v
o	--stream|-S	Always stream the response body by line, i.e., behave like `tail -f'	
o	--output|-o	Save output to FILE instead of stdout. If --download is also set, then only	v
o	--download|-d	Do not print the response body to stdout. Rather, download it and store it	
o	--continue|-c	Resume an interrupted download. Note that the --output option needs to be specified as well	
o	--quiet|-q	Do not print to stdout or stderr.	
o	--session	Create, or reuse and update a session. Within a session, custom headers,	v
o	--session-read-only	Create or read a session without updating it form the request/response exchange	v
o	--auth|-a	If only the username is provided (-a username), HTTPie will prompt for the password	v
o	--auth-type|-A	The authentication mechanism to be used. Defaults to "basic"	v
o	--ignore-netrc	Ignore credentials from .netrc	
o	--offline	Build the request and print it but don’t actually send it	
o	--proxy	String mapping protocol to the URL of the proxy	v
o	--follow|-F	Follow 30x Location redirects	
o	--max-redirects	By default, requests have a limit of 30 redirects (works with --follow)	v
o	--max-headers	The maximum number of response headers to be read before giving up (default 0, i.e., no limit)	v
o	--timeout	The connection timeout of the request in seconds.	v
o	--check-status	By default, HTTPie exits with 0 when no network or other fatal errors	
o	--path-as-is	Bypass dot segment (/../ or /./) URL squashing	
o	--chunked	Enable streaming via chunked transfer encoding	
o	--verify	Set to "no" (or "false") to skip checking the host's SSL certificate.	v
o	--ssl	The desired protocol version to use. This will default to	v
o	--ciphers	A string in the OpenSSL cipher list format	v
o	--cert	You can specify a local cert to use as client side SSL certificate.	v
o	--cert-key	The private key to use with SSL. Only needed if --cert is given and the certificate file does not…	v
o	--ignore-stdin|-I	Do not attempt to read stdin	
o	--help	Show the help message and exit	
o	--version	Show version and exit	
o	--traceback	Prints the exception traceback should one occur	
o	--default-scheme	The default scheme to use if not specified in the URL	v
o	--debug	Prints the exception traceback should one occur, as well as other	
a	3	1
=		--pretty
v	all	
v	colors	
v	format	
v	none	
=		--style
v	abap	
v	algol	
v	algol_nu	
v	arduino	
v	auto	
v	autumn	
v	borland	
v	bw	
v	colorful	
v	default	
v	emacs	
v	friendly	
v	fruity	
v	igor	
v	inkpot	
v	lovelace	
v	manni	
v	monokai	
v	murphy	
v	native	
v	paraiso-dark	
v	paraiso-light	
v	pastie	
v	perldoc	
v	rainbow_dash	
v	rrt	
v	sas	
v	solarized	
v	solarized-dark	
v	solarized-light	
v	stata	
v	stata-dark	
v	stata-light	
v	tango	
v	trac	
v	vim	
v	vs	
v	xcode	
=		--format-options
v	headers.sort:true	
v	json.format:true	
v	json.indent:4	
v	json.sort_keys:true	
=		--print
v	H	Request headers
v	B	Request body
v	h	Response headers
v	b	Response body
=		--history-print
v	H	Request headers
v	B	Request body
v	h	Response headers
v	b	Response body
=		--output
t	filepaths
=		--session
t	filepaths
=		--session-read-only
t	filepaths
=		--auth-type
v	basic	Basic HTTP auth
v	digest	Digest HTTP auth
=		--verify
v	no	
v	yes	
t	filepaths
=		--ssl
v	ssl2.3	
v	tls1	
v	tls1.1	
v	tls1.2	
=		--cert
t	filepaths
=		--cert-key
t	filepaths
#		1
v	GET	
v	POST	
v	PUT	
v	DELETE	
v	HEAD	
