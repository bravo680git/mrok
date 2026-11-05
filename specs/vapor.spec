@	
s	build	Builds an app in the console
s	new	Generates a new app
s	clean	Cleans temporary files
s	heroku	Commands for working with Heroku
s	run	Runs an app from the console. Equivalent to `swift run --enable-test-discovery Run`
s	supervisor	Commands for working with Supervisord
s	xcode	Opens an app in Xcode
o	--help|-h	Show help for vapor	v
=		--help
v	clean	
v	heroku	
v	new	
v	run	
v	supervisor	
v	xcode	
v	build	
@	build
@	new
o	--template|-T	The URL of a Git repository to use as a template	
o	--branch	Template repository branch to use	
o	--output|-o	The directory to place the new project in	
o	--no-commit	Skips adding a first commit to the newly created repo	
a	1	0
@	clean
o	--update|-u	Delete Package.resolved file if it exists	
o	--global|-g	Clean Xcode's global DerivedData cache	
o	--swiftpm|-s	Delete .swiftpm folder	
@	heroku
s	init	Configures app for deployment to Heroku
s	push	Deploys app to Heroku
@	heroku init
@	heroku push
@	run
@	supervisor
s	init	Creates a Supervisor entry for the current project
s	restart	Restarts current project in Supervisor
s	update	Updates Supervisor entry for current project
@	supervisor init
@	supervisor restart
@	supervisor update
@	xcode
