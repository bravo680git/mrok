@	
s	help	Help about any command
s	install|i	Install a gem into the local repository
s	cert	Manage RubyGems certificates and signing settings
s	check	Check a gem repository for added or missing files
s	cleanup	Clean up old versions of installed gems
s	contents	Display the contents of the installed gems
s	dependency	Show the dependencies of an installed gem
s	environment	Display information about the RubyGems environment
s	fetch	Download a gem and place it in the current directory
s	generate_index	Generates the index files for a gem server directory
s	info	Show information for the given gem
s	lock	Generate a lockdown list of gems
s	mirror	Mirror all gem files (requires rubygems-mirror)
s	open	Open gem sources in editor
s	pristine	Restores installed gems to pristine condition from files located in the gem cache
s	query	Query gem information in local or remote repositories
s	rdoc	Generates RDoc for pre-installed gems
s	search	Display remote gems whose name matches REGEXP
s	signin	Sign in to any gemcutter-compatible host. It defaults to https://rubygems.org
s	signout	Sign out from all the current sessions
s	sources	Manage the sources and cache file RubyGems uses to search for gems
s	specification	Display gem specification (in yaml)
s	stale	List gems along with access times
s	unpack	Unpack an installed gem to the current directory
s	yank	Remove a pushed gem from the index
s	uninstall	Uninstall gems from the local repository
s	list	Display local gems whose name matches REGEXP
s	build	Build a gem from a gemspec
s	push	Push a gem up to the gem server
s	server	Starts up a web server that hosts the RDoc (requires rubygems-server)
s	owner	Manage gem owners of a gem on the push server
s	which	Find the location of a library file you can require
s	outdated	Display all gems that need updates
s	update	Update installed gems to the latest version
o	--help|-h	Show help for gem	p
o	-V|--verbose	Set the verbose level of output	p
o	--no-verbose	Do not set the verbose level of output	p
o	-q|--quiet	Silence command progress meter	p
o	--silent	Silence RubyGems output	p
o	-config-file	Use this config file instead of default	vp
o	--backtrace	Show stack backtrace on errors	p
o	--debug	Turn on Ruby debugging	p
o	--norc	Avoid loading any .gemrc file	p
o	-v|--version	Show the gem version	
=		-config-file
t	filepaths
@	help
a	1	0
#	help	1
t	help
@	install
o	--platform	Specify the platform of gem to install	v
a	1	0
#	install	1
d
@	cert
o	-a|--add	Add a trusted certificate	v
o	-l|--list	List trusted certificates where the subject contains FILTER	V
o	-r|--remove	Remove trusted certificates where the subject contains FILTER	v
o	-b|--build	Build private key and self-signed certificate for EMAIL_ADDR	v
o	-C|--certificate	Signing certificate for --sign	v
o	-K|--private-key	Key for --sign or --build	v
o	-A|--key-algorithm	Select which key algorithm to use for --build	v
o	-s|--sign	Signs CERT with the key from -K and the certificate from -C	v
o	-d|--days	Days before the certificate expires	v
o	-R|--re-sign	Re-signs the certificate from -C with the key from -K	
=	cert	-a
t	filepaths
=	cert	-C
t	filepaths
=	cert	-K
t	filepaths
=	cert	-s
t	filepaths
@	check
o	-a|--alien	Report 'unmanaged' or rogue files in the gem repository	
o	--no-alien	Report 'managed' or rogue files in the gem repository	
o	--doctor	Clean up uninstalled gems and broken specifications	
o	--no-doctor	Do not clean up uninstalled gems and broken specifications	
o	--dry-run	Do not remove files, only report what would be removed	
o	--no-dry-run	Remove files	
o	--gems	Check installed gems for problems	
o	--no-gems	Check not installed gems for problems	
o	-v|--version	Specify version of gem to check	v
a	1	0
#	check	1
d
@	cleanup
o	-n|-d|--dry-run	Do not uninstall gems	
o	-D|--check-development	Check development dependencies while uninstalling (default: true)	
o	--no-check-development	Do not check development dependencies while uninstalling	
o	--user-install	Cleanup in user’s home directory instead of GEM_HOME	
o	--no-user-install	Cleanup in GEM_HOME instead of user’s home directory	
a	1	0
#	cleanup	1
d
@	contents
o	-v|--version	Specify version of gem to contents	v
o	--all	Contents for all gems	
o	-s|--spec-dir	Search for gems under specific paths	v
o	-l|--lib-only	Only return files in the Gem’s lib_dirs	
o	--no-lib-only	Not only return files in the Gem’s lib_dirs	
o	--prefix	Don’t include installed path prefix	
o	--no-prefix	Include installed path prefix	
o	--show-install-dir	Show only the gem install dir	
o	--no-show-install-dir	Do not show only the gem install dir	
a	1	0
=	contents	-s
t	filepaths
#	contents	1
d
@	dependency
o	-v|--version	Specify version of gem to dependency	v
o	--platform	Specify the platform of gem to dependency	v
o	--prerelease	Allow prerelease versions of a gem	
o	--no-prerelease	Do not allow prerelease versions of a gem	
o	-R|--reverse-dependencies	Include reverse dependencies in the output	
o	--no-reverse-dependencies	Do not include reverse dependencies in the output	
o	--pipe	Pipe Format (name --version ver)	
o	-l|--local	Restrict operations to the LOCAL domain	
o	-r|--remote	Restrict operations to the REMOTE domain	
o	-b|--both	Allow LOCAL and REMOTE operations	
o	-B|--bulk-threshold	Threshold for switching to bulk synchronization (default 1000)	v
o	--clear-sources	Clear the gem sources	
o	-s|--source	Append URL to list of remote gem sources	v
o	-p|--http-proxy	Use HTTP proxy for remote operations	V
o	--no-http-proxy	Do not use HTTP proxy for remote operations	
a	1	0
@	environment
a	1	0
#	environment	1
v	home	Display the path where gems are installed. Aliases: gemhome, gemdir, GEM_HOME
v	path	Display path used to search for gems. Aliases: gempath, GEM_PATH
v	user_gemhome	Display the path where gems are installed when --user-install is given. Aliases: user_gemdir
v	version	Display the gem format version
v	remotesources	Display the remote gem servers
v	platform	Display the supported gem platforms
@	fetch
o	-v|--version	Specify version of gem to fetch	v
o	--platform	Specify the platform of gem to fetch	v
o	--prerelease	Allow prerelease versions of a gem	
o	--no-prerelease	Do not allow prerelease versions of a gem	
o	--suggestions	Suggest alternates when gems are not found	
o	--no-suggestions	Do not suggest alternates when gems are not found	
o	-B|--bulk-threshold	Threshold for switching to bulk synchronization (default 1000)	v
o	-s|--source	Append URL to list of remote gem sources	v
o	--clear-sources	Clear the gem sources	
o	-p|--http-proxy	Use HTTP proxy for remote operations	V
o	--no-http-proxy	Do not use HTTP proxy for remote operations	
a	1	0
#	fetch	1
d
@	generate_index
o	-d|--directory	Repository base dir containing gems subdir	v=
o	--modern	Generate indexes for RubyGems (always true)	
o	--no-modern	Do not generate indexes for RubyGems	
o	--update	Update modern indexes with gems added since the last update	
=	generate_index	-d
t	folders
@	info
o	-I	Equivalent to --no-installed	
o	-a|--all	Display all gem versions	
o	-e|--exact	Name of gem(s) to query on matches the provided STRING	
o	--prerelease	Allow prerelease versions of a gem	
o	--no-prerelease	Do not allow prerelease versions of a gem	
o	-i|--installed	Check for installed gem	
o	-I|--no-installed	Check for not installed gem	
o	-v|--version	Specify version of gem to list for use with --installed	v
o	--versions	Display only gem names	
o	--no-versions	Display not only gem names	
a	1	0
#	info	1
d
@	lock
o	-s|--strict	Fail if unable to satisfy a dependency	
o	--no-strict	Do not fail if unable to satisfy a dependency	
a	1	0
@	mirror
@	open
o	-e|--editor	Prepends COMMAND to gem path. Could be used to specify editor	v
o	-v|--version	Opens specific gem version	v
a	1	0
#	open	1
d
@	pristine
o	--all	Restore all installed gems to pristine condition	
o	--skip	Restore all installed gems to pristine condition	v=
o	--extensions	Restore gems with extensions in addition to regular gems	
o	--no-extensions	Do not restore gems with extensions in addition to regular gems	
o	--only-executables	Only restore executables	
o	--only-plugins	Only restore plugins	
o	-E|--env-shebang	Rewrite executables with a shebang of /usr/bin/env	
o	--no-env-shebang	Do not rewrite executables with a shebang of /usr/bin/env	
o	-i|--install-dir	Gem repository to get binstubs and plugins installed	v
o	-n|--bindir	Directory where executables are located	v
o	-v|--version	Specify version of gem to restore to pristine condition	v
a	1	0
=	pristine	--skip
d
=	pristine	-i
t	folders
=	pristine	-n
t	folders
#	pristine	1
d
@	query
o	-n|--name-matches	Name of gem(s) to query on matches the provided REGEXP	v
o	-I	Equivalent to --no-installed	
o	-d|--details	Display detailed information of gem(s)	
o	--no-details	Do not display detailed information of gem(s)	
o	-a|--all	Display all gem versions	
o	-e|--exact	Name of gem(s) to query on matches the provided STRING	
o	--prerelease	Allow prerelease versions of a gem	
o	--no-prerelease	Do not allow prerelease versions of a gem	
o	-i|--installed	Check for installed gem	
o	-I|--no-installed	Check for not installed gem	
o	-v|--version	Specify version of gem to list for use with --installed	v
o	--versions	Display only gem names	
o	--no-versions	Display not only gem names	
o	-l|--local	Restrict operations to the LOCAL domain	
o	-r|--remote	Restrict operations to the REMOTE domain	
o	-b|--both	Allow LOCAL and REMOTE operations	
o	-B|--bulk-threshold	Threshold for switching to bulk synchronization (default 1000)	v
o	--clear-sources	Clear the gem sources	
o	-s|--source	Append URL to list of remote gem sources	v
o	-p|--http-proxy	Use HTTP proxy for remote operations	V
o	--no-http-proxy	Do not use HTTP proxy for remote operations	
@	rdoc
o	--all	Generate RDoc/RI documentation for all installed gems	
o	--rdoc	Generate RDoc HTML	
o	--no-rdoc	Do not generate RDoc HTML	
o	--ri	Generate RI data	
o	--no-ri	Do not generate RI data	
o	--overwrite	Overwrite installed documents	
o	--no-overwrite	Do not overwrite installed documents	
o	-v|--version	Specify version of gem to rdoc	v
a	1	0
#	rdoc	1
d
@	search
o	-I	Equivalent to --no-installed	
o	-d|--details	Display detailed information of gem(s)	
o	--no-details	Do not display detailed information of gem(s)	
o	-a|--all	Display all gem versions	
o	-e|--exact	Name of gem(s) to query on matches the provided STRING	
o	--prerelease	Allow prerelease versions of a gem	
o	--no-prerelease	Do not allow prerelease versions of a gem	
o	-i|--installed	Check for installed gem	
o	-I|--no-installed	Check for not installed gem	
o	-v|--version	Specify version of gem to list for use with --installed	v
o	--versions	Display only gem names	
o	--no-versions	Display not only gem names	
o	-l|--local	Restrict operations to the LOCAL domain	
o	-r|--remote	Restrict operations to the REMOTE domain	
o	-b|--both	Allow LOCAL and REMOTE operations	
o	-B|--bulk-threshold	Threshold for switching to bulk synchronization (default 1000)	v
o	--clear-sources	Clear the gem sources	
o	-s|--source	Append URL to list of remote gem sources	v
o	-p|--http-proxy	Use HTTP proxy for remote operations	V
o	--no-http-proxy	Do not use HTTP proxy for remote operations	
a	1	0
@	signin
o	--host	Use another gemcutter-compatible host (e.g. https://rubygems.org)	v
o	--otp	Digit code for multifactor authentication You can also use the environment variable…	v
@	signout
@	sources
o	-a|--add	Add source	v
o	-l|--list	List sources	
o	-r|--remove	Remove source	v
o	-c|--clear-all	Remove all sources (clear the cache)	
o	-u|--update	Update source cache	
o	-f|--force	Do not show any confirmation prompts and behave as if 'yes' was always answered	
o	--no-force	Show any confirmation prompts and behave as if 'yes' was always answered	
o	-p|--http-proxy	Use HTTP proxy for remote operations	V
o	--no-http-proxy	Do not use HTTP proxy for remote operations	
@	specification
o	-v|--version	Specify version of gem to examine	v
o	--platform	Specify the platform of gem to specification	v
o	--prerelease	Allow prerelease versions of a gem	
o	--no-prerelease	Do not allow prerelease versions of a gem	
o	--all	Output specifications for all versions of the gem	
o	--ruby	Output ruby format	
o	--yaml	Output YAML format	
o	--marshal	Output Marshal format	
a	2	0
#	specification	1
d
@	stale
@	unpack
o	--target	Target directory for unpacking	v=
o	--spec	Unpack the gem specification	
o	-v|--version	Specify version of gem to unpack	v
a	1	0
=	unpack	--target
t	folders
#	unpack	1
d
@	yank
o	-v|--version	Specify version of gem to dependency	v
o	--platform	Specify the platform of gem to dependency	v
o	--host	Use another gemcutter-compatible host (e.g. https://rubygems.org)	v
o	-k|--key	Use the given API key	v
o	--otp	Digit code for multifactor authentication You can also use the environment variable…	v
a	1	0
#	yank	1
d
@	uninstall
o	-a|--all	Uninstall all matching versions	
o	-I|--ignore-dependencies	Ignore dependency requirements while uninstalling	
o	-D|--check-development	Check development dependencies while uninstalling (default: false)	
o	-x|--executables	Uninstall applicable executables without confirmation	
o	-i|--install-dir	Directory to uninstall gem from	v
o	-n|--bindir	Directory to remove executables from	v
o	--user-install	Uninstall from user’s home directory in addition to GEM_HOME	
o	--format-executable	Assume executable names match Ruby’s prefix and suffix	
o	--force	Uninstall all versions of the named gems ignoring dependencies	
o	--abort-on-dependent	Prevent uninstalling gems that are depended on by other gems	
o	-v|--version	Specify version of gem to uninstall	v
o	--platform	Specify the platform of gem to uninstall	v
o	--vendor	Uninstall gem from the vendor directory. Only for use by gem repackagers	
a	1	0
=	uninstall	-i
t	folders
=	uninstall	-n
t	folders
#	uninstall	1
d
@	list
o	-d|--details	Display detailed information of gem(s)	
o	--no-details	Do not display detailed information of gem(s)	
o	-u|--update-sources	[Deprecated] Update local source cache	
o	--no-update-sources	[Deprecated] Do not update local source cache	
o	-a|--all	Display all gem versions	
o	-e|--exact	Name of gem(s) to query on matches the provided STRING	
o	--prerelease	Allow prerelease versions of a gem	
o	--no-prerelease	Do not allow prerelease versions of a gem	
o	-i|--installed	Check for installed gem	
o	-I|--no-installed	Check for not installed gem	
o	-v|--version	Specify version of gem to list for use with --installed	v
o	--versions	Display only gem names	
o	--no-versions	Display not only gem names	
o	-l|--local	Restrict operations to the LOCAL domain	
o	-r|--remote	Restrict operations to the REMOTE domain	
o	-b|--both	Allow LOCAL and REMOTE operations	
o	-B|--bulk-threshold	Threshold for switching to bulk synchronization (default 1000)	v
o	--clear-sources	Clear the gem sources	
o	-s|--source	Append URL to list of remote gem sources	v
o	-p|--http-proxy	Use HTTP proxy for remote operations	V
o	--no-http-proxy	Do not use HTTP proxy for remote operations	
a	1	0
@	build
o	--platform	Specify the platform of gem to build	v
o	--force	Skip validation of the spec	
o	--strict	Consider warnings as errors when validating the spec	
o	-o|--output	Output gem with the given filename	v
o	-C	Run as if gem build was started in <PATH> instead of the current working directory	v
a	1	0
=	build	-C
t	folders
@	push
o	--host	Use another gemcutter-compatible host (e.g. https://rubygems.org)	v
o	-k|--key	Use the given API key	v
o	--otp	Digit code for multifactor authentication You can also use the environment variable…	v
o	-p|--http-proxy	Use HTTP proxy for remote operations	V
o	--no-http-proxy	Do not use HTTP proxy for remote operations	
a	1	0
@	server
@	owner
o	-a|--add	Add an owner by user identifier	v
o	-r|--remove	Remove an owner by user identifier	v
o	--host	Use another gemcutter-compatible host (e.g. https://rubygems.org)	v
o	-k|--key	Use the given API key	v
o	--otp	Digit code for multifactor authentication You can also use the environment variable…	v
a	1	0
#	owner	1
d
@	which
o	-a|--all	Show all matching files	
o	-g|--gems-first	Search gems before non-gems	
a	1	0
#	which	1
t	filepaths
@	outdated
o	--platform	Specify the platform of gem to outdated	v
@	update
o	--system	Update the RubyGems system software	V
o	--platform	Update the RubyGems system software	v
o	--prerelease	Allow prerelease versions of a gem as update targets	
o	--install-dir|-i	Gem repository directory to get installed gems	v
o	--bindir|-n	Directory where executables will be placed when the gem is installed	v
o	--document	Generate documentation for installed gems	v
o	--build-root	Temporary installation root. Useful for building packages. Do not use this when installing remote…	v
o	--vendor	Install gem into the vendor directory. Only for use by gem repackagers	
o	--no-document|-N	Disable documentation generation	
o	--env-shebang|-E	Rewrite the shebang line on installed scripts to use /usr/bin/env	
o	--force|-f	Force gem to install, bypassing dependency checks	
o	--wrappers|-w	Use bin wrappers for executables. Not available on dosish platforms	
o	--trust-policy|-P	Specify gem trust policy	v
o	--ignore-dependencies	Do not install any required dependent gems	
o	--format-executable	Make installed executable names match Ruby	
o	--user-install	Install in user's home directory instead of GEM_HOME	
o	--development	Install additional development dependencies	
o	--development-all	Install development dependencies for all gems (including dev deps themselves)	
o	--conservative	Don't attempt to upgrade gems already meeting version requirement	
o	--minimal-deps	Don't upgrade any dependencies that already meet version requirements	
o	--post-install-message	Print post install message	
o	--file|-g	Read from a gem dependencies API file and install the listed gems	v
o	--without	Omit the named groups (comma separated) when installing from a gem dependencies file	v
o	--default	Add the gem's full specification to specifications/default and extract only its bin	
o	--explain	Rather than install the gems, indicate which would be installed	
o	--lock	Create a lock file (when used with -g/--file)	
o	--suggestions	Suggest alternates when gems are not found	
a	1	1
=	update	--install-dir
t	folders
=	update	--bindir
t	folders
=	update	--document
v	rdoc	
v	ri	
=	update	--build-root
t	folders
=	update	--file
t	filepaths
