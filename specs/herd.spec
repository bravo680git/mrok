@	
s	completion	Dump the shell completion script
s	composer	Proxy Composer commands with isolated site's PHP executable
s	coverage	Proxy PHP commands with isolated sith Xdebug code coverage enabled
s	debug	Proxy PHP commands with isolated site's PHP executable and debug.ini loaded
s	directory-listing	Determine directory-listing behavior. Default is off, which means a 404 will display
s	edit	Open the site in your favorite IDE
s	fetch-share-url	Get the URL to the current share tunnel for Expose
s	forget	Remove the current working (or specified) directory from Herd's list of paths
s	help	Display help for a command
s	init	Start the services defined in the Herd manifest file, and apply the configuration
s	isolate	Change the version of PHP used by Herd to serve the current working directory
s	isolate-node	Change the version of Node used by the CLI for the current working directory
s	isolated	List all sites using isolated versions of PHP
s	isolated-node	List all sites using isolated versions of Nodes
s	link	Link the current working directory to Herd
s	links	Display all of the registered Herd links
s	list	List commands
s	log	Tail log file
s	logs	Show the log viewer UI for the given site
s	loopback	Get or set the loopback address used for Herd sites
s	open	Open the site for the current (or specified) directory in your browser
s	park	Register the current working (or specified) directory with Herd
s	parked	Display all the current sites within parked paths
s	paths	Get all of the paths registered with Herd
s	php	Proxy PHP commands with isolated site's PHP executable
s	proxies	Display all of the proxy sites
s	proxy	Create an Nginx proxy site for the specified host. Useful for Reverb, Docker, etc
s	restart	Restart the Herd services
s	secure	Secure the given domain with a trusted TLS certificate
s	secured	Secure the given domain with a trusted TLS certificate
s	share	Share the current site via an Expose tunnel
s	site-information	Display information about the specified site
s	start	Start the Herd services
s	stop	Stop the Herd services
s	tinker	Run tinker/Tinkerwell
s	tld	[domain] Get or set the TLD used for Herd sites
s	unisolate	Stop customizing the version of PHP used by Herd to serve the current working directory
s	unisolate-node	Stop customizing the version of Node used the CLI for the current working directory
s	unlink	Remove the specified Herd link
s	unproxy	Delete an Nginx proxy config
s	unsecure	Stop serving the given domain over HTTPS and remove the trusted TLS certificate
s	use	Change the version of PHP used by Herd
s	which	Display which Herd driver serves the current working directory
s	which-php	Get the PHP executable path for a given site
s	init:fresh	Initialize a Herd manifest file
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	completion
o	--debug	Tail the completion debug log	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
#	completion	1
v	bash	
v	fish	
v	powershell	
v	zsh	
@	composer
@	coverage
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	debug
@	directory-listing
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
#	directory-listing	1
v	on	
v	off	
@	edit
o	--path		
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	fetch-share-url
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	forget
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	help
o	--format	The output format (txt, xml, json, or md) [default: "txt"]	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
#	help	1
d
@	init
o	--fresh	The output format (txt, xml, json, or md) [default: "txt"]	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	isolate
o	--site	Specify the site to isolate (e.g. if the site isn't linked as its directory name)	
o	--silent		
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	isolate-node
o	--site	Specify the site to isolate (e.g. if the site isn't linked as its directory name)	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	isolated
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	isolated-node
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	link
o	--secure	Link the site with a trusted TLS certificate	
o	--isolate	Isolate the site to the PHP version specified, for example 8.3	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	links
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	list
o	--raw	To output raw command list	
o	--format	The output format (txt, xml, json, or md) [default: "txt"]	
o	--short	To skip describing commands' arguments	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	log
o	--lines|-n		
o	--follow|-f		
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	logs
o	--sites	Specify the site to tinker with (e.g. if the site isn't linked as its directory name)	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	loopback
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	open
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	park
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	parked
o	--json		
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	paths
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	php
o	--site	Specify the site to use to get the PHP version (e.g. if the site isn't linked as its directory name)	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	proxies
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	proxy
o	--secure	Create a proxy with a trusted TLS certificate	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	2	0
@	restart
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	secure
o	--expireIn	The amount of days the self signed certificate is valid for. Default is set to "368" [default: 368]	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	secured
o	--expiring	Limits the results to only sites expiring within the next 60 days	
o	--days	To be used with --expiring. Limits the results to only sites expiring within the next X days…	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	share
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	site-information
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	start
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	stop
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	tinker
o	--site	Specify the site to tinker with (e.g. if the site isn't linked as its directory name)	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	tld
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	unisolate
o	--site	Specify the site to un-isolate (e.g. if the site isn't linked as its directory name)	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	unisolate-node
o	--site	Specify the site to un-isolate (e.g. if the site isn't linked as its directory name)	
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	unlink
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	unproxy
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	unsecure
o	--all		
o	--silent		
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	use
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	which
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
@	which-php
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
a	1	0
@	init:fresh
o	--help|-h	Display help for the given command. When no command is given display help for the list command	
o	--version|-V	Display this application version	
o	--quiet|-q	Do not output any message	
o	--verbose|-vv|-vvv|-v	Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	--no-interaction|-n	Do not ask any interactive question	
