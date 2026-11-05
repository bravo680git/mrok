@	
s	account:manageauth	Manages authentication IDs (authID) for all your projects. An authentication ID is a custom alias…
s	account:savetoken	Saves a TBA token that you issued previously in NetSuite
s	account:setup	Sets up an account to use with the SuiteCloud CLI for Node.js
s	file:create	Creates a SuiteScript file
s	file:import	Imports files from an account to your account customization project. You cannot import files from…
s	file:list	Lists the files in the File Cabinet of your account
s	file:upload	Uploads files from your project to an account
s	object:import	Imports custom objects from your NetSuite account to the SuiteCloud project. In account…
s	object:list	Lists the custom objects deployed in an account
s	object:update	Overwrites the custom objects in the project with the custom objects in an account
s	project:adddependencies	Adds the missing dependencies to the manifest file
s	project:create	Creates a SuiteCloud project, either a SuiteApp or an account customization project (ACP)
s	project:deploy	Deploys the folder containing the project. The project folder is zipped before deployment, only…
s	project:package	Generates a ZIP file from your project, respecting the structure specified in the deploy.xml file
s	project:validate	Validates the folder containing the SuiteCloud project
o	--version	Outputs the version number	
o	-h|--help	Displays help for the command	
@	account:manageauth
o	-i|--interactive	Runs the command in interactive mode	
o	--info	Prints the following information for the specified authentication ID (authID): account ID, role…	v
o	--list	Prints a list of all the configured authentication IDs (authID). Usage: account:manageauth --list	
o	--remove	Removes an authentication ID (authID). Usage: account:manageauth --remove {authID}	v
o	--rename	Renames an authentication ID (authID). You must specify it together with the renameto option…	v
o	--renameto	Specifies the new ID for an authentication ID (authID). You must specify it together with the…	v
o	-h|--help	Displays help for the command	
@	account:savetoken
o	--account	Specifies the ID of the account to log in to	v
o	--authid	References the custom name you gave to a specific account-role combination	v
o	--tokenid	Specifies the token ID of a TBA token you issued previously in NetSuite	v
o	--tokensecret	Specifies the token secret of a TBA token you issued previously in NetSuite	v
o	--url	Specifies the NetSuite domain of the account you want to use. You only need to specify the…	v
o	-h|--help	Displays help for the command	
@	account:setup
o	-i|--interactive	Runs the command in interactive mode	
o	-d|--dev	Specifies the NetSuite domain of the account you want to use. You only need to specify the…	
o	-h|--help	Displays help for the command	
@	file:create
o	-i|--interactive	Runs the command in interactive mode	
o	--module	Specifies the SuiteScript modules you want to add to the SuiteScript file. For example, "N/record"	v
o	--path	Specifies the File Cabinet path of the SuiteScript file to create. For example…	v
o	--type	Specifies the type of the SuiteScript file that you want to create. For example, "ClientScript"	v
o	-h|--help	Displays help for the command	
@	file:import
o	-i|--interactive	Runs the command in interactive mode	
o	--path	Specifies the File Cabinet paths of the files to import. For example, "/SuiteScripts/file.js"	v
o	--calledfromcomparefiles	Message displayed should be different if called from Compare Files	
o	--excludeproperties	Excludes all file properties within the .attributes folder	
o	-h|--help	Displays help for the command	
@	file:list
o	-i|--interactive	Runs the command in interactive mode	
o	--folder	Specifies the File Cabinet path, for example, "/SuiteScripts". All files within subfolders are…	v
o	-h|--help	Displays help for the command	
=	file:list	--folder
t	folders
@	file:upload
o	-i|--interactive	Runs the command in interactive mode	
o	--paths	Specifies the file cabinet paths of the files to upload. To specify multiple paths, enter a space…	v
o	-h|--help	Displays help for the command	
=	file:upload	--paths
t	filepaths
@	object:import
o	-i|--interactive	Runs the command in interactive mode	
o	--appid	Specifies your application ID. If specified, only custom objects with that application ID are…	v
o	--destinationfolder	Specifies the project folder where objects will be stored. It must be within the Objects folder of…	
o	--excludefiles	Indicates that the SuiteScript files referenced in custom objects are not imported. It can only be…	
o	--scriptid	Specifies the script ID. To specify multiple IDs, enter the IDs separated by spaces. Enter "ALL"…	
o	--type	Specifies the type of custom objects to import. Enter "ALL" to import all custom objects. To see…	
o	-h|--help	Displays help for the command	
@	object:list
o	-i|--interactive	Runs the command in interactive mode	
o	--appid	Specifies your application ID. If specified, only custom objects with that application ID are…	v
o	--scriptid	Specifies the script ID. If you specify it, only objects containing that script ID will be listed…	v
o	--type	Specifies the type of custom objects to list. To specify multiple types, enter the types separated…	v
o	-h|--help	Displays help for the command	
@	object:update
o	-i|--interactive	Runs the command in interactive mode	
o	--includeinstances	Includes instances. This is only available for custom records	
o	--scriptid	Specifies the script ID of the objects you want to overwrite	v
o	-h|--help	Displays help for the command	
@	project:adddependencies
@	project:create
o	-i|--interactive	Runs the command in interactive mode	
o	--overwrite	Overwrites the existing project	
o	--projectid	Specifies the project ID. It is mandatory for SuiteApps	v
o	--projectname	Specifies the project name	v
o	--projectversion	Specifies the project version. It is mandatory for SuiteApps	v
o	--publisherid	Specifies the publisher ID. It is mandatory for SuiteApps	v
o	--type	Specifies the project type. Enter one of the following options: ACCOUNTCUSTOMIZATION or SUITEAPP	v
o	-h|--help	Displays help for the command	
=	project:create	--type
v	ACCOUNTCUSTOMIZATION	
v	SUITEAPP	
@	project:deploy
o	-i|--interactive	Runs the command in interactive mode	
o	--dryrun	Runs a preview of your deploy process. Your project is not deployed	
o	--log	Sets the deployment log file location, as either a directory or a file name. If it is a directory…	v
o	--validate	Validates the project before deploying. If an error ocurrs during the deployment, the process is…	
o	--accountspecificvalues	Indicates how to handle the presence of account-specific values in an account customization…	v
o	-a|--applyinstallprefs	Applies the settings from the hiding.xml, locking.xml, and overwriting.xml files. It only applies…	
o	-h|--help	Displays help for the command	
=	project:deploy	--log
t	folders,filepaths
=	project:deploy	--accountspecificvalues
v	ERROR	
v	WARNING	
@	project:package
o	-i|--interactive	Runs the command in interactive mode	
o	-h|--help	Displays help for the command	
@	project:validate
o	-i|--interactive	Runs the command in interactive mode	
o	--log	Sets the validation log file location, as either a directory or a file name. If it is a directory…	v
o	--server	Indicates that the server will perform the validation	
o	--accountspecificvalues	Indicates how to handle the presence of account-specific values in an account customization…	v
o	-a|--applyinstallprefs	Applies the settings from the hiding.xml, locking.xml, and overwriting.xml files. It only applies…	
o	-h|--help	Displays help for the command	
=	project:validate	--log
t	folders,filepaths
=	project:validate	--accountspecificvalues
v	ERROR	
v	WARNING	
