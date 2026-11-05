@	
s	help	Display help for StepZen
s	login	Login to StepZen
s	logout	Logout of StepZen
s	start	Deploy, watch and develop your API
s	import	Import pre-configured schemas to Your API
s	list	List the assets of a specified type that are linked to the StepZen account
@	help
a	1	0
@	login
@	logout
@	start
o	--dir	The working directory for StepZen assets	v=
o	--endpoint	The folder/endpoint to deploy to	v=
o	--port	The port number to use for the GraphiQL explorer	v=
=	start	--dir
t	folders
=	start	--endpoint
d
@	import
o	--dir	The directory to which the schema will be imported	v=
a	1	0
=	import	--dir
t	folders
#	import	1
d
@	list
a	1	0
#	list	1
v	schemas	
v	configurationsets	
