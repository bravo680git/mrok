@	
s	create	Create things
s	delete	Delete things
s	get	Get things
s	list	List things
s	update	Update things
s	help	Help about any command
o	--help|-h	Display help	p
@	create
s	dns	Create a DNS record
s	paste	Create or update a paste
s	picture	Upload a picture to some.pics
s	purl	Create a PURL
s	status	Create a status
s	weblog	Create a weblog entry
@	create dns
o	--priority|-p	Priority of the DNS record	v
o	--ttl|-T	Time to live of the DNS record	v
a	3	0
@	create paste
o	--filename|-f	File to read paste from (default stdin)	v
o	--listed|-l	Create paste as listed (default false)	
a	1	0
=	create paste	--filename
t	filepaths
@	create picture
o	--description|-d	Description of the picture (default empty/unlisted)	
a	1	0
@	create purl
o	--listed|-l	Create as listed (default false)	
a	2	0
@	create status
o	--emoji|-e	Emoji to add to status (default sparkles)	v
o	--skip-mastodon-post	Do not cross-post to Mastodon	
a	1	0
@	create weblog
o	--filename|-f	File to read entry from (default stdin)	v
=	create weblog	--filename
t	filepaths
@	delete
s	account	Delete information about your account
s	dns	Delete a DNS record
s	paste	Delete a paste
s	picture	Delete a picture from some.pics
s	purl	Delete a PURL
s	status	Delete a status
s	weblog	Delete a weblog entry
@	delete account
s	session	Delete a session
@	delete account session
a	1	0
@	delete dns
a	1	0
@	delete paste
a	1	0
@	delete picture
a	1	0
@	delete purl
a	1	0
@	delete status
a	1	0
@	delete weblog
a	1	0
@	get
s	account	Get information about your account
s	address	Get information about an address
s	email	Get email forwarding address(es)
s	now	Get a Now page
s	paste	Get a paste
s	purl	Get a PURL
s	service	Get service stats
s	status	Get status
s	status-bio	Get status bio
s	theme	Get theme information
s	web	Get your webpage content
s	weblog	Get a weblog entry
@	get account
s	info	Get info about your account
s	name	Get your account name
s	settings	Get your account settings
@	get account info
@	get account name
@	get account settings
@	get address
s	availability	Get address availability
s	expiration	Get address expiration
s	info	Get information about an address
@	get address availability
a	1	0
@	get address expiration
a	1	0
@	get address info
s	private	Get private information about an address
s	public	Get public information about an address
@	get address info private
a	1	0
@	get address info public
a	1	0
@	get email
@	get now
o	--address|-a	Address whose Now page to get	v
o	--filename|-f	File to write Now page to (default stdout)	v
=	get now	--filename
t	filepaths
@	get paste
o	--address|-a	Address whose paste to get	v
o	--filename|-f	File to write paste to (default stdout)	v
a	1	0
=	get paste	--filename
t	filepaths
@	get purl
o	--address|-a	Address whose PURL to get	v
a	1	0
@	get service
@	get status
o	--address|-a	Address whose status to get	v
a	1	0
@	get status-bio
o	--address|-a	Address whose status bio to get	v
@	get theme
s	preview	Get theme preview
a	1	0
@	get theme preview
o	--filename|-f	File to write preview to (default stdout)	v
a	1	0
=	get theme preview	--filename
t	filepaths
@	get web
o	--filename|-f	File to write webpage to (default stdout)	v
=	get web	--filename
t	filepaths
@	get weblog
s	config	Get your weblog config
s	latest	Get the latest weblog entry
s	template	Get your weblog template
a	1	0
@	get weblog config
o	--filename|-f	File to write configuration to (default stdout)	v
=	get weblog config	--filename
t	filepaths
@	get weblog latest
@	get weblog template
o	--filename|-f	File to write template to (default stdout)	v
=	get weblog template	--filename
t	filepaths
@	list
s	account	List information about your account
s	directory	List the address directory
s	dns	List your dns records
s	now	List Now pages
s	paste	List pastes
s	picture	List pictures
s	purl	List all PURLs
s	status	List statuses
s	statuslog	List the statuslog
s	theme	List profile themes
s	weblog	List all weblog entries
@	list account
s	addresses	List your addresses
s	sessions	List your sessions
@	list account addresses
@	list account sessions
@	list directory
@	list dns
@	list now
@	list paste
o	--address|-a	Address whose pastes to list	v
@	list picture
@	list purl
o	--address|-a	Address whose PURLs to get	v
@	list status
o	--address|-a	Address whose status(es) to get	v
o	--limit|-l	How many status(es) to get (default all)	v
@	list statuslog
o	--all|-A	Get the entire statuslog (default is latest statuses only)	
@	list theme
@	list weblog
@	update
s	account	Update information about your account
s	dns	Update a DNS record
s	email	Set email forwarding address(es)
s	preference	Set a preference
s	set	Set Now page content
s	status	Update a status
s	status-bio	Update your status bio
s	web	Set webpage content
s	weblog	Set your weblog config
@	update account
s	name	Set the name on your account
s	settings	Set the settings on your account
@	update account name
@	update account settings
o	--communication|-c	Communication preference	v
o	--date-format|-d	Date format preference	v
o	--web-editor|-w	Web editor preference	v
@	update dns
o	--priority|-p	Updated priority	v
o	--ttl|-T	Updated TTL	v
@	update email
o	--destination|-d	Address(es) to forward to	v
@	update preference
@	update set
o	--filename|-f	File to read Now page from (default stdin)	v
o	--listed|-l	Create Now page as listed (default false)	
=	update set	--filename
t	filepaths
@	update status
o	--emoji|-e	Emoji to add to status (default sparkles)	v
@	update status-bio
@	update web
s	pfp	Set your profile picture
o	--filename|-f	File to read webpage from (default stdin)	v
o	--publish|-p	Publish the updated page (default false)	
=	update web	--filename
t	filepaths
@	update web pfp
@	update weblog
s	config	Set your weblog config
s	template	Set your weblog template
@	update weblog config
o	--filename|-f	File to read config from (default stdin)	v
=	update weblog config	--filename
t	filepaths
@	update weblog template
o	--filename|-f	File to read template from (default stdin)	v
=	update weblog template	--filename
t	filepaths
@	help
s	create	Create things
s	delete	Delete things
s	get	Get things
s	list	List things
s	update	Update things
@	help create
s	dns	Create a DNS record
s	paste	Create or update a paste
s	purl	Create a PURL
s	status	Create a status
s	weblog	Create a weblog entry
@	help create dns
@	help create paste
@	help create purl
@	help create status
@	help create weblog
@	help delete
s	account	Delete information about your account
s	dns	Delete a DNS record
s	paste	Delete a paste
s	purl	Delete a PURL
s	weblog	Delete a weblog entry
@	help delete account
s	session	Delete a session
@	help delete account session
@	help delete dns
@	help delete paste
@	help delete purl
@	help delete weblog
@	help get
s	account	Get information about your account
s	address	Get information about an address
s	email	Get email forwarding address(es)
s	now	Get a Now page
s	paste	Get a paste
s	purl	Get a PURL
s	service	Get service stats
s	status	Get status
s	status-bio	Get status bio
s	theme	Get theme information
s	web	Get your webpage content
s	weblog	Get a weblog entry
@	help get account
s	info	Get info about your account
s	name	Get your account name
s	settings	Get your account settings
@	help get account info
@	help get account name
@	help get account settings
@	help get address
s	availability	Get address availability
s	expiration	Get address expiration
s	info	Get information about an address
@	help get address availability
@	help get address expiration
@	help get address info
s	private	Get private information about an address
s	public	Get public information about an address
@	help get address info private
@	help get address info public
@	help get email
@	help get now
@	help get paste
@	help get purl
@	help get service
@	help get status
@	help get status-bio
@	help get theme
s	preview	Get theme preview
@	help get theme preview
@	help get web
@	help get weblog
s	config	Get your weblog config
s	latest	Get the latest weblog entry
s	template	Get your weblog template
@	help get weblog config
@	help get weblog latest
@	help get weblog template
@	help list
s	account	List information about your account
s	directory	List the address directory
s	dns	List your dns records
s	now	List Now pages
s	paste	List pastes
s	purl	List all PURLs
s	status	List statuses
s	statuslog	List the statuslog
s	theme	List profile themes
s	weblog	List all weblog entries
@	help list account
s	addresses	List your addresses
s	sessions	List your sessions
@	help list account addresses
@	help list account sessions
@	help list directory
@	help list dns
@	help list now
@	help list paste
@	help list purl
@	help list status
@	help list statuslog
@	help list theme
@	help list weblog
@	help update
s	account	Update information about your account
s	dns	Update a DNS record
s	email	Set email forwarding address(es)
s	preference	Set a preference
s	now	Update Now page content
s	status	Update a status
s	status-bio	Update your status bio
s	web	Set webpage content
s	weblog	Set your weblog config
@	help update account
s	name	Set the name on your account
s	settings	Set the settings on your account
@	help update account name
a	1	0
@	help update account settings
@	help update dns
a	4	0
@	help update email
a	1	0
@	help update preference
a	2	0
@	help update now
@	help update status
a	2	0
@	help update status-bio
a	1	0
@	help update web
s	pfp	Set your profile picture
@	help update web pfp
a	1	0
#	help update web pfp	1
t	filepaths
@	help update weblog
s	config	Set your weblog config
s	template	Set your weblog template
@	help update weblog config
@	help update weblog template
