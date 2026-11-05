@	
s	login	Log into a user account
s	logout	Log out of the current user account
s	lock	Lock the vault and destroy active session keys
s	unlock	Unlock the vault and return a new session key
s	sync	Pull the latest vault data from server
s	generate	Generate a password/passphrase
s	encode	Base 64 encode stdin
s	config	Configure CLI settings
s	update	Check for updates
s	completion	Generate shell completions
s	status	Show server details, last sync time & date, user information, and vault status
s	serve	Start a RESTful API webserver
s	list	Retrieves an array of objects (items, folders, collections, org-collections, org-members…
s	get	Get an object from the vault
s	create	Create an object in the vault
s	edit	Edit an object from the vault
s	delete	Delete an object from the vault
s	restore	Restores an object from the trash
s	move	Transfers a Vault item to an Organization
s	confirm	Confirm an object to the organization
s	import	Import vault data from a file
s	export	Export vault data to a CSV or JSON file
s	share	--DEPRECATED-- Move an item to an organization
s	send	Work with Bitwarden Sends. A Send can be quickly created using this command or subcommands can be…
s	device-approval	Manage device approval requests sent to organizations that use SSO with trusted devices
s	receive	Access a Bitwarden Send from a url
s	help	Display help for the Bitwarden CLI tool
o	--pretty	Format output. JSON is tabbed with two spaces	p
o	--raw	Return raw output instead of a descriptive message	p
o	--response	Return a JSON formatted version of response output	p
o	--cleanexit	Exit with a success exit code (0) unless an error is thrown	p
o	--quiet	Don't return anything to stdout	p
o	--nointeraction	Do not prompt for interactive user input	p
o	--session	Pass session key instead of reading from env	vp
o	-v|--version	Output BW CLI tool version number	
o	-h|--help	Display help for command	
@	login
o	--method	Two-step login method	v
o	--code	Two-step login code	v
o	--sso	Log in with Single-Sign On	
o	--apikey	Log in with an Api Key	
o	--passwordenv	Environment variable storing your password	v
o	--passwordfile	Path to a file containing your password as its first line	v
o	--check	Check login status	
o	-h|--help	Display help for login command	
a	2	0
=	login	--method
v	0	Authenticator
v	1	Email
v	3	YubiKey
=	login	--passwordfile
t	filepaths
@	logout
o	-h|--help	Display help for logout command	
@	lock
o	-h|--help	Display help for lock command	
@	unlock
o	--check	Check lock status	
o	--passwordenv	Supply an environment variable storing your password	v
o	--passwordfile	Path to a file containing your password as its first line	v
o	-h|--help	Display help for unlock command	
a	1	0
=	unlock	--passwordfile
t	filepaths
@	sync
o	-f|--force	Force a full sync	
o	--last	Show details of the last sync	
o	-h|--help	Display help for sync command	
@	generate
s	-p|--passphrase	Generate a passphrase
o	-u|--uppercase	Include uppercase characters	
o	-l|--lowercase	Include lowercase characters	
o	-n|--number	Include numeric characters	
o	-s|--special	Include special characters	
o	--length	Define password length	v
o	-h|--help	Display help for generate command	
@	generate -p
o	--words	Number of words to include in passphrase	v
o	-c|--capitalize	Title case passphrase	
o	--separator	Define word separator	v
o	--includeNumber	Include a number in output	
@	encode
o	-h|--help	Display help for encode command	
@	config
o	--web-vault	Provides a custom web vault URL that differs from the base URL	v
o	--api	Provides a custom API URL that differs from the base URL	v
o	--identity	Provides a custom identity URL that differs from the base URL	v
o	--icons	Provides a custom icon service URL that differs from the base URL	v
o	--notifications	Provides a custom notifications URL that differs from the base URL	v
o	--events	Provides a custom events URL that differs from the base URL	v
o	--key-connector	Provides the URL for your Key Connector server	v
o	-h|--help	Display help for the config command	
a	2	0
#	config	1
v	server	
@	update
o	-h|--help	Display help for update command	
@	completion
o	--shell	Shell to generate completions for	v
o	-h|--help	Display help for completion command	
=	completion	--shell
v	zsh	
@	status
o	-h|--help	Display help for status command	
@	serve
o	--hostname	The hostname to bind your API webserver to	v
o	--port	The port to run your API webserver on	v
o	-h|--help	Display help for serve command	
@	list
o	--search	Perform a search on the listed objects	v
o	--url	Filter items of type login with a url-match search	v
o	--folderid	Filter items by folder id	v
o	--collectionid	Filter items by collection id	v
o	--organizationid	Filter items or collections by organization id	v
o	--trash	Filter items that are in the trash	
o	-h|--help	Display help for the list command	
a	1	0
#	list	1
v	items	
v	folders	
v	collections	
v	org-collections	
v	org-members	
v	organizations	
@	get
s	template	Type of template to get
s	attachment	
o	--id	Exact id of the object	v
o	--organizationid	Organization id for an organization object	v
o	-h|--help	Display help for the get command	
a	2	0
#	get	1
v	item	
v	username	
v	password	
v	uri	
v	totp	
v	exposed	
v	folder	
v	collection	
@	get template
a	1	0
#	get template	1
v	item	
v	item.field	
v	item.login	
v	item.login.uri	
v	item.card	
v	item.identity	
v	item.securenote	
v	folder	
v	collection	
v	item-collections	
v	org-collection	
v	send.text	
v	send.file	
@	get attachment
o	--itemid	Vault Item ID containing attachment	v
o	--output	Output directory and/or filename	v
=	get attachment	--output
t	folders
@	create
o	--file	Path to file for attachment	v
o	--itemid	Attachment's item id	v
o	--organizationid	Organization id for an organization object	v
o	-h|--help	Display help for the create command	
a	2	0
=	create	--file
t	filepaths
#	create	1
v	item	
v	attachment	
v	folder	
v	org-collection	
@	edit
o	--organizationid	Organization id for an organization object	v
o	-h|--help	Display help for the edit command	
a	3	0
#	edit	1
v	item	
v	item-collections	
v	folder	
v	org-collection	
@	delete
o	--itemid	Attachment's item id	v
o	--organizationid	Organization id for an organization object	v
o	-p|--permanent	Permanently deletes the item instead of soft-deleting it (item only)	
o	-h|--help	Display help for the delete command	
a	2	0
#	delete	1
v	item	
v	attachment	
v	folder	
v	org-collection	
@	restore
o	-h|--help	Display help for the restore command	
a	2	0
@	move
o	-h|--help	Display help for the move command	
a	3	0
@	confirm
o	--organizationid	Organization id for an organization object	v
o	-h|--help	Display help for the confirm command	
a	2	0
@	import
o	--formats	List supported file formats	
o	--organizationid	ID of the organization to import to	v
o	-h|--help	Display help for the import command	
a	2	0
#	import	1
v	1password1pif	
v	1password1pux	
v	1passwordmaccsv	
v	1passwordwincsv	
v	ascendocsv	
v	avastcsv	
v	avastjson	
v	aviracsv	
v	bitwardencsv	
v	bitwardenjson	
v	blackberrycsv	
v	blurcsv	
v	buttercupcsv	
v	chromecsv	
v	clipperzhtml	
v	codebookcsv	
v	dashlanecsv	
v	dashlanejson	
v	encryptrcsv	
v	enpasscsv	
v	enpassjson	
v	firefoxcsv	
v	fsecurefsk	
v	gnomejson	
v	kasperskytxt	
v	keepass2xml	
v	keepassxcsv	
v	keepercsv	
v	lastpasscsv	
v	logmeoncecsv	
v	meldiumcsv	
v	msecurecsv	
v	mykicsv	
v	nordpasscsv	
v	operacsv	
v	padlockcsv	
v	passboltcsv	
v	passkeepcsv	
v	passmanjson	
v	passpackcsv	
v	passwordagentcsv	
v	passwordbossjson	
v	passworddragonxml	
v	passwordwallettxt	
v	pwsafexml	
v	remembearcsv	
v	roboformcsv	
v	safaricsv	
v	safeincloudxml	
v	saferpasscsv	
v	securesafecsv	
v	splashidcsv	
v	stickypasswordxml	
v	truekeycsv	
v	upmcsv	
v	vivaldicsv	
v	yoticsv	
v	zohovaultcsv	
#	import	2
t	filepaths
@	export
o	--output	Set output directory or filename	v
o	--format	Export file format	v
o	--password	Use a password to encrypt instead of your Bitwarden account encryption key. Only applies to the…	V
o	--organizationid	Enter organization id for an organization	v
o	-h|--help	Display help for the export command	
=	export	--output
t	folders
=	export	--format
v	csv	
v	json	
v	encrypted_json	
@	share
o	-h|--help	Display help for the share command	
a	3	0
@	send
s	list	List all the Sends owned by you
s	template	Get json templates for Send objects
s	get	Get Sends owned by you
s	receive	Access a Bitwarden Send from a url
s	create	Create a Send
s	edit	Edit a Send
s	remove-password	Removes the saved password from a Send
s	delete	Delete a Send
s	help	Display help for the Send command
o	-f|--file	Specifies that <data> is a filepath	
o	-d|--deleteInDays	The number of days in the future to set deletion date (defaults to 7 if not specified)	V
o	-a|--maxAccessCount	The max number of accesses allowed for this Send	v
o	--hidden	Hide <data> in web by default. Valid only if --file is not set	
o	-n|--name	The name of the Send. Defaults to a guid for text Sends and the filename for files	v
o	--notes	Notes to add to the Send	v
o	--fullObject	Specifies that the full Send object should be returned rather than just the access url	
o	-h|--help	Display help for the Send command	
a	1	0
@	send list
o	-h|--help	Display help for the Send command	
@	send template
o	-h|--help	Display help for the template sub-command	
a	1	0
#	send template	1
v	send.text	
v	send.file	
@	send get
o	--output	Output directory or filename for attachment	v
o	--text	Specifies to return the text content of a Send	
o	-h|--help	Display help for the Send get sub-command	
a	1	0
=	send get	--output
t	folders
@	send receive
o	--password	Password needed to access the Send	v
o	--passwordenv	Environment variable storing the Send's password	v
o	--passwordfile	Path to a file containing the Send's password as its first line	v
o	--obj	Return the Send's json object rather than the Send's content	
o	--output	Specify a file path to save a File-type Send to	v
o	-h|--help	Display help for the receive sub-command	
a	1	0
=	send receive	--passwordfile
t	filepaths
=	send receive	--output
t	folders
@	send create
o	--file	File to Send. Can also be specified in parent's JSON	v
o	--text	Text to Send. Can also be specified in parent's JSON	v
o	--hidden	Text hidden flag. Valid only with the --text option	
o	--password	Optional password to access this Send. Can also be specified in JSON	v
o	-h|--help	Display help for the create sub-command	
a	1	0
=	send create	--file
t	filepaths
@	send edit
o	--itemid	Overrides the itemId provided in [encodedJson]	v
o	-h|--help	Display help for the edit sub-command	
a	1	0
@	send remove-password
o	-h|--help	Display help for the remove-password sub-command	
a	1	0
@	send delete
o	-h|--help	Display help for the delete sub-command	
a	1	0
@	send help
a	1	0
@	device-approval
s	list	List all pending requests for an organisation
s	approve	Approve a pending request
s	approve-all	Approve all pending requests for an organisation
s	deny	Deny a pending request
s	deny-all	Deny all pending requests for an organisation
s	help	Display help for command
@	device-approval list
o	-h|--help	Display help for the list sub-command	
o	--organizationid	The organisation id (required)	v
@	device-approval approve
o	-h|--help	Display help for the approve sub-command	
o	requestId	The id of the request to approve	v
o	--organizationid	The organisation id (required)	v
@	device-approval approve-all
o	-h|--help	Display help for the approve-all sub-command	
o	--organizationid	The organisation id (required)	v
@	device-approval deny
o	-h|--help	Display help for the deny sub-command	
o	requestId	The id of the request to deny	v
o	--organizationid	The organisation id (required)	v
@	device-approval deny-all
o	-h|--help	Display help for the deny-all sub-command	
o	--organizationid	The organisation id (required)	v
@	device-approval help
a	1	0
@	receive
o	--password	Password needed to access the Send	v
o	--passwordenv	Environment variable storing the Send's password	v
o	--passwordfile	Path to a file containing the Send's password as its first line	v
o	--obj	Return the Send's json object rather than the Send's content	
o	--output	Specify a file path to save a File-type Send to	v
o	-h|--help	Display help for the receive sub-command	
a	1	0
=	receive	--passwordfile
t	filepaths
=	receive	--output
t	folders
@	help
a	1	0
#	help	1
v	login	
v	logout	
v	lock	
v	unlock	
v	sync	
v	generate	
v	encode	
v	config	
v	update	
v	completion	
v	status	
v	serve	
v	list	
v	get	
v	create	
v	edit	
v	delete	
v	restore	
v	move	
v	confirm	
v	import	
v	export	
v	share	
v	send	
v	receive	
v	device-approval	
