@	
s	create	Create a new project using a planter or public repo
s	list	List available planters
s	add	Add a planter to your list
s	edit	Edit a planter in your list
s	pin	Pins a planter to the top of your list
s	info	Prints all info about a planter in your list
s	help	Display help for command
o	-V|--version	Output the version number	
o	-h|--help	Display help for command	
@	create
o	-f|--force	Force the created directory to overwrite an existing one	
o	-h|--help	Display help for command	
a	2	0
@	list
o	-a|--alphanumeric	Sorts list of planters alphanumerically	
o	-h|--help	Display help for command	
@	add
o	-L|--local	Treat the location as a local repo instead of a remote repo	
o	-h|--help	Display help for command	
a	2	0
@	edit
o	-n|--name	Edit the name of a planter	v
o	-l|--location	Edit the location of a planter	v
o	-d|--delete	Remove a planter from your list	
o	-f|--force	Edit something... dangerously. (Force the edit without any prompts.)	
o	-R|--remote	Set the location type to remote	
o	-L|--local	Set the location type to local	
o	-h|--help	Display help for command	
a	1	0
@	pin
o	-u|--unpin	Removes position from the planter	
o	-h|--help	Display help for command	
a	2	0
@	info
o	-h|--help	Display help for command	
a	1	0
@	help
a	1	0
#	help	1
t	help
