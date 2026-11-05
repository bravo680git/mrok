@	
s	auth	A collection of authentication commands
s	clean	Removes items ddev has created
s	composer	Executes a composer command within the web container
s	config	Create or modify a ddev project configuration in the current directory
s	d|dbg|debug	A collection of debugging commands
s	delete	Remove all project information (including database) for an existing project
s	desc|st|status|describe	Get a detailed description of a running ddev project
s	.|exec	Execute a shell command in the container for a service. Uses the web service by default
s	export-db	Dump a database to a file or to stdout
s	get	Get/Download a 3rd party add-on (service, provider, etc.)
s	hostname	Manage your hostfile entries
s	import-db	Import a sql file into the project
s	import-files	Pull the uploaded files directory of an existing project to the default public upload directory of…
s	l|ls|list	List projects
s	logs	Get the logs from your running services
s	mutagen	Commands for mutagen status and sync, etc
s	sc|stop-containers|pause	Uses 'docker stop' to pause/stop the containers belonging to a project
s	powerdown|poweroff	Completely stop all projects and containers
s	pull	Pull files and database using a configured provider plugin
s	push	Push files and database using a configured provider plugin
s	restart	Restart a project or several projects
s	service	Add or remove, enable or disable extra services
s	share	Share project on the internet via ngrok
s	snapshot	Create a database snapshot for one or more projects
s	ssh	Starts a shell session in the container for a service. Uses web service by default
s	add|start	Start a ddev project
s	remove|rm|stop	Stop and remove the containers of a project. Does not lose or harm anything unless you add…
s	version	Print ddev version and component versions
s	help	Help about any command
o	--json-output|-j	If true, user-oriented output will be in JSON format	p
o	--help|-h	Display help	p
@	auth
s	ssh	Add ssh key authentication to the ddev-ssh-auth container
@	auth ssh
o	--ssh-key-path|-d	Full path to ssh key directory	v
@	clean
o	--all|-a	Clean all ddev projects	
o	--dry-run	Run the clean command without deleting	
@	composer
s	create	Executes 'composer create-project' within the web container with the arguments and flags provided
s	create-project	
@	composer create
o	--yes|-y	Yes - skip confirmation prompt	
@	composer create-project
@	config
s	global	Change global configuration
o	--additional-fqdns	A comma-delimited list of FQDNs for the project	v
o	--additional-hostnames	A comma-delimited list of hostnames for the project	v
o	--auto	Automatically run config without prompting	
o	--bind-all-interfaces	Bind host ports on all interfaces, not just on localhost network interface	
o	--composer-root	Overrides the default composer root directory for the web service	v
o	--composer-root-default	Unsets a web service composer root directory override	
o	--composer-version	Specify override for composer version in web container. This may be "", "1", "2", "2.2", "stable"…	v
o	--create-docroot	Prompts ddev to create the docroot if it doesn't exist	
o	--database	Specify the database type:version to use. Defaults to mariadb:10.4	v
o	--db-image	Sets the db container image	v
o	--db-image-default	Sets the default db container image for this ddev version	
o	--db-working-dir	Overrides the default working directory for the db service	v
o	--db-working-dir-default	Unsets a db service working directory override	
o	--dba-image	Sets the dba container image	v
o	--dba-image-default	Sets the default dba container image for this ddev version	
o	--dba-working-dir	Overrides the default working directory for the dba service	v
o	--dba-working-dir-default	Unsets a dba service working directory override	
o	--dbimage-extra-packages	A comma-delimited list of Debian packages that should be added to db container when the project is…	v
o	--default-container-timeout	Default time in seconds that ddev waits for all containers to become ready on start	v
o	--disable-settings-management	Prevent ddev from creating or updating CMS settings files	
o	--docroot	Provide the relative docroot of the project, like 'docroot' or 'htdocs' or 'web', defaults to…	v
o	--fail-on-hook-fail	Decide whether 'ddev start' should be interrupted by a failing hook	
o	--host-db-port	The db container's localhost-bound port	v
o	--host-dba-port	The dba (PHPMyAdmin) container's localhost-bound port, if exposed via bind-all-interfaces	v
o	--host-https-port	The web container's localhost-bound https port	v
o	--host-webserver-port	The web container's localhost-bound port	v
o	--http-port	The router HTTP port for this project	v
o	--https-port	The router HTTPS port for this project	v
o	--image-defaults	Sets the default web, db, and dba container images	
o	--mailhog-https-port	Router port to be used for mailhog access (https)	v
o	--mailhog-port	Router port to be used for mailhog access	v
o	--mutagen-enabled	Enable mutagen asynchronous update of project in web container	
o	--nfs-mount-enabled	Enable NFS mounting of project in container	
o	--ngrok-args	Provide extra args to ngrok in ddev share	v
o	--no-project-mount	Whether or not to skip mounting project code into the web container	
o	--nodejs-version	Specify the nodejs version to use if you don't want the default NodeJS 16	v
o	--omit-containers	A comma-delimited list of container types that should not be started when the project is started	v
o	--php-version	The version of PHP that will be enabled in the web container	v
o	--phpmyadmin-https-port	Router port to be used for PHPMyAdmin (dba) container access (https)	v
o	--phpmyadmin-port	Router port to be used for PHPMyAdmin (dba) container access	v
o	--project-name	Provide the project name of project to configure (normally the same as the last part of directory…	v
o	--project-tld	Set the top-level domain to be used for projects, defaults to ddev.site	v
o	--project-type	Provide the project type (one of backdrop, drupal10, drupal6, drupal7, drupal8, drupal9, laravel…	v
o	--show-config-location	Output the location of the config.yaml file if it exists, or error that it doesn't exist	
o	--timezone	Specify timezone for containers and php, like Europe/London or America/Denver or GMT or UTC	v
o	--upload-dir	Sets the project's upload directory, the destination directory of the import-files command	v
o	--use-dns-when-possible	Use DNS for hostname resolution instead of /etc/hosts when possible	
o	--web-environment	Set the environment variables in the web container: --web-environment="TYPO3_CONTEXT=Development,SO…	v
o	--web-environment-add	Append environment variables to the web container: --web-environment="TYPO3_CONTEXT=Development,SOM…	v
o	--web-image	Sets the web container image	v
o	--web-image-default	Sets the default web container image for this ddev version	
o	--web-working-dir	Overrides the default working directory for the web service	v
o	--web-working-dir-default	Unsets a web service working directory override	
o	--webimage-extra-packages	A comma-delimited list of Debian packages that should be added to web container when the project…	v
o	--webserver-type	Sets the project's desired webserver type: nginx-fpm or apache-fpm	v
o	--working-dir-defaults	Unsets all service working directory overrides	
o	--xdebug-enabled	Whether or not XDebug is enabled in the web container	
@	config global
o	--auto-restart-containers	If true, automatically restart containers after a reboot or docker restart	
o	--disable-http2	Optionally disable http2 in ddev-router, 'ddev global --disable-http2' or `ddev global…	
o	--fail-on-hook-fail	If true, 'ddev start' will fail when a hook fails	
o	--instrumentation-opt-in	Instrumentation-opt-in=true	
o	--internet-detection-timeout-ms	Increase timeout when checking internet timeout, in milliseconds	v
o	--letsencrypt-email	Email associated with Let's Encrypt, `ddev global --letsencrypt-email=me@example.com'	v
o	--mutagen-enabled	If true, web container will use mutagen caching/asynchronous updates	
o	--nfs-mount-enabled	Enable NFS mounting on all projects globally	
o	--no-bind-mounts	If true, don't use bind-mounts - useful for environments like remote docker where bind-mounts are…	
o	--omit-containers	For example, --omit-containers=dba,ddev-ssh-agent	v
o	--required-docker-compose-version	Override default docker-compose version	v
o	--router-bind-all-interfaces	Router-bind-all-interfaces=true	
o	--simple-formatting	If true, use simple formatting and no color for tables	
o	--table-style	Table style for list and describe, see ~/.ddev/global_config.yaml for values	v
o	--use-docker-compose-from-path	If true, use docker-compose from path instead of private ~/.ddev/bin/docker-compose	
o	--use-hardened-images	If true, use more secure 'hardened' images for an actual internet deployment	
o	--use-letsencrypt	Enables experimental Let's Encrypt integration, 'ddev global --use-letsencrypt' or `ddev global…	
o	--web-environment	Set the environment variables in the web container: --web-environment="TYPO3_CONTEXT=Development,SO…	v
o	--web-environment-add	Append environment variables to the web container: --web-environment="TYPO3_CONTEXT=Development,SOM…	v
@	d
s	capabilities	Show capabilities of this version of ddev
s	check-db-match	Verify that the database in the ddev-db server matches the configured type/version
s	compose-config	Prints the docker-compose configuration of the current project
s	configyaml	Prints the project config.*.yaml usage
s	dockercheck	Diagnose DDEV docker/colima setup
s	download-images	Download all images required by ddev
s	fix-commands	Fix up custom/shell commands without running ddev start
s	get-volume-db-version	Get the database type/version found in the ddev-dbserver's database volume, which may not be the…
s	migrate-database	Migrate a mysql or mariadb database to a different dbtype:dbversion; works only with mysql and…
s	mutagen	Allows access to any mutagen command
s	nfsmount	Checks to see if nfs mounting works for current project
s	refresh	Refreshes docker cache for project
s	router-nginx-config	Prints the nginx config of the router
s	test	Run diagnostics on ddev using the embedded test_ddev.sh script
@	d capabilities
@	d check-db-match
@	d compose-config
@	d configyaml
@	d dockercheck
@	d download-images
@	d fix-commands
@	d get-volume-db-version
@	d migrate-database
@	d mutagen
@	d nfsmount
@	d refresh
@	d router-nginx-config
@	d test
@	delete
s	images	Deletes drud/ddev-* docker images not in use by current ddev version
o	--all|-a	Delete all projects	
o	--clean-containers	Clean up all ddev docker containers which are not required by this version of ddev	
o	--omit-snapshot|-O	Omit/skip database snapshot	
o	--yes|-y	Yes - skip confirmation prompt	
@	delete images
o	--all|-a	If set, deletes all Docker images created by ddev	
o	--yes|-y	Yes - skip confirmation prompt	
@	desc
@	.
o	--dir|-d	Defines the execution directory within the container	v
o	--raw	Use raw exec (do not interpret with bash inside container)	
o	--service|-s	Defines the service to connect to. [e.g. web, db]	v
@	export-db
o	--bzip2	Use bzip2 compression	
o	--file|-f	Provide the path to output the dump	v
o	--gzip|-z	Use gzip compression	
o	--target-db|-d	If provided, target-db is alternate database to export	v
o	--xz	Use xz compression	
@	get
o	--all	List unofficial add-ons for 'ddev get' in addition to the official ones	
o	--list	List available add-ons for 'ddev get'	
@	hostname
o	--remove|-r	Remove the provided host name - ip correlation	
o	--remove-inactive|-R	Remove host names of inactive projects	
@	import-db
o	--extract-path	If provided asset is an archive, provide the path to extract within the archive	v
o	--no-drop	Set if you do NOT want to drop the db before importing	
o	--progress|-p	Display a progress bar during import	
o	--src|-f	Provide the path to a sql dump in .sql or tar/tar.gz/tgz/zip format	v
o	--target-db|-d	If provided, target-db is alternate database to import into	v
@	import-files
o	--extract-path	If provided asset is an archive, optionally provide the path to extract within the archive	v
o	--src	Provide the path to the source directory or tar/tar.gz/tgz/zip archive of files to import	v
@	l
o	--active-only|-A	If set, only currently active projects will be displayed	
o	--continuous	If set, project information will be emitted until the command is stopped	
o	--continuous-sleep-interval|-I	Time in seconds between ddev list --continuous output lists	v
o	--wrap-table|-W	Display table with wrapped text if required	
@	logs
o	--follow|-f	Follow the logs in real time	
o	--service|-s	Defines the service to retrieve logs from. [e.g. web, db]	v
o	--tail	How many lines to show	v
o	--time|-t	Add timestamps to logs	
@	mutagen
s	monitor	Monitor mutagen status
s	reset	Reset mutagen for project
s	st|status	Shows mutagen sync status
s	sync	Explicit sync for mutagen
@	mutagen monitor
@	mutagen reset
@	mutagen st
o	--verbose|-l	Extended/verbose output for mutagen status	
@	mutagen sync
o	--verbose	Extended/verbose output for mutagen status	
@	sc
o	--all|-a	Pause all running projects	
@	powerdown
@	pull
@	push
@	restart
o	--all|-a	Restart all projects	
@	service
s	disable	Disable a 3rd party service
s	enable	Enable a 3rd party service
@	service disable
@	service enable
@	share
o	--subdomain	Ngrok --subdomain argument, as in "ngrok --subdomain my-subdomain:, requires paid ngrok.com account"	v
@	snapshot
o	--all|-a	Snapshot all projects. Will start the project if it is stopped or paused	
o	--cleanup|-C	Cleanup snapshots	
o	--list|-l	List snapshots	
o	--name|-n	Provide a name for the snapshot	v
o	--yes|-y	Yes - skip confirmation prompt	
@	ssh
o	--dir|-d	Defines the destination directory within the container	v
o	--service|-s	Defines the service to connect to. [e.g. web, db]	v
@	add
o	--all|-a	Start all projects	
o	--select|-s	Interactively select a project to start	
o	--skip-confirmation|-y	Skip any confirmation steps	
@	remove
o	--all|-a	Stop and remove all running or container-stopped projects and remove from global projects list	
o	--omit-snapshot|-O	Omit/skip database snapshot	
o	--remove-data|-R	Remove stored project data (MySQL, logs, etc.)	
o	--select|-s	Interactively select a project to stop	
o	--snapshot|-S	Create database snapshot	
o	--stop-ssh-agent	Stop the ddev-ssh-agent container	
o	--unlist|-U	Remove the project from global project list, it won't show in ddev list until started again	
@	version
@	help
s	auth	A collection of authentication commands
s	clean	Removes items ddev has created
s	composer	Executes a composer command within the web container
s	config	Create or modify a ddev project configuration in the current directory
s	d|dbg|debug	A collection of debugging commands
s	delete	Remove all project information (including database) for an existing project
s	desc|st|status|describe	Get a detailed description of a running ddev project
s	.|exec	Execute a shell command in the container for a service. Uses the web service by default
s	export-db	Dump a database to a file or to stdout
s	get	Get/Download a 3rd party add-on (service, provider, etc.)
s	hostname	Manage your hostfile entries
s	import-db	Import a sql file into the project
s	import-files	Pull the uploaded files directory of an existing project to the default public upload directory of…
s	l|ls|list	List projects
s	logs	Get the logs from your running services
s	mutagen	Commands for mutagen status and sync, etc
s	sc|stop-containers|pause	Uses 'docker stop' to pause/stop the containers belonging to a project
s	powerdown|poweroff	Completely stop all projects and containers
s	pull	Pull files and database using a configured provider plugin
s	push	Push files and database using a configured provider plugin
s	restart	Restart a project or several projects
s	service	Add or remove, enable or disable extra services
s	share	Share project on the internet via ngrok
s	snapshot	Create a database snapshot for one or more projects
s	ssh	Starts a shell session in the container for a service. Uses web service by default
s	add|start	Start a ddev project
s	remove|rm|stop	Stop and remove the containers of a project. Does not lose or harm anything unless you add…
s	version	Print ddev version and component versions
@	help auth
s	ssh	Add ssh key authentication to the ddev-ssh-auth container
@	help auth ssh
@	help clean
@	help composer
s	create	Executes 'composer create-project' within the web container with the arguments and flags provided
s	create-project	
@	help composer create
@	help composer create-project
@	help config
s	global	Change global configuration
@	help config global
@	help d
s	capabilities	Show capabilities of this version of ddev
s	check-db-match	Verify that the database in the ddev-db server matches the configured type/version
s	compose-config	Prints the docker-compose configuration of the current project
s	configyaml	Prints the project config.*.yaml usage
s	dockercheck	Diagnose DDEV docker/colima setup
s	download-images	Download all images required by ddev
s	fix-commands	Fix up custom/shell commands without running ddev start
s	get-volume-db-version	Get the database type/version found in the ddev-dbserver's database volume, which may not be the…
s	migrate-database	Migrate a mysql or mariadb database to a different dbtype:dbversion; works only with mysql and…
s	mutagen	Allows access to any mutagen command
s	nfsmount	Checks to see if nfs mounting works for current project
s	refresh	Refreshes docker cache for project
s	router-nginx-config	Prints the nginx config of the router
s	test	Run diagnostics on ddev using the embedded test_ddev.sh script
@	help d capabilities
@	help d check-db-match
@	help d compose-config
@	help d configyaml
@	help d dockercheck
@	help d download-images
@	help d fix-commands
@	help d get-volume-db-version
@	help d migrate-database
@	help d mutagen
@	help d nfsmount
@	help d refresh
@	help d router-nginx-config
@	help d test
@	help delete
s	images	Deletes drud/ddev-* docker images not in use by current ddev version
@	help delete images
@	help desc
@	help .
@	help export-db
@	help get
@	help hostname
@	help import-db
@	help import-files
@	help l
@	help logs
@	help mutagen
s	monitor	Monitor mutagen status
s	reset	Reset mutagen for project
s	st|status	Shows mutagen sync status
s	sync	Explicit sync for mutagen
@	help mutagen monitor
@	help mutagen reset
@	help mutagen st
@	help mutagen sync
@	help sc
@	help powerdown
@	help pull
@	help push
@	help restart
@	help service
s	disable	Disable a 3rd party service
s	enable	Enable a 3rd party service
@	help service disable
@	help service enable
@	help share
@	help snapshot
@	help ssh
@	help add
@	help remove
@	help version
