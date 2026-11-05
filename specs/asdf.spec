@	
s	plugin	Plugin management sub-commands
s	plugin-add	Add a plugin from the plugin repo OR, add a Git repo as a plugin by specifying the name and repo url
s	plugin-list	List installed plugins. Optionally show git urls and git-ref
s	plugin-list-all	List plugins registered on asdf-plugins repository with URLs
s	plugin-remove	Remove plugin and package versions
s	plugin-update	Update a plugin to latest commit on default branch or a particular git-ref
s	install	Install plugin at stated version, or all from .tools-versions
s	uninstall	Remove a specific version of a package
s	current	Display current versions for named package (else all)
s	where	Display install path for given package at optional specified version
s	which	Display path to an executable
s	local	Set package local version
s	global	Set package global version
s	shell	Set the package version to ASDF_${LANG}_VERSION` in the current shell
s	latest	Display latest version available to install for a named package
s	list	List installed versions of a package
s	list-all	List all available (remote) versions of a package
s	help	Output documentation for plugin and tool
s	exec	Executes the command shim for the current version
s	env	Prints or runs an executable under a command environment
s	info	Print os, shell and asdf debug information
s	reshim	Recreate shims for version of a package
s	shim	Shim management sub-commands
s	shim-versions	List for given command which plugins and versions provide it
s	update	Update ASDF to the latest stable release (unless --head)
s	version	Version for asdf
o	--version	Version for asdf	
o	-h|--help	Help for asdf	
@	plugin
s	add	Add a plugin from the plugin repo OR, add a Git repo as a plugin by specifying the name and repo url
s	list	List installed plugins. Optionally show git urls and git-ref
s	remove	Remove plugin and package versions
s	update	Update a plugin to latest commit on default branch or a particular git-ref
@	plugin add
a	2	0
#	plugin add	1
d
@	plugin list
s	all	List plugins registered on asdf-plugins repository with URLs
o	--urls	Show git urls	
o	--refs	Show git refs	
@	plugin list all
@	plugin remove
a	1	0
#	plugin remove	1
d
@	plugin update
o	--all	Update all plugins to latest commit on default branch	
a	2	0
@	plugin-add
a	2	0
#	plugin-add	1
d
@	plugin-list
s	all	List plugins registered on asdf-plugins repository with URLs
o	--urls	Show git urls	
o	--refs	Show git refs	
@	plugin-list all
@	plugin-list-all
@	plugin-remove
a	1	0
#	plugin-remove	1
d
@	plugin-update
o	--all	Update all plugins to latest commit on default branch	
a	2	0
@	install
a	2	0
#	install	1
d
#	install	2
v	latest	
d
@	uninstall
a	2	0
#	uninstall	1
d
#	uninstall	2
d
@	current
a	1	0
#	current	1
d
@	where
a	2	0
#	where	1
d
#	where	2
d
@	which
a	1	0
#	which	1
d
@	local
a	2	0
#	local	1
d
#	local	2
d
@	global
a	2	0
#	global	1
d
#	global	2
d
@	shell
a	2	0
#	shell	1
d
#	shell	2
d
@	latest
a	2	0
#	latest	1
d
#	latest	2
d
@	list
s	all	List all available (remote) versions of a package
a	1	0
#	list	1
d
@	list all
a	2	0
#	list all	1
d
#	list all	2
d
@	list-all
a	2	0
#	list-all	1
d
#	list-all	2
d
@	help
a	2	0
#	help	1
d
#	help	2
d
@	exec
a	1	0
#	exec	1
d
@	env
a	1	0
#	env	1
d
@	info
@	reshim
a	2	0
#	reshim	1
d
#	reshim	2
d
@	shim
s	versions	List for given command which plugins and versions provide it
@	shim versions
a	1	0
#	shim versions	1
d
@	shim-versions
a	1	0
#	shim-versions	1
d
@	update
o	--head	Using HEAD commit	
@	version
