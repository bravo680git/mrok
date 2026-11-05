@	
s	install	Download and install a <version>. Uses .nvmrc if available and version is omitted
s	uninstall	Uninstall a version
s	use	Modify PATH to use <version>. Uses .nvmrc if available and version is omitted
s	exec	Run <command> on <version>. Uses .nvmrc if available and version is omitted
s	run	Run `node` on <version> with <args> as arguments. Uses .nvmrc if available and version is omitted
s	current	Display currently activated version of Node
s	ls	List installed versions, matching a given <version> if provided
s	ls-remote	List remote versions available for install, matching a given <version> if provided
s	version	Resolve the given description to a single local version
s	version-remote	Resolve the given description to a single remote version
s	deactivate	Undo effects of `nvm` on current shell
s	alias	Show all aliases beginning with <pattern> or Set an alias named <name> pointing to <version>
s	unalias	Deletes the alias named <name>
s	install-latest-npm	Attempt to upgrade to the latest working `npm` on the current node version
s	reinstall-packages	Reinstall global `npm` packages contained in <version> to current version
s	unload	Unload `nvm` from shell
s	which	Display path to installed node version. Uses .nvmrc if available and version is omitted
s	cache	
s	set-colors	Set five text colors using format "yMeBg". Available when supported
o	--help	Show help page	
o	--version	Print out the installed version of nvm	
o	--no-colors	Suppress colored output	
@	install
o	-s	Skip binary download, install from source only	
o	--reinstall-packages-from	When installing, reinstall packages installed in <version>	v
o	--lts	When installing, only select from LTS (long-term support) versions	
o	--lts	When installing, only select from versions for a specific LTS line	v
o	--skip-default-packages	When installing, skip the default-packages file if it exists	
o	--latest-npm	After installing, attempt to upgrade to the latest working npm on the given node version	
o	--no-progress	Disable the progress bar on any downloads	
o	--alias	After installing, set the alias specified to the version specified. (same as: nvm alias <name>…	v
o	--default	After installing, set default alias to the version specified. (same as: nvm alias default <version>)	
a	1	0
=	install	--reinstall-packages-from
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
#	install	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	uninstall
o	--lts	Uninstall using automatic LTS (long-term support) alias `lts/*`, if available	
o	--lts	Uninstall using automatic alias for provided LTS line, if available	v
a	1	0
#	uninstall	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	use
o	--silent	Silences stdout/stderr output	
o	--lts	Uses automatic LTS (long-term support) alias `lts/*`, if available	
o	--lts	Uses automatic alias for provided LTS line, if available	v
a	1	0
#	use	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	exec
o	--silent	Silences stdout/stderr output	
o	--lts	Uses automatic LTS (long-term support) alias `lts/*`, if available	
o	--lts	Uses automatic alias for provided LTS line, if available	v
a	2	1
#	exec	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	run
o	--silent	Silences stdout/stderr output	
o	--lts	Uses automatic LTS (long-term support) alias `lts/*`, if available	
o	--lts	Uses automatic alias for provided LTS line, if available	v
a	2	1
#	run	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	current
@	ls
o	--no-colors	Suppress colored output	
o	--no-alias	Suppress `nvm alias` output	
a	1	0
#	ls	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	ls-remote
o	--lts	When listing, only show LTS (long-term support) versions	
o	--lts	When listing, only show versions for a specific LTS line	v
o	--no-colors	Suppress colored output	
a	1	0
#	ls-remote	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	version
a	1	0
#	version	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	version-remote
o	--lts	When listing, only show LTS (long-term support) versions	
o	--lts	When listing, only show versions for a specific LTS line	v
a	1	0
#	version-remote	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	deactivate
o	--silent	Silences stdout/stderr output	
@	alias
a	2	0
@	unalias
a	1	0
@	install-latest-npm
@	reinstall-packages
a	1	0
#	reinstall-packages	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	unload
@	which
s	current	
o	--silent	Silences stdout/stderr output when a version is omitted	
a	1	0
#	which	1
v	node	The latest version of node
v	iojs	The latest version of io.js
v	system	System-installed version of node
@	which current
@	cache
a	1	0
#	cache	1
v	dir	Display path to the cache directory for nvm
v	clear	Empty cache directory for nvm
@	set-colors
a	1	0
