@	
s	devices	Device information and management commands
s	rules	Rules information and management commands
s	help	Shows a list of commands or help for one command
o	--help|-h	Show help	
o	--version|-v	Show version	
@	devices
s	upload	Upload blueprint to a device
s	logs	Stream logs from a device
s	upload-logs	Show blueprint uploading logs
s	execute	Execute command on device
s	help	Help
@	devices upload
o	--hardware-id	Hardware ID (UCM ID) of the device; can be obtained in cloud.enapter.com	v
o	--blueprint-dir	Directory which contains blueprint file	v
o	--timeout	Time to wait for blueprint uploading (default: 30s)	V
o	--help|-h	Show help	
=	devices upload	--blueprint-dir
t	filepaths
@	devices logs
o	--hardware-id	Hardware ID (UCM ID) of the device; can be obtained in cloud.enapter.com	v
o	--help|-h	Show help	
@	devices upload-logs
o	--hardware-id	Hardware ID (UCM ID) of the device; can be obtained in cloud.enapter.com	v
o	--help|-h	Show help	
@	devices execute
o	--hardware-id	Hardware ID (UCM ID) of the device; can be obtained in cloud.enapter.com	v
o	--command	Command name	v
o	--arguments	Command arguments as JSON object	v
o	--show-progress	Enable in-progress responses streaming (default: false)	
o	--help|-h	Show help	
@	devices help
@	rules
s	update	Update rule
s	logs	Stream logs from a rule
@	rules update
o	--rule-id	Rule ID; can be obtained in cloud.enapter.com	v
o	--rule-path	Path to file with rule Lua code	v
o	--execution-interval	Rule execution interval in milliseconds (default: chosen by the server)	V
o	--stdlib-version	Version of standard library used by the rule (default: chosen by the server)	V
o	--timeout	Time to wait for rule update (default: 30s)	V
o	--help|-h	Show help	
=	rules update	--rule-path
t	filepaths
@	rules logs
o	--rule-id	Rule ID; can be obtained in cloud.enapter.com	v
o	--help|-h	Show help	
@	help
a	1	0
