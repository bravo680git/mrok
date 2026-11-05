@	
s	i|install	Install a Node.js version
s	rm|–	Remove a Node.js version
s	prune	Remove all cached Node.js versions except the installed version
s	doctor	Display diagnostics to help resolve problems
s	uninstall	Remove the installed Node.js
s	ls|list	Output downloaded versions
s	lsr|ls-remote|list-remote	Output matching versions available for download
s	which|bin	Output path for downloaded node version
s	run|use|as	Execute downloaded Node.js version with args
s	exec	Execute command with modified PATH, so downloaded node version and npm first
o	-V|--version	Output version of n	
o	-h|--help	Display help information	
o	-p|--preserve	Preserve npm and npx during install of Node.js	
o	--no-preserve	Do not preserve npm and npx during install of Node.js	
o	-q|--quiet	Disable curl output. Disable log messages processing "auto" and "engine" labels	
o	-d|--download	Download only	
o	-a|--arch	Override system architecture	v
o	--insecure	Turn off certificate checking for https requests (may be needed from behind a proxy server)	
o	--use-xz	Override automatic detection of xz support and enable use of xz compressed node downloads	
o	--no-use-xz	Override automatic detection of xz support and disable use of xz compressed node downloads	
a	1	0
=		-a
v	x64	
v	x86_64	
v	arm64	
v	aarch64	
v	armv8l	
v	x86	
v	i386	
v	i686	
v	armv6l	
v	armv7l	
#		1
v	latest	Newest official release
v	current	Newest official release
v	lts	Newest Long Term Support official release
v	auto	Read version from file: .n-node-version, .node-version, .nvmrc, or package.json
v	engine	Read version from package.json
d
@	i
a	1	0
#	i	1
v	latest	Newest official release
v	current	Newest official release
v	lts	Newest Long Term Support official release
v	auto	Read version from file: .n-node-version, .node-version, .nvmrc, or package.json
v	engine	Read version from package.json
d
@	rm
a	1	1
#	rm	1
v	latest	Newest official release
v	current	Newest official release
v	lts	Newest Long Term Support official release
v	auto	Read version from file: .n-node-version, .node-version, .nvmrc, or package.json
v	engine	Read version from package.json
d
@	prune
@	doctor
@	uninstall
@	ls
@	lsr
o	--all	Ls-remote displays all matches instead of last 20	
a	1	0
#	lsr	1
v	latest	Newest official release
v	current	Newest official release
v	lts	Newest Long Term Support official release
v	auto	Read version from file: .n-node-version, .node-version, .nvmrc, or package.json
v	engine	Read version from package.json
d
@	which
a	1	0
#	which	1
v	latest	Newest official release
v	current	Newest official release
v	lts	Newest Long Term Support official release
v	auto	Read version from file: .n-node-version, .node-version, .nvmrc, or package.json
v	engine	Read version from package.json
d
@	run
o	-e|--eval=...	Evaluate script	v
o	--watch	Watch input files	
o	--watch-path	Specify a watch directory or file	v
o	--watch-preserve-output	Disable the clearing of the console when watch mode restarts the process	
o	--env-file	Specify a file containing environment variables	v
o	-p|--print	Evaluate script and print result	
o	-c|--check	Syntax check script without executing	
o	-v|--version	Print Node.js version	
o	-i|--interactive	Always enter the REPL even if stdin does not appear to be a terminal	
o	-h|--help	Print node command line options (currently set)	
o	--inspect	Activate inspector on host:port (default: 127.0.0.1:9229)	V=
o	--preserve-symlinks	Follows symlinks to directories when examining source code and templates for translation strings	
a	2	0
=	run	--watch-path
t	filepaths
=	run	--env-file
t	filepaths
#	run	1
v	latest	Newest official release
v	current	Newest official release
v	lts	Newest Long Term Support official release
v	auto	Read version from file: .n-node-version, .node-version, .nvmrc, or package.json
v	engine	Read version from package.json
d
#	run	2
d
@	exec
a	3	1
#	exec	1
v	latest	Newest official release
v	current	Newest official release
v	lts	Newest Long Term Support official release
v	auto	Read version from file: .n-node-version, .node-version, .nvmrc, or package.json
v	engine	Read version from package.json
d
