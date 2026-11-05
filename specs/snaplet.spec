@	
s	auth	Manage auth state
s	config	Manage configuration
s	database|db	Manage preview database
s	discord|chat	Open the Snaplet Discord chat window in your browser
s	documentation|docs	Opens the Snaplet Documentation in your browser
s	project	Manage project configuration
s	proxy|dev	Start a database proxy
s	seed|gen|generate	Populates an empty database with generated data
s	snapshot|ss	Manage snapshots
s	subset|subsetting	Manage subsetting
s	team	Manage team configuration
s	upgrade	Upgrade this binary
s	completion	Generate completion script
o	--help|-h	Show help for snaplet	p
o	--version|-v	Show version number	p
@	auth
s	login|setup	Login with an access token
@	auth login
a	1	0
@	config
s	generate	Generate transform files
s	list|ls	List config variables
s	pull	Pull cloud project config to local
s	push	Push local project config to cloud
s	setup	Setup local project configuration
@	config generate
o	--dry-run		
o	--type|-t		v
=	config generate	--type
v	typedefs	
v	transform	
v	keys	
v	seed	
@	config list
@	config pull
o	--type|-t		v
=	config pull	--type
v	typedefs	
v	transform	
v	keys	
v	seed	
@	config push
o	--type|-t		v
=	config push	--type
v	typedefs	
v	transform	
v	keys	
v	seed	
@	config setup
o	--generate		
o	--no-generate		
o	--yes	Automatically accept any prompt, useful for scripts	
a	1	0
@	database
s	cache|ca	Cache a snapshot into the preview database server
s	create|c	Create a preview database from a snapshot
s	drop|delete|d	Drop a preview database
s	url|u	Show a preview database url
s	destroy|ds	Destroy the database server
s	setup|s	Create a preview database server
s	list|ls	List preview databases
@	database cache
o	--tags	Filter snapshots by tags	v
o	--latest	Select the latest snapshot captured to cache in the preview database server	
o	--clear	Remove the snapshot from the preview database server cache	
a	1	0
#	database cache	1
d
@	database create
o	--tags	Filter snapshots by tags	v
o	--latest	Restore the latest snapshot	
o	--git	Infer the database name from the current git branch	
o	--no-snapshot	Create an empty database not based on a snapshot	
o	--force	Force the database creation, it will drop and recreate the existing database if present	
a	2	0
#	database create	2
d
@	database drop
o	--git	Infer the database name from the current git branch	
a	1	0
#	database drop	1
d
@	database url
o	--git	Infer the database name from the current git branch	
a	1	0
#	database url	1
d
@	database destroy
o	--yes	Automatically accept any prompt, useful for scripts	
@	database setup
o	--region	Fly.io region where the preview database server should be created	v
=	database setup	--region
v	ams	Amsterdam, Netherlands
v	cdg	Paris, France
v	den	Denver, Colorado (US)
v	dfw	Dallas, Texas (US)
v	ewr	Secaucus, NJ (US)
v	fra	Frankfurt, Germany
v	gru	São Paulo
v	hkg	Hong Kong, Hong Kong
v	iad	Ashburn, Virginia (US)
v	jnb	Johannesburg, South Africa
v	lax	Los Angeles, California (US)
v	lhr	London, United Kingdom
v	maa	Chennai (Madras), India
v	mad	Madrid, Spain
v	mia	Miami, Florida (US)
v	nrt	Tokyo, Japan
v	ord	Chicago, Illinois (US)
v	otp	Bucharest, Romania
v	scl	Santiago, Chile
v	sea	Seattle, Washington (US)
v	sin	Singapore
v	sjc	Sunnyvale, California (US)
v	syd	Sydney, Australia
v	waw	Warsaw, Poland
v	yul	Montreal, Canada
v	yyz	Toronto, Canada
@	database list
@	discord
@	documentation
@	project
s	create	Create a new project
s	invite	Create an invite URL for this project
s	setup	Set up a project
@	project create
o	--team|-t		v
a	1	0
@	project invite
@	project setup
a	1	0
@	proxy
@	seed
o	-i|--interactive	Show interactive prompts to customise seeding	
o	-n|--entriesPerTable		v
@	snapshot
s	capture|c	Capture a new snapshot
s	create	Create a snapshot in cloud
s	list|ls	List all snapshots
s	restore|r	Restore a snapshot
s	share|upload	Share a snapshot
s	sample|s	Create a sample of a database
@	snapshot capture
o	--env|--environment	Environment to use when capturing the snapshot	v
o	-m|--message	Attach a message to the snapshot	v
o	--subset-path|--subset	Path to a subset config file	v
o	--tags	Attach tags to the snapshot	v
o	-t|--transform-mode	Transformation mode to apply to the snapshot	v
a	1	0
=	snapshot capture	--env
v	cloud	
v	local	
=	snapshot capture	--subset-path
t	filepaths
=	snapshot capture	-t
v	strict	
v	unsafe	
v	auto	
#	snapshot capture	1
t	folders
@	snapshot create
o	--json		
@	snapshot list
o	--tags	Filter snapshots by tags	v
@	snapshot restore
o	data|--no-data	Restore data on the database (skip with --no-data)	
o	schema|--no-schema	Restore schema on the database (skip with --no-schema)	
o	reset|--no-reset	Drop destination database before restoring schemas (skip with --no-reset)	
o	--tags	Filter snapshots by tags	v
o	--latest	Restore the latest snapshot	
o	-y|--yes	Performs a restore without a confirmation message	
o	--schema-only	Skip data, only restore schema	
o	--data-only	Restore data only (keep the current schema and indexes)	
a	1	0
#	snapshot restore	1
d
@	snapshot share
o	--no-encrypt	Disable encryption	
o	--tags	Filter snapshots by tags	v
o	--latest	Share the latest snapshot	
a	1	0
#	snapshot share	1
d
@	snapshot sample
o	--env|--environment	Environment to use when slicing the snapshot	v
o	--sample-config-path|--subset-path	Path to a sample config file	v
o	-f|--force	Force overwrite existing sample file	
a	1	0
=	snapshot sample	--env
v	cloud	
v	local	
=	snapshot sample	--sample-config-path
t	filepaths
#	snapshot sample	1
t	folders
@	subset
s	setup|configure|config	Configure subsetting
@	subset setup
@	team
s	create	Create a new team
@	team create
a	1	0
@	upgrade
@	completion
