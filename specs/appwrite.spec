@	
s	login	The login command allows you to authenticate and manage a user account
s	init	The init command helps you initialize your Appwrite project, functions and collections
s	deploy	The deploy command provides a convenient wrapper for deploying your functions and collections
s	logout	The logout command allows you to logout of your Appwrite account
s	account	The account command allows you to authenticate and manage a user account
s	avatars	The avatars command aims to help you complete everyday tasks related to your app image, icons, and…
s	databases	The databases command allows you to create structured collections of documents, query and filter…
s	functions	The functions command allows you view, create and manage your Cloud Functions
s	health	The health command allows you to both validate and monitor your Appwrite server's health
s	locale	The locale command allows you to customize your app based on your users' location
s	projects	The projects command allows you to view, create and manage your Appwrite projects
s	storage	The storage command allows you to manage your project files
s	teams	The teams command allows you to group users of your project and to enable them to share read and…
s	users	The users command allows you to manage your project users
s	client	The client command allows you to configure your CLI
o	-v|--version	Output the version number	
o	--verbose	Show complete error log	
o	--json	Output in JSON format	
o	-h|--help	Display help for command	p
@	login
@	init
s	project	Initialise your Appwrite project
s	function	Initialise your Appwrite cloud function
s	collection	Initialise your Appwrite collections
@	init project
@	init function
@	init collection
o	--databaseId	Database ID	v
o	--all	Flag to initialize all databases	
@	deploy
s	function	Deploy functions in the current directory
s	collection	Deploy collections in the current project
@	deploy function
o	--functionId	Function ID	v
o	--all	Flag to deploy all functions	
@	deploy collection
o	--all	Flag to deploy all functions	
@	logout
@	account
s	get	Get currently logged in user data as JSON object
s	create	Use this endpoint to allow a new user to register a new account in your project. After the user…
s	updateEmail	Update currently logged in user account email address. After changing user address, the user…
s	createJWT	Use this endpoint to create a JSON Web Token. You can use the resulting JWT to authenticate on…
s	getLogs	Get currently logged in user list of latest security activity logs. Each log returns user IP…
s	updateName	Update currently logged in user account name
s	updatePassword	Update currently logged in user password. For validation, user is required to pass in the new…
s	updatePhone	Update the currently logged in user's phone number. After updating the phone number, the phone…
s	getPrefs	Get currently logged in user preferences as a key-value object
s	updatePrefs	Update currently logged in user account preferences. The object you pass is stored as is, and…
s	createRecovery	Sends the user an email with a temporary secret key for password reset. When the user clicks the…
s	updateRecovery	Use this endpoint to complete the user account password reset. Both the **userId** and **secret**…
s	getSessions	Get currently logged in user list of active sessions across different devices
s	deleteSessions	Delete all sessions from the user account and remove any sessions cookies from the end client
s	createAnonymousSession	Use this endpoint to allow a new user to register an anonymous account in your project. This route…
s	createEmailSession	Allow the user to login into their account by providing a valid email and password combination…
s	createMagicURLSession	Sends the user an email with a secret key for creating a session. When the user clicks the link in…
s	updateMagicURLSession	Use this endpoint to complete creating the session with the Magic URL. Both the **userId** and…
s	createOAuth2Session	Allow the user to login to their account using the OAuth2 provider of their choice. Each OAuth2…
s	createPhoneSession	Sends the user an SMS with a secret key for creating a session. Use the returned user ID and…
s	updatePhoneSession	Use this endpoint to complete creating a session with SMS. Use the **userId** from the…
s	getSession	Use this endpoint to get a logged in user's session using a Session ID. Inputting 'current' will…
s	updateSession	Access tokens have limited lifespan and expire to mitigate security risks. If session was created…
s	deleteSession	Use this endpoint to log out the currently logged in user from all their account sessions across…
s	updateStatus	Block the currently logged in user account. Behind the scene, the user record is not deleted but…
s	createVerification	Use this endpoint to send a verification message to your user email address to confirm they are…
s	updateVerification	Use this endpoint to complete the user email verification process. Use both the **userId** and…
s	createPhoneVerification	Use this endpoint to send a verification SMS to the currently logged in user. This endpoint is…
s	updatePhoneVerification	Use this endpoint to complete the user phone verification process. Use the **userId** and…
@	account get
@	account create
o	--userId	Unique Id. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid…	v
o	--email	User email	v
o	--password	User password. Must be at least 8 chars	v
o	--name	User name. Max length: 128 chars	v
@	account updateEmail
o	--email	User email	v
o	--password	User password. Must be at least 8 chars	v
@	account createJWT
@	account getLogs
o	--limit	Maximum number of logs to return in response. By default will return maximum 25 results. Maximum…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
@	account updateName
o	--name	User name. Max length: 128 chars	v
@	account updatePassword
o	--password	New user password. Must be at least 8 chars	v
o	--oldPassword	Current user password. Must be at least 8 chars	v
@	account updatePhone
o	--number	Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212	v
o	--password	User password. Must be at least 8 chars	v
@	account getPrefs
@	account updatePrefs
o	--prefs	Prefs key-value JSON object	v
@	account createRecovery
o	--email	User email	v
o	--url	URL to redirect the user back to your app from the recovery email. Only URLs from hostnames in…	v
@	account updateRecovery
o	--userId	User ID	v
o	--secret	Valid reset token	v
o	--password	New user password. Must be at least 8 chars	v
o	--passwordAgain	Repeat new user password. Must be at least 8 chars	v
@	account getSessions
@	account deleteSessions
@	account createAnonymousSession
@	account createEmailSession
o	--email	User email	v
o	--password	User password. Must be at least 8 chars	v
@	account createMagicURLSession
o	--userId	Unique Id. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid…	v
o	--email	User email	v
o	--url	URL to redirect the user back to your app from the magic URL login. Only URLs from hostnames in…	v
@	account updateMagicURLSession
o	--userId	User ID	v
o	--secret	Valid verification token	v
@	account createOAuth2Session
o	--provider	OAuth2 Provider. Currently, supported providers are: amazon, apple, auth0, autodesk, bitbucket…	v
o	--success	URL to redirect back to your app after a successful login attempt. Only URLs from hostnames in…	v
o	--failure	URL to redirect back to your app after a failed login attempt. Only URLs from hostnames in your…	v
o	--scopes	A list of custom OAuth2 scopes. Check each provider internal docs for a list of supported scopes…	v
@	account createPhoneSession
o	--userId	Unique Id. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid…	v
o	--number	Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212	v
@	account updatePhoneSession
o	--userId	User ID	v
o	--secret	Valid verification token	v
@	account getSession
o	--sessionId	Session ID. Use the string 'current' to get the current device session	v
@	account updateSession
o	--sessionId	Session ID. Use the string 'current' to update the current device session	v
@	account deleteSession
o	--sessionId	Session ID. Use the string 'current' to delete the current device session	v
@	account updateStatus
@	account createVerification
o	--url	URL to redirect the user back to your app from the verification email. Only URLs from hostnames in…	v
@	account updateVerification
o	--userId	User ID	v
o	--secret	Valid verification token	v
@	account createPhoneVerification
@	account updatePhoneVerification
o	--secret	Valid verification token	v
@	avatars
s	getBrowser	You can use this endpoint to show different browser icons to your users. The code argument…
s	getCreditCard	The credit card endpoint will return you the icon of the credit card provider you need. Use width…
s	getFavicon	Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL
s	getFlag	You can use this endpoint to show different country flags icons to your users. The code argument…
s	getImage	Use this endpoint to fetch a remote image URL and crop it to any image size you want. This…
s	getInitials	Use this endpoint to show your user initials avatar icon on your website or app. By default, this…
s	getQR	Converts a given plain text to a QR code image. You can use the query parameters to change the…
@	avatars getBrowser
o	--code	Browser Code	v
o	--width	Image width. Pass an integer between 0 to 2000. Defaults to 100	v
o	--height	Image height. Pass an integer between 0 to 2000. Defaults to 100	v
o	--quality	Image quality. Pass an integer between 0 to 100. Defaults to 100	v
o	--destination	Output file path	v
@	avatars getCreditCard
o	--code	Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo…	v
o	--width	Image width. Pass an integer between 0 to 2000. Defaults to 100	v
o	--height	Image height. Pass an integer between 0 to 2000. Defaults to 100	v
o	--quality	Image quality. Pass an integer between 0 to 100. Defaults to 100	v
o	--destination	Output file path	v
@	avatars getFavicon
o	--url	Website URL which you want to fetch the favicon from	v
o	--destination	Output file path	v
@	avatars getFlag
o	--code	Country Code. ISO Alpha-2 country code format	v
o	--width	Image width. Pass an integer between 0 to 2000. Defaults to 100	v
o	--height	Image height. Pass an integer between 0 to 2000. Defaults to 100	v
o	--quality	Image quality. Pass an integer between 0 to 100. Defaults to 100	v
o	--destination	Output file path	v
@	avatars getImage
o	--url	Image URL which you want to crop	v
o	--width	Resize preview image width, Pass an integer between 0 to 2000. Defaults to 400	v
o	--height	Resize preview image height, Pass an integer between 0 to 2000. Defaults to 400	v
o	--destination	Output file path	v
@	avatars getInitials
o	--name	Full Name. When empty, current user name or email will be used. Max length: 128 chars	v
o	--width	Image width. Pass an integer between 0 to 2000. Defaults to 100	v
o	--height	Image height. Pass an integer between 0 to 2000. Defaults to 100	v
o	--color	Changes text color. By default a random color will be picked and stay will persistent to the given…	v
o	--background	Changes background color. By default a random color will be picked and stay will persistent to the…	v
o	--destination	Output file path	v
@	avatars getQR
o	--text	Plain text to be converted to QR code image	v
o	--size	QR code size. Pass an integer between 1 to 1000. Defaults to 400	v
o	--margin	Margin from edge. Pass an integer between 0 to 10. Defaults to 1	v
o	--download	Return resulting image with 'Content-Disposition: attachment ' headers for the browser to start…	v
o	--destination	Output file path	v
@	databases
s	list	
s	create	
s	getUsage	
s	get	
s	update	
s	delete	
s	listCollections	
s	createCollection	
s	getCollection	
s	updateCollection	
s	deleteCollection	
s	listAttributes	
s	createBooleanAttribute	
s	createEmailAttribute	
s	createEnumAttribute	
s	createFloatAttribute	
s	createIntegerAttribute	
s	createIpAttribute	
s	createStringAttribute	
s	createUrlAttribute	
s	getAttribute	
s	deleteAttribute	
s	listDocuments	
s	createDocument	
s	getDocument	
s	updateDocument	
s	deleteDocument	
s	listDocumentLogs	
s	listIndexes	
s	createIndex	
s	getIndex	
s	deleteIndex	
s	listCollectionLogs	
s	getCollectionUsage	
s	listLogs	
s	getDatabaseUsage	
@	databases list
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Maximum number of collection to return in response. By default will return maximum 25 results…	v
o	--offset	Offset value. The default value is 0. Use this param to manage pagination. [learn more about…	v
o	--cursor	ID of the collection used as the starting point for the query, excluding the collection itself…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	databases create
o	--databaseId	Unique Id. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid…	v
o	--name	Collection name. Max length: 128 chars	v
@	databases getUsage
o	--range	'Date range	v
@	databases get
o	--databaseId	Database ID	v
@	databases update
o	--databaseId	Database ID	v
o	--name	Collection name. Max length: 128 chars	v
@	databases delete
o	--databaseId	Database ID	v
@	databases listCollections
o	--databaseId	Database ID	v
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Maximum number of collection to return in response. By default will return maximum 25 results…	v
o	--offset	Offset value. The default value is 0. Use this param to manage pagination. [learn more about…	v
o	--cursor	ID of the collection used as the starting point for the query, excluding the collection itself…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	databases createCollection
o	--databaseId	Database ID	v
o	--collectionId	Unique Id. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid…	v
o	--name	Collection name. Max length: 128 chars	v
o	--permission	Specifies the permissions model used in this collection, which accepts either 'collection' or…	v
o	--read	An array of strings with read permissions. By default no user is granted with any read…	v
o	--write	An array of strings with write permissions. By default no user is granted with any write…	v
@	databases getCollection
o	--databaseId	Database ID	v
o	--collectionId	Collection ID	v
@	databases updateCollection
o	--databaseId	Database ID	v
o	--collectionId	Collection ID	v
o	--name	Collection name. Max length: 128 chars	v
o	--permission	Permissions type model to use for reading documents in this collection. You can use…	v
o	--read	An array of strings with read permissions. By default inherits the existing read permissions…	v
o	--write	An array of strings with write permissions. By default inherits the existing write permissions…	v
o	--enabled	Is collection enabled?	v
@	databases deleteCollection
o	--databaseId	Database ID	v
o	--collectionId	Collection ID	v
@	databases listAttributes
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
@	databases createBooleanAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
o	--required	Is attribute required?	v
o	--xdefault	Default value for attribute when not provided. Cannot be set when attribute is required	v
o	--array	Is attribute an array?	v
@	databases createEmailAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
o	--required	Is attribute required?	v
o	--xdefault	Default value for attribute when not provided. Cannot be set when attribute is required	v
o	--array	Is attribute an array?	v
@	databases createEnumAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
o	--elements	Array of elements in enumerated type. Uses length of longest element to determine size. Maximum of…	v
o	--required	Is attribute required?	v
o	--xdefault	Default value for attribute when not provided. Cannot be set when attribute is required	v
o	--array	Is attribute an array?	v
@	databases createFloatAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
o	--required	Is attribute required?	v
o	--min	Minimum value to enforce on new documents	v
o	--max	Maximum value to enforce on new documents	v
o	--xdefault	Default value for attribute when not provided. Cannot be set when attribute is required	v
o	--array	Is attribute an array?	v
@	databases createIntegerAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
o	--required	Is attribute required?	v
o	--min	Minimum value to enforce on new documents	v
o	--max	Maximum value to enforce on new documents	v
o	--xdefault	Default value for attribute when not provided. Cannot be set when attribute is required	v
o	--array	Is attribute an array?	v
@	databases createIpAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
o	--required	Is attribute required?	v
o	--xdefault	Default value for attribute when not provided. Cannot be set when attribute is required	v
o	--array	Is attribute an array?	v
@	databases createStringAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
o	--size	Attribute size for text attributes, in number of characters	v
o	--required	Is attribute required?	v
o	--xdefault	Default value for attribute when not provided. Cannot be set when attribute is required	v
o	--array	Is attribute an array?	v
@	databases createUrlAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
o	--required	Is attribute required?	v
o	--xdefault	Default value for attribute when not provided. Cannot be set when attribute is required	v
o	--array	Is attribute an array?	v
@	databases getAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
@	databases deleteAttribute
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Attribute Key	v
@	databases listDocuments
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--queries	Array of query strings generated using the Query class provided by the SDK. [Learn more about…	v
o	--limit	Maximum number of documents to return in response. By default will return maximum 25 results…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
o	--cursor	ID of the document used as the starting point for the query, excluding the document itself. Should…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderAttributes	Array of attributes used to sort results. Maximum of 100 order attributes are allowed, each 4096…	v
o	--orderTypes	Array of order directions for sorting attribtues. Possible values are DESC for descending order…	v
@	databases createDocument
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--documentId	Document ID. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid…	v
o	--data	Document data as JSON object	v
o	--read	An array of strings with read permissions. By default only the current user is granted with read…	v
o	--write	An array of strings with write permissions. By default only the current user is granted with write…	v
@	databases getDocument
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--documentId	Document ID	v
@	databases updateDocument
o	--databaseId	Database ID	v
o	--collectionId	Collection ID	v
o	--documentId	Document ID	v
o	--data	Document data as JSON object. Include only attribute and value pairs to be updated	v
o	--read	An array of strings with read permissions. By default inherits the existing read permissions…	v
o	--write	An array of strings with write permissions. By default inherits the existing write permissions…	v
@	databases deleteDocument
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--documentId	Document ID	v
@	databases listDocumentLogs
o	--databaseId	Database ID	v
o	--collectionId	Collection ID	v
o	--documentId	Document ID	v
o	--limit	Maximum number of logs to return in response. By default will return maximum 25 results. Maximum…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
@	databases listIndexes
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
@	databases createIndex
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Index Key	v
o	--type	Index type	v
o	--attributes	Array of attributes to index. Maximum of 100 attributes are allowed, each 32 characters long	v
o	--orders	Array of index orders. Maximum of 100 orders are allowed	v
@	databases getIndex
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Index Key	v
@	databases deleteIndex
o	--databaseId	Database ID	v
o	--collectionId	Collection ID. You can create a new collection using the Database service [server…	v
o	--key	Index Key	v
@	databases listCollectionLogs
o	--databaseId	Database ID	v
o	--collectionId	Collection ID	v
o	--limit	Maximum number of logs to return in response. By default will return maximum 25 results. Maximum…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
@	databases getCollectionUsage
o	--databaseId	Database ID	v
o	--collectionId	Collection ID	v
o	--range	Date range	v
@	databases listLogs
o	--databaseId	Database ID	v
o	--limit	Maximum number of logs to return in response. By default will return maximum 25 results. Maximum…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
@	databases getDatabaseUsage
o	--databaseId	Database ID	v
o	--range	'Date range	v
@	functions
s	list	Get a list of all the project's functions. You can use the query params to filter your results
s	create	Create a new function. You can pass a list of [permissions](/docs/permissions) to allow different…
s	listRuntimes	Get a list of all runtimes that are currently active on your instance
s	get	Get a function by its unique ID
s	update	Update function by its unique ID
s	delete	Delete a function by its unique ID
s	listDeployments	Get a list of all the project's code deployments. You can use the query params to filter your…
s	createDeployment	Create a new function code deployment. Use this endpoint to upload a new version of your code…
s	getDeployment	Get a code deployment by its unique ID
s	updateDeployment	Update the function code deployment ID using the unique function ID. Use this endpoint to switch…
s	deleteDeployment	Delete a code deployment by its unique ID
s	retryBuild	
s	listExecutions	Get a list of all the current user function execution logs. You can use the query params to filter…
s	createExecution	Trigger a function execution. The returned object will return you the current execution status…
s	getExecution	Get a function execution log by its unique ID
s	getUsage	
@	functions list
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Maximum number of functions to return in response. By default will return maximum 25 results…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
o	--cursor	ID of the function used as the starting point for the query, excluding the function itself. Should…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	functions create
o	--functionId	Function ID. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid…	v
o	--name	Function name. Max length: 128 chars	v
o	--execute	An array of strings with execution permissions. By default no user is granted with any execute…	v
o	--runtime	Execution runtime	v
o	--vars	Key-value JSON object that will be passed to the function as environment variables	v
o	--events	Events list. Maximum of 100 events are allowed	v
o	--schedule	Schedule CRON syntax	v
o	--timeout	Function maximum execution time in seconds	v
@	functions listRuntimes
@	functions get
o	--functionId	Function ID	v
@	functions update
o	--functionId	Function ID	v
o	--name	Function name. Max length: 128 chars	v
o	--execute	An array of strings with execution permissions. By default no user is granted with any execute…	v
o	--vars	Key-value JSON object that will be passed to the function as environment variables	v
o	--events	Events list. Maximum of 100 events are allowed	v
o	--schedule	Schedule CRON syntax	v
o	--timeout	Maximum execution time in seconds	v
@	functions delete
o	--functionId	Function ID	v
@	functions listDeployments
o	--functionId	Function ID	v
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Maximum number of deployments to return in response. By default will return maximum 25 results…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
o	--cursor	ID of the deployment used as the starting point for the query, excluding the deployment itself…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	functions createDeployment
o	--functionId	Function ID	v
o	--entrypoint	Entrypoint File	v
o	--code	Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code…	v
o	--activate	Automatically activate the deployment when it is finished building	v
@	functions getDeployment
o	--functionId	Function ID	v
o	--deploymentId	Deployment ID	v
@	functions updateDeployment
o	--functionId	Function ID	v
o	--deploymentId	Deployment ID	v
@	functions deleteDeployment
o	--functionId	Function ID	v
o	--deploymentId	Deployment ID	v
@	functions retryBuild
o	--functionId	Function ID	v
o	--deploymentId	Deployment ID	v
o	--buildId	Build unique ID	v
@	functions listExecutions
o	--functionId	Function ID	v
o	--limit	Maximum number of executions to return in response. By default will return maximum 25 results…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--cursor	ID of the execution used as the starting point for the query, excluding the execution itself…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
@	functions createExecution
o	--functionId	Function ID	v
o	--data	String of custom data to send to function	v
o	--async	Execute code asynchronously. Default value is true	v
@	functions getExecution
o	--functionId	Function ID	v
o	--executionId	Execution ID	v
@	functions getUsage
o	--functionId	Function ID	v
o	--range	Date range	v
@	health
s	get	Check the Appwrite HTTP server is up and responsive
s	getAntivirus	Check the Appwrite Antivirus server is up and connection is successful
s	getCache	Check the Appwrite in-memory cache server is up and connection is successful
s	getDB	Check the Appwrite database server is up and connection is successful
s	getQueueCertificates	Get the number of certificates that are waiting to be issued against…
s	getQueueFunctions	
s	getQueueLogs	Get the number of logs that are waiting to be processed in the Appwrite internal queue server
s	getQueueWebhooks	Get the number of webhooks that are waiting to be processed in the Appwrite internal queue server
s	getStorageLocal	Check the Appwrite local storage device is up and connection is successful
s	getTime	Check the Appwrite server time is synced with Google remote NTP server. We use this technology to…
@	health get
@	health getAntivirus
@	health getCache
@	health getDB
@	health getQueueCertificates
@	health getQueueFunctions
@	health getQueueLogs
@	health getQueueWebhooks
@	health getStorageLocal
@	health getTime
@	locale
s	get	Get the current user location based on IP. Returns an object with user country code, country name…
s	getContinents	List of all continents. You can use the locale header to get the data in a supported language
s	getCountries	List of all countries. You can use the locale header to get the data in a supported language
s	getCountriesEU	List of all countries that are currently members of the EU. You can use the locale header to get…
s	getCountriesPhones	List of all countries phone codes. You can use the locale header to get the data in a supported…
s	getCurrencies	List of all currencies, including currency symbol, name, plural, and decimal digits for all major…
s	getLanguages	List of all languages classified by ISO 639-1 including 2-letter code, name in English, and name…
@	locale get
@	locale getContinents
@	locale getCountries
@	locale getCountriesEU
@	locale getCountriesPhones
@	locale getCurrencies
@	locale getLanguages
@	projects
s	list	
s	create	
s	get	
s	update	
s	delete	
s	updateAuthLimit	
s	updateAuthStatus	
s	listDomains	
s	createDomain	
s	getDomain	
s	deleteDomain	
s	updateDomainVerification	
s	listKeys	
s	createKey	
s	getKey	
s	updateKey	
s	deleteKey	
s	updateOAuth2	
s	listPlatforms	
s	createPlatform	
s	getPlatform	
s	updatePlatform	
s	deletePlatform	
s	updateServiceStatus	
s	getUsage	
s	listWebhooks	
s	createWebhook	
s	getWebhook	
s	updateWebhook	
s	deleteWebhook	
s	updateWebhookSignature	
@	projects list
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per…	v
o	--offset	Results offset. The default value is 0. Use this param to manage pagination. [learn more about…	v
o	--cursor	ID of the project used as the starting point for the query, excluding the project itself. Should…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	projects create
o	--projectId	Unique Id. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid…	v
o	--name	Project name. Max length: 128 chars	v
o	--teamId	Team unique ID	v
o	--description	Project description. Max length: 256 chars	v
o	--logo	Project logo	v
o	--url	Project URL	v
o	--legalName	Project legal Name. Max length: 256 chars	v
o	--legalCountry	Project legal Country. Max length: 256 chars	v
o	--legalState	Project legal State. Max length: 256 chars	v
o	--legalCity	Project legal City. Max length: 256 chars	v
o	--legalAddress	Project legal Address. Max length: 256 chars	v
o	--legalTaxId	Project legal Tax ID. Max length: 256 chars	v
@	projects get
o	--projectId	Project unique ID	v
@	projects update
o	--projectId	Project unique ID	v
o	--name	Project name. Max length: 128 chars	v
o	--description	Project description. Max length: 256 chars	v
o	--logo	Project logo	v
o	--url	Project URL	v
o	--legalName	Project legal name. Max length: 256 chars	v
o	--legalCountry	Project legal country. Max length: 256 chars	v
o	--legalState	Project legal state. Max length: 256 chars	v
o	--legalCity	Project legal city. Max length: 256 chars	v
o	--legalAddress	Project legal address. Max length: 256 chars	v
o	--legalTaxId	Project legal tax ID. Max length: 256 chars	v
@	projects delete
o	--projectId	Project unique ID	v
o	--password	Your user password for confirmation. Must be at least 8 chars	v
@	projects updateAuthLimit
o	--projectId	Project unique ID	v
o	--limit	Set the max number of users allowed in this project. Use 0 for unlimited	v
@	projects updateAuthStatus
o	--projectId	Project unique ID	v
o	--method	Auth Method. Possible values: email-password,magic-url,anonymous,invites,jwt,phone	v
o	--status	Set the status of this auth method	v
@	projects listDomains
o	--projectId	Project unique ID	v
@	projects createDomain
o	--projectId	Project unique ID	v
o	--domain	Domain name	v
@	projects getDomain
o	--projectId	Project unique ID	v
o	--domainId	Domain unique ID	v
@	projects deleteDomain
o	--projectId	Project unique ID	v
o	--domainId	Domain unique ID	v
@	projects updateDomainVerification
o	--projectId	Project unique ID	v
o	--domainId	Domain unique ID	v
@	projects listKeys
o	--projectId	Project unique ID	v
@	projects createKey
o	--projectId	Project unique ID	v
o	--name	Key name. Max length: 128 chars	v
o	--scopes	Key scopes list. Maximum of 100 scopes are allowed	v
o	--expire	Key expiration time in Unix timestamp. Use 0 for unlimited expiration	v
@	projects getKey
o	--projectId	Project unique ID	v
o	--keyId	Key unique ID	v
@	projects updateKey
o	--projectId	Project unique ID	v
o	--keyId	Key unique ID	v
o	--name	Key name. Max length: 128 chars	v
o	--scopes	Key scopes list. Maximum of 100 events are allowed	v
o	--expire	Key expiration time in Unix timestamp. Use 0 for unlimited expiration	v
@	projects deleteKey
o	--projectId	Project unique ID	v
o	--keyId	Key unique ID	v
@	projects updateOAuth2
o	--projectId	Project unique ID	v
o	--provider	Provider Name	v
o	--appId	Provider app ID. Max length: 256 chars	v
o	--secret	Provider secret key. Max length: 512 chars	v
@	projects listPlatforms
o	--projectId	Project unique ID	v
@	projects createPlatform
o	--projectId	Project unique ID	v
o	--type	Platform type	v
o	--name	Platform name. Max length: 128 chars	v
o	--key	Package name for Android or bundle ID for iOS or macOS. Max length: 256 chars	v
o	--store	App store or Google Play store ID. Max length: 256 chars	v
o	--hostname	Platform client hostname. Max length: 256 chars	v
@	projects getPlatform
o	--projectId	Project unique ID	v
o	--platformId	Platform unique ID	v
@	projects updatePlatform
o	--projectId	Project unique ID	v
o	--platformId	Platform unique ID	v
o	--name	Platform name. Max length: 128 chars	v
o	--key	Package name for android or bundle ID for iOS. Max length: 256 chars	v
o	--store	App store or Google Play store ID. Max length: 256 chars	v
o	--hostname	Platform client URL. Max length: 256 chars	v
@	projects deletePlatform
o	--projectId	Project unique ID	v
o	--platformId	Platform unique ID	v
@	projects updateServiceStatus
o	--projectId	Project unique ID	v
o	--service	Service name	v
o	--status	Service status	v
@	projects getUsage
o	--projectId	Project unique ID	v
o	--range	Date range	v
@	projects listWebhooks
o	--projectId	Project unique ID	v
@	projects createWebhook
o	--projectId	Project unique ID	v
o	--name	Webhook name. Max length: 128 chars	v
o	--events	Events list. Maximum of 100 events are allowed	v
o	--url	Webhook URL	v
o	--security	Certificate verification, false for disabled or true for enabled	v
o	--httpUser	Webhook HTTP user. Max length: 256 chars	v
o	--httpPass	Webhook HTTP password. Max length: 256 chars	v
@	projects getWebhook
o	--projectId	Project unique ID	v
o	--webhookId	Webhook unique ID	v
@	projects updateWebhook
o	--projectId	Project unique ID	v
o	--webhookId	Webhook unique ID	v
o	--name	Webhook name. Max length: 128 chars	v
o	--events	Events list. Maximum of 100 events are allowed	v
o	--url	Webhook URL	v
o	--security	Certificate verification, false for disabled or true for enabled	v
o	--httpUser	Webhook HTTP user. Max length: 256 chars	v
o	--httpPass	Webhook HTTP password. Max length: 256 chars	v
@	projects deleteWebhook
o	--projectId	Project unique ID	v
o	--webhookId	Webhook unique ID	v
@	projects updateWebhookSignature
o	--projectId	Project unique ID	v
o	--webhookId	Webhook unique ID	v
@	storage
s	listBuckets	Get a list of all the storage buckets. You can use the query params to filter your results
s	createBucket	Create a new storage bucket
s	getBucket	Get a storage bucket by its unique ID. This endpoint response returns a JSON object with the…
s	updateBucket	Update a storage bucket by its unique ID
s	deleteBucket	Delete a storage bucket by its unique ID
s	listFiles	Get a list of all the user files. You can use the query params to filter your results. On admin…
s	createFile	Create a new file. Before using this route, you should create a new bucket resource using either a…
s	getFile	Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata
s	updateFile	Update a file by its unique ID. Only users with write permissions have access to update this…
s	deleteFile	Delete a file by its unique ID. Only users with write permissions have access to delete this…
s	getFileDownload	Get a file content by its unique ID. The endpoint response return with a 'Content-Disposition…
s	getFilePreview	Get a file preview image. Currently, this method supports preview for image files (jpg, png, and…
s	getFileView	Get a file content by its unique ID. This endpoint is similar to the download method but returns…
s	getUsage	
s	getBucketUsage	
@	storage listBuckets
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per…	v
o	--offset	Results offset. The default value is 0. Use this param to manage pagination	v
o	--cursor	ID of the bucket used as the starting point for the query, excluding the bucket itself. Should be…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	storage createBucket
o	--bucketId	Unique Id. Choose your own unique ID or pass the string 'unique()' to auto generate it. Valid…	v
o	--name	Bucket name	v
o	--permission	Permissions type model to use for reading files in this bucket. You can use bucket-level…	v
o	--read	An array of strings with read permissions. By default no user is granted with any read…	v
o	--write	An array of strings with write permissions. By default no user is granted with any write…	v
o	--enabled	Is bucket enabled?	v
o	--maximumFileSize	Maximum file size allowed in bytes. Maximum allowed value is 30MB. For self-hosted setups you can…	v
o	--allowedFileExtensions	Allowed file extensions. Maximum of 100 extensions are allowed, each 64 characters long	v
o	--encryption	Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled	v
o	--antivirus	Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's…	v
@	storage getBucket
o	--bucketId	Bucket unique ID	v
@	storage updateBucket
o	--bucketId	Bucket unique ID	v
o	--name	Bucket name	v
o	--permission	Permissions type model to use for reading files in this bucket. You can use bucket-level…	v
o	--read	An array of strings with read permissions. By default inherits the existing read permissions…	v
o	--write	An array of strings with write permissions. By default inherits the existing write permissions…	v
o	--enabled	Is bucket enabled?	v
o	--maximumFileSize	Maximum file size allowed in bytes. Maximum allowed value is 30MB. For self hosted version you can…	v
o	--allowedFileExtensions	Allowed file extensions. Maximum of 100 extensions are allowed, each 64 characters long	v
o	--encryption	Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled	v
o	--antivirus	Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's…	v
@	storage deleteBucket
o	--bucketId	Bucket unique ID	v
@	storage listFiles
o	--bucketId	Storage bucket unique ID. You can create a new storage bucket using the Storage service [server…	v
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Maximum number of files to return in response. By default will return maximum 25 results. Maximum…	v
o	--offset	Offset value. The default value is 0. Use this param to manage pagination. [learn more about…	v
o	--cursor	ID of the file used as the starting point for the query, excluding the file itself. Should be used…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	storage createFile
o	--bucketId	Storage bucket unique ID. You can create a new storage bucket using the Storage service [server…	v
o	--fileId	File ID. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid chars…	v
o	--file	Binary file	v
o	--read	An array of strings with read permissions. By default only the current user is granted with read…	v
o	--write	An array of strings with write permissions. By default only the current user is granted with write…	v
@	storage getFile
o	--bucketId	Storage bucket unique ID. You can create a new storage bucket using the Storage service [server…	v
o	--fileId	File ID	v
@	storage updateFile
o	--bucketId	Storage bucket unique ID. You can create a new storage bucket using the Storage service [server…	v
o	--fileId	File unique ID	v
o	--read	An array of strings with read permissions. By default no user is granted with any read…	v
o	--write	An array of strings with write permissions. By default no user is granted with any write…	v
@	storage deleteFile
o	--bucketId	Storage bucket unique ID. You can create a new storage bucket using the Storage service [server…	v
o	--fileId	File ID	v
@	storage getFileDownload
o	--bucketId	Storage bucket ID. You can create a new storage bucket using the Storage service [server…	v
o	--fileId	File ID	v
o	--destination	Output file path	v
@	storage getFilePreview
o	--bucketId	Storage bucket unique ID. You can create a new storage bucket using the Storage service [server…	v
o	--fileId	File ID	v
o	--width	Resize preview image width, Pass an integer between 0 to 4000	v
o	--height	Resize preview image height, Pass an integer between 0 to 4000	v
o	--gravity	Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,botto…	v
o	--quality	Preview image quality. Pass an integer between 0 to 100. Defaults to 100	v
o	--borderWidth	Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0	v
o	--borderColor	Preview image border color. Use a valid HEX color, no # is needed for prefix	v
o	--borderRadius	Preview image border radius in pixels. Pass an integer between 0 to 4000	v
o	--opacity	Preview image opacity. Only works with images having an alpha channel (like png). Pass a number…	v
o	--rotation	Preview image rotation in degrees. Pass an integer between -360 and 360	v
o	--background	Preview image background color. Only works with transparent images (png). Use a valid HEX color…	v
o	--output	Output format type (jpeg, jpg, png, gif and webp)	v
o	--destination	Output file path	v
@	storage getFileView
o	--bucketId	Storage bucket unique ID. You can create a new storage bucket using the Storage service [server…	v
o	--fileId	File ID	v
o	--destination	Output file path	v
@	storage getUsage
o	--range	Date range	v
@	storage getBucketUsage
o	--bucketId	Bucket ID	v
o	--range	Date range	v
@	teams
s	list	Get a list of all the teams in which the current user is a member. You can use the parameters to…
s	create	Create a new team. The user who creates the team will automatically be assigned as the owner of…
s	get	Get a team by its ID. All team members have read access for this resource
s	update	Update a team using its ID. Only members with the owner role can update the team
s	delete	Delete a team using its ID. Only team members with the owner role can delete the team
s	listLogs	Get the team activity logs list by its unique ID
s	getMemberships	Use this endpoint to list a team's members using the team's ID. All team members have read access…
s	createMembership	Invite a new member to join your team. If initiated from the client SDK, an email with a link to…
s	getMembership	Get a team member by the membership unique id. All team members have read access for this resource
s	updateMembershipRoles	Modify the roles of a team member. Only team members with the owner role have access to this…
s	deleteMembership	This endpoint allows a user to leave a team or for a team owner to delete the membership of any…
s	updateMembershipStatus	Use this endpoint to allow a user to accept an invitation to join a team after being redirected…
@	teams list
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Maximum number of teams to return in response. By default will return maximum 25 results. Maximum…	v
o	--offset	Offset value. The default value is 0. Use this param to manage pagination. [learn more about…	v
o	--cursor	ID of the team used as the starting point for the query, excluding the team itself. Should be used…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	teams create
o	--teamId	Team ID. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid chars…	v
o	--name	Team name. Max length: 128 chars	v
o	--roles	Array of strings. Use this param to set the roles in the team for the user who created it. The…	v
@	teams get
o	--teamId	Team ID	v
@	teams update
o	--teamId	Team ID	v
o	--name	New team name. Max length: 128 chars	v
@	teams delete
o	--teamId	Team ID	v
@	teams listLogs
o	--teamId	Team ID	v
o	--limit	Maximum number of logs to return in response. By default will return maximum 25 results. Maximum…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
@	teams getMemberships
o	--teamId	Team ID	v
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Maximum number of memberships to return in response. By default will return maximum 25 results…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
o	--cursor	ID of the membership used as the starting point for the query, excluding the membership itself…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	teams createMembership
o	--teamId	Team ID	v
o	--email	Email of the new team member	v
o	--roles	Array of strings. Use this param to set the user roles in the team. A role can be any string…	v
o	--url	URL to redirect the user back to your app from the invitation email. Only URLs from hostnames in…	v
o	--name	Name of the new team member. Max length: 128 chars	v
@	teams getMembership
o	--teamId	Team ID	v
o	--membershipId	Membership ID	v
@	teams updateMembershipRoles
o	--teamId	Team ID	v
o	--membershipId	Membership ID	v
o	--roles	An array of strings. Use this param to set the user's roles in the team. A role can be any string…	v
@	teams deleteMembership
o	--teamId	Team ID	v
o	--membershipId	Membership ID	v
@	teams updateMembershipStatus
o	--teamId	Team ID	v
o	--membershipId	Membership ID	v
o	--secret	Secret key	v
@	users
s	list	Get a list of all the project's users. You can use the query params to filter your results
s	create	Create a new user
s	getUsage	
s	get	Get a user by its unique ID
s	delete	Delete a user by its unique ID, thereby releasing it's ID. Since ID is released and can be reused…
s	updateEmail	Update the user email by its unique ID
s	getLogs	Get the user activity logs list by its unique ID
s	getMemberships	Get the user membership list by its unique ID
s	updateName	Update the user name by its unique ID
s	updatePassword	Update the user password by its unique ID
s	updatePhone	Update the user phone by its unique ID
s	getPrefs	Get the user preferences by its unique ID
s	updatePrefs	Update the user preferences by its unique ID. The object you pass is stored as is, and replaces…
s	getSessions	Get the user sessions list by its unique ID
s	deleteSessions	Delete all user's sessions by using the user's unique ID
s	deleteSession	Delete a user sessions by its unique ID
s	updateStatus	Update the user status by its unique ID. Use this endpoint as an alternative to deleting a user if…
s	updateEmailVerification	Update the user email verification status by its unique ID
s	updatePhoneVerification	Update the user phone verification status by its unique ID
@	users list
o	--search	Search term to filter your list results. Max length: 256 chars	v
o	--limit	Maximum number of users to return in response. By default will return maximum 25 results. Maximum…	v
o	--offset	Offset value. The default value is 0. Use this param to manage pagination. [learn more about…	v
o	--cursor	ID of the user used as the starting point for the query, excluding the user itself. Should be used…	v
o	--cursorDirection	Direction of the cursor, can be either 'before' or 'after'	v
o	--orderType	Order result by ASC or DESC order	v
@	users create
o	--userId	User ID. Choose your own unique ID or pass the string "unique()" to auto generate it. Valid chars…	v
o	--email	User email	v
o	--password	User password. Must be at least 8 chars	v
o	--name	User name. Max length: 128 chars	v
@	users getUsage
o	--range	Date range	v
o	--provider	Provider Name	v
@	users get
@	users delete
@	users updateEmail
o	--userId	User ID	v
o	--email	User email	v
@	users getLogs
o	--userId	User ID	v
o	--limit	Maximum number of logs to return in response. By default will return maximum 25 results. Maximum…	v
o	--offset	Offset value. The default value is 0. Use this value to manage pagination. [learn more about…	v
@	users getMemberships
o	--userId	User ID	v
@	users updateName
o	--userId	User ID	v
o	--name	User name. Max length: 128 chars	v
@	users updatePassword
o	--userId	User ID	v
o	--password	New user password. Must be at least 8 chars	v
@	users updatePhone
o	--userId	User ID	v
o	--number	User phone number	v
@	users getPrefs
o	--userId	User ID	v
@	users updatePrefs
o	--userId	User ID	v
o	--prefs	Prefs key-value JSON object	v
@	users getSessions
o	--userId	User ID	v
@	users deleteSessions
o	--userId	User ID	v
@	users deleteSession
o	--userId	User ID	v
o	--sessionId	Session ID	v
@	users updateStatus
o	--userId	User ID	v
o	--status	User Status. To activate the user pass 'true' and to block the user pass 'false'	v
@	users updateEmailVerification
o	--userId	User ID	v
o	--emailVerification	User email verification status	v
@	users updatePhoneVerification
o	--userId	User ID	v
o	--phoneVerification	User phone verification status	v
@	client
o	--selfSigned	Configure the CLI to use a self-signed certificate ( true or false )	v
o	--endpoint	Set your Apwrite server endpoint	v
o	--projectId	Set your Apwrite project ID	v
o	--key	Set your Apwrite server's API key	v
o	--debug	Print CLI debug information	
o	--reset	Reset the CLI configuration	
