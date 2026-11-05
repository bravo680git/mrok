@	
s	api	Generate api related files
s	bug	Report a bug
s	completion	Generate the autocompletion script for the specified shell
s	docker	Generate Dockerfile
s	env	Check or edit goctl environment
s	kube	Generate kubernetes files
s	migrate	Migrate from tal-tech to zeromicro
s	model	Generate model code
s	quickstart	Quickly start a project
s	rpc	Generate rpc code
s	template	Template operation
s	upgrade	Upgrade goctl to latest version
s	help	Help about any command
o	--help|-h	Display help	p
@	api
s	dart	Generate dart files for provided api in api file
s	doc	Generate doc files
s	format	Format api files
s	go	Generate go files for provided api in yaml file
s	java	Generate java files for provided api in api file
s	kt	Generate kotlin code for provided api file
s	new	Fast create api service
s	plugin	Custom file generator
s	ts	Generate ts files for provided api in api file
s	validate	Validate api file
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--o	Output a sample api file	v
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
@	api dart
o	--api	The api file	v
o	--dir	The target dir	v
o	--hostname	Hostname of the server	v
o	--legacy	Legacy generator for flutter v1	
@	api doc
o	--dir	The target dir	v
o	--o	The output markdown directory	v
@	api format
o	--declare	Use to skip check api types already declare	
o	--dir	The format target dir	v
o	--iu	Ignore update	
o	--stdin	Use stdin to input api doc content, press "ctrl + d" to send EOF	
@	api go
o	--api	The api file	v
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--dir	The target dir	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--style	The file naming format, see [https://github.com/zeromicro/go-zero/blob/master/tools/goctl/config/re…	v
@	api java
o	--api	The api file	v
o	--dir	The target dir	v
@	api kt
o	--api	The api file	v
o	--dir	The target dir	v
o	--pkg	Define package name for kotlin file	v
@	api new
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--style	The file naming format, see [https://github.com/zeromicro/go-zero/blob/master/tools/goctl/config/re…	v
@	api plugin
o	--api	The api file	v
o	--dir	The target dir	v
o	--plugin|-p	The plugin file	v
o	--style	The file naming format, see [https://github.com/zeromicro/go-zero/tree/master/tools/goctl/config/re…	v
@	api ts
o	--api	The api file	v
o	--caller	The web api caller	v
o	--dir	The target dir	v
o	--unwrap	Unwrap the webapi caller for import	
o	--webapi	The web api file path	v
@	api validate
o	--api	Validate target api file	v
@	bug
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	completion bash
o	--no-descriptions	Disable completion descriptions	
@	completion fish
o	--no-descriptions	Disable completion descriptions	
@	completion powershell
o	--no-descriptions	Disable completion descriptions	
@	completion zsh
o	--no-descriptions	Disable completion descriptions	
@	docker
o	--base	The base image to build the docker image, default scratch	v
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--go	The directory that contains main function	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--port	The port to expose, default none	v
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--tz	The timezone of the container	v
o	--version	The goctl builder golang image version	v
@	env
s	check	Detect goctl env and dependency tools
s	install	Goctl env installation
o	--write|-w	Edit goctl environment	v
o	--force|-f	Silent installation of non-existent dependencies	p
o	--verbose|-v	Enable log output	p
@	env check
o	--install|-i	Install dependencies if not found	
@	env install
@	kube
s	deploy	Generate deployment yaml file
@	kube deploy
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--image	The docker image of deployment (required)	v
o	--limitCpu	The limit cpu to deploy	v
o	--limitMem	The limit memory to deploy	v
o	--maxReplicas	The max replicas to deploy	v
o	--minReplicas	The min replicas to deploy	v
o	--name	The name of deployment (required)	v
o	--namespace	The namespace of deployment (required)	v
o	--nodePort	The nodePort of the deployment to expose	v
o	--o	The output yaml file (required)	v
o	--port	The port of the deployment to listen on pod (required)	v
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--replicas	The number of replicas to deploy	v
o	--requestCpu	The request cpu to deploy	v
o	--requestMem	The request memory to deploy	v
o	--revisions	The number of revision history to limit	v
o	--secret	The secret to image pull from registry	v
o	--serviceAccount	The ServiceAccount for the deployment	v
@	migrate
o	--verbose|-v	Verbose enables extra logging	
o	--version	The target release version of github.com/zeromicro/go-zero to migrate	v
@	model
s	mongo	Generate mongo model
s	mysql	Generate mysql model
@	model mongo
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--cache|-c	Generate code with cache [optional]	
o	--dir|-d	The target dir	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--style	The file naming format, see [https://github.com/zeromicro/go-zero/tree/master/tools/goctl/config/re…	v
o	--type|-t	Specified model type name	v
@	model mysql
s	datasource	Generate model from datasource
s	ddl	Generate mysql model from ddl
s	pg	Generate postgresql model
@	model mysql datasource
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--cache|-c	Generate code with cache [optional]	
o	--dir|-d	The target dir	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--idea	For idea plugin [optional]	
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--style	The file naming format, see [https://github.com/zeromicro/go-zero/tree/master/tools/goctl/config/re…	v
o	--table|-t	The table or table globbing patterns in the database	v
o	--url	The data source of database,like "root:password@tcp(127.0.0.1:3306)/database"	v
@	model mysql ddl
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--cache|-c	Generate code with cache [optional]	
o	--database	The name of database [optional]	v
o	--dir|-d	The target dir	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--idea	For idea plugin [optional]	
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--src|-s	The path or path globbing patterns of the ddl	v
o	--style	The file naming format, see [https://github.com/zeromicro/go-zero/tree/master/tools/goctl/config/re…	v
@	model mysql pg
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--cache|-c	Generate code with cache [optional]	
o	--dir|-d	The target dir	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--idea	For idea plugin [optional]	
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--schema|-s	The table schema	v
o	--style	The file naming format, see [https://github.com/zeromicro/go-zero/tree/master/tools/goctl/config/re…	v
o	--table|-t	The table or table globbing patterns in the database	v
o	--url	The data source of database,like "root:password@tcp(127.0.0.1:3306)/database"	v
@	quickstart
o	--service-type|-t	Specify the service type, supported values: [mono, micro]	v
@	rpc
s	new	Generate rpc demo service
s	protoc	Generate grpc code
s	template	Generate proto template
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--o	Output a sample proto file	v
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
@	rpc new
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--idea	Whether the command execution environment is from idea plugin	
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--style	The file naming format, see [https://github.com/zeromicro/go-zero/tree/master/tools/goctl/config/re…	v
o	--verbose|-v	Enable log output	
@	rpc protoc
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--multiple|-m	Generated in multiple rpc service mode	
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
o	--style	The file naming format, see [https://github.com/zeromicro/go-zero/tree/master/tools/goctl/config/re…	v
o	--verbose|-v	Enable log output	
o	--zrpc_out	The zrpc output directory	v
@	rpc template
o	--branch	The branch of the remote repo, it does work with --remote	v
o	--home	The goctl home path of the template, --home and --remote cannot be set at the same time, if they…	v
o	--o	Output a sample proto file	v
o	--remote	The remote git repo of the template, --home and --remote cannot be set at the same time, if they…	v
@	template
s	clean	Clean the all cache templates
s	init	Initialize the all templates(force update)
s	revert	Revert the target template to the latest
s	update	Update template of the target category to the latest
@	template clean
o	--home	The goctl home path of the template	v
@	template init
o	--home	The goctl home path of the template	v
@	template revert
o	--category|-c	The category of template, enum [api,rpc,model,docker,kube]	v
o	--home	The goctl home path of the template	v
o	--name|-n	The target file name of template	v
@	template update
o	--category|-c	The category of template, enum [api,rpc,model,docker,kube]	v
o	--home	The goctl home path of the template	v
@	upgrade
@	help
s	api	Generate api related files
s	bug	Report a bug
s	completion	Generate the autocompletion script for the specified shell
s	docker	Generate Dockerfile
s	env	Check or edit goctl environment
s	kube	Generate kubernetes files
s	migrate	Migrate from tal-tech to zeromicro
s	model	Generate model code
s	quickstart	Quickly start a project
s	rpc	Generate rpc code
s	template	Template operation
s	upgrade	Upgrade goctl to latest version
@	help api
s	dart	Generate dart files for provided api in api file
s	doc	Generate doc files
s	format	Format api files
s	go	Generate go files for provided api in yaml file
s	java	Generate java files for provided api in api file
s	kt	Generate kotlin code for provided api file
s	new	Fast create api service
s	plugin	Custom file generator
s	ts	Generate ts files for provided api in api file
s	validate	Validate api file
@	help api dart
@	help api doc
@	help api format
@	help api go
@	help api java
@	help api kt
@	help api new
@	help api plugin
@	help api ts
@	help api validate
@	help bug
@	help completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh
@	help docker
@	help env
s	check	Detect goctl env and dependency tools
s	install	Goctl env installation
@	help env check
@	help env install
@	help kube
s	deploy	Generate deployment yaml file
@	help kube deploy
@	help migrate
@	help model
s	mongo	Generate mongo model
s	mysql	Generate mysql model
@	help model mongo
@	help model mysql
s	datasource	Generate model from datasource
s	ddl	Generate mysql model from ddl
s	pg	Generate postgresql model
@	help model mysql datasource
@	help model mysql ddl
@	help model mysql pg
@	help quickstart
@	help rpc
s	new	Generate rpc demo service
s	protoc	Generate grpc code
s	template	Generate proto template
@	help rpc new
@	help rpc protoc
@	help rpc template
@	help template
s	clean	Clean the all cache templates
s	init	Initialize the all templates(force update)
s	revert	Revert the target template to the latest
s	update	Update template of the target category to the latest
@	help template clean
@	help template init
@	help template revert
@	help template update
@	help upgrade
