@	
s	start	Starts a local Kubernetes cluster
s	status	Gets the status of a local Kubernetes cluster
s	stop	Stops a running local Kubernetes cluster
s	delete	Deletes a local Kubernetes cluster
s	unpause	Unpause Kubernetes
s	docker-env	Configure environment to use minikube's Docker daemon
s	podman-env	Configure environment to use minikube's Podman service
s	cache	Add, delete, or push a local image into minikube
s	image	Manage images
s	addons	Enable or disable a minikube addon
s	config	Modify persistent configuration values
s	profile	Get or list the current profiles (clusters)
s	update-context	Update kubeconfig in case of an IP or port change
s	service	Returns a URL to connect to a service
s	tunnel	Connect to LoadBalancer services
s	mount	Mounts the specified directory into minikube
s	ssh	Log into the minikube environment (for debugging)
s	kubectl	Run a kubectl binary matching the cluster version
s	node	Add, remove, or list additional nodes
s	cp	Copy the specified file into minikube
s	ssh-key	Retrieve the ssh identity key path of the specified node
s	ssh-host	Retrieve the ssh host key of the specified node
s	ip	Retrieves the IP address of the specified node
s	logs	Returns logs to debug a local Kubernetes cluster
s	update-check	Print current and latest version number
s	version	Print the version of minikube
s	options	Add, remove, or list additional nodes
s	completion	Generate command completion for a shell
@	start
o	--addons	Enable addons. see `minikube addons list` for a list of valid addon names	
o	--apiserver-ips	A set of apiserver IP Addresses which are used in the generated certificate for kubernetes	
o	--apiserver-name	The authoritative apiserver hostname for apiserver certificates and connectivity	
o	--apiserver-names	A set of apiserver names which are used in the generated certificate for kubernetes	
o	--apiserver-port	The apiserver listening port	
o	--auto-update-drivers	If set, automatically updates drivers to the latest version	v
o	--base-image	The base image to use for docker/podman drivers. Intended for local development	
o	--cache-images	If true, cache docker images for the current bootstrapper and load them into the machine	
o	--cert-expiration	Duration until minikube certificate expiration	
o	--cni	CNI plug-in to use	v
o	--container-runtime	The container runtime to be used	v
o	--cpus	Number of CPUs allocated to Kubernetes	v
o	--cri-socket	The cri socket path to be used	
o	--delete-on-failure	If set, delete the current cluster if start fails and try again	v
o	--disable-driver-mounts	Disables the filesystem mounts provided by the hypervisors	
o	--disk-size	Disk size allocated to the minikube VM	
o	--dns-domain	The cluster dns domain name used in the Kubernetes cluster	
o	--dns-proxy	Enable proxy for NAT DNS requests	
o	--docker-env	Environment variables to pass to the Docker daemon. (format: key=value)	
o	--docker-opt	Specify arbitrary flags to pass to the Docker daemon. (format: key=value)	
o	--download-only	If true, only download and cache files for later use - don't install or start anything	
o	--driver	Choose driver	v
o	--dry-run	Dry-run mode. Validates configuration, but does not mutate system state	
o	--embed-certs	If true, will embed the certs in kubeconfig	v
o	--extra-config	A set of key=value pairs that describe configuration that may be passed to different components	
o	--extra-disks	Number of extra disks created and attached to the minikube VM	
o	--feature-gates	A set of key=value pairs that describe feature gates for alpha/experimental features	
o	--force	Force minikube to perform possibly dangerous operations	
o	--force-systemd	If set, force the container runtime to use systemd as cgroup manager	v
o	--host-dns-resolver	Enable host resolver for NAT DNS requests	
o	--host-only-cidr	The CIDR to be used for the minikube VM	
o	--host-only-nic-type	NIC Type used for host only network	v
o	--hyperkit-vpnkit-sock	Location of the VPNKit socket used for networking	
o	--hyperkit-vsock-ports	List of guest VSock ports that should be exposed as sockets on the host	
o	--hyperv-external-adapter	External Adapter on which external switch will be created if no external switch is found	
o	--hyperv-use-external-switch	Whether to use external switch over Default Switch if virtual switch not explicitly specified	
o	--hyperv-virtual-switch	The hyperv virtual switch name. Defaults to first found	
o	--image-mirror-country	Country code of the image mirror to be used	
o	--image-repository	Alternative image repository to pull docker images from	
o	--insecure-registry	Insecure Docker registries to pass to the Docker daemon	
o	--install-addons	If set, install addons. Defaults to true	v
o	--interactive	Allow user prompts for more information	
o	--iso-url	Locations to fetch the minikube ISO from	
o	--keep-context	This will keep the existing kubectl context and will create a minikube context	
o	--kubernetes-version	The Kubernetes version that the minikube VM will use	
o	--kvm-gpu	Enable experimental NVIDIA GPU support in minikube	
o	--kvm-hidden	Hide the hypervisor signature from the guest in minikube	
o	--kvm-network	The KVM default network name	
o	--kvm-numa-count	Simulate numa node count in minikube, supported numa node count range is 1-8	v
o	--kvm-qemu-uri	The KVM QEMU connection URI	
o	--listen-address	IP Address to use to expose ports	
o	--memory	Amount of RAM to allocate to Kubernetes	
o	--mount	This will start the mount daemon and automatically mount files into minikube	
o	--mount-string	The argument to pass the minikube mount command on start	
o	--namespace	The named space to activate after start	
o	--nat-nic-type	NIC Type used for nat network	
o	--native-ssh	Use native Golang SSH client	
o	--network	Network to run minikube with	
o	--network-plugin	Kubelet network plug-in to use	
o	--nfs-share	Local folders to share with Guest via NFS mounts	
o	--nfs-shares-root	Where to root the NFS Shares	
o	--no-kubernetes	If set, minikube VM/container will start without starting or configuring Kubernetes	
o	--no-vtx-check	Disable checking for the availability of hardware virtualization before the vm is started	
o	--nodes|-n	The number of nodes to spin up	
o	--output|-o	Format to print stdout in	v
o	--ports	List of ports that should be exposed	
o	--preload	If set, download tarball of preloaded images if available to improve start time	v
o	--registry-mirror	Registry mirrors to pass to the Docker daemon	
o	--service-cluster-ip-range	The CIDR to be used for service cluster IPs	
o	--ssh-ip-address	IP address	
o	--ssh-key	SSH key	
o	--ssh-port	SSH port	
o	--ssh-user	SSH user	
o	--trace	Send trace events	v
o	--uuid	Provide VM UUID to restore MAC address	
o	--vm	Filter to use only VM Drivers	
o	--wait	Comma separated list of Kubernetes components to verify and wait for after starting a cluster	
o	--wait-timeout	Max time to wait per Kubernetes or host to be healthy	
=	start	--auto-update-drivers
v	true	
v	false	
=	start	--cni
v	auto	
v	bridge	
v	cilium	
v	flannel	
v	kindnet	
=	start	--container-runtime
v	docker	
v	cri-o	
v	containerd	
=	start	--cpus
v	max	
=	start	--delete-on-failure
v	true	
v	false	
=	start	--driver
v	virtualbox	
v	parallels	
v	vmwarefusion	
v	hyperkit	
v	vmware	
v	docker	
v	podman	
=	start	--embed-certs
v	true	
v	false	
=	start	--force-systemd
v	true	
v	false	
=	start	--host-only-nic-type
v	Am79C970A	
v	Am79C973	
v	82540EM	
v	82543GC	
v	82545EM	
v	virtio	
=	start	--install-addons
v	true	
v	false	
=	start	--kvm-numa-count
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
v	8	
=	start	--output
v	json	
v	text	
=	start	--preload
v	true	
v	false	
=	start	--trace
v	gcp	
@	status
o	--format|-f	Go template format string for the status output	
o	--layout|-l	Output layout	
o	--node|-n	The node to check status for	
o	--output|-o	Format to print stdout in	v
o	--watch|-w	Continuously listing/getting the status with optional interval duration	
=	status	--output
v	json	
v	text	
@	stop
o	--all	Set flag to stop all profiles (clusters)	
o	--cancel-scheduled	Output layout	
o	--keep-context-active	The node to check status for	
o	--output|-o	Format to print stdout in	v
o	--schedule	Set flag to stop cluster after a set amount of time	
=	stop	--output
v	json	
v	text	
@	delete
o	--all	Set flag to delete all profiles	
o	--purge	Set this flag to delete the '.minikube' folder from your user directory	
@	unpause
o	--all-namespaces|-A	If set, unpause all namespaces	
o	--namespaces|-n	Namespaces to unpause	
o	--output|-o	Format to print stdout in	v
=	unpause	--output
v	json	
v	text	
@	docker-env
o	--no-proxy|-A	If set, unpause all namespaces	
o	--output|-o	Format to print stdout in	v
o	--shell	Force environment to be configured for a specified shell	
o	--ssh-host	Use SSH connection instead of HTTPS (port 2376)	
o	--unset|-u	Unset variables instead of setting them	
=	docker-env	--output
v	json	
v	text	
@	podman-env
o	--shell	Force environment to be configured for a specified shell	
o	--unset|-u	Unset variables instead of setting them	
@	cache
s	add	Add an image to local cache
s	delete	Delete an image from the local cache
s	list	List all available images from the local cache
s	reload	Reload cached images
@	cache add
@	cache delete
@	cache list
@	cache reload
@	image
s	build	Build a container image in minikube
s	load	Load a image into minikube
s	ls	List images
s	pull	Pull images
s	push	Push images
s	rm	Remove one or more images
s	save	Save a image from minikube
s	tag	Tag images
@	image build
@	image load
@	image ls
@	image pull
@	image push
@	image rm
@	image save
@	image tag
@	addons
s	configure	Configures the addon w/ADDON_NAME within minikube
s	disable	Disables the addon w/ADDON_NAME within minikube
s	enable	Enables the addon w/ADDON_NAME within minikube
s	images	List image names the addon w/ADDON_NAME used
s	list	Lists all available minikube addons as well as their current statuses
s	open	Opens the addon w/ADDON_NAME within minikube
@	addons configure
@	addons disable
@	addons enable
@	addons images
@	addons list
@	addons open
@	config
s	defaults	Lists all valid default values for PROPERTY_NAME
s	get	Gets the value of PROPERTY_NAME from the minikube config file
s	set	Sets an individual value in a minikube config file
s	unset	Unsets an individual value in a minikube config file
s	view	Display values currently set in the minikube config file
@	config defaults
@	config get
@	config set
@	config unset
@	config view
@	profile
s	list	Lists all minikube profiles
@	profile list
@	update-context
@	service
s	list	Lists the URLs for the services in your local cluster
o	--https	Open the service URL with https instead of http	
o	--interval	The initial time interval for each check that wait performs in seconds	
o	--namespace	The service namespace	
o	--url	Display the Kubernetes service URL in the CLI instead of opening it in the default browser	
o	--wait	Amount of time to wait for a service in seconds	
@	service list
o	--namespace|-n	The services namespace	
@	tunnel
o	--cleanup|-c	Call with cleanup=true to remove old tunnels	
@	mount
o	--9p-version	Specify the 9p version that the mount should use	
o	--gid	Default group id used for the mount	
o	--ip	Specify the ip that the mount should be setup on	
o	--kill	Kill the mount process spawned by minikube start	
o	--mode	File permissions used for the mount	
o	--msize	The number of bytes to use for 9p packet payload	
o	--options	Additional mount options, such as cache=fscache	
o	--port	Specify the port that the mount should be setup on	
o	--type	Specify the mount filesystem type (supported types: 9p)	
o	--uid	Default user id used for the mount	
@	ssh
o	--native-ssh	Use native Golang SSH client	
o	--node|-n	The node to ssh into	
@	kubectl
o	--ssh	Use SSH for running kubernetes client on the node	
@	node
s	add	Adds a node to the given cluster
s	delete	Deletes a node from a cluster
s	list	List nodes
s	start	Starts a node
s	stop	Stops a node in a cluster
@	node add
@	node delete
@	node list
@	node start
@	node stop
@	cp
a	1	0
@	ssh-key
o	--node|-n	The node to get ssh-key path	
@	ssh-host
o	--append-known	Add host key to SSH known_hosts file	
o	--node|-n	The node to ssh into	
@	ip
o	--node|-n	The node to get IP	
@	logs
o	--file	If present, writes to the provided file instead of stdout	
o	--follow|-f	Show only the most recent journal entries	
o	--length|-n	Number of lines back to go within the log	
o	--node	The node to get logs from. Defaults to the primary control plane	
o	--problems	Show only log entries which point to known problems	
@	update-check
@	version
o	--components	List versions of all components included with minikube	
o	--output|-o	Format to print stdout in	v
o	--short	Print just the version number	v
=	version	--output
v	json	
v	text	
=	version	--short
v	true	
v	false	
@	options
@	completion
s	bash	Bash completion
s	fish	Fish completion
s	zsh	Zsh completion
@	completion bash
@	completion fish
@	completion zsh
