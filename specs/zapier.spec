@	
s	analytics	Show the status of the analytics that are collected. Also used to change what is collected
s	build	Build a pushable zip from the current directory
s	convert	Convert a Legacy Web Builder app or Visual Builder integration to a CLI integration
s	delete:integration|delete:app	Delete your integration (including all versions)
s	delete:version	Delete a specific version of your integration
s	deprecate	Mark a non-production version of your integration as deprecated, with removal by a certain date
s	describe	Describe the current integraiton
s	env:get	Get environment variables for a version
s	env:set	Set environment variables for a version
s	env:unset	Unset environment variables for a version
s	history	Get the history of your integration
s	init	Initialize a new Zapier integration with a project template
s	integrations|apps	List integrations you have admin access to
s	link	Link the current directory with an existing integration
s	login	Configure your `~/.zapierrc` with a deploy key
s	logout	Deactivate your active deploy key and reset `~/.zapierrc`
s	logs	Print recent logs
s	migrate	Migrate users from one version of your integration to another
s	promote	Promote a specific version to public access
s	push	Build and upload the current integration
s	register	Register a new integration in your account
s	scaffold	Add a starting trigger, create, search, or resource to your integration
s	team:add|team:invite	Add a team member to your integration
s	team:get|team:list	Get team members involved with your integration
s	team:remove|team:delete	Remove a team member from all versions of your integration
s	test	Test your integration via the "test" script in your "package.json"
s	upload	Upload the latest build of your integration to Zapier
s	users:add|users:invite	Add a user to some or all versions of your integration
s	users:get|users:list	Get a list of users who have been invited to your integration
s	users:links	Get a list of links that are used to invite users to your integration
s	users:remove|users:delete	Remove a user from all versions of your integration
s	validate	Validate your integration
s	versions	List the versions of your integration available for use in the Zapier editor
s	help	Display help for <%= config.bin %>
@	analytics
o	-m|--mode	Choose how much information to share. Anonymous mode drops the OS type and Zapier user id, but…	v
o	-d|--debug	Show extra debugging output	
=	analytics	-m
v	enabled	
v	anonymous	
v	disabled	
@	build
o	--disable-dependency-detection	Disable "smart" file inclusion. By default, Zapier only includes files that are required by…	
o	-d|--debug	Show extra debugging output	
@	convert
o	-v|--version	Convert a specific version. Required when converting a Visual Builder integration	v
o	-d|--debug	Show extra debugging output	
a	2	0
#	convert	2
t	folders
@	delete:integration
o	-d|--debug	Show extra debugging output	
@	delete:version
o	-d|--debug	Show extra debugging output	
a	1	0
@	deprecate
o	-d|--debug	Show extra debugging output	
a	2	0
@	describe
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
o	-d|--debug	Show extra debugging output	
=	describe	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	env:get
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
a	1	0
=	env:get	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	env:set
o	-d|--debug	Show extra debugging output	
a	2	1
@	env:unset
o	-d|--debug	Show extra debugging output	
a	2	1
@	history
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
o	-d|--debug	Show extra debugging output	
=	history	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	init
o	-t|--template	The template to start your integration with	v
o	-d|--debug	Show extra debugging output	
a	1	0
=	init	-t
v	basic-auth	
v	callback	
v	custom-auth	
v	digest-auth	
v	dynamic-dropdown	
v	files	
v	minimal	
v	oauth1-trello	
v	oauth2	
v	search-or-create	
v	session-auth	
v	typescript	
#	init	1
t	folders
@	integrations
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
o	-d|--debug	Show extra debugging output	
=	integrations	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	link
o	-d|--debug	Show extra debugging output	
@	login
o	-s|--sso	Use this flag if you log into Zapier a Single Sign-On (SSO) button and don't have a Zapier password	
o	-d|--debug	Show extra debugging output	
@	logout
o	-d|--debug	Show extra debugging output	
@	logs
o	-v|--version	Filter logs to the specified version	v
o	-s|--status	Filter logs to only see errors or successes	v
o	-t|--type	See logs of the specified type	v
o	--detailed	See extra info, like request/response body and headers	
o	-u|--user	Only show logs for this user. Defaults to your account	v
o	--limit	Cap the number of logs returned. Max is 50 (also the default)	v
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
o	-d|--debug	Show extra debugging output	
=	logs	-s
v	any	
v	success	
v	error	
=	logs	-t
v	console	
v	bundle	
v	http	
=	logs	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	migrate
o	--user	Migrate only this user	v
o	-d|--debug	Show extra debugging output	
a	3	0
@	promote
o	-d|--debug	Show extra debugging output	
a	1	0
@	push
o	--disable-dependency-detection	Disable "smart" file inclusion. By default, Zapier only includes files that are required by…	
o	-d|--debug	Show extra debugging output	
@	register
o	-d|--debug	Show extra debugging output	
a	1	0
@	scaffold
o	-d|--dest	Specify the new file's directory. Use this flag when you want to create a different folder…	v
o	--test-dest	Specify the new test file's directory. Use this flag when you want to create a different folder…	v
o	-e|--entry	Supply the path to your integration's root (`index.js`). Only needed if your `index.js` is in a…	v
o	-f|--force	Should we overwrite an existing trigger/search/create file?	
o	--no-help	When scaffolding, should we skip adding helpful intro comments? Useful if this isn't your first…	
o	-d|--debug	Show extra debugging output	
a	2	0
=	scaffold	-d
t	folders
=	scaffold	--test-dest
t	folders
=	scaffold	-e
t	filepaths
#	scaffold	1
v	trigger	
v	search	
v	create	
v	resource	
@	team:add
o	-d|--debug	Show extra debugging output	
a	3	0
#	team:add	2
v	admin	
v	subscriber	
@	team:get
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
o	-d|--debug	Show extra debugging output	
=	team:get	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	team:remove
o	-d|--debug	Show extra debugging output	
@	test
o	--skip-validate	Forgo running `zapier validate` before tests are run. This will speed up tests if you're modifying…	
o	--yarn	Use `yarn` instead of `npm`. This happens automatically if there's a `yarn.lock` file, but you can…	
o	-d|--debug	Show extra debugging output	
@	upload
o	-d|--debug	Show extra debugging output	
@	users:add
o	-f|--force	Skip confirmation. Useful for running programmatically	
o	-d|--debug	Show extra debugging output	
a	2	0
@	users:get
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
o	-d|--debug	Show extra debugging output	
=	users:get	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	users:links
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
o	-d|--debug	Show extra debugging output	
=	users:links	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	users:remove
o	-f|--force	Skips confirmation. Useful for running programmatically	
o	-d|--debug	Show extra debugging output	
a	1	0
@	validate
o	--without-style	Forgo pinging the Zapier server to run further checks	
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
o	-d|--debug	Show extra debugging output	
=	validate	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	versions
o	-f|--format	Change the way structured data is presented. If "json" or "raw", you can pipe the output of the…	v
o	-d|--debug	Show extra debugging output	
=	versions	-f
v	plain	
v	json	
v	raw	
v	row	
v	table	
@	help
o	--all	See all commands in CLI	
a	1	0
