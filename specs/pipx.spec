@	
s	install	Install a package
s	inject	Installs packages to an existing pipx-managed virtual environment
s	upgrade	Upgrade a package in a pipx-managed Virtual Environment by running 'pip install --upgrade PACKAGE'
s	upgrade-all	Upgrades all packages within their virtual environments by running 'pip install --upgrade PACKAGE'
s	uninstall	Uninstalls a pipx-managed Virtual Environment by deleting it and any files that point to its apps
s	uninstall-all	Uninstall all pipx-managed packages
s	reinstall	Reinstalls a package
s	reinstall-all	Reinstalls all packages
s	list	List packages and apps installed with pipx
s	run	Download the latest version of a package to a temporary virtual environment, then run an app from it
s	runpip	Run pip in an existing pipx-managed Virtual Environment
s	ensurepath	Ensure directory where pipx stores apps is in your PATH environment variable
s	environment	Print a list of variables used in pipx.constants
s	completions	Print instructions on enabling shell completions for pipx
o	--help|-h	Show help for pipx	
@	install
o	--include-deps	Include apps of dependent packages	
o	--force	Modify existing virtual environment and files in PIPX_BIN_DIR	
o	--suffix	Optional suffix for virtual environment and executable names	v
o	--python	The Python executable used to create the Virtual Environment and run the associated app/apps. Must…	v
o	--system-site-packages	Give the virtual environment access to the system site-packages dir	
o	--index-url|-i	Base URL of Python Package Index	v
o	--editable|-e	Install a project in editable mode	
o	--pip-args	Arbitrary pip arguments to pass directly to pip install/upgrade commands	v
o	--verbose	Show verbose output	
a	1	0
@	inject
o	--include-apps	Add apps from the injected packages onto your PATH	
o	--include-deps	Include apps of dependent packages	
o	--system-site-packages	Give the virtual environment access to the system site-packages dir	
o	--index-url|-i	Base URL of Python Package Index	v
o	--editable|-e	Install a project in editable mode	
o	--pip-args	Arbitrary pip arguments to pass directly to pip install/upgrade commands	v
o	--force|-f	Modify existing virtual environment and files in PIPX_BIN_DIR	
o	--verbose	Show verbose output	
a	2	0
#	inject	1
d
@	upgrade
o	--include-injected	Also upgrade packages injected into the main app's environment	
o	--force|-f	Modify existing virtual environment and files in PIPX_BIN_DIR	
o	--system-site-packages	Give the virtual environment access to the system site-packages dir	
o	--index-url|-i	Base URL of Python Package Index	v
o	--editable|-e	Install a project in editable mode	
o	--pip-args	Arbitrary pip arguments to pass directly to pip install/upgrade commands	v
o	--verbose	Show verbose output	
a	1	0
#	upgrade	1
d
@	upgrade-all
o	--include-injected	Also upgrade packages injected into the main app's environment	
o	--skip	Skip these packages	v
o	--force|-f	Modify existing virtual environment and files in PIPX_BIN_DIR	
o	--verbose	Show verbose output	
@	uninstall
o	--verbose	Show verbose output	
a	1	0
#	uninstall	1
d
@	uninstall-all
o	--verbose	Show verbose output	
@	reinstall
o	--python	The Python executable used to recreate the Virtual Environment and run the associated app/apps…	v
o	--verbose	Show verbose output	
a	1	0
#	reinstall	1
d
@	reinstall-all
o	--python	The Python executable used to recreate the Virtual Environment and run the associated app/apps…	v
o	--skip	Skip these packages	v
o	--verbose	Show verbose output	
@	list
o	--include-injected	Show packages injected into the main app's environment	
o	--json	Output rich data in json format	
o	--short	List packages only	
o	--verbose	Show verbose output	
@	run
o	--no-cache	Do not re-use cached virtual environment if it exists	
o	--pypackages	Require app to be run from local __pypackages__ directory	
o	--spec	The package name or specific installation source passed to pip	v
o	--python	The Python version to run package's CLI app with	v
o	--system-site-packages	Give the virtual environment access to the system site-packages dir	
o	--index-url|-i	Base URL of Python Package Index	v
o	--editable|-e	Install a project in editable mode	
o	--pip-args	Arbitrary pip arguments to pass directly to pip install/upgrade commands	v
o	--verbose	Show verbose output	
a	1	1
@	runpip
o	--verbose	Show verbose output	
a	2	1
@	ensurepath
o	--force|-f	Add text to your shell's config file even if it looks like your PATH already contains paths to…	
@	environment
o	--value	Print the value of the variable	v
=	environment	--value
v	PIPX_HOME	
v	PIPX_BIN_DIR	
v	PIPX_SHARED_LIBS	
v	PIPX_LOCAL_VENVS	
v	PIPX_LOG_DIR	
v	PIPX_TRASH_DIR	
v	PIPX_VENV_CACHEDIR	
@	completions
