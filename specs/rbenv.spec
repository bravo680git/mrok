@	
s	commands	List all available rbenv commands
s	global	Set or show the global Ruby version
s	install	Install a Ruby version using ruby-build
s	local	Set or show the local application-specific Ruby version
s	rehash	Rehash rbenv shims (run this after installing executables)
s	shell	Set or show the shell-specific Ruby version
s	uninstall	Uninstall a specific Ruby version
s	versions	List installed Ruby versions
s	whence	List all Ruby versions that contain the given executable
s	which	Display the full path to an executable
@	commands
o	--sh		
o	--no-sh		
@	global
o	--unset		
a	1	0
#	global	1
d
@	install
o	--version	Show version of ruby-build	V
a	1	0
#	install	1
d
@	local
o	--unset		
a	1	0
#	local	1
d
@	rehash
@	shell
a	1	0
#	shell	1
d
@	uninstall
o	-f	If the version does not exist, do not display an error message	v
@	versions
@	whence
@	which
a	1	0
