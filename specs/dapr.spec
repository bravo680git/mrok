@	
s	annotate	Add dapr annotations to a Kubernetes configuration. Supported platforms: Kubernetes
s	build-info	Print build info of Dapr CLI and runtime
s	completion	Generates shell completion scripts
s	components	List all Dapr components. Supported platforms: Kubernetes
s	configurations	List all Dapr configurations. Supported platforms: Kubernetes
s	dashboard	Start Dapr dashboard. Supported platforms: Kubernetes and self-hosted
s	init	Install Dapr on supported hosting platforms. Supported platforms: Kubernetes and self-hosted
s	invoke	Invoke a method on a given Dapr application. Supported platforms: Self-hosted
s	list	List all Dapr instances. Supported platforms: Kubernetes and self-hosted
s	logs	Get Dapr sidecar logs for an application. Supported platforms: Kubernetes
s	mtls	Check if mTLS is enabled. Supported platforms: Kubernetes
s	publish	Publish a pub-sub event. Supported platforms: Self-hosted
s	run	Run Dapr and (optionally) your application side by side. Supported platforms: Self-hosted
s	status	Show the health status of Dapr services. Supported platforms: Kubernetes
s	stop	Stop Dapr instances and their associated apps. Supported platforms: Self-hosted
s	uninstall	Uninstall Dapr runtime. Supported platforms: Kubernetes and self-hosted
s	upgrade	Upgrades or downgrades a Dapr control plane installation in a cluster. Supported platforms…
s	version	Print the Dapr runtime and CLI version
s	help	Help about any command
o	--version|-v	Version for dapr	
o	--log-as-json	Log output in JSON format	p
o	--runtime-path	The path to the dapr runtime installation directory	vp
o	--help|-h	Display help	p
=		--runtime-path
t	folders
@	annotate
o	--api-token-secret	The secret to use for the API token	v
o	--app-id|-a	The app id to annotate	v
o	--app-max-concurrency	The maximum number of concurrent requests to allow	v
o	--app-port|-p	The port to expose the app on	v
o	--app-protocol	The protocol to use for the app. Allowed values http, https, h2c, grpc, grpcs	v
o	--app-token-secret	The secret to use for the app token	v
o	--config|-c	The config file to annotate	v
o	--cpu-limit	The CPU limit to set	v
o	--cpu-request	The CPU request to set	v
o	--dapr-image	The image to use for the dapr sidecar container	v
o	--disable-builtin-k8s-secret-store	Disable the built-in k8s secret store	
o	--enable-api-logging	Enable API logging for the Dapr sidecar	
o	--enable-debug	Enable debug	
o	--enable-metrics	Enable metrics	
o	--enable-profile	Enable profiling	
o	--env	Environment variables to set (key value pairs, comma separated)	v
o	--graceful-shutdown-seconds	The number of seconds to wait for the app to shutdown	v
o	--http-read-buffer-size	The maximum size of HTTP header read buffer in kilobytes	v
o	--http-stream-request-body	Enable streaming request body for HTTP	
o	--kubernetes|-k	Apply annotations to Kubernetes resources	
o	--listen-addresses	The addresses to listen on	v
o	--liveness-probe-delay	The delay to use for the liveness probe	v
o	--liveness-probe-period	The period to use for the liveness probe	v
o	--liveness-probe-threshold	The threshold to use for the liveness probe	v
o	--liveness-probe-timeout	The timeout to use for the liveness probe	v
o	--log-as-json	Log as JSON	
o	--log-level	The log level to use	v
o	--max-request-body-size	The maximum request body size to use	v
o	--memory-limit	The memory limit to set	v
o	--memory-request	The memory request to set	v
o	--metrics-port	The port to expose the metrics on	v
o	--namespace|-n	The namespace the resource target is in (can only be set if --resource is also set)	v
o	--placement-host-address	Comma separated list of addresses for Dapr actor placement servers	v
o	--readiness-probe-delay	The delay to use for the readiness probe	v
o	--readiness-probe-period	The period to use for the readiness probe	v
o	--readiness-probe-threshold	The threshold to use for the readiness probe	v
o	--readiness-probe-timeout	The timeout to use for the readiness probe	v
o	--resource|-r	The resource to target to annotate	v
o	--unix-domain-socket-path	Linux domain socket path to use for communicating with the Dapr sidecar	v
o	--volume-mounts	List of pod volumes to be mounted to the sidecar container in read-only mode	v
o	--volume-mounts-rw	List of pod volumes to be mounted to the sidecar container in read-write mode	v
a	1	0
=	annotate	--app-id
d
=	annotate	--app-protocol
v	http	
v	https	
v	h2c	
v	grpc	
v	grpcs	
=	annotate	--config
d
#	annotate	1
d
@	build-info
o	--help|-h	Print this help message	
@	completion
s	bash	Generates bash completion scripts
s	fish	Generates fish completion scripts
s	powershell	Generates powershell completion scripts
s	zsh	Generates zsh completion scripts
o	--help|-h	Print this help message	
@	completion bash
o	--help|-h	Print this help message	
@	completion fish
o	--help|-h	Print this help message	
@	completion powershell
o	--help|-h	Print this help message	
@	completion zsh
o	--help|-h	Print this help message	
@	components
o	--all-namespaces|-A	If true, list all Dapr components in all namespaces	
o	--help|-h	Print this help message	
o	--kubernetes|-k	List all Dapr components in a Kubernetes cluster	
o	--name|-n	The components name to be printed (optional)	v
o	--namespace	List all namespace components in a Kubernetes cluster	v
o	--output|-o	Output format (options: json or yaml or list)	v
=	components	--output
v	json	
v	yaml	
v	list	
@	configurations
o	--all-namespaces|-A	If true, list all Dapr configurations in all namespaces	
o	--help|-h	Print this help message	
o	--kubernetes|-k	List all Dapr configurations in a Kubernetes cluster	
o	--name|-n	The configuration name to be printed (optional)	v
o	--namespace	List Define namespace configurations in a Kubernetes cluster	v
o	--output|-o	Output format (options: json or yaml or list)	v
=	configurations	--output
v	json	
v	yaml	
v	list	
@	dashboard
o	--address|-a	Address to listen on. Only accepts IP address or localhost as a value	v
o	--help|-h	Print this help message	
o	--kubernetes|-k	Opens Dapr dashboard in local browser via local proxy to Kubernetes cluster	
o	--namespace|-n	The namespace where Dapr dashboard is running	v
o	--port|-p	The local port on which to serve Dapr dashboard	v
o	--version|-v	Print the version for Dapr dashboard	
@	init
o	--ca-root-certificate	The root certificate file	v
o	--container-runtime	The container runtime to use. Supported values are docker (default) and podman	v
o	--dashboard-version	The version of the Dapr dashboard to install, for example: 0.13.0	v
o	--dev	Use Dev mode. Deploy Redis, Zipkin also in the Kubernetes cluster	
o	--enable-ha	Enable high availability (HA) mode	
o	--enable-mtls	Enable mTLS in your cluster	
o	--from-dir	Use Dapr artifacts from local directory for self-hosted installation	v
o	--help|-h	Print this help message	
o	--image-registry	Custom/private docker image repository URL	v
o	--image-variant	The image variant to use for the Dapr runtime, for example: mariner	v
o	--issuer-private-key	The issuer certificate private key	v
o	--issuer-public-certificate	The issuer certificate	v
o	--kubernetes|-k	Deploy Dapr to a Kubernetes cluster	
o	--namespace|-n	The Kubernetes namespace to install Dapr in	v
o	--network	The Docker network on which to deploy the Dapr runtime	v
o	--runtime-version	The version of the Dapr runtime to install, for example: 1.0.0	v
o	--set	Set values on the command line (can specify multiple or separate values with commas…	v
o	--slim|-s	Exclude placement service, Redis and Zipkin containers from self-hosted installation	
o	--timeout	The wait timeout for the Kubernetes installation	v
o	--wait	Wait for Kubernetes initialization to complete	
=	init	--container-runtime
v	docker	
v	podman	
=	init	--runtime-version
d
@	invoke
o	--app-id|-a	The application id to invoke	v
o	--data|-d	The JSON serialized data string (optional)	v
o	--data-file|-f	A file containing the JSON serialized data (optional)	v
o	--help|-h	Print this help message	
o	--method|-m	The method to invoke	v
o	--unix-domain-socket|-u	Path to a unix domain socket dir. If specified, Dapr API servers will use Unix Domain Sockets	v
o	--verb|-v	The HTTP verb to use	v
=	invoke	--app-id
d
=	invoke	--data-file
t	filepaths
@	list
o	--all-namespaces|-A	If true, list all Dapr pods in all namespaces	
o	--help|-h	Print this help message	
o	--kubernetes|-k	List all Dapr pods in a Kubernetes cluster	
o	--namespace	List define namespace pod in a Kubernetes cluster	v
o	--output|-o	The output format of the list. Valid values are: json, yaml, or table (default)	v
=	list	--output
v	json	
v	yaml	
v	table	
@	logs
o	--app-id|-a	The application id for which logs are needed	v
o	--help|-h	Print this help message	
o	--kubernetes|-k	Get logs from a Kubernetes cluster	
o	--namespace|-n	The Kubernetes namespace in which your application is deployed	v
o	--pod-name|-p	The name of the pod in Kubernetes, in case your application has multiple pods (optional)	v
=	logs	--app-id
d
@	mtls
s	expiry	Checks the expiry of the root certificate
s	export	Export the root CA, issuer cert and key from Kubernetes to local files
s	renew-cert|rnc|renew-certificate	Rotates the Dapr root certificate on your Kubernetes cluster
o	--help|-h	Print this help message	
o	--kubernetes|-k	Check if mTLS is enabled in a Kubernetes cluster	
@	mtls expiry
@	mtls export
o	--help|-h	Print this help message	
o	--out|-o	The output directory path to save the certs	v
@	mtls renew-cert
o	--ca-root-certificate	The root certificate file	v
o	--image-variant	The image variant to use for the Dapr runtime, for example: mariner	v
o	--issuer-private-key	The issuer certificate private key	v
o	--issuer-public-certificate	The issuer certificate	v
o	--kubernetes|-k	Renews root and issuer certificates of Dapr in a Kubernetes cluster	
o	--private-key	The root.key file which is used to generate root certificate	v
o	--restart	Restart Dapr control plane services	
o	--timeout	The timeout for the certificate renewal	v
o	--valid-until	Max days before certificate expires	v
@	publish
o	--data|-d	The JSON serialized data string (optional)	v
o	--data-file|-f	A file containing the JSON serialized data (optional)	v
o	--help|-h	Print this help message	
o	--metadata|-m	The JSON serialized publish metadata (optional)	v
o	--publish-app-id|-i	The ID of the publishing app	v
o	--pubsub|-p	The name of the pub/sub component	v
o	--topic|-t	The topic to be published to	v
o	--unix-domain-socket|-u	Path to a unix domain socket dir. If specified, Dapr API servers will use Unix Domain Sockets	v
@	run
o	--app-channel-address	The network address the application listens on	v
o	--app-health-check-path	Path used for health checks; HTTP only	v
o	--app-health-probe-interval	Interval to probe for the health of the app in seconds	v
o	--app-health-probe-timeout	Timeout for app health probes in milliseconds	v
o	--app-health-threshold	Number of consecutive failures for the app to be considered unhealthy	v
o	--app-id|-a	The id for your application, used for service discovery	v
o	--app-max-concurrency	The concurrency level of the application, otherwise is unlimited	v
o	--app-port|-p	The port your application is listening on	v
o	--app-protocol|-P	The protocol (grpc, grpcs, http, https, h2c) Dapr uses to talk to the application	v
o	--app-ssl	Enable https when Dapr invokes the application	
o	--components-path|-d	The path for components directory. Default is $HOME/.dapr/components or %USERPROFILE%.daprcomponents	v
o	--config|-c	Dapr configuration file	v
o	--dapr-grpc-port|-G	The gRPC port for Dapr to listen on	v
o	--dapr-http-max-request-size	Max size of request body in MB	v
o	--dapr-http-port|-H	The HTTP port for Dapr to listen on	v
o	--dapr-http-read-buffer-size	HTTP header read buffer in KB	v
o	--dapr-internal-grpc-port|-I	The gRPC port for the Dapr internal API to listen on	v
o	--dapr-listen-addresses	Comma separated list of IP addresses that sidecar will listen to	v
o	--enable-api-logging	Log API calls at INFO verbosity. Valid values are: true or false	
o	--enable-app-health-check	Enable health checks for the application using the protocol defined with app-protocol	
o	--enable-profiling	Enable pprof profiling via an HTTP endpoint	
o	--help|-h	Print this help message	
o	--kubernetes|-k	Run the multi-app run template against Kubernetes environment	
o	--log-level	The log verbosity. Valid values are: debug, info, warn, error, fatal, or panic	v
o	--metrics-port|-M	The port of metrics on dapr	v
o	--placement-host-address	The address of the placement service. Format is either <hostname> for default port or…	v
o	--profile-port	The port for the profile server to listen on	v
o	--resources-path	The path for resources directory	v
o	--run-file|-f	Path to the run template file for the list of apps to run	v
o	--unix-domain-socket|-u	Path to a unix domain socket dir. If specified, Dapr API servers will use Unix Domain Sockets	v
=	run	--app-protocol
v	http	
v	https	
v	h2c	
v	grpc	
v	grpcs	
=	run	--components-path
t	folders
=	run	--config
d
=	run	--resources-path
t	folders
=	run	--run-file
d
@	status
o	--help|-h	Print this help message	
o	--kubernetes|-k	Show the health status of Dapr services on Kubernetes cluster	
@	stop
o	--app-id|-a	The application id to be stopped	v
o	--help|-h	Print this help message	
o	--kubernetes|-k	Stop deployments in Kunernetes based on multi-app run file	
o	--run-file|-f	Path to the run template file for the list of apps to stop	v
=	stop	--app-id
d
=	stop	--run-file
d
@	uninstall
o	--all	Remove .dapr directory, Redis, Placement and Zipkin containers on local machine, and CRDs on a…	
o	--container-runtime	The container runtime to use. Supported values are docker (default) and podman	v
o	--dev	Uninstall Dapr Redis and Zipking installations from Kubernetes cluster	
o	--help|-h	Print this help message	
o	--kubernetes|-k	Uninstall Dapr from a Kubernetes cluster	
o	--namespace|-n	The Kubernetes namespace to uninstall Dapr from	v
o	--network	The Docker network from which to remove the Dapr runtime	v
o	--timeout	The timeout for the Kubernetes uninstall	v
@	upgrade
o	--dashboard-version	The version of the Dapr dashboard to upgrade or downgrade to, for example: 0.13.0	v
o	--help|-h	Print this help message	
o	--image-registry	Custom/Private docker image repository URL	v
o	--image-variant	The image variant to use for the Dapr runtime, for example: mariner	v
o	--kubernetes|-k	Upgrade or downgrade Dapr in a Kubernetes cluster	
o	--runtime-version	The version of the Dapr runtime to upgrade or downgrade to, for example: 1.0.0	v
o	--set	Set values on the command line (can specify multiple or separate values with commas…	v
o	--timeout	The timeout for the Kubernetes upgrade	v
@	version
o	--help|-h	Print this help message	
o	--output|-o	The output format of the version command. Valid values are: json	v
=	version	--output
v	json	
@	help
s	annotate	Add dapr annotations to a Kubernetes configuration. Supported platforms: Kubernetes
s	build-info	Print build info of Dapr CLI and runtime
s	completion	Generates shell completion scripts
s	components	List all Dapr components. Supported platforms: Kubernetes
s	configurations	List all Dapr configurations. Supported platforms: Kubernetes
s	dashboard	Start Dapr dashboard. Supported platforms: Kubernetes and self-hosted
s	init	Install Dapr on supported hosting platforms. Supported platforms: Kubernetes and self-hosted
s	invoke	Invoke a method on a given Dapr application. Supported platforms: Self-hosted
s	list	List all Dapr instances. Supported platforms: Kubernetes and self-hosted
s	logs	Get Dapr sidecar logs for an application. Supported platforms: Kubernetes
s	mtls	Check if mTLS is enabled. Supported platforms: Kubernetes
s	publish	Publish a pub-sub event. Supported platforms: Self-hosted
s	run	Run Dapr and (optionally) your application side by side. Supported platforms: Self-hosted
s	status	Show the health status of Dapr services. Supported platforms: Kubernetes
s	stop	Stop Dapr instances and their associated apps. Supported platforms: Self-hosted
s	uninstall	Uninstall Dapr runtime. Supported platforms: Kubernetes and self-hosted
s	upgrade	Upgrades or downgrades a Dapr control plane installation in a cluster. Supported platforms…
s	version	Print the Dapr runtime and CLI version
@	help annotate
@	help build-info
@	help completion
s	bash	Generates bash completion scripts
s	fish	Generates fish completion scripts
s	powershell	Generates powershell completion scripts
s	zsh	Generates zsh completion scripts
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh
@	help components
@	help configurations
@	help dashboard
@	help init
@	help invoke
@	help list
@	help logs
@	help mtls
s	expiry	Checks the expiry of the root certificate
s	export	Export the root CA, issuer cert and key from Kubernetes to local files
s	renew-cert|rnc|renew-certificate	Rotates the Dapr root certificate on your Kubernetes cluster
@	help mtls expiry
@	help mtls export
@	help mtls renew-cert
@	help publish
@	help run
@	help status
@	help stop
@	help uninstall
@	help upgrade
@	help version
