@	
s	login	Log in to Directory Connector
s	logout	Log out of Directory Connector
s	test	Prints a JSON formatted array of groups and users that would be synced to your Bitwarden…
s	sync	Run a live sync operation and push data to your Bitwarden organization
s	last-sync	The last-sync command returns an ISO 8601 timestamp for the last sync operation that was performed…
s	config	The config command allows you to specify your directory settings
s	data-file	Path to data.json database file
s	clear-cache	The clear-cache command allows you to clear cached data that the application stores while…
s	update	The update command allows you to check if your Directory Connector CLI is up-to-date
o	--help	Show help for bwdc	
@	login
o	--help		
a	2	0
@	logout
o	--help		
@	test
o	--last	Test only the changes since the last successful sync	
o	--help		
@	sync
o	--help		
@	last-sync
o	--help		
a	1	0
@	config
s	server	URL of your self-hosted installation (e.g. https://my.url.com) or https://vault.bitwarden.eu
s	directory	Type of directory to use
s	ldap.password	Password for connection to the LDAP server
s	azure.key	Azure AD secret key
s	gsuite.key	Google Workspace/GSuite private key
s	okta.token	Okta token
s	onelogin.secret	OneLogin client secret
o	--help		
a	2	0
@	config server
a	1	0
@	config directory
a	1	0
#	config directory	1
v	0	Active Directory/LDAP
v	1	Azure Active Directory
v	2	Google Workspace/GSuite
v	3	Okta
v	4	OneLogin
@	config ldap.password
a	1	0
@	config azure.key
a	1	0
@	config gsuite.key
a	1	0
@	config okta.token
a	1	0
@	config onelogin.secret
a	1	0
@	data-file
o	--help		
@	clear-cache
o	--help		
@	update
