@	
s	build	Create an optimized production build of your application
s	dev	Start the application in development mode
s	start	Start the application in production mode
s	export	Exports the application for production deployment
s	telemetry	Allows you to control Next.js' telemetry collection
o	-h|--help	Output usage information	
o	-v|--version	Output the version number	
@	build
o	--profile	Enable production profiling	
o	--debug	Enable more verbose build output	
a	1	0
#	build	1
t	folders
@	dev
o	-p|--port	A port number on which to start the application	v
o	-H|--hostname	Hostname on which to start the application	v
a	1	0
#	dev	1
t	folders
@	start
o	-p|--port	A port number on which to start the application	v
o	-H|--hostname	Hostname on which to start the application	v
a	1	0
#	start	1
t	folders
@	export
o	-s	Do not print any messages to console	
a	1	0
#	export	1
t	folders
@	telemetry
a	1	0
#	telemetry	1
v	enable	Enable Next.js' telemetry collection
v	disable	Disable Next.js' telemetry collection
