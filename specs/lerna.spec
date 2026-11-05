@	
s	init	Create a new lerna repo or upgrade an existing repo to the current version of Lerna
s	bootstrap	Bootstrap the packages in the current Lerna repo. Installing all their dependencies and linking…
s	import	Import the package in the local path <pathToRepo> into packages/<directory-name> with commit history
s	publish	Create a new release of the packages that have been updated. Prompts for a new version and updates…
s	ls	List local packages
s	ll	List local packages
s	la	List local packages
s	list	List local packages
s	changed	Check which packages have changed since the last release
s	run	Run an npm script in each package that contains that script
s	link	Symlink together all Lerna packages that are dependencies of each other in the current Lerna repo
s	info	Prints local environment information that proves to be useful especially while submitting bug…
s	version	Bump version of packages changed since the last release
s	diff	Diff all packages or a single package since the last release
s	exec	Execute an arbitrary command in each package
s	add	Add a dependency to matched packages
s	clean	Remove the node_modules directory from all packages
s	create	Create a new lerna-managed package
@	init
o	--concurrency	How many threads to use when Lerna parallelizes the tasks (defaults to count of logical CPU cores)	
o	--loglevel	What level of logs to report. On failure, all logs are written to lerna-debug.log in the current…	v
o	--max-buffer	Set a max buffer length for each underlying process call	v
o	--no-progress	Disable progress bars. This is always the case in a CI environment	
o	--no-sort	The --no-sort option disables sorting, instead executing tasks in an arbitrary order with maximum…	
o	--reject-cycles	Fail immediately if a cycle is found (in bootstrap, exec, publish or run)	
o	-h|--help	Show help	
o	-v|--version	Show version number	
o	--npm-client	The exececutable to run the script with	v
o	-i|--independent	Use independent versioning mode	
o	--exact	Set the exact version of lerna in the package.json file	
=	init	--loglevel
v	silent	
v	error	
v	warn	
v	success	
v	info	
v	verbose	
v	silly	
=	init	--npm-client
v	npm	
v	yarn	
v	pnpm	
@	bootstrap
o	--scope	Include only packages with names matching the given glob	v
o	--ignore	Exclude packages with names matching the given glob	v
o	--no-private	Exclude private packages. They are included by default	
o	--since	Only include packages that have been changed since the specified ref. If no ref is passed, it…	V
o	--exclude-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependencies	Include all transitive dependencies when running a command regardless of --scope, --ignore, or…	
o	--include-merged-tags	Include tags from merged branches when running a command with --since. This is only useful if you…	
o	--npm-client	The exececutable to run the script with	v
o	--hoist	Install external dependencies matching glob at the repo root so they're available to all packages	v
o	--nohoist	Do not install external dependencies matching glob at the repo root. This can be used to opt out…	v
o	--strict	When used in conjunction with hoist will throw an error and stop bootstrapping after emitting the…	
o	--ignore-prepublish	Skip prepublish lifecycle scripts run by default in bootstrapped packages	
o	--ignore-scripts	Skip any lifecycle scripts normally run (prepare, etc) in bootstrapped packages	
o	--registry	Forwarded npm commands will use the specified registry for your package(s)	v
o	--use-workspaces	Enables integration with Yarn Workspaces	
o	--no-ci	Disable usage of `npm ci` in CI environments	
o	--force-local	When passed, this flag causes the bootstrap command to always symlink local dependencies…	
=	bootstrap	--scope
d
=	bootstrap	--ignore
d
=	bootstrap	--npm-client
v	npm	
v	yarn	
v	pnpm	
@	import
o	--concurrency	How many threads to use when Lerna parallelizes the tasks (defaults to count of logical CPU cores)	
o	--loglevel	What level of logs to report. On failure, all logs are written to lerna-debug.log in the current…	v
o	--max-buffer	Set a max buffer length for each underlying process call	v
o	--no-progress	Disable progress bars. This is always the case in a CI environment	
o	--no-sort	The --no-sort option disables sorting, instead executing tasks in an arbitrary order with maximum…	
o	--reject-cycles	Fail immediately if a cycle is found (in bootstrap, exec, publish or run)	
o	-h|--help	Show help	
o	-v|--version	Show version number	
o	--flatten	Flatten the git history of the repository to import	
o	--dest	Specify the destination directory by the directory listed in lerna.json	
o	--preserve-commit	Preserve the original committer and commit date	
a	1	0
=	import	--loglevel
v	silent	
v	error	
v	warn	
v	success	
v	info	
v	verbose	
v	silly	
#	import	1
t	folders
@	publish
o	--concurrency	How many threads to use when Lerna parallelizes the tasks (defaults to count of logical CPU cores)	
o	--loglevel	What level of logs to report. On failure, all logs are written to lerna-debug.log in the current…	v
o	--max-buffer	Set a max buffer length for each underlying process call	v
o	--no-progress	Disable progress bars. This is always the case in a CI environment	
o	--no-sort	The --no-sort option disables sorting, instead executing tasks in an arbitrary order with maximum…	
o	--reject-cycles	Fail immediately if a cycle is found (in bootstrap, exec, publish or run)	
o	-h|--help	Show help	
o	-v|--version	Show version number	
o	--npm-tag	Publish to npm with the given npm dist-tag (Defaults to latest)	v
o	--canary|-c	Create a canary release	
o	--skip-git	Don't run any git commands	
o	--force-publish	Force publish for the specified packages (comma-separated)	v
=	publish	--loglevel
v	silent	
v	error	
v	warn	
v	success	
v	info	
v	verbose	
v	silly	
=	publish	--force-publish
v	*	Select all packages
d
@	ls
o	--json	Show information as a JSON array	
o	--ndjson	Show information as newline-delimited JSON	
o	-a|-all	Show all packages (including private)	
o	-l|--long	Show extended information	
o	-p|--parseable	Show parseable output instead of columnified view	
o	--toposort	Sort packages in topological order (dependencies before dependents) instead of lexical by directory	
o	--graph	Show dependency graph as a JSON-formatted adjacency list	
@	ll
o	--json	Show information as a JSON array	
o	--ndjson	Show information as newline-delimited JSON	
o	-a|-all	Show all packages (including private)	
o	-l|--long	Show extended information	
o	-p|--parseable	Show parseable output instead of columnified view	
o	--toposort	Sort packages in topological order (dependencies before dependents) instead of lexical by directory	
o	--graph	Show dependency graph as a JSON-formatted adjacency list	
@	la
o	--json	Show information as a JSON array	
o	--ndjson	Show information as newline-delimited JSON	
o	-a|-all	Show all packages (including private)	
o	-l|--long	Show extended information	
o	-p|--parseable	Show parseable output instead of columnified view	
o	--toposort	Sort packages in topological order (dependencies before dependents) instead of lexical by directory	
o	--graph	Show dependency graph as a JSON-formatted adjacency list	
@	list
o	--json	Show information as a JSON array	
o	--ndjson	Show information as newline-delimited JSON	
o	-a|-all	Show all packages (including private)	
o	-l|--long	Show extended information	
o	-p|--parseable	Show parseable output instead of columnified view	
o	--toposort	Sort packages in topological order (dependencies before dependents) instead of lexical by directory	
o	--graph	Show dependency graph as a JSON-formatted adjacency list	
@	changed
o	--concurrency	How many threads to use when Lerna parallelizes the tasks (defaults to count of logical CPU cores)	
o	--loglevel	What level of logs to report. On failure, all logs are written to lerna-debug.log in the current…	v
o	--max-buffer	Set a max buffer length for each underlying process call	v
o	--no-progress	Disable progress bars. This is always the case in a CI environment	
o	--no-sort	The --no-sort option disables sorting, instead executing tasks in an arbitrary order with maximum…	
o	--reject-cycles	Fail immediately if a cycle is found (in bootstrap, exec, publish or run)	
o	-h|--help	Show help	
o	-v|--version	Show version number	
a	1	0
=	changed	--loglevel
v	silent	
v	error	
v	warn	
v	success	
v	info	
v	verbose	
v	silly	
#	changed	1
d
@	run
o	--concurrency	How many threads to use when Lerna parallelizes the tasks (defaults to count of logical CPU cores)	
o	--loglevel	What level of logs to report. On failure, all logs are written to lerna-debug.log in the current…	v
o	--max-buffer	Set a max buffer length for each underlying process call	v
o	--no-progress	Disable progress bars. This is always the case in a CI environment	
o	--no-sort	The --no-sort option disables sorting, instead executing tasks in an arbitrary order with maximum…	
o	--reject-cycles	Fail immediately if a cycle is found (in bootstrap, exec, publish or run)	
o	-h|--help	Show help	
o	-v|--version	Show version number	
o	--scope	Include only packages with names matching the given glob	v
o	--ignore	Exclude packages with names matching the given glob	v
o	--no-private	Exclude private packages. They are included by default	
o	--since	Only include packages that have been changed since the specified ref. If no ref is passed, it…	V
o	--exclude-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependencies	Include all transitive dependencies when running a command regardless of --scope, --ignore, or…	
o	--include-merged-tags	Include tags from merged branches when running a command with --since. This is only useful if you…	
o	--stream	Stream output from child processes immediately, prefixed with the originating package name. This…	
o	--parallel	Similar to --stream, but completely disregards concurrency and topological sorting, running a…	
o	--no-bail	By default, lerna run will exit with an error if any script run returns a non-zero exit code. Pass…	
o	--no-prefix	Disable package name prefixing when output is streaming (--stream or --parallel). This option can…	
o	--profile	Profiles the script executions and produces a performance profile which can be analyzed using…	
o	--profile-location	You can provide a custom location for the performance profile output. The path provided will be…	v
a	1	0
=	run	--loglevel
v	silent	
v	error	
v	warn	
v	success	
v	info	
v	verbose	
v	silly	
=	run	--scope
d
=	run	--ignore
d
=	run	--profile-location
t	folders
#	run	1
d
@	link
o	--concurrency	How many threads to use when Lerna parallelizes the tasks (defaults to count of logical CPU cores)	
o	--loglevel	What level of logs to report. On failure, all logs are written to lerna-debug.log in the current…	v
o	--max-buffer	Set a max buffer length for each underlying process call	v
o	--no-progress	Disable progress bars. This is always the case in a CI environment	
o	--no-sort	The --no-sort option disables sorting, instead executing tasks in an arbitrary order with maximum…	
o	--reject-cycles	Fail immediately if a cycle is found (in bootstrap, exec, publish or run)	
o	-h|--help	Show help	
o	-v|--version	Show version number	
o	--force-local	When passed, this flag causes the link command to always symlink local dependencies regardless of…	
=	link	--loglevel
v	silent	
v	error	
v	warn	
v	success	
v	info	
v	verbose	
v	silly	
@	info
@	version
o	--allow-branch	An allowlist of globs that match git branches where lerna version is enabled	v
o	--amend	Perform all changes on the current commit, instead of adding a new one	
o	--changelog-preset	Change the changelog preset type	
o	--conventional-commits	Use the Conventional Commits Specification to determine the version bump and generate CHANGELOG.md…	
o	--conventional-graduate	Graduate the specified packages (comma-separated) or all packages using *	
o	--conventional-prerelease	Release with prerelease versions the specified packages (comma-separated) or all packages using *	
o	--create-release	Create an official release based on the changes packages	v
o	--exact	Specify updated dependencies in updated packages exactly	
o	--force-publish	Force publish the specified packages (comma-separated) or all packages using *	
o	--git-remote	Push the git changes to the specified remote instead of origin	v
o	--ignore-changes	Ignore changes in files matched by glob(s) when detecting changed packages	V
o	--ignore-scripts	Disable running lifecycle scripts during lerna version	
o	--include-merged-tags	Include tags from merged branches when detecting changed packages	
o	-m|--message	Use the provided message when committing the version updates for publication	v
o	--no-changelog	When using conventional-commits, do not generate any CHANGELOG.md files	
o	--no-commit-hooks	Disable running git commit hooks	
o	--no-git-tag-version	Don't commit changes to package.json files and don't tag the release	
o	--no-granular-pathspec		
o	--no-private	Don't include private packages	
o	--preid	Bump semver using the specified prerelease identifier	v
o	--sign-git-commit		
o	--sign-git-tag		
o	--force-git-tag		
o	--tag-version-prefix	Change the custom version prefix	v
o	--yes	Skip all confirmation prompts	
a	1	0
=	version	--allow-branch
d
=	version	--create-release
v	github	
v	gitlab	
=	version	--git-remote
d
=	version	--ignore-changes
t	folders
#	version	1
v	major	
v	minor	
v	patch	
v	premajor	
v	preminor	
v	prepatch	
v	prerelease	
@	diff
a	1	0
#	diff	1
d
@	exec
o	--concurrency	How many threads to use when Lerna parallelizes the tasks (defaults to count of logical CPU cores)	
o	--loglevel	What level of logs to report. On failure, all logs are written to lerna-debug.log in the current…	v
o	--max-buffer	Set a max buffer length for each underlying process call	v
o	--no-progress	Disable progress bars. This is always the case in a CI environment	
o	--no-sort	The --no-sort option disables sorting, instead executing tasks in an arbitrary order with maximum…	
o	--reject-cycles	Fail immediately if a cycle is found (in bootstrap, exec, publish or run)	
o	-h|--help	Show help	
o	-v|--version	Show version number	
o	--scope	Include only packages with names matching the given glob	v
o	--ignore	Exclude packages with names matching the given glob	v
o	--no-private	Exclude private packages. They are included by default	
o	--since	Only include packages that have been changed since the specified ref. If no ref is passed, it…	V
o	--exclude-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependencies	Include all transitive dependencies when running a command regardless of --scope, --ignore, or…	
o	--include-merged-tags	Include tags from merged branches when running a command with --since. This is only useful if you…	
o	--stream	Stream output from child processes immediately, prefixed with the originating package name. This…	
o	--parallel	Similar to --stream, but completely disregards concurrency and topological sorting, running a…	
o	--no-bail	By default, lerna run will exit with an error if any script run returns a non-zero exit code. Pass…	
o	--no-prefix	Disable package name prefixing when output is streaming (--stream or --parallel). This option can…	
o	--profile	Profiles the script executions and produces a performance profile which can be analyzed using…	
o	--profile-location	You can provide a custom location for the performance profile output. The path provided will be…	v
a	1	0
=	exec	--loglevel
v	silent	
v	error	
v	warn	
v	success	
v	info	
v	verbose	
v	silly	
=	exec	--scope
d
=	exec	--ignore
d
=	exec	--profile-location
t	folders
#	exec	1
d
@	add
o	--concurrency	How many threads to use when Lerna parallelizes the tasks (defaults to count of logical CPU cores)	
o	--loglevel	What level of logs to report. On failure, all logs are written to lerna-debug.log in the current…	v
o	--max-buffer	Set a max buffer length for each underlying process call	v
o	--no-progress	Disable progress bars. This is always the case in a CI environment	
o	--no-sort	The --no-sort option disables sorting, instead executing tasks in an arbitrary order with maximum…	
o	--reject-cycles	Fail immediately if a cycle is found (in bootstrap, exec, publish or run)	
o	-h|--help	Show help	
o	-v|--version	Show version number	
o	--scope	Include only packages with names matching the given glob	v
o	--ignore	Exclude packages with names matching the given glob	v
o	--no-private	Exclude private packages. They are included by default	
o	--since	Only include packages that have been changed since the specified ref. If no ref is passed, it…	V
o	--exclude-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependencies	Include all transitive dependencies when running a command regardless of --scope, --ignore, or…	
o	--include-merged-tags	Include tags from merged branches when running a command with --since. This is only useful if you…	
o	--dev	Add the new package to devDependencies instead of dependencies	
o	--exact	Add the new package with an exact version	
o	--peer	Add the new package to peerDependencies instead of dependencies	
o	--registry	Use a custom registry to install the targeted package	v
o	--no-bootstrap	Skip the chained lerna bootstrap	
=	add	--loglevel
v	silent	
v	error	
v	warn	
v	success	
v	info	
v	verbose	
v	silly	
=	add	--scope
d
=	add	--ignore
d
@	clean
o	--concurrency	How many threads to use when Lerna parallelizes the tasks (defaults to count of logical CPU cores)	
o	--loglevel	What level of logs to report. On failure, all logs are written to lerna-debug.log in the current…	v
o	--max-buffer	Set a max buffer length for each underlying process call	v
o	--no-progress	Disable progress bars. This is always the case in a CI environment	
o	--no-sort	The --no-sort option disables sorting, instead executing tasks in an arbitrary order with maximum…	
o	--reject-cycles	Fail immediately if a cycle is found (in bootstrap, exec, publish or run)	
o	-h|--help	Show help	
o	-v|--version	Show version number	
o	--scope	Include only packages with names matching the given glob	v
o	--ignore	Exclude packages with names matching the given glob	v
o	--no-private	Exclude private packages. They are included by default	
o	--since	Only include packages that have been changed since the specified ref. If no ref is passed, it…	V
o	--exclude-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependents	Exclude all transitive dependents when running a command with --since, overriding the default…	
o	--include-dependencies	Include all transitive dependencies when running a command regardless of --scope, --ignore, or…	
o	--include-merged-tags	Include tags from merged branches when running a command with --since. This is only useful if you…	
o	--yes	Skip all confirmation prompts	
=	clean	--loglevel
v	silent	
v	error	
v	warn	
v	success	
v	info	
v	verbose	
v	silly	
=	clean	--scope
d
=	clean	--ignore
d
@	create
o	--access	Set the scope of the package	v
o	--bin	Package has an executable	V
o	--description	Package description	
o	--dependencies	A list of package dependencies	v
o	--es-module	Initialize a transpiled ES Module	
o	--homepage	The package homepage, defaulting to a subpath of the root pkg.homepage	
o	--keywords	A list of package keywords	v
o	--license	The desired package license (SPDX identifier)	
o	--private	Make the new package private, never published	
o	--registry	Configure the package's publishConfig.registry	
o	--tag	Configure the package's publishConfig.tag	
o	--yes	Skip all prompts, accepting default values	
a	2	0
=	create	--access
v	public	
v	restricted	
