@	
s	send	Send file(s), or folder
s	relay	Start your own relay
s	help|h	Shows a list of commands or help for one command
o	--help|-h	Show help for croc	p
o	--internal-dns	Use a built-in DNS stub resolver rather than the host operating system	
o	--remember	Save these settings to reuse next time	
o	--debug	Toggle debug mode	
o	--yes	Automatically agree to all prompts	
o	--stdout	Redirect file to stdout	
o	--no-compress	Disable compression	
o	--ask	Make sure sender and recipient are prompted	
o	--local	Force to use only local connections	
o	--ignore-stdin	Ignore piped stdin	
o	--overwrite	Do not prompt to overwrite	
o	--curve	Choose an encryption curve	v
o	--ip	Set sender ip if known	v
o	--relay	Address of the relay	v
o	--relay6	Ipv6 address of the relay	v
o	--out	Specify an output folder to receive the file	v
o	--pass	Password for the relay (default: "pass123")	v
o	--socks5	Add a socks5 proxy	v
o	--throttleUpload	Throttle the upload speed e.g. 500k	v
o	--version|-v	Print the version	
a	1	0
=		--curve
v	p521	
v	p256	
v	p384	
v	siec	
@	send
o	--code|-c	Codephrase used to connect to relay	v
o	--hash	Hash algorithm	v
o	--text|-t	Send some text	v
o	--no-local	Disable local relay when sending	
o	--no-multi	Disable multiplexing	
o	--ports	Ports of the local relay	
a	1	0
=	send	--hash
v	xxhash	
v	imohash	
v	md5	
#	send	1
t	filepaths,folders
@	relay
o	--host	Host of the relay	v
o	--ports	Ports of the local relay	v
@	help
a	1	0
#	help	1
t	help
