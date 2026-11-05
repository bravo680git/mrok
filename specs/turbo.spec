@	
s	bin	Get the path to the turbo binary
s	link	Link your local directory to a Vercel organization and enable remote caching
s	login	Login to your Vercel account
s	logout	Logout of your Vercel account
s	prune	Prepare a subset of your monorepo
s	unlink	Unlink the current directory from your Vercel organization and disable remote caching
s	run	Run tasks in your monorepo
o	--version	Print the version	
o	--help	Print a help message	p
@	bin
@	link
o	--no-gitignore	Do not create or modify .gitignore	
@	login
o	--sso-team	Attempt to authenticate to the specified team using SSO	=
@	logout
@	prune
o	--scope	Specify package to act as entry point for pruned monorepo	v=
o	--docker	Output pruned workspace into 'fill' and 'json' directories optimized for Docker layer caching	
@	unlink
@	run
o	--scope	Specify packages to act as entry points for task execution	v=
o	--cache-dir	Specify local filesystem cache directory	v=
o	--concurrency	Limit the concurrency of task execution (use `1` for serial)	v=
o	--continue	Continue execution even if a task exits with an error	
o	--force	Ignore the existing cache	
o	--graph	Generate a Dot graph of the task execution	
o	--global-deps	Specify glob of global filesystem dependencies to be hashed (useful for .env and files in the root…	v=
o	--since	Limit/set scope to changed packages since a mergebase	v=
o	--team	The slug of a turborepo.com team	v=
o	--token	A turborepo.com access token	v=
o	--ignore	Files to ignore when calculating changed files (supports globs)	v=
o	--profile	File to write turbo's performance profile into	v=
o	--parallel	Execute all tasks in parallel	
o	--include-dependencies	Include the dependencies of tasks in execution	
o	--no-deps	Exclude dependent task consumers from execution	
o	--no-cache	Avoid saving task results to the cache (useful for development/watch tasks)	
o	--output-logs		v=
o	--dry|--dry-run	List the packages in scope and the tasks that would be run	V=
a	1	1
=	run	--cache-dir
t	folders
=	run	--since
d
=	run	--profile
t	filepaths
=	run	--output-logs
v	new-only	Only new output with hashes for cached tasks
v	hash-only	Only turbo-computed task hashes
v	full	Show all output
v	none	Hide process output
=	run	--dry
v	json	
#	run	1
d
