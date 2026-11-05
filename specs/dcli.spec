@	
s	sync|s	Manually synchronize the local vault with Dashlane
s	read	Retrieve a secret from the local vault via its path
s	exec	Execute a command with secrets injected into the environment variables (-- <command>)
s	inject	Inject secrets into a templated string or file (uses stdin and stdout by default)
s	password|p	Retrieve a password from the local vault and copy it to the clipboard
s	otp|o	Retrieve an OTP code from local vault and copy it to the clipboard
s	note|n	Retrieve a secure note from the local vault and open it
s	accounts|a	Manage your accounts connected to the CLI
s	devices|d	Operations on devices
s	team|t	Team related commands
s	configure|c	Configure the CLI
s	backup	Backup your local vault (will use the current directory by default)
s	logout	Logout and clean your local database and OS keychain
s	help	Display help for command
o	-h|--help	Display help for command	p
o	-V|--version	Output the version number	
o	--debug	Print debug messages	p
@	sync
@	read
a	1	0
@	exec
a	1	0
@	inject
o	-i|--in	Input file of a template to inject the credential into	v
o	-o|--out	Output file to write the injected template to	v
=	inject	-i
t	filepaths
=	inject	-o
t	filepaths
@	password
o	-o|--output	How to print the passwords. The JSON option outputs all the matching credentials	v
a	1	1
=	password	-o
v	clipboard	
v	password	
v	json	
@	otp
o	--print	Prints just the OTP code, instead of copying it to the clipboard	
a	1	1
@	note
o	-o|--output	How to print the notes. The JSON option outputs all the matching notes	v
a	1	1
=	note	-o
v	text	
v	json	
@	accounts
s	whoami	Prints the login email of the account currently in use
s	help	Display help for command
@	accounts whoami
@	accounts help
a	1	0
#	accounts help	1
t	help
@	devices
s	list	Lists all registered devices that can access your account
s	remove	De-registers a list of devices. De-registering the CLI will implies doing a "dcli logout"
s	register	Registers a new device to be used in non-interactive mode
s	help	Display help for command
@	devices list
o	--json	Output in JSON format	
@	devices remove
o	--all	Remove all devices including this one (dangerous)	
o	--others	Remove all other devices	
a	1	1
#	devices remove	1
d
@	devices register
o	--json	Output in JSON format	
a	1	0
@	devices help
a	1	0
#	devices help	1
t	help
@	team
s	credentials|c	Team credentials operations
s	members|m	List team members
s	logs|l	List audit logs
s	report|r	Get team report
s	help	Display help for command
@	team credentials
s	generate	Generate new team credentials
s	list	List all team credentials
s	revoke	Revoke credentials by access key
s	help	Display help for command
@	team credentials generate
o	--json	Output in JSON format	
@	team credentials list
o	--json	Output in JSON format	
@	team credentials revoke
a	1	0
#	team credentials revoke	1
d
@	team credentials help
a	1	0
#	team credentials help	1
t	help
@	team members
o	--csv	Output in CSV format	
o	--human-readable	Output dates in human readable format	
a	2	0
@	team logs
o	--start	Start timestamp in ms	v
o	--end	End timestamp in ms (use "now" to get the current timestamp)	v
o	--type	Log type	v
o	--category	Log category	v
o	--csv	Output in CSV format	
o	--human-readable	Output dates in human readable format	
@	team report
a	1	0
@	team help
a	1	0
#	team help	1
t	help
@	configure
s	disable-auto-sync	Disable automatic synchronization which is done once per hour (default: false)
s	save-master-password	Should the encrypted master password be saved and the OS keychain be used (default: true)
s	help	Display help for command
@	configure disable-auto-sync
a	1	0
#	configure disable-auto-sync	1
v	true	
v	false	
@	configure save-master-password
a	1	0
#	configure save-master-password	1
v	true	
v	false	
@	configure help
a	1	0
#	configure help	1
t	help
@	backup
o	--directory	Output directory of the backup ("." by default)	v
o	--filename	Filename of the backup ("dashlane-backup-<unix_timestamp>.db by default")	v
=	backup	--directory
t	folders
@	logout
@	help
a	1	0
#	help	1
t	help
