@	
s	add	Add credentials to the secure keystore
s	remove	Remove credentials from the secure keystore
s	list	List profiles, along with their credentials and sessions
s	rotate	Rotate credentials
s	exec	Execute a command with AWS credentials
s	export	Export AWS credentials
s	clear	Clear temporary credentials from the secure keystore
s	login	Generate a login link for the AWS Console
s	help	Show help about the command
o	--help	Show context-sensitive help (also try --help-long and --help-man)	
o	--version	Show application version	
o	--debug	Show debugging output	
@	add
a	1	0
@	remove
o	-f|--force	Force-remove the profile without a prompt	
a	1	0
#	remove	1
d
@	list
o	--profiles	Show only the profile names	
o	--sessions	Show only the session names	
o	--credentials	Show only the profiles with stored credential	
@	rotate
o	-n|--no-session	Use master credentials, no session or role used	
a	1	0
#	rotate	1
d
@	exec
o	-d|--duration	Duration of the temporary or assume-role session. Defaults to 1h	v
o	-n|--no-session	Use master credentials, no session or role used	
o	--region	The AWS region	v
o	-t|--mfa-token	The MFA token to use	v
a	2	0
#	exec	1
d
@	export
a	1	0
#	export	1
d
@	clear
a	1	0
#	clear	1
d
@	login
a	1	0
#	login	1
d
@	help
a	1	0
#	help	1
t	help
