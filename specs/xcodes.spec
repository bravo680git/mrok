@	
s	help	
s	download	Download a specific version of Xcode
s	install	Download and install a specific version of Xcode
s	installed	List the versions of Xcode that are installed
s	list	List all versions of Xcode available to install
s	select	Change the selected Xcode
s	uninstall	Uninstall a version of Xcode
s	update	Update the list of available versions of Xcode
s	version	Print the version number of xcodes itself
s	signout	Clears the stored username and password
o	--help|-h	Show help information	p
@	help
a	1	0
#	help	1
t	help
@	download
o	--latest	Update and then install the latest non-prerelease version available	
o	--latest-prerelease	Update and then install the latest prerelease version available, including GM seeds and GMs	
o	--aria2	The path to an aria2 executable. Searches $PATH by default	v
o	--no-aria2	Don't use aria2 to download Xcode, even if it's available	
o	--directory	The directory where your Xcodes are installed. Defaults to /Applications	v
o	--data-source	The data source for available Xcode versions. (default: xcodereleases)	v
o	--color	Color the output	
o	--no-color	Do not color the output	
a	1	0
=	download	--aria2
t	filepaths
=	download	--directory
t	folders
=	download	--data-source
v	xcodereleases	
v	apple	
#	download	1
d
@	install
o	--path	Local path to Xcode.xip	v
o	--latest	Update and then install the latest non-prerelease version available	
o	--latest-prerelease	Update and then install the latest prerelease version available, including GM seeds and GMs	
o	--aria2	The path to an aria2 executable. Searches $PATH by default	v
o	--no-aria2	Don't use aria2 to download Xcode, even if it's available	
o	--experimental-unxip	Use the experimental unxip functionality. May speed up unarchiving by up to 2-3x	
o	--directory	The directory where your Xcodes are installed. Defaults to /Applications	v
o	--data-source	The data source for available Xcode versions. (default: xcodereleases)	v
o	--color	Color the output	
o	--no-color	Do not color the output	
a	1	0
=	install	--path
t	filepaths
=	install	--aria2
t	filepaths
=	install	--directory
t	folders
=	install	--data-source
v	xcodereleases	
v	apple	
#	install	1
d
@	installed
o	--directory	The directory where your Xcodes are installed. Defaults to /Applications	v
o	--color	Color the output	
o	--no-color	Do not color the output	
=	installed	--directory
t	folders
@	list
o	--directory	The directory where your Xcodes are installed. Defaults to /Applications	v
o	--data-source	The data source for available Xcode versions. (default: xcodereleases)	v
o	--color	Color the output	
o	--no-color	Do not color the output	
=	list	--directory
t	folders
=	list	--data-source
v	xcodereleases	
v	apple	
@	select
o	-p|--print-path	Print the path of the selected Xcode	
o	--directory	The directory where your Xcodes are installed. Defaults to /Applications	v
o	--color	Color the output	
o	--no-color	Do not color the output	
a	1	0
=	select	--directory
t	folders
#	select	1
d
@	uninstall
o	--directory	The directory where your Xcodes are installed. Defaults to /Applications	v
o	--color	Color the output	
o	--no-color	Do not color the output	
a	1	0
=	uninstall	--directory
t	folders
#	uninstall	1
d
@	update
o	--directory	The directory where your Xcodes are installed. Defaults to /Applications	v
o	--data-source	The data source for available Xcode versions. (default: xcodereleases)	v
o	--color	Color the output	
o	--no-color	Do not color the output	
=	update	--directory
t	folders
=	update	--data-source
v	xcodereleases	
v	apple	
@	version
o	--color	Color the output	
o	--no-color	Do not color the output	
o	--help|-h	Show help information	
@	signout
o	--color	Color the output	
o	--no-color	Do not color the output	
