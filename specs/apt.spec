@	
s	update	Update the package database
s	upgrade	Install all available upgrades
s	full-upgrade	Install available upgrades, removing currently installed packages if needed to upgrade the system…
s	install	Install package(s)
s	reinstall	Reinstall package(s)
s	remove	Remove package(s)
s	purge	Remove package(s) and their configuration files
s	autoremove|auto-remove	Remove unused packages
s	list	List packages
s	search	Search for packages
s	show	Show package details
s	satisfy	Satisfy package dependencies
s	clean	Remove downloaded package files
s	edit-sources	Edit the list of package sources
s	source	Fetch package source files
s	build-dep	Install/remove packages in an attempt to satisfy the build dependencies for a source package
s	download	Download package binary into the current directory
s	autoclean|auto-clean	Like clean, but only removes package files that can no longer be downloaded
s	changelog	Show the changelog for a package
o	-h|--help	Print help message and exit	p
o	-v|--version	Print version information and exit	p
@	update
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
@	upgrade
o	-d|--download-only	For any operation that would download packages, download them, but do nothing else	
o	--no-download	Do not download packages, attempt to use already downloaded packages	
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
a	1	1
#	upgrade	1
d
@	full-upgrade
o	-d|--download-only	For any operation that would download packages, download them, but do nothing else	
o	--no-download	Do not download packages, attempt to use already downloaded packages	
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
@	install
o	-d|--download-only	For any operation that would download packages, download them, but do nothing else	
o	--no-download	Do not download packages, attempt to use already downloaded packages	
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
o	--reinstall	Reinstall the package if it is already installed	
o	-f|--fix-broken	Attempt to fix broken packages	
a	1	1
#	install	1
d
@	reinstall
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
a	1	1
#	reinstall	1
d
@	remove
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
o	-f|--fix-broken	Attempt to fix broken packages	
a	1	1
#	remove	1
d
@	purge
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
a	1	1
#	purge	1
d
@	autoremove
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
@	list
o	--installed	List installed packages	
o	--upgradable	List upgradable packages	
@	search
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
a	1	0
@	show
a	1	0
#	show	1
d
@	satisfy
o	-d|--download-only	For any operation that would download packages, download them, but do nothing else	
o	--no-download	Do not download packages, attempt to use already downloaded packages	
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
a	1	1
#	satisfy	1
d
@	clean
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
@	edit-sources
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
@	source
o	-d|--download-only	For any operation that would download packages, download them, but do nothing else	
o	--no-download	Do not download packages, attempt to use already downloaded packages	
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
o	--compile	Compile the package to a binary using dpkg-buildpackage	
o	--only-source		
o	--host-architecture	The architecture to build for	v
a	1	1
#	source	1
d
@	build-dep
o	-d|--download-only	For any operation that would download packages, download them, but do nothing else	
o	--no-download	Do not download packages, attempt to use already downloaded packages	
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
o	--host-architecture	The architecture to build for	v
o	--only-source		
a	1	0
#	build-dep	1
d
@	download
o	-d|--download-only	For any operation that would download packages, download them, but do nothing else	
o	--no-download	Do not download packages, attempt to use already downloaded packages	
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
a	1	0
#	download	1
d
@	autoclean
o	-d|--download-only	For any operation that would download packages, download them, but do nothing else	
o	--no-download	Do not download packages, attempt to use already downloaded packages	
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
o	-s|--simulate	Simulate running this command and show it's output, without actually changing anything	
@	changelog
o	-d|--download-only	For any operation that would download packages, download them, but do nothing else	
o	--no-download	Do not download packages, attempt to use already downloaded packages	
o	-y	Assume yes to all prompts	
o	--assume-no	Assume no to all prompts	
a	1	1
#	changelog	1
d
