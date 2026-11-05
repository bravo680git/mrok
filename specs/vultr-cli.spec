@	
s	account	Retrieve information about your account
s	apps|a	Display all available applications
s	backups	Display backups
s	bare-metal|bm	Bare-metal is used to access bare metal server commands
s	block-storage	Block storage commands
s	completion	Generate the autocompletion script for the specified shell
s	dns	Dns is used to access dns commands
s	firewall|fw	Firewall is used to access firewall commands
s	help	Help about any command
s	instance	Commands to interact with instances on vultr
s	iso	Iso is used to access iso commands
s	kubernetes|k	Kubernetes is used to access kubernetes commands
s	load-balancer|lb	Load balancer commands
s	network	Network interacts with network actions
s	object-storage	Object storage commands
s	os	Os is used to access os commands
s	plans|p	Get information about Vultr plans
s	regions	Get regions
s	reserved-ip|rip	Reserved-ip lets you interact with reserved-ip
s	script|ss	Startup script commands
s	snapshot|sn	Snapshot commands
s	ssh-key|ssh	Ssh-key commands
s	user|u	User commands
s	version	Display current version of Vultr-cli
@	account
@	apps
s	list|l	List applications
@	apps list
@	backups
s	get	Get backup
s	list|l	List backups
@	backups get
a	1	0
@	backups list
@	bare-metal
s	app|a	App is used to access bare metal server application commands
s	bandwidth|b	Get a bare metal server's bandwidth usage
s	create|c	Create a bare metal server
s	delete|destroy	Delete a bare metal server
s	get	Get a bare metal server by <bareMetalID>
s	halt|h	Halt a bare metal server
s	image|i	Image is used to access bare metal server image commands
s	ipv4	List the IPv4 information of a bare metal server
s	ipv6	List the IPv6 information of a bare metal server
s	list	List all bare metal servers
s	os	Os is used to access bare metal server operating system commands
s	reboot	Reboot a bare metal server. This is a hard reboot, which means that the server is powered off…
s	reinstall	Reinstall the operating system on a bare metal server
s	start	Start a bare metal server
s	user-data	User-data is used to access bare metal server user-data commands
s	vnc	Get a bare metal server's VNC url by <bareMetalID>
@	bare-metal app
s	change|c	Change a bare metal server's application
s	list	Available apps a bare metal server can change to
@	bare-metal app change
a	2	0
@	bare-metal app list
a	1	0
@	bare-metal bandwidth
a	1	0
@	bare-metal create
o	--os|-o	ID of the operating system that will be installed on the server	v
o	--persistent_pxe|-x	Enable persistent_pxe	v
o	--plan|-p	ID of the plan that the server will subscribe to	v
o	--region|-r	ID of the region where the server will be created	v
=	bare-metal create	--persistent_pxe
v	true	
v	false	
@	bare-metal delete
a	1	0
@	bare-metal get
a	1	0
@	bare-metal halt
a	1	0
@	bare-metal image
s	change	Change a bare metal server's image
s	list	Available images a bare metal server can change to
@	bare-metal image change
a	2	0
@	bare-metal image list
a	1	0
@	bare-metal ipv4
@	bare-metal ipv6
@	bare-metal list
@	bare-metal os
@	bare-metal reboot
@	bare-metal reinstall
@	bare-metal start
@	bare-metal user-data
@	bare-metal vnc
a	1	0
@	block-storage
s	attach	Attaches a block storage to an instance
s	create	Create a new block storage
s	delete	Delete a block storage
s	detach	Detaches a block storage from an instance
s	get	Retrieves a block storage
s	label	Sets a label for a block storage
s	list	Retrieves a list of active block storage
s	resize	Resize a block storage
@	block-storage attach
@	block-storage create
@	block-storage delete
@	block-storage detach
@	block-storage get
@	block-storage label
@	block-storage list
@	block-storage resize
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	completion bash
@	completion fish
@	completion powershell
@	completion zsh
@	dns
s	domain	Dns domain
s	record	Dns record
@	dns domain
@	dns record
@	firewall
s	group	Group is used to access firewall group commands
s	rule	Rule is used to access firewall rule commands
@	firewall group
@	firewall rule
@	help
s	account	Retrieve information about your account
s	apps	Display all available applications
s	backups	Display backups
s	bare-metal	Bare-metal is used to access bare metal server commands
s	block-storage	Block storage commands
s	completion	Generate the autocompletion script for the specified shell
s	dns	Dns is used to access dns commands
s	firewall	Firewall is used to access firewall commands
s	help	Help about any command
s	instance	Commands to interact with instances on vultr
s	iso	Iso is used to access iso commands
s	kubernetes	Kubernetes is used to access kubernetes commands
s	load-balancer	Load balancer commands
s	network	Network interacts with network actions
s	object-storage	Object storage commands
s	os	Os is used to access os commands
s	plans	Get information about Vultr plans
s	regions	Get regions
s	reserved-ip	Reserved-ip lets you interact with reserved-ip
s	script	Startup script commands
s	snapshot	Snapshot commands
s	ssh-key	Ssh-key commands
s	user	User commands
s	version	Display current version of Vultr-cli
@	help account
@	help apps
@	help backups
@	help bare-metal
@	help block-storage
@	help completion
@	help dns
@	help firewall
@	help help
@	help instance
@	help iso
@	help kubernetes
@	help load-balancer
@	help network
@	help object-storage
@	help os
@	help plans
@	help regions
@	help reserved-ip
@	help script
@	help snapshot
@	help ssh-key
@	help user
@	help version
@	instance
s	app	Update application for an instance
s	backup	List and create backup schedules for an instance
s	bandwidth	Bandwidth for instance
s	create	Create an instance
s	delete|destroy	Delete/destroy an instance
s	get	Get info about a specific instance
s	image	Update image for an instance
s	ipv4	List/create/delete ipv4 on instance
s	ipv6	Commands for ipv6 on instance
s	iso	Attach/detach ISOs to a given instance
s	label	Label an instance
s	list	List all available instances
s	os	Update operating system for an instance
s	plan	Update/list plans for an instance
s	reinstall	Reinstall an instance
s	restart	Restart an instance
s	restore	Restore instance from backup/snapshot
s	reverse-dns	Commands to handle reverse-dns on an instance
s	start	Starts an instance
s	stop	Stops an instance
s	tag	Add/modify tag on instance
s	update-firewall-group	Assign a firewall group to instance
s	user-data	Commands to handle userdata on an instance
@	instance app
@	instance backup
@	instance bandwidth
@	instance create
o	--os|-o	ID of the operating system that will be installed on the server	v
o	--persistent_pxe|-x	Enable persistent_pxe	v
o	--plan|-p	ID of the plan that the server will subscribe to	v
o	--region|-r	ID of the region where the server will be created	v
=	instance create	--persistent_pxe
v	true	
v	false	
@	instance delete
a	1	0
#	instance delete	1
d
@	instance get
a	1	0
#	instance get	1
d
@	instance image
@	instance ipv4
@	instance ipv6
@	instance iso
@	instance label
@	instance list
@	instance os
@	instance plan
@	instance reinstall
@	instance restart
@	instance restore
@	instance reverse-dns
@	instance start
@	instance stop
@	instance tag
@	instance update-firewall-group
@	instance user-data
@	iso
s	create	Create iso from url
s	delete	Delete a private iso
s	get	Get private ISO <isoID>
s	list	List all private ISOs available
s	public	List all public ISOs available
@	iso create
@	iso delete
@	iso get
a	1	0
@	iso list
@	iso public
@	kubernetes
s	config	Gets a kubernetes cluster's config
s	create	Create kubernetes cluster
s	delete	Delete a kubernetes cluster
s	delete-with-resources	Delete a kubernetes cluster and related resources
s	get	Retrieves a kubernetes cluster
s	list	List kubernetes clusters
s	node-pool	Node pools commands for a kubernetes cluster
s	update	Updates a kubernetes cluster
s	versions	Gets supported kubernetes versions
@	kubernetes config
@	kubernetes create
@	kubernetes delete
@	kubernetes delete-with-resources
@	kubernetes get
@	kubernetes list
@	kubernetes node-pool
@	kubernetes update
@	kubernetes versions
@	load-balancer
s	create	Create a load balancer
s	delete	Deletes a load balancer
s	firewall-rule	Get/list firewall rules for a load balancer
s	get	Retrieves a load balancer
s	list	Retrieves a list of active load balancers
s	rule	Create/delete/list forwarding rules for a load balancer
s	update	Updates a load balancer
@	load-balancer create
@	load-balancer delete
@	load-balancer firewall-rule
@	load-balancer get
@	load-balancer list
@	load-balancer rule
@	load-balancer update
@	network
s	create	Create a private network
s	delete	Delete a private network
s	get	Get a private network
s	list	List all private networks
@	network create
@	network delete
@	network get
@	network list
@	object-storage
s	create	Create a new object storage subscription
s	delete	Deletes an object storage subscription
s	get	Retrieves a given object storage subscription
s	label	Change the label for object storage subscription
s	list	Retrieves a list of active object storage subscriptions
s	list-cluster	Retrieves a list of object storage clusters
s	s3key-regenerate	Regenerate the S3 API keys of an object storage subscription
@	object-storage create
@	object-storage delete
@	object-storage get
@	object-storage label
@	object-storage list
@	object-storage list-cluster
@	object-storage s3key-regenerate
@	os
s	list	List all available operating systems
@	os list
@	plans
s	list	List plans
@	plans list
@	regions
s	availability	List availability in region
s	list	List regions
@	regions availability
@	regions list
@	reserved-ip
s	attach	Attach a reservedIP to an instance
s	convert	Convert IP address to reservedIP
s	create	Create reservedIP
s	delete	Delete a reserved ip
s	detach	Detach a reservedIP to an instance
s	get	Get a reserved IP
s	list	List all reserved IPs
@	reserved-ip attach
@	reserved-ip convert
@	reserved-ip create
@	reserved-ip delete
@	reserved-ip detach
@	reserved-ip get
@	reserved-ip list
@	script
s	create	Create a startup script
s	delete	Delete a startup script
s	get	Displays the contents of specified script
s	list	List all startup scripts
s	update	Update startup script
@	script create
@	script delete
@	script get
@	script list
@	script update
@	snapshot
s	create	Create a snapshot
s	create-url	Create a snapshot from a URL
s	delete	Delete a snapshot
s	get	Get a snapshot
s	list	List all snapshots
@	snapshot create
@	snapshot create-url
@	snapshot delete
@	snapshot get
@	snapshot list
@	ssh-key
s	create	Create an SSH key
s	delete	Delete an SSH key
s	get	Get an SSH key
s	list	List all SSH keys
s	update	Update SSH key
@	ssh-key create
@	ssh-key delete
@	ssh-key get
@	ssh-key list
@	ssh-key update
@	user
s	create	Create a user
s	delete	Delete a user
s	get	Get a user
s	list	List all available users
s	update	Update User
@	user create
@	user delete
@	user get
@	user list
@	user update
@	version
