@	
s	completion	Generate autocompletion scripts for the specified shell
s	create	Create a new chart with the given name
s	dep|dependencies|dependency	Manage a chart's dependencies
s	env	Helm client environment information
s	get	Download extended information of a named release
s	hist|history	Fetch release history
s	install	Install a chart
s	lint	Examine a chart for possible issues
s	ls|list	List releases
s	package	Package a chart directory into a chart archive
s	plugin	Install, list, or uninstall Helm plugins
s	fetch|pull	Download a chart from a repository and (optionally) unpack it in local directory
s	push	Push a chart to remote
s	registry	Login to or logout from a registry
s	repo	Add, list, remove, update, and index chart repositories
s	rollback	Roll back a release to a previous revision
s	s3	Manage chart repositories on Amazon S3
s	search	Search for a keyword in charts
s	inspect|show	Show information of a chart
s	status	Display the status of the named release
s	template	Locally render templates
s	test	Run tests for a release
s	del|delete|un|uninstall	Uninstall a release
s	unittest	Unittest for helm charts
s	upgrade	Upgrade a release
s	verify	Verify that a chart at the given path has been signed and is valid
s	version	Print the client version information
s	help	Help about any command
o	--burst-limit	Client-side default throttling limit	vp
o	--debug	Enable verbose output	p
o	--kube-apiserver	The address and the port for the Kubernetes API server	vp
o	--kube-as-group	Group to impersonate for the operation, this flag can be repeated to specify multiple groups	vp
o	--kube-as-user	Username to impersonate for the operation	vp
o	--kube-ca-file	The certificate authority file for the Kubernetes API server connection	vp
o	--kube-context	Name of the kubeconfig context to use	vp
o	--kube-insecure-skip-tls-verify	If true, the Kubernetes API server's certificate will not be checked for validity. This will make…	p
o	--kube-tls-server-name	Server name to use for Kubernetes API server certificate validation. If it is not provided, the…	vp
o	--kube-token	Bearer token used for authentication	vp
o	--kubeconfig	Path to the kubeconfig file	vp
o	--namespace|-n	Namespace scope for this request	vp
o	--registry-config	Path to the registry config file	vp
o	--repository-cache	Path to the file containing cached repository indexes	vp
o	--repository-config	Path to the file containing repository names and URLs	vp
o	--help|-h	Display help	p
=		--kube-ca-file
t	filepaths
=		--kubeconfig
t	filepaths
=		--registry-config
t	filepaths
=		--repository-cache
t	filepaths
=		--repository-config
t	filepaths
@	completion
s	bash	Generate autocompletion script for bash
s	fish	Generate autocompletion script for fish
s	powershell	Generate autocompletion script for powershell
s	zsh	Generate autocompletion script for zsh
@	completion bash
o	--no-descriptions	Disable completion descriptions	
@	completion fish
o	--no-descriptions	Disable completion descriptions	
@	completion powershell
o	--no-descriptions	Disable completion descriptions	
@	completion zsh
o	--no-descriptions	Disable completion descriptions	
@	create
o	--starter|-p	The name or absolute path to Helm starter scaffold	v
@	dep
s	build	Rebuild the charts/ directory based on the Chart.lock file
s	ls|list	List the dependencies for the given chart
s	up|update	Update charts/ based on the contents of Chart.yaml
@	dep build
o	--keyring	Keyring containing public keys	v
o	--skip-refresh	Do not refresh the local repository cache	
o	--verify	Verify the packages against signatures	
=	dep build	--keyring
t	filepaths
@	dep ls
o	--max-col-width	Maximum column width for output table	v
@	dep up
o	--keyring	Keyring containing public keys	v
o	--skip-refresh	Do not refresh the local repository cache	
o	--verify	Verify the packages against signatures	
=	dep up	--keyring
t	filepaths
@	env
@	get
s	all	Download all information for a named release
s	hooks	Download all hooks for a named release
s	manifest	Download the manifest for a named release
s	notes	Download the notes for a named release
s	values	Download the values file for a named release
@	get all
o	--revision	Get the named release with revision	v
o	--template	Go template for formatting the output, eg: {{.Release.Name}}	v
@	get hooks
o	--revision	Get the named release with revision	v
@	get manifest
o	--revision	Get the named release with revision	v
@	get notes
o	--revision	Get the named release with revision	v
@	get values
o	--all|-a	Dump all (computed) values	
o	--output|-o	Prints the output in the specified format. Allowed values: table, json, yaml	v
o	--revision	Get the named release with revision	v
@	hist
o	--max	Maximum number of revision to include in history	v
o	--output|-o	Prints the output in the specified format. Allowed values: table, json, yaml	v
@	install
o	--atomic	If set, the installation process deletes the installation on failure. The --wait flag will be set…	
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--create-namespace	Create the release namespace if not present	
o	--dependency-update	Update dependencies if they are missing before installing the chart	
o	--description	Add a custom description	v
o	--devel	Use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is…	
o	--disable-openapi-validation	If set, the installation process will not validate rendered templates against the Kubernetes…	
o	--dry-run	Simulate an install	
o	--generate-name|-g	Generate the name (and omit the NAME parameter)	
o	--insecure-skip-tls-verify	Skip tls certificate checks for the chart download	
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--keyring	Location of public keys used for verification	v
o	--name-template	Specify template used to name the release	v
o	--no-hooks	Prevent hooks from running during install	
o	--output|-o	Prints the output in the specified format. Allowed values: table, json, yaml	v
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password where to locate the requested chart	v
o	--post-renderer	The path to an executable to be used for post rendering. If it exists in $PATH, the binary will be…	v
o	--post-renderer-args	An argument to the post-renderer (can specify multiple)	v
o	--render-subchart-notes	If set, render subchart notes along with the parent	
o	--replace	Re-use the given name, only if that name is a deleted release which remains in the history. This…	
o	--repo	Chart repository url where to locate the requested chart	v
o	--set	Set values on the command line (can specify multiple or separate values with commas…	v
o	--set-file	Set values from respective files specified via the command line (can specify multiple or separate…	v
o	--set-string	Set STRING values on the command line (can specify multiple or separate values with commas…	v
o	--skip-crds	If set, no CRDs will be installed. By default, CRDs are installed if not already present	
o	--timeout	Time to wait for any individual Kubernetes operation (like Jobs for hooks)	v
o	--username	Chart repository username where to locate the requested chart	v
o	--values|-f	Specify values in a YAML file or a URL (can specify multiple)	v
o	--verify	Verify the package before using it	
o	--version	Specify a version constraint for the chart version to use. This constraint can be a specific tag…	v
o	--wait	If set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment…	
o	--wait-for-jobs	If set and --wait enabled, will wait until all Jobs have been completed before marking the release…	
=	install	--ca-file
t	filepaths
=	install	--cert-file
t	filepaths
=	install	--key-file
t	filepaths
=	install	--keyring
t	filepaths
=	install	--set-file
t	filepaths
=	install	--values
t	filepaths
@	lint
o	--quiet	Print only warnings and errors	
o	--set	Set values on the command line (can specify multiple or separate values with commas…	v
o	--set-file	Set values from respective files specified via the command line (can specify multiple or separate…	v
o	--set-string	Set STRING values on the command line (can specify multiple or separate values with commas…	v
o	--strict	Fail on lint warnings	
o	--values|-f	Specify values in a YAML file or a URL (can specify multiple)	v
o	--with-subcharts	Lint dependent charts	
=	lint	--set-file
t	filepaths
=	lint	--values
t	filepaths
@	ls
o	--all|-a	Show all releases without any filter applied	
o	--all-namespaces|-A	List releases across all namespaces	
o	--date|-d	Sort by release date	
o	--deployed	Show deployed releases. If no other is specified, this will be automatically enabled	
o	--failed	Show failed releases	
o	--filter|-f	A regular expression (Perl compatible). Any releases that match the expression will be included in…	v
o	--max|-m	Maximum number of releases to fetch	v
o	--no-headers	Don't print headers when using the default output format	
o	--offset	Next release index in the list, used to offset from start value	v
o	--output|-o	Prints the output in the specified format. Allowed values: table, json, yaml	v
o	--pending	Show pending releases	
o	--reverse|-r	Reverse the sort order	
o	--selector|-l	Selector (label query) to filter on, supports '=', '==', and '!='.(e.g. -l…	v
o	--short|-q	Output short (quiet) listing format	
o	--superseded	Show superseded releases	
o	--time-format	Format time using golang time formatter. Example: --time-format "2006-01-02 15:04:05Z0700"	v
o	--uninstalled	Show uninstalled releases (if 'helm uninstall --keep-history' was used)	
o	--uninstalling	Show releases that are currently being uninstalled	
@	package
o	--app-version	Set the appVersion on the chart to this version	v
o	--dependency-update|-u	Update dependencies from "Chart.yaml" to dir "charts/" before packaging	
o	--destination|-d	Location to write the chart	v
o	--key	Name of the key to use when signing. Used if --sign is true	v
o	--keyring	Location of a public keyring	v
o	--passphrase-file	Location of a file which contains the passphrase for the signing key. Use "-" in order to read…	v
o	--sign	Use a PGP private key to sign this package	
o	--version	Set the version on the chart to this semver version	v
=	package	--keyring
t	filepaths
=	package	--passphrase-file
t	filepaths
@	plugin
s	add|install	Install one or more Helm plugins
s	ls|list	List installed Helm plugins
s	rm|remove|uninstall	Uninstall one or more Helm plugins
s	up|update	Update one or more Helm plugins
@	plugin add
o	--version	Specify a version constraint. If this is not specified, the latest version is installed	v
@	plugin ls
@	plugin rm
@	plugin up
@	fetch
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--destination|-d	Location to write the chart. If this and untardir are specified, untardir is appended to this	v
o	--devel	Use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is…	
o	--insecure-skip-tls-verify	Skip tls certificate checks for the chart download	
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--keyring	Location of public keys used for verification	v
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password where to locate the requested chart	v
o	--prov	Fetch the provenance file, but don't perform verification	
o	--repo	Chart repository url where to locate the requested chart	v
o	--untar	If set to true, will untar the chart after downloading it	
o	--untardir	If untar is specified, this flag specifies the name of the directory into which the chart is…	v
o	--username	Chart repository username where to locate the requested chart	v
o	--verify	Verify the package before using it	
o	--version	Specify a version constraint for the chart version to use. This constraint can be a specific tag…	v
=	fetch	--ca-file
t	filepaths
=	fetch	--cert-file
t	filepaths
=	fetch	--key-file
t	filepaths
=	fetch	--keyring
t	filepaths
=	fetch	--untardir
t	filepaths
@	push
@	registry
s	login	Login to a registry
s	logout	Logout from a registry
@	registry login
o	--insecure	Allow connections to TLS registry without certs	
o	--password|-p	Registry password or identity token	v
o	--password-stdin	Read password or identity token from stdin	
o	--username|-u	Registry username	v
@	registry logout
@	repo
s	add	Add a chart repository
s	index	Generate an index file given a directory containing packaged charts
s	ls|list	List chart repositories
s	rm|remove	Remove one or more chart repositories
s	up|update	Update information of available charts locally from chart repositories
@	repo add
o	--allow-deprecated-repos	By default, this command will not allow adding official repos that have been permanently deleted…	
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--force-update	Replace (overwrite) the repo if it already exists	
o	--insecure-skip-tls-verify	Skip tls certificate checks for the repository	
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--no-update	Ignored. Formerly, it would disabled forced updates. It is deprecated by force-update	
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password	v
o	--password-stdin	Read chart repository password from stdin	
o	--username	Chart repository username	v
=	repo add	--ca-file
t	filepaths
=	repo add	--cert-file
t	filepaths
=	repo add	--key-file
t	filepaths
@	repo index
o	--merge	Merge the generated index into the given index	v
o	--url	Url of chart repository	v
@	repo ls
o	--output|-o	Prints the output in the specified format. Allowed values: table, json, yaml	v
@	repo rm
@	repo up
o	--fail-on-repo-update-fail	Update fails if any of the repository updates fail	
@	rollback
o	--cleanup-on-fail	Allow deletion of new resources created in this rollback when rollback fails	
o	--dry-run	Simulate a rollback	
o	--force	Force resource update through delete/recreate if needed	
o	--history-max	Limit the maximum number of revisions saved per release. Use 0 for no limit	v
o	--no-hooks	Prevent hooks from running during rollback	
o	--recreate-pods	Performs pods restart for the resource if applicable	
o	--timeout	Time to wait for any individual Kubernetes operation (like Jobs for hooks)	v
o	--wait	If set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment…	
o	--wait-for-jobs	If set and --wait enabled, will wait until all Jobs have been completed before marking the release…	
@	s3
@	search
s	hub	Search for charts in the Artifact Hub or your own hub instance
s	repo	Search repositories for a keyword in charts
@	search hub
o	--endpoint	Hub instance to query for charts	v
o	--list-repo-url	Print charts repository URL	
o	--max-col-width	Maximum column width for output table	v
o	--output|-o	Prints the output in the specified format. Allowed values: table, json, yaml	v
@	search repo
o	--devel	Use development versions (alpha, beta, and release candidate releases), too. Equivalent to version…	
o	--max-col-width	Maximum column width for output table	v
o	--output|-o	Prints the output in the specified format. Allowed values: table, json, yaml	v
o	--regexp|-r	Use regular expressions for searching repositories you have added	
o	--version	Search using semantic versioning constraints on repositories you have added	v
o	--versions|-l	Show the long listing, with each version of each chart on its own line, for repositories you have…	
@	inspect
s	all	Show all information of the chart
s	chart	Show the chart's definition
s	crds	Show the chart's CRDs
s	readme	Show the chart's README
s	values	Show the chart's values
@	inspect all
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--devel	Use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is…	
o	--insecure-skip-tls-verify	Skip tls certificate checks for the chart download	
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--keyring	Location of public keys used for verification	v
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password where to locate the requested chart	v
o	--repo	Chart repository url where to locate the requested chart	v
o	--username	Chart repository username where to locate the requested chart	v
o	--verify	Verify the package before using it	
o	--version	Specify a version constraint for the chart version to use. This constraint can be a specific tag…	v
=	inspect all	--ca-file
t	filepaths
=	inspect all	--cert-file
t	filepaths
=	inspect all	--key-file
t	filepaths
=	inspect all	--keyring
t	filepaths
@	inspect chart
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--devel	Use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is…	
o	--insecure-skip-tls-verify	Skip tls certificate checks for the chart download	
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--keyring	Location of public keys used for verification	v
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password where to locate the requested chart	v
o	--repo	Chart repository url where to locate the requested chart	v
o	--username	Chart repository username where to locate the requested chart	v
o	--verify	Verify the package before using it	
o	--version	Specify a version constraint for the chart version to use. This constraint can be a specific tag…	v
=	inspect chart	--ca-file
t	filepaths
=	inspect chart	--cert-file
t	filepaths
=	inspect chart	--keyring
t	filepaths
@	inspect crds
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--devel	Use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is…	
o	--insecure-skip-tls-verify	Skip tls certificate checks for the chart download	
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--keyring	Location of public keys used for verification	v
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password where to locate the requested chart	v
o	--repo	Chart repository url where to locate the requested chart	v
o	--username	Chart repository username where to locate the requested chart	v
o	--verify	Verify the package before using it	
o	--version	Specify a version constraint for the chart version to use. This constraint can be a specific tag…	v
=	inspect crds	--ca-file
t	filepaths
=	inspect crds	--cert-file
t	filepaths
=	inspect crds	--key-file
t	filepaths
=	inspect crds	--keyring
t	filepaths
@	inspect readme
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--devel	Use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is…	
o	--insecure-skip-tls-verify	Skip tls certificate checks for the chart download	
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--keyring	Location of public keys used for verification	v
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password where to locate the requested chart	v
o	--repo	Chart repository url where to locate the requested chart	v
o	--username	Chart repository username where to locate the requested chart	v
o	--verify	Verify the package before using it	
o	--version	Specify a version constraint for the chart version to use. This constraint can be a specific tag…	v
=	inspect readme	--ca-file
t	filepaths
=	inspect readme	--cert-file
t	filepaths
@	inspect values
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--devel	Use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is…	
o	--insecure-skip-tls-verify	Skip tls certificate checks for the chart download	
o	--jsonpath	Supply a JSONPath expression to filter the output	v
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--keyring	Location of public keys used for verification	v
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password where to locate the requested chart	v
o	--repo	Chart repository url where to locate the requested chart	v
o	--username	Chart repository username where to locate the requested chart	v
o	--verify	Verify the package before using it	
o	--version	Specify a version constraint for the chart version to use. This constraint can be a specific tag…	v
=	inspect values	--ca-file
t	filepaths
=	inspect values	--cert-file
t	filepaths
=	inspect values	--key-file
t	filepaths
=	inspect values	--keyring
t	filepaths
@	status
o	--output|-o	Prints the output in the specified format. Allowed values: table, json, yaml	v
o	--revision	If set, display the status of the named release with revision	v
o	--show-desc	If set, display the description message of the named release	
@	template
o	--api-versions|-a	Kubernetes api versions used for Capabilities.APIVersions	v
o	--atomic	If set, the installation process deletes the installation on failure. The --wait flag will be set…	
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--create-namespace	Create the release namespace if not present	
o	--dependency-update	Update dependencies if they are missing before installing the chart	
o	--description	Add a custom description	v
o	--devel	Use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is…	
o	--disable-openapi-validation	If set, the installation process will not validate rendered templates against the Kubernetes…	
o	--dry-run	Simulate an install	
o	--generate-name|-g	Generate the name (and omit the NAME parameter)	
o	--include-crds	Include CRDs in the templated output	
o	--insecure-skip-tls-verify	Skip tls certificate checks for the chart download	
o	--is-upgrade	Set .Release.IsUpgrade instead of .Release.IsInstall	
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--keyring	Location of public keys used for verification	v
o	--kube-version	Kubernetes version used for Capabilities.KubeVersion	v
o	--name-template	Specify template used to name the release	v
o	--no-hooks	Prevent hooks from running during install	
o	--output-dir	Writes the executed templates to files in output-dir instead of stdout	v
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password where to locate the requested chart	v
o	--post-renderer	The path to an executable to be used for post rendering. If it exists in $PATH, the binary will be…	v
o	--post-renderer-args	An argument to the post-renderer (can specify multiple)	v
o	--release-name	Use release name in the output-dir path	
o	--render-subchart-notes	If set, render subchart notes along with the parent	
o	--replace	Re-use the given name, only if that name is a deleted release which remains in the history. This…	
o	--repo	Chart repository url where to locate the requested chart	v
o	--set	Set values on the command line (can specify multiple or separate values with commas…	v
o	--set-file	Set values from respective files specified via the command line (can specify multiple or separate…	v
o	--set-string	Set STRING values on the command line (can specify multiple or separate values with commas…	v
o	--show-only|-s	Only show manifests rendered from the given templates	v
o	--skip-crds	If set, no CRDs will be installed. By default, CRDs are installed if not already present	
o	--skip-tests	Skip tests from templated output	
o	--timeout	Time to wait for any individual Kubernetes operation (like Jobs for hooks)	v
o	--username	Chart repository username where to locate the requested chart	v
o	--validate	Validate your manifests against the Kubernetes cluster you are currently pointing at. This is the…	
o	--values|-f	Specify values in a YAML file or a URL (can specify multiple)	v
o	--verify	Verify the package before using it	
o	--version	Specify a version constraint for the chart version to use. This constraint can be a specific tag…	v
o	--wait	If set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment…	
o	--wait-for-jobs	If set and --wait enabled, will wait until all Jobs have been completed before marking the release…	
=	template	--ca-file
t	filepaths
=	template	--cert-file
t	filepaths
=	template	--key-file
t	filepaths
=	template	--keyring
t	filepaths
=	template	--output-dir
t	filepaths
=	template	--set-file
t	filepaths
=	template	--values
t	filepaths
@	test
o	--filter	Specify tests by attribute (currently "name") using attribute=value syntax or '!attribute=value'…	v
o	--logs	Dump the logs from test pods (this runs after all tests are complete, but before any cleanup)	
o	--timeout	Time to wait for any individual Kubernetes operation (like Jobs for hooks)	v
@	del
o	--description	Add a custom description	v
o	--dry-run	Simulate a uninstall	
o	--keep-history	Remove all associated resources and mark the release as deleted, but retain the release history	
o	--no-hooks	Prevent hooks from running during uninstallation	
o	--timeout	Time to wait for any individual Kubernetes operation (like Jobs for hooks)	v
o	--wait	If set, will wait until all the resources are deleted before returning. It will wait for as long…	
@	unittest
@	upgrade
o	--atomic	If set, upgrade process rolls back changes made in case of failed upgrade. The --wait flag will be…	
o	--ca-file	Verify certificates of HTTPS-enabled servers using this CA bundle	v
o	--cert-file	Identify HTTPS client using this SSL certificate file	v
o	--cleanup-on-fail	Allow deletion of new resources created in this upgrade when upgrade fails	
o	--create-namespace	If --install is set, create the release namespace if not present	
o	--dependency-update	Update dependencies if they are missing before installing the chart	
o	--description	Add a custom description	v
o	--devel	Use development versions, too. Equivalent to version '>0.0.0-0'. If --version is set, this is…	
o	--disable-openapi-validation	If set, the upgrade process will not validate rendered templates against the Kubernetes OpenAPI…	
o	--dry-run	Simulate an upgrade	
o	--force	Force resource updates through a replacement strategy	
o	--history-max	Limit the maximum number of revisions saved per release. Use 0 for no limit	v
o	--insecure-skip-tls-verify	Skip tls certificate checks for the chart download	
o	--install|-i	If a release by this name doesn't already exist, run an install	
o	--key-file	Identify HTTPS client using this SSL key file	v
o	--keyring	Location of public keys used for verification	v
o	--no-hooks	Disable pre/post upgrade hooks	
o	--output|-o	Prints the output in the specified format. Allowed values: table, json, yaml	v
o	--pass-credentials	Pass credentials to all domains	
o	--password	Chart repository password where to locate the requested chart	v
o	--post-renderer	The path to an executable to be used for post rendering. If it exists in $PATH, the binary will be…	v
o	--post-renderer-args	An argument to the post-renderer (can specify multiple)	v
o	--render-subchart-notes	If set, render subchart notes along with the parent	
o	--repo	Chart repository url where to locate the requested chart	v
o	--reset-values	When upgrading, reset the values to the ones built into the chart	
o	--reuse-values	When upgrading, reuse the last release's values and merge in any overrides from the command line…	
o	--set	Set values on the command line (can specify multiple or separate values with commas…	v
o	--set-file	Set values from respective files specified via the command line (can specify multiple or separate…	v
o	--set-string	Set STRING values on the command line (can specify multiple or separate values with commas…	v
o	--skip-crds	If set, no CRDs will be installed when an upgrade is performed with install flag enabled. By…	
o	--timeout	Time to wait for any individual Kubernetes operation (like Jobs for hooks)	v
o	--username	Chart repository username where to locate the requested chart	v
o	--values|-f	Specify values in a YAML file or a URL (can specify multiple)	v
o	--verify	Verify the package before using it	
o	--version	Specify a version constraint for the chart version to use. This constraint can be a specific tag…	v
o	--wait	If set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment…	
o	--wait-for-jobs	If set and --wait enabled, will wait until all Jobs have been completed before marking the release…	
=	upgrade	--ca-file
t	filepaths
=	upgrade	--cert-file
t	filepaths
=	upgrade	--key-file
t	filepaths
=	upgrade	--keyring
t	filepaths
=	upgrade	--set-file
t	filepaths
=	upgrade	--values
t	filepaths
@	verify
o	--keyring	Keyring containing public keys	v
=	verify	--keyring
t	filepaths
@	version
o	--short	Print the version number	
o	--template	Template for version string format	v
@	help
s	completion	Generate autocompletion scripts for the specified shell
s	create	Create a new chart with the given name
s	dep|dependencies|dependency	Manage a chart's dependencies
s	env	Helm client environment information
s	get	Download extended information of a named release
s	hist|history	Fetch release history
s	install	Install a chart
s	lint	Examine a chart for possible issues
s	ls|list	List releases
s	package	Package a chart directory into a chart archive
s	plugin	Install, list, or uninstall Helm plugins
s	fetch|pull	Download a chart from a repository and (optionally) unpack it in local directory
s	push	Push a chart to remote
s	registry	Login to or logout from a registry
s	repo	Add, list, remove, update, and index chart repositories
s	rollback	Roll back a release to a previous revision
s	s3	Manage chart repositories on Amazon S3
s	search	Search for a keyword in charts
s	inspect|show	Show information of a chart
s	status	Display the status of the named release
s	template	Locally render templates
s	test	Run tests for a release
s	del|delete|un|uninstall	Uninstall a release
s	unittest	Unittest for helm charts
s	upgrade	Upgrade a release
s	verify	Verify that a chart at the given path has been signed and is valid
s	version	Print the client version information
@	help completion
s	bash	Generate autocompletion script for bash
s	fish	Generate autocompletion script for fish
s	powershell	Generate autocompletion script for powershell
s	zsh	Generate autocompletion script for zsh
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh
@	help create
@	help dep
s	build	Rebuild the charts/ directory based on the Chart.lock file
s	ls|list	List the dependencies for the given chart
s	up|update	Update charts/ based on the contents of Chart.yaml
@	help dep build
@	help dep ls
@	help dep up
@	help env
@	help get
s	all	Download all information for a named release
s	hooks	Download all hooks for a named release
s	manifest	Download the manifest for a named release
s	notes	Download the notes for a named release
s	values	Download the values file for a named release
@	help get all
@	help get hooks
@	help get manifest
@	help get notes
@	help get values
@	help hist
@	help install
@	help lint
@	help ls
@	help package
@	help plugin
s	add|install	Install one or more Helm plugins
s	ls|list	List installed Helm plugins
s	rm|remove|uninstall	Uninstall one or more Helm plugins
s	up|update	Update one or more Helm plugins
@	help plugin add
@	help plugin ls
@	help plugin rm
@	help plugin up
@	help fetch
@	help push
@	help registry
s	login	Login to a registry
s	logout	Logout from a registry
@	help registry login
@	help registry logout
@	help repo
s	add	Add a chart repository
s	index	Generate an index file given a directory containing packaged charts
s	ls|list	List chart repositories
s	rm|remove	Remove one or more chart repositories
s	up|update	Update information of available charts locally from chart repositories
@	help repo add
@	help repo index
@	help repo ls
@	help repo rm
@	help repo up
@	help rollback
@	help s3
@	help search
s	hub	Search for charts in the Artifact Hub or your own hub instance
s	repo	Search repositories for a keyword in charts
@	help search hub
@	help search repo
@	help inspect
s	all	Show all information of the chart
s	chart	Show the chart's definition
s	crds	Show the chart's CRDs
s	readme	Show the chart's README
s	values	Show the chart's values
@	help inspect all
@	help inspect chart
@	help inspect crds
@	help inspect readme
@	help inspect values
@	help status
@	help template
@	help test
@	help del
@	help unittest
@	help upgrade
@	help verify
@	help version
