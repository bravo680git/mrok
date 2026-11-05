@	
s	compute	Manage Compute resources like instances and images
s	network	Manage Virtual Cloud Network resources
s	db	Manage Database resources
s	os	Object Storage commands
s	iam	Manage Identity and Access Management resources
s	kms	Manage Key Management resources
s	monitoring	Manage Monitoring and Alerts
s	budget	Manage Budgets and Cost Controls
o	--help|-h	Show help for oci	
o	--profile|-p	The profile to load from the config file	v
o	--config-file	The path to the config file	v
o	--region	The region to make calls against	v
o	--output	The output format	v
o	--debug	Turn on debug logging	
o	--auth	The type of auth to use	v
o	--key-file	The path to the private key file	v
o	--wait-for-state	Wait until resource reaches a given state	v
o	--wait-interval-seconds	Check interval seconds for --wait-for-state	v
o	--max-wait-seconds	Maximum time to wait	v
o	--raw-output	Output raw response from OCI API	
o	--output-format	The output format for commands	v
o	--query	JMESPath query to filter the output	
=		--config-file
t	filepaths
=		--region
v	us-ashburn-1	
v	us-phoenix-1	
v	us-chicago-1	
v	ca-montreal-1	
v	ca-toronto-1	
v	sa-saopaulo-1	
v	sa-vinhedo-1	
v	sa-santiago-1	
v	eu-frankfurt-1	
v	eu-amsterdam-1	
v	eu-zurich-1	
v	eu-madrid-1	
v	uk-london-1	
v	uk-cardiff-1	
v	ap-tokyo-1	
v	ap-osaka-1	
v	ap-seoul-1	
v	ap-sydney-1	
v	ap-melbourne-1	
v	ap-hyderabad-1	
v	ap-mumbai-1	
v	me-dubai-1	
=		--output
v	json	
v	table	
v	text	
=		--auth
v	api_key	
v	instance_principal	
v	resource_principal	
v	security_token	
v	raw_token	
=		--key-file
t	filepaths
=		--wait-for-state
v	ACCEPTED	
v	AVAILABLE	
v	RUNNING	
v	PROVISIONING	
v	STOPPED	
v	TERMINATED	
v	FAILED	
=		--output-format
v	json	
v	table	
v	text	
@	compute
s	instance	Manage Compute instances
s	image	Manage Custom Images
@	compute instance
s	launch	Launch a new compute instance
s	terminate	Terminate a compute instance
s	start	Start a stopped instance
s	stop	Stop a running instance
@	compute instance launch
o	--availability-domain	The availability domain of the instance	
o	--compartment-id	The OCID of the compartment	
o	--shape	The shape of the instance	
@	compute instance terminate
o	--instance-id	The OCID of the instance	
@	compute instance start
o	--instance-id	The OCID of the instance	
@	compute instance stop
o	--instance-id	The OCID of the instance	
@	compute image
s	list	List available compute images
@	compute image list
o	--compartment-id	The OCID of the compartment	
@	network
s	vcn	Manage Virtual Cloud Networks
@	network vcn
s	create	Create a new VCN
@	network vcn create
o	--compartment-id	The OCID of the compartment	
o	--cidr-block	The CIDR block of the VCN	
@	db
s	autonomous-database	Manage Autonomous Databases
@	db autonomous-database
s	create	Create an Autonomous Database
@	db autonomous-database create
o	--compartment-id	The OCID of the compartment	
o	--db-name	The database name	
o	--cpu-core-count	Number of CPU cores	
@	os
s	bucket	Manage buckets
@	os bucket
s	create	Create a new bucket
@	os bucket create
o	--compartment-id	The OCID of the compartment	
o	--name	The name of the bucket	
@	iam
s	user	Manage users
s	policy	Manage IAM policies
s	group	Manage IAM groups
s	compartment	Manage compartments
@	iam user
s	create	Create a new user
@	iam user create
o	--name	Name of the user	
o	--description	Description for the user	
@	iam policy
s	create	Create a new policy
@	iam policy create
o	--name	Name of the policy	
o	--statements	Policy statements	
@	iam group
s	create	Create a new group
@	iam group create
o	--name	The name of the group	
o	--description	Description for the group	
@	iam compartment
s	create	Create a new compartment
@	iam compartment create
o	--name	The name of the compartment	
o	--description	Description for the compartment	
@	kms
s	key	Manage encryption keys
@	kms key
s	create	Create a new key
@	kms key create
o	--compartment-id	The OCID of the compartment	
o	--display-name	Display name of the key	
o	--key-shape	Shape of the key	v
=	kms key create	--key-shape
v	AES	
v	RSA	
v	ECDSA	
@	monitoring
s	alarm	Manage monitoring alarms
@	monitoring alarm
s	create	Create a new alarm
@	monitoring alarm create
o	--display-name	Display name of the alarm	
o	--metric-compartment-id	Compartment OCID containing the metric	
@	budget
s	create	Create a new budget
@	budget create
o	--compartment-id	The OCID of the compartment	
o	--amount	The amount for the budget	
o	--reset-period	The reset period for the budget	v
=	budget create	--reset-period
v	MONTHLY	
v	YEARLY	
