@	
s	init	Initialize an empty project with the recommended settings and dependencies
s	execute	Execute the formula and print the output to the terminal
s	auth	Set up authentication in your development environment so that you can execute Pack formulas with…
s	register	Create a new API token or register an existing one to be used with future commands
s	create	Create a new Pack on Coda’s servers and get assigned a Pack ID. Run this command just once for…
s	upload	Use this command to upload a new version of your Pack based on your latest code
s	release	Release a Pack version and make it live for your users
s	clone	Migrate the development of a Pack from the Pack Studio to a new local CLI Pack development
s	link	Link the development of a Pack from the Pack studio to an existing local CLI Pack development
s	whoami	Looks up information about the API token that is registered in this environment
s	build	Generate a bundle for your Pack
s	validate	Validate your Pack definition
s	setOption	Set a persistent build option for the Pack. This will be used for all builds of the Pack
o	--version	Show version number	p
o	--help	Show help	p
@	init
@	execute
o	--dynamicUrl	To run a sync for a dynamic sync table, use this parameter to specify which URL to sync from	v
a	3	1
#	execute	1
d
#	execute	2
d
@	auth
a	1	0
#	auth	1
d
@	register
a	1	0
@	create
o	--name	Specify a name for the Pack. You can always set or update the name in the Pack management UI later	v
o	--description	Specify a description for the Pack. You can always set or update the description in the Pack…	v
a	1	0
#	create	1
d
@	upload
a	1	0
#	upload	1
d
@	release
a	2	0
#	release	1
d
@	clone
a	1	0
@	link
a	2	0
#	link	1
d
@	whoami
a	1	0
@	build
a	1	0
#	build	1
d
@	validate
a	1	0
#	validate	1
d
@	setOption
a	3	0
#	setOption	1
d
#	setOption	2
v	timerStrategy	
#	setOption	3
v	none	
v	error	
v	fake	
