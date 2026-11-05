@	
s	help	Usage and help information for django-admin
s	changepassword	Change a user's password for django.contrib.auth
s	createsuperuser	Used to create a superuser
s	remove_stale_contenttypes	
s	check	Checks the entire Django project for potential problems
s	compilemessages	Compiles .po files to .mo files for use with builtin gettext support
s	createcachetable	Creates the tables needed to use the SQL cache backend
s	dbshell	Runs the command-line client for specified database, or the default database
s	diffsettings	Displays differences between the current settings.py and Django's default settings
s	dumpdata	Output the contents of the database as a fixture of the given format (using each model's default…
s	flush	Removes ALL DATA from the database, including data added during migrations
s	inspectdb	Introspects the database tables in the given database and outputs a Django
s	loaddata	Installs the named fixture(s) in the database
s	makemessages	Runs over the entire source tree of the current directory and pulls out all strings marked for…
s	makemigrations	Creates new migration(s) for apps
s	migrate	Updates database schema. Manages both apps with migrations and those without
s	sendtestemail	Sends a test email to the email addresses specified as arguments
s	shell	Runs a Python interactive interpreter. Tries to use IPython or bpython, if one of them is…
s	showmigrations	Shows all available migrations for the current project
s	sqlflush	Returns a list of the SQL statements required to return all tables in the database to the state…
s	sqlmigrate	Prints the SQL statements for the named migration
s	sqlsequencereset	Prints the SQL statements for resetting sequences for the given app name(s)
s	squashmigrations	Squashes an existing set of migrations (from first until specified) into a single new one
s	startapp	Creates a Django app directory structure for the given app name in the current directory or…
s	startproject	Creates a Django project directory structure for the given project name in the current directory…
s	test	Discover and run tests in the specified modules or the current directory
s	testserver	Runs a development server with data from the given fixture(s)
s	test_mail	
s	clearsessions	Can be run as a cronjob or directly to clean out expired sessions (only with the database backend…
s	collectstatic	Collect static files in a single location
s	findstatic	Finds the absolute paths for the given static file(s)
s	runserver	Starts a lightweight Web server for development and also serves static files
@	help
a	1	0
#	help	1
v	changepassword	Change a user's password for django.contrib.auth
v	createsuperuser	Used to create a superuser
v	remove_stale_contenttypes	
v	check	Checks the entire Django project for potential problems
v	compilemessages	Compiles .po files to .mo files for use with builtin gettext support
v	createcachetable	Creates the tables needed to use the SQL cache backend
v	dbshell	Runs the command-line client for specified database, or the default database
v	diffsettings	Displays differences between the current settings.py and Django's default settings
v	dumpdata	Output the contents of the database as a fixture of the given format (using each model's default…
v	flush	Removes ALL DATA from the database, including data added during migrations
v	inspectdb	Introspects the database tables in the given database and outputs a Django
v	loaddata	Installs the named fixture(s) in the database
v	makemessages	Runs over the entire source tree of the current directory and pulls out all strings marked for…
v	makemigrations	Creates new migration(s) for apps
v	migrate	Updates database schema. Manages both apps with migrations and those without
v	sendtestemail	Sends a test email to the email addresses specified as arguments
v	shell	Runs a Python interactive interpreter. Tries to use IPython or bpython, if one of them is…
v	showmigrations	Shows all available migrations for the current project
v	sqlflush	Returns a list of the SQL statements required to return all tables in the database to the state…
v	sqlmigrate	Prints the SQL statements for the named migration
v	sqlsequencereset	Prints the SQL statements for resetting sequences for the given app name(s)
v	squashmigrations	Squashes an existing set of migrations (from first until specified) into a single new one
v	startapp	Creates a Django app directory structure for the given app name in the current directory or…
v	startproject	Creates a Django project directory structure for the given project name in the current directory…
v	test	Discover and run tests in the specified modules or the current directory
v	testserver	Runs a development server with data from the given fixture(s)
v	test_mail	
v	clearsessions	Can be run as a cronjob or directly to clean out expired sessions (only with the database backend…
v	collectstatic	Collect static files in a single location
v	findstatic	Finds the absolute paths for the given static file(s)
v	runserver	Starts a lightweight Web server for development and also serves static files
@	changepassword
o	--database	Specifies the database to use. Default is "default"	v
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	0
=	changepassword	-v
v	0	
v	1	
v	2	
v	3	
=	changepassword	--pythonpath
t	folders
@	createsuperuser
o	--username	Specifies the login for the superuser	v
o	--noinput|--no-input	Tells Django to NOT prompt the user for input of any kind	
o	--database	Specifies the database to use. Default is "default"	v
o	--email	Specifies the email for the superuser	v
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	createsuperuser	-v
v	0	
v	1	
v	2	
v	3	
=	createsuperuser	--pythonpath
t	folders
@	remove_stale_contenttypes
o	--noinput|--no-input	Tells Django to NOT prompt the user for input of any kind	
o	--database	Nominates the database to use. Defaults to the "default" database	v
o	--include-stale-apps	Deletes stale content types including ones from previously installed apps that have been removed…	
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	remove_stale_contenttypes	-v
v	0	
v	1	
v	2	
v	3	
=	remove_stale_contenttypes	--pythonpath
t	folders
@	check
o	--tag|-t	Run only checks labeled with given tag	v
o	--list-tags	List available tags	
o	--deploy	Check deployment settings	
o	--fail-level	Message level that will cause the command to exit with a non-zero status. Default is ERROR	v
o	--database	Run database related checks against these aliases	v
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	check	--fail-level
v	CRITICAL	
v	ERROR	
v	WARNING	
v	INFO	
v	DEBUG	
=	check	-v
v	0	
v	1	
v	2	
v	3	
=	check	--pythonpath
t	folders
@	compilemessages
o	--locale|-l	Locale(s) to process (e.g. de_AT). Default is to process all. Can be used multiple times	v
o	--exclude|-x	Locales to exclude. Default is none. Can be used multiple times	v
o	--use-fuzzy|-f	Use fuzzy translations	
o	--ignore|-i	Ignore directories matching this glob-style pattern. Use multiple times to ignore more	v
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	compilemessages	-v
v	0	
v	1	
v	2	
v	3	
=	compilemessages	--pythonpath
t	folders
@	createcachetable
o	--database	Nominates a database onto which the cache tables will be installed. Defaults to the "default"…	v
o	--dry-run	Does not create the table, just prints the SQL that would be run	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	createcachetable	-v
v	0	
v	1	
v	2	
v	3	
=	createcachetable	--pythonpath
t	folders
@	dbshell
o	--database	Nominates a database onto which to open a shell	v
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	dbshell	-v
v	0	
v	1	
v	2	
v	3	
=	dbshell	--pythonpath
t	folders
@	diffsettings
o	--all	Display all settings, regardless of their value. In "hash" mode, default values are prefixed by…	
o	--default	The settings module to compare the current settings against. Leave empty to compare against…	v
o	--output	Selects the output format. 'hash' mode displays each changed setting, with the settings that don't…	v
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	diffsettings	--output
v	hash	
v	unified	
=	diffsettings	-v
v	0	
v	1	
v	2	
v	3	
=	diffsettings	--pythonpath
t	folders
@	dumpdata
o	--format	Specifies the output serialization format for fixtures	v
o	--indent	Specifies the indent level to use when pretty-printing output	v
o	--database	Nominates a specific database to dump fixtures from. Defaults to the "default" database	v
o	-e|--exclude	An app_label or app_label.ModelName to exclude (use multiple --exclude to exclude multiple…	v
o	--natural-foreign	Use natural foreign keys if they are available	
o	--natural-primary	Use natural primary keys if they are available	
o	-a|--all	Use Django's base manager to dump all models stored in the database, including those that would…	
o	--pks	Only dump objects with given primary keys. Accepts a comma-separated list of keys. This option…	v
o	-o|--output	Specifies file to which the output is written	v
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	dumpdata	-v
v	0	
v	1	
v	2	
v	3	
=	dumpdata	--pythonpath
t	folders
@	flush
o	--noinput|--no-input	Tells Django to NOT prompt the user for input of any kind	
o	--database	Nominates a database to flush. Defaults to the "default" database	v
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	flush	-v
v	0	
v	1	
v	2	
v	3	
=	flush	--pythonpath
t	folders
@	inspectdb
o	--database	Nominates a database to introspect. Defaults to using the "default" database	v
o	--include-partitions	Also output models for partition tables	
o	--include-views	Also output models for database views	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	inspectdb	-v
v	0	
v	1	
v	2	
v	3	
=	inspectdb	--pythonpath
t	folders
@	loaddata
o	--database	Nominates a specific database to load fixtures into. Defaults to the "default" database	v
o	--app	Only look for fixtures in the specified app	v
o	--ignorenonexistent|-i	Ignores entries in the serialized data for fields that do not currently exist on the model	
o	-e|--exclude	An app_label or app_label.ModelName to exclude. Can be used multiple times	v
o	--format	Format of serialized data when reading from stdin	v
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	loaddata	-v
v	0	
v	1	
v	2	
v	3	
=	loaddata	--pythonpath
t	folders
@	makemessages
o	--locale|-l	Creates or updates the message files for the given locale(s) (e.g. pt_BR). Can be used multiple…	v
o	--exclude|-x	Locales to exclude. Default is none. Can be used multiple times	v
o	--domain|-d	The domain of the message files (default: "django")	v
o	--all|-a	Updates the message files for all existing locales	
o	--extension|-e	The file extension(s) to examine (default: "html,txt,py", or "js" if the domain is "djangojs")…	v
o	--symlinks|-s	Follows symlinks to directories when examining source code and templates for translation strings	
o	--ignore|-i	Ignore files or directories matching this glob-style pattern. Use multiple times to ignore more	v
o	--no-default-ignore	Don't ignore the common glob-style patterns 'CVS', '.*', '*~' and '*.pyc'	
o	--no-wrap	Don't break long message lines into several lines	
o	--no-location	Don't write '#: filename:line' lines	
o	--add-location	[{full,file,never}] Controls '#: filename:line' lines. If the option is 'full' (the default if not…	V
o	--no-obsolete	Remove obsolete message strings	
o	--keep-pot	Keep .pot file after making messages. Useful when debugging	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	makemessages	--add-location
v	full	The lines include both file name and line number
v	file	The line number is omitted
v	never	The lines are suppressed (same as --no-location)
=	makemessages	-v
v	0	
v	1	
v	2	
v	3	
=	makemessages	--pythonpath
t	folders
@	makemigrations
o	--dry-run	Just show what migrations would be made; don't actually write them	
o	--merge	Enable fixing of migration conflicts	
o	--empty	Create an empty migration	
o	--noinput|--no-input	Tells Django to NOT prompt the user for input of any kind	
o	-n|--name	Use this name for migration file(s)	v
o	--no-header	Do not add header comments to new migration file(s)	
o	--check	Exit with a non-zero status if model changes are missing migrations	
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	makemigrations	-v
v	0	
v	1	
v	2	
v	3	
=	makemigrations	--pythonpath
t	folders
@	migrate
o	--noinput|--no-input	Tells Django to NOT prompt the user for input of any kind	
o	--database	Nominates a database to synchronize. Defaults to the "default" database	v
o	--fake	Mark migrations as run without actually running them	
o	--fake-initial	Detect if tables already exist and fake-apply initial migrations if so. Make sure that the current…	
o	--plan	Shows a list of the migration actions that will be performed	
o	--run-syncdb	Creates tables for apps without migrations	
o	--check	Exits with a non-zero status if unapplied migrations exist	
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	2	0
=	migrate	-v
v	0	
v	1	
v	2	
v	3	
=	migrate	--pythonpath
t	folders
@	sendtestemail
o	--managers	Send a test email to the addresses specified in settings.MANAGERS	
o	--admins	Send a test email to the addresses specified in settings.ADMINS	
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	sendtestemail	-v
v	0	
v	1	
v	2	
v	3	
=	sendtestemail	--pythonpath
t	folders
@	shell
o	--no-startup	When using plain Python, ignore the PYTHONSTARTUP environment variable and ~/.pythonrc.py script	
o	-i|--interface	Specify an interactive interpreter interface. Available options: "ipython", "bpython", and "python"	v
o	-c|--command	Instead of opening an interactive shell, run a command as Django and exit	v
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	shell	-i
v	ipython	
v	bpython	
v	python	
=	shell	-v
v	0	
v	1	
v	2	
v	3	
=	shell	--pythonpath
t	folders
@	showmigrations
o	--database	Nominates a database to synchronize. Defaults to the "default" database	v
o	--list|-l	Shows a list of all migrations and which are applied. With a verbosity level of 2 or above, the…	
o	--plan|-p	Shows all migrations in the order they will be applied. With a verbosity level of 2 or above all…	
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	showmigrations	-v
v	0	
v	1	
v	2	
v	3	
=	showmigrations	--pythonpath
t	folders
@	sqlflush
o	--database	Nominates a database to print the SQL for. Defaults to the "default" database	v
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	sqlflush	-v
v	0	
v	1	
v	2	
v	3	
=	sqlflush	--pythonpath
t	folders
@	sqlmigrate
o	--database	Nominates a database to create SQL for. Defaults to the "default" database	v
o	--backwards	Creates SQL to unapply the migration, rather than to apply it	
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	2	0
=	sqlmigrate	-v
v	0	
v	1	
v	2	
v	3	
=	sqlmigrate	--pythonpath
t	folders
@	sqlsequencereset
o	--database	Nominates a database to print the SQL for. Defaults to the "default" database	v
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	sqlsequencereset	-v
v	0	
v	1	
v	2	
v	3	
=	sqlsequencereset	--pythonpath
t	folders
@	squashmigrations
o	--no-optimize	Do not try to optimize the squashed operations	
o	--noinput|--no-input	Tells Django to NOT prompt the user for input of any kind	
o	--squashed-name	Sets the name of the new squashed migration	v
o	--no-header	Do not add a header comment to the new squashed migration	
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	3	0
=	squashmigrations	-v
v	0	
v	1	
v	2	
v	3	
=	squashmigrations	--pythonpath
t	folders
@	startapp
o	--template	The path or URL to load the template from	v
o	--extension|-e	The file extension(s) to render (default: "py"). Separate multiple extensions with commas, or use…	v
o	--name|-n	The file name(s) to render. Separate multiple file names with commas, or use -n multiple times	v
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	2	0
=	startapp	-v
v	0	
v	1	
v	2	
v	3	
=	startapp	--pythonpath
t	folders
@	startproject
o	--template	The path or URL to load the template from	v
o	--extension|-e	The file extension(s) to render (default: "py"). Separate multiple extensions with commas, or use…	v
o	--name|-n	The file name(s) to render. Separate multiple file names with commas, or use -n multiple times	v
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	2	0
=	startproject	-v
v	0	
v	1	
v	2	
v	3	
=	startproject	--pythonpath
t	folders
@	test
o	--noinput|--no-input	Tells Django to NOT prompt the user for input of any kind	
o	--failfast	Tells Django to stop running the test suite after first failed test	
o	--testrunner	Tells Django to use specified test runner class instead of the one specified by the TEST_RUNNER…	v
o	-t|--top-level-directory	Top level of project for unittest discovery	v
o	-p|--pattern	The test matching pattern. Defaults to test*.py	v
o	--keepdb	Preserves the test DB between runs	
o	-r|--reverse	Reverses test cases order	
o	--debug-mode	Sets settings.DEBUG to True	
o	-d|--debug-sql	Prints logged SQL queries on failure	
o	--parallel	Run tests using up to N parallel processes	v
o	--tag	Run only tests with the specified tag. Can be used multiple times	v
o	--exclude-tag	Do not run tests with the specified tag. Can be used multiple times	v
o	--pdb	Runs a debugger (pdb, or ipdb if installed) on error or failure	
o	-b|--buffer	Discard output from passing tests	
o	-k	Only run test methods and classes that match the pattern or substring. Can be used multiple times…	v
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	0
=	test	-t
t	folders
=	test	-v
v	0	
v	1	
v	2	
v	3	
=	test	--pythonpath
t	folders
@	testserver
o	--noinput|--no-input	Tells Django to NOT prompt the user for input of any kind	
o	--addrport	Port number or ipaddr:port to run the server on	v
o	--ipv6|-6	Tells Django to use an IPv6 address	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	0
=	testserver	-v
v	0	
v	1	
v	2	
v	3	
=	testserver	--pythonpath
t	folders
@	test_mail
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	test_mail	-v
v	0	
v	1	
v	2	
v	3	
=	test_mail	--pythonpath
t	folders
@	clearsessions
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	clearsessions	-v
v	0	
v	1	
v	2	
v	3	
=	clearsessions	--pythonpath
t	folders
@	collectstatic
o	--noinput|--no-input	Do NOT prompt the user for input of any kind	
o	--no-post-process	Do NOT post process collected files	
o	-i|--ignore	Ignore files or directories matching this glob-style pattern. Use multiple times to ignore more	v
o	-n|--dry-run	Do everything except modify the filesystem	
o	-c|--clear	Clear the existing files using the storage before trying to copy or link the original file	
o	-l|--link	Create a symbolic link to each file instead of copying	
o	--no-default-ignore	Don't ignore the common private glob-style patterns (defaults to 'CVS', '.*' and '*~')	
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
=	collectstatic	-v
v	0	
v	1	
v	2	
v	3	
=	collectstatic	--pythonpath
t	folders
@	findstatic
o	--first	Only return the first match for each static file	
o	--skip-checks	Skip system checks	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	1
=	findstatic	-v
v	0	
v	1	
v	2	
v	3	
=	findstatic	--pythonpath
t	folders
@	runserver
o	--ipv6|-6	Tells Django to use an IPv6 address	
o	--nothreading	Tells Django to NOT use threading	
o	--noreload	Tells Django to NOT use the auto-reloader	
o	--nostatic	Tells Django to NOT automatically serve static files at STATIC_URL	
o	--insecure	Allows serving static files even if DEBUG is False	
o	-h|--help	Show this help message and exit	
o	--version	Show program's version number and exit	
o	-v|--verbosity	Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output	v
o	--settings	The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the…	v
o	--pythonpath	A directory to add to the Python path, e.g. "/home/djangoprojects/myproject"	v
o	--traceback	Raise on CommandError exceptions	
o	--no-color	Don't colorize the command output	
o	--force-color	Force colorization of the command output	
a	1	0
=	runserver	-v
v	0	
v	1	
v	2	
v	3	
=	runserver	--pythonpath
t	folders
