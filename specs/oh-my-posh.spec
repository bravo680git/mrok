@	
s	init	Initialize oh-my-posh for your shell
s	get	Get oh-my-posh values
s	debug	Debug oh-my-posh, example usage: 'oh-my-posh debug'
s	config	Interact with the oh-my-posh configuration
s	print	Print a prompt
s	version	Display the oh-my-posh version, example usage: 'oh-my-posh version'
o	--help|-h	Show help for oh-my-posh	p
@	init
o	--config|-c	The config file to use	vp
o	--print|-p	Print the init script	
a	1	0
=	init	--config
t	filepaths,history
#	init	1
v	zsh	
v	fish	
v	pwsh	
v	powershell	
v	cmd	
v	bash	
v	shell	
@	get
a	1	0
#	get	1
v	millis	Get the current timestamp in milliseconds, example usage: 'oh-my-posh get millis'
v	shell	Get the current shell, example usage: 'oh-my-posh get shell'
@	debug
o	--config|-c	The config file to use	vp
=	debug	--config
t	filepaths,history
@	config
s	edit	Edit the config file, example usage: 'oh-my-posh config edit'
s	migrate	Migrate the config file, example usage: 'oh-my-posh config migrate --config ~/.config.omp.json'
s	export	Export the config file, example usage: 'oh-my-posh config export --config ~/.config.omp.toml'
o	--config|-c	The config file to use	vp
=	config	--config
t	filepaths,history
@	config edit
@	config migrate
o	--write|-w	Write the migrated config to the configuration file, example usage: 'oh-my-posh config migrate…	
o	--format|-f	The file format to use	v
=	config migrate	--format
v	json	
v	yaml	
v	toml	
@	config export
o	--output|-o	The file to output the migrated config to, example usage: 'oh-my-posh config export --output…	v
o	--format|-f	The file format to use	v
=	config export	--output
t	filepaths
=	config export	--format
v	json	
v	yaml	
v	toml	
@	print
o	--config|-c	The config file to use	vp
o	--terminal-width|-w	The terminal width, example usage: 'oh-my-posh print primary --terminal-width 200'	v
o	--command	The current command for tooltips, example usage: 'oh-my-posh print tooltip --command az'	v
o	--error|-e	The last exit code, example usage: 'oh-my-posh print primary --error 127'	v
o	--eval	Use eval to render the prompt, example usage: 'oh-my-posh print primary --eval'	
o	--execution-time	Use last command execution time in millis, example usage: 'oh-my-posh print primary…	v
o	--plain|-p	Print a prompt without ASNI codes, example usage: 'oh-my-posh print primary --plain'	
o	--pswd	The current working directory according to PowerShell, example usage: 'oh-my-posh print primary…	v
o	--pwd	The current working directory, example usage: 'oh-my-posh print primary --pwd /home/user/Documents'	v
o	--shell	The current shell, example usage: 'oh-my-posh print primary --shell fish'	v
o	--stack-count	The directory stack count, example usage: 'oh-my-posh print primary --stack-count 1'	v
a	1	0
=	print	--config
t	filepaths,history
=	print	--pswd
t	filepaths
=	print	--pwd
t	filepaths
=	print	--shell
v	zsh	
v	fish	
v	pwsh	
v	powershell	
v	cmd	
v	bash	
v	shell	
#	print	1
v	primary	
v	secondary	
v	right	
v	transient	
v	tooltip	
v	valid	
v	error	
@	version
