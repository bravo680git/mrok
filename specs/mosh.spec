@	
o	--help|-h	Show help for mosh	
o	--client	Mosh client on local machine (default: "mosh-client")	
o	--server	Mosh server on remote machine (default: "mosh-server")	
o	--predict	Local echo options	v=
o	-4	Use IPv4 only	
o	-6	Use IPv6 only	
o	--family	Network Type	v=
o	--port|-p	Server-side UDP port or range, (No effect on server-side SSH port)	
o	--bind-server	{ssh|any|IP}, ask the server to reply from an IP address, (default: "ssh")	
o	--ssh	Ssh command to run when setting up session, (example: "ssh -p 2222")	v=
o	--no-ssh-pty	Do not allocate a pseudo tty on ssh connection	
o	--no-init	Do not send terminal initialization string	
o	--local	Run mosh-server locally without using ssh	
o	--experimental-remote-ip	Select the method for discovering the remote IP address to use for mosh	v=
o	--version	Version and copyright information	
a	1	0
=		--predict
v	adaptive	Local echo for slower links [default]
v	always	Use local echo even on fast links
v	never	Never use local echo
v	experimental	Aggressively echo even when incorrect
=		--family
v	inet	Use IPv4 only
v	ine6	Use IPv6 only
v	auto	Autodetect network type for single-family hosts only
v	all	Try all network types
v	prefer-inet4	Use all network types, but try IPv4 first [default]
v	prefer-inet6	Use all network types, but try IPv6 first
=		--experimental-remote-ip
v	local	
v	remote	
v	proxy	
#		1
t	history
d
