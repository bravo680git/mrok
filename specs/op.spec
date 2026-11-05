@	
s	account	Manage your locally configured 1Password accounts
s	connect	Manage Connect instances and Connect tokens in your 1Password account
s	document	Perform CRUD operations on Document items in your vaults
s	events-api	Manage Events API integrations in your 1Password account
s	group	Perform CRUD operations on the groups of users in your 1Password account
s	item	Perform CRUD operations on the 1Password items in your vaults
s	user	Manage users within this 1Password account
s	vault	Manage permissions and perform CRUD operations on your 1Password vaults
s	completion	Generate shell completion information
s	inject	Inject secrets into a config file
s	read	Read a secret using the secrets reference syntax
s	run	Pass secrets as environment variables to a process
s	signin	Sign in to a 1Password account
s	signout	Sign out of a 1Password account
s	update	Check for and download updates
s	whoami	Get information about a signed-in account
o	--account	Select the account to execute the command by account shorthand, sign-in address, account ID, or…	vp
o	--cache	Store and use cached information	p
o	--config	Use this configuration directory	vp
o	--debug	Output debug logs. Can also be set using $OP_DEBUG environment variable	p
o	--encoding	Use this character encoding type. Default: UTF-8. Supported: SHIFT_JIS, gbk	vp
o	--format	Use this output format. Can be 'human-readable' or 'json'. Can be set as the OP_FORMAT environment…	vp
o	-h|--help	Get help for op	p
o	--iso-timestamps	Format timestamps according to ISO 8601 / RFC 3339. Can be set as the OP_ISO_TIMESTAMPS…	p
o	--no-color	Print output without color	p
o	--session	Authenticate with this session token. 1Password CLI outputs session tokens for successful 'op…	vp
o	-v|--version	Version for op	
=		--account
d
=		--config
t	folders
=		--encoding
v	UTF-8	
v	SHIFT_JIS	
v	gbk	
=		--format
v	human-readable	
v	json	
@	account
s	add	Add an account to sign in to for the first time
s	get	Get details about your account
s	list|ls	List users and accounts set up on this device
s	forget	Remove a 1Password account from this device
@	account add
o	--address	The sign-in address for your account	v
o	--email	The email address associated with your account	v
o	--raw	Only return the session token	
o	--shorthand	Set the short account name	v
@	account get
@	account list
@	account forget
o	--all	Forget all authenticated accounts	
a	1	0
@	connect
s	group	Manage group access to Secrets Automation
s	server	Manage Connect servers
s	token	Manage Connect tokens
s	vault	Manage connect server vault access
@	connect group
s	grant	Grant a group access to manage Secrets Automation
s	revoke	Revoke a group's access to manage Secrets Automation
@	connect group grant
o	--all-servers	Grant access to all current and future servers in the authenticated account	
o	--group	The group to receive access	v
@	connect group revoke
o	--all-servers	Revoke access to all current and future servers in the authenticated account	
o	--group	The group to revoke access from	v
@	connect server
s	create	Set up a Connect server
s	get	Get a Connect server
s	edit	Rename a Connect server
s	delete|remove|rm	Remove a Connect server
s	list|ls	List Connect servers
@	connect server create
@	connect server get
a	1	0
@	connect server edit
a	1	0
@	connect server delete
a	1	0
@	connect server list
@	connect token
s	create	Issue a token for a 1Password Connect server
s	edit	Rename a Connect token
s	delete|remove|rm	Revoke a token for a Connect server
s	list|ls	Get a list of tokens
@	connect token create
o	--expires-in	Set how long the Connect token is valid for in (s)econds, (m)inutes, or (h)ours	v
o	--server	Issue a token for this server	v
@	connect token edit
o	--name	Change the token's name	v
@	connect token delete
a	1	0
@	connect token list
@	connect vault
s	grant	Grant a Connect server access to a vault
s	revoke	Revoke a Connect server's access to a vault
@	connect vault grant
o	--server	The server to be granted access	v
@	connect vault revoke
o	--server	The server to revoke access from	v
@	document
s	create	Create a document item
s	get	Download a document
s	edit	Edit a document item
s	delete|remove|rm	Delete or archive a document item
s	list|ls	Get a list of documents
@	document create
o	--file-name	Set the file's name	v
o	--tags	Set the tags to the specified (comma-separated) values	v
o	--title	Set the document item's title	v
a	1	0
@	document get
o	--include-archive	Include document items in the Archive. Can also be set using OP_INCLUDE_ARCHIVE environment variable	
o	--output	Save the document to the file path instead of stdout	v
a	1	0
@	document edit
o	--file-name	Set the file's name	v
o	--tags	Set the tags to the specified (comma-separated) values. An empty value will remove all tags	v
o	--title	Set the document item's title	v
a	2	0
@	document delete
o	--archive	Move the document to the Archive	
a	1	0
@	document list
o	--include-archive	Include document items in the Archive. Can also be set using OP_INCLUDE_ARCHIVE environment variable	
@	events-api
s	create	Set up an integration with the Events API
@	events-api create
@	group
s	user	Manage users in groups
s	create	Create a group
s	get	Get details about a group
s	edit	Edit a group's name or description
s	delete|remove|rm	Remove a group
s	list|ls	List groups
@	group user
s	grant	Grant a user access to a group
s	revoke	Revoke a user's access to a vault or group
s	list|ls	Retrieve users that belong to a group
@	group user grant
o	--group	Specify the group to grant the user access to	v
o	--role	Specify the user's role as a member or manager. Default: member	v
@	group user revoke
o	--group	Specify the group to revoke the user's access to	v
@	group user list
@	group create
o	--description	Set the group's description	v
@	group get
a	1	0
@	group edit
o	--description	Change the group's description	v
a	1	0
@	group delete
a	1	0
@	group list
o	--user	List groups that a user belongs to	v
@	item
s	template	Manage templates
s	create	Create an item
s	get	Get an item's details
s	edit	Edit an item's details
s	delete|remove|rm	Delete or archive an item
s	list|ls	List items
s	share	Share an item
@	item template
s	get	Get an item template
s	list|ls	Get a list of templates
@	item template get
o	-f|--force	Do not prompt for confirmation	
a	1	0
@	item template list
@	item create
o	--category	Set the item's category	v
o	--dry-run	Perform a dry run of the command and output a preview of the resulting item	
o	--generate-password	Give the item a randomly generated password	v=
o	--tags	Set the tags to the specified (comma-separated) values	v
o	--template	Specify the filepath to read an item template from	v
o	--title	Set the item's title	v
o	--url	Set the URL associated with the item	v
a	1	0
@	item get
o	--fields	Only return data from these fields. Use 'label=' to get the field by name or 'type=' to filter…	v
o	--include-archive	Include items in the Archive. Can also be set using OP_INCLUDE_ARCHIVE environment variable	
o	--otp	Output the primary one-time password for this item	
o	--share-link	Get a shareable link for the item	
a	1	0
@	item edit
a	2	0
@	item delete
o	--archive	Move the item to the Archive	
a	1	0
@	item list
o	--categories	Only list items in these categories (comma-separated)	v
o	--include-archive	Include items in the Archive. Can also be set using OP_INCLUDE_ARCHIVE environment variable	
o	--long	Output a more detailed item list	
o	--tags	Only list items with these tags (comma-separated)	v
@	item share
o	--emails	Email addresses to share with	v
o	--expiry	Link expiring after the specified duration in (s)econds, (m)inutes, or (h)ours (default 7h)	v
o	--vault	Look for the item in this vault	v
a	1	0
@	user
s	provision	Provision a user in the authenticated account
s	confirm	Confirm a user
s	get	Get details about a user
s	edit	Edit a user's name or Travel Mode status
s	suspend	Suspend a user
s	reactivate	Reactivate a suspended user
s	delete|remove|rm	Remove a user and all their data from the account
s	list|ls	List users
@	user provision
o	--email	Provide the user's email address	v
o	--language	Provide the user's account language. (default "en")	v
@	user confirm
o	--all	Confirm all unconfirmed users	
a	1	0
@	user get
o	--fingerprint	Get the user's public key fingerprint	
a	1	0
#	user get	1
v	--me	Get the authenticated user's details
@	user edit
o	--name	Set the user's name	v
a	1	0
@	user suspend
o	--deauthorize-devices-after	Deauthorize the user's devices after a time (rounded down to seconds)	v
a	1	0
@	user reactivate
a	1	0
@	user delete
a	1	0
@	user list
o	--group	List users who belong to a group	v
@	vault
s	group	Manage group vault access
s	user	Manage user vault access
s	create	Create a new vault
s	get	Get details about a vault
s	edit	Edit a vault's name, description, icon or Travel Mode status
s	delete|remove|rm	Remove a vault
s	list|ls	List all vaults in the account
@	vault group
s	grant	Grant a group permissions to a vault
s	revoke	Revoke a portion or the entire access of a group to a vault
s	list|ls	List all the groups that have access to the given vault
@	vault group grant
o	--group	The group to receive access	v
o	--no-input	Do not prompt for input on interactive terminal	v
o	--permissions	The permissions to grant to the group	v
@	vault group revoke
o	--group	The group to revoke access from	v
o	--no-input	Do not prompt for input on interactive terminal	v
o	--permissions	The permissions to revoke from the group	v
@	vault group list
a	1	0
@	vault user
s	grant	Grant a user access to a vault
s	revoke	Revoke a portion or the entire access of a user to a vault
s	list|ls	List all users with access to the vault and their permissions
@	vault user grant
o	--no-input	Do not prompt for input on interactive terminal	v
o	--permissions	The permissions to grant to the user	v
o	--user	The user to receive access	v
@	vault user revoke
o	--no-input	Do not prompt for input on interactive terminal	v
o	--permissions	The permissions to revoke from the user	v
o	--user	The user to revoke access from	v
@	vault user list
@	vault create
o	--allow-admins-to-manage	Set whether admins can manage the vault. Default: false	v
o	--description	Set the group's description	v
@	vault get
a	1	0
@	vault edit
o	--description	Change the vault's description	v
o	--icon	Change the vault's icon	v
o	--name	Change the vault's name	v
o	--travel-mode	Turn Travel Mode on or off for the vault. Only vaults with Travel Mode enabled will be accessible…	v
a	1	0
@	vault delete
a	1	0
@	vault list
o	--group	List vaults a group has access to	v
@	completion
@	inject
@	read
o	--file-mode	Set filemode for the output file if it does not yet exist. It is ignored without the --out-file…	v
o	-f|--force	Do not prompt for confirmation	
o	-n|--no-newline	Do not print a new line after the secret	
@	run
o	--env-file	Enable Dotenv integration with specific Dotenv files to parse. For example: --env-file=.env	v=
o	--no-masking	Disable masking of secrets on stdout and stderr	
a	1	0
@	signin
o	-f|--force	Ignore warnings and print raw output from this command	
@	signout
o	--all	Sign out of all signed-in accounts	
o	--forget	Remove the details for a 1Password account from this device	
@	update
o	--directory	Download the update to this ''path''	v
=	update	--directory
t	folders
@	whoami
