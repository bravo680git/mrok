@	
s	edit|alter	Alter topics, partitions
s	attach	Run kafkactl pod in kubernetes and attach to it
s	clone	Clone topics, consumerGroups
s	completion	Generate shell auto-completion file
s	config	Show and edit configurations
s	consume	Consume messages from a topic
s	create	Create topics, consumerGroups, acls
s	delete	Delete topics, consumerGroups, consumer-group-offset, acls
s	describe	Describe topics, consumerGroups, brokers
s	list|get	Get info about topics, consumerGroups, acls, brokers
s	produce	Produce messages to a topic
s	reset	Reset consumerGroupsOffset
s	version	Print the version of kafkactl
s	help	Help about any command
o	--config-file|-C	Config file. one of: [$HOME/.config/kafkactl $HOME/.kafkactl $SNAP_REAL_HOME/.config/kafkactl…	vp
o	--verbose|-V	Verbose output	p
o	--help|-h	Display help	p
=		--config-file
t	filepaths
@	edit
s	partition	Alter a partition
s	topic	Alter a topic
@	edit partition
o	--replicas|-r	Set replicas for a partition	v
o	--validate-only|-v	Validate only	
@	edit topic
o	--config|-c	Configs in format `key=value`	v
o	--partitions|-p	Number of partitions	v
o	--replication-factor|-r	Replication factor	v
o	--validate-only|-v	Validate only	
@	attach
@	clone
s	cg|consumer-group	Clone existing consumerGroup with all offsets
s	topic	Clone existing topic (number of partitions, replication factor, config entries) to new one
@	clone cg
@	clone topic
@	completion
@	config
s	currentContext|current-context	Show current context
s	getContexts|get-contexts	List configured contexts
s	useContext|use-context	Switch active context
s	view	Show contents of config file
@	config currentContext
@	config getContexts
o	--output|-o	Output format. One of: compact	v
@	config useContext
@	config view
@	consume
o	--exit|-e	Stop consuming when latest offset is reached	
o	--from-beginning|-b	Set offset for consumer to the oldest offset	
o	--group|-g	Consumer group to join	v
o	--key-encoding	Key encoding (auto-detected by default). One of: none|hex|base64	v
o	--key-proto-type	Key protobuf message type	v
o	--max-messages	Stop consuming after n messages have been read	v
o	--offset	Offsets in format `partition=offset (for partitions not specified, other parameters apply)`	v
o	--output|-o	Output format. One of: json|yaml	v
o	--partitions|-p	Partitions to consume. The default is to consume from all partitions	v
o	--print-headers	Print message headers	
o	--print-keys|-k	Print message keys	
o	--print-schema|-a	Print details about avro schema used for decoding	
o	--print-timestamps|-t	Print message timestamps	
o	--proto-file	Additional protobuf description file for searching message description	v
o	--proto-import-path	Additional path to search files listed in proto 'import' directive	v
o	--protoset-file	Additional compiled protobuf description file for searching message description	v
o	--separator|-s	Separator to split key and value	v
o	--tail	Show only the last n messages on the topic	v
o	--value-encoding	Value encoding (auto-detected by default). One of: none|hex|base64	v
o	--value-proto-type	Value protobuf message type	v
=	consume	--proto-file
t	filepaths
=	consume	--proto-import-path
t	folders
=	consume	--protoset-file
t	filepaths
@	create
s	acl|access-control-list	Create an acl
s	cg|consumer-group	Create a consumerGroup
s	topic	Create a topic
@	create acl
o	--allow|-a	Acl of permissionType 'allow' (choose this or 'deny')	
o	--cluster|-c	Create acl for the cluster	
o	--deny|-d	Acl of permissionType 'deny' (choose this or 'allow')	
o	--group|-g	Create acl for a consumer group	v
o	--host	Hosts to allow	v
o	--operation|-o	Operations of acl	v
o	--pattern	Pattern type. one of (match, prefixed, literal)	v
o	--principal|-p	Principal to be authenticated	v
o	--topic|-t	Create acl for a topic	v
o	--validate-only|-v	Validate only	
@	create cg
o	--newest	Set the offset to newest offset (for all partitions or the specified partition)	
o	--offset	Set offset to this value. offset with value -1 is ignored	v
o	--oldest	Set the offset to oldest offset (for all partitions or the specified partition)	
o	--partition|-p	Partition to create group for. -1 stands for all partitions	v
o	--topic|-t	One or more topics to create group for	v
@	create topic
o	--config|-c	Configs in format `key=value`	v
o	--partitions|-p	Number of partitions	v
o	--replication-factor|-r	Replication factor	v
o	--validate-only|-v	Validate only	
@	delete
s	acl|access-control-list	Delete an acl
s	consumer-groups|consumer-group	Delete a consumer-group
s	cgo|offset|consumer-group-offset	Delete a consumer-group-offset
s	topic	Delete a topic
@	delete acl
o	--allow|-a	Acl of permissionType 'allow'	
o	--cluster|-c	Delete acl for the cluster	
o	--deny|-d	Acl of permissionType 'deny'	
o	--groups|-g	Delete acl for a consumer group	
o	--operation|-o	Operation of acl	v
o	--pattern	Pattern type. one of (any, match, prefixed, literal)	v
o	--topics|-t	Delete acl for a topic	
o	--validate-only|-v	Validate only	
@	delete consumer-groups
@	delete cgo
o	--partition|-p	Delete offset for this partition. -1 stands for all partitions	v
o	--topic|-t	Delete offset for this topic	v
@	delete topic
@	describe
s	broker	Describe a broker
s	cg|consumer-group	Describe a consumerGroup
s	topic	Describe a topic
@	describe broker
o	--output|-o	Output format. One of: json|yaml|wide	v
@	describe cg
o	--only-with-lag|-l	Show only partitions that have a lag	
o	--output|-o	Output format. One of: json|yaml|wide	v
o	--print-members|-m	Print group members	
o	--print-topics|-T	Print topic details	
o	--topic|-t	Show group details for given topic only	v
@	describe topic
o	--output|-o	Output format. One of: json|yaml|wide	v
o	--print-configs|-c	Print configs	
o	--skip-empty|-s	Show only partitions that have a messages	
@	list
s	acl|access-control-list	List available acls
s	brokers	List brokers
s	cg|consumer-groups	List available consumerGroups
s	topics	List available topics
@	list acl
o	--allow|-a	Acl of permissionType 'allow'	
o	--cluster|-c	List acl for the cluster	
o	--deny|-d	Acl of permissionType 'deny'	
o	--groups|-g	List acl for consumer groups	
o	--operation	Operation of acl	v
o	--output|-o	Output format. One of: json|yaml	v
o	--pattern	Pattern type. one of (any, match, prefixed, literal)	v
o	--topics|-t	List acl for topics	
@	list brokers
o	--output|-o	Output format. One of: json|yaml|compact	v
@	list cg
o	--output|-o	Output format. One of: json|yaml|wide|compact	v
o	--topic|-t	Show groups for given topic only	v
@	list topics
o	--output|-o	Output format. One of: json|yaml|wide|compact	v
@	produce
o	--file|-f	File to read input from	v
o	--header|-H	Headers in format `key:value`	v
o	--key|-k	Key to use for all messages	v
o	--key-encoding	Key encoding (none by default). One of: none|hex|base64	v
o	--key-proto-type	Key protobuf message type	v
o	--key-schema-version|-K	Avro schema version that should be used for key serialization (default is latest)	v
o	--lineSeparator|-L	Separator to split multiple messages from stdin or file	v
o	--max-message-bytes	The maximum permitted size of a message (defaults to 1000000)	v
o	--null-value	Produce a null value (can be used instead of providing a value with --value)	
o	--partition|-p	Partition to produce to	v
o	--partitioner|-P	The partitioning scheme to use. Can be `murmur2`, `hash`, `hash-ref` `manual`, or `random`…	v
o	--proto-file	Additional protobuf description file for searching message description	v
o	--proto-import-path	Additional path to search files listed in proto 'import' directive	v
o	--protoset-file	Additional compiled protobuf description file for searching message description	v
o	--rate|-r	Amount of messages per second to produce on the topic	v
o	--required-acks	Required acks. One of `NoResponse`, `WaitForLocal`, `WaitForAll`. (default is WaitForLocal)	v
o	--separator|-S	Separator to split key and value from stdin or file	v
o	--silent|-s	Do not write to standard output	
o	--value|-v	Value to produce	v
o	--value-encoding	Value encoding (none by default). One of: none|hex|base64	v
o	--value-proto-type	Value protobuf message type	v
o	--value-schema-version|-i	Avro schema version that should be used for value serialization (default is latest)	v
=	produce	--proto-file
t	filepaths
=	produce	--proto-import-path
t	folders
=	produce	--protoset-file
t	filepaths
@	reset
s	cgo|offset|consumer-group-offset	Reset a consumer group offset
@	reset cgo
o	--all-topics	Do the operation for all topics in the consumer group	
o	--execute|-e	Execute the reset (as default only the results are displayed for validation)	
o	--newest	Set the offset to newest offset (for all partitions or the specified partition)	
o	--offset	Set offset to this value. offset with value -1 is ignored	v
o	--oldest	Set the offset to oldest offset (for all partitions or the specified partition)	
o	--output|-o	Output format. One of: json|yaml	v
o	--partition|-p	Partition to apply the offset. -1 stands for all partitions	v
o	--topic|-t	One ore more topics to change offset for	v
@	version
@	help
s	edit|alter	Alter topics, partitions
s	attach	Run kafkactl pod in kubernetes and attach to it
s	clone	Clone topics, consumerGroups
s	completion	Generate shell auto-completion file
s	config	Show and edit configurations
s	consume	Consume messages from a topic
s	create	Create topics, consumerGroups, acls
s	delete	Delete topics, consumerGroups, consumer-group-offset, acls
s	describe	Describe topics, consumerGroups, brokers
s	list|get	Get info about topics, consumerGroups, acls, brokers
s	produce	Produce messages to a topic
s	reset	Reset consumerGroupsOffset
s	version	Print the version of kafkactl
@	help edit
s	partition	Alter a partition
s	topic	Alter a topic
@	help edit partition
@	help edit topic
@	help attach
@	help clone
s	cg|consumer-group	Clone existing consumerGroup with all offsets
s	topic	Clone existing topic (number of partitions, replication factor, config entries) to new one
@	help clone cg
@	help clone topic
@	help completion
@	help config
s	currentContext|current-context	Show current context
s	getContexts|get-contexts	List configured contexts
s	useContext|use-context	Switch active context
s	view	Show contents of config file
@	help config currentContext
@	help config getContexts
@	help config useContext
@	help config view
@	help consume
@	help create
s	acl|access-control-list	Create an acl
s	cg|consumer-group	Create a consumerGroup
s	topic	Create a topic
@	help create acl
@	help create cg
@	help create topic
@	help delete
s	acl|access-control-list	Delete an acl
s	consumer-groups|consumer-group	Delete a consumer-group
s	cgo|offset|consumer-group-offset	Delete a consumer-group-offset
s	topic	Delete a topic
@	help delete acl
@	help delete consumer-groups
@	help delete cgo
@	help delete topic
@	help describe
s	broker	Describe a broker
s	cg|consumer-group	Describe a consumerGroup
s	topic	Describe a topic
@	help describe broker
@	help describe cg
@	help describe topic
@	help list
s	acl|access-control-list	List available acls
s	brokers	List brokers
s	cg|consumer-groups	List available consumerGroups
s	topics	List available topics
@	help list acl
@	help list brokers
@	help list cg
@	help list topics
@	help produce
@	help reset
s	cgo|offset|consumer-group-offset	Reset a consumer group offset
@	help reset cgo
@	help version
