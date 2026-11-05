@	
s	auth	Authenticate with Hop
s	deploy	Deploy a new container
s	help	Prints this message or the help of the given subcommand(s)
s	ignite	Interact with Ignite containers
s	link	Link an existing deployment to a hopfile
s	projects	Interact with projects
s	whoami	Get information about the current user
o	--help|-h	Prints help information	
o	--version|-v	Prints version information	
o	--project|-p	Namespace or ID of the project to use	
@	auth
s	help	Prints this message or the help of the given subcommand(s)
s	login	Login to Hop
s	logout	Logout the current user
@	auth help
@	auth login
@	auth logout
@	deploy
o	--type|-t	Type of the container, defaults to `ephemeral`	v
o	--containers|-i	Number of containers to use, defaults to 1 if `scaling` is manual	v
o	--cpu|-c	The number of CPUs to use, defaults to 1	v
o	--env|-e	Environment variables to set, in the form of KEY=VALUE	v
o	--name|-n	Name of the deployment, defaults to the directory name	v
o	--project|-p	Namespace or ID of the project to use	V
o	--ram|-m	Amount of RAM to use, defaults to 512MB	v
o	--scaling|-s	Scaling strategy, defaults to `manual`	v
a	1	0
=	deploy	--type
v	ephemeral	
v	persistent	
=	deploy	--containers
v	1	
v	2	
v	4	
v	8	
v	10	
=	deploy	--cpu
v	1	
v	2	
v	4	
v	8	
=	deploy	--env
v	port=	
=	deploy	--ram
v	128MB	
v	256MB	
v	512MB	
v	1G	
v	2G	
v	4G	
=	deploy	--scaling
v	manual	
v	autoscale	
@	help
a	1	0
#	help	1
t	help
@	ignite
s	ls	List all deployments
s	rm	Delete a deployment
@	ignite ls
o	--project|-p	Namespace or ID of the project to use	
@	ignite rm
o	--project|-p	Namespace or ID of the project to use	
@	link
@	projects
s	info	Get information about a project
s	ls	List all projects that you're authorized to
s	new	Create a new project
s	rm	Delete a project
s	switch	Switch to a different project
@	projects info
@	projects ls
@	projects new
@	projects rm
@	projects switch
@	whoami
