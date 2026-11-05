@	
s	login	The auth:login command lets you log in to Contentstack and save the session
s	auth:tokens:add	Lets you add an existing management token from your Contentstack account and save it to the…
s	auth:tokens:remove	The auth:tokens:remove command lets you delete a management/ delivery token from your local CLI…
s	cm:bootstrap	The 'Bootstrap' plugin in Contentstack CLI allows users to automate the process of project setup…
s	auth:tokens	The auth:tokens command lists the existing tokens added to the session
s	config:get:region	The config:get:region command will return the name of the region on which you are performing…
s	config:set:region	The config:set:region command lets you select a region, from the available Contentstack regions…
s	cm:stacks:export	The cm:stacks:export command lets you export content from one stack to another
s	logout	The auth:logout command lets you log out of Contentstack and clear the session
s	whoami	The csdx auth:whoami command returns the username (email address) of the user who is currently…
o	--help|-h	Show help for csdx	p
@	login
o	-u|--username	Email address of your Contentstack account	v
o	-p|--password	Password can be passed in command	v
@	auth:tokens:add
o	-a|--alias	Alias (name) you want to assign to the token	v
o	--management	Alias (name) you want to assign to the token	
o	--delivery	Flag to set delivery token	
o	-k|--stack-api-key	API key of the stack where the token exists	v
o	--token	Value of the token	v
o	-f|--force	Force token replace	
@	auth:tokens:remove
o	-a|--alias	Alias (name) you want to assign to the token	v
o	-i|--ignore	Ignores if token not present. Command	
@	cm:bootstrap
o	--app-name	The name of the starter app you want to use. Example: reactjs-starter, nextjs-starter…	v
o	--project-dir	Directory/path to setup the project. If directory name has a space then provide the path as a…	v
o	--app-type	Sample or Starter app	v
o	-k|--stack-api-key	Provide stack API key to seed content	v
o	--org	Provide organization UID to create a new stack	v
o	-n|--stack-name	Name of the new stack that will be created	v
=	cm:bootstrap	--app-name
v	reactjs-starter	
v	nextjs-starter	
v	gatsby-starter	
v	angular-starter	
v	nuxt-starter	
=	cm:bootstrap	--app-type
v	Sample	
v	Starter	
@	auth:tokens
o	-x|--extended	To show extra columns	
o	--columns	To display specific columns, separated by comma	v
o	--csv	Output is csv format	
o	--filter	To filter the property by partial string matching, ex: name=foo	v
o	--no-header	To hide table’s header in output	
o	--no-truncate	To not truncate output to fit screen	
o	--output	To display output in a particular format	v
o	--sort	To sort the list, prepend '-' to sort in a descending order	v
=	auth:tokens	--output
v	csv	
v	json	
v	yaml	
@	config:get:region
@	config:set:region
a	1	0
#	config:set:region	1
v	EU	
v	AZURE-NA	
v	NA	
@	cm:stacks:export
o	-c|--config	[optional] path of the config	v
o	-k|--stack-api-key	API key of the source stack	v
o	-a|--alias	The management token of the source stack from which you will export content	v
o	-d|--data-dir	The path or the location in your file system to store the exported content. For e.g., ./content	v
o	--branch	The name of the branch where you want to export your content. If you don’t mention the branch…	v
o	--module	[optional] Specific module name. If not specified, the export command will export all the modules…	v
o	--content-types	[optional] content type	v
o	--secured-assets	[optional] use when assets are secured	v
=	cm:stacks:export	--module
v	assets	
v	content-types	
v	entries	
v	environments	
v	extensions	
v	global-fields	
v	labels	
v	locales	
v	webhooks	
v	workflows	
@	logout
@	whoami
