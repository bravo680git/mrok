@	
s	app	App commands
s	env	App environment variables
s	cluster	Cluster commands
s	certificate	Certificate commands
s	login	Login to tsuru server
s	logout	Logout from tsuru server
o	--help|-h	Show help for tsuru	
@	app
s	build	Builds a tsuru app image respecting
s	create	Creates a new app using the given name and platform
s	deploy	Deploys set of files and/or directories to tsuru server
s	grant	Allows a team to access an application
s	info	Shows information about an app
s	list	List all apps
s	log	Shows the logs of an app
s	metadata	Manage metadata for an app
s	quota	Shows the quota of an app
s	remove	Removes an app
s	restart	Restarts an application, or one of the processes of the application
s	revoke	Removes a team access to an application
s	router	Manage routers for an app
s	routes	List all routers
s	run	Runs a command inside an app
s	shell	Opens a remote shell inside unit, using the API server as a proxy
s	start	Starts an app
s	stop	Stops an application
s	swap	Swaps routing between two apps
s	unlock	Forces the removal of an application lock
s	update	Updates an app
@	app build
o	-a|--app	App name	v
o	-f|--files-only	Enables single file build into the root of the app's tree	v
o	-h|--help	Help for build	
o	-t|--tag	The image tag	
=	app build	-a
d
=	app build	-f
t	filepaths
@	app create
o	-o|--pool	Filter applications by pool	v
o	-t|--team	Team that will own the app	v
o	-p|--plan	Plan to be used by the app	v
o	-d|--description	Description of the app	
o	-g|--tag	Tag to be used by the app	
o	--router-opts	Router options	
a	2	0
=	app create	-o
d
=	app create	-t
d
=	app create	-p
d
#	app create	1
d
#	app create	2
d
@	app deploy
s	list	List information about deploys for an application
s	rebuild	Rebuild and deploy the last app image
s	rollback	Deploys an existing image for an app
o	-a|--app	App name	v
o	-f|--files-only	Enables single file deployment into the root of the app's tree	
o	-i|--image	The image to deploy in app	
o	-m|--message	A message describing this deploy	
o	--new-version	Creates a new version for the current deployment while preserving existing versions	
o	--override-old-versions	Force replace all deployed versions by this new deploy	
a	1	0
=	app deploy	-a
d
#	app deploy	1
t	filepaths
@	app deploy list
o	-a|--app	App name	v
=	app deploy list	-a
d
@	app deploy rebuild
o	-a|--app	App name	v
o	--new-version	Creates a new version for the current deployment while preserving existing versions	
o	--override-old-versions	Force replace all deployed versions by this new deploy	
=	app deploy rebuild	-a
d
@	app deploy rollback
s	update	Locks an existing image of an app
o	-a|--app	App name	v
o	--new-version	Creates a new version for the current deployment while preserving existing versions	
o	--override-old-versions	Force replace all deployed versions by this new deploy	
o	y|--yes	Answer yes to all questions	
=	app deploy rollback	-a
d
@	app deploy rollback update
o	-a|--app	App name	v
o	-d|--disable	Enables or disables the rollback on a specific image version	
o	-i|--image	The image name for an app version	
o	-r|--reason	The reason why the rollback has to be disabled	
=	app deploy rollback update	-a
d
@	app grant
o	-a|--app	App name	v
a	1	0
=	app grant	-a
d
#	app grant	1
d
@	app info
o	-a|--app	App name	v
=	app info	-a
d
@	app list
o	-n|--name	Filter applications by name	
o	-o|--pool	Filter applications by pool	v
o	-p|--platform	Filter applications by platform	v
o	-q	Display only applications name	
o	-s|--status	Filter applications by unit status. Accepts multiple values separated by commas. Possible values…	
o	-t|--team	Team that will own the app	v
o	-u|--user	Filter applications by owner	
=	app list	-o
d
=	app list	-p
d
=	app list	-t
d
@	app log
o	-a|--app	App name	v
o	-f|--follow	Follow log output	
o	-l|--lines	Number of lines to show	
o	no-data	No date information	
o	-s|--source	The log from the given source	
o	-u|--unit	The log from the given unit	
=	app log	-a
d
@	app metadata
s	get	Retrieves metadata for an application
s	set	Sets metadata for an application
s	unset	Unsets metadata for an application
@	app metadata get
o	-a|--app	App name	v
=	app metadata get	-a
d
@	app metadata set
o	-a|--app	App name	v
o	--no-restart	Do not restart the app after the metadata is set	
o	-t|--type	Metadata type: annotation or label	
a	1	1
=	app metadata set	-a
d
@	app metadata unset
o	-a|--app	App name	v
o	--no-restart	Do not restart the app after the metadata is set	
o	-t|--type	Metadata type: annotation or label	
a	1	1
=	app metadata unset	-a
d
@	app quota
s	change	Changes the limit of units that an app can have
s	view	Displays the current usage and limit of the given app
@	app quota change
o	-a|--app	App name	v
a	1	0
=	app quota change	-a
d
@	app quota view
o	-a|--app	App name	v
=	app quota view	-a
d
@	app remove
o	-a|--app	App name	v
=	app remove	-a
d
@	app restart
o	-a|--app	App name	v
o	-p|--process	Process name	
o	--version		
=	app restart	-a
d
@	app revoke
o	-a|--app	App name	v
a	1	0
=	app revoke	-a
d
#	app revoke	1
d
@	app router
s	add	Adds a router to an app
s	list	List routers for an app
s	remove	Removes a router from an app
s	update	Updates a router for an app
s	version	Manage router versions for an app
@	app router add
o	-a|--app	App name	v
o	-o|--opts	Custom options sent directly to router implementation	
a	1	0
=	app router add	-a
d
@	app router list
o	-a|--app	App name	v
=	app router list	-a
d
@	app router remove
o	-a|--app	App name	v
a	1	0
=	app router remove	-a
d
@	app router update
o	-a|--app	App name	v
o	-o|--opts	Custom options sent directly to router implementation	
=	app router update	-a
d
@	app router version
s	add	Adds a router version to an app
s	remove	Removes a router version from an app
@	app router version add
o	-a|--app	App name	v
a	1	0
=	app router version add	-a
d
@	app router version remove
o	-a|--app	App name	v
a	1	0
=	app router version remove	-a
d
@	app routes
s	rebuild	Rebuild routes for an application
@	app routes rebuild
o	-a|--app	App name	v
=	app routes rebuild	-a
d
@	app run
o	-a|--app	App name	v
o	-i|--isolated	Running in ephemeral container	
o	-o|--once	Running only one unit	
=	app run	-a
d
@	app shell
a	1	0
#	app shell	1
d
@	app start
o	-a|--app	App name	v
o	-p|--process	Process name	
o	--version	Version number	
=	app start	-a
d
@	app stop
o	-a|--app	App name	v
o	-p|--process	Process name	
o	--version	Version number	
=	app stop	-a
d
@	app swap
o	-c|--cname-only	Swap only the cname	
o	-f|--force	Force Swap among apps with different number of units or different platform	
@	app unlock
o	-a|--app	App name	v
o	-y|--assume-yes	Don't ask for confirmation	
=	app unlock	-a
d
@	app update
o	-a|--app	App name	v
o	--cpu	CPU limit for app, this will override the plan cpu value. One cpu is equivalent to 1 vCPU/Core…	
o	-d|--description	Changes description for the app	
o	-g|--tag	Add tags for the app	
o	-i|--image-reset	Forces next deploy to build app image from scratch	
o	-p|--platform	Filter applications by platform	v
o	--memory	Memory limit for app, this will override the plan memory value. You can express memory as a bytes…	
o	--no-restart	Prevent tsuru from restarting the application	
o	-o|--pool	Filter applications by pool	v
o	-p|--plan	Plan to be used by the app	v
o	-t|--team	Team that will own the app	v
=	app update	-a
d
=	app update	-p
d
=	app update	-o
d
=	app update	-p
d
=	app update	-t
d
@	env
s	get	Get environment variables from an app
s	set	Set environment variables to an app
s	unset	Unset environment variables from an app
o	-a|--app	App name	v
o	-p|--private	Private environment variables	
o	--no-restart	Don't restart the app after setting the env vars	
=	env	-a
d
@	env get
o	-a|--app	App name	v
=	env get	-a
d
@	env set
o	-a|--app	App name	v
o	-p|--private	Private environment variables	
o	--no-restart	Don't restart the app after setting the env vars	
=	env set	-a
d
@	env unset
o	-a|--app	App name	v
o	--no-restart	Don't restart the app after setting the env vars	
=	env unset	-a
d
@	cluster
s	add	Add a new cluster
s	list	List all clusters
s	remove	Remove a cluster
s	update	Update a cluster
@	cluster add
@	cluster list
@	cluster remove
@	cluster update
@	certificate
s	list	List App TLS certificates
s	set	Creates or update a TLS certificate into the specific app
s	unset	Unset a TLS certificate from a specific app
@	certificate list
@	certificate set
@	certificate unset
@	login
a	1	0
@	logout
