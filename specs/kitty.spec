@	
s	@	
s	icat	A cat like utility to display images in the terminal
s	+icat	A cat like utility to display images in the terminal
s	+list-fonts	
s	+hold	
s	+complete	
s	+runpy	
s	+launch	
s	+open	
s	+kitten	
s	+edit-config	
s	+shebang	
o	-T|--title	Set the OS window title	v
o	-C|--config	Specify a path to the configuration file(s) to use	v
o	-o|--override	Override individual configuration options	
o	-d|--directory|--working-directory	Change to the specified directory when launching	v
o	--session	Path to a file containing the startup session	v
o	--hold	Remain open after child process exits	
o	-1|--single-instance	Only a single instance of kitty will run	
o	--instance-group	Kitty will open a new window in an existing instance and quit immediately	v
o	--wait-for-single-instance-window-close	The new window will not quit till the newly opened window is closed	
o	--listen-on	Tell kitty to listen on the specified address for control messages	v
o	--start-as	Control how the initial kitty window is created	v
o	-v|--version	The current kitty version	
o	-h|--help	Display this help message	
a	1	0
=		-C
t	filepaths
=		-d
t	folders
=		--session
v	-	Read from stdin
t	filepaths
=		--start-as
v	normal	
v	fullscreen	
v	maximized	
v	minimized	
@	@
s	close-tab	Close the specified tab(s)
s	close-window	Close the specified window(s)
s	create-marker	
s	detach-tab	Detach the specified tab
s	detach-window	Detach the specified window
s	disable-ligatures	Control ligature rendering for the specified windows/tabs
s	env	Change the environment variables seen by processing in newly launched windows
s	focus-tab	The active window in the specified tab will be focused
s	focus-window	Focus the specified window, if no window is specified, focus the window this command is run inside
s	get-colors	Get the terminal colors for the specified window
s	get-text	
s	goto-layout	
s	kitten	
s	last-used-layout	
s	launch	
s	ls	
s	new-window	
s	remove-marker	
s	resize-os-window	
s	resize-window	
s	scroll-window	
s	select-window	
s	send-text	
s	set-background-image	
s	set-background-opacity	
s	set-colors	
s	set-enabled-layouts	
s	set-font-size	
s	set-spacing	
s	set-tab-color	The foreground and background colors when active and inactive can be overridden using this command
s	set-tab-title	Set the title for the specified tab(s)
s	set-window-logo	
s	set-window-title	Set the title of the specified window(s)
s	signal-child	Send one or more signals to the foreground process in the specified window(s)
o	--to	An address for the kitty instance to control	v
@	@ close-tab
o	-m|--match	The tab to match	v
o	--self	Close the tab of the window this command is run in, rather than the active tab	
o	--target-group	Close the specified group of tabs	v
@	@ close-window
o	-m|--match	The window to match	v
o	--self	Close the window this command is run in, rather than the active window	
@	@ create-marker
o	-m|--match	The window to match	v
o	--self	Close the window this command is run in, rather than the active window	
a	2	0
@	@ detach-tab
o	-m|--match	The tab to match	v
o	-t|--target-tab	The tab to match	v
o	--self	Detach the tab this command is run in, rather than the active tab	
@	@ detach-window
o	-m|--match	The window to match	v
o	-t|--target-tab	The tab to match	v
o	--self	Detach the window this command is run in, rather than the active window	
@	@ disable-ligatures
o	-a|--all	Disable in all windows	
o	-m|--match	The window to match	v
o	-t|--match-tab	The tab to match	
a	1	0
#	@ disable-ligatures	1
v	never	
v	always	
v	cursor	
@	@ env
a	1	1
@	@ focus-tab
o	-m|--match	The tab to match	v
o	--no-response	Don't wait for a response indicating the success of the action	
@	@ focus-window
o	-m|--match	The window to match	v
o	--no-response	Don't wait for a response indicating the success of the action	
@	@ get-colors
o	-c|--configured	Instead of outputting the colors for the specified window, output the currently configured colors	
o	-m|--match	The window to match	
@	@ get-text
@	@ goto-layout
@	@ kitten
@	@ last-used-layout
@	@ launch
@	@ ls
@	@ new-window
@	@ remove-marker
@	@ resize-os-window
@	@ resize-window
@	@ scroll-window
@	@ select-window
@	@ send-text
@	@ set-background-image
@	@ set-background-opacity
@	@ set-colors
@	@ set-enabled-layouts
@	@ set-font-size
@	@ set-spacing
@	@ set-tab-color
o	-m|--match	The tab to match	v
o	--self	Close the window this command is run in, rather than the active window	
@	@ set-tab-title
o	-m|--match	The tab to match	
@	@ set-window-logo
@	@ set-window-title
o	-m|--match	The window to match	
o	--temporary	The title can be overwritten by escape sequences	
@	@ signal-child
o	-m|--match	The window to match	
a	1	1
@	icat
o	--align	Horizontal alignment for the displayed image	v
o	--place	Choose where on the screen to display the image	v
o	--scale-up	Images that are smaller than the specified area to be scaled up to use as much of the specified…	
o	--background	Specify a background color, this will cause transparent images to be composited on top of the…	v
o	--mirror	Mirror the image about a horizontal or vertical axis or both	v
o	--clear	Remove all images currently displayed on the screen	
o	--transfer-mode	Which mechanism to use to transfer images to the terminal	v
o	--detect-support	Detect support for image display in the terminal	
o	--detection-timeout	How long to wait for detection to complete before aborting	v
o	--print-window-size	Print the current terminal window size in pixels	
o	--stdin	Read an image from stdin	
a	1	0
=	icat	--align
v	center	
v	left	
v	right	
=	icat	--background
v	none	
v	black	
v	white	
v	gray	
v	red	
v	green	
v	blue	
v	yellow	
v	magenta	
v	cyan	
=	icat	--mirror
v	horizontal	
v	both	
v	none	
v	vertical	
=	icat	--transfer-mode
v	file	
v	detect	
v	stream	
#	icat	1
t	filepaths
@	+icat
o	--align	Horizontal alignment for the displayed image	v
o	--place	Choose where on the screen to display the image	v
o	--scale-up	Images that are smaller than the specified area to be scaled up to use as much of the specified…	
o	--background	Specify a background color, this will cause transparent images to be composited on top of the…	v
o	--mirror	Mirror the image about a horizontal or vertical axis or both	v
o	--clear	Remove all images currently displayed on the screen	
o	--transfer-mode	Which mechanism to use to transfer images to the terminal	v
o	--detect-support	Detect support for image display in the terminal	
o	--detection-timeout	How long to wait for detection to complete before aborting	v
o	--print-window-size	Print the current terminal window size in pixels	
o	--stdin	Read an image from stdin	
a	1	0
=	+icat	--align
v	center	
v	left	
v	right	
=	+icat	--background
v	none	
v	black	
v	white	
v	gray	
v	red	
v	green	
v	blue	
v	yellow	
v	magenta	
v	cyan	
=	+icat	--mirror
v	horizontal	
v	both	
v	none	
v	vertical	
=	+icat	--transfer-mode
v	file	
v	detect	
v	stream	
#	+icat	1
t	filepaths
@	+list-fonts
@	+hold
@	+complete
@	+runpy
@	+launch
@	+open
@	+kitten
s	icat	A cat like utility to display images in the terminal
s	diff	
s	show_key	
s	clipboard	
s	unicode_input	
s	panel	
s	transfer	
s	query_terminal	
s	broadcast	
s	hyperlinked_grep	
s	ssh	
s	choose	
s	ask	
s	themes	Change the kitty theme
s	hints	
s	remote_file	
s	show_error	
s	resize_window	
s	mouse_demo	
@	+kitten icat
o	--align	Horizontal alignment for the displayed image	v
o	--place	Choose where on the screen to display the image	v
o	--scale-up	Images that are smaller than the specified area to be scaled up to use as much of the specified…	
o	--background	Specify a background color, this will cause transparent images to be composited on top of the…	v
o	--mirror	Mirror the image about a horizontal or vertical axis or both	v
o	--clear	Remove all images currently displayed on the screen	
o	--transfer-mode	Which mechanism to use to transfer images to the terminal	v
o	--detect-support	Detect support for image display in the terminal	
o	--detection-timeout	How long to wait for detection to complete before aborting	v
o	--print-window-size	Print the current terminal window size in pixels	
o	--stdin	Read an image from stdin	
a	1	0
=	+kitten icat	--align
v	center	
v	left	
v	right	
=	+kitten icat	--background
v	none	
v	black	
v	white	
v	gray	
v	red	
v	green	
v	blue	
v	yellow	
v	magenta	
v	cyan	
=	+kitten icat	--mirror
v	horizontal	
v	both	
v	none	
v	vertical	
=	+kitten icat	--transfer-mode
v	file	
v	detect	
v	stream	
#	+kitten icat	1
t	filepaths
@	+kitten diff
a	2	0
#	+kitten diff	1
t	filepaths
#	+kitten diff	2
t	filepaths
@	+kitten show_key
@	+kitten clipboard
@	+kitten unicode_input
@	+kitten panel
@	+kitten transfer
@	+kitten query_terminal
@	+kitten broadcast
@	+kitten hyperlinked_grep
@	+kitten ssh
@	+kitten choose
@	+kitten ask
@	+kitten themes
@	+kitten hints
@	+kitten remote_file
@	+kitten show_error
@	+kitten resize_window
@	+kitten mouse_demo
@	+edit-config
@	+shebang
