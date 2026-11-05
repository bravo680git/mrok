@	
s	auth	Authenticate with the App Store
s	completion	Generate shell completion script
s	download	Download (encrypted) iOS app packages from the App Store
s	help	Display help for command
s	purchase	Obtain a license for the app from the App Store
s	search	Search for iOS apps available on the App Store
o	-h|--help	Show help for ipatool	p
o	--non-interactive	Run in non-interactive session	p
o	--verbose	Enables verbose logs	p
o	--format	Output format	vp
o	-v|--version	Show version for ipatool	
=		--format
v	text	
v	json	
@	auth
s	info	Show current account info
s	login	Login to the App Store
s	revoke	Revoke your App Store credentials
@	auth info
@	auth login
o	--auth-code	2FA code for the Apple ID	v
o	-e|--email	Apple ID email address	
o	-p|--password	Apple ID password	
@	auth revoke
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	completion bash
@	completion fish
@	completion powershell
@	completion zsh
@	download
o	-b|--bundle-identifier	Bundle identifier of the app	v
o	-o|--output	The destination path of the downloaded app package	v
o	--purchase	Obtain a license for the app if needed	
=	download	-b
d
=	download	-o
t	folders
@	help
a	1	0
#	help	1
t	help
@	purchase
o	-b|--bundle-identifier	Bundle identifier of the app	v
=	purchase	-b
d
@	search
o	-l|--limit	Limit the number of results	v
a	1	0
