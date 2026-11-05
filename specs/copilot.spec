@	
s	init	Create a new ECS or App Runner application
s	docs	Open the copilot docs
s	app	Commands for applications. Applications are a collection of services and environments
s	env	Commands for environments. Environments are deployment stages shared between services
s	svc	Commands for services. Services are long-running ECS or App Runner services
s	job	Commands for jobs. Jobs are tasks that are triggered by events
s	task	Commands for tasks. One-off Amazon ECS tasks that terminate once their work is done
s	storage	Commands for working with storage and databases
s	secret	Commands for secrets. Secrets are sensitive information that you need in your application
s	version	Print the version number
s	completion	Output shell completion code
s	pipeline	Commands for pipelines. Continuous delivery pipelines to release services
s	deploy	Deploy a Copilot job or service
s	help	Help about any command
o	--help|-h	Help for command	
@	init
o	--app|-a	Name of the application	v
o	--deploy	Deploy your service or job to a "test" environment	
o	--dockerfile|-d	Path to the Dockerfile	v
o	--image|-i	The location of an existing Docker image	v
o	--name|-n	Name of the service or job	v
o	--port	The port on which your service listens	v
o	--retries	Optional. The number of times to try restarting the job on a failure	v
o	--schedule	The schedule on which to run this job. Accepts cron expressions of the format (M H DoM M DoW) and…	v
o	--tag	Optional. The container image tag	v
o	--timeout	Optional. The total execution time for the task, including retries. Accepts valid Go duration…	v
o	--type|-t	Type of job or svc to create	v
o	--help|-h	Help for command	
=	init	--type
v	Request-Driven Web Service	
v	Load Balanced Web Service	
v	Backend Service	
v	Worker Service	
v	Scheduled Job	
@	docs
o	--help|-h	Help for command	
@	app
s	init	Creates a new empty application
s	ls	Lists all the applications in your account
s	show	Shows info about an application
s	delete	Delete all resources associated with the application
s	upgrade	Upgrades the template of an application to the latest version
o	--help|-h	Help for command	
@	app init
o	--domain	Optional. Your existing custom domain name	v
o	--resource-tags	Optional. Labels with a key and value separated by commas. Allows you to categorize resources	v
o	--help|-h	Help for command	
@	app ls
o	--help|-h	Help for command	
@	app show
o	--json	Outputs in JSON format	
o	--name|-n	Name of the application	v
o	--help|-h	Help for command	
@	app delete
o	--name|-n	Name of the application	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
@	app upgrade
o	--name|-n	Name of the application	v
o	--help|-h	Help for command	
@	env
s	init	Creates a new environment in your application
s	ls	Lists all the environments in an application
s	delete	Deletes an environment from your application
s	show	Shows info about a deployed environment
o	--help|-h	Help for command	
@	env init
o	--app|-a	Name of the application	v
o	--aws-access-key-id	Optional. An AWS access key	v
o	--aws-secret-access-key	Optional. An AWS secret access key	v
o	--aws-session-token	Optional. An AWS session token for temporary credentials	v
o	--default-config	Optional. Skip prompting and use default environment configuration	
o	--import-private-subnets	Optional. Use existing private subnet IDs	v
o	--import-public-subnets	Optional. Use existing public subnet IDs	v
o	--import-vpc-id	Optional. Use an existing VPC ID	v
o	--name|-n	Name of the environment	v
o	--override-az-names	Optional. Availability Zone names. (default 2 random AZs)	v
o	--override-private-cidrs	Optional. CIDR to use for private subnets. (default 10.0.2.0/24,10.0.3.0/24)	v
o	--override-public-cidrs	Optional. CIDR to use for public subnets. (default 10.0.0.0/24,10.0.1.0/24)	v
o	--override-vpc-cidr	Optional. Global CIDR to use for VPC. (default 10.0.0.0/16)	v
o	--prod	If the environment contains production services	
o	--profile	Name of the profile	v
o	--region	Optional. An AWS region where the environment will be created	v
o	--help|-h	Help for command	
=	env init	--app
d
@	env ls
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--help|-h	Help for command	
=	env ls	--app
d
@	env delete
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	env delete	--app
d
@	env show
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the environment	v
o	--resources	Optional. Show the resources in your environment	
o	--help|-h	Help for command	
=	env show	--app
d
@	svc
s	init	Creates a new service in an application
s	ls	Lists all the services in an application
s	package	Prints the AWS CloudFormation template of a service
s	deploy	Deploys a service to an environment
s	delete	Deletes a service from an application
s	show	Shows info about a deployed service per environment
s	status	Shows status of a deployed service
s	logs	Displays logs of a deployed service
s	exec	Execute a command in a running container part of a service
s	pause	Pause running App Runner service
s	resume	Resumes a paused service
o	--help|-h	Help for command	
@	svc init
o	--app|-a	Name of the application	v
o	--dockerfile|-d	Path to the Dockerfile	v
o	--image|-i	The location of an existing Docker image	v
o	--name|-n	Name of the service	v
o	--no-subscribe	Optional. Turn off selection for adding subscriptions for worker services	
o	--port	The port on which your service listens	v
o	--subscribe-topics	Optional. SNS Topics to subscribe to from other services in your application. Must be of format…	v
o	--svc-type|-t	Type of service to create	v
o	--help|-h	Help for command	
=	svc init	--app
d
=	svc init	--svc-type
v	Request-Driven Web Service	
v	Load Balanced Web Service	
v	Backend Service	
v	Worker Service	
@	svc ls
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--local	Only show services in the workspace	
o	--help|-h	Help for command	
=	svc ls	--app
d
@	svc package
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--output-dir	Optional. Writes the stack template and template configuration to a directory	v
o	--tag	Optional. The container image tag	v
o	--help|-h	Help for command	
=	svc package	--app
d
@	svc deploy
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--force	Optional. Force a new service deployment using the existing image	
o	--name|-n	Name of the service	v
o	--resource-tags	Optional. Labels with a key and value separated by commas. Allows you to categorize resources	v
o	--tag	Optional. The container image tag	v
o	--help|-h	Help for command	
=	svc deploy	--app
d
@	svc delete
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	svc delete	--app
d
@	svc show
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the service	v
o	--resources	Optional. Show the resources in your service	
o	--help|-h	Help for command	
=	svc show	--app
d
@	svc status
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the service	v
o	--help|-h	Help for command	
=	svc status	--app
d
@	svc logs
o	--app|-a	Name of the application	v
o	--end-time	Optional. Only return logs before a specific date (RFC3339). Defaults to all logs	v
o	--name|-n	Name of the environment	v
o	--follow	Optional. Specifies if the logs should be streamed	
o	--json	Outputs in JSON format	
o	--limit	Optional. The maximum number of log events returned. Default is 10 unless any time filtering flags…	v
o	--log-group	Optional. Only return logs from specific log group	v
o	--name|-n	Name of the service	v
o	--since	Optional. Only return logs newer than a relative duration like 5s, 2m, or 3h. Defaults to all logs	v
o	--start-time	Optional. Only return logs after a specific date (RFC3339). Defaults to all logs	v
o	--tasks	Optional. Only return logs from specific task IDs	v
o	--help|-h	Help for command	
=	svc logs	--app
d
@	svc exec
o	--app|-a	Name of the application	v
o	--command|-c	Optional. The command that is passed to a running container	v
o	--container	Optional. The specific container you want to exec in. By default the first essential container…	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service, job, or task group	v
o	--task-id	Optional. ID of the task you want to exec in	v
o	--yes	Optional. Whether to update the Session Manager Plugin	
o	--help|-h	Help for command	
=	svc exec	--app
d
@	svc pause
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	svc pause	--app
d
@	svc resume
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--help|-h	Help for command	
=	svc resume	--app
d
@	job
s	init	Creates a new scheduled job in an application
s	ls	Lists all the jobs in an application
s	package	Prints the AWS CloudFormation template of a job
s	deploy	Deploys a job to an environment
s	delete	Deletes a job from an application
o	--help|-h	Help for command	
@	job init
o	--app|-a	Name of the application	v
o	--dockerfile|-d	Path to the Dockerfile	v
o	--image|-i	The location of an existing Docker image	v
o	--job-type|-t	Type of job to create	v
o	--name|-n	Name of the job	v
o	--retries	Optional. The number of times to try restarting the job on a failure	v
o	--schedule|-s	The schedule on which to run this job. Accepts cron expressions of the format (M H DoM M DoW) and…	v
o	--timeout	Optional. The total execution time for the task, including retries. Accepts valid Go duration…	v
o	--help|-h	Help for command	
=	job init	--app
d
=	job init	--job-type
v	Scheduled Job	
@	job ls
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--local	Only show jobs in the workspace	
o	--help|-h	Help for command	
=	job ls	--app
d
@	job package
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the job	v
o	--output-dir	Optional. Writes the stack template and template configuration to a directory	v
o	--tag	Optional. The container image tag	v
o	--help|-h	Help for command	
=	job package	--app
d
@	job deploy
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the job	v
o	--resource-tags	Optional. Labels with a key and value separated by commas. Allows you to categorize resources	v
o	--tag	Optional. The container image tag	v
o	--help|-h	Help for command	
=	job deploy	--app
d
@	job delete
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the job	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	job delete	--app
d
@	task
s	run	Run a one-off task on Amazon ECS
s	exec	Execute a command in a running container part of a task
s	delete	Deletes a one-off task from an application or default cluster
o	--help|-h	Help for command	
@	task run
o	--app	Optional. Name of the application	v
o	--build-context	Path to the Docker build context	v
o	--cluster	Optional. The short name or full ARN of the cluster to run the task in	v
o	--command	Optional. The command that is passed to "docker run" to override the default command	v
o	--count	Optional. The number of tasks to set up	v
o	--cpu	Optional. The number of CPU units to reserve for each task	v
o	--default	Optional. Run tasks in default cluster and default subnets	
o	--dockerfile	Path to the Dockerfile	v
o	--entrypoint	Optional. The entrypoint that is passed to "docker run" to override the default entrypoint	v
o	--env	Optional. Name of the environment	v
o	--env-vars	Optional. Environment variables specified by key=value separated by commas	v
o	--execution-role	Optional. The ARN of the role that grants the container agent permission to make AWS API calls	v
o	--follow	Optional. Specifies if the logs should be streamed	
o	--generate-cmd	Optional. Generate a command with a pre-filled value for each flag. To use it for an ECS service…	v
o	--image|-i	The location of an existing Docker image	v
o	--memory	Optional. The amount of memory to reserve in MiB for each task	v
o	--platform-arch	Optional. Architecture of the task. Must be specified along with 'platform-os'	v
o	--platform-os	Optional. Operating system of the task. Must be specified along with 'platform-arch'	v
o	--resource-tags	Optional. Labels with a key and value separated by commas. Allows you to categorize resources	v
o	--secrets	Optional. Secrets to inject into the container. Specified by key=value separated by commas	v
o	--security-groups	Optional. The security group IDs for the task to use. Can be specified multiple times	v
o	--subnets	Optional. The subnet IDs for the task to use. Can be specified multiple times	v
o	--tag	Optional. The container image tag in addition to "latest"	v
o	--task-group-name|-n	Optional. The group name of the task. Tasks with the same group name share the same set of…	v
o	--task-role	Optional. The ARN of the role for the task to use	v
o	--help|-h	Help for command	
=	task run	--app
d
@	task exec
o	--app|-a	Name of the application	v
o	--command|-c	Optional. The command that is passed to a running container	v
o	--default	Optional. Execute commands in running tasks in default cluster and default subnets	
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service, job, or task group	v
o	--task-id	Optional. ID of the task you want to exec in	v
o	--yes	Optional. Whether to update the Session Manager Plugin	
o	--help|-h	Help for command	
=	task exec	--app
d
@	task delete
o	--app|-a	Name of the application	v
o	--default	Optional. Delete a task which was launched in the default cluster and subnets	
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	task delete	--app
d
@	storage
s	init	Creates a new AWS CloudFormation template for a storage resource
o	--help|-h	Help for command	
@	storage init
o	--engine	The database engine used in the cluster. Must be either "MySQL" or "PostgreSQL"	v
o	--initial-db	The initial database to create in the cluster	v
o	--lsi	Optional. Attribute to use as an alternate sort key. May be specified up to 5 times. Must be of…	v
o	--name|-n	Name of the storage resource to create	v
o	--no-lsi	Optional. Don't ask about configuring alternate sort keys	
o	--no-sort	Optional. Skip configuring sort keys	
o	--parameter-group	Optional. The name of the parameter group to associate with the cluster	v
o	--partition-key	Partition key for the DDB table. Must be of the format '<keyName>:<dataType>'	v
o	--sort-key	Optional. Sort key for the DDB table. Must be of the format '<keyName>:<dataType>'	v
o	--storage-type|-t	Type of storage to add. Must be one of: "DynamoDB", "S3", "Aurora"	v
o	--workload|-w	Name of the service or job to associate with storage	v
o	--help|-h	Help for command	
@	secret
s	init	Create or update secrets in SSM Parameter Store
o	--help|-h	Help for command	
@	secret init
o	--app|-a	Name of the application	v
o	--cli-input-yaml	Optional. A YAML file in which the secret values are specified	v
o	--name|-n	The name of the secret	v
o	--overwrite	Optional. Whether to overwrite an existing secret	
o	--values	Values of the secret in each environment. Specified as <environment>=<value> separated by commas	v
o	--help|-h	Help for command	
=	secret init	--app
d
@	version
o	--help|-h	Help for command	
@	completion
o	--help|-h	Help for command	
@	pipeline
s	init	Creates a pipeline for the services in your workspace
s	update	Deploys a pipeline for the services in your workspace
s	delete	Deletes the pipeline associated with your workspace
s	show	Shows info about a deployed pipeline for an application
s	status	Shows the status of a pipeline
s	ls	Lists all the deployed pipelines in an application
o	--help|-h	Help for command	
@	pipeline init
o	--app|-a	Name of the application	v
o	--environments|-e	Environments to add to the pipeline	v
o	--git-branch|-b	Branch used to trigger your pipeline	v
o	--github-access-token|-t	GitHub personal access token for your repository	v
o	--github-url	(Deprecated.) Use --url instead. Repository URL to trigger your pipeline	v
o	--url|-u	The repository URL to trigger your pipeline. Supported providers are: GitHub, CodeCommit, Bitbucket	v
o	--help|-h	Help for command	
=	pipeline init	--app
d
@	pipeline update
o	--app|-a	Name of the application	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	pipeline update	--app
d
@	pipeline delete
o	--app|-a	Name of the application	v
o	--delete-secret	Deletes AWS Secrets Manager secret associated with a pipeline source repository	
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	pipeline delete	--app
d
@	pipeline show
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the pipeline	v
o	--resources	Optional. Show the resources in your pipeline	
o	--help|-h	Help for command	
=	pipeline show	--app
d
@	pipeline status
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the pipeline	v
o	--help|-h	Help for command	
=	pipeline status	--app
d
@	pipeline ls
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--help|-h	Help for command	
=	pipeline ls	--app
d
@	deploy
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--force	Optional. Force a new service deployment using the existing image	
o	--name|-n	Name of the service or job	v
o	--resource-tags	Optional. Labels with a key and value separated by commas. Allows you to categorize resources	v
o	--tag	Optional. The container image tag	v
o	--help|-h	Help for command	
=	deploy	--app
d
@	help
s	init	Create a new ECS or App Runner application
s	docs	Open the copilot docs
s	app	Commands for applications. Applications are a collection of services and environments
s	env	Commands for environments. Environments are deployment stages shared between services
s	svc	Commands for services. Services are long-running ECS or App Runner services
s	job	Commands for jobs. Jobs are tasks that are triggered by events
s	task	Commands for tasks. One-off Amazon ECS tasks that terminate once their work is done
s	storage	Commands for working with storage and databases
s	secret	Commands for secrets. Secrets are sensitive information that you need in your application
s	version	Print the version number
s	completion	Output shell completion code
s	pipeline	Commands for pipelines. Continuous delivery pipelines to release services
s	deploy	Deploy a Copilot job or service
o	--help|-h	Help for command	
@	help init
o	--help|-h	Help for command	
@	help docs
o	--help|-h	Help for command	
@	help app
s	init	Creates a new empty application
s	ls	Lists all the applications in your account
s	show	Shows info about an application
s	delete	Delete all resources associated with the application
s	upgrade	Upgrades the template of an application to the latest version
o	--help|-h	Help for command	
@	help app init
o	--domain	Optional. Your existing custom domain name	v
o	--resource-tags	Optional. Labels with a key and value separated by commas. Allows you to categorize resources	v
o	--help|-h	Help for command	
@	help app ls
o	--help|-h	Help for command	
@	help app show
o	--json	Outputs in JSON format	
o	--name|-n	Name of the application	v
o	--help|-h	Help for command	
@	help app delete
o	--name|-n	Name of the application	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
@	help app upgrade
o	--name|-n	Name of the application	v
o	--help|-h	Help for command	
@	help env
s	init	Creates a new environment in your application
s	ls	Lists all the environments in an application
s	delete	Deletes an environment from your application
s	show	Shows info about a deployed environment
o	--help|-h	Help for command	
@	help env init
o	--app|-a	Name of the application	v
o	--aws-access-key-id	Optional. An AWS access key	v
o	--aws-secret-access-key	Optional. An AWS secret access key	v
o	--aws-session-token	Optional. An AWS session token for temporary credentials	v
o	--default-config	Optional. Skip prompting and use default environment configuration	
o	--import-private-subnets	Optional. Use existing private subnet IDs	v
o	--import-public-subnets	Optional. Use existing public subnet IDs	v
o	--import-vpc-id	Optional. Use an existing VPC ID	v
o	--name|-n	Name of the environment	v
o	--override-az-names	Optional. Availability Zone names. (default 2 random AZs)	v
o	--override-private-cidrs	Optional. CIDR to use for private subnets. (default 10.0.2.0/24,10.0.3.0/24)	v
o	--override-public-cidrs	Optional. CIDR to use for public subnets. (default 10.0.0.0/24,10.0.1.0/24)	v
o	--override-vpc-cidr	Optional. Global CIDR to use for VPC. (default 10.0.0.0/16)	v
o	--prod	If the environment contains production services	
o	--profile	Name of the profile	v
o	--region	Optional. An AWS region where the environment will be created	v
o	--help|-h	Help for command	
=	help env init	--app
d
@	help env ls
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--help|-h	Help for command	
=	help env ls	--app
d
@	help env delete
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	help env delete	--app
d
@	help env show
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the environment	v
o	--resources	Optional. Show the resources in your environment	
o	--help|-h	Help for command	
=	help env show	--app
d
@	help svc
s	init	Creates a new service in an application
s	ls	Lists all the services in an application
s	package	Prints the AWS CloudFormation template of a service
s	deploy	Deploys a service to an environment
s	delete	Deletes a service from an application
s	show	Shows info about a deployed service per environment
s	status	Shows status of a deployed service
s	logs	Displays logs of a deployed service
s	exec	Execute a command in a running container part of a service
s	pause	Pause running App Runner service
s	resume	Resumes a paused service
o	--help|-h	Help for command	
@	help svc init
o	--app|-a	Name of the application	v
o	--dockerfile|-d	Path to the Dockerfile	v
o	--image|-i	The location of an existing Docker image	v
o	--name|-n	Name of the service	v
o	--no-subscribe	Optional. Turn off selection for adding subscriptions for worker services	
o	--port	The port on which your service listens	v
o	--subscribe-topics	Optional. SNS Topics to subscribe to from other services in your application. Must be of format…	v
o	--svc-type|-t	Type of service to create	v
o	--help|-h	Help for command	
=	help svc init	--app
d
=	help svc init	--svc-type
v	Request-Driven Web Service	
v	Load Balanced Web Service	
v	Backend Service	
v	Worker Service	
@	help svc ls
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--local	Only show services in the workspace	
o	--help|-h	Help for command	
=	help svc ls	--app
d
@	help svc package
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--output-dir	Optional. Writes the stack template and template configuration to a directory	v
o	--tag	Optional. The container image tag	v
o	--help|-h	Help for command	
=	help svc package	--app
d
@	help svc deploy
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--force	Optional. Force a new service deployment using the existing image	
o	--name|-n	Name of the service	v
o	--resource-tags	Optional. Labels with a key and value separated by commas. Allows you to categorize resources	v
o	--tag	Optional. The container image tag	v
o	--help|-h	Help for command	
=	help svc deploy	--app
d
@	help svc delete
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	help svc delete	--app
d
@	help svc show
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the service	v
o	--resources	Optional. Show the resources in your service	
o	--help|-h	Help for command	
=	help svc show	--app
d
@	help svc status
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the service	v
o	--help|-h	Help for command	
=	help svc status	--app
d
@	help svc logs
o	--app|-a	Name of the application	v
o	--end-time	Optional. Only return logs before a specific date (RFC3339). Defaults to all logs	v
o	--name|-n	Name of the environment	v
o	--follow	Optional. Specifies if the logs should be streamed	
o	--json	Outputs in JSON format	
o	--limit	Optional. The maximum number of log events returned. Default is 10 unless any time filtering flags…	v
o	--log-group	Optional. Only return logs from specific log group	v
o	--name|-n	Name of the service	v
o	--since	Optional. Only return logs newer than a relative duration like 5s, 2m, or 3h. Defaults to all logs	v
o	--start-time	Optional. Only return logs after a specific date (RFC3339). Defaults to all logs	v
o	--tasks	Optional. Only return logs from specific task IDs	v
o	--help|-h	Help for command	
=	help svc logs	--app
d
@	help svc exec
o	--app|-a	Name of the application	v
o	--command|-c	Optional. The command that is passed to a running container	v
o	--container	Optional. The specific container you want to exec in. By default the first essential container…	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service, job, or task group	v
o	--task-id	Optional. ID of the task you want to exec in	v
o	--yes	Optional. Whether to update the Session Manager Plugin	
o	--help|-h	Help for command	
=	help svc exec	--app
d
@	help svc pause
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	help svc pause	--app
d
@	help svc resume
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--help|-h	Help for command	
=	help svc resume	--app
d
@	help job
s	init	Creates a new scheduled job in an application
s	ls	Lists all the jobs in an application
s	package	Prints the AWS CloudFormation template of a job
s	deploy	Deploys a job to an environment
s	delete	Deletes a job from an application
o	--help|-h	Help for command	
@	help job init
o	--app|-a	Name of the application	v
o	--dockerfile|-d	Path to the Dockerfile	v
o	--image|-i	The location of an existing Docker image	v
o	--job-type|-t	Type of job to create	v
o	--name|-n	Name of the job	v
o	--retries	Optional. The number of times to try restarting the job on a failure	v
o	--schedule|-s	The schedule on which to run this job. Accepts cron expressions of the format (M H DoM M DoW) and…	v
o	--timeout	Optional. The total execution time for the task, including retries. Accepts valid Go duration…	v
o	--help|-h	Help for command	
=	help job init	--app
d
=	help job init	--job-type
v	Scheduled Job	
@	help job ls
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--local	Only show jobs in the workspace	
o	--help|-h	Help for command	
=	help job ls	--app
d
@	help job package
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the job	v
o	--output-dir	Optional. Writes the stack template and template configuration to a directory	v
o	--tag	Optional. The container image tag	v
o	--help|-h	Help for command	
=	help job package	--app
d
@	help job deploy
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the job	v
o	--resource-tags	Optional. Labels with a key and value separated by commas. Allows you to categorize resources	v
o	--tag	Optional. The container image tag	v
o	--help|-h	Help for command	
=	help job deploy	--app
d
@	help job delete
o	--app|-a	Name of the application	v
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the job	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	help job delete	--app
d
@	help task
s	run	Run a one-off task on Amazon ECS
s	exec	Execute a command in a running container part of a task
s	delete	Deletes a one-off task from an application or default cluster
o	--help|-h	Help for command	
@	help task run
o	--app	Optional. Name of the application	v
o	--build-context	Path to the Docker build context	v
o	--cluster	Optional. The short name or full ARN of the cluster to run the task in	v
o	--command	Optional. The command that is passed to "docker run" to override the default command	v
o	--count	Optional. The number of tasks to set up	v
o	--cpu	Optional. The number of CPU units to reserve for each task	v
o	--default	Optional. Run tasks in default cluster and default subnets	
o	--dockerfile	Path to the Dockerfile	v
o	--entrypoint	Optional. The entrypoint that is passed to "docker run" to override the default entrypoint	v
o	--env	Optional. Name of the environment	v
o	--env-vars	Optional. Environment variables specified by key=value separated by commas	v
o	--execution-role	Optional. The ARN of the role that grants the container agent permission to make AWS API calls	v
o	--follow	Optional. Specifies if the logs should be streamed	
o	--generate-cmd	Optional. Generate a command with a pre-filled value for each flag. To use it for an ECS service…	v
o	--image|-i	The location of an existing Docker image	v
o	--memory	Optional. The amount of memory to reserve in MiB for each task	v
o	--platform-arch	Optional. Architecture of the task. Must be specified along with 'platform-os'	v
o	--platform-os	Optional. Operating system of the task. Must be specified along with 'platform-arch'	v
o	--resource-tags	Optional. Labels with a key and value separated by commas. Allows you to categorize resources	v
o	--secrets	Optional. Secrets to inject into the container. Specified by key=value separated by commas	v
o	--security-groups	Optional. The security group IDs for the task to use. Can be specified multiple times	v
o	--subnets	Optional. The subnet IDs for the task to use. Can be specified multiple times	v
o	--tag	Optional. The container image tag in addition to "latest"	v
o	--task-group-name|-n	Optional. The group name of the task. Tasks with the same group name share the same set of…	v
o	--task-role	Optional. The ARN of the role for the task to use	v
o	--help|-h	Help for command	
=	help task run	--app
d
@	help task exec
o	--app|-a	Name of the application	v
o	--command|-c	Optional. The command that is passed to a running container	v
o	--default	Optional. Execute commands in running tasks in default cluster and default subnets	
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service, job, or task group	v
o	--task-id	Optional. ID of the task you want to exec in	v
o	--yes	Optional. Whether to update the Session Manager Plugin	
o	--help|-h	Help for command	
=	help task exec	--app
d
@	help task delete
o	--app|-a	Name of the application	v
o	--default	Optional. Delete a task which was launched in the default cluster and subnets	
o	--name|-n	Name of the environment	v
o	--name|-n	Name of the service	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	help task delete	--app
d
@	help storage
s	init	Creates a new AWS CloudFormation template for a storage resource
o	--help|-h	Help for command	
@	help storage init
o	--engine	The database engine used in the cluster. Must be either "MySQL" or "PostgreSQL"	v
o	--initial-db	The initial database to create in the cluster	v
o	--lsi	Optional. Attribute to use as an alternate sort key. May be specified up to 5 times. Must be of…	v
o	--name|-n	Name of the storage resource to create	v
o	--no-lsi	Optional. Don't ask about configuring alternate sort keys	
o	--no-sort	Optional. Skip configuring sort keys	
o	--parameter-group	Optional. The name of the parameter group to associate with the cluster	v
o	--partition-key	Partition key for the DDB table. Must be of the format '<keyName>:<dataType>'	v
o	--sort-key	Optional. Sort key for the DDB table. Must be of the format '<keyName>:<dataType>'	v
o	--storage-type|-t	Type of storage to add. Must be one of: "DynamoDB", "S3", "Aurora"	v
o	--workload|-w	Name of the service or job to associate with storage	v
o	--help|-h	Help for command	
@	help secret
s	init	Create or update secrets in SSM Parameter Store
o	--help|-h	Help for command	
@	help secret init
o	--app|-a	Name of the application	v
o	--cli-input-yaml	Optional. A YAML file in which the secret values are specified	v
o	--name|-n	The name of the secret	v
o	--overwrite	Optional. Whether to overwrite an existing secret	
o	--values	Values of the secret in each environment. Specified as <environment>=<value> separated by commas	v
o	--help|-h	Help for command	
=	help secret init	--app
d
@	help version
o	--help|-h	Help for command	
@	help completion
o	--help|-h	Help for command	
@	help pipeline
s	init	Creates a pipeline for the services in your workspace
s	update	Deploys a pipeline for the services in your workspace
s	delete	Deletes the pipeline associated with your workspace
s	show	Shows info about a deployed pipeline for an application
s	status	Shows the status of a pipeline
s	ls	Lists all the deployed pipelines in an application
o	--help|-h	Help for command	
@	help pipeline init
o	--app|-a	Name of the application	v
o	--environments|-e	Environments to add to the pipeline	v
o	--git-branch|-b	Branch used to trigger your pipeline	v
o	--github-access-token|-t	GitHub personal access token for your repository	v
o	--github-url	(Deprecated.) Use --url instead. Repository URL to trigger your pipeline	v
o	--url|-u	The repository URL to trigger your pipeline. Supported providers are: GitHub, CodeCommit, Bitbucket	v
o	--help|-h	Help for command	
=	help pipeline init	--app
d
@	help pipeline update
o	--app|-a	Name of the application	v
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	help pipeline update	--app
d
@	help pipeline delete
o	--app|-a	Name of the application	v
o	--delete-secret	Deletes AWS Secrets Manager secret associated with a pipeline source repository	
o	--yes	Skips confirmation prompt	
o	--help|-h	Help for command	
=	help pipeline delete	--app
d
@	help pipeline show
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the pipeline	v
o	--resources	Optional. Show the resources in your pipeline	
o	--help|-h	Help for command	
=	help pipeline show	--app
d
@	help pipeline status
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--name|-n	Name of the pipeline	v
o	--help|-h	Help for command	
=	help pipeline status	--app
d
@	help pipeline ls
o	--app|-a	Name of the application	v
o	--json	Outputs in JSON format	
o	--help|-h	Help for command	
=	help pipeline ls	--app
d
@	help deploy
o	--help|-h	Help for command	
