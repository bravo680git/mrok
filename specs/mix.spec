@	
s	new	Creates a new Elixir project at the given path
s	run	Starts the current application and runs code
s	help	Prints documentation for a given task (Lists all the tasks if no task is specified)
o	-h|--help	Shows usage information	
o	-v|--version	Shows versioning information	
a	1	0
#		1
d
@	new
o	-h|--help	Output usage information	
o	--app	Name the OTP application for the project	v
o	--modules	Name the modules in the generated code skeleton	v
o	--sup	Generate an OTP application skeleton including a supervision tree. Normally an app is generated…	
o	--umbrella	Generate an umbrella project	
a	1	0
@	run
o	--config	Loads the given configuration files	v
o	-e|--eval	Evaluates the given code	v
o	-r|--require	Executes the given pattern/file	v
o	-p|--parallel	Executes the given pattern/file	v
o	--preload-modules	Preloads all modules defined in applications	
o	--no-compile	Does not compile even if files require compilation	
o	--no-deps-check	Does not check dependencies	
o	--no-archives-check	Does not check archives	
o	--no-halt	Does not halt the system after running the command	
o	--no-mix-exs	Allows the command to run even if there is no mix.exs	
o	--no-start	Does not start applications after compilation	
o	--no-elixir-version-check	Does not check the Elixir version from mix.exs	
a	1	0
=	run	--config
t	filepaths
=	run	-r
d
=	run	-p
d
#	run	1
d
@	help
o	--search	Prints all tasks and aliases that contain 'pattern' in the name	v
o	--names	Prints all task names and aliases	
a	1	0
#	help	1
d
