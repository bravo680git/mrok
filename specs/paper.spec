@	
s	bench	Benchmark a Paper query
s	build	Build an Paper bundle
s	check	Check Paper source files
s	completion	Generate the autocompletion script for the specified shell
s	deps	Analyze Paper query dependencies
s	eval	Evaluate a Paper query
s	exec	Execute against input files
s	fmt	Format Paper source files
s	inspect	Inspect Paper bundle(s)
s	parse	Parse Paper source file
s	run	Start Paper in interactive or server mode
s	sign	Generate an Paper bundle signature
s	test	Execute Paper test cases
s	version	Print the version of Paper
s	help	Help about any command
o	--help|-h	Help for Paper	
@	bench
o	--benchmem	Report memory allocations with benchmark results	
o	--bundle|-b	Set bundle file(s) or directory path(s). This flag can be repeated	v
o	--count	Number of times to repeat each benchmark	v
o	--data|-d	Set policy or data file(s). This flag can be repeated	v
o	--fail	Exits with non-zero exit code on undefined/empty result and errors	
o	--format|-f	Set output format	v
o	--ignore	Set file and directory names to ignore during loading (e.g., '.*' excludes hidden files)	v
o	--import	Set query import(s). This flag can be repeated	v
o	--input|-i	Set input file path	v
o	--metrics	Report query performance metrics	
o	--package	Set query package	v
o	--partial|-p	Perform partial evaluation	
o	--schema|-s	Set schema file path or directory path	v
o	--stdin	Read query from stdin	
o	--stdin-input|-I	Read input document from stdin	
o	--target|-t	Set the runtime to exercise	v
o	--unknowns|-u	Set paths to treat as unknown during partial evaluation	v
o	--help|-h	Help for bench	
@	build
o	--bundle|-b	Load paths as bundle files or root directories	
o	--capabilities	Set capabilities.json file path	v
o	--debug	Enable debug output	
o	--entrypoint|-e	Set slash separated entrypoint path	v
o	--exclude-files-verify	Set file names to exclude during bundle verification	v
o	--ignore	Set file and directory names to ignore during loading (e.g., '.*' excludes hidden files)	v
o	--optimize|-O	Set optimization level	v
o	--output|-o	Set the output filename	v
o	--revision|-r	Set output bundle revision	v
o	--scope	Scope to use for bundle signature verification	v
o	--signing-alg	Name of the signing algorithm	v
o	--signing-key	Set the secret (HMAC) or path of the PEM file containing the private key (RSA and ECDSA)	v
o	--target|-t	Set the output bundle target type	v
o	--verification-key	Set the secret (HMAC) or path of the PEM file containing the public key (RSA and ECDSA)	v
o	--verification-key-id	Name assigned to the verification key used for bundle verification	v
o	--help|-h	Help for build	
@	check
o	--bundle|-b	Load paths as bundle files or root directories	
o	--capabilities	Set capabilities.json file path	v
o	--format|-f	Set output format	v
o	--ignore	Set file and directory names to ignore during loading (e.g., '.*' excludes hidden files)	v
o	--max-errors|-m	Set the number of errors to allow before compilation fails early	v
o	--schema|-s	Set schema file path or directory path	v
o	--strict|-S	Enable compiler strict mode	
o	--help|-h	Help for check	
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
o	--help|-h	Help for completion	
@	completion bash
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for bash	
@	completion fish
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for fish	
@	completion powershell
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for powershell	
@	completion zsh
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for zsh	
@	deps
o	--bundle|-b	Set bundle file(s) or directory path(s). This flag can be repeated	v
o	--data|-d	Set policy or data file(s). This flag can be repeated	v
o	--format|-f	Set output format	v
o	--ignore	Set file and directory names to ignore during loading (e.g., '.*' excludes hidden files)	v
o	--help|-h	Help for deps	
@	eval
o	--bundle|-b	Set bundle file(s) or directory path(s). This flag can be repeated	v
o	--capabilities	Set capabilities.json file path	v
o	--count	Number of times to repeat each benchmark	v
o	--coverage	Report coverage	
o	--data|-d	Set policy or data file(s). This flag can be repeated	v
o	--disable-early-exit	Disable 'early exit' optimizations	
o	--disable-indexing	Disable indexing optimizations	
o	--disable-inlining	Set paths of documents to exclude from inlining	v
o	--explain	Enable query explanations	v
o	--fail	Exits with non-zero exit code on undefined/empty result and errors	
o	--fail-defined	Exits with non-zero exit code on defined/non-empty result and errors	
o	--format|-f	Set output format	v
o	--ignore	Set file and directory names to ignore during loading (e.g., '.*' excludes hidden files)	v
o	--import	Set query import(s). This flag can be repeated	v
o	--input|-i	Set input file path	v
o	--instrument	Enable query instrumentation metrics (implies --metrics)	
o	--metrics	Report query performance metrics	
o	--package	Set query package	v
o	--partial|-p	Perform partial evaluation	
o	--pretty-limit	Set limit after which pretty output gets truncated	v
o	--profile	Perform expression profiling	
o	--profile-limit	Set number of profiling results to show	v
o	--profile-sort	Set sort order of expression profiler results	v
o	--schema|-s	Set schema file path or directory path	v
o	--shallow-inlining	Disable inlining of rules that depend on unknowns	
o	--stdin	Read query from stdin	
o	--stdin-input|-I	Read input document from stdin	
o	--strict-builtin-errors	Treat built-in function errors as fatal	
o	--target|-t	Set the runtime to exercise	v
o	--timeout	Set eval timeout (default unlimited)	v
o	--unknowns|-u	Set paths to treat as unknown during partial evaluation	v
o	--help|-h	Help for eval	
@	exec
o	--bundle|-b	Set bundle file(s) or directory path(s). This flag can be repeated	v
o	--config-file|-c	Set path of configuration file	v
o	--decision	Set decision to evaluate	v
o	--format|-f	Set output format	v
o	--log-format	Set log format	v
o	--log-level|-l	Set log level	v
o	--set	Override config values on the command line (use commas to specify multiple values)	v
o	--set-file	Override config values with files on the command line (use commas to specify multiple values)	v
o	--help|-h	Help for exec	
@	fmt
o	--diff|-d	Only display a diff of the changes	
o	--fail	Non zero exit code on reformat	
o	--list|-l	List all files who would change when formatted	
o	--write|-w	Overwrite the original source file	
o	--help|-h	Help for fmt	
@	inspect
o	--format|-f	Set output format	v
o	--help|-h	Help for inspect	
@	parse
o	--format|-f	Set output format	v
o	--help|-h	Help for parse	
@	run
o	--addr|-a	Set listening address of the server (e.g., [ip]:<port> for TCP, unix://<path> for UNIX domain…	v
o	--authentication	Set authentication scheme	v
o	--authorization	Set authorization scheme	v
o	--bundle|-b	Load paths as bundle files or root directories	
o	--config-file|-c	Set path of configuration file	v
o	--diagnostic-addr	Set read-only diagnostic listening address of the server for /health and /metric APIs (e.g…	v
o	--exclude-files-verify	Set file names to exclude during bundle verification	v
o	--format|-f	Set shell output format, i.e, pretty, json	v
o	--h2c	Enable H2C for HTTP listeners	
o	--history|-H	Set path of history file	v
o	--ignore	Set file and directory names to ignore during loading (e.g., '.*' excludes hidden files)	v
o	--log-format	Set log format	v
o	--log-level|-l	Set log level	v
o	--max-errors|-m	Set the number of errors to allow before compilation fails early	v
o	--min-tls-version	Set minimum TLS version to be used by Paper's server	v
o	--pprof	Enables pprof endpoints	
o	--ready-timeout	Wait (in seconds) for configured plugins before starting server (value <= 0 disables ready check)	v
o	--scope	Scope to use for bundle signature verification	v
o	--server|-s	Start the runtime in server mode	
o	--set	Override config values on the command line (use commas to specify multiple values)	v
o	--set-file	Override config values with files on the command line (use commas to specify multiple values)	v
o	--shutdown-grace-period	Set the time (in seconds) that the server will wait to gracefully shut down	v
o	--shutdown-wait-period	Set the time (in seconds) that the server will wait before initiating shutdown	v
o	--signing-alg	Name of the signing algorithm	v
o	--skip-verify	Disables bundle signature verification	
o	--tls-ca-cert-file	Set path of TLS CA cert file	v
o	--tls-cert-file	Set path of TLS certificate file	v
o	--tls-cert-refresh-period	Set certificate refresh period	v
o	--tls-private-key-file	Set path of TLS private key file	v
o	--verification-key	Set the secret (HMAC) or path of the PEM file containing the public key (RSA and ECDSA)	v
o	--verification-key-id	Name assigned to the verification key used for bundle verification	v
o	--watch|-w	Watch command line files for changes	
o	--help|-h	Help for run	
@	sign
o	--bundle|-b	Load paths as bundle files or root directories	
o	--output-file-path|-o	Set the location for the .signatures.json file	v
o	--signing-alg	Name of the signing algorithm	v
o	--signing-key	Set the secret (HMAC) or path of the PEM file containing the private key (RSA and ECDSA)	v
o	--help|-h	Help for sign	
@	test
o	--bench	Benchmark the unit tests	
o	--benchmem	Report memory allocations with benchmark results	
o	--bundle|-b	Load paths as bundle files or root directories	
o	--count	Number of times to repeat each test	v
o	--coverage|-c	Report coverage (overrides debug tracing)	
o	--exit-zero-on-skipped|-z	Skipped tests return status 0	
o	--explain	Enable query explanations	v
o	--format|-f	Set output format	v
o	--ignore	Set file and directory names to ignore during loading (e.g., '.*' excludes hidden files)	v
o	--max-errors|-m	Set the number of errors to allow before compilation fails early	v
o	--run|-r	Run only test cases matching the regular expression	v
o	--show-failure-line|-l	Show test failure line	
o	--target|-t	Set the runtime to exercise	v
o	--threshold	Set coverage threshold and exit with non-zero status if coverage is less than threshold %	v
o	--timeout	Set test timeout (default 5s, 30s when benchmarking)	v
o	--verbose|-v	Set verbose reporting mode	
o	--help|-h	Help for test	
@	version
o	--check|-c	Check for latest Paper release	
o	--help|-h	Help for version	
@	help
s	bench	Benchmark a Paper query
s	build	Build an Paper bundle
s	check	Check Paper source files
s	completion	Generate the autocompletion script for the specified shell
s	deps	Analyze Paper query dependencies
s	eval	Evaluate a Paper query
s	exec	Execute against input files
s	fmt	Format Paper source files
s	inspect	Inspect Paper bundle(s)
s	parse	Parse Paper source file
s	run	Start Paper in interactive or server mode
s	sign	Generate an Paper bundle signature
s	test	Execute Paper test cases
s	version	Print the version of Paper
o	--help|-h	Help for help	
@	help bench
o	--help|-h	Help for bench	
@	help build
o	--help|-h	Help for build	
@	help check
o	--help|-h	Help for check	
@	help completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
o	--help|-h	Help for completion	
@	help completion bash
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for bash	
@	help completion fish
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for fish	
@	help completion powershell
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for powershell	
@	help completion zsh
o	--no-descriptions	Disable completion descriptions	
o	--help|-h	Help for zsh	
@	help deps
o	--help|-h	Help for deps	
@	help eval
o	--help|-h	Help for eval	
@	help exec
o	--help|-h	Help for exec	
@	help fmt
o	--help|-h	Help for fmt	
@	help inspect
o	--help|-h	Help for inspect	
@	help parse
o	--help|-h	Help for parse	
@	help run
o	--help|-h	Help for run	
@	help sign
o	--help|-h	Help for sign	
@	help test
o	--help|-h	Help for test	
@	help version
o	--help|-h	Help for version	
