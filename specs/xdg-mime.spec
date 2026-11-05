@	
s	query	Returns information related to file types
s	default	Ask the desktop environment to make application the default application for opening files of type…
s	install	Adds the file type descriptions provided in mimetypes-file to the desktop environment
s	uninstall	Removes the file type descriptions provided in mimetypes-file and previously added with xdg-mime…
o	--help	Show command synopsis	
o	--manual	Show manual page	
o	--version	Show the xdg-utils version information	
@	query
a	1	1
#	query	1
t	filepaths
@	default
a	2	1
@	install
o	--mode		v
o	--novendor	Disables xdg-mime checks that the mimetypes-file to be installed has a proper vendor prefix	
a	1	0
=	install	--mode
v	user	
v	system	
#	install	1
t	filepaths
@	uninstall
o	--mode		v
a	1	0
=	uninstall	--mode
v	user	
v	system	
#	uninstall	1
t	filepaths
