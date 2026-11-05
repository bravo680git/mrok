@	
s	app	App related commands
s	docs	Open Homey Developer Documentation
s	list	List all Homeys
s	login	Log in with an Athom Account
s	logout	Log out the current user
s	select	Select a Homey as active
s	tools	Open Homey Developer Tools
s	unselect	Unselect the active Homey
s	whoami	Show the current logged in user
o	--help		p
o	--version		p
@	app
s	add-types	Install the Apps SDK TypeScript declarations
s	build	Build a Homey App for publishing
s	compose	Migrate app to Homey compose
s	create	Create a new Homey App
s	discovery	Discovery related commands
s	driver	Driver related commands
s	flow	Flow related commands
s	install	Install a Homey App
s	manage	View your app in the Homey Developer Tools
s	publish	Publish a Homey App to the Homey Apps Store
s	run	Run a Homey App in development mode
s	validate	Validate a Homey App
s	version	Update a Homey App's version
s	view	View your app in the Homey Apps Store
o	-p|--path	Path to a Homey App directory	vp
=	app	-p
t	folders
@	app add-types
@	app build
@	app compose
@	app create
@	app discovery
s	create	Create a new Discovery strategy
@	app discovery create
@	app driver
s	capabilities	Change the capabilities of a Driver
s	create	Create a new Driver
s	flow	Create a new Flow for a Driver
@	app driver capabilities
@	app driver create
@	app driver flow
@	app flow
s	create	Create a new Flow
@	app flow create
@	app install
o	-c|--clean		v
o	-s|--skip-build		v
=	app install	-c
v	false	
v	true	
=	app install	-s
v	false	
v	true	
@	app manage
@	app publish
@	app run
o	-c|--clean		v
o	-s|--skip-build		v
o	-l|--link-modules	Provide a comma-separated path to local Node.js modules to link. Only works on Homey Cloud	v
=	app run	-c
v	false	
v	true	
=	app run	-s
v	false	
v	true	
@	app validate
o	-l|--level	Validation level	v
=	app validate	-l
v	debug	
v	publish	
v	verified	
@	app version
a	1	0
#	app version	1
v	patch	
v	minor	
v	major	
v	semver	
@	app view
@	docs
@	list
@	login
@	logout
@	select
o	-i|--id	ID of the Homey	v
o	-n|--name	Name of the Homey	v
@	tools
@	unselect
@	whoami
