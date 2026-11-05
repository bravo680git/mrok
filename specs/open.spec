@	
o	-a	Specify the application to use for opening the file	v
o	-b	Specify the bundle identifier of the app to use to open the file	v
o	-D	Reveals the enclosing folder in finder	
o	-e	Opens the file with /Applications/TextEdit	
o	-t	Open the file with the default text editor	
o	-f	Read input from standard input and open the results in the default text editor	
o	-F|--fresh	Opens the application without restoring windows	
o	-W|--wait-apps	Waits until the applications exit	
o	-R|--reveal	Reveals the file(s) in the Finder instead of opening them	
o	-n|--new	Open a new instance of the application(s) even if one is already running	
o	-j|--hide	Launches the app hidden	
o	-g|--background	Do not bring the application to the foreground	
o	-h|--header	Searches header locations for a header whose name matches the given string and then opens it	
o	-s	For -h, the SDK to use; if supplied, only SDKs whose names contain the argument value are searched	v
o	-u|--url	Open this URL, even if it matches exactly a filepath	v
o	-i|--stdin	Launches the application with stdin connected to PATH; defaults to /dev/null	v
o	-o|--stdout	Launches the application with /dev/stdout connected to PATH	v
o	--stderr	Launches the application with /dev/stderr connected to PATH	v
o	--env	Add an enviroment variable to the launched process, where VAR is formatted AAA=foo	v
o	--args	All remaining arguments are passed to the opened application in the argv parameter to main()…	v
a	1	1
=		-a
d
=		-b
d
=		-i
t	filepaths
=		-o
t	filepaths
=		--stderr
t	filepaths
#		1
t	filepaths,folders
