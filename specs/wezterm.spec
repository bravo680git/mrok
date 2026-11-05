@	
s	start	Start the GUI, optionally running an alternative program
s	ssh	Establish an ssh session
s	serial	Open a serial port
s	connect	Connect to wezterm multiplexer
s	ls-fonts	Display information about fonts
s	show-keys	Show key assignments
s	cli	Interact with experimental mux server
s	imgcat	Output an image to the terminal
s	set-working-directory	Advise the terminal of the current working directory by emitting an OSC 7 escape sequence
s	record	Record a terminal session as an asciicast
s	replay	Replay an asciicast terminal session
s	shell-completion	Generate shell completion information
s	help	Print this message or the help of the given subcommand(s)
o	--config-file	Specify the configuration file to use, overrides the normal configuration file resolution	V
o	--config	Override specific configuration values	V
o	-h|--help	Print help information	
o	-V|--version	Print version information	
o	-n	Skip loading wezterm.lua	
=		--config-file
t	filepaths
@	start
o	--cwd	Specify the current working directory for the initially spawned program	V
o	--class	Override the default windowing system class. The default is "org.wezfurlong.wezterm". Under X11…	V
o	--workspace	Override the default workspace with the provided name. The default is "default"	V
o	--position	Override the position for the initial window launched by this process	V
o	--no-auto-connect	If true, do not connect to domains marked as connect_automatically in your wezterm configuration…	
o	--always-new-process	If enabled, don't try to ask an existing wezterm GUI instance to start the command. Instead…	
o	-h|--help	Print help information	
a	1	1
=	start	--cwd
t	folders
@	ssh
o	-o|--ssh-option	Override specific SSH configuration options. `wezterm ssh` is able to parse some (but not all!)…	V
o	--class	Override the default windowing system class. The default is "org.wezfurlong.wezterm". Under X11…	V
o	--position	Override the position for the initial window launched by this process	V
o	-v	Enable verbose ssh protocol tracing. The trace information is printed to the stderr stream of the…	
o	-h|--help	Print help information	
a	2	1
@	serial
o	--baud	Set the baud rate. The default is 9600 baud	V
o	--class	Override the default windowing system class. The default is "org.wezfurlong.wezterm". Under X11…	V
o	--position	Override the position for the initial window launched by this process	V
o	-h|--help	Print help information	
a	1	0
@	connect
o	--class	Override the default windowing system class. The default is "org.wezfurlong.wezterm". Under X11…	V
o	--workspace	Override the default workspace with the provided name. The default is "default"	V
o	--position	Override the position for the initial window launched by this process	V
o	-h|--help	Print help information	
a	2	1
@	ls-fonts
o	--text	Explain which fonts are used to render the supplied text string	V
o	--list-system	Whether to list all fonts available to the system	
o	--rasterize-ascii	Show rasterized glyphs for the text in --text using ascii blocks	
o	-h|--help	Print help information	
@	show-keys
o	--key-table	In lua mode, show only the named key table	V
o	--lua	Show the keys as lua config statements	
o	-h|--help	Print help information	
@	cli
s	list	List windows, tabs and panes
s	list-clients	List clients
s	proxy	Start rpc proxy pipe
s	tlscreds	Obtain tls credentials
s	move-pane-to-new-tab	Move a pane into a new tab
s	split-pane	Split the current pane. Outputs the pane-id for the newly created pane on success
s	spawn	Spawn a command into a new window or tab. Outputs the pane-id for the newly created pane on success
s	send-text	Send text to a pane as though it were pasted. If bracketed paste mode is enabled in the pane, then…
s	help	Print this message or the help of the given subcommand(s)
o	--class	When connecting to a gui instance, if you started the gui with `--class SOMETHING`, you should…	V
o	--no-auto-start	Don't automatically start the server	
o	--prefer-mux	Prefer connecting to a background mux server. The default is to prefer connecting to a running…	
o	-h|--help	Print help information	
@	cli list
o	--format	Controls the output format. "table" and "json" are possible formats	V
o	-h|--help	Print help information	
@	cli list-clients
o	--format	Controls the output format. "table" and "json" are possible formats	V
o	-h|--help	Print help information	
@	cli proxy
o	-h|--help	Print help information	
@	cli tlscreds
o	-h|--help	Print help information	
@	cli move-pane-to-new-tab
o	--pane-id	Specify the pane that should be moved. The default is to use the current pane based on the…	V
o	--window-id	Specify the window into which the new tab will be created. If omitted, the window associated with…	V
o	--workspace	If creating a new window, override the default workspace name with the provided name. The default…	V
o	--new-window	Create tab in a new window, rather than the window currently containing the pane	
o	-h|--help	Print help information	
@	cli split-pane
o	--pane-id	Specify the pane that should be split. The default is to use the current pane based on the…	V
o	--cells	The number of cells that the new split should have. If omitted, 50% of the available space is used	V
o	--percent	Specify the number of cells that the new split should have, expressed as a percentage of the…	V
o	--cwd	Specify the current working directory for the initially spawned program	V
o	--move-pane-id	Instead of spawning a new command, move the specified pane into the newly created split	V
o	--horizontal	Equivalent to `--right`. If neither this nor any other direction is specified, the default is…	
o	--left	Split horizontally, with the new pane on the left	
o	--right	Split horizontally, with the new pane on the right	
o	--top	Split vertically, with the new pane on the top	
o	--bottom	Split vertically, with the new pane on the bottom	
o	--top-level	Rather than splitting the active pane, split the entire window	
o	-h|--help	Print help information	
a	1	1
=	cli split-pane	--cwd
t	folders
@	cli spawn
o	--pane-id	Specify the current pane. The default is to use the current pane based on the environment variable…	V
o	--domain-name		V
o	--window-id	Specify the window into which to spawn a tab. If omitted, the window associated with the current…	V
o	--cwd	Specify the current working directory for the initially spawned program	V
o	--workspace	When creating a new window, override the default workspace name with the provided name. The…	V
o	--new-window	Spawn into a new window, rather than a new tab	
o	-h|--help	Print help information	
a	1	1
=	cli spawn	--cwd
t	folders
@	cli send-text
o	--pane-id	Specify the target pane. The default is to use the current pane based on the environment variable…	V
o	--no-paste	Send the text directly, rather than as a bracketed paste	
o	-h|--help	Print help information	
a	1	0
@	cli help
a	1	0
@	imgcat
o	--width	Specify the display width; defaults to "auto" which automatically selects an appropriate size. You…	V
o	--height	Specify the display height; defaults to "auto" which automatically selects an appropriate size…	V
o	--no-preserve-aspect-ratio	Do not respect the aspect ratio. The default is to respect the aspect ratio	
o	-h|--help	Print help information	
a	1	0
#	imgcat	1
t	filepaths
@	set-working-directory
o	-h|--help	Print help information	
a	2	0
#	set-working-directory	1
t	folders
@	record
o	-h|--help	Print help information	
a	1	0
@	replay
o	--explain	Explain what is being sent/received	
o	-h|--help	Print help information	
a	1	0
@	shell-completion
o	--shell	Which shell to generate for	v
o	-h|--help	Print help information	
=	shell-completion	--shell
v	bash	
v	elvish	
v	fish	
v	power-shell	
v	zsh	
v	fig	
@	help
a	1	0
