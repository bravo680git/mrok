@	
s	deploy	Deploy a Serverless service
s	info	Display information about the service
s	invoke	Invoke a deployed function
s	logs	Output the logs of a deployed function
s	metrics	Show metrics for a specific function
s	remove	Remove Serverless service and all resources
s	rollback	Rollback the Serverless service to a specific deployment
s	studio	Develop a Serverless application in the cloud
s	test	Run HTTP tests
s	package	Package a Serverless service
s	plugin	Handle plugins
s	print	Print your compiled and resolved config file
s	create	Create new Serverless service
s	dashboard	Open the Serverless dashboard
s	generate-event	Generate event
s	install	Install a Serverless service from GitHub or a plugin from the Serverless registry
s	login	Login or sign up for Serverless
s	logout	Logout from Serverless
s	output	Get/list value of dashboard deployment profile parameter
s	param	Get/list value of dashboard service output
s	slstats	Enable or disable stats
o	--help	Show help	
@	deploy
s	function	
s	list	
o	--conceal	Hide secrets from the output (e.g. API Gateway key values)	
o	--package|-p	Path of the deployment package	v
o	--verbose|-v	Show all stack events during deployment	v
o	--force	Forces a deployment to take place	
o	--function|-f	Name of the function	v
o	--aws-s3-accelerate	Enables S3 Transfer Acceleration making uploading artifacts much faster	
o	--region|-r	Region of the service	v
o	--aws-profile	AWS profile to use with the command	v
o	--app	Dashboard app	v
o	--org	Dashboard org	v
o	--use-local-credentials	Rely on locally resolved AWS credentials instead of loading them from Dashboard provider settings…	
o	--config|-c	Path to serverless config file	v
o	--stage|-s	Stage of the service	v
o	--help|-h	Show help	
o	--version	Show version info	
=	deploy	--package
t	folders
=	deploy	--region
v	us-east-2	
v	us-east-1	
v	us-west-1	
v	us-west-2	
v	af-south-1	
v	ap-east-1	
v	ap-south-1	
v	ap-northeast-3	
v	ap-northeast-2	
v	ap-southeast-1	
v	ap-southeast-2	
v	ap-northeast-1	
v	ca-central-1	
v	cn-north-1	
v	cn-northwest-1	
v	eu-central-1	
v	eu-west-1	
v	eu-west-2	
v	eu-south-1	
v	eu-west-3	
v	eu-north-1	
v	me-south-1	
v	sa-east-1	
v	us-gov-east-1	
v	us-gov-west-1	
=	deploy	--config
t	filepaths
@	deploy function
o	--app	Dashboard app	v
o	--aws-profile	AWS profile to use with the command	v
o	--config|-c	Path to serverless config file	v
o	--function|-f	Name of the function	v
o	--help|-h	Show help	
o	--org	Dashboard org	v
o	--region|-r	Region of the service	v
o	--stage|-s	Stage of the service	v
o	--use-local-credentials	Rely on locally resolved AWS credentials instead of loading them from Dashboard provider settings…	
o	--version	Show version info	
o	--force	Forces a deployment to take place	
o	--update-config|-u	Updates function configuration, e.g. Timeout or Memory Size without deploying code	v
=	deploy function	--config
t	filepaths
=	deploy function	--region
v	us-east-2	
v	us-east-1	
v	us-west-1	
v	us-west-2	
v	af-south-1	
v	ap-east-1	
v	ap-south-1	
v	ap-northeast-3	
v	ap-northeast-2	
v	ap-southeast-1	
v	ap-southeast-2	
v	ap-northeast-1	
v	ca-central-1	
v	cn-north-1	
v	cn-northwest-1	
v	eu-central-1	
v	eu-west-1	
v	eu-west-2	
v	eu-south-1	
v	eu-west-3	
v	eu-north-1	
v	me-south-1	
v	sa-east-1	
v	us-gov-east-1	
v	us-gov-west-1	
@	deploy list
s	functions	
o	--region|-r	Region of the service	v
o	--aws-profile	AWS profile to use with the command	v
o	--app	Dashboard app	v
o	--org	Dashboard org	v
o	--use-local-credentials	Rely on locally resolved AWS credentials instead of loading them from Dashboard provider settings…	
o	--config|-c	Path to serverless config file	v
o	--stage|-s	Stage of the service	v
o	--help|-h	Show help	
o	--version	Show version info	
=	deploy list	--region
v	us-east-2	
v	us-east-1	
v	us-west-1	
v	us-west-2	
v	af-south-1	
v	ap-east-1	
v	ap-south-1	
v	ap-northeast-3	
v	ap-northeast-2	
v	ap-southeast-1	
v	ap-southeast-2	
v	ap-northeast-1	
v	ca-central-1	
v	cn-north-1	
v	cn-northwest-1	
v	eu-central-1	
v	eu-west-1	
v	eu-west-2	
v	eu-south-1	
v	eu-west-3	
v	eu-north-1	
v	me-south-1	
v	sa-east-1	
v	us-gov-east-1	
v	us-gov-west-1	
=	deploy list	--config
t	filepaths
@	deploy list functions
o	--region|-r	Region of the service	v
o	--aws-profile	AWS profile to use with the command	v
o	--app	Dashboard app	v
o	--org	Dashboard org	v
o	--use-local-credentials	Rely on locally resolved AWS credentials instead of loading them from Dashboard provider settings…	
o	--config|-c	Path to serverless config file	v
o	--stage|-s	Stage of the service	v
o	--help|-h	Show help	
o	--version	Show version info	
=	deploy list functions	--region
v	us-east-2	
v	us-east-1	
v	us-west-1	
v	us-west-2	
v	af-south-1	
v	ap-east-1	
v	ap-south-1	
v	ap-northeast-3	
v	ap-northeast-2	
v	ap-southeast-1	
v	ap-southeast-2	
v	ap-northeast-1	
v	ca-central-1	
v	cn-north-1	
v	cn-northwest-1	
v	eu-central-1	
v	eu-west-1	
v	eu-west-2	
v	eu-south-1	
v	eu-west-3	
v	eu-north-1	
v	me-south-1	
v	sa-east-1	
v	us-gov-east-1	
v	us-gov-west-1	
=	deploy list functions	--config
t	filepaths
@	info
o	--conceal	Hide secrets from the output (e.g. API Gateway key values)	
o	--region|-r	Region of the service	v
o	--aws-profile	AWS profile to use with the command	v
o	--app	Dashboard app	v
o	--org	Dashboard org	v
o	--use-local-credentials	Rely on locally resolved AWS credentials instead of loading them from Dashboard provider settings…	
o	--config|-c	Path to serverless config file	v
o	--stage|-s	Stage of the service	v
o	--help|-h	Show help	
o	--version	Show version info	
=	info	--region
v	us-east-2	
v	us-east-1	
v	us-west-1	
v	us-west-2	
v	af-south-1	
v	ap-east-1	
v	ap-south-1	
v	ap-northeast-3	
v	ap-northeast-2	
v	ap-southeast-1	
v	ap-southeast-2	
v	ap-northeast-1	
v	ca-central-1	
v	cn-north-1	
v	cn-northwest-1	
v	eu-central-1	
v	eu-west-1	
v	eu-west-2	
v	eu-south-1	
v	eu-west-3	
v	eu-north-1	
v	me-south-1	
v	sa-east-1	
v	us-gov-east-1	
v	us-gov-west-1	
=	info	--config
t	filepaths
@	invoke
s	local	
o	--function|-f	Name of the function	v
o	--path|-p	Path to JSON or YAML file holding input data	v
o	--data|-d	Input data	v
o	--raw	Flag to pass input data as a raw string	
o	--context	Context of the service	v
o	--contextPath	Path to JSON or YAML file holding context data	v
o	--region|-r	Region of the service	v
o	--aws-profile	AWS profile to use with the command	v
o	--app	Dashboard app	v
o	--org	Dashboard org	v
o	--use-local-credentials	Rely on locally resolved AWS credentials instead of loading them from Dashboard provider settings…	
o	--config|-c	Path to serverless config file	v
o	--stage|-s	Stage of the service	v
o	--help|-h	Show help	
o	--version	Show version info	
=	invoke	--path
t	filepaths
=	invoke	--contextPath
t	filepaths
=	invoke	--region
v	us-east-2	
v	us-east-1	
v	us-west-1	
v	us-west-2	
v	af-south-1	
v	ap-east-1	
v	ap-south-1	
v	ap-northeast-3	
v	ap-northeast-2	
v	ap-southeast-1	
v	ap-southeast-2	
v	ap-northeast-1	
v	ca-central-1	
v	cn-north-1	
v	cn-northwest-1	
v	eu-central-1	
v	eu-west-1	
v	eu-west-2	
v	eu-south-1	
v	eu-west-3	
v	eu-north-1	
v	me-south-1	
v	sa-east-1	
v	us-gov-east-1	
v	us-gov-west-1	
=	invoke	--config
t	filepaths
@	invoke local
o	--function|-f	Name of the function	v
o	--path|-p	Path to JSON or YAML file holding input data	v
o	--data|-d	Input data	v
o	--raw	Flag to pass input data as a raw string	
o	--context	Context of the service	v
o	--contextPath	Path to JSON or YAML file holding context data	v
o	--env|-e	Override environment variables. e.g. --env VAR1=val1 --env VAR2=val2	v
o	--region|-r	Region of the service	v
o	--aws-profile	AWS profile to use with the command	v
o	--app	Dashboard app	v
o	--org	Dashboard org	v
o	--use-local-credentials	Rely on locally resolved AWS credentials instead of loading them from Dashboard provider settings…	
o	--config|-c	Path to serverless config file	v
o	--stage|-s	Stage of the service	v
o	--help|-h	Show help	
o	--version	Show version info	
=	invoke local	--path
t	filepaths
=	invoke local	--contextPath
t	filepaths
=	invoke local	--region
v	us-east-2	
v	us-east-1	
v	us-west-1	
v	us-west-2	
v	af-south-1	
v	ap-east-1	
v	ap-south-1	
v	ap-northeast-3	
v	ap-northeast-2	
v	ap-southeast-1	
v	ap-southeast-2	
v	ap-northeast-1	
v	ca-central-1	
v	cn-north-1	
v	cn-northwest-1	
v	eu-central-1	
v	eu-west-1	
v	eu-west-2	
v	eu-south-1	
v	eu-west-3	
v	eu-north-1	
v	me-south-1	
v	sa-east-1	
v	us-gov-east-1	
v	us-gov-west-1	
=	invoke local	--config
t	filepaths
@	logs
@	metrics
@	remove
@	rollback
@	studio
@	test
@	package
@	plugin
@	print
@	create
@	dashboard
@	generate-event
@	install
@	login
@	logout
@	output
@	param
@	slstats
