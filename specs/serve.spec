@	
o	-h|--help	Shows help message	
o	-v|--version	Displays the current version of serve	
o	-l|--listen	Specify a URI endpoint on which to listen - more than one may be specified to listen in multiple…	v
o	-p	Specify custom port	v
o	-d|--debug	Show debugging information	
o	-s|--single	Rewrite all not-found requests to `index.html`	
o	-c|--config	Specify custom path to `serve.json`	v
o	-C|--cors	Enable CORS, sets `Access-Control-Allow-Origin` to `*`	
o	-n|--no-clipboard	Do not copy the local address to the clipboard	
o	-u|--no-compression	Do not compress files	
o	--no-etag	Send `Last-Modified` header instead of `ETag`	
o	-S|--symlinks	Resolve symlinks instead of showing 404 errors	
o	--ssl-cert	Optional path to an SSL/TLS certificate to serve with HTTPS	v
o	--ssl-key	Optional path to the SSL/TLS certificate's private key	v
o	--ssl-pass	Optional path to the SSL/TLS certificate's passphrase	v
o	--no-port-switching	Do not open a port other than the one specified when it's taken	
a	1	0
=		-l
v	port	E.g. serve --listen 1234
v	host/port	E.g. serve --listen tcp://hostname:1234
v	unix domain	E.g. serve --listen unix:/path/to/socket.sock
v	windows pipe	E.g. serve -l pipe:\.pipePipeName
=		-c
t	filepaths
=		--ssl-cert
t	filepaths
=		--ssl-key
t	filepaths
=		--ssl-pass
t	filepaths
#		1
t	folders
