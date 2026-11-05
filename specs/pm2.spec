@	
s	start	Starts and daemonizes an app
s	trigger	Deploy your json
s	deploy	Deploy your json
s	startOrRestart	Start or restart JSON file
s	startOrReload	Start or gracefully reload JSON file
s	pid	Return pid of the specified app or all
s	startOrGracefulReload	Start or gracefully reolad JSON file
s	stop	Stop a process
s	restart	Restart a process
s	scale	Scale up/down a process in cluster mode depending on the `number` param
s	snapshot	Snapshot PM2 memory
s	profile	Profile CPU
s	reload	Reload processes (for apps using HTTP/HTTPS)
s	gracefulReload	Gracefully reload a process. Send a “shutdown” message to close all connections
s	id	Get process id by name
s	delete	Stops and deletes a process from pm2 process list
s	sendSignal	Send a system signal to the target process
s	ping	Ping pm2 daemon - if not it will launch up
s	updatePM2	Update in-memory PM2 with local PM2
s	update	(alias) update in-memory PM2 with local PM2
s	install|module:install	Install or update a module and run it forever
s	module:generate	Generate a sample module in current folder
s	uninstall|module:uninstall	Stop and uninstall a module
s	publish|module:publish	Publish the module you are currently on
s	set	Sets the specified config
s	multiset	Multiset eg `key1 val1 key2 val2`
s	get	Get value for the specified key
s	conf	Get / set module config values
s	config	Get / set module config values
s	unset	Clears the specified config key
s	report	Give a full pm2 report for https://github.com/Unitech/pm2/issues
s	link|interact	Linking action to keymetrics.io
s	unlink	Linking action to keymetrics.io
s	unmonitor	Unmonitor target process
s	monitor	<Unm>onitor target process
s	open	Open dashboard in browser
s	register	Create an account on keymetrics
s	login	Login to keymetrics and link current PM2
s	web	Launch a health API on 0.0.0.0:9615
s	dump|save	Dump all processes for resurrecting them later
s	send	Send stdin to pm id
s	attach	Attach stdin/stdout to application identified by pm id
s	resurrect	Resurrect previously dumped processes
s	unstartup	Disable and clear auto startup
s	startup	Setup script for pm2 at boot
s	logrotate	Copy default logrotate configuration
s	ecosystem|init	Generate a process conf file
s	reset	Reset counters for process
s	describe	Describe all parameters of a process id
s	desc|info|show	(alias) Describe all parameters of a process id
s	list|ls	List all processes
s	l|ps|status	(alias) list all processes
s	jlist	List all processes in JSON format
s	prettylist	Print json in a prettified JSON
s	monit	Launch termcaps monitoring
s	imonit	Launch legacy termcaps monitoring
s	dashboard|dash	Launch dashboard with monitoring and logs
s	flush	Flush logs
s	reloadLogs	Reload all logs
s	logs	Stream logs logs file
s	kill	Kill daemon
s	pull	Updates repository for a given app
s	forward	Updates repository to the next commit for a given app
s	backward	Downgrades repository to the previous commit for a given app
s	gc	Force PM2 to trigger garbage collection
s	deepUpdate	Performs a deep update of PM2
s	serve|expose	Serves a directory over http via port
o	-V|--version	Outputs the version number	
o	-v	Gets version	
o	-s|--silent	Hides all messages	
o	-m|--mini-list	Displays a compacted list without formatting	
o	-f|--force	Forces actions	
o	--disable-logs	Do not write logs	
o	-n|--name	Sets a name for script	v
o	-i|--instances	Launches [number] instances (for networked app)(load balanced)	v
o	--parallel	Number of parallel actions (for restart/reload)	v
o	-l|--log	Specifies entire log file (error and out are both included)	V
o	-o|--output	Specifies out log file	v
o	-e|--error	Specifies error log file	v
o	-p|--pid	Specify pid file	v
o	-k|--kill-timeout	Delays before sending final SIGKILL signal to process	v
o	--listen-timeout	Listen timeout on application reload	v
o	--max-memory-restart	Specify max memory amount used to autorestart (in octet or use syntax like 100M)	v
o	--restart-delay	Specify a delay between restarts (in milliseconds)	v
o	--env	Specify environment to get specific env variables	v
o	--log-type	Specify log output style (raw by default, json optional)	v
o	-x|--execute-command	Execute a program using fork system	
o	--max-restarts	Only Restart the script COUNT times	V
o	-u|--user	Defines user when generating startup script	v
o	--uid	Runs target script with <uid> rights	v
o	--gid	Runs target script with <gid> rights	v
o	--cwd	Runs target script as <username>	v
o	--hp	Defines home path when generating startup script	v
o	--wait-ip	Overrides systemd script to wait for full internet connectivity to launch pm2	
o	--service-name	Defines service name when generating startup script	v
o	-c|--cron	Restarts a running process based on a cron pattern	v
o	-w|--write	Writes configuration in local folder	
o	--interpreter	The interpreter pm2 should use for executing app (bash, python…)	v
o	--interpreter-args	Interprets options (alias of –node-args)	v
o	--log-date-format	Adds custom prefix timestamp to logs	v
o	--no-daemon	Runs pm2 daemon in the foreground if it doesn’t exist already	
o	-a|--update-env	Updates environment on restart/reload (-a <=> apply)	
o	–-source-map-support	Force source map support	
o	–-only	With json declaration, allow to only act on one application	v
o	–-disable-source-map-support	Force source map support	
o	–-wait-ready	Asks pm2 to wait for ready event from your app	
o	–-merge-logs	Merges logs from different instances but keep error and out separated	
o	–-watch	Watches application folder for changes (default: )	v
o	–-ignore-watch	Folder/files to be ignored watching	v
o	–-node-args	Space delimited arguments to pass to node in cluster mode	v
o	–-no-color	Skip colors	
o	–-no-vizion	Starts an app without vizion feature (versioning control)	
o	–-no-autorestart	Starts an app without automatic restart	
o	–-no-treekill	Only kills the main process, not detached children	
o	–-no-pmx	Starts an app without apm	
o	–-no-automation	Starts an app without apm	
o	–-trace	Enables transaction tracing with km	
o	–-disable-trace	Disables transaction tracing with km	
o	–-attach	Attaches logging after your start/restart/stop/reload	
o	–-sort	Sort process according to field’s name	v
o	–-v8	Enables v8 data collecting	
o	–-event-loop-inspector	Enables event-loop-inspector dump in apm	
o	–-deep-monitoring	Enables all monitoring tools (equivalent to –v8 –event-loop-inspector –trace)	
o	-h|–-help	Outputs usage information	
=		-l
t	filepaths
=		-o
t	filepaths
=		-e
t	filepaths
=		-p
t	filepaths
=		--cwd
t	filepaths
=		--hp
t	folders
=		–-watch
t	folders
=		–-ignore-watch
t	folders,filepaths
@	start
o	-V|--version	Outputs the version number	
o	-v	Gets version	
o	-s|--silent	Hides all messages	
o	-m|--mini-list	Displays a compacted list without formatting	
o	-f|--force	Forces actions	
o	--disable-logs	Do not write logs	
o	-n|--name	Sets a name for script	v
o	-i|--instances	Launches [number] instances (for networked app)(load balanced)	v
o	--parallel	Number of parallel actions (for restart/reload)	v
o	-l|--log	Specifies entire log file (error and out are both included)	V
o	-o|--output	Specifies out log file	v
o	-e|--error	Specifies error log file	v
o	-p|--pid	Specify pid file	v
o	-k|--kill-timeout	Delays before sending final SIGKILL signal to process	v
o	--listen-timeout	Listen timeout on application reload	v
o	--max-memory-restart	Specify max memory amount used to autorestart (in octet or use syntax like 100M)	v
o	--restart-delay	Specify a delay between restarts (in milliseconds)	v
o	--env	Specify environment to get specific env variables	v
o	--log-type	Specify log output style (raw by default, json optional)	v
o	-x|--execute-command	Execute a program using fork system	
o	--max-restarts	Only Restart the script COUNT times	V
o	-u|--user	Defines user when generating startup script	v
o	--uid	Runs target script with <uid> rights	v
o	--gid	Runs target script with <gid> rights	v
o	--cwd	Runs target script as <username>	v
o	--hp	Defines home path when generating startup script	v
o	--wait-ip	Overrides systemd script to wait for full internet connectivity to launch pm2	
o	--service-name	Defines service name when generating startup script	v
o	-c|--cron	Restarts a running process based on a cron pattern	v
o	-w|--write	Writes configuration in local folder	
o	--interpreter	The interpreter pm2 should use for executing app (bash, python…)	v
o	--interpreter-args	Interprets options (alias of –node-args)	v
o	--log-date-format	Adds custom prefix timestamp to logs	v
o	--no-daemon	Runs pm2 daemon in the foreground if it doesn’t exist already	
o	-a|--update-env	Updates environment on restart/reload (-a <=> apply)	
o	–-source-map-support	Force source map support	
o	–-only	With json declaration, allow to only act on one application	v
o	–-disable-source-map-support	Force source map support	
o	–-wait-ready	Asks pm2 to wait for ready event from your app	
o	–-merge-logs	Merges logs from different instances but keep error and out separated	
o	–-watch	Watches application folder for changes (default: )	v
o	–-ignore-watch	Folder/files to be ignored watching	v
o	–-node-args	Space delimited arguments to pass to node in cluster mode	v
o	–-no-color	Skip colors	
o	–-no-vizion	Starts an app without vizion feature (versioning control)	
o	–-no-autorestart	Starts an app without automatic restart	
o	–-no-treekill	Only kills the main process, not detached children	
o	–-no-pmx	Starts an app without apm	
o	–-no-automation	Starts an app without apm	
o	–-trace	Enables transaction tracing with km	
o	–-disable-trace	Disables transaction tracing with km	
o	–-attach	Attaches logging after your start/restart/stop/reload	
o	–-sort	Sort process according to field’s name	v
o	–-v8	Enables v8 data collecting	
o	–-event-loop-inspector	Enables event-loop-inspector dump in apm	
o	–-deep-monitoring	Enables all monitoring tools (equivalent to –v8 –event-loop-inspector –trace)	
o	-h|–-help	Outputs usage information	
a	1	0
=	start	-l
t	filepaths
=	start	-o
t	filepaths
=	start	-e
t	filepaths
=	start	-p
t	filepaths
=	start	--cwd
t	filepaths
=	start	--hp
t	folders
=	start	–-watch
t	folders
=	start	–-ignore-watch
t	folders,filepaths
@	trigger
a	3	0
@	deploy
a	1	0
#	deploy	1
t	filepaths
@	startOrRestart
a	1	0
#	startOrRestart	1
d
@	startOrReload
a	1	0
#	startOrReload	1
d
@	pid
a	1	0
@	startOrGracefulReload
a	1	0
#	startOrGracefulReload	1
d
@	stop
o	-V|--version	Outputs the version number	
o	-v	Gets version	
o	-s|--silent	Hides all messages	
o	-m|--mini-list	Displays a compacted list without formatting	
o	-f|--force	Forces actions	
o	--disable-logs	Do not write logs	
o	-n|--name	Sets a name for script	v
o	-i|--instances	Launches [number] instances (for networked app)(load balanced)	v
o	--parallel	Number of parallel actions (for restart/reload)	v
o	-l|--log	Specifies entire log file (error and out are both included)	V
o	-o|--output	Specifies out log file	v
o	-e|--error	Specifies error log file	v
o	-p|--pid	Specify pid file	v
o	-k|--kill-timeout	Delays before sending final SIGKILL signal to process	v
o	--listen-timeout	Listen timeout on application reload	v
o	--max-memory-restart	Specify max memory amount used to autorestart (in octet or use syntax like 100M)	v
o	--restart-delay	Specify a delay between restarts (in milliseconds)	v
o	--env	Specify environment to get specific env variables	v
o	--log-type	Specify log output style (raw by default, json optional)	v
o	-x|--execute-command	Execute a program using fork system	
o	--max-restarts	Only Restart the script COUNT times	V
o	-u|--user	Defines user when generating startup script	v
o	--uid	Runs target script with <uid> rights	v
o	--gid	Runs target script with <gid> rights	v
o	--cwd	Runs target script as <username>	v
o	--hp	Defines home path when generating startup script	v
o	--wait-ip	Overrides systemd script to wait for full internet connectivity to launch pm2	
o	--service-name	Defines service name when generating startup script	v
o	-c|--cron	Restarts a running process based on a cron pattern	v
o	-w|--write	Writes configuration in local folder	
o	--interpreter	The interpreter pm2 should use for executing app (bash, python…)	v
o	--interpreter-args	Interprets options (alias of –node-args)	v
o	--log-date-format	Adds custom prefix timestamp to logs	v
o	--no-daemon	Runs pm2 daemon in the foreground if it doesn’t exist already	
o	-a|--update-env	Updates environment on restart/reload (-a <=> apply)	
o	–-source-map-support	Force source map support	
o	–-only	With json declaration, allow to only act on one application	v
o	–-disable-source-map-support	Force source map support	
o	–-wait-ready	Asks pm2 to wait for ready event from your app	
o	–-merge-logs	Merges logs from different instances but keep error and out separated	
o	–-watch	Watches application folder for changes (default: )	v
o	–-ignore-watch	Folder/files to be ignored watching	v
o	–-node-args	Space delimited arguments to pass to node in cluster mode	v
o	–-no-color	Skip colors	
o	–-no-vizion	Starts an app without vizion feature (versioning control)	
o	–-no-autorestart	Starts an app without automatic restart	
o	–-no-treekill	Only kills the main process, not detached children	
o	–-no-pmx	Starts an app without apm	
o	–-no-automation	Starts an app without apm	
o	–-trace	Enables transaction tracing with km	
o	–-disable-trace	Disables transaction tracing with km	
o	–-attach	Attaches logging after your start/restart/stop/reload	
o	–-sort	Sort process according to field’s name	v
o	–-v8	Enables v8 data collecting	
o	–-event-loop-inspector	Enables event-loop-inspector dump in apm	
o	–-deep-monitoring	Enables all monitoring tools (equivalent to –v8 –event-loop-inspector –trace)	
o	-h|–-help	Outputs usage information	
a	1	0
=	stop	-l
t	filepaths
=	stop	-o
t	filepaths
=	stop	-e
t	filepaths
=	stop	-p
t	filepaths
=	stop	--cwd
t	filepaths
=	stop	--hp
t	folders
=	stop	–-watch
t	folders
=	stop	–-ignore-watch
t	folders,filepaths
@	restart
o	-V|--version	Outputs the version number	
o	-v	Gets version	
o	-s|--silent	Hides all messages	
o	-m|--mini-list	Displays a compacted list without formatting	
o	-f|--force	Forces actions	
o	--disable-logs	Do not write logs	
o	-n|--name	Sets a name for script	v
o	-i|--instances	Launches [number] instances (for networked app)(load balanced)	v
o	--parallel	Number of parallel actions (for restart/reload)	v
o	-l|--log	Specifies entire log file (error and out are both included)	V
o	-o|--output	Specifies out log file	v
o	-e|--error	Specifies error log file	v
o	-p|--pid	Specify pid file	v
o	-k|--kill-timeout	Delays before sending final SIGKILL signal to process	v
o	--listen-timeout	Listen timeout on application reload	v
o	--max-memory-restart	Specify max memory amount used to autorestart (in octet or use syntax like 100M)	v
o	--restart-delay	Specify a delay between restarts (in milliseconds)	v
o	--env	Specify environment to get specific env variables	v
o	--log-type	Specify log output style (raw by default, json optional)	v
o	-x|--execute-command	Execute a program using fork system	
o	--max-restarts	Only Restart the script COUNT times	V
o	-u|--user	Defines user when generating startup script	v
o	--uid	Runs target script with <uid> rights	v
o	--gid	Runs target script with <gid> rights	v
o	--cwd	Runs target script as <username>	v
o	--hp	Defines home path when generating startup script	v
o	--wait-ip	Overrides systemd script to wait for full internet connectivity to launch pm2	
o	--service-name	Defines service name when generating startup script	v
o	-c|--cron	Restarts a running process based on a cron pattern	v
o	-w|--write	Writes configuration in local folder	
o	--interpreter	The interpreter pm2 should use for executing app (bash, python…)	v
o	--interpreter-args	Interprets options (alias of –node-args)	v
o	--log-date-format	Adds custom prefix timestamp to logs	v
o	--no-daemon	Runs pm2 daemon in the foreground if it doesn’t exist already	
o	-a|--update-env	Updates environment on restart/reload (-a <=> apply)	
o	–-source-map-support	Force source map support	
o	–-only	With json declaration, allow to only act on one application	v
o	–-disable-source-map-support	Force source map support	
o	–-wait-ready	Asks pm2 to wait for ready event from your app	
o	–-merge-logs	Merges logs from different instances but keep error and out separated	
o	–-watch	Watches application folder for changes (default: )	v
o	–-ignore-watch	Folder/files to be ignored watching	v
o	–-node-args	Space delimited arguments to pass to node in cluster mode	v
o	–-no-color	Skip colors	
o	–-no-vizion	Starts an app without vizion feature (versioning control)	
o	–-no-autorestart	Starts an app without automatic restart	
o	–-no-treekill	Only kills the main process, not detached children	
o	–-no-pmx	Starts an app without apm	
o	–-no-automation	Starts an app without apm	
o	–-trace	Enables transaction tracing with km	
o	–-disable-trace	Disables transaction tracing with km	
o	–-attach	Attaches logging after your start/restart/stop/reload	
o	–-sort	Sort process according to field’s name	v
o	–-v8	Enables v8 data collecting	
o	–-event-loop-inspector	Enables event-loop-inspector dump in apm	
o	–-deep-monitoring	Enables all monitoring tools (equivalent to –v8 –event-loop-inspector –trace)	
o	-h|–-help	Outputs usage information	
a	1	0
=	restart	-l
t	filepaths
=	restart	-o
t	filepaths
=	restart	-e
t	filepaths
=	restart	-p
t	filepaths
=	restart	--cwd
t	filepaths
=	restart	--hp
t	folders
=	restart	–-watch
t	folders
=	restart	–-ignore-watch
t	folders,filepaths
@	scale
a	2	0
@	snapshot
@	profile
a	1	0
@	reload
a	1	0
@	gracefulReload
a	1	0
@	id
a	1	0
@	delete
a	1	0
@	sendSignal
a	2	0
@	ping
@	updatePM2
@	update
@	install
o	-V|--version	Outputs the version number	
o	-v	Gets version	
o	-s|--silent	Hides all messages	
o	-m|--mini-list	Displays a compacted list without formatting	
o	-f|--force	Forces actions	
o	--disable-logs	Do not write logs	
o	-n|--name	Sets a name for script	v
o	-i|--instances	Launches [number] instances (for networked app)(load balanced)	v
o	--parallel	Number of parallel actions (for restart/reload)	v
o	-l|--log	Specifies entire log file (error and out are both included)	V
o	-o|--output	Specifies out log file	v
o	-e|--error	Specifies error log file	v
o	-p|--pid	Specify pid file	v
o	-k|--kill-timeout	Delays before sending final SIGKILL signal to process	v
o	--listen-timeout	Listen timeout on application reload	v
o	--max-memory-restart	Specify max memory amount used to autorestart (in octet or use syntax like 100M)	v
o	--restart-delay	Specify a delay between restarts (in milliseconds)	v
o	--env	Specify environment to get specific env variables	v
o	--log-type	Specify log output style (raw by default, json optional)	v
o	-x|--execute-command	Execute a program using fork system	
o	--max-restarts	Only Restart the script COUNT times	V
o	-u|--user	Defines user when generating startup script	v
o	--uid	Runs target script with <uid> rights	v
o	--gid	Runs target script with <gid> rights	v
o	--cwd	Runs target script as <username>	v
o	--hp	Defines home path when generating startup script	v
o	--wait-ip	Overrides systemd script to wait for full internet connectivity to launch pm2	
o	--service-name	Defines service name when generating startup script	v
o	-c|--cron	Restarts a running process based on a cron pattern	v
o	-w|--write	Writes configuration in local folder	
o	--interpreter	The interpreter pm2 should use for executing app (bash, python…)	v
o	--interpreter-args	Interprets options (alias of –node-args)	v
o	--log-date-format	Adds custom prefix timestamp to logs	v
o	--no-daemon	Runs pm2 daemon in the foreground if it doesn’t exist already	
o	-a|--update-env	Updates environment on restart/reload (-a <=> apply)	
o	–-source-map-support	Force source map support	
o	–-only	With json declaration, allow to only act on one application	v
o	–-disable-source-map-support	Force source map support	
o	–-wait-ready	Asks pm2 to wait for ready event from your app	
o	–-merge-logs	Merges logs from different instances but keep error and out separated	
o	–-watch	Watches application folder for changes (default: )	v
o	–-ignore-watch	Folder/files to be ignored watching	v
o	–-node-args	Space delimited arguments to pass to node in cluster mode	v
o	–-no-color	Skip colors	
o	–-no-vizion	Starts an app without vizion feature (versioning control)	
o	–-no-autorestart	Starts an app without automatic restart	
o	–-no-treekill	Only kills the main process, not detached children	
o	–-no-pmx	Starts an app without apm	
o	–-no-automation	Starts an app without apm	
o	–-trace	Enables transaction tracing with km	
o	–-disable-trace	Disables transaction tracing with km	
o	–-attach	Attaches logging after your start/restart/stop/reload	
o	–-sort	Sort process according to field’s name	v
o	–-v8	Enables v8 data collecting	
o	–-event-loop-inspector	Enables event-loop-inspector dump in apm	
o	–-deep-monitoring	Enables all monitoring tools (equivalent to –v8 –event-loop-inspector –trace)	
o	-h|–-help	Outputs usage information	
a	1	0
=	install	-l
t	filepaths
=	install	-o
t	filepaths
=	install	-e
t	filepaths
=	install	-p
t	filepaths
=	install	--cwd
t	filepaths
=	install	--hp
t	folders
=	install	–-watch
t	folders
=	install	–-ignore-watch
t	folders,filepaths
@	module:generate
a	1	0
@	uninstall
a	1	0
@	publish
@	set
a	2	0
@	multiset
a	1	1
@	get
a	1	0
@	conf
a	2	0
@	config
a	2	0
@	unset
a	1	0
@	report
@	link
o	-V|--version	Outputs the version number	
o	-v	Gets version	
o	-s|--silent	Hides all messages	
o	-m|--mini-list	Displays a compacted list without formatting	
o	-f|--force	Forces actions	
o	--disable-logs	Do not write logs	
o	-n|--name	Sets a name for script	v
o	-i|--instances	Launches [number] instances (for networked app)(load balanced)	v
o	--parallel	Number of parallel actions (for restart/reload)	v
o	-l|--log	Specifies entire log file (error and out are both included)	V
o	-o|--output	Specifies out log file	v
o	-e|--error	Specifies error log file	v
o	-p|--pid	Specify pid file	v
o	-k|--kill-timeout	Delays before sending final SIGKILL signal to process	v
o	--listen-timeout	Listen timeout on application reload	v
o	--max-memory-restart	Specify max memory amount used to autorestart (in octet or use syntax like 100M)	v
o	--restart-delay	Specify a delay between restarts (in milliseconds)	v
o	--env	Specify environment to get specific env variables	v
o	--log-type	Specify log output style (raw by default, json optional)	v
o	-x|--execute-command	Execute a program using fork system	
o	--max-restarts	Only Restart the script COUNT times	V
o	-u|--user	Defines user when generating startup script	v
o	--uid	Runs target script with <uid> rights	v
o	--gid	Runs target script with <gid> rights	v
o	--cwd	Runs target script as <username>	v
o	--hp	Defines home path when generating startup script	v
o	--wait-ip	Overrides systemd script to wait for full internet connectivity to launch pm2	
o	--service-name	Defines service name when generating startup script	v
o	-c|--cron	Restarts a running process based on a cron pattern	v
o	-w|--write	Writes configuration in local folder	
o	--interpreter	The interpreter pm2 should use for executing app (bash, python…)	v
o	--interpreter-args	Interprets options (alias of –node-args)	v
o	--log-date-format	Adds custom prefix timestamp to logs	v
o	--no-daemon	Runs pm2 daemon in the foreground if it doesn’t exist already	
o	-a|--update-env	Updates environment on restart/reload (-a <=> apply)	
o	–-source-map-support	Force source map support	
o	–-only	With json declaration, allow to only act on one application	v
o	–-disable-source-map-support	Force source map support	
o	–-wait-ready	Asks pm2 to wait for ready event from your app	
o	–-merge-logs	Merges logs from different instances but keep error and out separated	
o	–-watch	Watches application folder for changes (default: )	v
o	–-ignore-watch	Folder/files to be ignored watching	v
o	–-node-args	Space delimited arguments to pass to node in cluster mode	v
o	–-no-color	Skip colors	
o	–-no-vizion	Starts an app without vizion feature (versioning control)	
o	–-no-autorestart	Starts an app without automatic restart	
o	–-no-treekill	Only kills the main process, not detached children	
o	–-no-pmx	Starts an app without apm	
o	–-no-automation	Starts an app without apm	
o	–-trace	Enables transaction tracing with km	
o	–-disable-trace	Disables transaction tracing with km	
o	–-attach	Attaches logging after your start/restart/stop/reload	
o	–-sort	Sort process according to field’s name	v
o	–-v8	Enables v8 data collecting	
o	–-event-loop-inspector	Enables event-loop-inspector dump in apm	
o	–-deep-monitoring	Enables all monitoring tools (equivalent to –v8 –event-loop-inspector –trace)	
o	-h|–-help	Outputs usage information	
a	3	0
=	link	-l
t	filepaths
=	link	-o
t	filepaths
=	link	-e
t	filepaths
=	link	-p
t	filepaths
=	link	--cwd
t	filepaths
=	link	--hp
t	folders
=	link	–-watch
t	folders
=	link	–-ignore-watch
t	folders,filepaths
@	unlink
@	unmonitor
a	1	0
@	monitor
a	1	0
@	open
@	register
@	login
@	web
@	dump
@	send
a	2	0
@	attach
a	2	0
@	resurrect
@	unstartup
a	1	0
#	unstartup	1
v	systemd	
v	upstart	
v	launchd	
v	rcd	
@	startup
a	1	0
#	startup	1
v	systemd	
v	upstart	
v	launchd	
v	rcd	
@	logrotate
@	ecosystem
a	1	0
#	ecosystem	1
v	null	
v	simple	
@	reset
a	1	0
@	describe
a	1	0
@	desc
a	1	0
@	list
@	l
@	jlist
@	prettylist
@	monit
@	imonit
@	dashboard
@	flush
@	reloadLogs
@	logs
o	-V|--version	Outputs the version number	
o	-v	Gets version	
o	-s|--silent	Hides all messages	
o	-m|--mini-list	Displays a compacted list without formatting	
o	-f|--force	Forces actions	
o	--disable-logs	Do not write logs	
o	-n|--name	Sets a name for script	v
o	-i|--instances	Launches [number] instances (for networked app)(load balanced)	v
o	--parallel	Number of parallel actions (for restart/reload)	v
o	-l|--log	Specifies entire log file (error and out are both included)	V
o	-o|--output	Specifies out log file	v
o	-e|--error	Specifies error log file	v
o	-p|--pid	Specify pid file	v
o	-k|--kill-timeout	Delays before sending final SIGKILL signal to process	v
o	--listen-timeout	Listen timeout on application reload	v
o	--max-memory-restart	Specify max memory amount used to autorestart (in octet or use syntax like 100M)	v
o	--restart-delay	Specify a delay between restarts (in milliseconds)	v
o	--env	Specify environment to get specific env variables	v
o	--log-type	Specify log output style (raw by default, json optional)	v
o	-x|--execute-command	Execute a program using fork system	
o	--max-restarts	Only Restart the script COUNT times	V
o	-u|--user	Defines user when generating startup script	v
o	--uid	Runs target script with <uid> rights	v
o	--gid	Runs target script with <gid> rights	v
o	--cwd	Runs target script as <username>	v
o	--hp	Defines home path when generating startup script	v
o	--wait-ip	Overrides systemd script to wait for full internet connectivity to launch pm2	
o	--service-name	Defines service name when generating startup script	v
o	-c|--cron	Restarts a running process based on a cron pattern	v
o	-w|--write	Writes configuration in local folder	
o	--interpreter	The interpreter pm2 should use for executing app (bash, python…)	v
o	--interpreter-args	Interprets options (alias of –node-args)	v
o	--log-date-format	Adds custom prefix timestamp to logs	v
o	--no-daemon	Runs pm2 daemon in the foreground if it doesn’t exist already	
o	-a|--update-env	Updates environment on restart/reload (-a <=> apply)	
o	–-source-map-support	Force source map support	
o	–-only	With json declaration, allow to only act on one application	v
o	–-disable-source-map-support	Force source map support	
o	–-wait-ready	Asks pm2 to wait for ready event from your app	
o	–-merge-logs	Merges logs from different instances but keep error and out separated	
o	–-watch	Watches application folder for changes (default: )	v
o	–-ignore-watch	Folder/files to be ignored watching	v
o	–-node-args	Space delimited arguments to pass to node in cluster mode	v
o	–-no-color	Skip colors	
o	–-no-vizion	Starts an app without vizion feature (versioning control)	
o	–-no-autorestart	Starts an app without automatic restart	
o	–-no-treekill	Only kills the main process, not detached children	
o	–-no-pmx	Starts an app without apm	
o	–-no-automation	Starts an app without apm	
o	–-trace	Enables transaction tracing with km	
o	–-disable-trace	Disables transaction tracing with km	
o	–-attach	Attaches logging after your start/restart/stop/reload	
o	–-sort	Sort process according to field’s name	v
o	–-v8	Enables v8 data collecting	
o	–-event-loop-inspector	Enables event-loop-inspector dump in apm	
o	–-deep-monitoring	Enables all monitoring tools (equivalent to –v8 –event-loop-inspector –trace)	
o	-h|–-help	Outputs usage information	
a	1	0
=	logs	-l
t	filepaths
=	logs	-o
t	filepaths
=	logs	-e
t	filepaths
=	logs	-p
t	filepaths
=	logs	--cwd
t	filepaths
=	logs	--hp
t	folders
=	logs	–-watch
t	folders
=	logs	–-ignore-watch
t	folders,filepaths
@	kill
@	pull
a	2	0
@	forward
a	1	0
@	backward
a	1	0
@	gc
@	deepUpdate
@	serve
a	2	0
