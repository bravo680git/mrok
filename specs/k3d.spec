@	
s	cluster	Manage k3s clusters
s	completion	Generate shell completion scripts
s	config	Manage k3d config
s	image	Manage k3d images
s	kubeconfig	Manage k3d kubeconfig
s	node	Manage k3d nodes
s	registry|registries|reg	Manage registry/registries
s	version	Show k3d and default k3s version
o	-h|--help	Help for k3d	p
o	--verbose	Verbose output	p
o	--trace	Trace output	p
o	--version	Print version information	
o	--timestamps	Print timestamp in log output	p
@	cluster
s	create	Create a new k3s cluster
s	delete|del|rm	Delete a cluster
s	edit|update	Edit a cluster
s	list|ls|get	List clusters
s	start	Start a cluster
s	stop	Stop a cluster
@	cluster create
o	-a|--agents	Number of agents to create	v
o	--agents-memory	Memory limit imposed on the agents nodes	v
o	--api-port	Specify the Kubernetes API server port exposed on the LoadBalancer	v
o	-c|--config	Path of a config file to use	v
o	-e|--env	Add environment variables to nodes	v
o	--gpus	GPU devices to add to the cluster node containers	v
o	-h|--help	Help for create	
o	--host-alias	Add ip:host[,host,...] mappings	v
o	--host-pid-mode	Enable host pid mode of server(s) and agent(s)	
o	-i|--image	Specify k3s image that you want to use for the nodes	v
o	--k3s-arg	Additional args passed to k3s command	v
o	--k3s-node-label	Add label to k3s node	v
o	--kubeconfig-switch-context	Directly switch the default kubeconfig's current-context to the new cluster's context (requires…	
o	--kubeconfig-update-default	Directly update the default kubeconfig with the new cluster's context (default true)	
o	--lb-config-override	Use dotted YAML path syntax to override nginx loadbalancer settings	v
o	--network	Specify the docker network to use	v
o	--no-image-volume	Don't create a volume for the container's root filesystem	
o	--no-lb	Don't create a loadbalancer for the cluster	
o	--no-rollback	Don't rollback changes if cluster creation failed	
o	-p|--port	Map ports from the node containers (via the serverlb) to the host	v
o	--registry-config	Specify path to an extra registries.yaml file	v
o	--registry-create	Create a k3d-managed registry and connect it to the cluster (Format: NAME[:HOST][:HOSTPORT] -…	v
o	--registry-use	Connect to one or more k3d-managed registries running locally	v
o	--runtime-label	Add label to container runtime (Format: KEY[=VALUE][@NODEFILTER[;NODEFILTER...]] - Example: `k3d…	
o	-s|--servers	Specify how many servers you want to create	v
o	--servers-memory	Memory limit imposed on the server nodes [From docker]	v
o	--subnet	[Experimental: IPAM] Define a subnet for the newly created container network	v
o	--timeout	Rollback changes if cluster couldn't be created in specified duration	v
o	--token	Specify a cluster token. By default, we generate one	v
o	-v|--volume	Mount volumes into the nodes	v
o	--wait	Wait for the server(s) to be ready before returning	
a	1	0
@	cluster delete
o	-a|--all	Delete all clusters	
o	-c|--config	Path of a config file to use	v
a	1	0
#	cluster delete	1
d
@	cluster edit
o	--port-add	Map ports from the node containers	
a	1	0
#	cluster edit	1
d
@	cluster list
o	--no-headers	Don't print headers	
o	-o|--output	Output format	v
o	--token	Print k3s cluster token	
a	1	0
=	cluster list	-o
v	json	
v	yaml	
#	cluster list	1
d
@	cluster start
o	a|--all	Start all clusters	
o	--timeout	Maximum waiting time for '--wait' before canceling/returning	v
o	--wait	Wait for the server(s) (and loadbalancer) to be ready before returning	
a	1	0
#	cluster start	1
d
@	cluster stop
o	-a|--all	Stop all clusters	
a	1	0
#	cluster stop	1
d
@	completion
a	1	0
#	completion	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	powershell	Powershell
@	config
s	init|create	Create a new config file
s	migrate|update	Migrate a config file to the latest version
@	config init
o	-f|--force	Force overwrite of target file	
o	-o|--output	Write a default k3d config (default "k3d-default.yaml")	
@	config migrate
@	image
s	import|load	Import image(s) from docker into k3d cluster(s)
@	image import
o	-c|--cluster	Cluster to import image(s) into	v
o	-k|--keep-tarball	Do not delete the tarball containing the saved images from the shared volume	
o	-t|--keep-tools	Do not delete the tools node after import	
o	-m|--mode	Import mode	v
a	1	0
=	image import	-c
d
=	image import	-m
v	auto	
v	direct	
v	tools	
#	image import	1
d
@	kubeconfig
s	get|print|show	
s	merge|write	Write/Merge kubeconfig(s) from cluster(s) into new or existing kubeconfig/file
@	kubeconfig get
o	-a|--all		
a	1	0
#	kubeconfig get	1
d
@	kubeconfig merge
o	-a|--all		
o	-d|--kubeconfig-merge-default	Merge into the default kubeconfig ($KUBECONFIG or /Users/balli/.kube/config)	
o	-s|--kubeconfig-switch-context	Switch to new context (default true)	
o	-o|--output	Define output [ - | FILE ] (default from $KUBECONFIG or /Users/balli/.kube/config	v
o	--overwrite	[Careful!] Overwrite existing file, ignoring its contents	
o	-u|--update	Update conflicting fields in existing kubeconfig (default true)	
a	1	0
#	kubeconfig merge	1
d
@	node
s	create	Create a new node
s	delete	Delete a node
s	edit|update	[EXPERIMENTAL] Edit node(s)
s	list|ls|get	List nodes
s	start	Start a node
s	stop	Stop a node
@	node create
o	-c|--cluster	Cluster URL or k3d cluster name to connect to. (default "k3s-default")	v
o	-i|--image	Node image to use	v
o	--k3s-arg	Additional k3s arguments	v
o	--k3s-node-label	Specify k3s node labels in format	v
o	--memory	Memory limit for the node container	v
o	-n|--network	Add node to (another) runtime network	v
o	--replicas	Number of replicas to create	v
o	--role	Node role	v
o	--runtime-label	Specify runtime labels in format	v
o	--timeout	Maximum waiting time for '--wait' before canceling/returning	v
o	-t|--token	Override cluster token	v
o	--wait	Wait for the node(s) to be ready before returning	
a	1	0
=	node create	-c
d
=	node create	--replicas
v	1	
v	2	
v	3	
v	4	
v	5	
=	node create	--role
v	agent	
v	server	
@	node delete
o	-a|--all	Delete all existing nodes	
o	-r|--registry	Also delete registries	
a	1	0
#	node delete	1
d
@	node edit
o	--port-add	Map ports from the node container to the host	v
a	1	0
#	node edit	1
d
@	node list
o	--no-headers	Don't print headers (default print headers)	
o	-o|--output	Output format	v
=	node list	-o
v	json	
v	yaml	
@	node start
a	1	0
#	node start	1
d
@	node stop
a	1	0
#	node stop	1
d
@	registry
s	create	Create a new registry
s	delete|del|rm	Delete registry/registries
s	list|ls|get	List registries
@	registry create
o	--default-network	Specify the network connected to the registry (default "bridge")	
o	-i|--image	Specify image used for the registry (default "docker.io/library/registry:2")	v
o	--no-help	Disable the help text (How-To use the registry)	
o	-p|--port	Select which port the registry should be listening on your machine (localhost) (Format…	v
o	--proxy-password	Specify the password of the proxied remote registry	v
o	--proxy-remote-url	Specify the url of the proxied remote registry	v
o	--proxy-username	Specify the username of the proxied remote registry	v
o	-v|--volume	Mount volumes into the registry node (Format: [SOURCE:]DEST	v
a	1	0
@	registry delete
o	-a|--all		
a	1	0
#	registry delete	1
d
@	registry list
o	--no-headers	Don't print headers (default print headers)	
o	-o|--output	Output format	v
a	1	0
=	registry list	-o
v	json	
v	yaml	
#	registry list	1
d
@	version
