@	
s	bundlerextension	Work with Jupyter bundler extensions
s	kernel	Run a kernel locally in a subprocess
s	kernelspec	Manage Jupyter kernel specifications
s	migrate	Migrate configuration and data from .ipython prior to 4.0 to Jupyter locations
s	nbconvert	This application is used to convert notebook files (*.ipynb) to various other formats
s	nbextension	
s	notebook	Run the Jupyter notebook server
s	run	Run a notebook
s	serverextension	Manage server extensions
s	troubleshoot	Log for troubleshooting
s	trust	Manage trust
o	--help|-h	Show help for jupyter	
o	--version	Show the jupyter command's version and exit	
o	--config-dir	Show Jupyter config dir	
o	--data-dir	Show Jupyter data dir	
o	--runtime-dir	Show Jupyter runtime dir	
o	--paths	Show all Jupyter paths. Add --json for machine-readable format	
o	--json	Output paths as machine-readable json	
o	--debug	Output debug information about paths	
@	bundlerextension
s	enable	Enable a bundler extension
s	disable	Disable a bundler extension
s	list	List bundler extensions
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
o	--log-level	Set the log level by value or name	v
o	--config	Choose a config file	v
o	--user	Apply the operation only for the given user	v
o	--system	Apply the operation system-wide	
o	--sys-prefix	Use sys.prefix as the prefix for installing nbextensions (for environments, packaging)	
o	--py|--python	Install from a Python package	
=	bundlerextension	--config
t	filepaths
@	bundlerextension enable
@	bundlerextension disable
@	bundlerextension list
@	kernel
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
o	--kernel		v
o	--ip		v
@	kernelspec
s	list	
s	install	Install a kernel specification directory
s	uninstall	Alias for remove
s	remove	Remove one or more Jupyter kernelspecs by name
@	kernelspec list
o	--json	Output spec name and location as json	
@	kernelspec install
o	--log-level	Set the log level by value or name	v
o	--config	Choose a config file	v
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
a	1	0
=	kernelspec install	--config
t	filepaths
@	kernelspec uninstall
a	1	0
@	kernelspec remove
a	1	0
@	migrate
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
o	--log-level	Set the log level by value or name	v
o	--config	Choose a config file	v
o	--generate-config	Generate default config file	
o	-y	Answer yes to any questions instead of prompting	
=	migrate	--config
t	filepaths
@	nbconvert
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
o	--log-level	Set the log level by value or name	v
o	--config	Choose a config file	v
a	1	0
=	nbconvert	--config
t	filepaths
#	nbconvert	1
t	filepaths
@	nbextension
s	install	Install an nbextension
s	uninstall	Uninstall an nbextension
s	enable	Enable an nbextension
s	disable	Disable an nbextension
s	list	List nbextensions
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
o	--log-level	Set the log level by value or name	v
o	--config	Choose a config file	v
=	nbextension	--config
t	filepaths
@	nbextension install
a	1	0
@	nbextension uninstall
a	1	0
@	nbextension enable
a	1	0
@	nbextension disable
a	1	0
@	nbextension list
@	notebook
s	list	List currently running notebook servers
s	stop	Stop currently running notebook server
s	password	Set a password for the notebook server
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
o	--log-level	Set the log level by value or name	v
o	--config	Choose a config file	v
=	notebook	--config
t	filepaths
@	notebook list
@	notebook stop
@	notebook password
@	run
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
o	--log-level	Set the log level by value or name	v
o	--config	Choose a config file	v
=	run	--config
t	filepaths
@	serverextension
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
o	--log-level	Set the log level by value or name	v
o	--config	Choose a config file	v
=	serverextension	--config
t	filepaths
@	troubleshoot
@	trust
o	--debug	Set log level to logging.DEBUG (maximize logging output)	
o	-h|--help	Show this message	
o	--log-level	Set the log level by value or name	v
o	--config	Choose a config file	v
=	trust	--config
t	filepaths
