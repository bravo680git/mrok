@	
s	action|ac	Send actions to a specific session
s	attach|a	Attach to a session
s	convert-config	Convert configuration files
s	convert-layout	Convert layout files
s	convert-theme	Convert theme files
s	delete-all-sessions|da	Delete all sessions
s	delete-session|d	Delete a specific session
s	edit|e	Edit file with default $EDITOR / $VISUAL
s	help	Print this message or the help of the given subcommand(s)
s	kill-all-sessions|ka	Kill all sessions
s	kill-session|k	Kill a specific session
s	list-aliases|la	List existing plugin aliases
s	list-sessions|ls	List active sessions
s	options	Change the behaviour of zellij
s	pipe	Send data to one or more plugins, launch them if they are not running
s	plugin|p	Load a plugin
s	run|r	Run a command in a new pane
s	setup	Setup zellij and check its configuration
o	-c|--config	Change where zellij looks for the configuration file	v
o	--config-dir	Change where zellij looks for the configuration directory	v
o	-d|--debug	Specify emitting additional debug information	
o	--data-dir	Change where zellij looks for plugins	v
o	-h|--help	Print help information	p
o	-l|--layout	Name of a predefined layout inside the layout directory or the path to a layout file	v
o	--max-panes	Maximum panes on screen, caution: opening more panes will close old ones	v
o	-n|--new-session-with-layout	Name of a predefined layout inside the layout directory or the path to a layout file	v
o	-s|--session	Specify name of a new session	v
o	-V|--version	Print version information	
=		-c
t	filepaths
=		--config-dir
t	folders
=		--data-dir
t	folders
=		-l
t	filepaths
=		-n
t	filepaths
@	action
s	clear	Clear all buffers for a focused pane
s	close-pane	Close the focused pane
s	close-tab	Close the current tab
s	dump-layout	Dump current layout to stdout
s	dump-screen	Dump the focused pane to a file
s	edit	Open the specified file in a new zellij pane with your default EDITOR
s	edit-scrollback	Open the pane scrollback in your default editor
s	focus-next-pane	Change focus to the next pane
s	focus-previous-pane	Change focus to the previous pane
s	go-to-next-tab	Go to the next tab
s	go-to-previous-tab	Go to the previous tab
s	go-to-tab	Go to tab with index [index]
s	go-to-tab-name	Go to tab with name [name]
s	half-page-scroll-down	Scroll down half page in focus pane
s	half-page-scroll-up	Scroll up half page in focus pane
s	help	Print this message or the help of the given subcommand(s)
s	launch-or-focus-plugin	Launch or focus a plugin
s	launch-plugin	Launch a plugin
s	list-clients	List connected clients
s	move-focus	Move the focused pane in the specified direction. [right|left|up|down]
s	move-focus-or-tab	Move focus to the pane or tab (if on screen edge) in the specified direction [right|left|up|down]
s	move-pane	Change the location of the focused pane in the specified direction or rotate forwards…
s	move-pane-backwards	Rotate the location of the previous pane backwards
s	move-tab	Move the focused tab in the specified direction. [right|left]
s	new-pane	Open a new pane in the specified direction [right|down] If no direction is specified, will try to…
s	new-tab	Create a new tab, optionally with a specified tab layout and name
s	next-swap-layout	Swap to the next layout
s	page-scroll-down	Scroll down one page in focus pane
s	page-scroll-up	Scroll up one page in focus pane
s	previous-swap-layout	Swap to the previous layout
s	query-tab-names	Query all tab names
s	rename-pane	Renames the focused pane
s	rename-session	Rename the current session
s	rename-tab	Renames the focused pane
s	resize	[increase|decrease] the focused panes area at the [left|down|up|right] border
s	scroll-down	Scroll down in focus pane
s	scroll-to-bottom	Scroll down to bottom in focus pane
s	scroll-to-top	Scroll up to top in focus pane
s	scroll-up	Scroll up in the focused pane
s	start-or-reload-plugin	Start or reload a plugin
s	switch-mode	Switch input mode of all connected clients [locked|pane|tab|resize|move|search|session]
s	toggle-active-sync-tab	Toggle between sending text commands to all panes on the current tab and normal mode
s	toggle-floating-panes	Toggle the visibility of all floating panes in the current Tab, open one if none exist
s	toggle-fullscreen	Toggle between fullscreen focus pane and normal layout
s	toggle-pane-embed-or-floating	Embed focused pane if floating or float focused pane if embedded
s	toggle-pane-frames	Toggle frames around panes in the UI
s	undo-rename-pane	Remove a previously set pane name
s	undo-rename-tab	Remove a previously set tab name
s	write	Write bytes to the terminal
s	write-chars	Write characters to the terminal
@	action clear
@	action close-pane
@	action close-tab
@	action dump-layout
@	action dump-screen
a	1	0
#	action dump-screen	1
t	filepaths
@	action edit
@	action edit-scrollback
@	action focus-next-pane
@	action focus-previous-pane
@	action go-to-next-tab
@	action go-to-previous-tab
@	action go-to-tab
@	action go-to-tab-name
@	action half-page-scroll-down
@	action half-page-scroll-up
@	action help
@	action launch-or-focus-plugin
@	action launch-plugin
@	action list-clients
@	action move-focus
@	action move-focus-or-tab
@	action move-pane
@	action move-pane-backwards
@	action move-tab
@	action new-pane
@	action new-tab
@	action next-swap-layout
@	action page-scroll-down
@	action page-scroll-up
@	action previous-swap-layout
@	action query-tab-names
@	action rename-pane
@	action rename-session
@	action rename-tab
@	action resize
@	action scroll-down
@	action scroll-to-bottom
@	action scroll-to-top
@	action scroll-up
@	action start-or-reload-plugin
@	action switch-mode
@	action toggle-active-sync-tab
@	action toggle-floating-panes
@	action toggle-fullscreen
@	action toggle-pane-embed-or-floating
@	action toggle-pane-frames
@	action undo-rename-pane
@	action undo-rename-tab
@	action write
@	action write-chars
@	attach
o	-b|--background	Create a detached session in the background if one does not exist	
o	-c|--create	Create a session if one does not exist	
o	-f|--force-run-commands	If resurrecting a dead session, immediately run all its commands on startup	
o	--index	Number of the session index in the active sessions ordered creation date	
a	1	0
#	attach	1
d
@	convert-config
a	1	0
#	convert-config	1
t	filepaths
@	convert-layout
a	1	0
#	convert-layout	1
t	filepaths
@	convert-theme
a	1	0
#	convert-theme	1
t	filepaths
@	delete-all-sessions
o	-f|--force	Kill the sessions if they're running before deleting them	
o	-y|--yes	Automatic yes to prompts	
@	delete-session
o	-f|--force	Kill the sessions if they're running before deleting them	
a	1	0
#	delete-session	1
d
@	edit
o	--cwd	Change the working directory of the editor	v
o	-d|--direction	Direction to open the new pane in	v
o	-f|--floating	Open the new pane in floating mode	
o	--height	The height if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
o	-i|--in-place	Open the new pane in place of the current pane, temporarily suspending it	
o	-l|--line-number	Open the file in the specified line number	v
o	--width	The width if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
o	-x|--x	The x coordinates if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
o	-y|--y	The y coordinates if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
a	1	0
=	edit	--cwd
t	folders
#	edit	1
t	filepaths
@	help
@	kill-all-sessions
o	-y|--yes	Automatic yes to prompts	
@	kill-session
a	1	0
#	kill-session	1
d
@	list-aliases
@	list-sessions
o	-n|--no-formatting	Do not add colors and formatting to the list	
o	-r|--reverse	List the sessions in reverse order	
o	-s|--short	Print just the session name	
@	options
o	--attach-to-session	Whether to attach to a session specified in 'session-name' if it exists	v
o	--auto-layout	Whether to lay out panes in a predefined set of layouts whenever possible	v
o	--copy-clipboard	OSC52 destination clipboard	v
o	--copy-command	Switch to using a user supplied command for clipboard instead of OSC52	v
o	--copy-on-select	Automatically copy when selecting text (true or false)	v
o	--default-cwd	Set the default cwd	v
o	--default-layout	Set the default layout	v
o	--default-mode	Set the default mode	v
o	--default-shell	Set the default shell	v
o	--disable-mouse-mode	Disable handling of mouse events	
o	--disable-session-metadata	If true, will disable writing session metadata to disk	v
o	--layout-dir	Set the layout_dir, defaults to subdirectory of config dir	v
o	--mirror-session	Mirror session when multiple users are connected	v
o	--mouse-mode	Set the handling of mouse events (true or false) Can be temporarily bypassed by the [SHIFT] key	v
o	--no-pane-frames	Disable display of pane frames	
o	--on-force-close	Set behaviour on force close (quit or detach)	v
o	--pane-frames	Set display of the pane frames (true or false)	v
o	--scroll-buffer-size		v
o	--scrollback-editor	Explicit full path to open the scrollback editor (default is $EDITOR or $VISUAL)	v
o	--scrollback-lines-to-serialize	Scrollback lines to serialize along with the pane viewport when serializing sessions, 0 defaults…	v
o	--serialization-interval	The interval at which to serialize sessions for resurrection (in seconds)	v
o	--serialize-pane-viewport	Whether pane viewports are serialized along with the session, default is false	v
o	--session-name	The name of the session to create when starting Zellij	v
o	--session-serialization	Whether sessions should be serialized to the HD	v
o	--simplified-ui	Allow plugins to use a more simplified layout that is compatible with more fonts	v
o	--styled-underlines	Whether to use ANSI styled underlines	v
o	--support-kitty-keyboard-protocol	Whether to enable support for the Kitty keyboard protocol	v
o	--theme	Set the default theme	v
o	--theme-dir	Set the theme_dir, defaults to subdirectory of config dir	v
=	options	--attach-to-session
v	true	
v	false	
=	options	--auto-layout
v	true	
v	false	
=	options	--copy-clipboard
v	system	
v	primary	
=	options	--copy-on-select
v	true	
v	false	
=	options	--disable-session-metadata
v	true	
v	false	
=	options	--layout-dir
t	folders
=	options	--mirror-session
v	true	
v	false	
=	options	--mouse-mode
v	true	
v	false	
=	options	--pane-frames
v	true	
v	false	
=	options	--serialize-pane-viewport
v	true	
v	false	
=	options	--session-serialization
v	true	
v	false	
=	options	--simplified-ui
v	true	
v	false	
=	options	--styled-underlines
v	true	
v	false	
=	options	--support-kitty-keyboard-protocol
v	true	
v	false	
=	options	--theme-dir
t	folders
@	pipe
o	-n|--name	The name of the pipe	v
o	-a|--args	The args of the pipe	v
o	-p|--plugin	The plugin url (eg. file:/tmp/my-plugin.wasm) to direct this pipe to, if not specified, will be…	v
o	-c|--plugin-configuration	The plugin configuration (note: the same plugin with different configuration is considered a…	v
a	1	0
@	plugin
o	-c|--configuration	Plugin configuration	v
o	-f|--floating	Open the new pane in floating mode	
o	--height	The height if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
o	-i|--in-place	Open the new pane in place of the current pane, temporarily suspending it	
o	--width	The width if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
o	-x|--x	The x coordinates if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
o	-y|--y	The y coordinates if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
a	1	0
@	run
o	-c|--close-on-exit	Close the pane immediately when its command exits	
o	--cwd	Change the working directory of the new pane	v
o	-d|--direction	Direction to open the new pane in	v
o	-f|--floating	Open the new pane in floating mode	
o	--height	The height if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
o	-i|--in-place	Open the new pane in place of the current pane, temporarily suspending it	
o	-n|--name	Name of the new pane	v
o	-s|--start-suspended	Start the command suspended, only running after you first presses ENTER	
o	--width	The width if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
o	-x|--x	The x coordinates if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
o	-y|--y	The y coordinates if the pane is floating as a bare integer (eg. 1) or percent (eg. 10%)	v
a	1	0
=	run	--cwd
t	folders
@	setup
o	--check	Checks the configuration of zellij and displays currently used directories	
o	--clean	Disables loading of configuration file at default location, loads the defaults that zellij ships…	
o	--dump-config	Dump the default configuration file to stdout	
o	--dump-layout	Dump specified layout to stdout	v
o	--dump-plugins	Dump the builtin plugins to DIR or 'DATA DIR' if unspecified	v
o	--dump-swap-layout	Dump the specified swap layout file to stdout	v
o	--generate-auto-start	Generates auto-start script for the specified shell	v
o	--generate-completion	Generates completion for the specified shell	v
=	setup	--generate-completion
v	bash	
v	fish	
v	zsh	
