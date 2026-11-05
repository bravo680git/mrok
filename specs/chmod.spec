@	
o	-f	Do not display a diagnostic message if chmod could not modify the mode for file, nor modify the…	
o	-H	If the -R option is specified, symbolic links on the command line are followed and hence…	
o	-h	If the file is a symbolic link, change the mode of the link itself rather than the file that the…	
o	-L	If the -R option is specified, all symbolic links are followed	
o	-P	If the -R option is specified, no symbolic links are followed. This is the default	
o	-R	Change the modes of the file hierarchies rooted in the files, instead of just the files…	
o	-v	Cause chmod to be verbose, showing filenames as the mode is modified. If the -v flag is specified…	
a	2	0
#		1
v	u+x	Give execute permission for the user
v	a+rx	Adds read and execute permissions for all classes
v	744	Sets read, write, and execute permissions for user, and sets read permission for Group and Others
v	664	Sets read and write permissions for user and Group, and provides read to Others
v	777	⚠️ allows all actions for all users
#		2
t	filepaths
