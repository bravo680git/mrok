@	
s	about	Shows information about poetry
s	add	Adds a new dependency to pyproject.toml
s	build	Builds a package, as a tarball and a wheel by default
s	cache	The cache command regroups sub commands to interact with poetry's cache
s	check	Checks the validity of the pyproject.toml file
s	config	Manages configuration settings
s	debug	The debug command regroups sub commands to interact with debug session
s	env	The env command regroups sub commands to interact with the virtualenvs associated with a specific…
s	init	Creates a basic pyproject.toml file in the current directory
s	install	Installs the project dependencies
s	lock	Locks the project dependencies
s	new	Creates a new Python project at <path>
s	publish	Publishes a package to a remote repository
s	remove	Removes a package from the project dependencies
s	run	Runs a command in the appropriate environment
s	search	Searches for packages on remote repositories
s	self	The self namespace regroups sub commands to manage the poetry installation itself
s	shell	Spawns a shell within the virtual environment
s	show	Shows information about packages
s	source	The source namespace regroups sub commands to manage repository sources for a poetry project
s	update	Update the dependencies as according to the pyproject.toml file
s	version	Shows the version of the project or bumps it when a valid bump rule is provided
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
@	about
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
@	add
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--group	The group to add the dependency to	
o	--dev	Add as a development dependency. (Deprecated) Use --group=dev instead	
o	--editable	Add vcs/path dependencies as editable	
o	--extras	Extras to activate for the dependency	
o	--optional	Add as an optional dependency	
o	--python	Python version for which the dependency must be installed	
o	--platform	Platforms for which the dependency must be installed	
o	--source	Name of the source to use to install the package	
o	--allow-prereleases	Accept prereleases	
o	--dry-run	Output the operations but do not execute anything (implicitly enables --verbose)	
o	--lock	Do not perform operations (only update the lockfile)	
a	1	0
@	build
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--format	Limit the format to either sdist or wheel	
@	cache
s	clear	Clears a poetry cache by name
s	list	List poetry's caches
@	cache clear
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--all	Clear all entries in the cache	
a	1	0
@	cache list
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
@	check
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
@	config
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--list	List configuration settings	
o	--unset	Unset configuration setting	
o	--local	Set/Get from the project's local configuration	
a	2	0
@	debug
s	info	Shows debug information
s	resolve	Debugs dependency resolution
@	debug info
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
@	debug resolve
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--extras	Extras to activate for the dependency	
o	--python	Python version(s) to use for resolution	
o	--tree	Display the dependency tree	
o	--install	Show what would be installed for the current system	
a	1	0
@	env
s	info	Displays information about the current environment
s	list	Lists all virtualenvs associated with the current project
s	remove	Remove virtual environments associated with the project
s	use	Activates or creates a new virtualenv for the current project
@	env info
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--path	Only display the environment's path	
o	--executable	Only display the environment's python executable path	
@	env list
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--full-path	Output the full paths of the virtualenvs	
@	env remove
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--all	Remove all managed virtual environments associated with the project	
a	1	0
@	env use
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
a	1	0
@	init
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--name	Name of the package	
o	--description	Description of the package	
o	--author	Author name of the package	
o	--python	Compatible Python versions	
o	--dependency	Package to require, with an optional version constraint, e.g. requests:^2.10.0 or requests=2.11.1	
o	--dev-dependency	Package to require for development, with an optional version constraint, e.g. requests:^2.10.0 or…	
o	--license	License of the package	
@	install
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--without	The dependency groups to ignore	
o	--with	The optional dependency groups to include	
o	--only	The only dependency groups to include	
o	--no-dev	Do not install the development dependencies. (Deprecated)	
o	--sync	Synchronize the environment with the locked packages and the specified groups	
o	--no-root	Do not install the root package (the current project)	
o	--no-directory	Do not install any directory path dependencies; useful to install dependencies without source…	
o	--dry-run	Output the operations but do not execute anything (implicitly enables --verbose)	
o	--remove-untracked	Removes packages not present in the lock file. (Deprecated)	
o	--extras	Extra sets of dependencies to install	
o	--all-extras	Install all extra dependencies	
o	--only-root	Exclude all dependencies	
o	--compile	Compile Python source files to bytecode. (This option has no effect if modern-installation is…	
@	lock
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--no-update	Do not update locked versions, only refresh lock file	
o	--check	Check that the poetry.lock file corresponds to the current version of pyproject.toml	
@	new
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--name	Set the resulting package name	
o	--src	Use the src layout for the project	
o	--readme	Specify the readme file format. One of md (default) or rst	
a	1	0
@	publish
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--repository	The repository to publish the package to	
o	--username	The username to access the repository	
o	--password	The password to access the repository	
o	--cert	Certificate authority to access the repository	
o	--client-cert	Client certificate to access the repository	
o	--build	Build the package before publishing	
o	--dry-run	Perform all actions except upload the package	
o	--skip-existing	Ignore errors from files already existing in the repository	
@	remove
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--group	The group to remove the dependency from	
o	--dev	Remove a package from the development dependencies. (Deprecated) Use --group=dev instead	
o	--dry-run	Output the operations but do not execute anything (implicitly enables --verbose)	
o	--lock	Do not perform operations (only update the lockfile)	
a	1	0
@	run
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
a	1	0
@	search
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
a	1	0
@	self
s	add	Add additional packages to poetry's runtime environment
s	install	Install locked packages (incl. addons) required by this poetry installation
s	lock	Lock the poetry installation's system requirements
s	remove	Remove additional packages from poetry's runtime environment
s	show	Show packages from poetry's runtime environment
s	update	Updates poetry to the latest version
@	self add
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--editable	Add vcs/path dependencies as editable	
o	--extras	Extras to activate for the dependency	
o	--source	Name of the source to use to install the package	
o	--allow-prereleases	Accept prereleases	
o	--dry-run	Output the operations but do not execute anything (implicitly enables --verbose)	
a	1	0
@	self install
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--sync	Synchronize the environment with the locked packages and the specified groups	
o	--dry-run	Output the operations but do not execute anything (implicitly enables --verbose)	
@	self lock
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--no-update	Do not update locked versions, only refresh lock file	
o	--check	Check that the poetry.lock file corresponds to the current version of pyproject.toml	
@	self remove
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--dry-run	Output the operations but do not execute anything (implicitly enables --verbose)	
a	1	0
@	self show
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--addons	List only add-on packages installed	
o	--tree	List the dependencies as a tree	
o	--latest	Show the latest version	
o	--outdated	Show the latest version but only for packages that are outdated	
a	1	0
@	self update
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--preview	Allow the installation of pre-release versions	
o	--dry-run	Output the operations but do not execute anything (implicitly enables --verbose)	
a	1	0
@	shell
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
@	show
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--without	The dependency groups to ignore	
o	--with	The optional dependency groups to include	
o	--only	The only dependency groups to include	
o	--no-dev	Do not list the development dependencies. (Deprecated)	
o	--tree	List the dependencies as a tree	
o	--why	When showing the full list, or a --tree for a single package, also display why it's included	
o	--latest	Show the latest version	
o	--outdated	Show the latest version but only for packages that are outdated	
o	--all	Show all packages (even those not compatible with current system)	
o	--top-level	Show only top-level dependencies	
a	1	0
@	source
s	add	Add source configuration for project
s	remove	Remove source configured for the project
s	show	Show information about sources configured for the project
@	source add
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--default	Set this source as the default (disable PyPI). A default source will also be the fallback source…	
o	--secondary	Set this source as secondary. (Deprecated, use --priority)	
o	--priority	Set the priority of this source. One of: default, primary, secondary, supplemental, explicit…	
a	2	0
@	source remove
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
a	1	0
@	source show
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
a	1	0
@	update
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--without	The dependency groups to ignore	
o	--with	The optional dependency groups to include	
o	--only	The only dependency groups to include	
o	--no-dev	Do not update the development dependencies. (Deprecated)	
o	--dry-run	Output the operations but do not execute anything (implicitly enables --verbose)	
o	--lock	Do not perform operations (only update the lockfile)	
a	1	0
@	version
o	-h|--help	Display help information	
o	-v|--verbose	Increase the verbosity of messages	
o	-vv	More verbose output	
o	-vvv	Debug output	
o	-V|--version	Display this application version	
o	--ansi	Force ANSI output	
o	--no-ansi	Disable ANSI output	
o	-n|--no-interaction	Do not ask any interactive question	
o	--no-plugins	Disables plugins	
o	--no-cache	Disables poetry source caches	
o	--directory	The working directory for the poetry command	v
o	-q|--quiet	Do not output any message	
o	--short	Output the version number only	
o	--dry-run	Do not update pyproject.toml file	
a	1	0
