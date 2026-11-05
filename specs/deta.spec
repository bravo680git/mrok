@	
s	login	Trigger the login process for the Deta CLI
s	version	Print the Deta version
s	projects	List Deta projects
s	new	Create a new Deta Micro
s	deploy	Deploy new code to a Deta Micro
s	details	Get detailed information about a specific Deta micro
s	watch	Auto-deploy locally saved changes in real time to your Deta micro
s	auth	Change auth settings for a Deta Micro
s	pull	Pull the latest deployed code of a Deta Micro to your local machine
s	clone	Clone a Deta Micro
s	update	Update a Deta Micro's name or environment variables
s	visor	Change the Visor settings for a Deta Micro
s	run	Run a Deta Micro from the CLI
s	cron	Change cron settings for a Deta Micro
o	-h	Show help for deta	
@	login
o	-h	Show help for login	
@	version
s	upgrade	Upgrade Deta CLI version
o	-h	Show help for version	
@	version upgrade
o	-h	Show help for upgrade	
o	-v	Upgrade CLI to specific version	v
@	projects
o	-h	Show help for projects	
@	new
o	-h	Show help for new	
o	-n	Create a micro with Node (node14.x) runtime	
o	-p	Create a micro with Python (python 3.9) runtime	
o	--name	Set the name of the new micro	v
o	--project	Set the project under which the micro is created	v
o	--runtime	Create a micro with a specified runtime	v
a	1	0
=	new	--runtime
v	node12	Runtime
v	node14	Runtime
v	python3.7	Runtime
v	python3.9	Runtime
@	deploy
o	-h	Show help for deploy	
a	1	0
#	deploy	1
t	folders
@	details
o	-h	Show help for details	
a	1	0
#	details	1
t	folders
@	watch
o	-h	Show help for watch	
a	1	0
#	watch	1
t	folders
@	auth
s	disable	Disable HTTP Auth for a Deta Micro
s	enable	Enable HTTP Auth for a Deta Micro
s	create-api-key	Create an API key for a Deta Micro
s	delete-api-key	Delete an API key for a Deta Micro
o	-h	Show help for auth	
@	auth disable
o	-h	Show help for auth disable	
@	auth enable
o	-h	Show help for auth enable	
@	auth create-api-key
o	-h	Show help for auth create-api-key	
o	-d	Set the api-key description	v
o	-n	Set the api-key name	v
o	-o	Set the api-key output file	v
=	auth create-api-key	-o
t	filepaths
@	auth delete-api-key
o	-h	Show help for auth delete-api-key	
o	-n	Set the api-key name	v
@	pull
o	-h	Show help for pull	
o	-f	Force the overwrite of existing files	
@	clone
o	-h	Show help for clone	
o	-n	The name of the micro to be cloned	v
o	-p	The name of the project with the micro to be cloned	v
a	1	0
@	update
o	-h	Show help for pull	
o	-n	The new name of the micro	v
o	-r	The new runtime of the micro	v
o	-e	The new env file of the micro	v
=	update	-r
v	node12	Runtime
v	node14	Runtime
v	python3.7	Runtime
v	python3.9	Runtime
=	update	-e
t	filepaths
@	visor
s	open	Open Micro's visor page in the browser
s	enable	Enable Visor for a Deta Micro
s	disable	Disable Visor for a Deta Micro
o	-h	Show help for visor	
@	visor open
o	-h	Show help for visor open	
@	visor enable
o	-h	Show help for visor enable	
@	visor disable
o	-h	Show help for visor disable	
@	run
o	-h	Show help for run	
o	-l	Show the micro logs	
a	1	0
@	cron
s	set	Set Deta Micro to run on a schedule
s	remove	Remove a schedule from a Deta Micro
o	-h	Show help for cron	
@	cron set
o	-h	Show help for cron set	
a	1	0
@	cron remove
o	-h	Show help for cron remove	
a	1	0
