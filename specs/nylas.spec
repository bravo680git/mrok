@	
s	api	Access the Nylas API endpoints
s	auth	Auth your email account
s	docs	Documentation lookup (preview)
s	init	Setup your dashboard application credentials
s	version	Gets the current CLI version
s	webhook	Create and test Nylas' Webhooks
s	help	Help about any command
o	--access_token	Nylas account access token	vp
o	--config_dir	Config directory	vp
o	--config_file	Config file (default is config.yaml)	vp
o	--dashboard_api_url	Dashboard API URL	vp
o	--debug	Enable debugging output	p
o	--disable_telemetry	Disables sending telemetry data	p
o	--nylas_api_url	Nylas API URL	vp
o	--output|-o	Output format (e.g. json, table)	vp
o	--region	Nylas Region (values: us, ireland, canada, australia)	vp
o	--silent	Silences the output	p
o	--help|-h	Display help	p
=		--config_dir
t	folders
=		--config_file
t	filepaths
=		--output
v	json	
v	table	
=		--region
v	us	
v	ireland	
v	canada	
v	australia	
@	api
s	a	A API commands
s	accounts	Gets a list of authed accounts
s	applications	Gets your application info
s	calendars	Calendars API commands
s	connect	Connect API commands
s	contacts	Contacts API commands
s	delta	Delta API commands
s	drafts	Drafts API commands
s	events	Events API commands
s	files	Files API commands
s	folders	Folders API commands
s	ip-addresses	Gets a list of Nylas IP addresses (paid customers only)
s	job-statuses	Job-Statuses API commands
s	labels	Labels API commands
s	messages	Messages API commands
s	neural	Neural API commands
s	resources	Resources API commands
s	send	Send API commands
s	send-rsvp	Send-Rsvp API commands
s	threads	Threads API commands
s	v2	V2 API commands
s	webhooks	Gets a list of webhooks
@	api a
s	accounts	Accounts commands
s	accounts:downgrade	Accounts:downgrade commands
s	accounts:revoke-all	Accounts:revoke-all commands
s	accounts:token-info	Accounts:token-info commands
s	accounts:upgrade	Accounts:upgrade commands
@	api a accounts
s	delete	Delete an Account
s	get	Return All Accounts
@	api a accounts delete
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api a accounts get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--limit	The number of objects to return. Defaults to 100. If set too high, requests may fail to prevent…	v
o	--metadata_key	Pass in your keys to search for metadata. `?metadata_key=goodmorning`. You can also combine this…	v
o	--metadata_pair	Pass in your metadata key and value pair to search for metadata…	v
o	--metadata_value	Pass in your value to search for metadata. `?metadata_value=goodnight`. You can also combine this…	v
o	--offset	Zero-based offset from default object sorting. See [pagination](/docs/api/#overview--pagintaion)…	v
@	api a accounts:downgrade
s	post	Cancel an Account
@	api a accounts:downgrade post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api a accounts:revoke-all
s	post	Revoke All Tokens
@	api a accounts:revoke-all post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api a accounts:token-info
s	post	Return Token Information
@	api a accounts:token-info post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api a accounts:upgrade
s	post	Reactivate an Account
@	api a accounts:upgrade post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api accounts
o	--limit|-l	This is usage	v
@	api applications
@	api calendars
s	availability	Availability commands
s	availability:consecutive	Availability:consecutive commands
s	delete	Delete a Calendar
s	free-busy	Free-busy commands
s	get	Return All Calendars
s	post	Create a Calendar
s	put	Update A Calendar
@	api calendars availability
s	post	Availability for a Single Meeting
@	api calendars availability post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api calendars availability:consecutive
s	post	Availability for Multiple Meetings
@	api calendars availability:consecutive post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api calendars delete
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api calendars free-busy
s	post	Calendar Free or Busy
@	api calendars free-busy post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api calendars get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--limit	The number of objects to return. Defaults to 100. If set too high, requests may fail to prevent…	v
o	--metadata_key	Pass in your keys to search for metadata. `?metadata_key=goodmorning`. You can also combine this…	v
o	--metadata_pair	Pass in your metadata key and value pair to search for metadata…	v
o	--metadata_value	Pass in your value to search for metadata. `?metadata_value=goodnight`. You can also combine this…	v
o	--offset	Zero-based offset from default object sorting. See [pagination](/docs/api/#overview--pagintaion)…	v
o	--view	If using Search, only `view=expanded` is supported. See [Views](/docs/api/#overview--views) for…	v
@	api calendars post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api calendars put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api connect
s	detect-provider	Detect-provider commands
@	api connect detect-provider
s	post	Detect Provider
@	api connect detect-provider post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api contacts
s	delete	Delete a Contact
s	get	Return All Contacts
s	groups	Groups commands
s	picture	Picture commands
s	post	Create a Contact
s	put	Update a Contact
@	api contacts delete
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api contacts get
o	--country	Returns the contacts matching the contact's exact physical addresses	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--email	Returns the contacts matching the exact contact's email	v
o	--group	Returns the contacts belonging to the Contact Group matching this ID	v
o	--limit	The number of objects to return. Defaults to 100. If set too high, requests may fail to prevent…	v
o	--offset	Zero-based offset from default object sorting. See [pagination](/docs/api/#overview--pagintaion)…	v
o	--phone_number	Returns the contacts matching the contact's exact phone number	v
o	--postal_code	Returns the contacts matching the contact's exact postal code of one of the contact's addresses	v
o	--source	Returns the contacts matching from the address book or auto-generated contacts from emails. For…	v
o	--state	Returns the contacts matching the contact's exact state for one of the contact's physical addresses	v
o	--street_address	Returns the contacts matching the one of the contact's exact street address	v
@	api contacts groups
s	get	Return Contact Groups
@	api contacts groups get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api contacts picture
s	get	Returns a Contacts Picture
@	api contacts picture get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api contacts post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api contacts put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api delta
s	get	Request Delta Cursors
s	latest:cursor	Latest:cursor commands
s	longpoll	Longpoll commands
s	streaming	Streaming commands
@	api delta get
o	--cursor	The data cursor from `/delta/latest_cursor`	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--excluded_types	A comma-separated list of object types to exclude from the returned deltas. You can not use…	v
o	--include_types	A comma-separated list of the object types that will only be included in the returned deltas. You…	v
o	--view	This value indicates if the data expands thread and message objects in the response to include…	v
@	api delta latest:cursor
s	post	Get a Delta Cursor
@	api delta latest:cursor post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api delta longpoll
s	get	Return Long-Polling Deltas
@	api delta longpoll get
o	--cursor	The data cursor from `/delta/latest_cursor`	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--excluded_types	A comma-separated list of object types to exclude from the returned deltas. You can not use…	v
o	--include_types	A comma-separated list of the object types that will only be included in the returned deltas. You…	v
o	--timeout	The time difference between the deltas retrieved	v
o	--view	This value indicates if the data expands thread and message objects in the response to include…	v
@	api delta streaming
s	get	Streaming Deltas
@	api delta streaming get
o	--cursor	The data cursor from `/delta/latest_cursor`	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--excluded_types	A comma-separated list of object types to exclude from the returned deltas. You can not use…	v
o	--include_types	A comma-separated list of the object types that will only be included in the returned deltas. You…	v
o	--view	This value indicates if the data expands thread and message objects in the response to include…	v
@	api drafts
s	delete	Delete a Draft
s	get	Return All Drafts
s	post	Create a New Draft
s	put	Update a Draft
@	api drafts delete
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api drafts get
o	--any_email	Return emails that have been sent or received from this comma-separated list of email addresses…	v
o	--bcc	Return threads containing messages that were BCC'd to this email address, likely sent from the…	v
o	--cc	Return threads containing messages that were CC'd to this email address	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--filename	Return object with the filename	v
o	--in	This parameter supports the name, display_name, or id of a folder or label. To return drafts, pass…	v
o	--last_message_after	Return threads whose most recent message was received after this Unix-based timestamp	v
o	--last_message_before	Return threads whose most recent message was received before this Unix-based timestamp	v
o	--not_in	Filter messages not in a given folder or label. The filter supports the name, display, or ID of a…	v
o	--started_after	Return threads whose first message was received after this Unix-based timestamp	v
o	--started_before	Return threads whose first message was received before this Unix-based timestamp	v
o	--subject	Return threads with a matching literal subject	v
o	--thread_id	Return messages belonging to a specific thread	v
o	--to	Return threads containing messages sent to this email address	v
o	--view	If using Search, only `view=expanded` is supported. See [Views](/docs/api/#overview--views) for…	v
@	api drafts post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api drafts put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api events
s	delete	Delete An Event
s	get	Return All Events
s	post	Create an Event
s	put	Update An Event
s	to-ics	To-ics commands
@	api events delete
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api events get
o	--calendar_id	Return events belonging to the specified calendar ID	v
o	--count	See [Count](/docs/api/#overview--count-view) for more information	v
o	--description	Return events matching the specified description	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--ends_after	Return events ending after the specified unix timestamp	v
o	--ends_before	Return events ending before the specified unix timestamp	v
o	--event_id	Return the event matching the specified event ID	v
o	--limit	The number of objects to return. Defaults to 100. If set too high, requests may fail to prevent…	v
o	--location	Return events matching the specified location	v
o	--metadata_key	Pass in your keys to search for metadata. `?metadata_key=goodmorning`. You can also combine this…	v
o	--metadata_pair	Pass in your metadata key and value pair to search for metadata…	v
o	--metadata_value	Pass in your value to search for metadata. `?metadata_value=goodnight`. You can also combine this…	v
o	--offset	Zero-based offset from default object sorting. See [pagination](/docs/api/#overview--pagintaion)…	v
o	--show_cancelled	Return events that have a status of `cancelled`. If an event is recurring, then it returns no…	v
o	--starts_after	Return events starting after the specified unix timestamp	v
o	--starts_before	Return events starting before the specified unix timestamp	v
o	--title	Return events matching the specified title	v
@	api events post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api events put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api events to-ics
s	post	Generate ICS File
@	api events to-ics post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api files
s	delete	Delete a File
s	download	Download commands
s	get	Return All Files
s	post	Upload a New File
@	api files delete
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api files download
s	get	Download a File
@	api files download get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api files get
o	--content_type	Return objects matching the specified content type	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--filename	Return object with the filename	v
o	--message_id	Return objects matching the specified message ID	v
o	--view	If using Search, only `view=expanded` is supported. See [Views](/docs/api/#overview--views) for…	v
@	api files post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api folders
s	delete	Delete a Folder
s	get	Return All Folders
s	post	Create a Folder
s	put	Update a Folder
@	api folders delete
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api folders get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--limit	The number of objects to return. Defaults to 100. If set too high, requests may fail to prevent…	v
o	--offset	Zero-based offset from default object sorting. See [pagination](/docs/api/#overview--pagintaion)…	v
@	api folders post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api folders put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api ip-addresses
@	api job-statuses
s	get	Return All Job Statuses
@	api job-statuses get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api labels
s	delete	Delete a Label
s	get	Return All Labels
s	post	Create a Label
s	put	Update a Label
@	api labels delete
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api labels get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--limit	The number of objects to return. Defaults to 100. If set too high, requests may fail to prevent…	v
o	--offset	Zero-based offset from default object sorting. See [pagination](/docs/api/#overview--pagintaion)…	v
@	api labels post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api labels put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api messages
s	get	Return All Messages
s	put	Update a Message
@	api messages get
o	--any_email	Return emails that have been sent or received from this comma-separated list of email addresses…	v
o	--bcc	Return threads containing messages that were BCC'd to this email address, likely sent from the…	v
o	--cc	Return threads containing messages that were CC'd to this email address	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--filename	Return object with the filename	v
o	--from	Return threads containing messages sent from this email address	v
o	--in	This parameter supports the name, display_name, or id of a folder or label. To return drafts, pass…	v
o	--limit	The number of objects to return. Defaults to 100. If set too high, requests may fail to prevent…	v
o	--not_in	Filter messages not in a given folder or label. The filter supports the name, display, or ID of a…	v
o	--offset	Zero-based offset from default object sorting. See [pagination](/docs/api/#overview--pagintaion)…	v
o	--received_after	Return messages received after this unix timestamp	v
o	--received_before	Return messages received before this unix timestamp	v
o	--subject	Return threads with a matching literal subject	v
o	--thread_id	Return messages belonging to a specific thread	v
o	--to	Return threads containing messages sent to this email address	v
o	--view	If using Search, only `view=expanded` is supported. See [Views](/docs/api/#overview--views) for…	v
@	api messages put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural
s	categorize	Categorize commands
s	categorize:feedback	Categorize:feedback commands
s	conversation	Conversation commands
s	conversation:feedback	Conversation:feedback commands
s	ocr	Ocr commands
s	ocr:feedback	Ocr:feedback commands
s	sentiment	Sentiment commands
s	sentiment:feedback	Sentiment:feedback commands
s	signature	Signature commands
s	signature:feedback	Signature:feedback commands
@	api neural categorize
s	put	Categorize a Message
@	api neural categorize put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural categorize:feedback
s	post	Categorize Message Feedback
@	api neural categorize:feedback post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural conversation
s	put	Clean Conversation
@	api neural conversation put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural conversation:feedback
s	post	Clean Conversations Feedback
@	api neural conversation:feedback post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural ocr
s	put	Optical Character Recognition
@	api neural ocr put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural ocr:feedback
s	post	Optical Character Recognition Feedback
@	api neural ocr:feedback post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural sentiment
s	put	Sentiment Analysis
@	api neural sentiment put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural sentiment:feedback
s	post	Sentiment Analysis Feedback
@	api neural sentiment:feedback post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural signature
s	put	Signature Extraction
@	api neural signature put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api neural signature:feedback
s	post	Signature Extraction Feedback
@	api neural signature:feedback post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api resources
s	get	Return Room Resource Information
@	api resources get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--limit	The number of objects to return. Defaults to 100. If set too high, requests may fail to prevent…	v
@	api send
s	post	Send a Message
@	api send post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api send-rsvp
s	post	Send RSVP
@	api send-rsvp post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api threads
s	get	Returns All Threads
s	put	Update a Thread
@	api threads get
o	--any_email	Return emails that have been sent or received from this comma-separated list of email addresses…	v
o	--bcc	Return threads containing messages that were BCC'd to this email address, likely sent from the…	v
o	--cc	Return threads containing messages that were CC'd to this email address	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
o	--filename	Return object with the filename	v
o	--from	Return threads containing messages sent from this email address	v
o	--in	This parameter supports the name, display_name, or id of a folder or label. To return drafts, pass…	v
o	--last_message_after	Return threads whose most recent message was received after this Unix-based timestamp	v
o	--last_message_before	Return threads whose most recent message was received before this Unix-based timestamp	v
o	--last_updated_after	Return threads whose most recent last updated date is after this Unix-based timestamp	v
o	--last_updated_before	Return threads whose most recent last updated date is before this Unix-based timestamp	v
o	--last_updated_timestamp	Return threads that been updated or changed recently. UNIX timestamp	v
o	--limit	The number of objects to return. Defaults to 100. If set too high, requests may fail to prevent…	v
o	--not_in	Filter messages not in a given folder or label. The filter supports the name, display, or ID of a…	v
o	--offset	Zero-based offset from default object sorting. See [pagination](/docs/api/#overview--pagintaion)…	v
o	--started_after	Return threads whose first message was received after this Unix-based timestamp	v
o	--started_before	Return threads whose first message was received before this Unix-based timestamp	v
o	--subject	Return threads with a matching literal subject	v
o	--to	Return threads containing messages sent to this email address	v
o	--view	If using Search, only `view=expanded` is supported. See [Views](/docs/api/#overview--views) for…	v
@	api threads put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api v2
s	outbox	Outbox commands
@	api v2 outbox
s	delete	Delete Scheduled Message
s	get	Return All Messages to Be Sent
s	post	Send a Message
s	put	Update Send Time
@	api v2 outbox delete
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api v2 outbox get
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api v2 outbox post
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api v2 outbox put
o	--body	Request body (or use < to redirect a JSON file)	v
o	--display_columns	(optional) A comma separated list of column headers to display for the table output	v
@	api webhooks
o	--limit|-l	This is usage	v
@	auth
@	docs
@	init
@	version
@	webhook
s	tunnel	Starts listening for incoming Nylas webhook events
@	webhook tunnel
o	--callback_domain	The domain for the callback URL	v
o	--forward|-f	Address to forward requests to (e.g. http://localhost:3000)	v
o	--print|-p	Prints the (json) payload to the console	
o	--triggers|-t	The triggers to register for your webhooks	v
o	--websocket_domain	The domain for the websocket server	v
=	webhook tunnel	--triggers
v	account.connected	
v	account.running	
v	account.stopped	
v	account.invalid	
v	account.sync_error	
v	message.created	
v	message.opened	
v	message.updated	
v	message.link_clicked	
v	message.bounced	
v	thread.replied	
v	calendar.created	
v	calendar.updated	
v	calendar.deleted	
v	event.created	
v	event.updated	
v	event.deleted	
v	contact.created	
v	contact.updated	
v	contact.updated	
v	contact.deleted	
v	job.successful	
v	job.failed	
@	help
s	api	Access the Nylas API endpoints
s	auth	Auth your email account
s	docs	Documentation lookup (preview)
s	init	Setup your dashboard application credentials
s	version	Gets the current CLI version
s	webhook	Create and test Nylas' Webhooks
@	help api
s	a	A API commands
s	accounts	Gets a list of authed accounts
s	applications	Gets your application info
s	calendars	Calendars API commands
s	connect	Connect API commands
s	contacts	Contacts API commands
s	delta	Delta API commands
s	drafts	Drafts API commands
s	events	Events API commands
s	files	Files API commands
s	folders	Folders API commands
s	ip-addresses	Gets a list of Nylas IP addresses (paid customers only)
s	job-statuses	Job-Statuses API commands
s	labels	Labels API commands
s	messages	Messages API commands
s	neural	Neural API commands
s	resources	Resources API commands
s	send	Send API commands
s	send-rsvp	Send-Rsvp API commands
s	threads	Threads API commands
s	v2	V2 API commands
s	webhooks	Gets a list of webhooks
@	help api a
s	accounts	Accounts commands
s	accounts:downgrade	Accounts:downgrade commands
s	accounts:revoke-all	Accounts:revoke-all commands
s	accounts:token-info	Accounts:token-info commands
s	accounts:upgrade	Accounts:upgrade commands
@	help api a accounts
s	delete	Delete an Account
s	get	Return All Accounts
@	help api a accounts delete
@	help api a accounts get
@	help api a accounts:downgrade
s	post	Cancel an Account
@	help api a accounts:downgrade post
@	help api a accounts:revoke-all
s	post	Revoke All Tokens
@	help api a accounts:revoke-all post
@	help api a accounts:token-info
s	post	Return Token Information
@	help api a accounts:token-info post
@	help api a accounts:upgrade
s	post	Reactivate an Account
@	help api a accounts:upgrade post
@	help api accounts
@	help api applications
@	help api calendars
s	availability	Availability commands
s	availability:consecutive	Availability:consecutive commands
s	delete	Delete a Calendar
s	free-busy	Free-busy commands
s	get	Return All Calendars
s	post	Create a Calendar
s	put	Update A Calendar
@	help api calendars availability
s	post	Availability for a Single Meeting
@	help api calendars availability post
@	help api calendars availability:consecutive
s	post	Availability for Multiple Meetings
@	help api calendars availability:consecutive post
@	help api calendars delete
@	help api calendars free-busy
s	post	Calendar Free or Busy
@	help api calendars free-busy post
@	help api calendars get
@	help api calendars post
@	help api calendars put
@	help api connect
s	detect-provider	Detect-provider commands
@	help api connect detect-provider
s	post	Detect Provider
@	help api connect detect-provider post
@	help api contacts
s	delete	Delete a Contact
s	get	Return All Contacts
s	groups	Groups commands
s	picture	Picture commands
s	post	Create a Contact
s	put	Update a Contact
@	help api contacts delete
@	help api contacts get
@	help api contacts groups
s	get	Return Contact Groups
@	help api contacts groups get
@	help api contacts picture
s	get	Returns a Contacts Picture
@	help api contacts picture get
@	help api contacts post
@	help api contacts put
@	help api delta
s	get	Request Delta Cursors
s	latest:cursor	Latest:cursor commands
s	longpoll	Longpoll commands
s	streaming	Streaming commands
@	help api delta get
@	help api delta latest:cursor
s	post	Get a Delta Cursor
@	help api delta latest:cursor post
@	help api delta longpoll
s	get	Return Long-Polling Deltas
@	help api delta longpoll get
@	help api delta streaming
s	get	Streaming Deltas
@	help api delta streaming get
@	help api drafts
s	delete	Delete a Draft
s	get	Return All Drafts
s	post	Create a New Draft
s	put	Update a Draft
@	help api drafts delete
@	help api drafts get
@	help api drafts post
@	help api drafts put
@	help api events
s	delete	Delete An Event
s	get	Return All Events
s	post	Create an Event
s	put	Update An Event
s	to-ics	To-ics commands
@	help api events delete
@	help api events get
@	help api events post
@	help api events put
@	help api events to-ics
s	post	Generate ICS File
@	help api events to-ics post
@	help api files
s	delete	Delete a File
s	download	Download commands
s	get	Return All Files
s	post	Upload a New File
@	help api files delete
@	help api files download
s	get	Download a File
@	help api files download get
@	help api files get
@	help api files post
@	help api folders
s	delete	Delete a Folder
s	get	Return All Folders
s	post	Create a Folder
s	put	Update a Folder
@	help api folders delete
@	help api folders get
@	help api folders post
@	help api folders put
@	help api ip-addresses
@	help api job-statuses
s	get	Return All Job Statuses
@	help api job-statuses get
@	help api labels
s	delete	Delete a Label
s	get	Return All Labels
s	post	Create a Label
s	put	Update a Label
@	help api labels delete
@	help api labels get
@	help api labels post
@	help api labels put
@	help api messages
s	get	Return All Messages
s	put	Update a Message
@	help api messages get
@	help api messages put
@	help api neural
s	categorize	Categorize commands
s	categorize:feedback	Categorize:feedback commands
s	conversation	Conversation commands
s	conversation:feedback	Conversation:feedback commands
s	ocr	Ocr commands
s	ocr:feedback	Ocr:feedback commands
s	sentiment	Sentiment commands
s	sentiment:feedback	Sentiment:feedback commands
s	signature	Signature commands
s	signature:feedback	Signature:feedback commands
@	help api neural categorize
s	put	Categorize a Message
@	help api neural categorize put
@	help api neural categorize:feedback
s	post	Categorize Message Feedback
@	help api neural categorize:feedback post
@	help api neural conversation
s	put	Clean Conversation
@	help api neural conversation put
@	help api neural conversation:feedback
s	post	Clean Conversations Feedback
@	help api neural conversation:feedback post
@	help api neural ocr
s	put	Optical Character Recognition
@	help api neural ocr put
@	help api neural ocr:feedback
s	post	Optical Character Recognition Feedback
@	help api neural ocr:feedback post
@	help api neural sentiment
s	put	Sentiment Analysis
@	help api neural sentiment put
@	help api neural sentiment:feedback
s	post	Sentiment Analysis Feedback
@	help api neural sentiment:feedback post
@	help api neural signature
s	put	Signature Extraction
@	help api neural signature put
@	help api neural signature:feedback
s	post	Signature Extraction Feedback
@	help api neural signature:feedback post
@	help api resources
s	get	Return Room Resource Information
@	help api resources get
@	help api send
s	post	Send a Message
@	help api send post
@	help api send-rsvp
s	post	Send RSVP
@	help api send-rsvp post
@	help api threads
s	get	Returns All Threads
s	put	Update a Thread
@	help api threads get
@	help api threads put
@	help api v2
s	outbox	Outbox commands
@	help api v2 outbox
s	delete	Delete Scheduled Message
s	get	Return All Messages to Be Sent
s	post	Send a Message
s	put	Update Send Time
@	help api v2 outbox delete
@	help api v2 outbox get
@	help api v2 outbox post
@	help api v2 outbox put
@	help api webhooks
@	help auth
@	help docs
@	help init
@	help version
@	help webhook
s	tunnel	Starts listening for incoming Nylas webhook events
@	help webhook tunnel
