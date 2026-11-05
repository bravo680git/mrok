@	
s	activate	Activate an environment
s	deactivate	Deactivate an environment
s	clean	Remove unused packages and caches
s	compare	Compare packages between conda environments
s	create	Create a new conda environment from a list of specified packages
s	info	Display information about current conda install
s	init	Initialize conda for shell interaction. [Experimental]
s	install	Installs a list of packages into a specified conda environment
s	list	List linked packages in a conda environment
s	package	Low-level conda package utility. (EXPERIMENTAL)
s	remove	Remove a list of packages from a specified conda environment
s	uninstall	Alias for remove
s	run	Run an executable in a conda environment
s	search	Search for packages and display associated information. The input is a MatchSpec, a query language…
s	update	Updates conda packages to the latest compatible version
s	upgrade	Alias for update
s	repoquery	Query repositories using mamba
s	env	Manage environments
o	--help|-h	Show help for mamba and exit	
o	--version|-V	Show the conda version number and exit	
@	activate
o	--stack	Stack the environment being activated on top of the previous active environment	
o	--no-stack	Do not stack the environment. Overrides 'auto_stack' setting	
a	1	0
#	activate	1
d
@	deactivate
@	clean
o	-a|--all	Remove index cache, lock files, unused cache packages, and tarballs	
o	-i|--index-cache	Remove index cache	
o	-p|--packages	Remove unused packages from writable package caches	
o	-t|--tarballs	Remove cached package tarballs	
o	-f|--force-pkgs-dirs	Remove all writable package caches	
o	-l|--logfiles	Remove log files	
o	--locks	Remove lock files	
o	-c|--tempfiles	Remove temporary files that could not be deleted earlier due to being in-use. Argument is path(s)…	v
o	-d|--dry-run	Only display what would have been done	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-q|--quiet	Do not display progress bar	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-y|--yes	Do not ask for confirmation	
=	clean	-c
t	filepaths
@	compare
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
o	-h|--help	Show this help message and exit	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-v|--verbose	Use once for info, twice for debug, three times for trace	
o	-q|--quiet	Do not display progress bar	
a	1	0
=	compare	-p
t	filepaths
#	compare	1
t	filepaths
@	create
o	--clone	Path to (or name of) existing local environment	v
o	--file	Read package versions from the given file. Repeated file specifications can be passed (e.g…	v
o	--dev	Use sys.executable -m conda in wrapper scripts instead of CONDA_EXE. This is mainly for use during…	
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	--strict-channel-priority	Packages in lower priority channels are not considered if a package with the same name appears in…	
o	--no-channel-priority	Package version takes precedence over channel priority. Overrides the value given by conda config…	
o	--no-deps	Do not install, update, remove, or change dependencies. This WILL lead to broken environments and…	
o	--only-deps	Only install dependencies	
o	--no-pin	Ignore pinned file	
o	--no-default-packages	Ignore create_default_packages in the .condarc file	
o	--copy	Install all packages using copies instead of hard- or soft-linking	
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	-d|--dry-run	Only display what would have been done	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-q|--quiet	Do not display progress bar	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-y|--yes	Do not ask for confirmation	
o	--download-only	Solve an environment and ensure package caches are populated, but exit prior to unlinking and…	
o	--show-channel-urls	Show channel urls. Overrides the value given by conda config --show show_channel_urls	
a	1	1
=	create	--clone
d
=	create	--file
t	filepaths
=	create	-p
t	filepaths
@	info
o	-a|--all	Show all information	
o	--base	Display base environment path	
o	-e|--envs	List all known conda environments	
o	-s|--system	List environment variables	
o	--unsafe-channels	Display list of channels with tokens exposed	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-v|--verbose	Use once for info, twice for debug, three times for trace	
o	-q|--quiet	Do not display progress bar	
@	init
@	install
o	--revision	Revert to the specified REVISION	v
o	--file	Read package versions from the given file. Repeated file specifications can be passed (e.g…	v
o	--dev	Use sys.executable -m conda in wrapper scripts instead of CONDA_EXE. This is mainly for use during…	
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	--strict-channel-priority	Packages in lower priority channels are not considered if a package with the same name appears in…	
o	--no-channel-priority	Package version takes precedence over channel priority. Overrides the value given by conda config…	
o	--no-deps	Do not install, update, remove, or change dependencies. This WILL lead to broken environments and…	
o	--only-deps	Only install dependencies	
o	--no-pin	Ignore pinned file	
o	--force-reinstall	Ensure that any user-requested package for the current operation is uninstalled and reinstalled…	
o	--freeze-installed|--no-update-deps	Do not update or change already-installed dependencies	
o	--update-deps	Update dependencies	
o	-S|--satisfied-skip-solve	Exit early and do not run the solver if the requested specs are satisfied. Also skips aggressive…	
o	--update-all|--all	Update all installed packages in the environment	
o	--update-specs	Update based on provided specifications	
o	--copy	Install all packages using copies instead of hard- or soft-linking	
o	-m|--mkdir	Create the environment directory if necessary	
o	--clobber	Allow clobbering of overlapping file paths within packages, and suppress related warnings	
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	-d|--dry-run	Only display what would have been done	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-q|--quiet	Do not display progress bar	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-y|--yes	Do not ask for confirmation	
o	--download-only	Solve an environment and ensure package caches are populated, but exit prior to unlinking and…	
o	--show-channel-urls	Show channel urls. Overrides the value given by conda config --show show_channel_urls	
a	1	1
=	install	--file
t	filepaths
=	install	-p
t	filepaths
#	install	1
d
@	list
o	--show-channel-urls	Show channel urls. Overrides the value given by conda config --show show_channel_urls	
o	-c|--canonical	Output canonical names of packages only. Implies --no-pip	
o	-f|--full-name	Only search for full names, i.e., ^<regex>$	
o	--explicit	List explicitly all installed conda packaged with URL (output may be used by conda create --file)	
o	--md5	Add MD5 hashsum when using --explicit	
o	-e|--export	Output requirement string only (output may be used by conda create --file)	
o	-r|--revisions	List the revision history and exit	
o	--no-pip	Do not include pip-only installed packages	
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-v|--verbose	Use once for info, twice for debug, three times for trace	
o	-q|--quiet	Do not display progress bar	
a	1	0
=	list	-p
t	filepaths
@	package
o	-w|--which	Given some PATH print which conda package the file came from	v
o	-r|--reset	Remove all untracked files and exit	
o	-u|--untracked	Display all untracked files and exit	
o	--pkg-name	Package name of the created package	v
o	--pkg-version	Package version of the created package	v
o	--pkg-build	Package build number of the created package	v
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
=	package	-p
t	filepaths
@	remove
o	--dev	Use sys.executable -m conda in wrapper scripts instead of CONDA_EXE. This is mainly for use during…	
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	--all	Remove all packages, i.e., the entire environment	
o	--features	Remove features (instead of packages)	
o	--force-remove|--force	Forces removal of a package without removing packages that depend on it. Using this option will…	
o	--no-pin	Ignore pinned file	
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	-d|--dry-run	Only display what would have been done	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-q|--quiet	Do not display progress bar	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-y|--yes	Do not ask for confirmation	
a	1	1
=	remove	-p
t	filepaths
#	remove	1
d
@	uninstall
o	--dev	Use sys.executable -m conda in wrapper scripts instead of CONDA_EXE. This is mainly for use during…	
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	--all	Remove all packages, i.e., the entire environment	
o	--features	Remove features (instead of packages)	
o	--force-remove|--force	Forces removal of a package without removing packages that depend on it. Using this option will…	
o	--no-pin	Ignore pinned file	
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	-d|--dry-run	Only display what would have been done	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-q|--quiet	Do not display progress bar	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-y|--yes	Do not ask for confirmation	
a	1	1
=	uninstall	-p
t	filepaths
#	uninstall	1
d
@	run
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
o	-v|--verbose	Use once for info, twice for debug, three times for trace	
o	--dev	Sets `CONDA_EXE` to `python -m conda`, assuming the CWD contains the root of conda development…	
o	--debug-wrapper-scripts	When this is set, where implemented, the shell wrapper scripts will echo to stderr a lot of…	
o	--cwd	Current working directory for command to run in. Defaults to cwd	v
o	--no-capture-output	Don't capture stdout/stderr	
o	--live-stream	Display the output for the subprocess stdout and stderr on real time	
a	1	0
=	run	-p
t	filepaths
=	run	--cwd
t	folders
#	run	1
t	filepaths
@	search
o	--envs	Search all of the current user's environments. If run as Administrator (on Windows) or UID 0 (on…	
o	-i|--info	Provide detailed information about each package	
o	--subdir|--platform	Search the given subdir. Should be formatted like 'osx-64', 'linux-32', 'win-64', and so on. The…	v
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-v|--verbose	Use once for info, twice for debug, three times for trace	
o	-q|--quiet	Do not display progress bar	
a	1	0
@	update
o	--file	Read package versions from the given file. Repeated file specifications can be passed (e.g…	v
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	--strict-channel-priority	Packages in lower priority channels are not considered if a package with the same name appears in…	
o	--no-channel-priority	Package version takes precedence over channel priority. Overrides the value given by conda config…	
o	--no-deps	Do not install, update, remove, or change dependencies. This WILL lead to broken environments and…	
o	--only-deps	Only install dependencies	
o	--no-pin	Ignore pinned file	
o	--force-reinstall	Ensure that any user-requested package for the current operation is uninstalled and reinstalled…	
o	--freeze-installed|--no-update-deps	Do not update or change already-installed dependencies	
o	--update-deps	Update dependencies	
o	-S|--satisfied-skip-solve	Exit early and do not run the solver if the requested specs are satisfied. Also skips aggressive…	
o	--update-all|--all	Update all installed packages in the environment	
o	--update-specs	Update based on provided specifications	
o	--copy	Install all packages using copies instead of hard- or soft-linking	
o	--clobber	Allow clobbering of overlapping file paths within packages, and suppress related warnings	
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	-d|--dry-run	Only display what would have been done	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-q|--quiet	Do not display progress bar	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-y|--yes	Do not ask for confirmation	
o	--download-only	Solve an environment and ensure package caches are populated, but exit prior to unlinking and…	
o	--show-channel-urls	Show channel urls. Overrides the value given by conda config --show show_channel_urls	
a	1	1
=	update	--file
t	filepaths
=	update	-p
t	filepaths
#	update	1
v	mamba	Update mamba
d
@	upgrade
o	--file	Read package versions from the given file. Repeated file specifications can be passed (e.g…	v
o	-n|--name	Name of environment	v
o	-p|--prefix	Full path to environment location (i.e. prefix)	v
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	--strict-channel-priority	Packages in lower priority channels are not considered if a package with the same name appears in…	
o	--no-channel-priority	Package version takes precedence over channel priority. Overrides the value given by conda config…	
o	--no-deps	Do not install, update, remove, or change dependencies. This WILL lead to broken environments and…	
o	--only-deps	Only install dependencies	
o	--no-pin	Ignore pinned file	
o	--force-reinstall	Ensure that any user-requested package for the current operation is uninstalled and reinstalled…	
o	--freeze-installed|--no-update-deps	Do not update or change already-installed dependencies	
o	--update-deps	Update dependencies	
o	-S|--satisfied-skip-solve	Exit early and do not run the solver if the requested specs are satisfied. Also skips aggressive…	
o	--update-all|--all	Update all installed packages in the environment	
o	--update-specs	Update based on provided specifications	
o	--copy	Install all packages using copies instead of hard- or soft-linking	
o	--clobber	Allow clobbering of overlapping file paths within packages, and suppress related warnings	
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	-d|--dry-run	Only display what would have been done	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-q|--quiet	Do not display progress bar	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-y|--yes	Do not ask for confirmation	
o	--download-only	Solve an environment and ensure package caches are populated, but exit prior to unlinking and…	
o	--show-channel-urls	Show channel urls. Overrides the value given by conda config --show show_channel_urls	
a	1	1
=	upgrade	--file
t	filepaths
=	upgrade	-p
t	filepaths
#	upgrade	1
v	mamba	Update mamba
d
@	repoquery
s	search	Search for packages and display associated information. The input is a MatchSpec, a query language…
s	depends	List dependencies for a package
s	whoneeds	List packages that require a given package
@	repoquery search
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform 'insecure SSL' connections and transfers. Equivalent to setting…	
o	--offline	Offline mode. Don't connect to the Internet	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-q|--quiet	Do not display progress bar	
a	1	0
#	repoquery search	1
v	xtensor>=0.18	Search for xtensor version which is more than 0.18
d
@	repoquery depends
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform 'insecure SSL' connections and transfers. Equivalent to setting…	
o	--offline	Offline mode. Don't connect to the Internet	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-q|--quiet	Do not display progress bar	
a	1	0
#	repoquery depends	1
v	xtensor	List dependencies for xtensor package
d
@	repoquery whoneeds
o	-c|--channel	They are given (including local directories using the 'file://' syntax or simply a path like…	v
o	--use-local	Use locally built packages. Identical to '-c local'	
o	--override-channels	Do not search default or .condarc channels. Requires --channel	
o	--repodata-fn	Specify name of repodata on remote server. Conda will try whatever you specify, but will…	v
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform insecure SSL connections and transfers. Equivalent to setting 'ssl_verify'…	
o	--offline	Offline mode. Don't connect to the Internet	
o	-C|--use-index-cache	Use cache of channel index files, even if it has expired	
o	-k|--insecure	Allow conda to perform 'insecure SSL' connections and transfers. Equivalent to setting…	
o	--offline	Offline mode. Don't connect to the Internet	
o	--json	Report all output as json. Suitable for using conda programmatically	
o	-v|--verbose	Can be used multiple times. Once for INFO, twice for DEBUG, three times for TRACE	
o	-q|--quiet	Do not display progress bar	
a	1	0
#	repoquery whoneeds	1
v	xtl	List packages that require xtl package
@	env
s	list	List environments
@	env list
a	1	0
#	env list	1
d
