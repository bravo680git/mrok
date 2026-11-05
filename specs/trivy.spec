@	
s	image|i	Scan an image
s	filesystem|fs	Scan local filesystem for language-specific dependencies and config files
s	rootfs	Scan rootfs
s	sbom	Generate SBOM for an artifact
s	repository|repo	Scan remote repository
s	client|c	Client mode
s	server|s	Server mode
s	config|conf	Scan config files
s	plugin|p	Manage plugins
s	version	Print the version
s	help|h	Shows a list of commands or help for one command
o	--quiet|-q	Suppress progress bar and log output [$TRIVY_QUIET]	
o	--debug|-d	Enable debug output [$TRIVY_DEBUG]	
o	--cache-dir	Cache directory [$TRIVY_CACHE_DIR]	v
o	--help|-h	Show help	p
o	--version|-v	Print the version	
=		--cache-dir
t	folders
@	image
s	--template|-t	Output template [$TRIVY_TEMPLATE]
s	--format|-f	Format (table, json, sarif, template) (default: "table") [$TRIVY_FORMAT]
s	--severity|-s	Severities of vulnerabilities to be displayed (comma separated) (default…
s	--output|-o	Output file name [$TRIVY_OUTPUT]
s	--exit-code	Exit code when vulnerabilities were found (default: 0) [$TRIVY_EXIT_CODE]
s	--clear-cache|-c	Clear image caches without scanning [$TRIVY_CLEAR_CACHE]
s	--vuln-type	Comma-separated list of vulnerability types (os,library) (default: "os,library") [$TRIVY_VULN_TYPE]
s	--security-checks	Comma-separated list of what security issues to detect (vuln,config) (default: "vuln")…
s	--ignorefile	Specify .trivyignore file (default: ".trivyignore") [$TRIVY_IGNOREFILE]]
s	--timeout	Timeout (default: 5m0s) [$TRIVY_TIMEOUT]
s	--ignore-policy	Specify the Rego file to evaluate each vulnerability [$TRIVY_IGNORE_POLICY]
s	--list-all-pkgs	Enabling the option will output all packages regardless of vulnerability (default: false)…
s	--cache-backend	Cache backend (e.g. redis://localhost:6379) (default: "fs") [$TRIVY_CACHE_BACKEND]
s	--no-progress	Suppress progress bar [$TRIVY_NO_PROGRESS]
s	--offline-scan	Do not issue API requests to identify dependencies [$TRIVY_OFFLINE_SCAN]
s	--skip-files	Specify the file paths to skip traversal [$TRIVY_SKIP_FILES]
s	--skip-dirs	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
s	--skip-db-update|--skip-update	Skip updating vulnerability database [$TRIVY_SKIP_UPDATE, $TRIVY_SKIP_DB_UPDATE]
s	--removed-pkgs	Detect vulnerabilities of removed packages (default: false) [$TRIVY_REMOVED_PKGS]
s	--input|-i	Input file path instead of image name [$TRIVY_INPUT]
s	--download-db-only	Download/update vulnerability database but don't run a scan [$TRIVY_DOWNLOAD_DB_ONLY]
s	--reset	Remove all caches and database [$TRIVY_RESET]
s	--ignore-unfixed	Display only fixed vulnerabilities [$TRIVY_IGNORE_UNFIXED]
s	--light	Deprecated [$TRIVY_LIGHT]
s	--insecure	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
a	1	0
@	image --template
a	1	0
@	image --format
a	1	0
#	image --format	1
v	table	
v	json	
v	sarif	
v	template	
@	image --severity
a	1	0
#	image --severity	1
d
@	image --output
a	1	0
#	image --output	1
t	filepaths
@	image --exit-code
a	1	0
@	image --clear-cache
@	image --vuln-type
a	1	0
#	image --vuln-type	1
d
@	image --security-checks
a	1	0
#	image --security-checks	1
d
@	image --ignorefile
a	1	0
#	image --ignorefile	1
t	filepaths
@	image --timeout
a	1	0
@	image --ignore-policy
a	1	0
#	image --ignore-policy	1
t	filepaths
@	image --list-all-pkgs
@	image --cache-backend
a	1	0
@	image --no-progress
@	image --offline-scan
@	image --skip-files
a	1	0
#	image --skip-files	1
t	filepaths
@	image --skip-dirs
a	1	0
#	image --skip-dirs	1
t	folders
@	image --skip-db-update
@	image --removed-pkgs
@	image --input
a	1	0
#	image --input	1
t	filepaths
@	image --download-db-only
@	image --reset
@	image --ignore-unfixed
@	image --light
@	image --insecure
@	filesystem
s	--template|-t	Output template [$TRIVY_TEMPLATE]
s	--format|-f	Format (table, json, sarif, template) (default: "table") [$TRIVY_FORMAT]
s	--severity|-s	Severities of vulnerabilities to be displayed (comma separated) (default…
s	--output|-o	Output file name [$TRIVY_OUTPUT]
s	--exit-code	Exit code when vulnerabilities were found (default: 0) [$TRIVY_EXIT_CODE]
s	--clear-cache|-c	Clear image caches without scanning [$TRIVY_CLEAR_CACHE]
s	--vuln-type	Comma-separated list of vulnerability types (os,library) (default: "os,library") [$TRIVY_VULN_TYPE]
s	--security-checks	Comma-separated list of what security issues to detect (vuln,config) (default: "vuln")…
s	--ignorefile	Specify .trivyignore file (default: ".trivyignore") [$TRIVY_IGNOREFILE]]
s	--timeout	Timeout (default: 5m0s) [$TRIVY_TIMEOUT]
s	--ignore-policy	Specify the Rego file to evaluate each vulnerability [$TRIVY_IGNORE_POLICY]
s	--list-all-pkgs	Enabling the option will output all packages regardless of vulnerability (default: false)…
s	--cache-backend	Cache backend (e.g. redis://localhost:6379) (default: "fs") [$TRIVY_CACHE_BACKEND]
s	--no-progress	Suppress progress bar [$TRIVY_NO_PROGRESS]
s	--offline-scan	Do not issue API requests to identify dependencies [$TRIVY_OFFLINE_SCAN]
s	--skip-files	Specify the file paths to skip traversal [$TRIVY_SKIP_FILES]
s	--skip-dirs	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
s	--skip-policy-update	Skip updating built-in policies [$TRIVY_SKIP_POLICY_UPDATE]
s	--ignore-unfixed	Display only fixed vulnerabilities [$TRIVY_IGNORE_UNFIXED]
s	--config-policy	Specify paths to the Rego policy files directory, applying config files [$TRIVY_CONFIG_POLICY]
s	--config-data	Specify paths from which data for the Rego policies will be recursively loaded [$TRIVY_CONFIG_DATA]
s	--policy-namespaces|--namespaces	Rego namespaces (default: "users") [$TRIVY_POLICY_NAMESPACES]
s	--skip-db-update|--skip-update	Skip updating vulnerability database [$TRIVY_SKIP_UPDATE, $TRIVY_SKIP_DB_UPDATE]
s	--server	Server address [$TRIVY_SERVER]
s	--token	For authentication in client/server mode [$TRIVY_TOKEN]
s	--token-header	Specify a header name for token in client/server mode (default: "Trivy-Token") [$TRIVY_TOKEN_HEADER]
s	--custom-headers	Custom headers in client/server mode [$TRIVY_CUSTOM_HEADERS]
a	1	0
#	filesystem	1
t	filepaths
@	filesystem --template
a	1	0
@	filesystem --format
a	1	0
#	filesystem --format	1
v	table	
v	json	
v	sarif	
v	template	
@	filesystem --severity
a	1	0
#	filesystem --severity	1
d
@	filesystem --output
a	1	0
#	filesystem --output	1
t	filepaths
@	filesystem --exit-code
a	1	0
@	filesystem --clear-cache
@	filesystem --vuln-type
a	1	0
#	filesystem --vuln-type	1
d
@	filesystem --security-checks
a	1	0
#	filesystem --security-checks	1
d
@	filesystem --ignorefile
a	1	0
#	filesystem --ignorefile	1
t	filepaths
@	filesystem --timeout
a	1	0
@	filesystem --ignore-policy
a	1	0
#	filesystem --ignore-policy	1
t	filepaths
@	filesystem --list-all-pkgs
@	filesystem --cache-backend
a	1	0
@	filesystem --no-progress
@	filesystem --offline-scan
@	filesystem --skip-files
a	1	0
#	filesystem --skip-files	1
t	filepaths
@	filesystem --skip-dirs
a	1	0
#	filesystem --skip-dirs	1
t	folders
@	filesystem --skip-policy-update
@	filesystem --ignore-unfixed
@	filesystem --config-policy
a	1	0
#	filesystem --config-policy	1
t	folders
@	filesystem --config-data
a	1	0
#	filesystem --config-data	1
t	folders
@	filesystem --policy-namespaces
a	1	0
@	filesystem --skip-db-update
@	filesystem --server
a	1	0
@	filesystem --token
a	1	0
@	filesystem --token-header
a	1	0
@	filesystem --custom-headers
a	1	0
@	rootfs
s	--template|-t	Output template [$TRIVY_TEMPLATE]
s	--format|-f	Format (table, json, sarif, template) (default: "table") [$TRIVY_FORMAT]
s	--severity|-s	Severities of vulnerabilities to be displayed (comma separated) (default…
s	--output|-o	Output file name [$TRIVY_OUTPUT]
s	--exit-code	Exit code when vulnerabilities were found (default: 0) [$TRIVY_EXIT_CODE]
s	--clear-cache|-c	Clear image caches without scanning [$TRIVY_CLEAR_CACHE]
s	--vuln-type	Comma-separated list of vulnerability types (os,library) (default: "os,library") [$TRIVY_VULN_TYPE]
s	--security-checks	Comma-separated list of what security issues to detect (vuln,config) (default: "vuln")…
s	--ignorefile	Specify .trivyignore file (default: ".trivyignore") [$TRIVY_IGNOREFILE]]
s	--timeout	Timeout (default: 5m0s) [$TRIVY_TIMEOUT]
s	--ignore-policy	Specify the Rego file to evaluate each vulnerability [$TRIVY_IGNORE_POLICY]
s	--list-all-pkgs	Enabling the option will output all packages regardless of vulnerability (default: false)…
s	--cache-backend	Cache backend (e.g. redis://localhost:6379) (default: "fs") [$TRIVY_CACHE_BACKEND]
s	--no-progress	Suppress progress bar [$TRIVY_NO_PROGRESS]
s	--offline-scan	Do not issue API requests to identify dependencies [$TRIVY_OFFLINE_SCAN]
s	--skip-files	Specify the file paths to skip traversal [$TRIVY_SKIP_FILES]
s	--skip-dirs	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
s	--skip-policy-update	Skip updating built-in policies [$TRIVY_SKIP_POLICY_UPDATE]
s	--config-policy	Specify paths to the Rego policy files directory, applying config files [$TRIVY_CONFIG_POLICY]
s	--config-data	Specify paths from which data for the Rego policies will be recursively loaded [$TRIVY_CONFIG_DATA]
s	--policy-namespaces|--namespaces	Rego namespaces (default: "users") [$TRIVY_POLICY_NAMESPACES]
s	--skip-db-update|--skip-update	Skip updating vulnerability database [$TRIVY_SKIP_UPDATE, $TRIVY_SKIP_DB_UPDATE]
a	1	0
#	rootfs	1
t	filepaths
@	rootfs --template
a	1	0
@	rootfs --format
a	1	0
#	rootfs --format	1
v	table	
v	json	
v	sarif	
v	template	
@	rootfs --severity
a	1	0
#	rootfs --severity	1
d
@	rootfs --output
a	1	0
#	rootfs --output	1
t	filepaths
@	rootfs --exit-code
a	1	0
@	rootfs --clear-cache
@	rootfs --vuln-type
a	1	0
#	rootfs --vuln-type	1
d
@	rootfs --security-checks
a	1	0
#	rootfs --security-checks	1
d
@	rootfs --ignorefile
a	1	0
#	rootfs --ignorefile	1
t	filepaths
@	rootfs --timeout
a	1	0
@	rootfs --ignore-policy
a	1	0
#	rootfs --ignore-policy	1
t	filepaths
@	rootfs --list-all-pkgs
@	rootfs --cache-backend
a	1	0
@	rootfs --no-progress
@	rootfs --offline-scan
@	rootfs --skip-files
a	1	0
#	rootfs --skip-files	1
t	filepaths
@	rootfs --skip-dirs
a	1	0
#	rootfs --skip-dirs	1
t	folders
@	rootfs --skip-policy-update
@	rootfs --config-policy
a	1	0
#	rootfs --config-policy	1
t	folders
@	rootfs --config-data
a	1	0
#	rootfs --config-data	1
t	folders
@	rootfs --policy-namespaces
a	1	0
@	rootfs --skip-db-update
@	sbom
s	--output|-o	Output file name [$TRIVY_OUTPUT]
s	--clear-cache|-c	Clear image caches without scanning [$TRIVY_CLEAR_CACHE]
s	--ignorefile	Specify .trivyignore file (default: ".trivyignore") [$TRIVY_IGNOREFILE]]
s	--timeout	Timeout (default: 5m0s) [$TRIVY_TIMEOUT]
s	--severity|-s	Severities of vulnerabilities to be displayed (comma separated) (default…
s	--offline-scan	Do not issue API requests to identify dependencies [$TRIVY_OFFLINE_SCAN]
s	--skip-files	Specify the file paths to skip traversal [$TRIVY_SKIP_FILES]
s	--skip-dirs	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
s	--artifact-type|--type	Input artifact type (image, fs, repo, archive) (default: "image") [$TRIVY_ARTIFACT_TYPE]
s	--sbom-format|--format	SBOM format (cyclonedx) (default: "cyclonedx") [$TRIVY_SBOM_FORMAT]
@	sbom --output
a	1	0
#	sbom --output	1
t	filepaths
@	sbom --clear-cache
@	sbom --ignorefile
a	1	0
#	sbom --ignorefile	1
t	filepaths
@	sbom --timeout
a	1	0
@	sbom --severity
a	1	0
#	sbom --severity	1
d
@	sbom --offline-scan
@	sbom --skip-files
a	1	0
#	sbom --skip-files	1
t	filepaths
@	sbom --skip-dirs
a	1	0
#	sbom --skip-dirs	1
t	folders
@	sbom --artifact-type
a	1	0
#	sbom --artifact-type	1
v	image	
v	fs	
v	repo	
v	archive	
@	sbom --sbom-format
a	1	0
#	sbom --sbom-format	1
v	cyclonedx	
@	repository
s	--template|-t	Output template [$TRIVY_TEMPLATE]
s	--format|-f	Format (table, json, sarif, template) (default: "table") [$TRIVY_FORMAT]
s	--severity|-s	Severities of vulnerabilities to be displayed (comma separated) (default…
s	--output|-o	Output file name [$TRIVY_OUTPUT]
s	--exit-code	Exit code when vulnerabilities were found (default: 0) [$TRIVY_EXIT_CODE]
s	--clear-cache|-c	Clear image caches without scanning [$TRIVY_CLEAR_CACHE]
s	--vuln-type	Comma-separated list of vulnerability types (os,library) (default: "os,library") [$TRIVY_VULN_TYPE]
s	--security-checks	Comma-separated list of what security issues to detect (vuln,config) (default: "vuln")…
s	--ignorefile	Specify .trivyignore file (default: ".trivyignore") [$TRIVY_IGNOREFILE]]
s	--timeout	Timeout (default: 5m0s) [$TRIVY_TIMEOUT]
s	--ignore-policy	Specify the Rego file to evaluate each vulnerability [$TRIVY_IGNORE_POLICY]
s	--list-all-pkgs	Enabling the option will output all packages regardless of vulnerability (default: false)…
s	--cache-backend	Cache backend (e.g. redis://localhost:6379) (default: "fs") [$TRIVY_CACHE_BACKEND]
s	--no-progress	Suppress progress bar [$TRIVY_NO_PROGRESS]
s	--offline-scan	Do not issue API requests to identify dependencies [$TRIVY_OFFLINE_SCAN]
s	--skip-files	Specify the file paths to skip traversal [$TRIVY_SKIP_FILES]
s	--skip-dirs	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
s	--skip-policy-update	Skip updating built-in policies [$TRIVY_SKIP_POLICY_UPDATE]
s	--skip-db-update|--skip-update	Skip updating vulnerability database [$TRIVY_SKIP_UPDATE, $TRIVY_SKIP_DB_UPDATE]
s	--ignore-unfixed	Display only fixed vulnerabilities [$TRIVY_IGNORE_UNFIXED]
s	--removed-pkgs	Detect vulnerabilities of removed packages (default: false) [$TRIVY_REMOVED_PKGS]
s	--input|-i	Input file path instead of image name [$TRIVY_INPUT]
s	--quiet|-q	Suppress progress bar and log output [$TRIVY_QUIET]
s	--insecure	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
@	repository --template
a	1	0
@	repository --format
a	1	0
#	repository --format	1
v	table	
v	json	
v	sarif	
v	template	
@	repository --severity
a	1	0
#	repository --severity	1
d
@	repository --output
a	1	0
#	repository --output	1
t	filepaths
@	repository --exit-code
a	1	0
@	repository --clear-cache
@	repository --vuln-type
a	1	0
#	repository --vuln-type	1
d
@	repository --security-checks
a	1	0
#	repository --security-checks	1
d
@	repository --ignorefile
a	1	0
#	repository --ignorefile	1
t	filepaths
@	repository --timeout
a	1	0
@	repository --ignore-policy
a	1	0
#	repository --ignore-policy	1
t	filepaths
@	repository --list-all-pkgs
@	repository --cache-backend
a	1	0
@	repository --no-progress
@	repository --offline-scan
@	repository --skip-files
a	1	0
#	repository --skip-files	1
t	filepaths
@	repository --skip-dirs
a	1	0
#	repository --skip-dirs	1
t	folders
@	repository --skip-policy-update
@	repository --skip-db-update
@	repository --ignore-unfixed
@	repository --removed-pkgs
@	repository --input
a	1	0
#	repository --input	1
t	filepaths
@	repository --quiet
@	repository --insecure
@	client
s	--template|-t	Output template [$TRIVY_TEMPLATE]
s	--format|-f	Format (table, json, sarif, template) (default: "table") [$TRIVY_FORMAT]
s	--severity|-s	Severities of vulnerabilities to be displayed (comma separated) (default…
s	--output|-o	Output file name [$TRIVY_OUTPUT]
s	--exit-code	Exit code when vulnerabilities were found (default: 0) [$TRIVY_EXIT_CODE]
s	--clear-cache|-c	Clear image caches without scanning [$TRIVY_CLEAR_CACHE]
s	--vuln-type	Comma-separated list of vulnerability types (os,library) (default: "os,library") [$TRIVY_VULN_TYPE]
s	--security-checks	Comma-separated list of what security issues to detect (vuln,config) (default: "vuln")…
s	--ignorefile	Specify .trivyignore file (default: ".trivyignore") [$TRIVY_IGNOREFILE]]
s	--timeout	Timeout (default: 5m0s) [$TRIVY_TIMEOUT]
s	--ignore-policy	Specify the Rego file to evaluate each vulnerability [$TRIVY_IGNORE_POLICY]
s	--list-all-pkgs	Enabling the option will output all packages regardless of vulnerability (default: false)…
s	--cache-backend	Cache backend (e.g. redis://localhost:6379) (default: "fs") [$TRIVY_CACHE_BACKEND]
s	--no-progress	Suppress progress bar [$TRIVY_NO_PROGRESS]
s	--offline-scan	Do not issue API requests to identify dependencies [$TRIVY_OFFLINE_SCAN]
s	--skip-files	Specify the file paths to skip traversal [$TRIVY_SKIP_FILES]
s	--skip-dirs	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
s	--severity|-s	Severities of vulnerabilities to be displayed (comma separated) (default…
s	--input|-i	Input file path instead of image name [$TRIVY_INPUT]
s	--ignore-unfixed	Display only fixed vulnerabilities [$TRIVY_IGNORE_UNFIXED]
s	--insecure	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
s	--removed-pkgs	Detect vulnerabilities of removed packages (default: false) [$TRIVY_REMOVED_PKGS]
s	--output|-o	Output file name [$TRIVY_OUTPUT]
s	--config-policy	Specify paths to the Rego policy files directory, applying config files [$TRIVY_CONFIG_POLICY]
s	--skip-files	Specify the file paths to skip traversal [$TRIVY_SKIP_FILES]
s	--skip-dirs	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
s	--token	For authentication in client/server mode [$TRIVY_TOKEN]
s	--token-header	Specify a header name for token in client/server mode (default: "Trivy-Token") [$TRIVY_TOKEN_HEADER]
s	--custom-headers	Custom headers in client/server mode [$TRIVY_CUSTOM_HEADERS]
s	--remote	Server address (default: "http://localhost:4954") [$TRIVY_REMOTE]
@	client --template
a	1	0
@	client --format
a	1	0
#	client --format	1
v	table	
v	json	
v	sarif	
v	template	
@	client --severity
a	1	0
#	client --severity	1
d
@	client --output
a	1	0
#	client --output	1
t	filepaths
@	client --exit-code
a	1	0
@	client --clear-cache
@	client --vuln-type
a	1	0
#	client --vuln-type	1
d
@	client --security-checks
a	1	0
#	client --security-checks	1
d
@	client --ignorefile
a	1	0
#	client --ignorefile	1
t	filepaths
@	client --timeout
a	1	0
@	client --ignore-policy
a	1	0
#	client --ignore-policy	1
t	filepaths
@	client --list-all-pkgs
@	client --cache-backend
a	1	0
@	client --no-progress
@	client --offline-scan
@	client --skip-files
a	1	0
#	client --skip-files	1
t	filepaths
@	client --skip-dirs
a	1	0
#	client --skip-dirs	1
t	folders
@	client --severity
a	1	0
#	client --severity	1
d
@	client --input
a	1	0
#	client --input	1
t	filepaths
@	client --ignore-unfixed
@	client --insecure
@	client --removed-pkgs
@	client --output
a	1	0
#	client --output	1
t	filepaths
@	client --config-policy
a	1	0
#	client --config-policy	1
t	folders
@	client --skip-files
a	1	0
#	client --skip-files	1
t	filepaths
@	client --skip-dirs
a	1	0
#	client --skip-dirs	1
t	folders
@	client --token
a	1	0
@	client --token-header
a	1	0
@	client --custom-headers
a	1	0
@	client --remote
a	1	0
@	server
s	--skip-db-update|--skip-update	Skip updating vulnerability database [$TRIVY_SKIP_UPDATE, $TRIVY_SKIP_DB_UPDATE]
s	--download-db-only	Download/update vulnerability database but don't run a scan [$TRIVY_DOWNLOAD_DB_ONLY]
s	--reset	Remove all caches and database [$TRIVY_RESET]
s	--cache-backend	Cache backend (e.g. redis://localhost:6379) (default: "fs") [$TRIVY_CACHE_BACKEND]
s	--token	For authentication in client/server mode [$TRIVY_TOKEN]
s	--token-header	Specify a header name for token in client/server mode (default: "Trivy-Token") [$TRIVY_TOKEN_HEADER]
s	--listen	Listen address (default: "localhost:4954") [$TRIVY_LISTEN]
@	server --skip-db-update
@	server --download-db-only
@	server --reset
@	server --cache-backend
a	1	0
@	server --token
a	1	0
@	server --token-header
a	1	0
@	server --listen
a	1	0
@	config
s	--template|-t	Output template [$TRIVY_TEMPLATE]
s	--format|-f	Format (table, json, sarif, template) (default: "table") [$TRIVY_FORMAT]
s	--severity|-s	Severities of vulnerabilities to be displayed (comma separated) (default…
s	--output|-o	Output file name [$TRIVY_OUTPUT]
s	--exit-code	Exit code when vulnerabilities were found (default: 0) [$TRIVY_EXIT_CODE]
s	--skip-policy-update	Skip updating built-in policies [$TRIVY_SKIP_POLICY_UPDATE]
s	--reset	Remove all caches and database [$TRIVY_RESET]
s	--clear-cache|-c	Clear image caches without scanning [$TRIVY_CLEAR_CACHE]
s	--ignorefile	Specify .trivyignore file (default: ".trivyignore") [$TRIVY_IGNOREFILE]]
s	--timeout	Timeout (default: 5m0s) [$TRIVY_TIMEOUT]
s	--skip-files	Specify the file paths to skip traversal [$TRIVY_SKIP_FILES]
s	--skip-dirs	Allow insecure server connections when using SSL [$TRIVY_INSECURE]
s	--config-policy	Specify paths to the Rego policy files directory, applying config files [$TRIVY_CONFIG_POLICY]
s	--config-data	Specify paths from which data for the Rego policies will be recursively loaded [$TRIVY_CONFIG_DATA]
s	--policy-namespaces|--namespaces	Rego namespaces (default: "users") [$TRIVY_POLICY_NAMESPACES]
s	--file-patterns	Specify file patterns [$TRIVY_FILE_PATTERNS
s	--include-non-failures	Enable more verbose trace output for custom queries [$TRIVY_TRACE]
s	--trace	Enable more verbose trace output for custom queries [$TRIVY_TRACE]
@	config --template
a	1	0
@	config --format
a	1	0
#	config --format	1
v	table	
v	json	
v	sarif	
v	template	
@	config --severity
a	1	0
#	config --severity	1
d
@	config --output
a	1	0
#	config --output	1
t	filepaths
@	config --exit-code
a	1	0
@	config --skip-policy-update
@	config --reset
@	config --clear-cache
@	config --ignorefile
a	1	0
#	config --ignorefile	1
t	filepaths
@	config --timeout
a	1	0
@	config --skip-files
a	1	0
#	config --skip-files	1
t	filepaths
@	config --skip-dirs
a	1	0
#	config --skip-dirs	1
t	folders
@	config --config-policy
a	1	0
#	config --config-policy	1
t	folders
@	config --config-data
a	1	0
#	config --config-data	1
t	folders
@	config --policy-namespaces
a	1	0
@	config --file-patterns
a	1	0
@	config --include-non-failures
@	config --trace
@	plugin
s	install|i	Install a plugin
s	uninstall|u	Uninstall plugin
s	list|l	List installed plugin
s	info	Information about a plugin
s	run|r	Run a plugin on the fly
s	update	Update an existing plugin
s	help|h	Shows a list of commands or help for one command
@	plugin install
a	1	0
@	plugin uninstall
a	1	0
@	plugin list
@	plugin info
a	1	0
@	plugin run
a	1	0
@	plugin update
a	1	0
@	plugin help
a	1	0
#	plugin help	1
t	help
@	version
@	help
