@	
s	config	Set configuration for FVM
s	dart	Proxies Dart commands
s	doctor	Shows information about environment, and project configuration
s	flavor	Switches between different project flavors
s	flutter	Proxies Flutter commands
s	global	Sets Flutter SDK version as global
s	install	Installs Flutter SDK version
s	list	Lists installed Flutter SDK versions
s	releases	View all Flutter SDK releases available for install
s	remove	Removes Flutter SDK version
s	spawn	Spawn a Flutter SDK version command
s	use	Sets a Flutter SDK version to be used in a project
o	-h|--help	Print this usage information	
o	--verbose	Print verbose output	
o	--version	Current FVM version	
@	config
o	-h|--help	Print this usage information	
o	-c|--cache-path	Set the path which FVM will cache the version. Priority over FVM_HOME	v
o	-s|--skip-setup|--no-skip-setup	Skip setup after a version install	
o	-g|--git-cache|--no-git-cache	ADVANCED: Will cache a local version of Flutter repo for faster version install	
=	config	-c
t	filepaths
@	dart
@	doctor
@	flavor
a	1	0
@	flutter
@	global
a	1	0
@	install
o	-h|--help	Print this usage information	
o	-s|--skip-setup	Skips Flutter setup after install	
a	1	0
#	install	1
v	stable	Latest stable release of Flutter
v	beta	Latest beta release of Flutter
v	dev	Latest dev release of Flutter (master)
d
@	list
o	-h|--help	Print this usage information	
@	releases
o	-h|--help	Print this usage information	
@	remove
o	-h|--help	Print this usage information	
o	--force	Skips version global check	
a	1	0
@	spawn
a	1	0
@	use
o	-h|--help	Print this usage information	
o	-f|--force	Skips command guards that does Flutter project checks	
o	-p|--pin	If version provided is a channel. Will pin the latest release of the channel	
o	--flavor	Sets version for a project flavor	
a	1	0
