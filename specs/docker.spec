@	
s	attach	Attach local standard input, output, and error streams to a running container,
s	build	Build an image from a Dockerfile
s	commit	Create a new image from a container's changes
s	cp	Copy files/folders between a container and the local filesystem
s	create	Create a new container
s	diff	Inspect changes to files or directories on a container's filesystem
s	events	Get real time events from the server
s	exec	Run a command in a running container
s	export	Export a container's filesystem as a tar archive
s	history	Show the history of an image
s	images	List images
s	import	Import the contents from a tarball to create a filesystem image
s	info	Display system-wide information
s	inspect	Return low-level information on Docker objects
s	kill	Kill one or more running containers
s	load	Load an image from a tar archive or STDIN
s	login	Log in to a Docker registry
s	logout	Log out from a Docker registry
s	logs	Fetch the logs of a container
s	pause	Pause all processes within one or more containers
s	port	List port mappings or a specific mapping for the container
s	ps	List containers
s	pull	Pull an image or a repository from a registry
s	push	Push an image or a repository to a registry
s	rename	Rename a container
s	restart	Restart one or more containers
s	rm	Remove one or more containers
s	rmi	Remove one or more images
s	run	Run a command in a new container
s	save	Save one or more images to a tar archive (streamed to STDOUT by default)
s	search	Search the Docker Hub for images
s	sbom	View the packaged-based Software Bill Of Materials (SBOM) for an image
s	start	Start one or more stopped containers
s	stats	Display a live stream of container(s) resource usage statistics
s	stop	Stop one or more running containers
s	tag	Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
s	top	Display the running processes of a container
s	unpause	Unpause all processes within one or more containers
s	update	Update configuration of one or more containers
s	version	Show the Docker version information
s	wait	Block until one or more containers stop, then print their exit codes
s	builder	Manage builds
s	config	Manage Docker configs
s	container	Manage containers
s	context	Manage contexts
s	image	Manage images
s	network	Manage networks
s	node	Manage Swarm nodes
s	buildx	Extended build capabilities with BuildKit
s	plugin	Manage plugins
s	secret	Manage Docker secrets
s	service	Manage services
s	stack	Manage Docker stacks
s	swarm	Manage Swarm
s	system	Manage Docker
s	trust	Manage trust on Docker images
s	volume	Manage volumes
s	compose	Define and run multi-container applications with Docker
@	attach
o	--detach-keys	Override the key sequence for detaching a container	v
o	--no-stdin	Do not attach STDIN	
o	--sig-proxy	Proxy all received signals to the process (default true)	
@	build
o	--add-host		v
o	--build-arg		v
o	--cache-from		v
o	--disable-content-trust	Skip image verification (default true)	
o	-f|--file	Name of the Dockerfile (Default is 'PATH/Dockerfile')	v
o	--iidfile	Write the image ID to the file	v
o	--isolation	Container isolation technology	v
o	--label	Set metadata for an image	v
o	--network	Set the networking mode for the RUN instructions during build (default "default")	v
o	--no-cache	Do not use cache when building the image	
o	-o|--output	Output destination (format: type=local,dest=path)	v
o	--platform	Set platform if server is multi-platform capable	v
o	--progress	Set type of progress output (auto, plain, tty). Use plain to show container output	v
o	--pull	Always attempt to pull a newer version of the image	
o	-q|--quiet	Suppress the build output and print image ID on success	
o	--secret	Secret file to expose to the build (only if BuildKit enabled): id=mysecret,src=/local/secret	v
o	--squash	Squash newly built layers into a single new layer	
o	--ssh	SSH agent socket or keys to expose to the build (only if BuildKit enabled) (format…	v
o	-t|--tag	Name and optionally a tag in the 'name:tag' format	
o	--target	Set the target build stage to build	v
a	1	0
=	build	-f
t	filepaths
=	build	--progress
v	auto	
v	plain	
v	tty	
=	build	--target
d
#	build	1
t	folders
@	commit
o	-a|--author	Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")	v
o	-c|--change	Apply Dockerfile instruction to the created image	v
o	-m|--message	Commit message	v
o	-p|--pause	Pause container during commit (default true)	
a	2	0
#	commit	1
d
@	cp
o	-a|--archive	Archive mode (copy all uid/gid information)	
o	-L|--follow-link	Always follow symbol link in SRC_PATH	
a	1	0
@	create
o	--add-host	Add a custom host-to-IP mapping (host:ip)	v
o	-a|--attach	Attach to STDIN, STDOUT or STDERR	v
o	--blkio-weight	Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)	v
o	--blkio-weight-device	Block IO weight (relative device weight) (default [])	v
o	--cap-add	Add Linux capabilities	v
o	--cap-drop	Drop Linux capabilities	v
o	--cgroup-parent	Optional parent cgroup for the container	v
o	--cgroupns	Cgroup namespace to use (host|private)	v
o	--cidfile	Write the container ID to the file	v
o	--cpu-period	Limit CPU CFS (Completely Fair Scheduler) period	v
o	--cpu-quota	Limit CPU CFS (Completely Fair Scheduler) quota	v
o	--cpu-rt-period	Limit CPU real-time period in microseconds	v
o	--cpu-rt-runtime	Limit CPU real-time runtime in microseconds	v
o	-c|--cpu-shares	CPU shares (relative weight)	v
o	--cpus	Number of CPUs	v
o	--cpuset-cpus	CPUs in which to allow execution (0-3, 0,1)	v
o	--cpuset-mems	MEMs in which to allow execution (0-3, 0,1)	v
o	--device	Add a host device to the container	v
o	--device-cgroup-rule	Add a rule to the cgroup allowed devices list	v
o	--device-read-bps	Limit read rate (bytes per second) from a device (default [])	v
o	--device-read-iops	Limit read rate (IO per second) from a device (default [])	v
o	--device-write-bps	Limit write rate (bytes per second) to a device (default [])	v
o	--device-write-iops	Limit write rate (IO per second) to a device (default [])	v
o	--disable-content-trust	Skip image verification (default true)	
o	--dns	Set custom DNS servers	v
o	--dns-option	Set DNS options	v
o	--dns-search	Set custom DNS search domains	v
o	--domainname	Container NIS domain name	v
o	--entrypoint	Overwrite the default ENTRYPOINT of the image	v
o	-e|--env	Set environment variables	v
o	--env-file	Read in a file of environment variables	v
o	--expose	Expose a port or a range of ports	v
o	--gpus	GPU devices to add to the container ('all' to pass all GPUs)	v
o	--group-add	Add additional groups to join	v
o	--health-cmd	Command to run to check health	v
o	--health-interval	Time between running the check (ms|s|m|h) (default 0s)	v
o	--health-retries	Consecutive failures needed to report unhealthy	v
o	--health-start-period	Start period for the container to initialize before starting health-retries countdown (ms|s|m|h)…	v
o	--health-timeout	Maximum time to allow one check to run (ms|s|m|h) (default 0s)	v
o	--help	Print usage	
o	-h|--hostname	Container host name	v
o	--init	Run an init inside the container that forwards signals and reaps processes	
o	-i|--interactive	Keep STDIN open even if not attached	
o	--ip	IPv4 address (e.g., 172.30.100.104)	v
o	--ip6	IPv6 address (e.g., 2001:db8::33)	v
o	--ipc	IPC mode to use	v
o	--isolation	Container isolation technology	v
o	--kernel-memory	Kernel memory limit	v
o	-l|--label	Set meta data on a container	v
o	--label-file	Read in a line delimited file of labels	v
o	--link	Add link to another container	v
o	--link-local-ip	Container IPv4/IPv6 link-local addresses	v
o	--log-driver	Logging driver for the container	v
o	--log-opt	Log driver options	v
o	--mac-address	Container MAC address (e.g., 92:d0:c6:0a:29:33)	v
o	-m|--memory	Memory limit	v
o	--memory-reservation	Memory soft limit	v
o	--memory-swap	Swap limit equal to memory plus swap: '-1' to enable unlimited swap	v
o	--memory-swappiness	Tune container memory swappiness (0 to 100) (default -1)	v
o	--mount	Attach a filesystem mount to the container	v
o	--name	Assign a name to the container	v
o	--network	Connect a container to a network	v
o	--network-alias	Add network-scoped alias for the container	v
o	--no-healthcheck	Disable any container-specified HEALTHCHECK	
o	--oom-kill-disable	Disable OOM Killer	
o	--oom-score-adj	Tune host's OOM preferences (-1000 to 1000)	v
o	--pid	PID namespace to use	v
o	--pids-limit	Tune container pids limit (set -1 for unlimited)	v
o	--platform	Set platform if server is multi-platform capable	v
o	--privileged	Give extended privileges to this container	
o	-p|--publish	Publish a container's port(s) to the host	v
o	-P|--publish-all	Publish all exposed ports to random ports	
o	--pull	Pull image before creating ("always"|"missing"|"never") (default "missing")	v
o	--read-only	Mount the container's root filesystem as read only	
o	--restart	Restart policy to apply when a container exits (default "no")	v
o	--rm	Automatically remove the container when it exits	
o	--runtime	Runtime to use for this container	v
o	--security-opt	Security Options	v
o	--shm-size	Size of /dev/shm	v
o	--stop-signal	Signal to stop a container (default "SIGTERM")	v
o	--stop-timeout	Timeout (in seconds) to stop a container	v
o	--storage-opt	Storage driver options for the container	v
o	--sysctl	Sysctl options (default map[])	v
o	--tmpfs	Mount a tmpfs directory	v
o	-t|--tty	Allocate a pseudo-TTY	
o	--ulimit	Ulimit options (default [])	v
o	-u|--user	Username or UID (format: <name|uid>[:<group|gid>])	v
o	--userns	User namespace to use	v
o	--uts	UTS namespace to use	v
o	-v|--volume	Bind mount a volume	v
o	--volume-driver	Optional volume driver for the container	v
o	--volumes-from	Mount volumes from the specified container(s)	v
o	-w|--workdir	Working directory inside the container	v
a	2	0
#	create	1
d
@	diff
a	1	0
#	diff	1
d
@	events
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Format the output using the given Go template	v
o	--since	Show all events created since timestamp	v
o	--until	Stream events until this timestamp	v
@	exec
o	-it	Launch an interactive session	
o	-d|--detach	Detached mode: run command in the background	
o	--detach-keys	Override the key sequence for detaching a container	v
o	-e|--env	Set environment variables	v
o	--env-file	Read in a file of environment variables	v
o	-i|--interactive	Keep STDIN open even if not attached	
o	--privileged	Give extended privileges to the command	
o	-t|--tty	Allocate a pseudo-TTY	
o	-u|--user	Username or UID (format: <name|uid>[:<group|gid>])	v
o	-w|--workdir	Working directory inside the container	v
a	2	0
#	exec	1
d
@	export
o	-o|--output	Write to a file, instead of STDOUT	v
a	1	0
#	export	1
d
@	history
o	--format	Pretty-print images using a Go template	v
o	-H|--human	Print sizes and dates in human readable format (default true)	
o	--no-trunc	Don't truncate output	
o	-q|--quiet	Only show image IDs	
a	1	0
#	history	1
d
@	images
o	-a|--all	Show all images (default hides intermediate images)	
o	--digests	Show digests	
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print images using a Go template	v
o	--no-trunc	Don't truncate output	
o	-q|--quiet	Only show image IDs	
a	1	0
@	import
o	-c|--change	Apply Dockerfile instruction to the created image	v
o	-m|--message	Set commit message for imported image	v
o	--platform	Set platform if server is multi-platform capable	v
a	1	0
@	info
o	-f|--format	Format the output using the given Go template	v
@	inspect
o	-f|--format	Format the output using the given Go template	v
o	-s|--size	Display total file sizes if the type is container	
o	--type	Return JSON for specified type	v
a	1	0
#	inspect	1
d
@	kill
o	-s|--signal	Signal to send to the container (default "KILL")	v
a	1	1
#	kill	1
d
@	load
o	-i	Read from tar archive file, instead of STDIN	v
o	-q|--quiet	Suppress the load output	
@	login
o	-p|--password	Password	v
o	--password-stdin	Take the password from stdin	
o	-u|--username	Username	v
a	1	0
@	logout
a	1	0
@	logs
o	--details	Show extra details provided to logs	
o	-f|--follow	Follow log output	
o	--since	Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)	v
o	-n|--tail	Number of lines to show from the end of the logs (default "all")	v
o	-t|--timestamps	Show timestamps	
o	--until	Show logs before a timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)	v
a	1	0
#	logs	1
d
@	pause
a	1	0
#	pause	1
d
@	port
a	2	0
#	port	1
d
@	ps
o	-a|--all	Show all containers (default shows just running)	
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print containers using a Go template	v
o	-n|--last	Show n last created containers (includes all states) (default -1)	v
o	-l|--latest	Show the latest created container (includes all states)	
o	--no-trunc	Don't truncate output	
o	-q|--quiet	Only display container IDs	
o	-s|--size	Display total file sizes	
@	pull
o	-a|--all-tags	Download all tagged images in the repository	
o	--disable-content-trust	Skip image verification (default true)	
o	--platform	Set platform if server is multi-platform capable	v
o	-q|--quiet	Suppress verbose output	
a	1	0
#	pull	1
d
@	push
o	-a|--all-tags	Push all tagged images in the repository	
o	--disable-content-trust	Skip image signing (default true)	
o	-q|--quiet	Suppress verbose output	
a	1	0
@	rename
a	2	0
#	rename	1
d
@	restart
o	-t|--time	Seconds to wait for stop before killing the container (default 10)	v
a	1	0
#	restart	1
d
@	rm
o	-f|--force	Force the removal of a running container (uses SIGKILL)	
o	-l|--link	Remove the specified link	
o	-v|--volumes	Remove the anonymous volumes associated with the container	
a	1	1
#	rm	1
d
@	rmi
o	-f|--force	Force removal of the image	
o	--no-prune	Do not delete untagged parents	
a	1	1
#	rmi	1
d
@	run
o	-it	Launch an interactive session	
o	--add-host	Add a custom host-to-IP mapping (host:ip)	v
o	-a|--attach	Attach to STDIN, STDOUT or STDERR	v
o	--blkio-weight	Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)	v
o	--blkio-weight-device	Block IO weight (relative device weight) (default [])	v
o	--cap-add	Add Linux capabilities	v
o	--cap-drop	Drop Linux capabilities	v
o	--cgroup-parent	Optional parent cgroup for the container	v
o	--cgroupns	Cgroup namespace to use (host|private)	v
o	--cidfile	Write the container ID to the file	v
o	--cpu-period	Limit CPU CFS (Completely Fair Scheduler) period	v
o	--cpu-quota	Limit CPU CFS (Completely Fair Scheduler) quota	v
o	--cpu-rt-period	Limit CPU real-time period in microseconds	v
o	--cpu-rt-runtime	Limit CPU real-time runtime in microseconds	v
o	-c|--cpu-shares	CPU shares (relative weight)	v
o	--cpus	Number of CPUs	v
o	--cpuset-cpus	CPUs in which to allow execution (0-3, 0,1)	v
o	--cpuset-mems	MEMs in which to allow execution (0-3, 0,1)	v
o	-d|--detach	Run container in background and print container ID	
o	--detach-keys	Override the key sequence for detaching a container	v
o	--device	Add a host device to the container	v
o	--device-cgroup-rule	Add a rule to the cgroup allowed devices list	v
o	--device-read-bps	Limit read rate (bytes per second) from a device (default [])	v
o	--device-read-iops	Limit read rate (IO per second) from a device (default [])	v
o	--device-write-bps	Limit write rate (bytes per second) to a device (default [])	v
o	--device-write-iops	Limit write rate (IO per second) to a device (default [])	v
o	--disable-content-trust	Skip image verification (default true)	
o	--dns	Set custom DNS servers	v
o	--dns-option	Set DNS options	v
o	--dns-search	Set custom DNS search domains	v
o	--domainname	Container NIS domain name	v
o	--entrypoint	Overwrite the default ENTRYPOINT of the image	v
o	-e|--env	Set environment variables	v
o	--env-file	Read in a file of environment variables	v
o	--expose	Expose a port or a range of ports	v
o	--gpus	GPU devices to add to the container ('all' to pass all GPUs)	v
o	--group-add	Add additional groups to join	v
o	--health-cmd	Command to run to check health	v
o	--health-interval	Time between running the check (ms|s|m|h) (default 0s)	v
o	--health-retries	Consecutive failures needed to report unhealthy	v
o	--health-start-period	Start period for the container to initialize before starting health-retries countdown (ms|s|m|h)…	v
o	--health-timeout	Maximum time to allow one check to run (ms|s|m|h) (default 0s)	v
o	--help	Print usage	
o	-h|--hostname	Container host name	v
o	--init	Run an init inside the container that forwards signals and reaps processes	
o	-i|--interactive	Keep STDIN open even if not attached	
o	--ip	IPv4 address (e.g., 172.30.100.104)	v
o	--ip6	IPv6 address (e.g., 2001:db8::33)	v
o	--ipc	IPC mode to use	v
o	--isolation	Container isolation technology	v
o	--kernel-memory	Kernel memory limit	v
o	-l|--label	Set meta data on a container	v
o	--label-file	Read in a line delimited file of labels	v
o	--link	Add link to another container	v
o	--link-local-ip	Container IPv4/IPv6 link-local addresses	v
o	--log-driver	Logging driver for the container	v
o	--log-opt	Log driver options	v
o	--mac-address	Container MAC address (e.g., 92:d0:c6:0a:29:33)	v
o	-m|--memory	Memory limit	v
o	--memory-reservation	Memory soft limit	v
o	--memory-swap	Swap limit equal to memory plus swap: '-1' to enable unlimited swap	v
o	--memory-swappiness	Tune container memory swappiness (0 to 100) (default -1)	v
o	--mount	Attach a filesystem mount to the container	v
o	--name	Assign a name to the container	v
o	--network	Connect a container to a network	v
o	--network-alias	Add network-scoped alias for the container	v
o	--no-healthcheck	Disable any container-specified HEALTHCHECK	
o	--oom-kill-disable	Disable OOM Killer	
o	--oom-score-adj	Tune host's OOM preferences (-1000 to 1000)	v
o	--pid	PID namespace to use	v
o	--pids-limit	Tune container pids limit (set -1 for unlimited)	v
o	--platform	Set platform if server is multi-platform capable	v
o	--privileged	Give extended privileges to this container	
o	-p|--publish	Publish a container's port(s) to the host	v
o	-P|--publish-all	Publish all exposed ports to random ports	
o	--pull	Pull image before running ('always'|'missing'|'never') (default 'missing')	v
o	--read-only	Mount the container's root filesystem as read only	
o	--restart	Restart policy to apply when a container exits (default 'no')	v
o	--rm	Automatically remove the container when it exits	
o	--runtime	Runtime to use for this container	v
o	--security-opt	Security Options	v
o	--shm-size	Size of /dev/shm	v
o	--sig-proxy	Proxy received signals to the process (default true)	
o	--stop-signal	Signal to stop a container (default 'SIGTERM')	v
o	--stop-timeout	Timeout (in seconds) to stop a container	v
o	--storage-opt	Storage driver options for the container	v
o	--sysctl	Sysctl options (default map[])	v
o	--tmpfs	Mount a tmpfs directory	v
o	-t|--tty	Allocate a pseudo-TTY	
o	--ulimit	Ulimit options (default [])	v
o	-u|--user	Username or UID (format: <name|uid>[:<group|gid>])	v
o	--userns	User namespace to use	v
o	--uts	UTS namespace to use	v
o	-v|--volume	Bind mount a volume	v
o	--volume-driver	Optional volume driver for the container	v
o	--volumes-from	Mount volumes from the specified container(s)	v
o	-w|--workdir	Working directory inside the container	v
a	2	0
=	run	--log-driver
v	json-file	
v	syslog	
v	journald	
v	gelf	
v	fluentd	
v	awslogs	
v	splunk	
v	etwlogs	
v	gcplogs	
v	none	
#	run	1
d
@	save
o	-o|--output	Write to a file, instead of STDOUT	v
a	1	0
#	save	1
d
@	search
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print search using a Go template	v
o	--limit	Max number of search results (default 25)	v
o	--no-trunc	Don't truncate output	
a	1	0
@	sbom
o	-D|--debug	Show debug logging	
o	--exclude	Exclude paths from being scanned using a glob expression	v
o	--format	Report output format	v
o	--layers	[experimental] selection of layers to catalog	v
o	-o|--output	File to write the default report output to (default is STDOUT)	v
o	--platform	An optional platform specifier for container image sources (e.g. 'linux/arm64', 'linux/arm64/v8'…	v
o	--quiet	Suppress all non-report output	
o	-v|--version	Version for sbom	
a	1	0
=	sbom	--format
v	syft-json	
v	cyclonedx-xml	
v	cyclonedx-json	
v	github-0-json	
v	spdx-tag-value	
v	spdx-json	
v	table	
v	text	
=	sbom	--layers
v	squashed	
v	all	
=	sbom	-o
t	filepaths
#	sbom	1
d
@	start
o	-a|--attach	Attach STDOUT/STDERR and forward signals	
o	--detach-keys	Override the key sequence for detaching a container	v
o	-i|--interactive	Attach container's STDIN	
a	1	0
#	start	1
d
@	stats
o	-a|--all	Show all containers (default shows just running)	
o	--format	Pretty-print images using a Go template	v
o	--no-stream	Disable streaming stats and only pull the first result	
o	--no-trunc	Do not truncate output	
a	1	0
#	stats	1
d
@	stop
o	-t|--t	Seconds to wait for stop before killing it (default 10)	v
a	1	0
#	stop	1
d
@	tag
a	1	0
@	top
a	1	0
#	top	1
d
@	unpause
a	1	0
#	unpause	1
d
@	update
o	--blkio-weight	Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)	v
o	--cpu-period	Limit CPU CFS (Completely Fair Scheduler) period	v
o	--cpu-quota	Limit CPU CFS (Completely Fair Scheduler) quota	v
o	--cpu-rt-period	Limit the CPU real-time period in microseconds	v
o	--cpu-rt-runtime	Limit the CPU real-time runtime in microseconds	v
o	-c|--cpu-shares	CPU shares (relative weight)	v
o	--cpus	Number of CPUs	v
o	--cpuset-cpus	CPUs in which to allow execution (0-3, 0,1)	v
o	--cpuset-mems	MEMs in which to allow execution (0-3, 0,1)	v
o	--kernel-memory	Kernel memory limit	v
o	-m|--memory	Memory limit	v
o	--memory-reservation	Memory soft limit	v
o	--memory-swap	Swap limit equal to memory plus swap: '-1' to enable unlimited swap	v
o	--pids-limit	Tune container pids limit (set -1 for unlimited)	v
o	--restart	Restart policy to apply when a container exits	v
a	1	0
#	update	1
d
@	version
o	-f|--format	Format the output. Values: [pretty | json]. (Default: pretty)	v
o	--kubeconfig	Kubernetes config file	v
=	version	-f
v	pretty	
v	json	
@	wait
a	1	0
#	wait	1
d
@	builder
s	build	Build an image from a Dockerfile
s	prune	Amount of disk space to keep for cache
@	builder build
o	--add-host		v
o	--build-arg		v
o	--cache-from		v
o	--disable-content-trust	Skip image verification (default true)	
o	-f|--file	Name of the Dockerfile (Default is 'PATH/Dockerfile')	v
o	--iidfile	Write the image ID to the file	v
o	--isolation	Container isolation technology	v
o	--label	Set metadata for an image	v
o	--network	Set the networking mode for the RUN instructions during build (default "default")	v
o	--no-cache	Do not use cache when building the image	
o	-o|--output	Output destination (format: type=local,dest=path)	v
o	--platform	Set platform if server is multi-platform capable	v
o	--progress	Set type of progress output (auto, plain, tty). Use plain to show container output	v
o	--pull	Always attempt to pull a newer version of the image	
o	-q|--quiet	Suppress the build output and print image ID on success	
o	--secret	Secret file to expose to the build (only if BuildKit enabled): id=mysecret,src=/local/secret	v
o	--squash	Squash newly built layers into a single new layer	
o	--ssh	SSH agent socket or keys to expose to the build (only if BuildKit enabled) (format…	v
o	-t|--tag	Name and optionally a tag in the 'name:tag' format	
o	--target	Set the target build stage to build	v
a	1	0
=	builder build	-f
t	filepaths
=	builder build	--progress
v	auto	
v	plain	
v	tty	
=	builder build	--target
d
#	builder build	1
t	folders
@	builder prune
o	-a|--all	Remove all unused build cache, not just dangling ones	
o	--filter	Provide filter values (e.g. 'until=24h')	v
o	-f|--force	Do not prompt for confirmation	
o	--keep-storage	Amount of disk space to keep for cache	v
@	config
s	create	Create a config from a file or STDIN
s	inspect	Display detailed information on one or more configs
s	ls	List configs
s	rm	Remove one or more configs
@	config create
o	-l	Config labels	v
o	--template-driver	Template driver	v
a	1	0
#	config create	1
t	filepaths
@	config inspect
o	-f	Format the output using the given Go template	v
o	--pretty	Print the information in a human friendly format	
a	1	1
@	config ls
o	-f	Filter output based on conditions provided	v
o	--format	Pretty-print configs using a Go template	v
o	-q|--quiet	Only display IDs	
@	config rm
a	1	1
@	container
s	attach	Attach local standard input, output, and error streams to a running container,
s	cp	Copy files/folders between a container and the local filesystem
s	create	Create a new container
s	diff	Inspect changes to files or directories on a container's filesystem
s	exec	Run a command in a running container
s	export	Export a container's filesystem as a tar archive
s	inspect	Return low-level information on Docker objects
s	kill	Kill one or more running containers
s	logs	Fetch the logs of a container
s	ls	List containers
s	pause	Pause all processes within one or more containers
s	port	List port mappings or a specific mapping for the container
s	prune	Remove all stopped containers
s	rename	Rename a container
s	restart	Restart one or more containers
s	rm	Remove one or more containers
s	run	Run a command in a new container
s	start	Start one or more stopped containers
s	stats	Display a live stream of container(s) resource usage statistics
s	stop	Stop one or more running containers
s	top	Display the running processes of a container
s	unpause	Unpause all processes within one or more containers
s	update	Update configuration of one or more containers
s	wait	Block until one or more containers stop, then print their exit codes
@	container attach
o	--detach-keys	Override the key sequence for detaching a container	v
o	--no-stdin	Do not attach STDIN	
o	--sig-proxy	Proxy all received signals to the process (default true)	
@	container cp
o	-a|--archive	Archive mode (copy all uid/gid information)	
o	-L|--follow-link	Always follow symbol link in SRC_PATH	
a	1	0
@	container create
o	--add-host	Add a custom host-to-IP mapping (host:ip)	v
o	-a|--attach	Attach to STDIN, STDOUT or STDERR	v
o	--blkio-weight	Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)	v
o	--blkio-weight-device	Block IO weight (relative device weight) (default [])	v
o	--cap-add	Add Linux capabilities	v
o	--cap-drop	Drop Linux capabilities	v
o	--cgroup-parent	Optional parent cgroup for the container	v
o	--cgroupns	Cgroup namespace to use (host|private)	v
o	--cidfile	Write the container ID to the file	v
o	--cpu-period	Limit CPU CFS (Completely Fair Scheduler) period	v
o	--cpu-quota	Limit CPU CFS (Completely Fair Scheduler) quota	v
o	--cpu-rt-period	Limit CPU real-time period in microseconds	v
o	--cpu-rt-runtime	Limit CPU real-time runtime in microseconds	v
o	-c|--cpu-shares	CPU shares (relative weight)	v
o	--cpus	Number of CPUs	v
o	--cpuset-cpus	CPUs in which to allow execution (0-3, 0,1)	v
o	--cpuset-mems	MEMs in which to allow execution (0-3, 0,1)	v
o	--device	Add a host device to the container	v
o	--device-cgroup-rule	Add a rule to the cgroup allowed devices list	v
o	--device-read-bps	Limit read rate (bytes per second) from a device (default [])	v
o	--device-read-iops	Limit read rate (IO per second) from a device (default [])	v
o	--device-write-bps	Limit write rate (bytes per second) to a device (default [])	v
o	--device-write-iops	Limit write rate (IO per second) to a device (default [])	v
o	--disable-content-trust	Skip image verification (default true)	
o	--dns	Set custom DNS servers	v
o	--dns-option	Set DNS options	v
o	--dns-search	Set custom DNS search domains	v
o	--domainname	Container NIS domain name	v
o	--entrypoint	Overwrite the default ENTRYPOINT of the image	v
o	-e|--env	Set environment variables	v
o	--env-file	Read in a file of environment variables	v
o	--expose	Expose a port or a range of ports	v
o	--gpus	GPU devices to add to the container ('all' to pass all GPUs)	v
o	--group-add	Add additional groups to join	v
o	--health-cmd	Command to run to check health	v
o	--health-interval	Time between running the check (ms|s|m|h) (default 0s)	v
o	--health-retries	Consecutive failures needed to report unhealthy	v
o	--health-start-period	Start period for the container to initialize before starting health-retries countdown (ms|s|m|h)…	v
o	--health-timeout	Maximum time to allow one check to run (ms|s|m|h) (default 0s)	v
o	--help	Print usage	
o	-h|--hostname	Container host name	v
o	--init	Run an init inside the container that forwards signals and reaps processes	
o	-i|--interactive	Keep STDIN open even if not attached	
o	--ip	IPv4 address (e.g., 172.30.100.104)	v
o	--ip6	IPv6 address (e.g., 2001:db8::33)	v
o	--ipc	IPC mode to use	v
o	--isolation	Container isolation technology	v
o	--kernel-memory	Kernel memory limit	v
o	-l|--label	Set meta data on a container	v
o	--label-file	Read in a line delimited file of labels	v
o	--link	Add link to another container	v
o	--link-local-ip	Container IPv4/IPv6 link-local addresses	v
o	--log-driver	Logging driver for the container	v
o	--log-opt	Log driver options	v
o	--mac-address	Container MAC address (e.g., 92:d0:c6:0a:29:33)	v
o	-m|--memory	Memory limit	v
o	--memory-reservation	Memory soft limit	v
o	--memory-swap	Swap limit equal to memory plus swap: '-1' to enable unlimited swap	v
o	--memory-swappiness	Tune container memory swappiness (0 to 100) (default -1)	v
o	--mount	Attach a filesystem mount to the container	v
o	--name	Assign a name to the container	v
o	--network	Connect a container to a network	v
o	--network-alias	Add network-scoped alias for the container	v
o	--no-healthcheck	Disable any container-specified HEALTHCHECK	
o	--oom-kill-disable	Disable OOM Killer	
o	--oom-score-adj	Tune host's OOM preferences (-1000 to 1000)	v
o	--pid	PID namespace to use	v
o	--pids-limit	Tune container pids limit (set -1 for unlimited)	v
o	--platform	Set platform if server is multi-platform capable	v
o	--privileged	Give extended privileges to this container	
o	-p|--publish	Publish a container's port(s) to the host	v
o	-P|--publish-all	Publish all exposed ports to random ports	
o	--pull	Pull image before creating ("always"|"missing"|"never") (default "missing")	v
o	--read-only	Mount the container's root filesystem as read only	
o	--restart	Restart policy to apply when a container exits (default "no")	v
o	--rm	Automatically remove the container when it exits	
o	--runtime	Runtime to use for this container	v
o	--security-opt	Security Options	v
o	--shm-size	Size of /dev/shm	v
o	--stop-signal	Signal to stop a container (default "SIGTERM")	v
o	--stop-timeout	Timeout (in seconds) to stop a container	v
o	--storage-opt	Storage driver options for the container	v
o	--sysctl	Sysctl options (default map[])	v
o	--tmpfs	Mount a tmpfs directory	v
o	-t|--tty	Allocate a pseudo-TTY	
o	--ulimit	Ulimit options (default [])	v
o	-u|--user	Username or UID (format: <name|uid>[:<group|gid>])	v
o	--userns	User namespace to use	v
o	--uts	UTS namespace to use	v
o	-v|--volume	Bind mount a volume	v
o	--volume-driver	Optional volume driver for the container	v
o	--volumes-from	Mount volumes from the specified container(s)	v
o	-w|--workdir	Working directory inside the container	v
a	2	0
#	container create	1
d
@	container diff
a	1	0
#	container diff	1
d
@	container exec
o	-it	Launch an interactive session	
o	-d|--detach	Detached mode: run command in the background	
o	--detach-keys	Override the key sequence for detaching a container	v
o	-e|--env	Set environment variables	v
o	--env-file	Read in a file of environment variables	v
o	-i|--interactive	Keep STDIN open even if not attached	
o	--privileged	Give extended privileges to the command	
o	-t|--tty	Allocate a pseudo-TTY	
o	-u|--user	Username or UID (format: <name|uid>[:<group|gid>])	v
o	-w|--workdir	Working directory inside the container	v
a	2	0
#	container exec	1
d
@	container export
o	-o|--output	Write to a file, instead of STDOUT	v
a	1	0
#	container export	1
d
@	container inspect
o	-f|--format	Format the output using the given Go template	v
o	-s|--size	Display total file sizes if the type is container	
a	1	0
#	container inspect	1
d
@	container kill
o	-s|--signal	Signal to send to the container (default "KILL")	v
a	1	1
#	container kill	1
d
@	container logs
o	--details	Show extra details provided to logs	
o	-f|--follow	Follow log output	
o	--since	Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)	v
o	-n|--tail	Number of lines to show from the end of the logs (default "all")	v
o	-t|--timestamps	Show timestamps	
o	--until	Show logs before a timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)	v
a	1	0
#	container logs	1
d
@	container ls
o	-a|--all	Show all containers (default shows just running)	
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print containers using a Go template	v
o	-n|--last	Show n last created containers (includes all states) (default -1)	v
o	-l|--latest	Show the latest created container (includes all states)	
o	--no-trunc	Don't truncate output	
o	-q|--quiet	Only display container IDs	
o	-s|--size	Display total file sizes	
@	container pause
a	1	0
#	container pause	1
d
@	container port
a	2	0
#	container port	1
d
@	container prune
o	--filter	Provide filter values (e.g. 'until=<timestamp>')	v
o	-f|--force	Do not prompt for confirmation	
@	container rename
a	2	0
#	container rename	1
d
@	container restart
o	-t|--time	Seconds to wait for stop before killing the container (default 10)	v
a	1	0
#	container restart	1
d
@	container rm
o	-f|--force	Force the removal of a running container (uses SIGKILL)	
o	-l|--link	Remove the specified link	
o	-v|--volumes	Remove the anonymous volumes associated with the container	
a	1	1
#	container rm	1
d
@	container run
o	-it	Launch an interactive session	
o	--add-host	Add a custom host-to-IP mapping (host:ip)	v
o	-a|--attach	Attach to STDIN, STDOUT or STDERR	v
o	--blkio-weight	Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)	v
o	--blkio-weight-device	Block IO weight (relative device weight) (default [])	v
o	--cap-add	Add Linux capabilities	v
o	--cap-drop	Drop Linux capabilities	v
o	--cgroup-parent	Optional parent cgroup for the container	v
o	--cgroupns	Cgroup namespace to use (host|private)	v
o	--cidfile	Write the container ID to the file	v
o	--cpu-period	Limit CPU CFS (Completely Fair Scheduler) period	v
o	--cpu-quota	Limit CPU CFS (Completely Fair Scheduler) quota	v
o	--cpu-rt-period	Limit CPU real-time period in microseconds	v
o	--cpu-rt-runtime	Limit CPU real-time runtime in microseconds	v
o	-c|--cpu-shares	CPU shares (relative weight)	v
o	--cpus	Number of CPUs	v
o	--cpuset-cpus	CPUs in which to allow execution (0-3, 0,1)	v
o	--cpuset-mems	MEMs in which to allow execution (0-3, 0,1)	v
o	-d|--detach	Run container in background and print container ID	
o	--detach-keys	Override the key sequence for detaching a container	v
o	--device	Add a host device to the container	v
o	--device-cgroup-rule	Add a rule to the cgroup allowed devices list	v
o	--device-read-bps	Limit read rate (bytes per second) from a device (default [])	v
o	--device-read-iops	Limit read rate (IO per second) from a device (default [])	v
o	--device-write-bps	Limit write rate (bytes per second) to a device (default [])	v
o	--device-write-iops	Limit write rate (IO per second) to a device (default [])	v
o	--disable-content-trust	Skip image verification (default true)	
o	--dns	Set custom DNS servers	v
o	--dns-option	Set DNS options	v
o	--dns-search	Set custom DNS search domains	v
o	--domainname	Container NIS domain name	v
o	--entrypoint	Overwrite the default ENTRYPOINT of the image	v
o	-e|--env	Set environment variables	v
o	--env-file	Read in a file of environment variables	v
o	--expose	Expose a port or a range of ports	v
o	--gpus	GPU devices to add to the container ('all' to pass all GPUs)	v
o	--group-add	Add additional groups to join	v
o	--health-cmd	Command to run to check health	v
o	--health-interval	Time between running the check (ms|s|m|h) (default 0s)	v
o	--health-retries	Consecutive failures needed to report unhealthy	v
o	--health-start-period	Start period for the container to initialize before starting health-retries countdown (ms|s|m|h)…	v
o	--health-timeout	Maximum time to allow one check to run (ms|s|m|h) (default 0s)	v
o	--help	Print usage	
o	-h|--hostname	Container host name	v
o	--init	Run an init inside the container that forwards signals and reaps processes	
o	-i|--interactive	Keep STDIN open even if not attached	
o	--ip	IPv4 address (e.g., 172.30.100.104)	v
o	--ip6	IPv6 address (e.g., 2001:db8::33)	v
o	--ipc	IPC mode to use	v
o	--isolation	Container isolation technology	v
o	--kernel-memory	Kernel memory limit	v
o	-l|--label	Set meta data on a container	v
o	--label-file	Read in a line delimited file of labels	v
o	--link	Add link to another container	v
o	--link-local-ip	Container IPv4/IPv6 link-local addresses	v
o	--log-driver	Logging driver for the container	v
o	--log-opt	Log driver options	v
o	--mac-address	Container MAC address (e.g., 92:d0:c6:0a:29:33)	v
o	-m|--memory	Memory limit	v
o	--memory-reservation	Memory soft limit	v
o	--memory-swap	Swap limit equal to memory plus swap: '-1' to enable unlimited swap	v
o	--memory-swappiness	Tune container memory swappiness (0 to 100) (default -1)	v
o	--mount	Attach a filesystem mount to the container	v
o	--name	Assign a name to the container	v
o	--network	Connect a container to a network	v
o	--network-alias	Add network-scoped alias for the container	v
o	--no-healthcheck	Disable any container-specified HEALTHCHECK	
o	--oom-kill-disable	Disable OOM Killer	
o	--oom-score-adj	Tune host's OOM preferences (-1000 to 1000)	v
o	--pid	PID namespace to use	v
o	--pids-limit	Tune container pids limit (set -1 for unlimited)	v
o	--platform	Set platform if server is multi-platform capable	v
o	--privileged	Give extended privileges to this container	
o	-p|--publish	Publish a container's port(s) to the host	v
o	-P|--publish-all	Publish all exposed ports to random ports	
o	--pull	Pull image before running ('always'|'missing'|'never') (default 'missing')	v
o	--read-only	Mount the container's root filesystem as read only	
o	--restart	Restart policy to apply when a container exits (default 'no')	v
o	--rm	Automatically remove the container when it exits	
o	--runtime	Runtime to use for this container	v
o	--security-opt	Security Options	v
o	--shm-size	Size of /dev/shm	v
o	--sig-proxy	Proxy received signals to the process (default true)	
o	--stop-signal	Signal to stop a container (default 'SIGTERM')	v
o	--stop-timeout	Timeout (in seconds) to stop a container	v
o	--storage-opt	Storage driver options for the container	v
o	--sysctl	Sysctl options (default map[])	v
o	--tmpfs	Mount a tmpfs directory	v
o	-t|--tty	Allocate a pseudo-TTY	
o	--ulimit	Ulimit options (default [])	v
o	-u|--user	Username or UID (format: <name|uid>[:<group|gid>])	v
o	--userns	User namespace to use	v
o	--uts	UTS namespace to use	v
o	-v|--volume	Bind mount a volume	v
o	--volume-driver	Optional volume driver for the container	v
o	--volumes-from	Mount volumes from the specified container(s)	v
o	-w|--workdir	Working directory inside the container	v
a	2	0
=	container run	--log-driver
v	json-file	
v	syslog	
v	journald	
v	gelf	
v	fluentd	
v	awslogs	
v	splunk	
v	etwlogs	
v	gcplogs	
v	none	
#	container run	1
d
@	container start
o	-a|--attach	Attach STDOUT/STDERR and forward signals	
o	--detach-keys	Override the key sequence for detaching a container	v
o	-i|--interactive	Attach container's STDIN	
a	1	0
#	container start	1
d
@	container stats
o	-a|--all	Show all containers (default shows just running)	
o	--format	Pretty-print images using a Go template	v
o	--no-stream	Disable streaming stats and only pull the first result	
o	--no-trunc	Do not truncate output	
a	1	0
#	container stats	1
d
@	container stop
o	-t|--t	Seconds to wait for stop before killing it (default 10)	v
a	1	0
#	container stop	1
d
@	container top
a	1	0
#	container top	1
d
@	container unpause
a	1	0
#	container unpause	1
d
@	container update
o	--blkio-weight	Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)	v
o	--cpu-period	Limit CPU CFS (Completely Fair Scheduler) period	v
o	--cpu-quota	Limit CPU CFS (Completely Fair Scheduler) quota	v
o	--cpu-rt-period	Limit the CPU real-time period in microseconds	v
o	--cpu-rt-runtime	Limit the CPU real-time runtime in microseconds	v
o	-c|--cpu-shares	CPU shares (relative weight)	v
o	--cpus	Number of CPUs	v
o	--cpuset-cpus	CPUs in which to allow execution (0-3, 0,1)	v
o	--cpuset-mems	MEMs in which to allow execution (0-3, 0,1)	v
o	--kernel-memory	Kernel memory limit	v
o	-m|--memory	Memory limit	v
o	--memory-reservation	Memory soft limit	v
o	--memory-swap	Swap limit equal to memory plus swap: '-1' to enable unlimited swap	v
o	--pids-limit	Tune container pids limit (set -1 for unlimited)	v
o	--restart	Restart policy to apply when a container exits	v
a	1	0
#	container update	1
d
@	container wait
a	1	0
#	container wait	1
d
@	context
s	create	Create new context
s	export	Export a context to a tar or kubeconfig file
s	import	Import a context from a tar or zip file
s	inspect	Display detailed information on one or more contexts
s	list	List available contexts
s	rm	Remove one or more contexts
s	show	Print the current context
s	update	Update a context
s	use	Set the default context
o	-h|--help	Help for context	
@	context create
s	aci	Create a context for Azure Container Instances
s	ecs	Create a context for Amazon ECS
o	--default-stack-orchestrator	Default orchestrator for stack operations to use with this context (swarm|kubernetes|all)	v
o	--description	Description of the context	v
o	--docker	Set the docker endpoint (default [])	v
o	--from	Create context from a named context	v
o	-h|--help	Help for create	
o	--kubernetes	Set the kubernetes endpoint (default [])	v
=	context create	--default-stack-orchestrator
v	swarm	
v	kubernetes	
v	all	
@	context create aci
o	--description	Description of the context	v
o	-h|--help	Help for aci	
o	--location	Location (default "eastus")	v
o	--resource-group	Resource group	v
o	--subscription-id	Location	v
a	1	0
@	context create ecs
o	--access-keys	Use AWS access keys from file	v
o	--description	Description of the context	v
o	--from-env	Use AWS environment variables for profile, or credentials and region	
o	-h|--help	Help for ecs	
o	--local-simulation	Create context for ECS local simulation endpoints	
o	--profile	Use an existing AWS profile	v
a	1	0
@	context export
o	-h|--help	Help for export	
o	--kubeconfig	Export as a kubeconfig file	
a	2	0
#	context export	1
d
#	context export	2
t	filepaths
@	context import
o	-h|--help	Help for export	
a	2	0
#	context import	2
t	filepaths
@	context inspect
o	-f	Format the output using the given Go template	v
o	-h|--help	Help for inspect	
a	1	1
#	context inspect	1
d
@	context list
o	--format	Format the output. Values: [pretty | json]. (Default: pretty)	v
o	-h|--help	Help for list	
o	-q|--quiet	Only show context names	
=	context list	--format
v	pretty	
v	json	
@	context rm
o	-f|--force	Force removing current context	
o	-h|--help	Help for rm	
a	1	1
#	context rm	1
d
@	context show
o	-h|--help	Help for show	
@	context update
o	--default-stack-orchestrator	Default orchestrator for stack operations to use with this context (swarm|kubernetes|all)	v
o	--description	Description of the context	v
o	--docker	Set the docker endpoint (default [])	v
o	-h|--help	Help for update	
o	--kubernetes	Set the kubernetes endpoint (default [])	v
a	1	0
=	context update	--default-stack-orchestrator
v	swarm	
v	kubernetes	
v	all	
#	context update	1
d
@	context use
o	-h|--help	Help for use	
a	1	0
#	context use	1
d
@	image
s	build	Build an image from a Dockerfile
s	history	Show the history of an image
s	import	Import the contents from a tarball to create a filesystem image
s	inspect	Display detailed information on one or more images
s	load	Load an image from a tar archive or STDIN
s	ls	List images
s	prune	Remove unused images
s	pull	Pull an image or a repository from a registry
s	push	Push an image or a repository to a registry
s	rm	Remove one or more images
s	save	Save one or more images to a tar archive (streamed to STDOUT by default)
s	tag	Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
@	image build
o	--add-host		v
o	--build-arg		v
o	--cache-from		v
o	--disable-content-trust	Skip image verification (default true)	
o	-f|--file	Name of the Dockerfile (Default is 'PATH/Dockerfile')	v
o	--iidfile	Write the image ID to the file	v
o	--isolation	Container isolation technology	v
o	--label	Set metadata for an image	v
o	--network	Set the networking mode for the RUN instructions during build (default "default")	v
o	--no-cache	Do not use cache when building the image	
o	-o|--output	Output destination (format: type=local,dest=path)	v
o	--platform	Set platform if server is multi-platform capable	v
o	--progress	Set type of progress output (auto, plain, tty). Use plain to show container output	v
o	--pull	Always attempt to pull a newer version of the image	
o	-q|--quiet	Suppress the build output and print image ID on success	
o	--secret	Secret file to expose to the build (only if BuildKit enabled): id=mysecret,src=/local/secret	v
o	--squash	Squash newly built layers into a single new layer	
o	--ssh	SSH agent socket or keys to expose to the build (only if BuildKit enabled) (format…	v
o	-t|--tag	Name and optionally a tag in the 'name:tag' format	
o	--target	Set the target build stage to build	v
a	1	0
=	image build	-f
t	filepaths
=	image build	--progress
v	auto	
v	plain	
v	tty	
=	image build	--target
d
#	image build	1
t	folders
@	image history
o	--format	Pretty-print images using a Go template	v
o	-H|--human	Print sizes and dates in human readable format (default true)	
o	--no-trunc	Don't truncate output	
o	-q|--quiet	Only show image IDs	
a	1	0
#	image history	1
d
@	image import
o	-c|--change	Apply Dockerfile instruction to the created image	v
o	-m|--message	Set commit message for imported image	v
o	--platform	Set platform if server is multi-platform capable	v
a	1	0
@	image inspect
o	-f	Format the output using the given Go template	v
a	1	1
#	image inspect	1
d
@	image load
o	-i	Read from tar archive file, instead of STDIN	v
o	-q|--quiet	Suppress the load output	
@	image ls
o	-a|--all	Show all images (default hides intermediate images)	
o	--digests	Show digests	
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print images using a Go template	v
o	--no-trunc	Don't truncate output	
o	-q|--quiet	Only show image IDs	
a	1	0
@	image prune
o	-a|--all	Remove all unused images, not just dangling ones	
o	--filter	Provide filter values (e.g. 'until=<timestamp>')	v
o	-f|--force	Do not prompt for confirmation	
@	image pull
o	-a|--all-tags	Download all tagged images in the repository	
o	--disable-content-trust	Skip image verification (default true)	
o	--platform	Set platform if server is multi-platform capable	v
o	-q|--quiet	Suppress verbose output	
a	1	0
#	image pull	1
d
@	image push
o	-a|--all-tags	Push all tagged images in the repository	
o	--disable-content-trust	Skip image signing (default true)	
o	-q|--quiet	Suppress verbose output	
a	1	0
@	image rm
o	-f|--force	Force removal of the image	
o	--no-prune	Do not delete untagged parents	
a	1	1
#	image rm	1
d
@	image save
o	-o|--output	Write to a file, instead of STDOUT	v
a	1	0
#	image save	1
d
@	image tag
a	1	0
@	network
s	connect	Connect a container to a network
s	create	Create a network
s	disconnect	Disconnect a container from a network
s	inspect	Display detailed information on one or more networks
s	ls	List networks
s	prune	Remove all unused networks
s	rm	Remove one or more networks
@	network connect
o	--alias	Add network-scoped alias for the container	v
o	--driver-opt	Driver options for the network	v
o	--ip	IPv4 address (e.g., 172.30.100.104)	v
o	--ip6	IPv6 address (e.g., 2001:db8::33)	v
o	--link	Add link to another container	v
o	--link-local-ip	Add a link-local address for the container	v
a	2	0
#	network connect	1
d
#	network connect	2
d
@	network create
o	--attachable	Enable manual container attachment	
o	--aux-address	Auxiliary IPv4 or IPv6 addresses used by Network driver (default map[])	v
o	--config-from	The network from which to copy the configuration	v
o	--config-only	Create a configuration only network	
o	-d|--driver	Driver to manage the Network (default "bridge")	v
o	--gateway	IPv4 or IPv6 Gateway for the master subnet	v
o	--ingress	Create swarm routing-mesh network	
o	--internal	Restrict external access to the network	
o	--ip-range	Allocate container ip from a sub-range	v
o	--ipam-driver	IP Address Management Driver (default "default")	v
o	--ipam-opt	Set IPAM driver specific options (default map[])	v
o	--ipv6	Enable IPv6 networking	
o	--label	Set metadata on a network	v
o	-o|--opt	Set driver specific options (default map[])	v
o	--scope	Control the network's scope	v
o	--subnet	Subnet in CIDR format that represents a network segment	v
a	1	0
@	network disconnect
o	-f|--force	Force the container to disconnect from a network	
a	2	0
#	network disconnect	1
d
#	network disconnect	2
d
@	network inspect
o	-f|--format	Format the output using the given Go template	v
o	-v|--verbose	Verbose output for diagnostics	
a	1	1
#	network inspect	1
d
@	network ls
o	-f|--filter	Provide filter values (e.g. 'driver=bridge')	v
o	--format	Pretty-print networks using a Go template	v
o	--no-trunc	Do not truncate the output	
o	-q|--quiet	Only display network IDs	
@	network prune
o	--filter	Provide filter values (e.g. 'until=<timestamp>')	v
o	-f|--force	Do not prompt for confirmation	
@	network rm
a	1	1
#	network rm	1
d
@	node
s	demote	Demote one or more nodes from manager in the swarm
s	inspect	Display detailed information on one or more nodes
s	ls	List nodes in the swarm
s	promote	Promote one or more nodes to manager in the swarm
s	ps	List tasks running on one or more nodes, defaults to current node
s	rm	Remove one or more nodes from the swarm
s	update	Update a node
@	node demote
a	1	1
#	node demote	1
d
@	node inspect
o	-f|--format	Format the output using the given Go template	v
o	--pretty	Print the information in a human friendly format	
a	1	1
#	node inspect	1
d
@	node ls
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print nodes using a Go template	v
o	-q|--quiet	Only display IDs	
@	node promote
a	1	1
#	node promote	1
d
@	node ps
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print tasks using a Go template	v
o	--no-resolve	Do not map IDs to Names	
o	--no-trunc	Do not truncate output	
o	-q|--quiet	Only display task IDs	
a	1	1
#	node ps	1
d
@	node rm
o	-f|--force	Force remove a node from the swarm	
a	1	1
#	node rm	1
d
@	node update
o	--availability	Availability of the node ("active"|"pause"|"drain")	v
o	--label-add	Add or update a node label (key=value)	v
o	--label-rm	Remove a node label if exists	v
o	--role	Role of the node ("worker"|"manager")	v
a	1	1
#	node update	1
d
@	buildx
s	bake	Bake is a high-level build command. Each specified target will run in parallel as part of the build
s	build	The buildx build command starts a build using BuildKit. This command is similar to the UI of…
s	create	Create a new builder instance
s	du	Disk usage
s	imagetools	Imagetools contains commands for working with manifest lists in the registry. These commands are…
s	inspect	Inspect current builder instance
s	install	Install buildx as a ‘docker builder’ alias
s	ls	List builder instances
s	prune	Remove build cache
s	rm	Remove a builder instance
s	stop	Stop builder instance
s	uninstall	Uninstall the ‘docker builder’ alias
s	use	Set the current builder instance
s	version	Show buildx version information
o	--builder	Override the configured builder instance	vp
@	buildx bake
o	-f|--file	Build definition file	v
o	--load	Shorthand for --set=*.output=type=docker	v
o	--metadata-file	Write build result metadata to the file	v
o	--no-cache	Do not use cache when building the image	v
o	--print	Print the options without building	v
o	--progress	Set type of progress output (auto, plain, tty). Use plain to show container output	v
o	--pull	Always attempt to pull all referenced images	v
o	--push	Shorthand for --set=*.output=type=registry	v
o	--set	Override target value (e.g., targetpattern.key=value)	v
a	1	0
=	buildx bake	--progress
v	auto	
v	plain	
v	tty	
@	buildx build
o	--add-host	Add a custom host-to-IP mapping	v
o	--allow	Allow extra privileged entitlement	v
o	--build-arg	Set build-time variables	v
o	--build-context	Additional build contexts	v
o	--cache-from	External cache sources	v
o	--cache-to	Cache export destinations	v
o	--cgroup-parent	Optional parent cgroup for the container	v
o	--compress	Compress the build context using gzip	v
o	--cpu-period	Limit the CPU CFS (Completely Fair Scheduler) period	v
o	--cpu-quota	Limit the CPU CFS (Completely Fair Scheduler) quota	v
o	--cpu-shares|-c	CPU shares (relative weight)	v
o	--cpuset-cpus	CPUs in which to allow execution (0-3, 0,1)	v
o	--cpuset-mems	MEMs in which to allow execution (0-3, 0,1)	v
o	--file|-f	Name of the Dockerfile	v
o	--force-rm	Always remove intermediate containers	v
o	--iidfile	Write the image ID to the file	v
o	--invoke	Invoke a command after the build [experimental]	v
o	--isolation	Container isolation technology	v
o	--label	Set metadata for an image	v
o	--load	Shorthand for --output=type=docker	v
o	--memory|-m	Memory limit	v
o	--memory-swap	Swap limit equal to memory plus swap: -1 to enable unlimited swap	v
o	--metadata-file	Write build result metadata to the file	v
o	--network	Set the networking mode for the RUN instructions during build	v
o	--no-cache	Do not use cache when building the image	v
o	--no-cache-filter	Do not cache specified stages	v
o	--output|-o	Output destination (format: type=local,dest=path)	v
o	--platform	Set target platform for build	v
o	--print	Print result of information request (e.g., outline, targets) [experimental]	v
o	--progress	Set type of progress output (auto, plain, tty). Use plain to show container output	v
o	--pull	Always attempt to pull all referenced images	v
o	--push	Shorthand for --output=type=registry	v
o	--quiet|-q	Suppress the build output and print image ID on success	v
o	--rm	Remove intermediate containers after a successful build	v
o	--secret	Secret to expose to the build (format: id=mysecret[,src=/local/secret])	v
o	--security-opt	Security options	v
o	--shm-size	Size of /dev/shm	v
o	--squash	Squash newly built layers into a single new layer	v
o	--ssh	SSH agent socket or keys to expose to the build (format: default|&lt;id&gt;[=&lt;socket&gt;|&lt;key…	v
o	--tag|-t	Name and optionally a tag (format: name:tag)	v
o	--target	Set the target build stage to build	v
o	--ulimit	Ulimit options	v
a	1	0
=	buildx build	--progress
v	auto	
v	plain	
v	tty	
@	buildx create
o	--append	Append a node to builder instead of changing it	v
o	--bootstrap	Boot builder after creation	v
o	--buildkitd-flags	Flags for buildkitd daemon	v
o	--config	BuildKit config file	v
o	--driver	Driver to use (available: docker-container, kubernetes, remote)	v
o	--driver-opt	Options for the driver	v
o	--leave	Remove a node from builder instead of changing it	v
o	--name	Builder instance name	v
o	--node	Create/modify node with given name	v
o	--platform	Fixed platforms for current node	v
o	--use	Set the current builder instance	v
a	1	0
@	buildx du
o	--filter	Provide filter values	
o	--verbose	Provide a more verbose output	
a	1	0
@	buildx imagetools
s	create	Create a new image based on source images
s	inspect	Inspect current builder instance
a	1	0
@	buildx imagetools create
o	--append	Append to existing manifest	v
o	--dry-run	Show final image instead of pushing	v
o	--file|-f	Read source descriptor from file	v
o	--progress	Set type of progress output (auto, plain, tty). Use plain to show container output	v
o	--tag|-t	Set reference for new image	v
a	1	0
=	buildx imagetools create	--progress
v	auto	
v	plain	
v	tty	
@	buildx imagetools inspect
o	--format	Format the output using the given Go template	v
o	--raw	Show original, unformatted JSON manifest	
a	1	0
@	buildx inspect
o	--bootstrap	Ensure builder has booted before inspecting	v
a	1	0
@	buildx install
@	buildx ls
@	buildx prune
o	--all|-a	Include internal/frontend images	v
o	--filter	Provide filter values (e.g., until=24h)	v
o	--force|-f	Do not prompt for confirmation	v
o	--keep-storage	Amount of disk space to keep for cache	v
o	--verbose	Provide a more verbose output	v
a	1	0
@	buildx rm
o	--all-inactive	Remove all inactive builders	v
o	--force|-f	Do not prompt for confirmation	v
o	--keep-daemon	Keep the buildkitd daemon running	v
o	--keep-state	Keep BuildKit state	v
a	1	0
@	buildx stop
a	1	0
@	buildx uninstall
@	buildx use
o	--default	Set builder as default for current context	v
o	--global	Builder persists context changes	v
a	1	0
@	buildx version
@	plugin
s	create	Create a plugin from a rootfs and configuration. Plugin data directory must contain config.json…
s	disable	Disable a plugin
s	enable	Enable a plugin
s	inspect	Display detailed information on one or more plugins
s	install	Install a plugin
s	ls	List plugins
s	push	Push a plugin to a registry
s	rm	Remove one or more plugins
s	set	Change settings for a plugin
s	upgrade	Upgrade an existing plugin
@	plugin create
o	--compress	Compress the context using gzip	
a	2	0
#	plugin create	2
t	filepaths
@	plugin disable
o	-f|--force	Force the disable of an active plugin	
a	1	0
#	plugin disable	1
d
@	plugin enable
o	--timeout	HTTP client timeout (in seconds) (default 30)	v
a	1	0
#	plugin enable	1
d
@	plugin inspect
o	-f|--format	Format the output using the given Go template	v
a	1	1
#	plugin inspect	1
d
@	plugin install
o	--alias	Local name for plugin	v
o	--disable	Do not enable the plugin on install	
o	--disable-content-trust	Skip image verification (default true)	
o	--grant-all-permissions	Grant all permissions necessary to run the plugin	
a	2	1
@	plugin ls
o	-f|--filter	Provide filter values (e.g. 'enabled=true')	v
o	--format	Pretty-print plugins using a Go template	v
o	--no-trunc	Don't truncate output	
o	-q|--quiet	Only display plugin IDs	
@	plugin push
o	--disable-content-trust	Skip image signing (default true)	
a	1	0
@	plugin rm
o	-f|--force	Force the removal of an active plugin	
a	1	1
#	plugin rm	1
d
@	plugin set
a	2	1
#	plugin set	1
d
@	plugin upgrade
o	--disable-content-trust	Skip image verification (default true)	
o	--grant-all-permissions	Grant all permissions necessary to run the plugin	
o	--skip-remote-check	Do not check if specified remote plugin matches existing plugin image	
a	2	0
#	plugin upgrade	1
d
@	secret
s	create	Create a secret from a file or STDIN as content
s	inspect	Display detailed information on one or more secrets
s	ls	List secrets
s	rm	Remove one or more secrets
@	secret create
o	-d|--driver	Secret driver	v
o	-l|--label	Secret labels	v
o	--template-driver	Template driver	v
a	2	0
#	secret create	2
t	filepaths
@	secret inspect
o	-f|--format	Format the output using the given Go template	v
o	--pretty	Print the information in a human friendly format	
a	1	1
#	secret inspect	1
d
@	secret ls
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print secrets using a Go template	v
o	-q|--quiet	Only display IDs	
@	secret rm
a	1	1
#	secret rm	1
d
@	service
s	create	Create a new service
s	inspect	Display detailed information on one or more services
s	logs	Fetch the logs of a service or task
s	ls	List services
s	ps	List the tasks of one or more services
s	rm	Remove one or more services
s	rollback	Revert changes to a service's configuration
s	scale	Scale one or multiple replicated services
s	update	Update a service
@	service create
o	--cap-add	Add Linux capabilities	v
o	--cap-drop	Drop Linux capabilities	v
o	--config	Specify configurations to expose to the service	v
o	--constraint	Placement constraints	v
o	--container-label	Container labels	v
o	--credential-spec	Credential spec for managed service account (Windows only)	v
o	-d|--detach	Exit immediately instead of waiting for the service to converge	
o	--dns	Set custom DNS servers	v
o	--dns-option	Set DNS options	v
o	--dns-search	Set custom DNS search domains	v
o	--endpoint-mode	Endpoint mode (vip or dnsrr) (default "vip")	v
o	--entrypoint	Overwrite the default ENTRYPOINT of the image	v
o	-e|--env	Set environment variables	v
o	--env-file	Read in a file of environment variables	v
o	--generic-resource	User defined resources	v
o	--group	Set one or more supplementary user groups for the container	v
o	--health-cmd	Command to run to check health	v
o	--health-interval	Time between running the check (ms|s|m|h)	v
o	--health-retries	Consecutive failures needed to report unhealthy	v
o	--health-start-period	Start period for the container to initialize before counting retries towards unstable (ms|s|m|h)	v
o	--health-timeout	Maximum time to allow one check to run (ms|s|m|h)	v
o	--host	Set one or more custom host-to-IP mappings (host:ip)	v
o	--hostname	Container hostname	v
o	--init	Use an init inside each service container to forward signals and reap processes	
o	--isolation	Service container isolation mode	v
o	-l|--label	Service labels	v
o	--limit-cpu	Limit CPUs	v
o	--limit-memory	Limit Memory	v
o	--limit-pids	Limit maximum number of processes (default 0 = unlimited)	v
o	--log-driver	Logging driver for service	v
o	--log-opt	Logging driver options	v
o	--max-concurrent	Number of job tasks to run concurrently (default equal to --replicas)	v
o	--mode	Service mode (replicated, global, replicated-job, or global-job) (default "replicated")	v
o	--mount	Attach a filesystem mount to the service	v
o	--name	Service name	v
o	--network	Network attachments	v
o	--no-healthcheck	Disable any container-specified HEALTHCHECK	
o	--no-resolve-image	Do not query the registry to resolve image digest and supported platforms	
o	--placement-pref	Add a placement preference	v
o	-p|--publish	Publish a port as a node port	v
o	-q|--quiet	Suppress progress output	
o	--read-only	Mount the container's root filesystem as read only	
o	--replicas	Number of tasks	v
o	--replicas-max-per-node	Maximum number of tasks per node (default 0 = unlimited)	v
o	--reserve-cpu	Reserve CPUs	v
o	--reserve-memory	Reserve Memory	v
o	--restart-condition	Restart when condition is met ("none"|"on-failure"|"any") (default "any")	v
o	--restart-delay	Delay between restart attempts (ns|us|ms|s|m|h) (default 5s)	v
o	--restart-max-attempts	Maximum number of restarts before giving up	v
o	--restart-window	Window used to evaluate the restart policy (ns|us|ms|s|m|h)	v
o	--rollback-delay	Delay between task rollbacks (ns|us|ms|s|m|h) (default 0s)	v
o	--rollback-failure-action	Action on rollback failure ("pause"|"continue") (default "pause")	v
o	--rollback-max-failure-ratio	Failure rate to tolerate during a rollback (default 0)	v
o	--rollback-monitor	Duration after each task rollback to monitor for failure (ns|us|ms|s|m|h) (default 5s)	v
o	--rollback-order	Rollback order ("start-first"|"stop-first") (default "stop-first")	v
o	--rollback-parallelism	Maximum number of tasks rolled back simultaneously (0 to roll back all at once) (default 1)	v
o	--secret	Specify secrets to expose to the service	v
o	--stop-grace-period	Time to wait before force killing a container (ns|us|ms|s|m|h) (default 10s)	v
o	--stop-signal	Signal to stop the container	v
o	--sysctl	Sysctl options	v
o	-t|--tty	Allocate a pseudo-TTY	
o	--ulimit	Ulimit options (default [])	v
o	--update-delay	Delay between updates (ns|us|ms|s|m|h) (default 0s)	v
o	--update-failure-action	Action on update failure ("pause"|"continue"|"rollback") (default "pause")	v
o	--update-max-failure-ratio	Failure rate to tolerate during an update (default 0)	v
o	--update-monitor	Duration after each task update to monitor for failure (ns|us|ms|s|m|h) (default 5s)	v
o	--update-order	Update order ("start-first"|"stop-first") (default "stop-first")	v
o	--update-parallelism	Maximum number of tasks updated simultaneously (0 to update all at once) (default 1)	v
o	-u|--user	Username or UID (format: <name|uid>[:<group|gid>])	v
o	--with-registry-auth	Send registry authentication details to swarm agents	
o	-w|--workdir	Working directory inside the container	v
a	2	0
=	service create	--mode
v	replicated	
v	global	
v	replicated-job	
v	global-job	
#	service create	1
d
@	service inspect
o	-f|--format	Format the output using the given Go template	v
o	--pretty	Print the information in a human friendly format	
a	1	1
#	service inspect	1
d
@	service logs
o	--details	Show extra details provided to logs	
o	-f|--follow	Follow log output	
o	--no-resolve	Do not map IDs to Names in output	
o	--no-task-ids	Do not include task IDs in output	
o	--no-trunc	Do not truncate output	
o	--raw	Do not neatly format logs	
o	--since	Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)	v
o	-n|--tail	Number of lines to show from the end of the logs (default "all")	v
o	-t|--timestamps	Show timestamps	
a	1	0
#	service logs	1
d
@	service ls
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print services using a Go template	v
o	-q|--quiet	Only display IDs	
@	service ps
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print tasks using a Go template	v
o	--no-resolve	Do not map IDs to Names	
o	--no-trunc	Do not truncate output	
o	-q|--quiet	Only display task IDs	
a	1	1
#	service ps	1
d
@	service rm
a	1	1
#	service rm	1
d
@	service rollback
o	-d|--detach	Exit immediately instead of waiting for the service to converge	
o	-q|--quiet	Suppress progress output	
a	1	0
#	service rollback	1
d
@	service scale
o	-d|--detach	Exit immediately instead of waiting for the service to converge	
a	1	1
#	service scale	1
d
@	service update
o	--args	Service command args	v
o	--cap-add	Add Linux capabilities	v
o	--cap-drop	Drop Linux capabilities	v
o	--config-add	Add or update a config file on a service	v
o	--config-rm	Remove a configuration file	v
o	--constraint-add	Add or update a placement constraint	v
o	--constraint-rm	Remove a constraint	v
o	--container-label-add	Add or update a container label	v
o	--container-label-rm	Remove a container label by its key	v
o	--credential-spec	Credential spec for managed service account (Windows only)	v
o	-d|--detach	Exit immediately instead of waiting for the service to converge	
o	--dns-add	Add or update a custom DNS server	v
o	--dns-option-add	Add or update a DNS option	v
o	--dns-option-rm	Remove a DNS option	v
o	--dns-rm	Remove a custom DNS server	v
o	--dns-search-add	Add or update a custom DNS search domain	v
o	--dns-search-rm	Remove a DNS search domain	v
o	--endpoint-mode	Endpoint mode (vip or dnsrr)	v
o	--entrypoint	Overwrite the default ENTRYPOINT of the image	v
o	--env-add	Add or update an environment variable	v
o	--env-rm	Remove an environment variable	v
o	--force	Force update even if no changes require it	
o	--generic-resource-add	Add a Generic resource	v
o	--generic-resource-rm	Remove a Generic resource	v
o	--group-add	Add an additional supplementary user group to the container	v
o	--group-rm	Remove a previously added supplementary user group from the container	v
o	--health-cmd	Command to run to check health	v
o	--health-interval	Time between running the check (ms|s|m|h)	v
o	--health-retries	Consecutive failures needed to report unhealthy	v
o	--health-start-period	Start period for the container to initialize before counting retries towards unstable (ms|s|m|h)	v
o	--health-timeout	Maximum time to allow one check to run (ms|s|m|h)	v
o	--host-add	Add a custom host-to-IP mapping (host:ip)	v
o	--host-rm	Remove a custom host-to-IP mapping (host:ip)	v
o	--hostname	Container hostname	v
o	--image	Service image tag	v
o	--init	Use an init inside each service container to forward signals and reap processes	
o	--isolation	Service container isolation mode	v
o	--label-add	Add or update a service label	v
o	--label-rm	Remove a label by its key	v
o	--limit-cpu	Limit CPUs	v
o	--limit-memory	Limit Memory	v
o	--limit-pids	Limit maximum number of processes (default 0 = unlimited)	v
o	--log-driver	Logging driver for service	v
o	--log-opt	Logging driver options	v
o	--max-concurrent	Number of job tasks to run concurrently (default equal to --replicas)	v
o	--mount-add	Add or update a mount on a service	v
o	--mount-rm	Remove a mount by its target path	v
o	--network-add	Add a network	v
o	--network-rm	Remove a network	v
o	--no-healthcheck	Disable any container-specified HEALTHCHECK	
o	--no-resolve-image	Do not query the registry to resolve image digest and supported platforms	
o	--placement-pref-add	Add a placement preference	v
o	--placement-pref-rm	Remove a placement preference	v
o	--publish-add	Add or update a published port	v
o	--publish-rm	Remove a published port by its target port	v
o	-q|--quiet	Suppress progress output	
o	--read-only	Mount the container's root filesystem as read only	
o	--replicas	Number of tasks	v
o	--replicas-max-per-node	Maximum number of tasks per node (default 0 = unlimited)	v
o	--reserve-cpu	Reserve CPUs	v
o	--reserve-memory	Reserve Memory	v
o	--restart-condition	Restart when condition is met ("none"|"on-failure"|"any")	v
o	--restart-delay	Delay between restart attempts (ns|us|ms|s|m|h)	v
o	--restart-max-attempts	Maximum number of restarts before giving up	v
o	--restart-window	Window used to evaluate the restart policy (ns|us|ms|s|m|h)	v
o	--rollback	Rollback to previous specification	
o	--rollback-delay	Delay between task rollbacks (ns|us|ms|s|m|h)	v
o	--rollback-failure-action	Action on rollback failure ("pause"|"continue")	v
o	--rollback-max-failure-ratio	Failure rate to tolerate during a rollback	v
o	--rollback-monitor	Duration after each task rollback to monitor for failure (ns|us|ms|s|m|h)	v
o	--rollback-order	Rollback order ("start-first"|"stop-first")	v
o	--rollback-parallelism	Maximum number of tasks rolled back simultaneously (0 to roll back all at once)	v
o	--secret-add	Add or update a secret on a service	v
o	--secret-rm	Remove a secret	v
o	--stop-grace-period	Time to wait before force killing a container (ns|us|ms|s|m|h)	v
o	--stop-signal	Signal to stop the container	v
o	--sysctl-add	Add or update a Sysctl option	v
o	--sysctl-rm	Remove a Sysctl option	v
o	-t|--tty	Allocate a pseudo-TTY	
o	--ulimit-add	Add or update a ulimit option (default [])	v
o	--ulimit-rm	Remove a ulimit option	v
o	--update-delay	Delay between updates (ns|us|ms|s|m|h)	v
o	--update-failure-action	Action on update failure ("pause"|"continue"|"rollback")	v
o	--update-max-failure-ratio	Failure rate to tolerate during an update	v
o	--update-monitor	Duration after each task update to monitor for failure (ns|us|ms|s|m|h)	v
o	--update-order	Update order ("start-first"|"stop-first")	v
o	--update-parallelism	Maximum number of tasks updated simultaneously (0 to update all at once)	v
o	-u|--user	Username or UID (format: <name|uid>[:<group|gid>])	v
o	--with-registry-auth	Send registry authentication details to swarm agents	
o	-w|--workdir	Working directory inside the container	v
a	1	0
#	service update	1
d
@	stack
s	deploy	Deploy a new stack or update an existing stack
s	ls	List stacks
s	ps	List the tasks in the stack
s	rm	Remove one or more stacks
s	services	List the services in the stack
@	stack deploy
o	-c|--compose-file	Path to a Compose file, or "-" to read from stdin	v
o	--orchestrator	Orchestrator to use (swarm|kubernetes|all)	v
o	--prune	Prune services that are no longer referenced	
o	--resolve-image	Query the registry to resolve image digest and supported platforms ("always"|"changed"|"never")…	v
o	--with-registry-auth	Send registry authentication details to Swarm agents	
a	1	0
=	stack deploy	-c
t	filepaths
@	stack ls
o	--format	Pretty-print stacks using a Go template	v
o	--orchestrator	Orchestrator to use (swarm|kubernetes|all)	v
@	stack ps
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print tasks using a Go template	v
o	--no-resolve	Do not map IDs to Names	
o	--no-trunc	Do not truncate output	
o	--orchestrator	Orchestrator to use (swarm|kubernetes|all)	v
o	-q|--quiet	Only display task IDs	
a	1	0
#	stack ps	1
d
@	stack rm
o	--orchestrator	Orchestrator to use (swarm|kubernetes|all)	v
a	1	1
#	stack rm	1
d
@	stack services
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Pretty-print services using a Go template	v
o	--orchestrator	Orchestrator to use (swarm|kubernetes|all)	v
o	-q|--quiet	Only display IDs	
a	1	0
#	stack services	1
d
@	swarm
s	ca	Display and rotate the root CA
s	init	Initialize a swarm
s	join	Join a swarm as a node and/or manager
s	join-token	Manage join tokens
s	leave	Leave the swarm
s	unlock	Unlock swarm
s	unlock-key	Manage the unlock key
s	update	Update the swarm
@	swarm ca
o	--ca-cert	Path to the PEM-formatted root CA certificate to use for the new cluster	v
o	--ca-key	Path to the PEM-formatted root CA key to use for the new cluster	v
o	--cert-expiry	Validity period for node certificates (ns|us|ms|s|m|h) (default 2160h0m0s)	v
o	-d|--detach	Exit immediately instead of waiting for the root rotation to converge	
o	--external-ca	Specifications of one or more certificate signing endpoints	v
o	-q|--quiet	Suppress progress output	
o	--rotate	Rotate the swarm CA - if no certificate or key are provided, new ones will be generated	
=	swarm ca	--ca-cert
t	filepaths
=	swarm ca	--ca-key
t	filepaths
@	swarm init
o	--advertise-addr	Advertised address (format: <ip|interface>[:port])	v
o	--autolock	Enable manager autolocking (requiring an unlock key to start a stopped manager)	
o	--availability	Availability of the node ("active"|"pause"|"drain") (default "active")	v
o	--cert-expiry	Validity period for node certificates (ns|us|ms|s|m|h) (default 2160h0m0s)	v
o	--data-path-addr	Address or interface to use for data path traffic (format: <ip|interface>)	v
o	--data-path-port	Port number to use for data path traffic (1024 - 49151). If no value is set or is set to 0, the…	v
o	--default-addr-pool	Default address pool in CIDR format (default [])	v
o	--default-addr-pool-mask-length	Default address pool subnet mask length (default 24)	v
o	--dispatcher-heartbeat	Dispatcher heartbeat period (ns|us|ms|s|m|h) (default 5s)	v
o	--external-ca	Specifications of one or more certificate signing endpoints	v
o	--force-new-cluster	Force create a new cluster from current state	
o	--listen-addr	Listen address (format: <ip|interface>[:port]) (default 0.0.0.0:2377)	v
o	--max-snapshots	Number of additional Raft snapshots to retain	v
o	--snapshot-interval	Number of log entries between Raft snapshots (default 10000)	v
o	--task-history-limit	Task history retention limit (default 5)	v
@	swarm join
o	--advertise-addr	Advertised address (format: <ip|interface>[:port])	v
o	--availability	Availability of the node ("active"|"pause"|"drain") (default "active")	v
o	--data-path-addr	Address or interface to use for data path traffic (format: <ip|interface>)	v
o	--listen-addr	Listen address (format: <ip|interface>[:port]) (default 0.0.0.0:2377)	v
o	--token	Token for entry into the swarm	v
a	1	0
@	swarm join-token
o	-q|--quiet	Only display token	
o	--rotate	Rotate join token	
a	1	0
#	swarm join-token	1
v	worker	
v	manager	
@	swarm leave
o	-f|--force	Force this node to leave the swarm, ignoring warnings	
@	swarm unlock
@	swarm unlock-key
o	-q|--quiet	Only display token	
o	--rotate	Rotate unlock key	
@	swarm update
o	--autolock	Change manager autolocking setting (true|false)	v
o	--cert-expiry	Validity period for node certificates (ns|us|ms|s|m|h) (default 2160h0m0s)	v
o	--dispatcher-heartbeat	Dispatcher heartbeat period (ns|us|ms|s|m|h) (default 5s)	v
o	--external-ca	Specifications of one or more certificate signing endpoints	v
o	--max-snapshots	Number of additional Raft snapshots to retain	v
o	--snapshot-interval	Number of log entries between Raft snapshots (default 10000)	v
o	--task-history-limit	Task history retention limit (default 5)	v
=	swarm update	--autolock
v	true	
v	false	
@	system
s	prune	Remove unused data
s	df	Show docker disk usage
s	events	Get real time events from the server
s	info	Display system-wide information
@	system prune
o	-a|--all	Remove all unused images not just dangling ones	
o	--filter	Provide filter values (e.g. 'label=<key>=<value')	v
o	-f|--force	Do not prompt for confirmation	
o	--volumes	Prune volumes	
@	system df
o	--format	Pretty-print images using a Go template	v
o	-v|--verbose	Show detailed information on space usage	
@	system events
o	-f|--filter	Filter output based on conditions provided	v
o	--format	Format the output using the given Go template	v
o	--since	Show all events created since timestamp	v
o	--until	Stream events until this timestamp	v
@	system info
o	-f|--format	Format the output using the given Go template	v
@	trust
s	inspect	Return low-level information about keys and signatures
s	revoke	Remove trust for an image
s	sign	Sign an image
@	trust inspect
o	--pretty	Print the information in a human friendly format	
a	1	1
@	trust revoke
o	-y|--yes	Do not prompt for confirmation	
a	1	0
#	trust revoke	1
d
@	trust sign
o	--local	Sign a locally tagged image	
a	1	0
#	trust sign	1
d
@	volume
s	create	Create a volume
s	inspect	Display detailed information on one or more volumes
s	ls	List volumes
s	prune	Remove all unused local volumes
s	rm	Remove one or more volumes
@	volume create
o	-d|--driver	Specify volume driver name (default "local")	v
o	--label	Set metadata for a volume	v
o	-o|--opt	Set driver specific options (default map[])	v
a	1	0
@	volume inspect
o	-f|--format	Format the output using the given Go template	v
a	1	1
#	volume inspect	1
d
@	volume ls
o	-f|--filter	Provide filter values (e.g. 'dangling=true')	v
o	--format	Pretty-print volumes using a Go template	v
o	-q|--quiet	Only display volume names	
@	volume prune
o	--filter	Provide filter values (e.g. 'label=<label>')	v
o	-f|--force	Do not prompt for confirmation	
@	volume rm
o	-f|--force	Force the removal of one or more volumes	
a	1	1
#	volume rm	1
d
@	compose
