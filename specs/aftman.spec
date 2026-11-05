@	
s	init	Creates a new aftman.toml file in the given directory
s	add	Adds a new tool to Aftman and installs it
s	install	Install all tools listed in aftman.toml files based on your current directory
s	self-install	Installs Aftman, upgrades any references to Aftman, and adds aftman to your system PATH if supported
s	trust	
o	--help|-h	Show help for aftman	
o	--version|-V	Show aftman's version	
@	init
a	1	0
@	add
o	--global	Install this tool globally	
a	2	0
@	install
o	--no-trust-check	All tools will be installed, regardless of whether they are known	
@	self-install
@	trust
a	1	0
