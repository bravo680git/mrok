@	
s	clock	Returns the current clock value for a watched root
s	find	Finds all files that match the optional list of patterns under the specified dir
s	flush-subscriptions	This is designed to be used by interactive programs that have a background process or daemon…
s	get-config	Returns the .watchmanconfig for the root
s	get-sockname	Get socket path
s	list-capabilities	Returns the full list of supported capabilities offered by the watchman server
s	log	Generates a log line in the watchman log
s	log-level	Changes the log level of your connection to the watchman service
s	query	Executes a query against the specified root
s	shutdown-server	This causes your watchman service to exit with a normal status code
s	since	Finds all files that were modified since the specified clockspec that match the optional list of…
s	state-enter	This causes a watch to be marked as being in a particular named state
s	state-leave	This causes a watch to no longer be marked as being in a particular named state
s	subscribe	Subscribes to changes against a specified root and requests that they be sent to the client via…
s	trigger	This will create or replace a trigger
s	trigger-del	Deletes a named trigger from the list of registered triggers
s	trigger-list	Returns the set of registered triggers associated with a root directory
s	unsubscribe	Cancels a named subscription against the specified root
s	version	The version and build information for the currently running watchman service
s	watch-del	Removes a watch and any associated triggers
s	watch-del-all	Removes all watches and associated triggers
s	watch-list	Returns a list of watched dirs
s	watch-project	Requests that the project containing the requested dir is watched for changes
o	--help|-h	Show help for watchman	
o	--inetd	Spawning from an inetd style supervisor	
o	-S|--no-site-spawner	Don't use the site or system spawner	
o	-v|--version	Show version number for watchman	
o	--named-pipe-path	Specify alternate named pipe path	v=
o	-u	Specify alternate unix domain socket path	v
o	--unix-listener-path	Specify alternate unix domain socket path	v=
o	-o	Specify the path to logfile	v
o	--logfile	Specify the path to logfile	v=
o	--log-level	Set the log level	v
o	--pidfile	Specify path to pidfile	
o	-p|--persistent	Persist and wait for further responses	
o	-n|--no-save-state	Don't save state between invocations	
o	--statefile	Specify path to file to hold watch and trigger state	v
o	-j|--json-command	Instead of parsing CLI arguments, take a single json object from stdin	
o	--output-encoding	CLI output encoding	v=
o	--server-encoding	CLI<->server encoding	v=
o	-f|--foreground	Run the service in the foreground	
o	--no-pretty	Don't pretty print JSON	
o	--no-spawn	Don't try to start the service if it is not available	
o	--no-local	When no-spawn is enabled, don't try to handle request in client mode if service is unavailable	
=		--log-level
v	0	
v	1	
v	2	
=		--output-encoding
v	json	
v	bser	
=		--server-encoding
v	bser	
v	json	
@	clock
a	1	0
#	clock	1
t	folders
@	find
a	1	1
#	find	1
t	folders
@	flush-subscriptions
@	get-config
s	path	The path to root
@	get-config path
@	get-sockname
@	list-capabilities
@	log
a	1	0
#	log	1
v	debug	
v	error	
v	off	
@	log-level
a	1	0
#	log-level	1
v	debug	
v	error	
v	off	
@	query
@	shutdown-server
@	since
a	1	0
#	since	1
t	folders
@	state-enter
@	state-leave
@	subscribe
@	trigger
a	1	0
#	trigger	1
t	folders
@	trigger-del
@	trigger-list
@	unsubscribe
@	version
@	watch-del
a	1	0
#	watch-del	1
t	folders
@	watch-del-all
@	watch-list
@	watch-project
