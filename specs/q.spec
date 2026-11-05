@	
s	debug	Debug the app
s	settings|setting	Customize appearance & behavior
s	install	Install cli components
s	update|upgrade	Update the Q application
s	diagnostic|diagnostics	Run diagnostic tests
s	init	Generate the dotfiles for the given shell
s	theme	Get or set theme
s	issue	Create a new Github issue
s	login	Login
s	logout	Logout
s	whoami	Prints details about the current user
s	user	Manage your account
s	doctor	Fix and diagnose common issues
s	launch	Launch the desktop app
s	quit	Quit the desktop app
s	restart	Restart the desktop app
s	integrations|integration	Manage system integrations
s	translate|ai	Natural Language to Shell translation
s	dashboard	Open the dashboard
s	chat	AI assistant in your terminal
s	help	Print this message or the help of the given subcommand(s)
o	-v|--verbose	Increase logging verbosity	
o	--help-all	Print help for all subcommands	
o	-h|--help	Print help	
o	-V|--version	Print version	
@	debug
s	app	Debug the app
s	build	Switch to another branch of a Fig.js app
s	autocomplete-window	Toggle/set autocomplete window debug mode
s	logs	Show debug logs
s	input-method	Input method debugger
s	prompt-accessibility	Prompt accessibility
s	sample	Sample desktop process
s	verify-codesign	Debug application codesigning
s	accessibility	Accessibility
s	key-tester	Key Tester
s	diagnostics	Watches diagnostics
s	query-index	Queries remote repository for updates given the specified metadata
s	devtools	Open up the devtools of a specific webview
s	get-index	Displays remote index
s	list-intellij-variants	Lists installed IntelliJ variants
s	shell	Disables sourcing of user shell config and instead uses a minimal shell config
s	help	Print this message or the help of the given subcommand(s)
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug app
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug build
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	2	0
#	debug build	1
v	dashboard	
v	autocomplete	
#	debug build	2
v	production	
v	beta	
v	develop	
@	debug autocomplete-window
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
#	debug autocomplete-window	1
v	on	
v	off	
@	debug logs
o	--level		V
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	1
@	debug input-method
s	install	
s	uninstall	
s	list	
s	status	
s	source	
s	help	Print this message or the help of the given subcommand(s)
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug input-method install
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
#	debug input-method install	1
t	filepaths
@	debug input-method uninstall
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
#	debug input-method uninstall	1
t	filepaths
@	debug input-method list
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug input-method status
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
#	debug input-method status	1
t	filepaths
@	debug input-method source
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	2	0
#	debug input-method source	2
v	enable	
v	disable	
v	select	
v	deselect	
@	debug input-method help
s	install	
s	uninstall	
s	list	
s	status	
s	source	
s	help	Print this message or the help of the given subcommand(s)
@	debug input-method help install
@	debug input-method help uninstall
@	debug input-method help list
@	debug input-method help status
@	debug input-method help source
@	debug input-method help help
@	debug prompt-accessibility
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug sample
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug verify-codesign
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug accessibility
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
#	debug accessibility	1
v	refresh	
v	reset	
v	prompt	
v	open	
v	status	
@	debug key-tester
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug diagnostics
o	--rate		V
o	--watch		
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug query-index
o	-c|--channel		v
o	-o|--os		v
o	-V|--variant		v
o	-e|--version		v
o	-a|--architecture		v
o	-t|--override-threshold		V
o	-f|--file-type		v
o	-r|--enable-rollout		
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug devtools
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
#	debug devtools	1
v	dashboard	
v	autocomplete	
@	debug get-index
o	-d|--debug	Display using debug formatting	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
@	debug list-intellij-variants
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug shell
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	debug help
s	app	Debug the app
s	build	Switch to another branch of a Fig.js app
s	autocomplete-window	Toggle/set autocomplete window debug mode
s	logs	Show debug logs
s	input-method	Input method debugger
s	prompt-accessibility	Prompt accessibility
s	sample	Sample desktop process
s	verify-codesign	Debug application codesigning
s	accessibility	Accessibility
s	key-tester	Key Tester
s	diagnostics	Watches diagnostics
s	query-index	Queries remote repository for updates given the specified metadata
s	devtools	Open up the devtools of a specific webview
s	get-index	Displays remote index
s	list-intellij-variants	Lists installed IntelliJ variants
s	shell	Disables sourcing of user shell config and instead uses a minimal shell config
s	help	Print this message or the help of the given subcommand(s)
@	debug help app
@	debug help build
@	debug help autocomplete-window
@	debug help logs
@	debug help input-method
s	install	
s	uninstall	
s	list	
s	status	
s	source	
@	debug help input-method install
@	debug help input-method uninstall
@	debug help input-method list
@	debug help input-method status
@	debug help input-method source
@	debug help prompt-accessibility
@	debug help sample
@	debug help verify-codesign
@	debug help accessibility
@	debug help key-tester
@	debug help diagnostics
@	debug help query-index
@	debug help devtools
@	debug help get-index
@	debug help list-intellij-variants
@	debug help shell
@	debug help help
@	settings
s	open	Open the settings file
s	all	List all the settings
s	help	Print this message or the help of the given subcommand(s)
o	-f|--format	Format of the output	V
o	-d|--delete	Delete a value	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
a	2	0
=	settings	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	settings open
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	settings all
o	-f|--format	Format of the output	V
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
=	settings all	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	settings help
s	open	Open the settings file
s	all	List all the settings
s	help	Print this message or the help of the given subcommand(s)
@	settings help open
@	settings help all
@	settings help help
@	install
o	--dotfiles	Install only the shell integrations	
o	--input-method	Prompt input method installation	
o	--no-confirm	Don't confirm automatic installation	
o	--force	Force installation of fig	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	update
o	-y|--non-interactive	Don't prompt for confirmation	
o	--relaunch-dashboard	Relaunch into dashboard after update (false will launch in background)	
o	--rollout	Uses rollout	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	diagnostic
o	-f|--format	The format of the output	V
o	--force	Force limited diagnostic output	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
=	diagnostic	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	init
o	--rcfile		V
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
a	2	0
#	init	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	nu	Nu shell
#	init	2
v	pre	
v	post	
@	theme
o	--list		
o	--folder		
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
#	theme	1
d
@	issue
o	-f|--force	Force issue creation	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	1
@	login
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	logout
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	whoami
o	-f|--format	Output format to use	V
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
=	whoami	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	user
s	login	Login
s	logout	Logout
s	whoami	Prints details about the current user
s	help	Print this message or the help of the given subcommand(s)
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	user login
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	user logout
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	user whoami
o	-f|--format	Output format to use	V
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
=	user whoami	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	user help
s	login	Login
s	logout	Logout
s	whoami	Prints details about the current user
s	help	Print this message or the help of the given subcommand(s)
@	user help login
@	user help logout
@	user help whoami
@	user help help
@	doctor
o	-a|--all	Run all doctor tests, with no fixes	
o	-s|--strict	Error on warnings	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	launch
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	quit
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	restart
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
#	restart	1
v	app	Desktop Process
@	integrations
s	install	
s	uninstall	
s	reinstall	
s	status	
s	help	Print this message or the help of the given subcommand(s)
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations install
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin|jetbrains-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
o	-s|--silent	Suppress status messages	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations install dotfiles
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
a	1	0
#	integrations install dotfiles	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	nu	Nu shell
@	integrations install ssh
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations install input-method
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations install vscode
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations install intellij-plugin
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations install all
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations install help
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
@	integrations install help dotfiles
@	integrations install help ssh
@	integrations install help input-method
@	integrations install help vscode
@	integrations install help intellij-plugin
@	integrations install help all
@	integrations install help help
@	integrations uninstall
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin|jetbrains-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
o	-s|--silent	Suppress status messages	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations uninstall dotfiles
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
a	1	0
#	integrations uninstall dotfiles	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	nu	Nu shell
@	integrations uninstall ssh
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations uninstall input-method
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations uninstall vscode
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations uninstall intellij-plugin
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations uninstall all
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations uninstall help
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
@	integrations uninstall help dotfiles
@	integrations uninstall help ssh
@	integrations uninstall help input-method
@	integrations uninstall help vscode
@	integrations uninstall help intellij-plugin
@	integrations uninstall help all
@	integrations uninstall help help
@	integrations reinstall
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin|jetbrains-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
o	-s|--silent	Suppress status messages	
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations reinstall dotfiles
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
a	1	0
#	integrations reinstall dotfiles	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	nu	Nu shell
@	integrations reinstall ssh
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations reinstall input-method
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations reinstall vscode
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations reinstall intellij-plugin
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations reinstall all
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations reinstall help
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
@	integrations reinstall help dotfiles
@	integrations reinstall help ssh
@	integrations reinstall help input-method
@	integrations reinstall help vscode
@	integrations reinstall help intellij-plugin
@	integrations reinstall help all
@	integrations reinstall help help
@	integrations status
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin|jetbrains-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
o	-f|--format		V
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
=	integrations status	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	integrations status dotfiles
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help (see more with '--help')	
a	1	0
#	integrations status dotfiles	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	nu	Nu shell
@	integrations status ssh
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations status input-method
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations status vscode
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations status intellij-plugin
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations status all
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	integrations status help
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
@	integrations status help dotfiles
@	integrations status help ssh
@	integrations status help input-method
@	integrations status help vscode
@	integrations status help intellij-plugin
@	integrations status help all
@	integrations status help help
@	integrations help
s	install	
s	uninstall	
s	reinstall	
s	status	
s	help	Print this message or the help of the given subcommand(s)
@	integrations help install
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
@	integrations help install dotfiles
@	integrations help install ssh
@	integrations help install input-method
@	integrations help install vscode
@	integrations help install intellij-plugin
@	integrations help install all
@	integrations help uninstall
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
@	integrations help uninstall dotfiles
@	integrations help uninstall ssh
@	integrations help uninstall input-method
@	integrations help uninstall vscode
@	integrations help uninstall intellij-plugin
@	integrations help uninstall all
@	integrations help reinstall
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
@	integrations help reinstall dotfiles
@	integrations help reinstall ssh
@	integrations help reinstall input-method
@	integrations help reinstall vscode
@	integrations help reinstall intellij-plugin
@	integrations help reinstall all
@	integrations help status
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
@	integrations help status dotfiles
@	integrations help status ssh
@	integrations help status input-method
@	integrations help status vscode
@	integrations help status intellij-plugin
@	integrations help status all
@	integrations help help
@	translate
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	1
@	dashboard
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
@	chat
o	-v|--verbose	Increase logging verbosity	
o	-h|--help	Print help	
a	1	0
@	help
s	debug	Debug the app
s	settings	Customize appearance & behavior
s	install	Install cli components
s	update	Update the Q application
s	diagnostic	Run diagnostic tests
s	init	Generate the dotfiles for the given shell
s	theme	Get or set theme
s	issue	Create a new Github issue
s	login	Login
s	logout	Logout
s	whoami	Prints details about the current user
s	user	Manage your account
s	doctor	Fix and diagnose common issues
s	launch	Launch the desktop app
s	quit	Quit the desktop app
s	restart	Restart the desktop app
s	integrations	Manage system integrations
s	translate	Natural Language to Shell translation
s	dashboard	Open the dashboard
s	chat	AI assistant in your terminal
s	help	Print this message or the help of the given subcommand(s)
@	help debug
s	app	Debug the app
s	build	Switch to another branch of a Fig.js app
s	autocomplete-window	Toggle/set autocomplete window debug mode
s	logs	Show debug logs
s	input-method	Input method debugger
s	prompt-accessibility	Prompt accessibility
s	sample	Sample desktop process
s	verify-codesign	Debug application codesigning
s	accessibility	Accessibility
s	key-tester	Key Tester
s	diagnostics	Watches diagnostics
s	query-index	Queries remote repository for updates given the specified metadata
s	devtools	Open up the devtools of a specific webview
s	get-index	Displays remote index
s	list-intellij-variants	Lists installed IntelliJ variants
s	shell	Disables sourcing of user shell config and instead uses a minimal shell config
@	help debug app
@	help debug build
@	help debug autocomplete-window
@	help debug logs
@	help debug input-method
s	install	
s	uninstall	
s	list	
s	status	
s	source	
@	help debug input-method install
@	help debug input-method uninstall
@	help debug input-method list
@	help debug input-method status
@	help debug input-method source
@	help debug prompt-accessibility
@	help debug sample
@	help debug verify-codesign
@	help debug accessibility
@	help debug key-tester
@	help debug diagnostics
@	help debug query-index
@	help debug devtools
@	help debug get-index
@	help debug list-intellij-variants
@	help debug shell
@	help settings
s	open	Open the settings file
s	all	List all the settings
@	help settings open
@	help settings all
@	help install
@	help update
@	help diagnostic
@	help init
@	help theme
@	help issue
@	help login
@	help logout
@	help whoami
@	help user
s	login	Login
s	logout	Logout
s	whoami	Prints details about the current user
@	help user login
@	help user logout
@	help user whoami
@	help doctor
@	help launch
@	help quit
@	help restart
@	help integrations
s	install	
s	uninstall	
s	reinstall	
s	status	
@	help integrations install
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
@	help integrations install dotfiles
@	help integrations install ssh
@	help integrations install input-method
@	help integrations install vscode
@	help integrations install intellij-plugin
@	help integrations install all
@	help integrations uninstall
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
@	help integrations uninstall dotfiles
@	help integrations uninstall ssh
@	help integrations uninstall input-method
@	help integrations uninstall vscode
@	help integrations uninstall intellij-plugin
@	help integrations uninstall all
@	help integrations reinstall
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
@	help integrations reinstall dotfiles
@	help integrations reinstall ssh
@	help integrations reinstall input-method
@	help integrations reinstall vscode
@	help integrations reinstall intellij-plugin
@	help integrations reinstall all
@	help integrations status
s	dotfiles	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
@	help integrations status dotfiles
@	help integrations status ssh
@	help integrations status input-method
@	help integrations status vscode
@	help integrations status intellij-plugin
@	help integrations status all
@	help translate
@	help dashboard
@	help chat
@	help help
