@	
s	app	Interact with the desktop app
s	debug	Debug CodeWhisperer
s	settings|setting	Customize appearance & behavior
s	tips	Enable/disable CodeWhisperer tips
s	install	Install CodeWhisperer cli components
s	update	Check for updates
s	diagnostic|diagnostics	Run diagnostic tests
s	init	Generate the dotfiles for the given shell
s	theme	Get or set theme
s	issue	Create a new Github issue
s	login	Login to CodeWhisperer
s	logout	Logout of CodeWhisperer
s	whoami	Prints details about the current user
s	user	Manage your CodeWhisperer user
s	doctor	Check CodeWhisperer is properly configured
s	launch	Launch the CodeWhisperer desktop app
s	quit	Quit the CodeWhisperer desktop app
s	restart	Restart the CodeWhisperer desktop app
s	integrations|integration	Manage system integrations
s	ai|q	English -> Bash translation
s	version	Version
s	help-all	Print help for all subcommands
s	dashboard	Open the fig dashboard
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help	
o	-V|--version	Print version	
@	app
s	install	Install the CodeWhisperer app
s	onboarding	Run the CodeWhisperer tutorial again
s	running	Check if CodeWhisperer is running
s	launch	Launch the CodeWhisperer desktop app
s	restart	Restart the CodeWhisperer desktop app
s	quit	Quit the CodeWhisperer desktop app
s	set-path	Set the internal pseudo-terminal path
s	uninstall	Uninstall the CodeWhisperer app
s	prompts	Prompts shown on terminal startup
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help	
@	app install
o	-h|--help	Print help	
@	app onboarding
o	-h|--help	Print help	
@	app running
o	-h|--help	Print help	
@	app launch
o	-h|--help	Print help	
@	app restart
o	-h|--help	Print help	
@	app quit
o	-h|--help	Print help	
@	app set-path
o	-h|--help	Print help	
@	app uninstall
o	--app-bundle	Remove executable and user data	
o	--input-method	Remove input method	
o	--daemon	Remove CodeWhisperer daemon	
o	--dotfiles	Remove dotfile shell integration	
o	--ssh	Remove SSH integration	
o	--no-open	Do not open the uninstallation page	
o	--only-open	Only open the uninstallation page	
o	-h|--help	Print help	
@	app prompts
o	-h|--help	Print help	
@	app help
s	install	Install the CodeWhisperer app
s	onboarding	Run the CodeWhisperer tutorial again
s	running	Check if CodeWhisperer is running
s	launch	Launch the CodeWhisperer desktop app
s	restart	Restart the CodeWhisperer desktop app
s	quit	Quit the CodeWhisperer desktop app
s	set-path	Set the internal pseudo-terminal path
s	uninstall	Uninstall the CodeWhisperer app
s	prompts	Prompts shown on terminal startup
s	help	Print this message or the help of the given subcommand(s)
@	app help install
@	app help onboarding
@	app help running
@	app help launch
@	app help restart
@	app help quit
@	app help set-path
@	app help uninstall
@	app help prompts
@	app help help
@	debug
s	app	Debug CodeWhisperer app
s	build	Switch to another branch of a Fig.js app
s	autocomplete-window	Toggle/set autocomplete window debug mode
s	logs	Show CodeWhisperer debug logs
s	input-method	CodeWhisperer input method editor
s	prompt-accessibility	Prompt accessibility
s	sample	Sample CodeWhisperer process
s	verify-codesign	Debug CodeWhisperer codesign verification
s	accessibility	Accessibility
s	key-tester	Key Tester
s	diagnostics	Watches diagnostics
s	query-index	Queries remote repository for updates given the specified metadata
s	devtools	Open up the devtools of a specific webview
s	get-index	Displays remote index
s	list-intellij-variants	Lists installed IntelliJ variants
s	shell	Disables sourcing of user shell config and instead uses a minimal CodeWhisperer default
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help	
@	debug app
o	-h|--help	Print help	
@	debug build
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
o	-h|--help	Print help	
a	1	0
#	debug autocomplete-window	1
v	on	
v	off	
@	debug logs
o	--level		V
o	-h|--help	Print help	
a	1	1
@	debug input-method
s	install	
s	uninstall	
s	list	
s	status	
s	source	
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help	
@	debug input-method install
o	-h|--help	Print help	
a	1	0
#	debug input-method install	1
t	filepaths
@	debug input-method uninstall
o	-h|--help	Print help	
a	1	0
#	debug input-method uninstall	1
t	filepaths
@	debug input-method list
o	-h|--help	Print help	
@	debug input-method status
o	-h|--help	Print help	
a	1	0
#	debug input-method status	1
t	filepaths
@	debug input-method source
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
o	-h|--help	Print help	
@	debug sample
o	-h|--help	Print help	
@	debug verify-codesign
o	-h|--help	Print help	
@	debug accessibility
o	-h|--help	Print help	
a	1	0
#	debug accessibility	1
v	refresh	
v	reset	
v	prompt	
v	open	
v	status	
@	debug key-tester
o	-h|--help	Print help	
@	debug diagnostics
o	--rate		V
o	--watch		
o	-h|--help	Print help	
@	debug query-index
o	-c|--channel		v
o	-k|--kind		v
o	-v|--variant		v
o	-e|--version		v
o	-a|--architecture		v
o	-t|--override-threshold		V
o	-r|--enable-rollout		
o	-h|--help	Print help	
@	debug devtools
o	-h|--help	Print help	
a	1	0
#	debug devtools	1
v	dashboard	
v	autocomplete	
@	debug get-index
o	-d|--debug	Display using debug formatting	
o	-h|--help	Print help	
a	1	0
@	debug list-intellij-variants
o	-h|--help	Print help	
@	debug shell
o	-h|--help	Print help	
@	debug help
s	app	Debug CodeWhisperer app
s	build	Switch to another branch of a Fig.js app
s	autocomplete-window	Toggle/set autocomplete window debug mode
s	logs	Show CodeWhisperer debug logs
s	input-method	CodeWhisperer input method editor
s	prompt-accessibility	Prompt accessibility
s	sample	Sample CodeWhisperer process
s	verify-codesign	Debug CodeWhisperer codesign verification
s	accessibility	Accessibility
s	key-tester	Key Tester
s	diagnostics	Watches diagnostics
s	query-index	Queries remote repository for updates given the specified metadata
s	devtools	Open up the devtools of a specific webview
s	get-index	Displays remote index
s	list-intellij-variants	Lists installed IntelliJ variants
s	shell	Disables sourcing of user shell config and instead uses a minimal CodeWhisperer default
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
o	-h|--help	Print help (see more with '--help')	
a	2	0
=	settings	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	settings open
o	-h|--help	Print help	
@	settings all
o	-f|--format	Format of the output	V
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
@	tips
s	enable	Enable CodeWhisperer tips
s	disable	Disable CodeWhisperer tips
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help	
@	tips enable
o	-h|--help	Print help	
@	tips disable
o	-h|--help	Print help	
@	tips help
s	enable	Enable CodeWhisperer tips
s	disable	Disable CodeWhisperer tips
s	help	Print this message or the help of the given subcommand(s)
@	tips help enable
@	tips help disable
@	tips help help
@	install
o	--daemon	Install only the daemon	
o	--dotfiles	Install only the shell integrations	
o	--input-method	Prompt input method installation	
o	--no-confirm	Don't confirm automatic installation	
o	--force	Force installation of CodeWhisperer	
o	--ssh	Install only the ssh integration	
o	-h|--help	Print help	
@	update
o	--no-confirm	(deprecated) Use --non-interactive instead	
o	-y|--non-interactive	Don't prompt for confirmation	
o	--relaunch-dashboard	Relaunch into dashboard after update (false will launch in background)	
o	--rollout	Uses rollout	
o	-h|--help	Print help	
@	diagnostic
o	-f|--format	The format of the output	V
o	--force	Force limited diagnostic output	
o	-h|--help	Print help (see more with '--help')	
=	diagnostic	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	init
o	--rcfile		V
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
o	-h|--help	Print help	
a	1	0
#	theme	1
g	cw theme --list	\n
@	issue
o	-f|--force	Force issue creation	
o	-h|--help	Print help	
a	1	1
@	login
o	-h|--help	Print help	
@	logout
o	-h|--help	Print help	
@	whoami
o	-f|--format	Output format to use	V
o	-h|--help	Print help (see more with '--help')	
=	whoami	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	user
s	login	Login to CodeWhisperer
s	logout	Logout of CodeWhisperer
s	whoami	Prints details about the current user
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help	
@	user login
o	-h|--help	Print help	
@	user logout
o	-h|--help	Print help	
@	user whoami
o	-f|--format	Output format to use	V
o	-h|--help	Print help (see more with '--help')	
=	user whoami	-f
v	plain	Outputs the results as markdown
v	json	Outputs the results as JSON
v	json-pretty	Outputs the results as pretty print JSON
@	user help
s	login	Login to CodeWhisperer
s	logout	Logout of CodeWhisperer
s	whoami	Prints details about the current user
s	help	Print this message or the help of the given subcommand(s)
@	user help login
@	user help logout
@	user help whoami
@	user help help
@	doctor
o	--verbose	Run all doctor tests, with no fixes	
o	--strict	Error on warnings	
o	-h|--help	Print help	
@	launch
o	-h|--help	Print help	
@	quit
o	-h|--help	Print help	
@	restart
o	-h|--help	Print help	
a	1	0
#	restart	1
v	daemon	Daemon process
v	app	CodeWhisperer process
@	integrations
s	install	
s	uninstall	
s	reinstall	
s	status	
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help	
@	integrations install
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
o	-s|--silent	Suppress status messages	
o	-h|--help	Print help	
@	integrations install dotfiles
o	-h|--help	Print help (see more with '--help')	
a	1	0
#	integrations install dotfiles	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	nu	Nu shell
@	integrations install daemon
o	-h|--help	Print help	
@	integrations install ssh
o	-h|--help	Print help	
@	integrations install input-method
o	-h|--help	Print help	
@	integrations install vscode
o	-h|--help	Print help	
@	integrations install intellij-plugin
o	-h|--help	Print help	
@	integrations install all
o	-h|--help	Print help	
@	integrations install help
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
s	help	Print this message or the help of the given subcommand(s)
@	integrations install help dotfiles
@	integrations install help daemon
@	integrations install help ssh
@	integrations install help input-method
@	integrations install help vscode
@	integrations install help intellij
@	integrations install help all
@	integrations install help help
@	integrations uninstall
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
o	-s|--silent	Suppress status messages	
o	-h|--help	Print help	
@	integrations uninstall dotfiles
o	-h|--help	Print help (see more with '--help')	
a	1	0
#	integrations uninstall dotfiles	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	nu	Nu shell
@	integrations uninstall daemon
o	-h|--help	Print help	
@	integrations uninstall ssh
o	-h|--help	Print help	
@	integrations uninstall input-method
o	-h|--help	Print help	
@	integrations uninstall vscode
o	-h|--help	Print help	
@	integrations uninstall intellij-plugin
o	-h|--help	Print help	
@	integrations uninstall all
o	-h|--help	Print help	
@	integrations uninstall help
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
s	help	Print this message or the help of the given subcommand(s)
@	integrations uninstall help dotfiles
@	integrations uninstall help daemon
@	integrations uninstall help ssh
@	integrations uninstall help input-method
@	integrations uninstall help vscode
@	integrations uninstall help intellij
@	integrations uninstall help all
@	integrations uninstall help help
@	integrations reinstall
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
o	-s|--silent	Suppress status messages	
o	-h|--help	Print help	
@	integrations reinstall dotfiles
o	-h|--help	Print help (see more with '--help')	
a	1	0
#	integrations reinstall dotfiles	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	nu	Nu shell
@	integrations reinstall daemon
o	-h|--help	Print help	
@	integrations reinstall ssh
o	-h|--help	Print help	
@	integrations reinstall input-method
o	-h|--help	Print help	
@	integrations reinstall vscode
o	-h|--help	Print help	
@	integrations reinstall intellij-plugin
o	-h|--help	Print help	
@	integrations reinstall all
o	-h|--help	Print help	
@	integrations reinstall help
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
s	help	Print this message or the help of the given subcommand(s)
@	integrations reinstall help dotfiles
@	integrations reinstall help daemon
@	integrations reinstall help ssh
@	integrations reinstall help input-method
@	integrations reinstall help vscode
@	integrations reinstall help intellij
@	integrations reinstall help all
@	integrations reinstall help help
@	integrations status
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij-plugin	
s	all	
s	help	Print this message or the help of the given subcommand(s)
o	-h|--help	Print help	
@	integrations status dotfiles
o	-h|--help	Print help (see more with '--help')	
a	1	0
#	integrations status dotfiles	1
v	bash	Bash shell
v	zsh	Zsh shell
v	fish	Fish shell
v	nu	Nu shell
@	integrations status daemon
o	-h|--help	Print help	
@	integrations status ssh
o	-h|--help	Print help	
@	integrations status input-method
o	-h|--help	Print help	
@	integrations status vscode
o	-h|--help	Print help	
@	integrations status intellij-plugin
o	-h|--help	Print help	
@	integrations status all
o	-h|--help	Print help	
@	integrations status help
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
s	help	Print this message or the help of the given subcommand(s)
@	integrations status help dotfiles
@	integrations status help daemon
@	integrations status help ssh
@	integrations status help input-method
@	integrations status help vscode
@	integrations status help intellij
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
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
@	integrations help install dotfiles
@	integrations help install daemon
@	integrations help install ssh
@	integrations help install input-method
@	integrations help install vscode
@	integrations help install intellij
@	integrations help install all
@	integrations help uninstall
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
@	integrations help uninstall dotfiles
@	integrations help uninstall daemon
@	integrations help uninstall ssh
@	integrations help uninstall input-method
@	integrations help uninstall vscode
@	integrations help uninstall intellij
@	integrations help uninstall all
@	integrations help reinstall
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
@	integrations help reinstall dotfiles
@	integrations help reinstall daemon
@	integrations help reinstall ssh
@	integrations help reinstall input-method
@	integrations help reinstall vscode
@	integrations help reinstall intellij
@	integrations help reinstall all
@	integrations help status
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
@	integrations help status dotfiles
@	integrations help status daemon
@	integrations help status ssh
@	integrations help status input-method
@	integrations help status vscode
@	integrations help status intellij
@	integrations help status all
@	integrations help help
@	ai
o	-h|--help	Print help	
a	1	1
@	version
o	-h|--help	Print help	
@	help-all
o	-h|--help	Print help	
@	dashboard
o	-h|--help	Print help	
@	help
s	app	Interact with the desktop app
s	debug	Debug CodeWhisperer
s	settings	Customize appearance & behavior
s	tips	Enable/disable fig tips
s	install	Install fig cli components
s	update	Update dotfiles
s	diagnostic	Run diagnostic tests
s	init	Generate the dotfiles for the given shell
s	theme	Get or set theme
s	issue	Create a new Github issue
s	login	Login to CodeWhisperer
s	logout	Logout of CodeWhisperer
s	whoami	Prints details about the current user
s	user	Manage your fig user
s	doctor	Check CodeWhisperer is properly configured
s	launch	Launch the CodeWhisperer desktop app
s	quit	Quit the CodeWhisperer desktop app
s	restart	Restart the CodeWhisperer desktop app
s	integrations	Manage system integrations
s	ai	English -> Bash translation
s	version	Version
s	help-all	Print help for all subcommands
s	dashboard	Open the fig dashboard
s	help	Print this message or the help of the given subcommand(s)
@	help app
s	install	Install the Fig app
s	onboarding	Run the CodeWhisperer tutorial again
s	running	Check if CodeWhisperer is running
s	launch	Launch the CodeWhisperer desktop app
s	restart	Restart the CodeWhisperer desktop app
s	quit	Quit the CodeWhisperer desktop app
s	set-path	Set the internal pseudo-terminal path
s	uninstall	Uninstall the CodeWhisperer app
s	prompts	Prompts shown on terminal startup
@	help app install
@	help app onboarding
@	help app running
@	help app launch
@	help app restart
@	help app quit
@	help app set-path
@	help app uninstall
@	help app prompts
@	help debug
s	app	Debug CodeWhisperer app
s	build	Switch to another branch of a Fig.js app
s	autocomplete-window	Toggle/set autocomplete window debug mode
s	logs	Show CodeWhisperer debug logs
s	input-method	CodeWhisperer input method editor
s	prompt-accessibility	Prompt accessibility
s	sample	Sample CodeWhisperer process
s	verify-codesign	Debug CodeWhisperer codesign verification
s	accessibility	Accessibility
s	key-tester	Key Tester
s	diagnostics	Watches diagnostics
s	query-index	Queries remote repository for updates given the specified metadata
s	devtools	Open up the devtools of a specific webview
s	get-index	Displays remote index
s	list-intellij-variants	Lists installed IntelliJ variants
s	shell	Disables sourcing of user shell config and instead uses a minimal CodeWhisperer default
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
@	help tips
s	enable	Enable fig tips
s	disable	Disable fig tips
@	help tips enable
@	help tips disable
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
s	login	Login to CodeWhisperer
s	logout	Logout of CodeWhisperer
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
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
@	help integrations install dotfiles
@	help integrations install daemon
@	help integrations install ssh
@	help integrations install input-method
@	help integrations install vscode
@	help integrations install intellij
@	help integrations install all
@	help integrations uninstall
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
@	help integrations uninstall dotfiles
@	help integrations uninstall daemon
@	help integrations uninstall ssh
@	help integrations uninstall input-method
@	help integrations uninstall vscode
@	help integrations uninstall intellij
@	help integrations uninstall all
@	help integrations reinstall
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
@	help integrations reinstall dotfiles
@	help integrations reinstall daemon
@	help integrations reinstall ssh
@	help integrations reinstall input-method
@	help integrations reinstall vscode
@	help integrations reinstall intellij
@	help integrations reinstall all
@	help integrations status
s	dotfiles	
s	daemon	
s	ssh	
s	input-method	
s	vscode	
s	intellij	
s	all	
@	help integrations status dotfiles
@	help integrations status daemon
@	help integrations status ssh
@	help integrations status input-method
@	help integrations status vscode
@	help integrations status intellij
@	help integrations status all
@	help ai
@	help version
@	help help-all
@	help dashboard
@	help help
