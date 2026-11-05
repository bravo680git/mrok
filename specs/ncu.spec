@	
o	--cache	Cache versions to a local cache file. Default --cacheFile is ~/.ncu-cache.json and default…	
o	--cacheClear	Clear the default cache, or the cache file specified by --cacheFile	
o	--cacheExpiration	Cache expiration in minutes. Only works with --cache. (default: 10)	v
o	--cacheFile	Filepath for the cache file. Only works with --cache. (default: "~/.ncu-cache.json")	v
o	--color	Force color in terminal	
o	--concurrency	Max number of concurrent HTTP requests to registry. (default: 8)	v
o	--configFileName	Config file name. (default: .ncurc.{json,yml,js,cjs})	v
o	--configFilePath	Directory of .ncurc config file. (default: directory of packageFile)	v
o	--cwd	Working directory in which npm will be executed	v
o	--deep	Run recursively in current working directory. Alias of (--packageFile '**/package.json')	
o	--dep	Check one or more sections of dependencies only: dev, optional, peer, prod, or packageManager…	v
o	--deprecated	Include deprecated packages	
o	--doctor|-d	Iteratively installs upgrades and runs tests to identify breaking upgrades. Requires -u to…	
o	--doctorInstall	Specifies the install script to use in doctor mode. (default: npm install/yarn)	v
o	--doctorTest	Specifies the test script to use in doctor mode. (default: npm test)	v
o	--enginesNode	Include only packages that satisfy engines.node as specified in the package file	
o	--errorLevel|-e	Set the error level. 1: exits with error code 0 if no errors occur. 2: exits with error code 0 if…	v
o	--filter|-f	Include only package names matching the given string, wildcard, glob, comma-or-space-delimited…	v
o	--filterResults	Filters out upgrades based on a user provided function. Run "ncu --help --filterResults" for details	
o	--filterVersion	Filter on package version using comma-or-space-delimited list, /regex/, or predicate function	v
o	--format	Modify the output formatting or show additional information. Specify one or more comma-delimited…	v
o	--global|-g	Check global packages instead of in the current project	
o	--groupFunction	Customize how packages are divided into groups when using --format group. Run "ncu --help…	
o	--help|-h	Show help	
o	--interactive|-i	Enable interactive prompts for each dependency; implies -u unless one of the json options are set	
o	--jsonAll|-j	Output new package file instead of human-readable message	
o	--jsonDeps	Like jsonAll but only lists dependencies, devDependencies, optionalDependencies, etc of the new…	
o	--jsonUpgraded	Output upgraded dependencies in json	
o	--loglevel|-l	Amount to log: silent, error, minimal, warn, info, verbose, silly. (default: "warn")	v
o	--mergeConfig	Merges nested configs with the root config file for --deep or --packageFile options. (default…	
o	--minimal|-m	Do not upgrade newer versions that are already satisfied by the version range according to semver	
o	--packageData	Package file data (you can also use stdin)	v
o	--packageFile	Package file(s) location. (default: ./package.json)	v
o	--packageManager|-p	Npm, yarn, pnpm, deno, staticRegistry (default: npm). Run "ncu --help --packageManager" for details	v
o	--peer	Check peer dependencies of installed packages and filter updates to compatible versions. Run "ncu…	
o	--pre	Include prerelease versions, e.g. -alpha.0, -beta.5, -rc.2. Automatically set to 1 when --target…	v
o	--prefix	Current working directory of npm	v
o	--registry|-r	Third-party npm registry. Run "ncu --help --registry" for details	v
o	--reject|-x	Exclude packages matching the given string, wildcard, glob, comma-or-space-delimited list…	v
o	--rejectVersion	Exclude package.json versions using comma-or-space-delimited list, /regex/, or predicate function	v
o	--removeRange	Remove version ranges from the final package version	
o	--retry	Number of times to retry failed requests for package info. (default: 3)	v
o	--root	Runs updates on the root project in addition to specified workspaces. Only allowed with…	
o	--silent|-s	Don't output anything. Alias for --loglevel silent	
o	--stdin	Read package.json from stdin	
o	--target|-t	Determines the version to upgrade to: latest, newest, greatest, minor, patch, @[tag], or…	v
o	--timeout	Global timeout in milliseconds. (default: no global timeout and 30 seconds per npm-registry-fetch)	v
o	--upgrade|-u	Overwrite package file with upgraded versions instead of just outputting to console	
o	--verbose	Log additional information for debugging. Alias for --loglevel verbose	
o	--version|-v	Output the version number of npm-check-updates	
o	--workspace|-w	Run on one or more specified workspaces. Add --root to also upgrade the root project. (default: [])	v
o	--workspaces|-ws	Run on all workspaces. Add --root to also upgrade the root project	
a	1	1
=		--cacheFile
t	filepaths
=		--configFileName
t	filepaths
=		--configFilePath
t	folders
=		--cwd
t	folders
=		--dep
v	dev	
v	optional	
v	peer	
v	prod	
v	packageManager	
=		--format
v	group	
v	ownerChanged	
v	repo	
v	time	
v	lines	
=		--loglevel
v	silent	
v	error	
v	minimal	
v	warn	
v	info	
v	verbose	
v	silly	
=		--packageFile
t	filepaths
=		--packageManager
v	npm	
v	yarn	
v	pnpm	
v	deno	
v	staticRegistry	
=		--prefix
t	folders
=		--target
v	latest	
v	newest	
v	greatest	
v	minor	
v	patch	
