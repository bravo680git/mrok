@	
s	install	Install a new Node.js version
s	uninstall	Uninstall a Node.js version
s	use	Change Node.js version
s	exec	Run a command within fnm context
s	current	Print the current Node.js version
s	list|ls	List all locally installed Node.js versions
s	list-remote|ls-remote	List all remote Node.js versions
s	alias	Alias a version to a common name
s	unalias	Deletes the alias named <name>
s	completions	Print shell completions to stdout
s	default	Set a version as the default version. This is a shorthand for 'fnm alias VERSION default'
s	env	Print and set up required environment variables for fnm
s	help	Prints the help page or the help of the given subcommand(s)
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
=		--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=		--fnm-dir
t	folders
=		--log-level
v	quiet	
v	info	
v	error	
=		--version-file-strategy
v	local	
v	recursive	
@	install
o	--lts	Install latest LTS	
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
a	1	0
=	install	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	install	--fnm-dir
t	folders
=	install	--log-level
v	quiet	
v	info	
v	error	
=	install	--version-file-strategy
v	local	
v	recursive	
#	install	1
d
@	uninstall
o	--lts	Install latest LTS	
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
a	1	0
=	uninstall	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	uninstall	--fnm-dir
t	folders
=	uninstall	--log-level
v	quiet	
v	info	
v	error	
=	uninstall	--version-file-strategy
v	local	
v	recursive	
#	uninstall	1
d
@	use
o	--install-if-missing	Install the version if it isn't installed yet	
o	--lts	Install latest LTS	
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
a	1	0
=	use	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	use	--fnm-dir
t	folders
=	use	--log-level
v	quiet	
v	info	
v	error	
=	use	--version-file-strategy
v	local	
v	recursive	
#	use	1
d
@	exec
o	--using	Either an explicit version, or a filename with the version written in it	V
o	--lts	Install latest LTS	
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
a	1	1
=	exec	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	exec	--fnm-dir
t	folders
=	exec	--log-level
v	quiet	
v	info	
v	error	
=	exec	--version-file-strategy
v	local	
v	recursive	
@	current
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
=	current	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	current	--fnm-dir
t	folders
=	current	--log-level
v	quiet	
v	info	
v	error	
=	current	--version-file-strategy
v	local	
v	recursive	
@	list
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
=	list	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	list	--fnm-dir
t	folders
=	list	--log-level
v	quiet	
v	info	
v	error	
=	list	--version-file-strategy
v	local	
v	recursive	
@	list-remote
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
=	list-remote	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	list-remote	--fnm-dir
t	folders
=	list-remote	--log-level
v	quiet	
v	info	
v	error	
=	list-remote	--version-file-strategy
v	local	
v	recursive	
@	alias
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
a	2	0
=	alias	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	alias	--fnm-dir
t	folders
=	alias	--log-level
v	quiet	
v	info	
v	error	
=	alias	--version-file-strategy
v	local	
v	recursive	
#	alias	1
d
@	unalias
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
a	1	0
=	unalias	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	unalias	--fnm-dir
t	folders
=	unalias	--log-level
v	quiet	
v	info	
v	error	
=	unalias	--version-file-strategy
v	local	
v	recursive	
@	completions
o	shell	The shell syntax to use. Infers when missing	v
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
=	completions	shell
v	zsh	
v	bash	
v	fish	
v	powershell	
v	elvish	
=	completions	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	completions	--fnm-dir
t	folders
=	completions	--log-level
v	quiet	
v	info	
v	error	
=	completions	--version-file-strategy
v	local	
v	recursive	
@	default
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
a	1	0
=	default	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	default	--fnm-dir
t	folders
=	default	--log-level
v	quiet	
v	info	
v	error	
=	default	--version-file-strategy
v	local	
v	recursive	
#	default	1
d
@	env
o	--use-on-cd	Print the script to change Node versions every directory change	
o	shell	The shell syntax to use. Infers when missing	v
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
=	env	shell
v	zsh	
v	bash	
v	fish	
v	powershell	
v	elvish	
=	env	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	env	--fnm-dir
t	folders
=	env	--log-level
v	quiet	
v	info	
v	error	
=	env	--version-file-strategy
v	local	
v	recursive	
@	help
o	--help|-h	Prints help information	
o	--version|-V	Prints version information	
o	--arch	Override the architecture of the installed Node binary. Defaults to arch of fnm binary	v
o	--fnm-dir	The root directory of fnm installations	v
o	--log-level	The log level of fnm commands	v
o	--node-dist-mirror	Mirror of https://nodejs.org/dist	v
o	--version-file-strategy	Strategy for how to resolve the Node version	v
a	1	0
=	help	--arch
v	x86	
v	x64	
v	arm64	
v	armv7l	
v	ppc64le	
v	ppc64	
v	s390x	
=	help	--fnm-dir
t	folders
=	help	--log-level
v	quiet	
v	info	
v	error	
=	help	--version-file-strategy
v	local	
v	recursive	
#	help	1
t	help
