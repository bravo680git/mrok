@	
s	help	Shows help
s	addon	Addons management commands: install, remove (fin help addon)
s	alias	Manage aliases that allow fin @alias execution (fin help alias). Create/update alias with…
s	db	Manage databases (fin help db)
s	hosts	Hosts file commands: add, remove, list (fin help hosts)
s	project	Manage project(s) (fin help project)
s	ssh-key	Manage SSH keys (fin help ssh-key)
s	system	Manage Docksal state (fin help system)
s	vm	Manage Docksal VM (fin help vm)
s	bash	Open shell into service's container. Defaults to cli
s	config	Show or change configuration (fin help config)
s	exec	Execute a command or a script in cli
s	exec-url	Download script from URL and run it on host (URL should be public)
s	init	Initialize a project (override it with your own automation, see fin help init)
s	image	Image management commands: registry, save, load (fin help image)
s	logs	Show service logs (e.g., Apache logs, MySQL logs) and Unison logs (fin help logs)
s	run-cli|rc	Run a command in a standalone cli container in the current directory (fin help run-cli)
s	share	Create temporary public url for current project using ngrok
s	share-v2	Create a temporary public URL for the project using Cloudflare Tunnel
s	vhosts	List all virtual *.docksal hosts registered in Docksal proxy
s	docker|d	Run Docker commands directly
s	docker-compose|dc	Run Docker Compose commands directly
s	docker-machine|dm	Run Docker Machine commands directly
s	composer	Run Composer commands
s	drush	Drush command (requires Drupal)
s	drupal	Drupal Console command (requires Drupal 8)
s	platform	Platform.sh's CLI (requires docksal/cli 2.3+)
s	terminus	Pantheon's Terminus (requires docksal/cli 2.1+)
s	wp	WordPress CLI command (requires WordPress)
s	cleanup	Remove all unused Docker images, unused Docksal volumes and containers
s	diagnose	Show diagnostic information for troubleshooting and bug reporting
s	sysinfo	Show system information
s	update	Update Docksal
s	version|--version|v|-v	Print fin version. [v, -v] prints short version
@	help
@	addon
s	install	Install addon
s	remove	Remove addon
@	addon install
a	1	0
@	addon remove
a	1	0
@	alias
s	list	Show aliases list
s	remove	Remove alias
a	2	0
@	alias list
@	alias remove
a	1	0
#	alias remove	1
d
@	db
s	import	Truncate the database and import from SQL dump file or stdin
s	dump	Dump a database into an SQL dump file or stdout
s	list|ls	Show list of existing databases
s	cli	Open command line interface to the DB server (and execute query if provided)
s	create	Create a database
s	drop	Delete a database
s	truncate	Truncate a database (defaults to the `default`)
o	--db	Use another database (default is the one set with 'MYSQL_DATABASE')	v=
o	--db-user	Use another mysql username (default is 'root')	v=
o	--db-password	Use another database password (default is the one set with 'MYSQL_ROOT_PASSWORD', see fin config)	v=
o	--db-charset	Override charset when creating a database (default is utf8)	v=
o	--db-collation	Override collation when creating a database (default is utf8_general_ci)	v=
@	db import
o	--progress	Show import progess (requires pv)	
o	--no-truncate	Do no truncate database before import	
a	1	0
#	db import	1
t	filepaths
@	db dump
a	1	0
#	db dump	1
t	filepaths
@	db list
@	db cli
a	1	0
@	db create
a	1	0
@	db drop
a	1	0
#	db drop	1
d
@	db truncate
a	1	0
@	hosts
s	add	Add hostname to hosts file. If none provided uses VIRTUAL_HOST
s	remove	Remove lines containing hostname from hosts file. If none provided uses VIRTUAL_HOST
s	list	Output hosts file
@	hosts add
a	1	0
@	hosts remove
a	1	0
#	hosts remove	1
d
@	hosts list
@	project
s	start	Start project services (alias: fin start)
s	up	Configuration re-read and start project services (alias: fin up)
s	stop	Stop all or specified project services (alias: fin stop)
s	status	List project services (alias: fin ps)
s	restart	Restart project services (alias: fin restart)
s	reset	Recreate all or specified project services, their containers and volumes
s	remove|rm	Remove all project services, networks and all their volumes, or specified services only
s	list	List running Docksal projects (alias: fin pl)
s	create	Create a new project with a pre-configured boilerplate: Drupal, Wordpress, Magento, Laravel…
s	config	Show project configuration
s	build	Build or rebuild services (alias for 'docker-compose build')
@	project start
@	project up
@	project stop
o	--all|-a	Stop all services on all Docksal projects	
a	1	0
#	project stop	1
g	fin docker ps --format '{{.Names}}'	\n
@	project status
@	project restart
@	project reset
a	1	0
#	project reset	1
g	fin docker ps --format '{{.Names}}'	\n
@	project remove
o	--force|-f	Do not ask for confirmation when deleting all project services	
a	1	0
#	project remove	1
g	fin docker ps --format '{{.Names}}'	\n
@	project list
o	--all|-a	List all Docksal projects (stopped as well)	
@	project create
o	--name	Provide project name upfront	v=
o	--choice	Provide software choice number upfront	v=
o	--repo	Clone from a custom repo: name (--choice is set to '0' automatically)	v=
o	--branch	Clone from a custom repo: branch name (optional)	v=
o	--yes|-y	Avoid confirmation	
@	project config
@	project build
@	ssh-key
s	add	Add a private SSH key from $HOME/.ssh by file name. Adds all default keys…
s	ls	List SSH keys loaded in the docksal-ssh-agent
s	rm	Remove all keys from the docksal-ssh-agent
s	new	Generate a new SSH key pair
@	ssh-key add
o	--quiet	Suppress key already loaded notifications	
a	1	0
#	ssh-key add	1
g	bash -c '\command ls $HOME/.ssh | \command grep --color=never -v '\''pub'\'''	\n
@	ssh-key ls
@	ssh-key rm
@	ssh-key new
a	1	0
@	system
s	reset	Reset Docksal
s	start	Start Docksal
s	stop	Stop Docksal
s	status	Check Docksal status
@	system reset
@	system start
@	system stop
@	system status
@	vm
s	start	Start the machine (create if needed)
s	stop	Stop the machine
s	kill	Forcibly stop the machine
s	restart	Restart the machine
s	status	Get the status
s	ssh	Log into ssh or run a command via ssh
s	remove	Remove Docksal machine and cleanup after it
s	ip	Show the machine IP address
s	ls	List all docker machines
s	env	Display the commands to set up the shell for direct use of Docker client
s	mount	Try remounting host filesystem (NFS on macOS, SMB on Windows)
s	ram	Show memory size
s	hdd	Show disk size and usage
s	stats	Show CPU and network usage
s	regenerate-certs	Regenerate TLS certificates and restart the VM
@	vm start
@	vm stop
@	vm kill
@	vm restart
@	vm status
@	vm ssh
a	1	0
@	vm remove
@	vm ip
@	vm ls
@	vm env
@	vm mount
@	vm ram
a	1	0
@	vm hdd
@	vm stats
@	vm regenerate-certs
@	bash
a	1	0
#	bash	1
g	fin docker ps --format '{{.Names}}'	\n
@	config
s	show	Display configuration for the current project
s	env	Display only environment variables section
s	yml	Display static YML project config suitable for export (NOTE: SECRET_* values will not be hidden)
s	generate	Generate empty Docksal configuration for the project
s	set	Set value(s) for the variable(s) in project ENV file
s	remove|rm	Remove variable(s) from project ENV file
s	get	Get the value of the single variable from project ENV file
@	config show
o	--show-secrets	Do not truncate value of SECRET_* environment vars	
@	config env
@	config yml
@	config generate
o	--stack	Set non-default DOCKSAL_STACK during config generate	v=
o	--docroot	Set non-default DOCROOT during config generate	v=
@	config set
o	--global	Set for global ENV file	
o	--env	Set in environment specific project ENV file	v=
a	1	1
=	config set	--env
t	filepaths
@	config remove
o	--global	Remove from global ENV file	
o	--env	Remove from environment specific project ENV file	v=
a	1	1
@	config get
o	--global	Get value from global ENV file	
o	--env	Get value from environment specific project ENV file	v=
a	1	0
=	config get	--env
t	filepaths
@	exec
a	1	0
@	exec-url
a	1	0
@	init
@	image
s	registry	Show all Docksal images on Docker Hub
s	save	Save docker images into a tar archive
s	load	Load docker images from a tar archive
@	image registry
a	1	0
@	image save
o	--system	Save Docksal system images	
o	--project	Save current project's images	
o	--all	Save all images available on the host	
@	image load
a	1	0
#	image load	1
t	filepaths
@	logs
o	-f|--follow	Follow log output	
o	--no-color	Produce monochrome output	
o	--no-log-prefix	Don't print prefix in logs	
o	--since	Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)	v
o	--tail	Number of lines to show from the end of the logs for each container. (default "all")	v
o	-t|--timestamps	Show timestamps	
o	--until	Show logs before a timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)	v
a	1	0
#	logs	1
g	fin docker ps --format '{{.Names}}'	\n
@	run-cli
o	--clean	Run command with a non-persistent $HOME directory	
o	--clenup	Clean the persistent $HOME directory and run command	
o	--debug	Print container debug output	
o	--image	Override default container image	v=
o	-e	Pass environment variable(s) to the container	v
o	-T	Disable pseudo-tty allocation (useful to get clean stdout)	
a	1	0
@	share
o	--host	Override a hostname for ngrok to route to (default is $VIRTUAL_HOST)	v=
@	share-v2
s	start	Start tunnel and print public URL
s	stop	Stop tunnel
s	status	Prints tunnel status and public URL (if Active)
s	url	Prints tunnel public URL
s	logs	Prints tunnel container logs
@	share-v2 start
@	share-v2 stop
@	share-v2 status
@	share-v2 url
@	share-v2 logs
@	vhosts
@	docker
@	docker-compose
@	docker-machine
a	1	0
@	composer
a	1	0
@	drush
a	1	0
@	drupal
a	1	0
@	platform
a	1	0
@	terminus
a	1	0
@	wp
a	1	0
@	cleanup
o	--images	Docker images cleanup Wizard	
o	--hard	Remove ALL stopped containers even unrelated to Docksal (potentially destructive operation)	
@	diagnose
@	sysinfo
@	update
o	DOCKSAL_VERSION	Update Docksal to the latest development version	v=
@	version
