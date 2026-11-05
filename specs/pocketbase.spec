@	
s	help	Help about any command
s	migrate	Executes DB migration scripts
s	serve	Starts the web server (default to 127.0.0.1:8090)
o	--debug	Enable debug mode, aka showing more detailed logs	
o	--dir	PocketBase data directory (default "pb_data")	v
o	--encryptionEnv	Environment variable whose value of 32 chars will be used as encryption key for the app settings…	v
o	-h|--help	Show help for pocketbase	
o	-v|--version	Show version for pocketbase	
=		--dir
t	folders
@	help
a	1	0
#	help	1
t	help
@	migrate
s	collections	(Experimental) Creates new migration file with the most recent local collections configuration
s	create	Creates new migration template file
s	down	Reverts the last [number] applied migrations
s	up	Runs all available migrations
@	migrate collections
a	1	0
#	migrate collections	1
t	folders
@	migrate create
a	2	0
#	migrate create	2
t	folders
@	migrate down
a	1	0
@	migrate up
@	serve
o	--http	API HTTP server address (default "127.0.0.1:8090")	v
o	--https	API HTTPS server address (auto TLS via Let's Encrypt). The incoming --http address traffic also…	v
o	--origins	CORS allowed domain origins list (default [*])	v
