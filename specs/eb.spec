@	
s	init	Initialize a new AWS Elastic Beanstalk application
s	deploy	Deploys the application source bundle from the initialized project directory to the running…
s	abort	Abort the current running process
s	clone	Clones an environment to a new environment so that both have identical environment settings
s	open	Opens the public URL of your website in the default browser
s	list	List environments
s	printenv	Prints all the environment properties in the command window
s	ssh	Connect to a Linux Amazon EC2 instance in your environment using Secure Shell
s	use	Sets the specified environment as the default environment
@	init
o	-i|--interactive	Forces EB CLI to prompt you to provide a value for every eb init command option	
o	-k|--keyname	The name of the AWS EC2 key pair	v
o	--modules	List of child directories to initialize	
o	-p|--platform	The platform version to use	v
o	--tags	List of tags to apply to the application	v
a	1	0
@	deploy
o	-l|--label	Specify a label to use for the version that the EB CLI creates	v
o	--env-group-suffix	Group name to append to the environment name	v
o	-m|--message	The description for the application version, enclosed in double quotation marks	v
o	--modules	List of components to update. Only for Compose Environments	v
o	-p|--platform	Preprocess and validate the environment manifest and configuration files in the source bundle	
o	--source	CodeCommit repository and branch	v
o	--staged	Deploy files staged in the git index instead of the HEAD commit	
o	--timeout	The number of minutes before the command times out	v
o	--version	An existing application version to deploy	v
a	1	0
#	deploy	1
d
@	abort
@	clone
o	-n|--clone_name	Desired name for the cloned environment	v
o	-c|--cname	Desired CNAME prefix for the cloned environment	v
o	--envvars	Environment properties in a comma-separated list with the format name=value	
o	--exact	Prevents Elastic Beanstalk from updating the solution stack version for the new clone environment…	
o	--scale	The number of instances to run in the clone environment when it is launched	v
o	--tags	Tags for the resources in your environment in a comma-separated list with the format name=value	v
o	--timeout	The number of minutes before the command times out	
a	1	0
#	clone	1
d
@	open
a	1	0
#	open	1
d
@	list
o	-a|--all	List all environments from all applications	
o	-v|--verbose	Provides more detailed information about all environments, including instances	
@	printenv
a	1	0
#	printenv	1
d
@	ssh
o	-i|--instance	The ID of the instance to connect to	
o	-n|--number	The number of the instance to connect to by number	
o	-o|--keep_open	Leave port 22 open on the security group after the SSH session ends	
o	--command	Execute a shell command on the specified instance instead of starting an SSH session	
o	--custom	Specify an SSH command to use instead of 'ssh -i keyfile'. Do not include the remote user and…	
o	--setup	Change the key pair assigned to the environment's instances	
o	--force	Open port 22 to incoming traffic from 0.0.0.0/0 in the environment's security group, even if the…	
o	--timeout	Set number of minutes before the command times out	v
a	1	0
#	ssh	1
d
@	use
o	-r|--region	Change the region in which you create environments	v
o	--source	CodeCommit repository and branch	v
a	1	0
#	use	1
d
