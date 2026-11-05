@	
s	query	Query the dpkg database
s	install	Install or upgrade packages
s	remove	Remove packages
s	purge	Remove packages and their configuration files
s	configure	Configure a package after installation
s	reconfigure	Reconfigure a package
s	list	List packages in the dpkg database
s	builddeb	Build Debian package files from sources
s	check	Check the dependencies of packages
s	compare-versions	Compare package versions
o	-h|--help	Help for dpkg	
@	query
o	-l|--list	List packages matching a pattern	v
o	-s|--status	Display the status of available packages	v
o	-L|--listfiles	List files in a package	v
o	-S|--search	Search for a package owning a file	v
o	-p|--print-avail	Display details about a package in the dpkg database	v
o	-W|--show	Show a package in the dpkg database	v
@	install
o	-R|--recursive	Recursively handle packages	
o	-B|--auto-deconfigure	Uninstall packages that depend on the target package	
o	--skip-same-version	Don't upgrade if the same version is already installed	
o	--force-depends	Ignore dependency problems	
o	--force-confnew	Always install the new version of configuration files	
o	--force-confold	Always install the old version of configuration files	
o	--force-confdef	Always install the default version of configuration files	
o	--force-confmiss	Always install missing configuration files	
o	--no-triggers	Skip processing triggers	
o	--no-act	Simulate the action, but don't execute	
a	1	0
@	remove
o	-R|--recursive	Recursively remove packages	
o	-B|--auto-deconfigure	Uninstall packages that depend on the target package	
o	--no-act	Simulate the action, but don't execute	
a	1	0
@	purge
o	-R|--recursive	Recursively remove packages	
o	--no-act	Simulate the action, but don't execute	
a	1	0
@	configure
o	--pending	Configure all unconfigured packages	
o	--no-triggers	Skip processing triggers	
o	--no-act	Simulate the action, but don't execute	
a	1	0
@	reconfigure
o	--no-triggers	Skip processing triggers	
o	--no-act	Simulate the action, but don't execute	
a	1	0
@	list
o	-l|--list	List packages matching a pattern	v
o	-s|--status	Display the status of available packages	v
o	-L|--listfiles	List files in a package	v
o	-S|--search	Search for a package owning a file	v
o	-p|--print-avail	Display details about a package in the dpkg database	v
o	-W|--show	Show a package in the dpkg database	v
o	--installed	List installed packages	
o	--avail	List available packages	
o	--hold	List packages on hold	
o	--deferred	List deferred packages	
@	builddeb
o	-us|--unsigned	Build unsigned .changes and .dsc files	
o	-uc|--unsigned-changes	Build unsigned .changes file	
o	-sa|--source	Build source package	
o	-rfakeroot	Use fakeroot when building the package	
o	-b|--binary	Build binary package from source	
o	--force-sign	Force signing of changes file	
o	-m|--maintainer	Specify the package maintainer	v
o	-c|--changes	Specify the changes file to use	v
o	-v|--version	Specify the version to use	v
o	--increment	Increment the version number in the changelog	
a	1	0
@	check
o	-a|--all	Check all installed packages	
o	-d|--unmet	Check for unmet dependencies	
o	-i|--check-installed	Check installed packages	
o	-U|--check-unpacked	Check unpacked packages	
o	-c|--nocheck	Skip checking for broken dependencies	
o	-r|--reverse	Check reverse dependencies	
a	1	0
@	compare-versions
a	3	0
#	compare-versions	2
v	lt	
v	le	
v	eq	
v	ne	
v	gt	
v	ge	
