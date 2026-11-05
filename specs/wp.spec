@	
s	cache	Adds, removes, fetches, and flushes the WP Object Cache object
s	cap	Adds, removes, and lists capabilities of a user role
s	cli	Reviews current WP-CLI info, checks for updates, or views defined aliases
s	comment	Creates, updates, deletes, and moderates comments
s	config	Generates and reads the wp-config.php file
s	core	Downloads, installs, updates, and manages a WordPress installation
s	cron	Tests, runs, and deletes WP-Cron events; manages WP-Cron schedules
s	db	Performs basic database operations using credentials stored in wp-config.php
s	dist-archive	Create a distribution archive based on a project’s .distignore file
s	embed	Inspects oEmbed providers, clears embed cache, and more
s	eval	Executes arbitrary PHP code
s	eval-file	Loads and executes a PHP file
s	export	Exports WordPress content to a WXR file
s	find	Find WordPress installations on the filesystem
s	help	Gets help on WP-CLI, or on a specific command
s	i18n	Provides internationalization tools for WordPress projects
s	import	Imports content from a given WXR file
s	language	Installs, activates, and manages language packs
s	maintenance-mode	Activates, deactivates or checks the status of the maintenance mode of a site
s	media	Imports files as attachments, regenerates thumbnails, or lists registered image sizes
s	menu	Lists, creates, assigns, and deletes the active theme’s navigation menus
s	network	Perform network-wide operations
s	option	Retrieves and sets site options, including plugin and WordPress settings
s	package	Lists, installs, and removes WP-CLI packages
s	plugin	Manages plugins, including installs, activations, and updates
s	post	Manages posts, content, and meta
s	post-type	Retrieves details on the site’s registered post types
s	profile	
s	rewrite	Lists or flushes the site’s rewrite rules, updates the permalink structure
s	role	Manages user roles, including creating new roles and resetting to defaults
s	scaffold	Generates code for post types, taxonomies, plugins, child themes, etc
s	search-replace	Searches/replaces strings in the database
s	server	Launches PHP’s built-in web server for a specific WordPress installation
s	shell	Opens an interactive PHP console for running and testing PHP code
s	sidebar	Lists registered sidebars
s	site	Creates, deletes, empties, moderates, and lists one or more sites on a multisite installation
s	super-admin	Lists, adds, or removes super admin users on a multisite installation
s	taxonomy	Retrieves information about registered taxonomies
s	term	Manages taxonomy terms and term meta, with create, delete, and list commands
s	theme	Manages themes, including installs, activations, and updates
s	transient	Adds, gets, and deletes entries in the WordPress Transient Cache
s	user	Manages users, along with their roles, capabilities, and meta
s	widget	Manages widgets, including adding and moving them within sidebars
@	cache
s	add	Adds a value to the object cache
s	decr	Decrements a value in the object cache
s	delete	Removes a value from the object cache
s	flush	Flushes the object cache
s	get	Gets a value from the object cache
s	incr	Increments a value in the object cache
s	replace	Replaces a value in the object cache, if the value already exists
s	set	Sets a value to the object cache, regardless of whether it already exists
s	type	Attempts to determine which object cache is being used
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	cache	--path
t	filepaths
=	cache	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	cache	--user
v	id	
v	login	
v	email	
@	cache add
a	4	0
@	cache decr
a	3	0
@	cache delete
a	2	0
@	cache flush
@	cache get
a	2	0
@	cache incr
a	3	0
@	cache replace
a	4	0
@	cache set
a	4	0
@	cache type
@	cap
s	add	Adds a value to the object cache
s	list	Lists capabilities for a given role
s	remove	Removes capabilities from a given role
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	cap	--path
t	filepaths
=	cap	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	cap	--user
v	id	
v	login	
v	email	
@	cap add
o	--grant	Adds the capability as an explicit boolean value, instead of implicitly defaulting to true	v
a	2	0
=	cap add	--grant
v	true	
v	false	
@	cap list
o	--format	Render output in a particular format	v=
o	--show-grant	Display all capabilities defined for a role including grant	
a	1	0
=	cap list	--format
v	list	
v	table	
v	csv	
v	json	
v	count	
v	yaml	
@	cap remove
a	2	0
@	cli
s	alias	Retrieves, sets and updates aliases for WordPress Installations
s	cache	Manages the internal WP-CLI cache,
s	check-update	Checks to see if there is a newer version of WP-CLI available
s	cmd-dump	Dumps the list of installed commands, as JSON
s	completions	Generates tab completion strings
s	has-command	Detects if a command exists
s	info	Prints various details about the WP-CLI environment
s	param-dump	Dumps the list of global parameters, as JSON or in var_export format
s	update	Updates WP-CLI to the latest release
s	version	Prints WP-CLI version
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	cli	--path
t	filepaths
=	cli	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	cli	--user
v	id	
v	login	
v	email	
@	cli alias
s	add	Creates an alias
s	delete	Deletes an alias
s	get	Gets the value for an alias
s	list	Lists available WP-CLI aliases
s	update	Updates an alias
@	cli alias add
o	--set-user	Set user for alias	v=
o	--set-url	Set url for alias	v=
o	--set-path	Set path for alias	v=
o	--set-ssh	Set ssh for alias	v=
o	--set-http	Set http for alias	v=
o	--grouping	For grouping multiple aliases	v=
o	--config	Config file to be considered for operations	v=
a	1	0
=	cli alias add	--set-path
t	folders
=	cli alias add	--config
v	global	
v	project	
@	cli alias delete
o	--config	Config file to be considered for operations	v=
a	1	0
=	cli alias delete	--config
v	global	
v	project	
@	cli alias get
a	1	0
@	cli alias list
o	--format	Set user for alias	v=
=	cli alias list	--format
v	yaml	
v	json	
v	var_export	
@	cli alias update
o	--set-user	Set user for alias	v=
o	--set-url	Set url for alias	v=
o	--set-path	Set path for alias	v=
o	--set-ssh	Set ssh for alias	v=
o	--set-http	Set http for alias	v=
o	--grouping	For grouping multiple aliases	v=
o	--config	Config file to be considered for operations	v=
a	1	0
=	cli alias update	--set-path
t	folders
=	cli alias update	--config
v	global	
v	project	
@	cli cache
s	clear	Clears the internal cache
s	prune	Prunes the internal cache
@	cli cache clear
@	cli cache prune
@	cli check-update
o	--patch	Only list patch updates	
o	--minor	Only list minor updates	
o	--major	Only list major updates	
o	--field	Prints the value of a single field for each update	v=
o	--fields	Limit the output to specific object fields. Defaults to version,update_type,package_url	v=
o	--format	Render output in a particular format	v=
=	cli check-update	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
@	cli cmd-dump
@	cli completions
o	--line	The current command line to be executed	v=
o	--point	The index to the current cursor position relative to the beginning of the command	v=
@	cli has-command
a	1	0
@	cli info
o	--format	Render output in a particular format	v=
=	cli info	--format
v	list	
v	json	
@	cli param-dump
o	--with-values	Display current values also	
o	--format	Render output in a particular format	v=
=	cli param-dump	--format
v	var_export	
v	json	
@	cli update
o	--patch	Only perform patch updates	
o	--minor	Only perform minor updates	
o	--major	Only perform major updates	
o	--stable	Update to the latest stable release. Skips update check	
o	--nightly	Update to the latest built version of the master branch. Potentially unstable	
o	--yes	Do not prompt for confirmation	
o	--insecure	Retry without certificate validation if TLS handshake fails. Note: This makes the request…	
@	cli version
@	comment
s	approve	Approves a comment
s	count	Counts comments, on whole blog or on a given post
s	create	Creates a new comment
s	delete	Deletes a comment
s	exists	Verifies whether a comment exists
s	generate	Generates some number of new dummy comments
s	get	Gets the data of a single comment
s	list	Gets a list of comments
s	meta	Adds, updates, deletes, and lists comment custom fields
s	recount	Recalculates the comment_count value for one or more posts
s	spam	Marks a comment as spam
s	status	Gets the status of a comment
s	trash	Trashes a comment
s	unapprove	Unapproves a comment
s	unspam	Unmarks a comment as spam
s	untrash	Untrashes a comment
s	update	Updates one or more comments
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	comment	--path
t	filepaths
=	comment	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	comment	--user
v	id	
v	login	
v	email	
@	comment approve
a	1	0
@	comment count
a	1	0
@	comment create
o	--field=value	Associative args for the new comment. See wp_insert_comment()	v
o	--porcelain	Output just the new comment id	
@	comment delete
o	--force	Skip the trash bin	
a	1	0
@	comment exists
a	1	0
@	comment generate
o	--count	How many comments to generate?	v=
o	--post_id	Assign comments to a specific post	v=
o	--format	Render output in a particular format	v=
=	comment generate	--count
v	100	
=	comment generate	--format
v	progress	
v	ids	
@	comment get
o	--field	Instead of returning the whole comment, returns the value of a single field	v=
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	comment get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	comment list
o	--field=value	One or more args to pass to WP_Comment_Query	
o	--field	Prints the value of a single field for each comment	v=
o	--fields	Limit the output to specific object fields	v=
o	--format	Render output in a particular format	v=
=	comment list	--format
v	table	
v	ids	
v	csv	
v	json	
v	count	
v	yaml	
@	comment meta
s	add	Add a meta field
s	delete	Delete a meta field
s	get	Get meta field value
s	list	List all metadata associated with an object
s	patch	Update a nested value for a meta field
s	pluck	Get a nested value from a meta field
s	update	Update a meta field
@	comment meta add
o	--format	The serialization format for the value	v=
a	3	0
=	comment meta add	--format
v	plaintext	
v	json	
@	comment meta delete
o	--all	Delete all meta for the object	
a	3	0
@	comment meta get
o	--format	Get value in a particular format	v=
a	2	0
=	comment meta get	--format
v	var_export	
v	json	
v	yaml	
@	comment meta list
o	--keys	Limit output to metadata of specific keys	v=
o	--fields	Limit the output to specific row fields. Defaults to id,meta_key,meta_value	v=
o	--format	Render output in a particular format	v=
o	--orderby	Set orderby which field	v=
o	--order	Set ascending or descending order	v=
o	--unserialize	Unserialize meta_value output	
a	1	0
=	comment meta list	--format
v	table	
v	csv	
v	json	
v	yaml	
v	count	
=	comment meta list	--orderby
v	id	
v	meta_key	
v	meta_value	
=	comment meta list	--order
v	asc	
v	desc	
@	comment meta patch
o	--format	The serialization format for the value	v=
a	5	0
=	comment meta patch	--format
v	plaintext	
v	json	
#	comment meta patch	1
v	insert	
v	update	
v	delete	
@	comment meta pluck
o	--format	The output format of the value	v=
a	3	0
=	comment meta pluck	--format
v	plaintext	
v	json	
v	yaml	
@	comment meta update
o	--format	The serialization format for the value	v=
a	3	0
=	comment meta update	--format
v	plaintext	
v	json	
@	comment recount
a	1	0
@	comment spam
a	1	0
@	comment status
a	1	0
@	comment trash
a	1	0
@	comment unapprove
a	1	0
@	comment unspam
a	1	0
@	comment untrash
a	1	0
@	comment update
o	--field=value	One or more fields to update. See wp_update_comment()	
a	1	0
@	config
s	create	Generates a wp-config.php file
s	delete	Deletes a specific constant or variable from the wp-config.php file
s	edit	Launches system editor to edit the wp-config.php file
s	get	Gets the value of a specific constant or variable defined in wp-config.php file
s	has	Checks whether a specific constant or variable exists in the wp-config.php file
s	list	Lists variables, constants, and file includes defined in wp-config.php file
s	path	Gets the path to wp-config.php file
s	set	Sets the value of a specific constant or variable defined in wp-config.php file
s	shuffle-salts	Refreshes the salts defined in the wp-config.php file
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	config	--path
t	filepaths
=	config	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	config	--user
v	id	
v	login	
v	email	
@	config create
o	--dbname	Set the database name	v=
o	--dbuser	Set the database user	v=
o	--dbpass	Set the database password	v=
o	--dbhost	Set the database host	v=
o	--dbprefix	Set the database table prefix	v=
o	--dbcharset	Set the database charset	v=
o	--dbcollate	Set the database collation	v=
o	--locale	Set the WPLANG constant. Defaults to $wp_local_package variable	v=
o	--extra-php	If set, the command copies additional PHP code into wp-config.php from STDIN	
o	--skip-salts	If set, keys and salts won’t be generated, but should instead be passed via --extra-php	
o	--skip-check	If set, the database connection is not checked	
o	--force	Overwrites existing files, if present	
o	--insecure	Retry API download without certificate validation if TLS handshake fails. Note: This makes the…	
=	config create	--dbpass
v	plaintext	
v	json	
=	config create	--dbhost
v	localhost	
=	config create	--dbprefix
v	wp_	
=	config create	--dbcharset
v	utf8	
@	config delete
o	--type	Type of the config value to delete. Defaults to ‘all’	v=
a	1	0
=	config delete	--type
v	constant	
v	variable	
v	all	
@	config edit
@	config get
o	--type	Type of the config value to delete. Defaults to ‘all’	v=
o	--format	Get value in a particular format	v=
a	1	0
=	config get	--type
v	constant	
v	variable	
v	all	
=	config get	--format
v	var_export	
v	json	
v	yaml	
@	config has
o	--type	Type of the config value to delete. Defaults to ‘all’	v=
a	1	0
=	config has	--type
v	constant	
v	variable	
v	all	
@	config list
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
o	--strict	Enforce strict matching when a filter is provided	
a	1	0
=	config list	--format
v	table	
v	csv	
v	json	
v	yaml	
@	config path
@	config set
o	--add	Add the value if it doesn’t exist yet. This is the default behavior, override with –no-add	
o	--no-add	Add the value if it doesn’t exist yet. This is the default behavior, override with –no-add	
o	--raw	Place the value into the wp-config.php file as is, instead of as a quoted string	
o	--anchor	Anchor string where additions of new values are anchored around. Defaults to “/* That’s all, stop…	v=
o	--placement	Where to place the new values in relation to the anchor string	v=
o	--separator	Separator string to put between an added value and its anchor string. The following escape…	v=
o	--type	Type of the config value to set. Defaults to ‘all’	v=
a	2	0
=	config set	--placement
v	before	
v	after	
=	config set	--type
v	constant	
v	variable	
v	all	
@	config shuffle-salts
o	--force	If an unknown key is requested to be shuffled, add it instead of throwing a warning	
o	--insecure	Retry API download without certificate validation if TLS handshake fails. Note: This makes the…	
a	1	0
@	core
s	check-update	Checks for WordPress updates via Version Check API
s	download	Downloads core WordPress files
s	install	Runs the standard WordPress installation process
s	is-installed	Checks if WordPress is installed
s	multisite-convert	Transforms an existing single-site installation into a multisite installation
s	multisite-install	Installs WordPress multisite from scratch
s	update	Updates WordPress to a newer version
s	update-db	Runs the WordPress database update procedure
s	verify-checksums	Verifies WordPress files against WordPress.org’s checksums
s	version	Displays the WordPress version
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	core	--path
t	filepaths
=	core	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	core	--user
v	id	
v	login	
v	email	
@	core check-update
o	--minor	Compare only the first two parts of the version number	
o	--major	Compare only the first part of the version number	
o	--field	Prints the value of a single field for each update	v=
o	--fields	Limit the output to specific object fields. Defaults to version,update_type,package_url	v=
o	--format	Render output in a particular format	v=
=	core check-update	--format
v	table	
v	csv	
v	count	
v	json	
v	yaml	
@	core download
o	--path	Specify the path in which to install WordPress. Defaults to current directory	v=
o	--locale	Select which language you want to download	v=
o	--version	Select which version you want to download. Accepts a version number, ‘latest’ or ‘nightly’	v=
o	--skip-content	Download WP without the default themes and plugins	
o	--force	Overwrites existing files, if present	
o	--insecure	Retry download without certificate validation if TLS handshake fails. Note: This makes the request…	
a	1	0
=	core download	--path
t	folders
=	core download	--version
v	<number>	
v	latest	
v	nightly	
@	core install
o	--url	The address of the new site	v=
o	--title	The title of the new site	v=
o	--admin_user	The name of the admin user	v=
o	--admin_password	The password for the admin user. Defaults to randomly generated string	v=
o	--admin_email	The email address for the admin user	v=
o	--skip-email	Don’t send an email notification to the new admin user	
@	core is-installed
o	--network	Check if this is a multisite installation	
@	core multisite-convert
o	--title	The title of the new network	v=
o	--base	Base path after the domain name that each site url will start with	v=
o	--subdomains	If passed, the network will use subdomains, instead of subdirectories. Doesn’t work with ‘localhost’	
=	core multisite-convert	--base
v	/	
@	core multisite-install
o	--url	The address of the new site	v=
o	--base	Base path after the domain name that each site url will start with	v=
o	--subdomains	If passed, the network will use subdomains, instead of subdirectories. Doesn’t work with ‘localhost’	
o	--title	The title of the new site	v=
o	--admin_user	The name of the admin user	v=
o	--admin_password	The password for the admin user. Defaults to randomly generated string	v=
o	--admin_email	The email address for the admin user	v=
o	--skip-email	Don’t send an email notification to the new admin user	
o	--skip-config	Don’t add multisite constants to wp-config.php	
=	core multisite-install	--base
v	/	
=	core multisite-install	--admin_user
v	admin	
@	core update
o	--minor	Only perform updates for minor releases (e.g. update from WP 4.3 to 4.3.3 instead of 4.4.2)	
o	--version	Update to a specific version, instead of to the latest version. Alternatively accepts ‘nightly’	v=
o	--force	Update even when installed WP version is greater than the requested version	
o	--locale	Select which language you want to download	v=
o	--insecure	Retry download without certificate validation if TLS handshake fails. Note: This makes the request…	
a	1	0
#	core update	1
t	filepaths
@	core update-db
o	--network	Update databases for all sites on a network	
o	--dry-run	Compare database versions without performing the update	
@	core verify-checksums
o	--version	Verify checksums against a specific version of WordPress	v=
o	--locale	Verify checksums against a specific locale of WordPress	v=
o	--insecure	Verify checksums against a specific locale of WordPress	
@	core version
o	--extra	Show extended version information	
@	cron
s	event	Schedules, runs, and deletes WP-Cron events
s	schedule	Gets WP-Cron schedules
s	test	Tests the WP Cron spawning system and reports back its status
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	cron	--path
t	filepaths
=	cron	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	cron	--user
v	id	
v	login	
v	email	
@	cron event
s	delete	Deletes all scheduled cron events for the given hook
s	list	Lists scheduled cron events
s	run	Runs the next scheduled cron event for the given hook
s	schedule	Schedules a new cron event
s	unschedule	Unschedules all cron events for a given hook
@	cron event delete
a	1	0
@	cron event list
o	--fields	Limit the output to specific object fields	v=
o	--field=value	Filter by one or more fields	
o	--field	Prints the value of a single field for each term	v=
o	--format	Render output in a particular format	v=
=	cron event list	--format
v	table	
v	csv	
v	ids	
v	json	
v	count	
v	yaml	
@	cron event run
o	--due-now	Run all hooks due right now	
o	--all	Run all hooks	
a	1	0
@	cron event schedule
o	--field=value	Arguments to pass to the hook for the event. <field> should be a numeric key, not a string	
a	3	0
@	cron event unschedule
a	1	0
@	cron schedule
s	list	List available cron schedules
@	cron schedule list
o	--fields	Limit the output to specific object fields	v=
o	--field	Prints the value of a single field for each schedule	v=
o	--format	Render output in a particular format	v=
=	cron schedule list	--format
v	table	
v	csv	
v	ids	
v	json	
v	yaml	
@	cron test
@	db
s	check	Checks the current status of the database
s	clean	Removes all tables with `$table_prefix` from the database
s	cli	Opens a MySQL console using credentials from wp-config.php
s	columns	Displays information about a given table
s	create	Creates a new database
s	drop	Deletes the existing database
s	export	Exports the database to a file or to STDOUT
s	import	Imports a database from a file or from STDIN
s	optimize	Optimizes the database
s	prefix	Displays the database table prefix
s	query	Executes a SQL query against the database
s	repair	Repairs the database
s	reset	Removes all tables from the database
s	search	Finds a string in the database
s	size	Displays the database name and size
s	tables	Lists the database tables
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	db	--path
t	filepaths
=	db	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	db	--user
v	id	
v	login	
v	email	
@	db check
o	--dbuser	Username to pass to mysqlcheck. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysqlcheck. Defaults to DB_PASSWORD	v=
o	--field=value	Extra arguments to pass to mysqlcheck. Refer to mysqlcheck docs	
o	--defaults	Loads the environment’s MySQL option files. Default behavior is to skip loading them to avoid…	
@	db clean
o	--dbuser	Username to pass to mysqlcheck. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysqlcheck. Defaults to DB_PASSWORD	v=
o	--yes	Answer yes to the confirmation message	
@	db cli
o	--database	Use a specific database. Defaults to DB_NAME	v=
o	--default-character-set	Use a specific character set. Defaults to DB_CHARSET when defined	v=
o	--dbuser	Username to pass to mysql. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysql. Defaults to DB_PASSWORD	v=
o	--field=value	Extra arguments to pass to mysql. Refer to mysql docs	
o	--defaults	Loads the environment’s MySQL option files. Default behavior is to skip loading them to avoid…	
@	db columns
o	--format	Render output in a particular format	v=
a	1	0
=	db columns	--format
v	table	
v	csv	
v	json	
v	yaml	
@	db create
o	--dbuser	Username to pass to mysql. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysql. Defaults to DB_PASSWORD	v=
@	db drop
o	--dbuser	Username to pass to mysql. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysql. Defaults to DB_PASSWORD	v=
o	--yes	Answer yes to the confirmation message	
@	db export
o	--dbuser	Username to pass to mysqldump. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysqldump. Defaults to DB_PASSWORD	v=
o	--field=value	Extra arguments to pass to mysqldump. Refer to mysqldump docs	
o	--tables	The comma separated list of specific tables to export. Excluding this parameter will export all…	v=
o	--exclude_tables	The comma separated list of specific tables that should be skipped from exporting. Excluding this…	v=
o	--include-tablespaces	Skips adding the default –no-tablespaces option to mysqldump	
o	--porcelain	Output filename for the exported database	
o	--defaults	Loads the environment’s MySQL option files. Default behavior is to skip loading them to avoid…	
a	1	0
@	db import
o	--dbuser	Username to pass to mysql. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysql. Defaults to DB_PASSWORD	v=
o	--field=value	Extra arguments to pass to mysql. Refer to mysql binary docs	
o	--skip-optimization	When using an SQL file, do not include speed optimization such as disabling auto-commit and key…	
o	--defaults	Loads the environment’s MySQL option files. Default behavior is to skip loading them to avoid…	
a	1	0
=	db import	--dbuser
v	DB_USER	
=	db import	--dbpass
v	DB_PASSWORD	
@	db optimize
o	--dbuser	Username to pass to mysqlcheck. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysqlcheck. Defaults to DB_PASSWORD	v=
o	--field=value	Extra arguments to pass to mysqldump. Refer to mysqldump docs	
o	--defaults	Loads the environment’s MySQL option files. Default behavior is to skip loading them to avoid…	
=	db optimize	--dbuser
v	DB_USER	
=	db optimize	--dbpass
v	DB_PASSWORD	
@	db prefix
@	db query
o	--dbuser	Username to pass to mysql. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysql. Defaults to DB_PASSWORD	v=
o	--field=value	Extra arguments to pass to mysql. Refer to mysql docs	
o	--defaults	Loads the environment’s MySQL option files. Default behavior is to skip loading them to avoid…	
a	1	0
=	db query	--dbuser
v	DB_USER	
=	db query	--dbpass
v	DB_PASSWORD	
@	db repair
o	--dbuser	Username to pass to mysqlcheck. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysqlcheck. Defaults to DB_PASSWORD	v=
o	--field=value	Extra arguments to pass to mysqlcheck. Refer to mysqlcheck docs	
o	--defaults	Loads the environment’s MySQL option files. Default behavior is to skip loading them to avoid…	
=	db repair	--dbuser
v	DB_USER	
=	db repair	--dbpass
v	DB_PASSWORD	
@	db reset
o	--dbuser	Username to pass to mysql. Defaults to DB_USER	v=
o	--dbpass	Password to pass to mysql. Defaults to DB_PASSWORD	v=
o	--yes	Answer yes to the confirmation message	
=	db reset	--dbuser
v	DB_USER	
=	db reset	--dbpass
v	DB_PASSWORD	
@	db search
o	--network	Search through all the tables registered to $wpdb in a multisite install	
o	--all-tables-with-prefix	Search through all tables that match the registered table prefix, even if not registered on $wpdb…	
o	--all-tables	Search through ALL tables in the database, regardless of the prefix, and even if not registered on…	
o	--before_context	Number of characters to display before the match	v=
o	--after_context	Number of characters to display after the match	v=
o	--regex	Runs the search as a regular expression (without delimiters). The search becomes case-sensitive…	
o	--regex-flags	Pass PCRE modifiers to the regex search (e.g. ‘i’ for case-insensitivity)	v=
o	--regex-delimiter	The delimiter to use for the regex. It must be escaped if it appears in the search string. The…	v=
o	--table_column_once	Output the ‘table:column’ line once before all matching row lines in the table column rather than…	
o	--one_line	Place the ‘table:column’ output on the same line as the row id and match…	
o	--matches_only	Only output the string matches (including context). No ‘table:column’s or row ids are outputted	
o	--stats	Output stats on the number of matches found, time taken, tables/columns/rows searched, tables…	
o	--table_column_color	Percent color code to use for the ‘table:column’ output. For a list of available percent color…	v=
o	--id_color	Percent color code to use for the row id output. For a list of available percent color codes, see…	v=
o	--match_color	Percent color code to use for the match (unless both before and after context are 0, when no color…	v=
a	2	0
=	db search	--before_context
v	40	
=	db search	--after_context
v	40	
@	db size
o	--size_format	Display the database size only, as a bare number	v=
o	--tables	Display each table name and size instead of the database size	
o	--human-readable	Display database sizes in human readable formats	
o	--format	Render output in a particular format	v=
o	--scope	Can be all, global, ms_global, blog, or old tables. Defaults to all	v=
o	--network	List all the tables in a multisite install	
o	--all-tables-with-prefix	List all tables that match the table prefix even if not registered on $wpdb. Overrides –network	
o	--all-tables	List all tables in the database, regardless of the prefix, and even if not registered on $wpdb…	
=	db size	--size_format
v	b	
v	kb	
v	mb	
v	gb	
v	tb	
v	B	
v	KB	
v	KiB	
v	MB	
v	MiB	
v	GB	
v	GiB	
v	TB	
v	TiB	
=	db size	--format
v	table	
v	csv	
v	json	
v	yaml	
@	db tables
o	--scope	Can be all, global, ms_global, blog, or old tables. Defaults to all	v=
o	--network	List all the tables in a multisite install	
o	--all-tables-with-prefix	List all tables that match the table prefix even if not registered on $wpdb. Overrides –network	
o	--all-tables	List all tables in the database, regardless of the prefix, and even if not registered on $wpdb…	
o	--format	Render output in a particular format	v=
a	1	0
=	db tables	--format
v	list	
v	csv	
@	dist-archive
o	--create-target-dir	Automatically create the target directory as needed	
o	--format	Choose the format for the archive	v=
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
a	2	0
=	dist-archive	--format
v	zip	
v	targz	
=	dist-archive	--path
t	filepaths
=	dist-archive	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	dist-archive	--user
v	id	
v	login	
v	email	
#	dist-archive	1
t	folders
#	dist-archive	2
t	filepaths
@	embed
s	cache	Finds, triggers, and deletes oEmbed caches
s	fetch	Attempts to convert a URL into embed HTML
s	handler	Retrieves embed handlers
s	provider	Retrieves oEmbed providers
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	embed	--path
t	filepaths
=	embed	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	embed	--user
v	id	
v	login	
v	email	
@	embed cache
s	clear	Deletes all oEmbed caches for a given post
s	find	Finds an oEmbed cache post ID for a given URL
s	trigger	Triggers the caching of all oEmbed results for a given post
@	embed cache clear
a	1	0
@	embed cache find
o	--width	Width of the embed in pixels. Part of cache key so must match. Defaults to content_width if set…	v=
o	--height	Height of the embed in pixels. Part of cache key so must match. Defaults to 1.5 * default width…	v=
o	--discover	Whether to search with the discover attribute set or not. Part of cache key so must match. If not…	
a	1	0
@	embed cache trigger
a	1	0
@	embed fetch
o	--width	Width of the embed in pixels	v=
o	--height	Height of the embed in pixels	v=
o	--post-id	Cache oEmbed response for a given post	v=
o	--discover	Enable oEmbed discovery. Defaults to true	
o	--skip-cache	Ignore already cached oEmbed responses. Has no effect if using the ‘raw’ option, which doesn’t use…	
o	--skip-sanitization	Remove the filter that WordPress from 4.4 onwards uses to sanitize oEmbed responses. Has no effect…	
o	--do-shortcode	If the URL is handled by a registered embed handler and returns a shortcode, do shortcode and…	
o	--limit-response-size	Limit the size of the resulting HTML when using discovery. Default 150 KB (the standard WordPress…	v=
o	--raw	Return the raw oEmbed response instead of the resulting HTML. Ignores the cache and does not…	
o	--raw-format	The serialization format for the value	v=
a	1	0
=	embed fetch	--raw-format
v	json	
v	xml	
@	embed handler
s	list	Lists all available embed handlers
@	embed handler list
o	--field	Display the value of a single field	v=
o	--fields	Limit the output to specific fields	v=
o	--format	Render output in a particular format	v=
=	embed handler list	--format
v	table	
v	csv	
v	json	
@	embed provider
s	list	Lists all available oEmbed providers
s	match	Gets the matching provider for a given URL
@	embed provider list
o	--field	Display the value of a single field	v=
o	--fields	Limit the output to specific fields	v=
o	--format	Render output in a particular format	v=
=	embed provider list	--format
v	table	
v	csv	
v	json	
@	embed provider match
o	--discover	Whether to use oEmbed discovery or not. Defaults to true	
o	--limit-response-size	Limit the size of the resulting HTML when using discovery. Default 150 KB (the standard WordPress…	v=
o	--link-type	Whether to accept only a certain link type when using discovery. Defaults to any (json or xml)…	v=
a	1	0
=	embed provider match	--link-type
v	json	
v	xml	
@	eval
o	--skip-wordpress	Execute code without loading WordPress	
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
a	1	0
=	eval	--path
t	filepaths
=	eval	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	eval	--user
v	id	
v	login	
v	email	
@	eval-file
o	--skip-wordpress	Load and execute file without loading WordPress	
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
a	2	0
=	eval-file	--path
t	filepaths
=	eval-file	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	eval-file	--user
v	id	
v	login	
v	email	
@	export
o	--dir	Full path to directory where WXR export files should be stored. Defaults to current working…	v=
o	--stdout	Output the whole XML using standard output (incompatible with –dir=)	
o	--skip_comments	Don’t include comments in the WXR export file	
o	--max_file_size	A single export file should have this many megabytes. -1 for unlimited	v=
o	--start_date	Export only posts published after this date, in format YYYY-MM-DD	v=
o	--end_date	Export only posts published before this date, in format YYYY-MM-DD	v=
o	--post_type	Export only posts with this post_type. Separate multiple post types with a comma	v=
o	--post_type__not_in	Export all post types except those identified. Separate multiple post types with a comma. Defaults…	v=
o	--post_in	Export all posts specified as a comma- or space-separated list of IDs. Post’s attachments won’t be…	v=
o	--with_attachments	Force including attachments in case –post__in has been specified	
o	--start_id	Export only posts with IDs greater than or equal to this post ID	v=
o	--max_num_posts	Export no more than <num> posts (excluding attachments)	v=
o	--author	Export only posts by this author. Can be either user login or user ID	v=
o	--category	Export only posts in this category	v=
o	--post_status	Export only posts with this status	v=
o	--filename_format	Use a custom format for export filenames. Defaults to ‘{site}.wordpress.{date}.{n}.xml’	v=
=	export	--dir
t	folders
=	export	--max_file_size
v	15	
=	export	--post_type
v	any	
@	find
o	--skip-ignored-paths	Skip the paths that are ignored by default	
o	--include_ignored_paths	Include additional ignored paths as CSV (e.g. ‘/sys-backup/,/temp/’)	v=
o	--max_depth	Only recurse to a specified depth, inclusive	v=
o	--fields	Limit the output to specific row fields	v=
o	--field	Output a specific field for each row	v=
o	--format	Render output in a particular format	v=
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
a	1	0
=	find	--format
v	table	
v	json	
v	csv	
v	yaml	
v	count	
=	find	--path
t	filepaths
=	find	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	find	--user
v	id	
v	login	
v	email	
#	find	1
t	folders
@	help
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
a	1	0
=	help	--path
t	filepaths
=	help	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	help	--user
v	id	
v	login	
v	email	
@	i18n
s	make-json	Extract JavaScript strings from PO files and add them to individual JSON files
s	make-mo	Create MO files from PO files
s	make-pot	Create a POT file for a WordPress project
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	i18n	--path
t	filepaths
=	i18n	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	i18n	--user
v	id	
v	login	
v	email	
@	i18n make-json
o	--purge	Whether to purge the strings that were extracted from the original source file. Defaults to true…	
o	--pretty-print	Pretty-print resulting JSON files	
a	2	0
#	i18n make-json	1
t	filepaths
#	i18n make-json	2
t	folders
@	i18n make-mo
a	2	0
#	i18n make-mo	1
t	filepaths
#	i18n make-mo	2
t	folders
@	i18n make-pot
o	--slug	Plugin or theme slug. Defaults to the source directory’s basename	v=
o	--domain	Text domain to look for in the source code, unless the --ignore-domain option is used. By default…	v=
o	--ignore-domain	Ignore the text domain completely and extract strings with any text domain	
o	--merge	Comma-separated list of POT files whose contents should be merged with the extracted strings. If…	v=
o	--subtract	Comma-separated list of POT files whose contents should act as some sort of blacklist for string…	v=
o	--include	Comma-separated list of files and paths that should be used for string extraction. If provided…	v=
o	--exclude	Comma-separated list of files and paths that should be skipped for string extraction. For example…	v=
o	--headers	Array in JSON format of custom headers which will be added to the POT file. Defaults to empty array	v=
o	--skip-js	Skips JavaScript string extraction. Useful when this is done in another build step, e.g. through…	
o	--skip-php	Skips PHP string extraction	
o	--skip-block-json	Skips string extraction from block.json files	
o	--skip-audit	Skips string audit where it tries to find possible mistakes in translatable strings. Useful when…	
o	--file-comment	String that should be added as a comment to the top of the resulting POT file. By default, a…	v=
o	--package-name	Name to use for package name in the resulting POT file’s Project-Id-Version header. Overrides…	v=
a	2	0
@	import
o	--authors	How the author mapping should be handled. Options are ‘create’, ‘mapping.csv’, or ‘skip’. The…	v=
o	--skip	Skip importing specific data. Supported options are: ‘attachment’ and ‘image_resize’ (skip…	v=
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
a	1	0
=	import	--path
t	filepaths
=	import	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	import	--user
v	id	
v	login	
v	email	
#	import	1
t	filepaths
@	language
s	core	Installs, activates, and manages core language packs
s	plugin	Installs, activates, and manages plugin language packs
s	theme	Installs, activates, and manages theme language packs
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	language	--path
t	filepaths
=	language	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	language	--user
v	id	
v	login	
v	email	
@	language core
s	activate	Activates a given language
s	install	Installs a given language
s	is-installed	Checks if a given language is installed
s	list	Lists all available languages
s	uninstall	Uninstalls a given language
s	update	Updates installed languages for core
@	language core activate
a	1	0
@	language core install
o	--activate	If set, the language will be activated immediately after install	
a	1	0
@	language core is-installed
a	1	0
@	language core list
o	--field	Display the value of a single field	v=
o	--field=value	Filter results by key=value pairs	
o	--fields	Limit the output to specific fields	v=
o	--format	Render output in a particular format	v=
=	language core list	--format
v	table	
v	csv	
v	json	
@	language core uninstall
a	1	0
@	language core update
o	--dry-run	Preview which translations would be updated	
@	language plugin
s	install	Installs a given language for a plugin
s	is-installed	Checks if a given language is installed
s	list	Lists all available languages for one or more plugins
s	uninstall	Uninstalls a given language for a plugin
s	update	Updates installed languages for one or more plugins
@	language plugin install
o	--all	If set, languages for all plugins will be installed	
o	--format	Render output in a particular format. Used when installing languages for all plugins	v=
a	2	0
=	language plugin install	--format
v	table	
v	csv	
v	json	
v	summary	
@	language plugin is-installed
a	2	0
@	language plugin list
o	--all	If set, languages for all plugins will be listed	
o	--field	Display the value of a single field	v=
o	--field=value	Filter results by key=value pairs	
o	--fields	Limit the output to specific fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	language plugin list	--format
v	table	
v	csv	
v	json	
@	language plugin uninstall
a	2	0
@	language plugin update
o	--all	If set, languages for all plugins will be updated	
o	--dry-run	Preview which translations would be updated	
a	1	0
@	language theme
s	install	Installs a given language for a theme
s	is-installed	Checks if a given language is installed
s	list	Lists all available languages for one or more themes
s	uninstall	Uninstalls a given language for a theme
s	update	Updates installed languages for one or more themes
@	language theme install
o	--all	If set, languages for all themes will be installed	
o	--format	Render output in a particular format. Used when installing languages for all themes	v=
a	2	0
=	language theme install	--format
v	table	
v	csv	
v	json	
v	summary	
@	language theme is-installed
a	2	0
@	language theme list
o	--all	If set, available languages for all themes will be listed	
o	--field	Display the value of a single field	v=
o	--field=value	Filter results by key=value pairs	
o	--fields	Limit the output to specific fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	language theme list	--format
v	table	
v	csv	
v	json	
@	language theme uninstall
a	2	0
@	language theme update
o	--all	If set, languages for all themes will be updated	
o	--dry-run	Preview which translations would be updated	
a	1	0
@	maintenance-mode
s	activate	Activates maintenance mode
s	deactivate	Deactivates maintenance mode
s	is-active	Detects maintenance mode status
s	status	Displays maintenance mode status
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	maintenance-mode	--path
t	filepaths
=	maintenance-mode	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	maintenance-mode	--user
v	id	
v	login	
v	email	
@	maintenance-mode activate
o	--force	Force maintenance mode activation operation	
@	maintenance-mode deactivate
@	maintenance-mode is-active
@	maintenance-mode status
@	media
s	fix-orientation	Fix image orientation for one or more attachments
s	image-size	Lists image sizes registered with WordPress
s	import	Creates attachments from local files or URLs
s	regenerate	Regenerates thumbnails for one or more attachments
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	media	--path
t	filepaths
=	media	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	media	--user
v	id	
v	login	
v	email	
@	media fix-orientation
o	--dry-run	Check images needing orientation without performing the operation	
a	1	0
@	media image-size
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
=	media image-size	--format
v	table	
v	json	
v	csv	
v	yaml	
v	count	
@	media import
o	--post_id	ID of the post to attach the imported files to	v=
o	--title	Attachment title (post title field)	v=
o	--caption	Caption for attachent (post excerpt field)	v=
o	--alt	Alt text for image (saved as post meta)	v=
o	--desc	'Description' field (post content) of attachment post	v=
o	--skip-copy	If set, media files (local only) are imported to the library but not moved on disk. File names…	
o	--preserve-filetime	Use the file modified time as the post published & modified dates. Remote files will always use…	
o	--featured_image	If set, set the imported image as the Featured Image of the post its attached to	
o	--porcelain	Output just the new attachment ID	
a	1	0
#	media import	1
t	filepaths
@	media regenerate
o	--image_size	Name of the image size to regenerate. Only thumbnails of this image size will be regenerated…	v=
o	--skip-delete	Skip deletion of the original thumbnails. If your thumbnails are linked from sources outside your…	
o	--only-missing	Only generate thumbnails for images missing image sizes	
o	--yes	Answer yes to the confirmation message. Confirmation only shows when no IDs passed as arguments	
a	1	0
@	menu
s	create	Creates a new menu
s	delete	Deletes one or more menus
s	item	List, add, and delete items associated with a menu
s	list	Gets a list of menus
s	location	Assigns, removes, and lists a menu’s locations
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	menu	--path
t	filepaths
=	menu	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	menu	--user
v	id	
v	login	
v	email	
@	menu create
o	--porcelain	Output just the new menu ID	
a	1	0
@	menu delete
a	1	0
@	menu item
s	add-custom	Adds a custom menu item
s	add-post	Adds a post as a menu item
s	add-term	Adds a taxonomy term as a menu item
s	delete	Deletes one or more items from a menu
s	list	Gets a list of items associated with a menu
s	update	Updates a menu item
@	menu item add-custom
o	--description	Set a custom description for the menu item	v=
o	--attr-title	Set a custom title attribute for the menu item	v=
o	--target	Set a custom link target for the menu item	v=
o	--classes	Set a custom link classes for the menu item	v=
o	--position	Specify the position of this menu item	v=
o	--parent-id	Make this menu item a child of another menu item	v=
o	--porcelain	Output just the new menu item ID	
a	3	0
@	menu item add-post
o	--title	Set a custom title for the menu item	v=
o	--link	Set a custom url for the menu item	v=
o	--description	Set a custom description for the menu item	v=
o	--attr-title	Set a custom title attribute for the menu item	v=
o	--target	Set a custom link target for the menu item	v=
o	--classes	Set a custom link classes for the menu item	v=
o	--position	Specify the position of this menu item	v=
o	--parent-id	Make this menu item a child of another menu item	v=
o	--porcelain	Output just the new menu item id	
a	2	0
@	menu item add-term
o	--title	Set a custom title for the menu item	v=
o	--link	Set a custom url for the menu item	v=
o	--description	Set a custom description for the menu item	v=
o	--attr-title	Set a custom title attribute for the menu item	v=
o	--target	Set a custom link target for the menu item	v=
o	--classes	Set a custom link classes for the menu item	v=
o	--position	Specify the position of this menu item	v=
o	--parent-id	Make this menu item a child of another menu item	v=
o	--porcelain	Output just the new menu item id	
a	3	0
@	menu item delete
a	1	0
@	menu item list
o	--fields	Limit the output to specific object fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	menu item list	--format
v	table	
v	csv	
v	json	
v	count	
v	ids	
v	yaml	
@	menu item update
o	--title	Set a custom title for the menu item	v=
o	--link	Set a custom url for the menu item	v=
o	--description	Set a custom description for the menu item	v=
o	--attr-title	Set a custom title attribute for the menu item	v=
o	--target	Set a custom link target for the menu item	v=
o	--classes	Set a custom link classes for the menu item	v=
o	--position	Specify the position of this menu item	v=
o	--parent-id	Make this menu item a child of another menu item	v=
a	1	0
@	menu list
o	--fields	Limit the output to specific object fields	v=
o	--format	Render output in a particular format	v=
=	menu list	--format
v	table	
v	csv	
v	json	
v	count	
v	ids	
v	yaml	
@	menu location
s	assign	Assigns a location to a menu
s	list	Lists locations for the current theme
s	remove	Removes a location from a menu
@	menu location assign
a	2	0
@	menu location list
o	--format	Render output in a particular format	v=
=	menu location list	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
v	ids	
@	menu location remove
a	2	0
@	network
s	meta	Gets, adds, updates, deletes, and lists network custom fields
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	network	--path
t	filepaths
=	network	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	network	--user
v	id	
v	login	
v	email	
@	network meta
s	add	Add a meta field
s	delete	Delete a meta field
s	get	Get meta field value
s	list	List all metadata associated with an object
s	patch	Update a nested value for a meta field
s	pluck	Get a nested value from a meta field
s	update	Update a meta field
@	network meta add
o	--format	The serialization format for the value	v=
a	3	0
=	network meta add	--format
v	plaintext	
v	json	
@	network meta delete
o	--all	Delete all meta for the object	
a	3	0
@	network meta get
o	--format	Get value in a particular format	v=
a	2	0
=	network meta get	--format
v	var_export	
v	json	
v	yaml	
@	network meta list
o	--keys	Limit output to metadata of specific keys	v=
o	--fields	Limit the output to specific row fields. Defaults to id,meta_key,meta_value	v=
o	--format	Render output in a particular format	v=
o	--orderby	Set orderby which field	v=
o	--order	Set ascending or descending order	v=
o	--unserialize	Unserialize meta_value output	
a	1	0
=	network meta list	--format
v	table	
v	csv	
v	json	
v	yaml	
v	count	
=	network meta list	--orderby
v	id	
v	meta_key	
v	meta_value	
=	network meta list	--order
v	asc	
v	desc	
@	network meta patch
o	--format	The serialization format for the value	v=
a	5	0
=	network meta patch	--format
v	plaintext	
v	json	
#	network meta patch	1
v	insert	
v	update	
v	delete	
@	network meta pluck
o	--format	The output format of the value	v=
a	3	0
=	network meta pluck	--format
v	plaintext	
v	json	
v	yaml	
@	network meta update
o	--format	The serialization format for the value	v=
a	3	0
=	network meta update	--format
v	plaintext	
v	json	
@	option
s	add	Adds a new option value
s	delete	Deletes an option
s	get	Gets the value for an option
s	list	Lists options and their values
s	patch	Updates a nested value in an option
s	pluck	Gets a nested value from an option
s	update	Updates an option value
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	option	--path
t	filepaths
=	option	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	option	--user
v	id	
v	login	
v	email	
@	option add
o	--format	The serialization format for the value	v=
o	--autoload	Should this option be automatically loaded	v=
a	2	0
=	option add	--format
v	plaintext	
v	json	
=	option add	--autoload
v	'yes'	
v	'no'	
@	option delete
a	1	0
@	option get
o	--format	Get value in a particular format	v=
a	1	0
=	option get	--format
v	var_export	
v	json	
v	yaml	
@	option list
o	--search	Use wildcards ( * and ? ) to match option name	v=
o	--exclude	Pattern to exclude. Use wildcards ( * and ? ) to match option name	v=
o	--autoload	Match only autoload options when value is on, and only not-autoload option when off	v=
o	--transients	List only transients. Use --no-transients to ignore all transients	
o	--no-transients	List only transients. Use --no-transients to ignore all transients	
o	--unserialize	Unserialize option values in output	
o	--field	Prints the value of a single field	v=
o	--fields	Limit the output to specific object fields	v=
o	--format	The serialization format for the value. total_bytes displays the total size of matching options in…	v=
o	--orderby	Set orderby which field	v=
o	--order	Set ascending or descending order	v=
=	option list	--format
v	table	
v	json	
v	csv	
v	count	
v	yaml	
v	total_bytes	
=	option list	--orderby
v	option_id	
v	option_name	
v	option_value	
=	option list	--order
v	asc	
v	desc	
@	option patch
o	--format	The serialization format for the value	v=
a	4	0
=	option patch	--format
v	plaintext	
v	json	
#	option patch	1
v	insert	
v	update	
v	delete	
@	option pluck
o	--format	The output format for the value	v=
a	2	0
=	option pluck	--format
v	plaintext	
v	json	
v	yaml	
@	option update
o	--autoload	Requires WP 4.2. Should this option be automatically loaded	v=
o	--format	The serialization format for the value	v=
a	2	0
=	option update	--autoload
v	'yes'	
v	'no	
=	option update	--format
v	plaintext	
v	json	
@	package
s	browse	Browses WP-CLI packages available for installation
s	install	Installs a WP-CLI package
s	list	Lists installed WP-CLI packages
s	path	Gets the path to an installed WP-CLI package, or the package directory
s	uninstall	Uninstalls a WP-CLI package
s	update	Updates all installed WP-CLI packages to their latest version
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	package	--path
t	filepaths
=	package	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	package	--user
v	id	
v	login	
v	email	
@	package browse
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
=	package browse	--format
v	table	
v	csv	
v	ids	
v	json	
v	yaml	
@	package install
o	--insecure	Retry downloads without certificate validation if TLS handshake fails. Note: This makes the…	
a	1	0
@	package list
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
=	package list	--format
v	table	
v	csv	
v	ids	
v	json	
v	yaml	
@	package path
a	1	0
#	package path	1
t	folders
@	package uninstall
a	1	0
@	package update
@	plugin
s	activate	Activates one or more plugins
s	auto-updates	Manages plugin auto-updates
s	deactivate	Deactivates one or more plugins
s	delete	Deletes plugin files without deactivating or uninstalling
s	get	Gets details about an installed plugin
s	install	Installs one or more plugins
s	is-active	Checks if a given plugin is active
s	is-installed	Checks if a given plugin is installed
s	list	Gets a list of plugins
s	path	Gets the path to a plugin or to the plugin directory
s	search	Searches the WordPress.org plugin directory
s	status	Reveals the status of one or all plugins
s	toggle	Toggles a plugin’s activation state
s	uninstall	Uninstalls one or more plugins
s	update	Updates one or more plugins
s	verify-checksums	Verifies plugin files against WordPress.org’s checksums
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	plugin	--path
t	filepaths
=	plugin	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	plugin	--user
v	id	
v	login	
v	email	
@	plugin activate
o	--all	If set, all plugins will be activated	
o	--network	If set, the plugin will be activated for the entire multisite network	
a	1	0
@	plugin auto-updates
s	disable	Disables the auto-updates for a plugin
s	enable	Enables the auto-updates for a plugin
s	status	Shows the status of auto-updates for a plugin
@	plugin auto-updates disable
o	--all	If set, auto-updates will be disabled for all plugins	
o	--enabled-only	If set, filters list of plugins to only include the ones that have auto-updates enabled	
a	1	0
@	plugin auto-updates enable
o	--all	If set, auto-updates will be enabled for all plugins	
o	--disabled-only	If set, filters list of plugins to only include the ones that have auto-updates disabled	
a	1	0
@	plugin auto-updates status
o	--all	If set, the status of auto-updates for all plugins will be shown	
o	--enabled-only	If set, filters list of plugins to only include the ones that have auto-updates enabled	
o	--disabled-only	If set, filters list of plugins to only include the ones that have auto-updates disabled	
o	--field	Only show the provided field	v=
a	1	0
@	plugin deactivate
o	--uninstall	Uninstall the plugin after deactivation	
o	--all	If set, all plugins will be deactivated	
o	--network	If set, the plugin will be deactivated for the entire multisite network	
a	1	0
@	plugin delete
o	--all	If set, all plugins will be deleted	
a	1	0
@	plugin get
o	--field	Instead of returning the whole plugin, returns the value of a single field	v=
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	plugin get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	plugin install
o	--version	If set, get that particular version from wordpress.org, instead of the stable version	v=
o	--force	If set, the command will overwrite any installed version of the plugin, without prompting for…	
o	--activate	If set, the plugin will be activated immediately after install	
o	--activate-network	If set, the plugin will be network activated immediately after installl	
o	--insecure	Retry downloads without certificate validation if TLS handshake fails. Note: This makes the…	
a	1	0
@	plugin is-active
o	--network	If set, check if plugin is network-activated	
a	1	0
@	plugin is-installed
a	1	0
@	plugin list
o	--field=value	Filter results based on the value of a field	
o	--field	Prints the value of a single field for each plugin	v=
o	--fields	Limit the output to specific object fields	v=
o	--format	Render output in a particular format	v=
o	--status	Filter the output by plugin status	v=
=	plugin list	--format
v	table	
v	csv	
v	count	
v	json	
v	yaml	
=	plugin list	--status
v	active	
v	active-network	
v	dropin	
v	inactive	
v	must-use	
@	plugin path
o	--dir	If set, get the path to the closest parent directory, instead of the plugin file	
a	1	0
@	plugin search
o	--page	Optional page to display	v=
o	--per-page	Optional number of results to display	v=
o	--field	Prints the value of a single field for each plugin	v=
o	--fields	Ask for specific fields from the API. Defaults to name,slug,author_profile,rating. Acceptable…	v=
o	--format	Render output in a particular format	v=
a	1	0
=	plugin search	--page
v	1	
=	plugin search	--per-page
v	10	
=	plugin search	--fields
v	name	
v	slug	
v	version	
v	author	
v	author_profile	
v	contributors	
v	requires	
v	tested	
v	compatibility	
v	rating	
v	ratings	
v	num_ratings	
v	homepage	
v	description	
v	short_description	
v	sections	
v	downloaded	
v	last_updated	
v	added	
v	tags	
v	versions	
v	donate_link	
v	banners	
v	icons	
v	active_installs	
v	contributors	
v	url	
=	plugin search	--format
v	plaintext	
v	table	
v	csv	
v	count	
v	json	
v	yaml	
@	plugin status
a	1	0
@	plugin toggle
o	--network	If set, the plugin will be toggled for the entire multisite network	
a	1	0
@	plugin uninstall
o	--deactivate	Deactivate the plugin before uninstalling. Default behavior is to warn and skip if the plugin is…	
o	--skip-delete	If set, the plugin files will not be deleted. Only the uninstall procedure will be run	
o	--all	If set, all plugins will be uninstalled	
a	1	0
@	plugin update
o	--all	If set, all plugins that have updates will be updated	
o	--exclude	Comma separated list of plugin names that should be excluded from updating	v=
o	--minor	Only perform updates for minor releases (e.g. from 1.3 to 1.4 instead of 2.0)	
o	--patch	Only perform updates for patch releases (e.g. from 1.3 to 1.3.3 instead of 1.4)	
o	--format	Render output in a particular format	v=
o	--version	If set, the plugin will be updated to the specified version	=
o	--dry-run	Preview which plugins would be updated	
o	--insecure	Retry downloads without certificate validation if TLS handshake fails. Note: This makes the…	
a	1	0
=	plugin update	--format
v	table	
v	csv	
v	json	
v	summary	
@	plugin verify-checksums
o	--all	If set, all plugins will be verified	
o	--strict	If set, even “soft changes” like readme.txt changes will trigger checksum errors	
o	--format	Render output in a particular format	v=
o	--insecure	Retry downloads without certificate validation if TLS handshake fails. Note: This makes the…	
a	1	0
=	plugin verify-checksums	--format
v	table	
v	json	
v	csv	
v	yaml	
v	count	
@	post
s	create	Creates a new post
s	delete	Deletes an existing post
s	edit	Launches system editor to edit post content
s	exists	Verifies whether a post exists
s	generate	Generates some posts
s	get	Gets details about a post
s	list	Gets a list of posts
s	meta	Adds, updates, deletes, and lists post custom fields
s	term	Adds, updates, removes, and lists post terms
s	update	Updates one or more existing posts
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	post	--path
t	filepaths
=	post	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	post	--user
v	id	
v	login	
v	email	
@	post create
o	--post_author	The ID of the user who added the post. Default is the current user ID	v=
o	--post_date	The date of the post. Default is the current time	v=
o	--post_date_gmt	The date of the post in the GMT timezone. Default is the value of $post_date	v=
o	--post_content	The post content. Default empty	v=
o	--post_content_filtered	The filtered post content. Default empty	v=
o	--post_title	The post title. Default empty	v=
o	--post_excerpt	The post excerpt. Default empty	v=
o	--post_status	The post status. Default ‘draft’	v=
o	--post_type	The post type. Default ‘post’	v=
o	--comment_status	Whether the post can accept comments. Accepts ‘open’ or ‘closed’. Default is the value of…	v=
o	--ping_status	Whether the post can accept pings. Accepts ‘open’ or ‘closed’. Default is the value of…	v=
o	--post_password	The password to access the post. Default empty	v=
o	--post_name	The post name. Default is the sanitized post title when creating a new post	v=
o	--from-post	Post id of a post to be duplicated	v=
o	--to_ping	Space or carriage return-separated list of URLs to ping. Default empty	v=
o	--pinged	Space or carriage return-separated list of URLs that have been pinged. Default empty	v=
o	--post_modified	The date when the post was last modified. Default is the current time	v=
o	--post_modified_gmt	The date when the post was last modified in the GMT timezone. Default is the current time	v=
o	--post_parent	Set this for the post it belongs to, if any. Default 0	v=
o	--menu_order	The order the post should be displayed in. Default 0	v=
o	--post_mime_type	The mime type of the post. Default empty	v=
o	--guid	Global Unique ID for referencing the post. Default empty	v=
o	--post_category	Array of category names, slugs, or IDs. Defaults to value of the ‘default_category’ option	v=
o	--tags_input	Array of tag names, slugs, or IDs. Default empty	v=
o	--tax_input	Array of taxonomy terms keyed by their taxonomy name. Default empty	v=
o	--meta_input	Array in JSON format of post meta values keyed by their post meta key. Default empty	v=
o	--field=value	Associative args for the new post. See wp_insert_post()	
o	--edit	Immediately open system’s editor to write or edit post content. If content is read from a file…	
o	--porcelain	Output just the new post id	
a	1	0
=	post create	--comment_status
v	'open'	
v	'closed	
=	post create	--ping_status
v	'open'	
v	'closed	
=	post create	--post_parent
v	0	
=	post create	--menu_order
v	0	
@	post delete
o	--force	Skip the trash bin	
o	--defer-term-counting	Recalculate term count in batch, for a performance boost	
a	1	0
@	post edit
a	1	0
@	post exists
a	1	0
@	post generate
o	--count	How many posts to generate?	v=
o	--post_type	The type of the generated posts	v=
o	--post_status	The status of the generated posts	v=
o	--post_title	The post title	v=
o	--post_author	The author of the generated posts	v=
o	--post_date	The date of the generated posts. Default: current date	v=
o	--post_date_gmt	The GMT date of the generated posts. Default: value of post_date (or current date if it’s not set)	v=
o	--post_content	If set, the command reads the post_content from STDIN	
o	--max_depth	For hierarchical post types, generate child posts down to a certain depth	v=
o	--format	Render output in a particular format	v=
=	post generate	--count
v	100	
=	post generate	--post_type
v	post	
=	post generate	--post_status
v	publish	
=	post generate	--max_depth
v	1	
=	post generate	--format
v	progress	
v	ids	
@	post get
o	--field	Instead of returning the whole post, returns the value of a single field	v=
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	post get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	post list
o	--field=value	One or more args to pass to WP_Query	
o	--field	Prints the value of a single field for each post	v=
o	--fields	Limit the output to specific object fields	v=
o	--format	Render output in a particular format	v=
=	post list	--field
v	ID	
v	post_title	
v	post_name	
v	post_date	
v	post_status	
v	post_author	
v	post_date_gmt	
v	post_content	
v	post_excerpt	
v	comment_status	
v	ping_status	
v	post_password	
v	to_ping	
v	pinged	
v	post_modified	
v	post_modified_gmt	
v	post_content_filtered	
v	post_parent	
v	guid	
v	menu_order	
v	post_type	
v	post_mime_type	
v	comment_count	
v	filter	
v	url	
=	post list	--fields
v	ID	
v	post_title	
v	post_name	
v	post_date	
v	post_status	
v	post_author	
v	post_date_gmt	
v	post_content	
v	post_excerpt	
v	comment_status	
v	ping_status	
v	post_password	
v	to_ping	
v	pinged	
v	post_modified	
v	post_modified_gmt	
v	post_content_filtered	
v	post_parent	
v	guid	
v	menu_order	
v	post_type	
v	post_mime_type	
v	comment_count	
v	filter	
v	url	
=	post list	--format
v	table	
v	csv	
v	ids	
v	json	
v	count	
v	yaml	
@	post meta
s	add	Add a meta field
s	delete	Delete a meta field
s	get	Get meta field value
s	list	List all metadata associated with an object
s	patch	Update a nested value for a meta field
s	pluck	Get a nested value from a meta field
s	update	Update a meta field
@	post meta add
o	--format	The serialization format for the value	v=
a	3	0
=	post meta add	--format
v	plaintext	
v	json	
@	post meta delete
o	--all	Delete all meta for the object	
a	3	0
@	post meta get
o	--format	Get value in a particular format	v=
a	2	0
=	post meta get	--format
v	var_export	
v	json	
v	yaml	
@	post meta list
o	--keys	Limit output to metadata of specific keys	v=
o	--fields	Limit the output to specific row fields. Defaults to id,meta_key,meta_value	v=
o	--format	Render output in a particular format	v=
o	--orderby	Set orderby which field	v=
o	--order	Set ascending or descending order	v=
o	--unserialize	Unserialize meta_value output	
a	1	0
=	post meta list	--format
v	table	
v	csv	
v	json	
v	yaml	
v	count	
=	post meta list	--orderby
v	id	
v	meta_key	
v	meta_value	
=	post meta list	--order
v	asc	
v	desc	
@	post meta patch
o	--format	The serialization format for the value	v=
a	5	0
=	post meta patch	--format
v	plaintext	
v	json	
#	post meta patch	1
v	insert	
v	update	
v	delete	
@	post meta pluck
o	--format	The output format of the value	v=
a	3	0
=	post meta pluck	--format
v	plaintext	
v	json	
v	yaml	
@	post meta update
o	--format	The serialization format for the value	v=
a	3	0
=	post meta update	--format
v	plaintext	
v	json	
@	post term
s	add	Add a term to an object
s	list	List all terms associated with an object
s	remove	Remove a term from an object
s	set	Set object terms
@	post term add
o	--by	Explicitly handle the term value as a slug or id	v=
a	3	0
=	post term add	--by
v	slug	
v	id	
@	post term list
o	--field	Prints the value of a single field for each term	v=
o	--fields	Limit the output to specific row fields	v=
o	--format	Render output in a particular format	v=
a	2	0
=	post term list	--field
v	term_id	
v	name	
v	slug	
v	taxonomy	
v	term_taxonomy_id	
v	description	
v	term_group	
v	parent	
v	count	
=	post term list	--fields
v	term_id	
v	name	
v	slug	
v	taxonomy	
v	term_taxonomy_id	
v	description	
v	term_group	
v	parent	
v	count	
=	post term list	--format
v	table	
v	csv	
v	json	
v	yaml	
v	count	
v	ids	
@	post term remove
o	--by	Explicitly handle the term value as a slug or id	v=
o	--all	Remove all terms from the object	
a	3	0
=	post term remove	--by
v	slug	
v	id	
@	post term set
o	--by	Explicitly handle the term value as a slug or id	v=
a	3	0
=	post term set	--by
v	slug	
v	id	
@	post update
o	--post_author	The ID of the user who added the post. Default is the current user ID	v=
o	--post_date	The date of the post. Default is the current time	v=
o	--post_date_gmt	The date of the post in the GMT timezone. Default is the value of $post_date	v=
o	--post_content	The post content. Default empty	v=
o	--post_content_filtered	The filtered post content. Default empty	v=
o	--post_title	The post title. Default empty	v=
o	--post_excerpt	The post excerpt. Default empty	v=
o	--post_status	The post status. Default ‘draft’	v=
o	--post_type	The post type. Default ‘post’	v=
o	--comment_status	Whether the post can accept comments. Accepts ‘open’ or ‘closed’. Default is the value of…	v=
o	--ping_status	Whether the post can accept pings. Accepts ‘open’ or ‘closed’. Default is the value of…	v=
o	--post_password	The password to access the post. Default empty	v=
o	--post_name	The post name. Default is the sanitized post title when creating a new post	v=
o	--to_ping	Space or carriage return-separated list of URLs to ping. Default empty	v=
o	--pinged	Space or carriage return-separated list of URLs that have been pinged. Default empty	v=
o	--post_modified	The date when the post was last modified. Default is the current time	v=
o	--post_modified_gmt	The date when the post was last modified in the GMT timezone. Default is the current time	v=
o	--post_parent	Set this for the post it belongs to, if any. Default 0	v=
o	--menu_order	The order the post should be displayed in. Default 0	v=
o	--post_mime_type	The mime type of the post. Default empty	v=
o	--guid	Global Unique ID for referencing the post. Default empty	v=
o	--post_category	Array of category names, slugs, or IDs. Defaults to value of the ‘default_category’ option	v=
o	--tags_input	Array of tag names, slugs, or IDs. Default empty	v=
o	--tax_input	Array of taxonomy terms keyed by their taxonomy name. Default empty	v=
o	--meta_input	Array in JSON format of post meta values keyed by their post meta key. Default empty	v=
o	--field	One or more fields to update. See wp_insert_post()	=
o	--defer-term-counting	Recalculate term count in batch, for a performance boost	
a	2	0
=	post update	--comment_status
v	'open'	
v	'closed	
=	post update	--ping_status
v	'open'	
v	'closed	
=	post update	--post_parent
v	0	
=	post update	--menu_order
v	0	
@	post-type
s	get	Gets details about a registered post type
s	list	Lists registered post types
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	post-type	--path
t	filepaths
=	post-type	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	post-type	--user
v	id	
v	login	
v	email	
@	post-type get
o	--field	Instead of returning the whole taxonomy, returns the value of a single field	v=
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	post-type get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	post-type list
o	--field=value	Filter by one or more fields (see get_post_types() first parameter for a list of available fields)	
o	--field	Prints the value of a single field for each post type	v=
o	--fields	Limit the output to specific post type fields	v=
o	--format	Render output in a particular format	v=
=	post-type list	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
@	profile
s	eval	Profile arbitrary code execution
s	eval-file	Profile execution of an arbitrary file
s	hook	Profile key metrics for WordPress hooks (actions and filters)
s	stage	Profile each stage of the WordPress load process (bootstrap, main_query, template)
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	profile	--path
t	filepaths
=	profile	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	profile	--user
v	id	
v	login	
v	email	
@	profile eval
o	--hook	Focus on key metrics for all hooks, or callbacks on a specific hook	v=
o	--fields	Display one or more fields	v=
o	--format	Render output in a particular format	v=
o	--order	Ascending or descending order	v=
o	--orderby	Order by fields	v=
a	1	0
=	profile eval	--format
v	table	
v	json	
v	yaml	
v	csv	
=	profile eval	--order
v	ASC	
v	DESC	
@	profile eval-file
o	--hook	Focus on key metrics for all hooks, or callbacks on a specific hook	v=
o	--fields	Display one or more fields	v=
o	--format	Render output in a particular format	v=
o	--order	Ascending or descending order	v=
o	--orderby	Order by fields	v=
a	1	0
=	profile eval-file	--format
v	table	
v	json	
v	yaml	
v	csv	
=	profile eval-file	--order
v	ASC	
v	DESC	
#	profile eval-file	1
t	filepaths
@	profile hook
o	--all	Profile callbacks for all WordPress hooks	
o	--spotlight	Filter out logs with zero-ish values from the set	
o	--url	Execute a request against a specified URL. Defaults to the home URL	v=
o	--fields	Display one or more fields	v=
o	--format	Render output in a particular format	v=
o	--order	Ascending or descending order	v=
o	--orderby	Order by fields	v=
a	1	0
=	profile hook	--format
v	table	
v	json	
v	yaml	
v	csv	
=	profile hook	--order
v	ASC	
v	DESC	
@	profile stage
o	--all	Expand upon all stages	
o	--spotlight	Filter out logs with zero-ish values from the set	
o	--url	Execute a request against a specified URL. Defaults to the home URL	v=
o	--fields	Limit the output to specific fields. Default is all fields	v=
o	--format	Render output in a particular format	v=
o	--order	Ascending or descending order	v=
o	--orderby	Order by fields	v=
a	1	0
=	profile stage	--format
v	table	
v	json	
v	yaml	
v	csv	
=	profile stage	--order
v	asc	
v	desc	
@	rewrite
s	flush	Flushes rewrite rules
s	list	Gets a list of the current rewrite rules
s	structure	Updates the permalink structure
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	rewrite	--path
t	filepaths
=	rewrite	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	rewrite	--user
v	id	
v	login	
v	email	
@	rewrite flush
o	--hard	Perform a hard flush – update .htaccess rules as well as rewrite rules in database. Works only on…	
@	rewrite list
o	--match	Show rewrite rules matching a particular URL	v=
o	--source	Show rewrite rules from a particular source	v=
o	--fields	Limit the output to specific fields. Defaults to match,query,source	v=
o	--format	Render output in a particular format	v=
=	rewrite list	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
@	rewrite structure
o	--category-base	Set the base for category permalinks, i.e. ‘/category/’	v=
o	--tag-base	Set the base for tag permalinks, i.e. ‘/tag/’	v=
o	--hard	Perform a hard flush – update .htaccess rules as well as rewrite rules in database. Works only on…	
a	1	0
@	role
s	create	Creates a new role
s	delete	Deletes an existing role
s	exists	Checks if a role exists
s	list	Lists all roles
s	reset	Resets any default role to default capabilities
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	role	--path
t	filepaths
=	role	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	role	--user
v	id	
v	login	
v	email	
@	role create
o	--clone	Clone capabilities from an existing role	v=
a	2	0
@	role delete
a	1	0
@	role exists
a	1	0
@	role list
o	--fields	Limit the output to specific row fields	v=
o	--field	Prints the value of a single field	v=
o	--format	Render output in a particular format	v=
=	role list	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
@	role reset
o	--all	If set, all default roles will be reset	
a	1	0
@	scaffold
s	block	Generates PHP, JS and CSS code for registering a Gutenberg block for a plugin or theme
s	child-theme	Generates child theme based on an existing theme
s	plugin	Generates starter code for a plugin
s	plugin-tests	Generates files needed for running PHPUnit tests in a plugin
s	post-type	Generates PHP code for registering a custom post type
s	taxonomy	Generates PHP code for registering a custom taxonomy
s	theme-tests	Generates files needed for running PHPUnit tests in a theme
s	underscores	Generates starter code for a theme based on _s
s	_s	Generates starter code for a theme based on _s
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	scaffold	--path
t	filepaths
=	scaffold	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	scaffold	--user
v	id	
v	login	
v	email	
@	scaffold block
o	--title	The display title for your block	v=
o	--dashicon	The dashicon to make it easier to identify your block	v=
o	--category	The category name to help users browse and discover your block	v=
o	--theme	Create files in the active theme directory. Specify a theme with --theme=<theme> to have the file…	
o	--plugin	Create files in the given plugin’s directory	v=
o	--force	Overwrite files that already exist	
a	1	0
=	scaffold block	--category
v	common	
v	embed	
v	formatting	
v	layout	
v	widgets	
@	scaffold child-theme
o	--parent_theme	What to put in the ‘Template:’ header in ‘style.css’	v=
o	--theme_name	What to put in the ‘Theme Name:’ header in ‘style.css’	v=
o	--author	What to put in the ‘Author:’ header in ‘style.css’	v=
o	--author_uri	What to put in the ‘Author URI:’ header in ‘style.css’	v=
o	--theme_uri	What to put in the ‘Theme URI:’ header in ‘style.css’	v=
o	--activate	Activate the newly created child theme	
o	--enable-network	Enable the newly created child theme for the entire network	
o	--force	Overwrite files that already exist	
a	1	0
@	scaffold plugin
o	--dir	Put the new plugin in some arbitrary directory path. Plugin directory will be path plus supplied…	v=
o	--plugin_name	What to put in the ‘Plugin Name:’ header	v=
o	--plugin_description	What to put in the ‘Description:’ header	v=
o	--plugin_author	What to put in the ‘Author:’ header	v=
o	--plugin_author_uri	What to put in the ‘Author URI:’ header	v=
o	--plugin_uri	What to put in the ‘Plugin URI:’ header	v=
o	--skip-tests	Don’t generate files for unit testing	
o	--ci	Choose a configuration file for a continuous integration provider	v=
o	--activate	Activate the newly created plugin	
o	--enable-network	Network activate the newly generated plugin	
o	--force	Overwrite files that already exist	
a	1	0
=	scaffold plugin	--dir
t	folders
=	scaffold plugin	--ci
v	travis	
v	circle	
v	gitlab	
@	scaffold plugin-tests
o	--dir	Generate test files for a non-standard plugin path. If no plugin slug is specified, the directory…	v=
o	--ci	Choose a configuration file for a continuous integration provider	v=
o	--force	Overwrite files that already exist	
a	1	0
=	scaffold plugin-tests	--dir
t	folders
=	scaffold plugin-tests	--ci
v	travis	
v	circle	
v	gitlab	
v	bitbucket	
@	scaffold post-type
o	--label	The text used to translate the update messages	v=
o	--textdomain	The textdomain to use for the labels	v=
o	--dashicon	The dashicon to use in the menu	v=
o	--theme	Create a file in the active theme directory, instead of sending to STDOUT. Specify a theme with…	
o	--plugin	Create a file in the given plugin’s directory, instead of sending to STDOUT	v=
o	--raw	Just generate the register_post_type() call and nothing else	
o	--force	Overwrite files that already exist	
a	1	0
@	scaffold taxonomy
o	--post_types	Post types to register for use with the taxonomy	v=
o	--label	The text used to translate the update messages	v=
o	--textdomain	The textdomain to use for the labels	v=
o	--theme	Create a file in the active theme directory, instead of sending to STDOUT. Specify a theme with…	
o	--plugin	Create a file in the given plugin’s directory, instead of sending to STDOUT	v=
o	--raw	Just generate the register_taxonomy() call and nothing else	
o	--force	Overwrite files that already exist	
a	1	0
@	scaffold theme-tests
o	--dir	Generate test files for a non-standard theme path. If no theme slug is specified, the directory…	v=
o	--ci	Choose a configuration file for a continuous integration provider	v=
o	--force	Overwrite files that already exist	
a	1	0
=	scaffold theme-tests	--dir
t	folders
=	scaffold theme-tests	--ci
v	travis	
v	circle	
v	gitlab	
v	bitbucket	
@	scaffold underscores
o	--activate	Activate the newly downloaded theme	
o	--enable-network	Enable the newly downloaded theme for the entire network	
o	--theme_name	What to put in the ‘Theme Name:’ header in ‘style.css’	v=
o	--author	What to put in the ‘Author:’ header in ‘style.css’	v=
o	--author_uri	What to put in the ‘Author URI:’ header in ‘style.css’	v=
o	--sassify	Include stylesheets as SASS	
o	--woocommerce	Include WooCommerce boilerplate files	
o	--force	Overwrite files that already exist	
a	1	0
@	scaffold _s
o	--activate	Activate the newly downloaded theme	
o	--enable-network	Enable the newly downloaded theme for the entire network	
o	--theme_name	What to put in the ‘Theme Name:’ header in ‘style.css’	v=
o	--author	What to put in the ‘Author:’ header in ‘style.css’	v=
o	--author_uri	What to put in the ‘Author URI:’ header in ‘style.css’	v=
o	--sassify	Include stylesheets as SASS	
o	--woocommerce	Include WooCommerce boilerplate files	
o	--force	Overwrite files that already exist	
a	1	0
@	search-replace
o	--dry-run	Run the entire search/replace operation and show report, but don’t save changes to the database	
o	--network	Search/replace through all the tables registered to $wpdb in a multisite install	
o	--all-tables-with-prefix	Enable replacement on any tables that match the table prefix even if not registered on $wpdb	
o	--all-tables	Enable replacement on ALL tables in the database, regardless of the prefix, and even if not…	
o	--export	Write transformed data as SQL file instead of saving replacements to the database. If <file> is…	v=
o	--export_insert_size	Define number of rows in single INSERT statement when doing SQL export. You might want to change…	v=
o	--skip-tables	Do not perform the replacement on specific tables. Use commas to specify multiple tables…	v=
o	--skip-columns	Do not perform the replacement on specific columns. Use commas to specify multiple columns	v=
o	--include-columns	Perform the replacement on specific columns. Use commas to specify multiple columns	v=
o	--precise	Force the use of PHP (instead of SQL) which is more thorough, but slower	
o	--recurse-objects	Enable recursing into objects to replace strings. Defaults to true; pass –no-recurse-objects to…	
o	--no-recurse-objects	Enable recursing into objects to replace strings. Defaults to true; pass –no-recurse-objects to…	
o	--verbose	Prints rows to the console as they’re updated	
o	--regex	Runs the search using a regular expression (without delimiters). Warning: search-replace will take…	
o	--regex-flags	Pass PCRE modifiers to regex search-replace (e.g. ‘i’ for case-insensitivity)	v=
o	--regex-delimiter	The delimiter to use for the regex. It must be escaped if it appears in the search string. The…	v=
o	--regex-limit	The maximum possible replacements for the regex per row (or per unserialized data bit per row)…	v=
o	--format	Render output in a particular format	v=
o	--report	Produce report. Defaults to true	
o	--report-changed-only	Report changed fields only. Defaults to false, unless logging, when it defaults to true	
o	--log	Log the items changed. If <file> is not supplied or is “-“, will output to STDOUT. Warning: causes…	V=
o	--before_context	For logging, number of characters to display before the old match and the new replacement. Default…	v=
o	--after_context	For logging, number of characters to display after the old match and the new replacement. Default…	v=
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
a	3	0
=	search-replace	--export_insert_size
v	50	
=	search-replace	--format
v	table	
v	count	
=	search-replace	--path
t	filepaths
=	search-replace	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	search-replace	--user
v	id	
v	login	
v	email	
@	server
o	--host	The hostname to bind the server to	v=
o	--port	The port number to bind the server to	v=
o	--docroot	The path to use as the document root. If the path global parameter is set, the default value is it	v=
o	--config	Config the server with a specific .ini file	v=
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	server	--host
v	localhost	
=	server	--port
v	8080	
=	server	--docroot
t	folders
=	server	--path
t	filepaths
=	server	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	server	--user
v	id	
v	login	
v	email	
@	shell
o	--basic	Force the use of WP-CLI’s built-in PHP REPL, even if the Boris or PsySH PHP REPLs are available	
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	shell	--path
t	filepaths
=	shell	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	shell	--user
v	id	
v	login	
v	email	
@	sidebar
s	list	Lists registered sidebars
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	sidebar	--path
t	filepaths
=	sidebar	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	sidebar	--user
v	id	
v	login	
v	email	
@	sidebar list
o	--fields	Limit the output to specific row fields	v=
o	--format	Render output in a particular format	v=
=	sidebar list	--format
v	table	
v	csv	
v	json	
v	ids	
v	count	
v	yaml	
@	site
s	activate	Activates one or more sites
s	archive	Archives one or more sites
s	create	Creates a site in a multisite installation
s	deactivate	Deactivates one or more sites
s	delete	Deletes a site in a multisite installation
s	empty	Empties a site of its content (posts, comments, terms, and meta)
s	list	Lists all sites in a multisite installation
s	mature	Sets one or more sites as mature
s	meta	Adds, updates, deletes, and lists site custom fields
s	option	Adds, updates, deletes, and lists site options in a multisite installation
s	private	Sets one or more sites as private
s	public	Sets one or more sites as public
s	spam	Marks one or more sites as spam
s	switch-language	Activates a given language
s	unarchive	Unarchives one or more sites
s	unmature	Sets one or more sites as immature
s	unspam	Removes one or more sites from spam
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	site	--path
t	filepaths
=	site	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	site	--user
v	id	
v	login	
v	email	
@	site activate
a	1	0
@	site archive
a	1	0
@	site create
o	--slug	Path for the new site. Subdomain on subdomain installs, directory on subdirectory installs	v=
o	--title	Title of the new site. Default: prettified slug	v=
o	--email	Email for Admin user. User will be created if none exists. Assignment to Super Admin if not included	v=
o	--network_id	Network to associate new site with. Defaults to current network (typically 1)	v=
o	--private	If set, the new site will be non-public (not indexed)	
o	--porcelain	If set, only the site id will be output on success	
@	site deactivate
a	1	0
@	site delete
o	--slug	Path of the blog to be deleted. Subdomain on subdomain installs, directory on subdirectory installs	v=
o	--yes	Answer yes to the confirmation message	
o	--keep-tables	Delete the blog from the list, but don’t drop it’s tables	
a	1	0
@	site empty
o	--uploads	Also delete all files in the site’s uploads directory	
o	--yes	Proceed to empty the site without a confirmation prompt	
@	site list
o	--network	The network to which the sites belong	v=
o	--field=value	The serialization format for the value	
o	--site_in	Only list the sites with these blog_id values (comma-separated)	v=
o	--field	Prints the value of a single field for each site	v=
o	--fields	Comma-separated list of fields to show	v=
o	--format	Render output in a particular format	v=
=	site list	--format
v	table	
v	csv	
v	count	
v	ids	
v	json	
v	yaml	
@	site mature
a	1	0
@	site meta
s	add	Add a meta field
s	delete	Delete a meta field
s	get	Get meta field value
s	list	List all metadata associated with an object
s	patch	Update a nested value for a meta field
s	pluck	Get a nested value from a meta field
s	update	Update a meta field
@	site meta add
o	--format	The serialization format for the value	v=
a	3	0
=	site meta add	--format
v	plaintext	
v	json	
@	site meta delete
o	--all	Delete all meta for the object	
a	3	0
@	site meta get
o	--format	Get value in a particular format	v=
a	2	0
=	site meta get	--format
v	var_export	
v	json	
v	yaml	
@	site meta list
o	--keys	Limit output to metadata of specific keys	v=
o	--fields	Limit the output to specific row fields. Defaults to id,meta_key,meta_value	v=
o	--format	Render output in a particular format	v=
o	--orderby	Set orderby which field	v=
o	--order	Set ascending or descending order	v=
o	--unserialize	Unserialize meta_value output	
a	1	0
=	site meta list	--fields
v	id,meta_key,meta_value	
=	site meta list	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
=	site meta list	--orderby
v	id	
v	meta_key	
v	meta_value	
=	site meta list	--order
v	asc	
v	desc	
@	site meta patch
o	--format	The serialization format for the value	v=
a	5	0
=	site meta patch	--format
v	plaintext	
v	json	
#	site meta patch	1
v	insert	
v	update	
v	delete	
@	site meta pluck
o	--format	The output format of the value	v=
a	3	0
=	site meta pluck	--format
v	plaintext	
v	json	
v	yaml	
@	site meta update
o	--format	The serialization format for the value	v=
a	3	0
=	site meta update	--format
v	plaintext	
v	json	
@	site option
s	add	Adds a site option
s	delete	Deletes a site option
s	get	Gets a site option
s	list	Lists site options
s	patch	Updates a nested value in an option
s	pluck	Gets a nested value from an option
s	update	Updates a site option
@	site option add
o	--format	The serialization format for the value	v=
a	2	0
=	site option add	--format
v	plaintext	
v	json	
@	site option delete
a	1	0
@	site option get
o	--format	Get value in a particular format	v=
a	1	0
=	site option get	--format
v	var_export	
v	json	
v	yaml	
@	site option list
o	--search	Use wildcards ( * and ? ) to match option name	v=
o	--site_id	Limit options to those of a particular site id	v=
o	--field	Prints the value of a single field	v=
o	--fields	Limit the output to specific object fields	v=
o	--format	The serialization format for the value. total_bytes displays the total size of matching options in…	v=
=	site option list	--format
v	table	
v	json	
v	csv	
v	count	
v	yaml	
v	total_bytes	
@	site option patch
o	--format	The serialization format for the value	v=
a	4	0
=	site option patch	--format
v	plaintext	
v	json	
#	site option patch	1
v	insert	
v	update	
v	delete	
@	site option pluck
o	--format	The output format of the value	v=
a	2	0
=	site option pluck	--format
v	plaintext	
v	json	
v	yaml	
@	site option update
o	--format	The serialization format for the value	v=
a	2	0
=	site option update	--format
v	plaintext	
v	json	
@	site private
a	1	0
@	site public
a	1	0
@	site spam
a	1	0
@	site switch-language
a	1	0
@	site unarchive
a	1	0
@	site unmature
a	1	0
@	site unspam
a	1	0
@	super-admin
s	add	Grants super admin privileges to one or more users
s	list	Lists users with super admin capabilities
s	remove	Removes super admin privileges from one or more users
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	super-admin	--path
t	filepaths
=	super-admin	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	super-admin	--user
v	id	
v	login	
v	email	
@	super-admin add
a	1	0
@	super-admin list
o	--format	Render output in a particular format	v=
=	super-admin list	--format
v	list	
v	table	
v	csv	
v	json	
v	count	
v	yaml	
@	super-admin remove
a	1	0
@	taxonomy
s	get	Gets details about a registered taxonomy
s	list	Lists registered taxonomies
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	taxonomy	--path
t	filepaths
=	taxonomy	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	taxonomy	--user
v	id	
v	login	
v	email	
@	taxonomy get
o	--field	Instead of returning the whole taxonomy, returns the value of a single field	v=
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	taxonomy get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	taxonomy list
o	--field=value	Filter by one or more fields (see get_taxonomies() first parameter for a list of available fields)	
o	--field	Prints the value of a single field for each taxonomy	v=
o	--fields	Limit the output to specific taxonomy fields	v=
o	--format	Render output in a particular format	v=
=	taxonomy list	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
@	term
s	create	Creates a new term
s	delete	Deletes an existing term
s	generate	Generates some terms
s	get	Gets details about a term
s	list	Lists terms in a taxonomy
s	meta	Adds, updates, deletes, and lists term custom fields
s	migrate	Migrate a term of a taxonomy to another taxonomy
s	recount	Recalculates number of posts assigned to each term
s	update	Updates an existing term
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	term	--path
t	filepaths
=	term	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	term	--user
v	id	
v	login	
v	email	
@	term create
o	--slug	A unique slug for the new term. Defaults to sanitized version of name	v=
o	--description	A description for the new term	v=
o	--parent	A parent for the new term	v=
o	--porcelain	Output just the new term id	
a	2	0
@	term delete
o	--by	Explicitly handle the term value as a slug or id	v=
a	2	0
=	term delete	--by
v	slug	
v	id	
@	term generate
o	--count	How many terms to generate?	v=
o	--max_depth	Generate child terms down to a certain depth	v=
o	--format	Render output in a particular format	v=
a	1	0
=	term generate	--count
v	100	
=	term generate	--max_depth
v	1	
=	term generate	--format
v	progress	
v	ids	
@	term get
o	--by	Explicitly handle the term value as a slug or id	v=
o	--field	Instead of returning the whole term, returns the value of a single field	v=
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Get value in a particular format	v=
a	2	0
=	term get	--by
v	slug	
v	id	
=	term get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	term list
o	--field=value	Filter by one or more fields (see get_terms() $args parameter for a list of fields)	
o	--field	Prints the value of a single field for each term	v=
o	--fields	Limit the output to specific object fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	term list	--format
v	table	
v	csv	
v	ids	
v	json	
v	count	
v	yaml	
@	term meta
s	add	Add a meta field
s	delete	Delete a meta field
s	get	Get meta field value
s	list	List all metadata associated with an object
s	patch	Update a nested value for a meta field
s	pluck	Get a nested value from a meta field
s	update	Update a meta field
@	term meta add
o	--format	The serialization format for the value	v=
a	3	0
=	term meta add	--format
v	plaintext	
v	json	
@	term meta delete
o	--all	Delete all meta for the object	
a	3	0
@	term meta get
o	--format	Get value in a particular format	v=
a	2	0
=	term meta get	--format
v	var_export	
v	json	
v	yaml	
@	term meta list
o	--keys	Limit output to metadata of specific keys	v=
o	--fields	Limit the output to specific row fields. Defaults to id,meta_key,meta_value	v=
o	--format	Render output in a particular format	v=
o	--orderby	Set orderby which field	v=
o	--order	Set ascending or descending order	v=
o	--unserialize	Unserialize meta_value output	
a	1	0
=	term meta list	--fields
v	id,meta_key,meta_value	
=	term meta list	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
=	term meta list	--orderby
v	id	
v	meta_key	
v	meta_value	
=	term meta list	--order
v	asc	
v	desc	
@	term meta patch
o	--format	The serialization format for the value	v=
a	5	0
=	term meta patch	--format
v	plaintext	
v	json	
#	term meta patch	1
v	insert	
v	update	
v	delete	
@	term meta pluck
o	--format	The output format of the value	v=
a	3	0
=	term meta pluck	--format
v	plaintext	
v	json	
v	yaml	
@	term meta update
o	--format	The serialization format for the value	v=
a	3	0
=	term meta update	--format
v	plaintext	
v	json	
@	term migrate
o	--by	Explicitly handle the term value as a slug or id	v=
o	--from	Taxonomy slug of the term to migrate	v=
o	--to	Taxonomy slug to migrate to	v=
a	1	0
=	term migrate	--by
v	slug	
v	id	
@	term recount
a	1	0
@	term update
o	--by	Explicitly handle the term value as a slug or id	v=
o	--name	A new name for the term	v=
o	--slug	A new slug for the term	v=
o	--description	A new description for the term	v=
o	--parent	A new parent for the term	v=
a	2	0
=	term update	--by
v	slug	
v	id	
@	theme
s	activate	Activates a theme
s	auto-updates	Manages theme auto-updates
s	delete	Deletes one or more themes
s	disable	Disables a theme on a WordPress multisite install
s	enable	Enables a theme on a WordPress multisite install
s	get	Gets details about a theme
s	install	Installs one or more themes
s	is-active	Checks if a given theme is active
s	is-installed	Checks if a given theme is installed
s	list	Gets a list of themes
s	mod	Sets, gets, and removes theme mods
s	path	Gets the path to a theme or to the theme directory
s	search	Searches the WordPress.org theme directory
s	status	Reveals the status of one or all themes
s	update	Updates one or more themes
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	theme	--path
t	filepaths
=	theme	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	theme	--user
v	id	
v	login	
v	email	
@	theme activate
a	1	0
@	theme auto-updates
s	disable	Disables the auto-updates for a theme
s	enable	Enables the auto-updates for a theme
s	status	Shows the status of auto-updates for a theme
@	theme auto-updates disable
o	--all	If set, auto-updates will be disabled for all themes	
o	--enabled-only	If set, filters list of themes to only include the ones that have auto-updates enabled	
a	1	0
@	theme auto-updates enable
o	--all	If set, auto-updates will be enabled for all themes	
o	--enabled-only	If set, filters list of themes to only include the ones that have auto-updates disabled	
a	1	0
@	theme auto-updates status
o	--all	If set, the status of auto-updates for all themes will be shown	
o	--enabled-only	If set, filters list of themes to only include the ones that have auto-updates enabled	
o	--disabled-only	If set, filters list of themes to only include the ones that have auto-updates disabled	
o	--field	Only show the provided field	v=
a	1	0
@	theme delete
o	--all	If set, all themes will be deleted except active theme	
o	--force	To delete active theme use this	
a	1	0
@	theme disable
o	--network	If set, the theme is disabled on the network level. Note that individual sites may still have this…	
a	1	0
@	theme enable
o	--network	If set, the theme is enabled for the entire network	
o	--activate	If set, the theme is activated for the current site. Note that the “network” flag has no influence…	
a	1	0
@	theme get
o	--field	Instead of returning the whole theme, returns the value of a single field	v=
o	--fields	Limit the output to specific fields. Defaults to all fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	theme get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	theme install
o	--version	If set, get that particular version from wordpress.org, instead of the stable version	v=
o	--force	If set, the command will overwrite any installed version of the theme, without prompting for…	
o	--activate	If set, the theme is activated for the current site. Note that the “network” flag has no influence…	
o	--insecure	Retry downloads without certificate validation if TLS handshake fails. Note: This makes the…	
a	1	0
@	theme is-active
a	1	0
@	theme is-installed
a	1	0
@	theme list
o	--field=value	Filter results based on the value of a field	
o	--field	Prints the value of a single field for each theme	v=
o	--fields	Limit the output to specific object fields	v=
o	--format	Render output in a particular format	v=
o	--status	Filter the output by theme status	v=
=	theme list	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
=	theme list	--status
v	active	
v	parent	
v	inactive	
@	theme mod
s	get	Gets one or more theme mods
s	list	Gets a list of theme mods
s	remove	Removes one or more theme mods
s	set	Sets the value of a theme mod
@	theme mod get
o	--field	Returns the value of a single field	=
o	--all	List all theme mods	
o	--format	Render output in a particular format	v=
a	1	0
=	theme mod get	--format
v	table	
v	json	
v	csv	
v	yaml	
@	theme mod list
o	--field	Returns the value of a single field	v=
o	--format	Render output in a particular format	v=
=	theme mod list	--format
v	table	
v	json	
v	csv	
v	yaml	
@	theme mod remove
o	--all	Remove all theme mods	
a	1	0
@	theme mod set
a	2	0
@	theme path
o	--dir	If set, get the path to the closest parent directory, instead of the theme’s “style.css” file	
a	1	0
@	theme search
o	--page	Optional page to display	v=
o	--per-page	Optional number of results to display. Defaults to 10	v=
o	--field	Prints the value of a single field for each theme	v=
o	--fields	Ask for specific fields from the API. Defaults to name,slug,author,rating	v=
o	--format	Render output in a particular format	v=
a	1	0
=	theme search	--page
v	1	
=	theme search	--per-page
v	10	
=	theme search	--fields
v	name	
v	slug	
v	version	
v	author	
v	preview_url	
v	screenshot_url	
v	rating	
v	num_ratings	
v	homepage	
v	description	
v	url	
=	theme search	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
@	theme status
a	1	0
@	theme update
o	--all	If set, all themes that have updates will be updated	
o	--exclude	Comma separated list of theme names that should be excluded from updating	v=
o	--format	Render output in a particular format	v=
o	--version	If set, the theme will be updated to the specified version	v=
o	--dry-run	Preview which themes would be updated	
o	--insecure	Retry downloads without certificate validation if TLS handshake fails. Note: This makes the…	
a	1	0
=	theme update	--format
v	table	
v	csv	
v	json	
v	summary	
@	transient
s	delete	Deletes a transient value
s	get	Gets a transient value
s	list	Lists transients and their values
s	set	Sets a transient value
s	type	Determines the type of transients implementation
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	transient	--path
t	filepaths
=	transient	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	transient	--user
v	id	
v	login	
v	email	
@	transient delete
o	--network	Delete the value of a network|site transient. On single site, this is a specially-named cache key…	
o	--all	Delete all transients	
o	--expired	Delete all expired transients	
a	1	0
@	transient get
o	--format	Render output in a particular format	v=
o	--network	Get the value of a network|site transient. On single site, this is a specially-named cache key. On…	
a	1	0
=	transient get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	transient list
o	--search	Use wildcards ( * and ? ) to match transient name	v=
o	--exclude	Pattern to exclude. Use wildcards ( * and ? ) to match transient name	v=
o	--network	Get the values of network|site transients. On single site, this is a specially-named cache key. On…	
o	--unserialize	Unserialize transient values in output	
o	--human-readable	Human-readable output for expirations	
o	--fields	Limit the output to specific object fields	v=
o	--format	Render output in a particular format	v=
=	transient list	--format
v	table	
v	json	
v	csv	
v	count	
v	yaml	
@	transient set
o	--network	Set the value of a network|site transient. On single site, this is a specially-named cache key. On…	
a	3	0
@	transient type
@	user
s	add-cap	Adds a capability to a user
s	add-role	Adds a role for a user
s	check-password	Checks if a user’s password is valid or not
s	create	Creates a new user
s	delete	Deletes one or more users from the current site
s	generate	Generates some users
s	get	Gets details about a user
s	import-csv	Imports users from a CSV file
s	list	Lists users
s	list-caps	Lists all capabilities for a user
s	meta	Adds, updates, deletes, and lists user custom fields
s	remove-cap	Removes a user’s capability
s	remove-role	Removes a user’s role
s	reset-password	Resets the password for one or more users
s	session	Destroys and lists a user’s sessions
s	set-role	Sets the user role
s	spam	Marks one or more users as spam
s	term	Adds, updates, removes, and lists user terms
s	unspam	Removes one or more users from spam
s	update	Updates an existing user
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	user	--path
t	filepaths
=	user	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	user	--user
v	id	
v	login	
v	email	
@	user add-cap
a	2	0
@	user add-role
a	2	0
@	user check-password
o	--escape-chars	Escape password with wp_slash() to mimic the same behavior as wp-login.php	
a	2	0
@	user create
o	--role	The role of the user to create. Default: default role. Possible values include ‘administrator’…	v=
o	--user_pass	The user password. Default: randomly generated	v=
o	--user_registered	The date the user registered. Default: current date	v=
o	--display_name	The display name	v=
o	--user_nicename	A string that contains a URL-friendly name for the user. The default is the user’s username	v=
o	--user_url	A string containing the user’s URL for the user’s web site	v=
o	--nickname	The user’s nickname, defaults to the user’s username	v=
o	--first_name	The user’s first name	v=
o	--last_name	The user’s last name	v=
o	--description	A string containing content about the user	v=
o	--rich_editing	A string for whether to enable the rich editor or not. False if not empty	v=
o	--send-email	Send an email to the user with their new account details	
o	--porcelain	Output just the new user id	
a	2	0
=	user create	--role
v	administrator	
v	editor	
v	author	
v	contributor	
v	subscriber	
@	user delete
o	--network	On multisite, delete the user from the entire network	
o	--reassign	User ID to reassign the posts to	v=
o	--yes	Answer yes to any confirmation prompts	
a	1	0
@	user generate
o	--count	How many users to generate?	v=
o	--role	The role of the generated users. Default: default role from WP	v=
o	--format	Render output in a particular format	v=
=	user generate	--count
v	100	
=	user generate	--format
v	progress	
v	ids	
@	user get
o	--field	Instead of returning the whole user, returns the value of a single field	v=
o	--fields	Get a specific subset of the user’s fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	user get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	user import-csv
o	--send-email	Send an email to new users with their account details	
o	--skip-update	Don’t update users that already exist	
a	1	0
@	user list
o	--role	Only display users with a certain role	v=
o	--field=value	Control output by one or more arguments of WP_User_Query()	
o	--network	List all users in the network for multisite	
o	--field	Prints the value of a single field for each user	v=
o	--fields	Limit the output to specific object fields	v=
o	--format	Render output in a particular format	v=
=	user list	--format
v	table	
v	csv	
v	ids	
v	json	
v	count	
v	yaml	
@	user list-caps
o	--format	Render output in a particular format	v=
a	1	0
=	user list-caps	--format
v	list	
v	table	
v	csv	
v	json	
v	count	
v	yaml	
@	user meta
s	add	Adds a meta field
s	delete	Deletes a meta field
s	get	Gets meta field value
s	list	Lists all metadata associated with a user
s	patch	Update a nested value for a meta field
s	pluck	Get a nested value from a meta field
s	update	Updates a meta field
@	user meta add
o	--format	The serialization format for the value	v=
a	3	0
=	user meta add	--format
v	plaintext	
v	json	
@	user meta delete
a	3	0
@	user meta get
o	--format	Render output in a particular format	v=
a	2	0
=	user meta get	--format
v	table	
v	csv	
v	json	
v	yaml	
@	user meta list
o	--keys	Limit output to metadata of specific keys	v=
o	--fields	Limit the output to specific row fields. Defaults to id,meta_key,meta_value	v=
o	--format	Render output in a particular format	v=
o	--orderby	Set orderby which field	v=
o	--order	Set ascending or descending order	v=
o	--unserialize	Unserialize meta_value output	
a	1	0
=	user meta list	--fields
v	id,meta_key,meta_value	
=	user meta list	--format
v	table	
v	csv	
v	json	
v	count	
v	yaml	
=	user meta list	--orderby
v	id	
v	meta_key	
v	meta_value	
=	user meta list	--order
v	asc	
v	desc	
@	user meta patch
o	--format	The serialization format for the value	v=
a	5	0
=	user meta patch	--format
v	plaintext	
v	json	
#	user meta patch	1
v	insert	
v	update	
v	delete	
@	user meta pluck
o	--format	The output format of the value	v=
a	3	0
=	user meta pluck	--format
v	plaintext	
v	json	
v	yaml	
@	user meta update
o	--format	The serialization format for the value	v=
a	3	0
=	user meta update	--format
v	plaintext	
v	json	
@	user remove-cap
a	2	0
@	user remove-role
a	2	0
@	user reset-password
o	--skip-email	Don’t send an email notification to the affected user(s)	
a	1	0
@	user session
s	destroy	Destroy a session for the given user
s	list	List sessions for the given user
@	user session destroy
o	--all	Destroy all of the user’s sessions	
a	2	0
@	user session list
o	--fields	Limit the output to specific fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	user session list	--format
v	table	
v	csv	
v	json	
v	yaml	
v	count	
v	ids	
@	user set-role
a	2	0
@	user spam
a	1	0
@	user term
s	add	Add a term to an object
s	list	List all terms associated with an object
s	remove	Remove a term from an object
s	set	Set object terms
@	user term add
o	--by	Explicitly handle the term value as a slug or id	v=
a	3	0
=	user term add	--by
v	slug	
v	id	
@	user term list
o	--field	Prints the value of a single field for each term	v=
o	--fields	Limit the output to specific row fields	v=
o	--format	Render output in a particular format	v=
a	2	0
=	user term list	--format
v	table	
v	csv	
v	json	
v	yaml	
v	count	
v	ids	
@	user term remove
o	--by	Explicitly handle the term value as a slug or id	v=
o	--all	Remove all terms from the object	
a	3	0
=	user term remove	--by
v	slug	
v	id	
@	user term set
o	--by	Explicitly handle the term value as a slug or id	v=
a	3	0
=	user term set	--by
v	slug	
v	id	
@	user unspam
a	1	0
@	user update
o	--user_pass	A string that contains the plain text password for the user	v=
o	--user_nicename	A string that contains a URL-friendly name for the user. The default is the user’s username	v=
o	--user_url	A string containing the user’s URL for the user’s web site	v=
o	--user_email	A string containing the user’s email address	v=
o	--display_name	The display name	v=
o	--nickname	The user’s nickname, defaults to the user’s username	v=
o	--first_name	The user’s first name	v=
o	--last_name	The user’s last name	v=
o	--description	A string containing content about the user	v=
o	--rich_editing	A string for whether to enable the rich editor or not. False if not empty	v=
o	--user_registered	The date the user registered. Default: current date	v=
o	--role	A string used to set the user’s role	v=
o	--field	One or more fields to update. For accepted fields, see wp_update_user()	v=
o	--skip-email	Don’t send an email notification to the user	
a	1	0
@	widget
s	add	Adds a widget to a sidebar
s	deactivate	Deactivates one or more widgets from an active sidebar
s	delete	Deletes one or more widgets from a sidebar
s	list	Lists widgets associated with a sidebar
s	move	Moves the position of a widget
s	reset	Resets sidebar
s	update	Updates options for an existing widget
o	--path	Path to the WordPress files	v=
o	--url	Pretend request came from given URL. In multisite, this argument is how the target site is specified	v=
o	--ssh	Perform operation against a remote server over SSH (or a container using scheme of “docker”…	v=
o	--http	Perform operation against a remote WordPress installation over HTTP	v=
o	--user	Set the WordPress user	v=
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	
o	--skip-plugins	Skip loading all plugins, or a comma-separated list of plugins. Note: mu-plugins are still loaded	v=
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	
o	--skip-themes	Skip loading all themes, or a comma-separated list of themes	v=
o	--skip-packages	Skip loading all installed packages	
o	--require	Load PHP file before running the command (may be used more than once)	v=
o	--exec	Execute PHP code before running the command (may be used more than once)	v=
o	--color	Whether to colorize the output	
o	--no-color	Whether to colorize the output	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	
o	--debug	Show all PHP errors and add verbosity to WP-CLI output. Built-in groups include: bootstrap…	v=
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	
o	--prompt	Prompt the user to enter values for all command arguments, or a subset specified as…	v=
o	--quiet	Suppress informational messages	
=	widget	--path
t	filepaths
=	widget	--ssh
v	scheme:	
v	user@	
v	host	
v	container	
v	:port	
v	path	
=	widget	--user
v	id	
v	login	
v	email	
@	widget add
o	--field=value	Widget option to add, with its new value	
a	3	0
@	widget deactivate
a	1	0
@	widget delete
a	1	0
@	widget list
o	--fields	Limit the output to specific row fields	v=
o	--format	Render output in a particular format	v=
a	1	0
=	widget list	--format
v	table	
v	csv	
v	ids	
v	json	
v	count	
v	yaml	
@	widget move
o	--position	Assign the widget to a new position	v=
o	--sidebar-id	Assign the widget to a new sidebars	v=
a	1	0
@	widget reset
o	--all	If set, all sidebars will be reset	
a	1	0
@	widget update
o	--field=value	Field to update, with its new value	
a	1	0
