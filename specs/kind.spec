@	
s	Build	Build one of [node-image]
s	create	Creates a cluster
s	completion	Generates shell completion scripts
s	delete	Deletes one or more clusters
s	export	Exports a cluster's kubeconfig
s	get	Gets one of [clusters, nodes, kubeconfig]
s	load	Loads images into node from an archive or image on host
s	version	Prints the kind CLI version
o	-h|--help	Help for kind	p
o	-q|--quiet	Silence all stderr output	p
o	-v|--verbosity	Info log verbosity, higher value produces more output	vp
@	Build
s	node-image	Builds a node image
@	Build node-image
o	--arch	Architecture to build for, defaults to the host architecture	v
o	--base-image	Base image to use for the node image	v
o	--image	Name:tag of the resulting image to be built	v
o	--kube-root	Path to the Kubernetes source directory	v
o	--type	Type of node image to build	v
@	create
s	cluster	Creates a cluster
@	create cluster
o	--config	Path to a kind config file	
o	--image	Node docker image to use for booting the cluster	
o	--kubeconfig	Sets kubeconfig path instead of $KUBECONFIG or $HOME/.kube/config	
o	--name	Cluster name	
o	--retain	Retain nodes for debugging when cluster creation fails	
o	--wait	Wait for control-plane node to be ready	
@	completion
s	bash	Output shell completions for bash
s	fish	Output shell completions for fish
s	zsh	Output shell completions for zsh
@	completion bash
@	completion fish
@	completion zsh
@	delete
s	cluster	Delete Cluster
s	clusters	Delete Clusters
@	delete cluster
o	--name	Cluster name	v
=	delete cluster	--name
d
@	delete clusters
o	-A|--all	Delete all clusters	
o	--kubeconfig	Sets kubeconfig path instead of $KUBECONFIG or $HOME/.kube/config	
@	export
s	kubeconfig	Exports a cluster's kubeconfig
s	logs	Exports logs to a tempdir or [output-dir] if specified
@	export kubeconfig
o	--name	Cluster name	
o	--internal	Use internal address instead of externalt	
o	--kubeconfig	Sets kubeconfig path instead of $KUBECONFIG or $HOME/.kube/config	
@	export logs
o	--name	Cluster name	v
=	export logs	--name
d
@	get
s	clusters	Lists existing kind clusters by their name
s	kubeconfig	Prints cluster kubeconfig
s	nodes	Lists existing kind nodes by their name
@	get clusters
@	get kubeconfig
o	--name	Cluster name	v
o	--internal	Use internal address instead of external	
=	get kubeconfig	--name
d
@	get nodes
o	-A|--all	List all nodes	
o	--name	Cluster name	v
=	get nodes	--name
d
@	load
s	docker-image	Loads docker images from host into all or specified nodes by name
s	image-archive	Loads docker images from archive into all or specified nodes by name
@	load docker-image
o	--name	Cluster name	v
o	--nodes	Comma separated list of nodes to load images into	v
=	load docker-image	--name
d
=	load docker-image	--nodes
d
@	load image-archive
o	--name	Cluster name	v
o	--nodes	Comma separated list of nodes to load images into	v
=	load image-archive	--name
d
=	load image-archive	--nodes
d
@	version
