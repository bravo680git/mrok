@	
s	attach	Attach to a running container
s	build	Build an image using instructions from Containerfiles
s	commit	Create new image based on the changed container
s	cp	Copy files/folders between a container and the local filesystem
s	create	Create but do not start a container
s	diff	Display the changes to the object's file system
s	events	Show podman system events
s	exec	Run a process in a running container
s	export	Export container's filesystem contents as a tar archive
s	history	Show history of a specified image
s	images	List images in local storage
s	import	Import a tarball to create a filesystem image
s	info	Display podman system information
s	inspect	Display the configuration of object denoted by ID
s	kill	Kill one or more running containers with a specific signal
s	load	Load image(s) from a tar archive
s	login	Log in to a container registry
s	logout	Log out of a container registry
s	logs	Fetch the logs of one or more containers
s	pause	Pause all processes within one or more containers
s	port	List port mappings or a specific mapping for the container
s	ps	List containers
s	pull	Pull an image from a registry
s	push	Push an image to a specified destination
s	rename	Rename an existing container
s	restart	Restart one or more containers
s	rm	Remove one or more containers
s	rmi	Remove one or more images from local storage
s	run	Run a command in a new container
s	save	Save image(s) to an archive
s	search	Search registry for image
s	start	Start one or more containers
s	stats	Display a live stream of container resource usage statistics
s	stop	Stop one or more containers
s	tag	Add an additional name to a local image
s	top	Display the running processes of a container
s	unpause	Unpause the processes in one or more containers
s	update	Update an existing container
s	version	Display the Podman version information
s	wait	Block on one or more containers
s	container	Manage containers
s	image	Manage images
s	network	Manage networks
s	secret	Manage secrets
s	system	Manage podman
s	volume	Manage volumes
s	compose	Run compose workloads via an external provider such as docker-compose or podman-compose
s	generate	Generate structured data based on containers, pods or volumes
s	healthcheck	Manage health checks on containers
s	help	Help about any command
s	init	Initialize one or more containers
s	kube	Play containers, pods or volumes from a structured file
s	machine	Manage a virtual machine
s	manifest	Manipulate manifest lists and image indexes
s	pod	Manage pods
s	untag	Remove a name from a local image
o	--connection|-c	Connection to use for remote Podman service	
o	--help|-h	Help for podman	
o	--identity	Path to SSH identity file, (CONTAINER_SSHKEY)	
o	--log-level	Log messages above specified level (trace, debug, info, warn, warning, error, fatal, panic)…	
o	--out	Send output (stdout) from podman to a file	
o	--ssh	Define the ssh mode (default 'golang')	
o	--storage-opt	Used to pass an option to the storage driver	
o	--url	URL to access Podman service (CONTAINER_HOST)	
o	--version|-v	Version for podman	
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
@	container
s	attach	Attach to a running container
s	cp	Copy files/folders between a container and the local filesystem
s	create	Create but do not start a container
s	diff	Display the changes to the object's file system
s	exec	Run a process in a running container
s	export	Export container's filesystem contents as a tar archive
s	inspect	Return low-level information on Docker objects
s	kill	Kill one or more running containers with a specific signal
s	logs	Fetch the logs of one or more containers
s	ls	List containers
s	pause	Pause all processes within one or more containers
s	port	List port mappings or a specific mapping for the container
s	prune	Remove all stopped containers
s	rename	Rename an existing container
s	restart	Restart one or more containers
s	rm	Remove one or more containers
s	run	Run a command in a new container
s	start	Start one or more containers
s	stats	Display a live stream of container resource usage statistics
s	stop	Stop one or more containers
s	top	Display the running processes of a container
s	unpause	Unpause the processes in one or more containers
s	update	Update an existing container
s	wait	Block on one or more containers
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
@	image
s	build	Build an image using instructions from Containerfiles
s	history	Show history of a specified image
s	import	Import a tarball to create a filesystem image
s	inspect	Display detailed information on one or more images
s	load	Load image(s) from a tar archive
s	ls	List images in local storage
s	prune	Remove unused images
s	pull	Pull an image from a registry
s	push	Push an image to a specified destination
s	rm	Remove one or more images from local storage
s	save	Save image(s) to an archive
s	tag	Add an additional name to a local image
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
@	system
s	prune	Remove unused data
s	df	Show podman disk usage
s	events	Get real time events from the server
s	info	Display podman system information
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
@	generate
@	healthcheck
@	help
@	init
@	kube
@	machine
s	info	Display machine host info
s	init	Initialize a virtual machine
s	inspect	Inspect an existing machine
s	list	List machines
s	os	Manage a Podman virtual machine's OS
s	rm	Remove an existing machine
s	set	Set a virtual machine setting
s	ssh	SSH into an existing machine
s	start	Start an existing machine
s	stop	Stop an existing machine
@	machine info
@	machine init
@	machine inspect
@	machine list
@	machine os
@	machine rm
@	machine set
@	machine ssh
@	machine start
@	machine stop
@	manifest
@	pod
@	untag
