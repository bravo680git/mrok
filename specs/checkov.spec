@	
o	--help|-h	Show help for checkov	
o	--version|-v	Show the version of checkov	
o	--quiet	CLI output, display only failed checks	
o	--compact	CLI output, do not display code blocks	
o	--list|-l	List checks	
o	--no-guide	Do not fetch Bridgecrew platform IDs and guidelines for the checkov output report. Note: this…	
o	--output-bc-ids	Print Bridgecrew platform IDs (BC...) instead of Checkov IDs (CKV...), if the check exists in the…	
o	--directory|-d	IaC root directory (can not be used together with --file)	v
o	--output|-o	Report output format. Add multiple outputs by using the flag multiple times (-o sarif -o cli)	v
o	--framework	IaC frameworks to include checks for	v
o	--skip-framework	IaC frameworks to exclude checks for	v
o	--add-check	Generate a new check via CLI prompt	
o	--file|-f	IaC file(can not be used together with --directory)	v
o	--skip-path	Path (file or directory) to skip, using regular expression logic, relative to current working…	v
o	--check|-c	Filter scan to run only on a specific check identifier (allowlist). You can specify multiple…	v
o	--skip-check	Filter scan to run all check except a specific check identifier (denylist). You can specify…	v
o	--run-all-external-checks	Run all external checks (loaded via --external-checks options) even if the checks are not present…	
o	--external-checks-dir	Directory for custom checks to be loaded. Can be repeated	v
o	--bc-api-key	Bridgecrew API key. You may also use the environment variable: BC_API_KEY	v
o	--docker-image	Scan docker images by name or ID. Only works with --bc-api-key flag	v
o	--dockerfile-path	Path to the Dockerfile of the scanned docker image	v
o	--repo-id	Identity string of the repository, with form <repo_owner>/<repo_name>	v
o	--branch|-b	Selected branch of the persisted repository. Only has effect when using the --bc-api-key flag	v
o	--skip-fixes	Do not download fixed resource templates from Bridgecrew. Only has an effect when using the…	
o	--skip-suppressions	Do not download preconfigured suppressions from the Bridgecrew platform. Code comment suppressions…	
o	--skip-policy-download	Do not download custom policies configured in the Bridgecrew platform. Only has an effect when…	
o	--download-external-modules	Download external terraform modules from public git repositories and terraform registry. You may…	v
o	--var-file	Variable files to load in addition to the default files (see https://www.terraform.io/docs/language…	v
o	--external-modules-download-path	Set the path for the download external terraform modules. You may also use the environment…	v
o	--evaluate-variables	Evaluate the values of variables and locals	v
o	--ca-certificate|-ca	Custom CA (bundle) fila. You may also use the environment variablee: CA_CERTIFICATE	v
o	--repo-root-for-plan-enrichment	Directory containing the hcl code used to generate a given plan file. Use with -f FILE	v
o	--config-file	Path to the Checkov configuration YAML file	v
o	--create-config	Takes the current command line args and writes them out to a config file at the given path	v
o	--show-config	Prints all arguments and config settings and where they came from (eg. commandline, config file…	
o	--create-baseline	Save all current results to a '.checkov.baseline' file so future runs will only flag new findings…	
o	--baseline	Use a '.checkov.baseline' file to compare current results with a known baseline. Report will…	v
o	--soft-fail|-s	Runs checks but suppresses the error code	
o	--soft-fail-on	Exits with a 0 exit code for specified checks. You can specify multiple checks separated by comma…	v
o	--hard-fail-on	Exits with a non-zero exit code for specified checks. You can specify multiple checks separated by…	v
o	--min-cve-severity	Set minimum severity to return a non-zero exit code	v
o	--skip-cve-package	Ignore specific open source package when SCA scanning for CVEs in package dependencies. Can be…	v
o	--use-enforcement-rules	Use the Enforcement rules configured in the platform for hard / soft fail logic	v
o	--support	Enable debug logs and upload the logs to the server	v
o	--summary-position	Chose whether the summary will be appended on top or on bottom	v
o	--skip-resources-without-violations	Exclude extra resources (resources without violations)	v
o	--skip-download	Do not download any data from Prisma Cloud	v
o	--secrets-history-timeout	Maximum time to run the history scan	v
o	--scan-secrets-history	Will scan the history of commits for secrets	v
o	--prisma-api-url	The Prisma Cloud API URL	v
o	--policy-metadata-filter	Comma separated key:value string to filter policies based on Prisma Cloud policy metadata	v
o	--output-file-path	Name of the output folder to save the chosen output formats	v
o	--output-baseline-as-skipped	Output checks that are skipped due to baseline file presence	v
o	--openai-api-key	Add an OpenAI API key to enhance finding guidelines. This will send Code to OpenAI	v
o	--no-fail-on-crash	Return exit code 0 instead of 2	v
o	--mask	Each entry in the list will be used for masking the desired attribute	v
o	--include-all-checkov-policies	When running with an API key, Checkov will omit any policies that do not exist in the Bridgecrew…	v
o	--external-checks-git	GitHub URL of external checks to be added	v
o	--enable-secret-scan-all-files	Enable secret scan for all files	v
o	--deep-analysis	Enable combine TF graph and TF Plan graph	v
o	--block-list-secret-scan	List of files to filter out from the secret scanner	v
=		--directory
t	folders
=		--output
v	cli	
v	cyclonedx	
v	json	
v	junitxml	
v	github_failed_only	
v	sarif	
=		--framework
v	arm	
v	cloudformation	
v	dockerfile	
v	github_configuration	
v	gitlab_configuration	
v	helm	
v	json	
v	kubernetes	
v	kustomize	
v	sca_package	
v	secrets	
v	serverless	
v	terraform	
v	terraform_plan	
v	all	
=		--skip-framework
v	arm	
v	cloudformation	
v	dockerfile	
v	github_configuration	
v	gitlab_configuration	
v	helm	
v	json	
v	kubernetes	
v	kustomize	
v	sca_package	
v	secrets	
v	serverless	
v	terraform	
v	terraform_plan	
v	all	
=		--file
t	filepaths
=		--skip-path
t	filepaths
=		--branch
d
=		--config-file
t	filepaths
=		--min-cve-severity
v	critical	
v	high	
v	medium	
v	low	
v	none	
=		--summary-position
v	top	
v	bottom	
