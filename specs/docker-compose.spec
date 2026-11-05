@	
s	build	Build or rebuild services
s	config|convert	Converts the compose file to platform's canonical format
s	cp	Copy files/folders between a service container and the local filesystem
s	create	Creates containers for a service
s	down	Stop and remove containers, networks
s	events	Receive real time events from containers
s	exec	Execute a command in a running container
s	images	List images used by the created containers
s	kill	Force stop service containers
s	logs	View output from containers
s	ls	List running compose projects
s	pause	Pause services
s	port	Print the public port for a port binding
s	ps	List containers
s	pull	Pull service images
s	push	Push service images
s	restart	Restart containers
s	rm	Removes stopped service containers
s	run	Run a one-off command on a service
s	start	Start services
s	stop	Stop services
s	top	Display the running processes
s	unpause	Unpause services
s	up	Create and start containers
s	version	Show the Docker Compose version information
o	--ansi	Control when to print ANSI control characters ("never"|"always"|"auto")	v
o	--compatibility	Run compose in backward compatibility mode	
o	--env-file	Specify an alternate environment file	v
o	--file|-f	Compose configuration files	v
o	--profile	Specify a profile to enable	v
o	--project-directory	Specify an alternate working directory (default: the path of the, first specified, Compose file)	v
o	--project-name|-p	Project name	v
=		--ansi
v	never	
v	always	
v	auto	
=		--env-file
t	filepaths
=		--file
t	filepaths
=		--profile
d
=		--project-directory
t	folders
@	build
o	--build-arg	Set build-time variables for services	v
o	--no-cache	Do not use cache when building the image	
o	--progress	Set type of progress output (auto, tty, plain, quiet)	v
o	--pull	Always attempt to pull a newer version of the image	
o	--quiet|-q	Don't print anything to STDOUT	
o	--ssh	Set SSH authentications used when building service images. (use 'default' for using your default…	v
a	1	1
=	build	--build-arg
d
=	build	--progress
v	auto	
v	tty	
v	plain	
v	quiet	
#	build	1
d
@	config
o	--format	Format the output. Values: [yaml | json]	v
o	--hash	Print the service config hash, one per line	v
o	--images	Print the image names, one per line	
o	--no-interpolate	Don't interpolate environment variables	
o	--no-normalize	Don't normalize compose model	
o	--output|-o	Save to file (default to stdout)	v
o	--profiles	Print the profile names, one per line	
o	--quiet|-q	Only validate the configuration, don't print anything	
o	--resolve-image-digests	Pin image tags to digests	
o	--services	Print the service names, one per line	
o	--volumes	Print the volume names, one per line	
a	1	1
=	config	--format
v	yaml	
v	json	
=	config	--output
t	filepaths
#	config	1
d
@	cp
o	--archive|-a	Archive mode (copy all uid/gid information)	
o	--follow-link|-L	Always follow symbol link in SRC_PATH	
o	--index	Index of the container if there are multiple instances of a service	v
a	2	0
@	create
o	--build	Build images before starting containers	
o	--force-recreate	Recreate containers even if their configuration and image haven't changed	
o	--no-build	Don't build an image, even if it's missing	
o	--no-recreate	If containers already exist, don't recreate them. Incompatible with --force-recreate	
a	1	1
#	create	1
d
@	down
o	--remove-orphans	Remove containers for services not defined in the Compose file	
o	--rmi	Remove images used by services. "local" remove only images that don't have a custom tag…	v
o	--timeout|-t	Specify a shutdown timeout in seconds	v
o	--volumes|-v	Remove named volumes declared in the `volumes` section of the Compose file and anonymous volumes…	
@	events
o	--json	Output events as a stream of json objects	
a	1	1
#	events	1
d
@	exec
o	--detach|-d	Detached mode: Run command in the background	
o	--env|-e	Set environment variables	v
o	--index	Index of the container if there are multiple instances of a service [default: 1]	v
o	--no-TTY|-T	Disable pseudo-TTY allocation. By default `docker compose exec` allocates a TTY	
o	--privileged	Give extended privileges to the process	
o	--user|-u	Run the command as this user	v
o	--workdir|-w	Path to workdir directory for this command	v
a	2	1
=	exec	--workdir
t	folders
#	exec	1
d
@	images
o	--quiet|-q	Only display IDs	
a	1	1
#	images	1
d
@	kill
o	--signal|-s	SIGNAL to send to the container	v
a	1	1
#	kill	1
d
@	logs
o	--follow|-f	Follow log output	
o	--no-color	Produce monochrome output	
o	--no-log-prefix	Don't print prefix in logs	
o	--since	Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)	v
o	--tail	Number of lines to show from the end of the logs for each container	v
o	--timestamps|-t	Show timestamps	
o	--until	Show logs before a timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)	v
a	1	1
=	logs	--tail
v	all	
#	logs	1
d
@	ls
o	--all|-a	Show all stopped Compose projects	
o	--filter	Filter output based on conditions provided	v
o	--format	Format the output. Values: [pretty | json]	v
o	--quiet|-q	Only display IDs	
=	ls	--format
v	pretty	
v	json	
@	pause
a	1	1
#	pause	1
d
@	port
o	--index	Index of the container if service has multiple replicas	v
o	--protocol	Tcp or udp	v
a	2	0
=	port	--protocol
v	tcp	
v	udp	
#	port	1
d
@	ps
o	--all|-a	Show all stopped containers (including those created by the run command)	
o	--filter	Filter services by a property (supported filters: status)	v
o	--format	Format the output. Values: [pretty | json]	v
o	--quiet|-q	Only display IDs	
o	--services	Display services	
o	--status	Filter services by status. Values: [paused | restarting | removing | running | dead | created |…	v
a	1	1
=	ps	--format
v	pretty	
v	json	
=	ps	--status
v	paused	
v	restarting	
v	removing	
v	running	
v	dead	
v	created	
v	exited	
#	ps	1
d
@	pull
o	--ignore-pull-failures	Pull what it can and ignores images with pull failures	
o	--include-deps	Also pull services declared as dependencies	
o	--quiet|-q	Pull without printing progress information	
a	1	1
#	pull	1
d
@	push
o	--ignore-push-failures	Push what it can and ignores images with push failures	
a	1	1
#	push	1
d
@	restart
o	--timeout|-t	Specify a shutdown timeout in seconds	v
a	1	1
#	restart	1
d
@	rm
o	--force|-f	Don't ask to confirm removal	
o	--stop|-s	Stop the containers, if required, before removing	
o	--volumes|-v	Remove any anonymous volumes attached to containers	
a	1	1
#	rm	1
d
@	run
o	--detach|-d	Run container in background and print container ID	
o	--entrypoint	Override the entrypoint of the image	v
o	--env|-e	Set environment variables	v
o	--interactive|-i	Keep STDIN open even if not attached	
o	--label|-l	Add or override a label	v
o	--name	Assign a name to the container	v
o	--no-TTY|-T	Disable pseudo-TTY allocation (default: auto-detected)	
o	--no-deps	Don't start linked services	
o	--publish|-p	Publish a container's port(s) to the host	v
o	--quiet-pull	Pull without printing progress information	
o	--rm	Automatically remove the container when it exits	
o	--service-ports	Run command with the service's ports enabled and mapped to the host	
o	--use-aliases	Use the service's network useAliases in the network(s) the container connects to	
o	--user|-u	Run as specified username or uid	v
o	--volume|-v	Bind mount a volume	v
o	--workdir|-w	Working directory inside the container	v
a	2	0
=	run	--workdir
t	folders
#	run	1
d
@	start
a	1	1
#	start	1
d
@	stop
o	--timeout|-t	Specify a shutdown timeout in seconds	v
a	1	1
#	stop	1
d
@	top
a	1	1
#	top	1
d
@	unpause
a	1	1
#	unpause	1
d
@	up
o	--abort-on-container-exit	Stops all containers if any container was stopped. Incompatible with -d	
o	--always-recreate-deps	Recreate dependent containers. Incompatible with --no-recreate	
o	--attach	Attach to service output	v
o	--attach-dependencies	Attach to dependent containers	
o	--build	Build images before starting containers	
o	--detach|-d	Detached mode: Run containers in the background	
o	--exit-code-from	Return the exit code of the selected service container. Implies --abort-on-container-exit	v
o	--force-recreate	Recreate containers even if their configuration and image haven't changed	
o	--no-build	Don't build an image, even if it's missing	
o	--no-color	Produce monochrome output	
o	--no-deps	Don't start linked services	
o	--no-log-prefix	Don't print prefix in logs	
o	--no-recreate	If containers already exist, don't recreate them. Incompatible with --force-recreate	
o	--no-start	Don't start the services after creating them	
o	--quiet-pull	Pull without printing progress information	
o	--remove-orphans	Remove containers for services not defined in the Compose file	
o	--renew-anon-volumes|-V	Recreate anonymous volumes instead of retrieving data from the previous containers	
o	--scale	Scale SERVICE to NUM instances. Overrides the `scale` setting in the Compose file if present	v
o	--timeout|-t	Use this timeout in seconds for container shutdown when attached or when containers are already…	v
o	--wait	Wait for services to be running|healthy. Implies detached mode	
a	1	1
#	up	1
d
@	version
o	--format|-f	Format the output. Values: [pretty | json]. (Default: pretty)	v
o	--short	Shows only Compose's version number	
=	version	--format
v	pretty	
v	json	
