@	
s	a|at|attach|attach-session	Attach to last session
s	bind|bind-key	Bind a key to a command
s	breakp|break-pane	Break a pane from an exiting into a new window
s	capturep|capture-pane	Capture the contents of a pane to a buffer
s	choose-buffer	Put a pane into buffer choice mode
s	choose-client	Put a pane into buffer client mode
s	choose-tree	Put a pane into buffer tree mode
s	clearhist|clear-history	Remove and clear history for a pane
s	clock-mode	Enter clock mode
s	command-prompt	Open the tmux command prompt in a client
s	confirm|confirm-before	Run a command but ask for confirmation before
s	copy-mode	Enter copy mode
s	deleteb|delete-buffer	Delete a paste buffer
s	detach|detach-client	Detach a client from the server
s	menu|display-menu	Display menu on target-client
s	display|display-message	Display a message in the status line
s	displayp|display-panes	Display an indicator for each visible pane
s	findw|find-window	Search for a pattern in windows
s	has|has-session	Check and report if a session exists on the server
s	if|if-shell	Execute a tmux command if a shell-command succeeded
s	joinp|join-pane|movep|move-pane	Split a pane and move an existing one into the new space
s	killp|kill-pane	Destroy a given pane
s	kill-server	Kill clients, session and server
s	kill-ses|kill-session	Kill/delete sessions
s	killw|kill-window	Destroy a given window
s	lastp|last-pane	Select the previously selected pane
s	last|last-window	Select the previously selected window
s	linkw|link-window	Link a window to another
s	lsb|list-buffers	List paste buffers of a session
s	lsc|list-clients	List clients attached to a server
s	lscm|list-commands	List supported sub-commands
s	lsk|list-keys	List all key-bindings
s	lsp|list-panes	List panes of a window
s	ls|list-sessions	List sessions managed by a server
s	lsw|list-windows	List windows of a session
s	loadb|load-buffer	Load a file into a paste buffer
s	lockc|lock-client	Lock a client
s	lock|lock-server	Lock all clients attached to the server
s	locks|lock-session	Lock all clients attached to a session
s	movew|move-window	Move a window to another
s	new|new-session	Create a new session
s	neww|new-window	Create a new window
s	nextl|next-layout	Move a window to the next layout
s	next|next-window	Move to the next window in a session
s	pasteb|paste-buffer	Insert a paste buffer into the window
s	pipep|pipe-pane	Pipe output from a pane to a shell command
s	prevl|previous-layout	Move a window to the previous layout
s	prev|previous-window	Move to the previous window in a session
s	refresh|refresh-client	Refresh a client
s	rename|rename-session	Rename a session
s	renamew|rename-window	Rename a window
s	resizep|resize-pane	Resize a pane
s	resizew|resize-window	Resize a window
s	respawnp|respawn-pane	Reactivate a pane in which a command has exited
s	respawnw|respawn-window	Reactivate a window in which a command has exited
s	rotatew|rotate-window	Rotate positions of panes in a window
s	run|run-shell	Execute a command without create a new window
s	saveb|save-buffer	Save a paste buffer to a file
s	selectl|select-layout	Choose a layout for a pane
s	selectp|select-pane	Make a pane the active one in the window
s	selectw|select-window	Select a window
s	send|send-keys	Send key(s) to a window
s	send-prefix	Send the prefix key to a window
s	info|server-info	Show every session, window, pane, etc
s	setb|set-buffer	Set content of a paste buffer
s	setenv|set-environment	(Un)set an environment variable
s	set-hook	Set a hook to a command
s	set|set-option	Set a session option
s	setw|set-window-option	Set a window option
s	showb|show-buffer	Display the contents of a paste buffer
s	showenv|show-environment	Display the environment
s	show-hooks	Show the global list of hooks
s	showmsgs|show-messages	Show client's message log
s	show|show-options	Show session options
s	showw|show-winsow-options	Show window options
s	source|source-file	Execute tmux commands from a file
s	splitw|split-window	Splits a pane into two
s	start|start-server	Start a tmux server
s	suspendc|suspend-client	Suspend a client
s	swapp|swap-pane	Swap two panes
s	swapw|swap-window	Swap two windows
s	switchc|switch-client	Switch the client to another session
s	unbind|unbind-key	Unbind a key
s	unlinkw|unlink-window	Unlink a window
s	wait|wait-for	Wait for an event or trigger it
@	a
o	-d	Detach all others clients to the session	
o	-x	Send SIGHUP to the parent process and detach the client	
o	-f	Set client flags	v
o	-c	Set the session's working directory	v
o	-E	Don't use update-environment option	
o	-t	Attach to a session with the given name	v
=	a	-f
v	active-pane	
v	ignore-size	
v	no-output	
v	pause-after	
v	read-only	
v	wait-exit	
=	a	-c
t	folders
=	a	-t
d
@	bind
o	-n	Alias for -T root	
o	-r	Indicate that this key may repeat	
o	-N	Attach a note to the key	v
o	-T	The key table to use	v
a	3	1
@	breakp
o	-a	Move the window to the next index after	
o	-b	Move the window to the next index before	
o	-d	The new windows does not become the current window	
o	-P	Print information about the new window	
o	-F	Format output	v
o	-n	The target window	v
o	-s	The source pane	v
o	-t	The destination window	v
=	breakp	-n
d
=	breakp	-s
d
=	breakp	-t
d
@	capturep
o	-a	Use the alternate screen and history is not accessible	
o	-e	Include escape sequences for text and background attributes	
o	-p	Redirect output to stdout	
o	-P	Capture only outputs that is the beginning of an as-yet incomplete escape sequence	
o	-q	Do not throw an error if not alternate screen is found	
o	-C	Escape non-printable characters as octal	
o	-J	Preserve trailing spaces and join any wrapped lines	
o	-N	Preserve trailing spaces at each line's end	
o	-b	The buffer name	v
o	-E	Ending line number	v
o	-S	Starting line number	v
o	-t	The target pane	v
=	capturep	-b
d
=	capturep	-t
d
@	choose-buffer
o	-N	Start without the preview	
o	-Z	Zoom the pane	
o	-r	Reverse the sort order	
o	-F	Format output	v
o	-f	Specify an initial filter	v
o	-O	Specify the sort order	v
o	-t	The target pane	v
a	1	0
=	choose-buffer	-O
v	time	
v	name	
v	size	
=	choose-buffer	-t
d
@	choose-client
o	-N	Start without the preview	
o	-r	Reserve the sort order	
o	-Z	Zoom the pane	
o	-F	Format output	v
o	-f	Specify an initial filter	v
o	-O	Specify the initial sort field	v
o	-t	The target pane	v
a	1	0
=	choose-client	-O
v	name	
v	size	
v	creation	
v	activity	
=	choose-client	-t
d
@	choose-tree
o	-G	Include all sessions in any session group in the tree	
o	-N	Start without the preview	
o	-r	Reserve the sort order	
o	-s	Start with sessions collapsed	
o	-w	Start with windows collapsed	
o	-Z	Zoom the pane	
o	-F	Format output	v
o	-f	Specify an initial filter	v
o	-O	Specify the initial sort field	v
o	-t	The target pane	v
a	1	0
=	choose-tree	-O
v	name	
v	size	
v	creation	
v	activity	
=	choose-tree	-t
d
@	clearhist
@	clock-mode
@	command-prompt
o	-l	The prompt only accept one key press	
o	-i	Execute the command every time the prompt input changes	
o	-k	Like -l but the key press is translated to a key name	
o	-N	The prompt only accept numeric key press	
o	-T	Tell that the prompt is for a target	
o	-W	Tell that the prompt is for a window	
o	-I	Comma-separated list of the initial text for each prompt	v
o	-p	Comma-separated list of prompts which are displayed in order	v
o	-t	The target client	v
a	1	0
=	command-prompt	-t
d
@	confirm
o	-p	A prompt to display for confirmation	v
o	-t	The target client	v
a	1	1
=	confirm	-t
d
@	copy-mode
o	-e	Scrolling to the bottom should exit copy mode	
o	-H	Hide the position indicator	
o	-M	Begin a mouse drag	
o	-q	Cancel copy mode and any other modes	
o	-u	Scroll one page up	
o	-s	The source pane	v
o	-t	The target pane	v
=	copy-mode	-s
d
=	copy-mode	-t
d
@	deleteb
o	-b	The target buffer	v
=	deleteb	-b
d
@	detach
o	-a	Kills all but the client given with -t	
o	-P	Send SIGHUP to the parent process	
o	-E	Run the given shell-command to replace the client	v
o	-t	The target client	v
o	-s	Detach all clients attached to the specified session	v
=	detach	-t
d
=	detach	-s
d
@	menu
o	-O	Do not close the menu when the mouse button is released	
o	-c	The target client	v
o	-t	The target pane	v
o	-T	Specify a title	v
o	-x	Give the x position of the menu	v
o	-y	Give the y position of the menu	v
a	3	1
=	menu	-c
d
=	menu	-t
d
@	display
o	-a	List the format variables and their values	
o	-I	Forward any input read from stdin to the empty pane target-pane	
o	-p	Print output to stdout	
o	-v	Print verbose logging as the format is parsed	v
o	-d	A delay for the message	v
o	-t	The target pane	v
a	1	0
=	display	-v
d
=	display	-t
d
@	displayp
o	-b	Do not block other commands from running until the indicator is closed	
o	-N	Do not close the indicator when a key is pressed	
o	-d	Specify the duration	v
o	-t	The target client	v
a	1	0
=	displayp	-t
d
@	findw
o	-i	Make the search ignore cases	
o	-C	Match only visible window contents	
o	-N	Match only the window name	
o	-r	Search a regular expression	
o	-T	Match only the window's title	
o	-Z	Zoom the pane	
o	-t	The target pane	v
a	1	0
=	findw	-t
d
@	has
o	-t	Specify the target session	v
=	has	-t
d
@	if
@	joinp
o	-b	Src-pane will be joined to left of or above dst-pane	v
o	-l	Set the size of the new space	v
o	-s	The source pane	v
o	-t	The destination pane	v
=	joinp	-b
d
=	joinp	-s
d
=	joinp	-t
d
@	killp
o	-a	Kill all but the target-pane	
o	-t	The target pane	v
=	killp	-t
d
@	kill-server
@	kill-ses
o	-t	Kill/delete session with the given name	v
o	-a	Kill/delete all session but the current	
o	-C	Clear alerts (bell, activity, or silence) in all windows linked to the session	
=	kill-ses	-t
d
@	killw
o	-a	Kill all but the target-window	
o	-t	The target window	v
=	killw	-t
d
@	lastp
o	-d	Disable input to the pane	
o	-e	Enable input to the pane	
o	-Z	Keep the window zoomed if it was zoomed	
o	-t	The target window	v
=	lastp	-t
d
@	last
o	-t	Select the previously select window of the target-session	v
=	last	-t
d
@	linkw
o	-a	Move the window to the next index after dst-window	
o	-b	Move the window to the next index before dst-window	
o	-d	Do not select the newly linked window	
o	-k	Kill dst-window if exist	
o	-s	The source window	v
o	-t	The destination window	v
=	linkw	-s
d
=	linkw	-t
d
@	lsb
@	lsc
o	-F	Format output	v
o	-t	List only clients connected to that session	v
=	lsc	-t
d
@	lscm
o	-F	Format output	v
a	1	0
@	lsk
@	lsp
o	-a	Ignore target-window and list all panes	
o	-s	Target-window becomes a session	
o	-F	Format output	v
o	-f	Specify a filter	v
o	-t	The target window	v
=	lsp	-t
d
@	ls
o	-F	Format output	v
o	-f	Filter the sessions	v
@	lsw
o	-a	Ignore target-session and list all windows	
o	-F	Format output	v
o	-f	Specify a filter	v
o	-t	The target session	v
=	lsw	-t
d
@	loadb
o	-w	Send the buffer to the clipboard	
o	-b	The target buffer	v
o	-t	The target client	v
a	1	0
=	loadb	-b
d
=	loadb	-t
d
@	lockc
o	-t	The target client	v
=	lockc	-t
d
@	lock
@	locks
o	-t	Lock all clients attached to target-session	v
=	locks	-t
d
@	movew
o	-a	Move the window to the next index after dst-window	
o	-b	Move the window to the next index before dst-window	
o	-r	Renumber all windows in the session in sequential order	
o	-d	Do not select the newly linked window	
o	-k	Kill dst-window if exist	
o	-s	The source window	v
o	-t	The destination window	v
=	movew	-s
d
=	movew	-t
d
@	new
o	-A	Behave like attach-session if session-name already exist	
o	-d	Use the initial size from default-size	
o	-D	Behave like -d if -A is set	
o	-E	Do not use update-environment option	
o	-P	Print information about the new session	
o	-X	Behave like -x if -A is set	
o	-c	Specify a start directory for the session	v
o	-e	Set environment variables	v
o	-f	Set client flags	v
o	-F	Format output	v
o	-n	Start a new session with the given name	v
o	-s	Start a new session with the given name	v
o	-t	The name of the group	v
o	-x	The width of the session	v
o	-y	The height of the session	v
a	1	0
=	new	-c
t	folders
=	new	-f
v	active-pane	
v	ignore-size	
v	no-output	
v	pause-after	
v	read-only	
v	wait-exit	
@	neww
o	-a	Insert the new window at the next index after target-window	
o	-b	Insert the new window at the next index before target-window	
o	-d	The session does not make the new window the current window	
o	-k	Kill the target-window if exist	
o	-P	Print information about the new window	
o	-S	Select window-name if exist	
o	-c	Specify a start directory for the window	v
o	-e	Set environment variables	v
o	-F	Format output	v
o	-n	Start a new window with the given name	v
o	-t	The target window	v
a	1	0
=	neww	-c
t	folders
=	neww	-t
d
@	nextl
o	-t	The target pane	v
=	nextl	-t
d
@	next
o	-a	Move to the next window with an alert	
o	-t	Move to the next window of the target-session	v
=	next	-t
d
@	pasteb
@	pipep
o	-I	Connect stdout to shell-command	
o	-O	Connect stdin to shell-command	
o	-o	Only open a new pipe if no previous pipe exists	
o	-t	The target pane	v
a	1	0
=	pipep	-t
d
@	prevl
o	-t	The target window	v
=	prevl	-t
d
@	prev
o	-a	Move with an alert	
o	-t	Move to the previous window of the target-session	v
=	prev	-t
d
@	refresh
o	-c	Return the tracking cursor	
o	-D	Allow the visible portion of a window to be changed	
o	-l	Request the clipboard from the client	
o	-L	Allow the visible portion of a window to be changed	
o	-R	Allow the visible portion of a window to be changed	
o	-S	Only update the client's status line	
o	-U	Allow the visible portion of a window to be changed	
o	-A	The target pane	v
o	-B	A subscription to a format for a control mode	v
o	-C	Set the width and height	v
o	-f	Set client flags	v
o	-t	The target client	v
a	1	0
=	refresh	-A
d
=	refresh	-f
v	active-pane	
v	ignore-size	
v	no-output	
v	pause-after	
v	read-only	
v	wait-exit	
=	refresh	-t
d
@	rename
o	-t	Rename the target-session	v
a	1	0
=	rename	-t
d
@	renamew
o	-t	The target window	v
a	1	0
=	renamew	-t
d
@	resizep
o	-D	Resize down by adjustment	
o	-L	Resize left by adjustment	
o	-M	Begin mouse resizing	
o	-R	Resize right by adjustment	
o	-T	Trim all lines below the current cursor position	
o	-U	Resize up by adjustment	
o	-Z	Toggle the active pane between zoomed and unzoomed	
o	-t	The target pane	v
o	-x	The width of the pane	v
o	-y	The height of the pane	v
a	1	0
=	resizep	-t
d
@	resizew
o	-a	Set the size of the smallest session containing the window	
o	-A	Set the size of the largest session containing the window	
o	-D	Resize down by adjustment	
o	-L	Resize left by adjustment	
o	-R	Resize right by adjustment	
o	-U	Resize up by adjustment	
o	-t	The target window	v
o	-x	The width of the pane	v
o	-y	The height of the pane	v
a	1	0
=	resizew	-t
d
@	respawnp
o	-k	Kill the target-pane if exist	
o	-c	Specify a start directory for the pane	v
o	-e	Set environment variables	v
o	-t	The target pane	v
a	1	0
=	respawnp	-c
t	folders
=	respawnp	-t
d
@	respawnw
o	-k	Kill the target-window if exist	
o	-c	Specify a start directory for the window	v
o	-e	Set environment variables	v
o	-t	The target window	v
a	1	0
=	respawnw	-c
t	folders
=	respawnw	-t
d
@	rotatew
o	-D	Rotate upward	
o	-U	Rotate downward	
o	-Z	Keep the window zoomed if it was zoomed	
o	-t	The target window	v
=	rotatew	-t
d
@	run
@	saveb
@	selectl
o	-E	Spread the current pane and any panes next to it evenly	
o	-n	Equivalent to next-layout	
o	-o	Apply the last set layout if possible	
o	-p	Equivalent to previous-layout	
o	-t	The target pane	v
a	1	0
=	selectl	-t
d
@	selectp
o	-D	Use the down pane	
o	-d	Disable input to the pane	
o	-e	Enable input to the pane	
o	-L	Use the left pane	
o	-l	Same as last-pane command	
o	-M	Clear the marked pane	
o	-m	Set the market pane	
o	-R	Use the right pane	
o	-U	Use the up pane	
o	-Z	Set the pane's title	
o	-T	Set the pane title	v
o	-t	The target pane	v
=	selectp	-t
d
@	selectw
o	-l	Same as last-window	
o	-n	Same as next-window	
o	-p	Same as previous-window	
o	-T	Same as last-window if the selected window is already the current window	
o	-t	The target window	v
=	selectw	-t
d
@	send
@	send-prefix
@	info
@	setb
o	-a	Append to rather than overwriting the buffer	
o	-w	Send the buffer to the clipboard	
o	-b	The name of the buffer	v
o	-t	The target client	v
o	-n	The new name of the buffer	v
a	1	0
=	setb	-b
d
=	setb	-t
d
@	setenv
@	set-hook
@	set
@	setw
@	showb
@	showenv
o	-t	Display the environment of the target-session	v
=	showenv	-t
d
@	show-hooks
@	showmsgs
o	-T	Show debugging information about terminals	
o	-J	Show debugging information about jobs	
o	-t	The target client	v
=	showmsgs	-t
d
@	show
@	showw
@	source
o	-F	Expand path as a format	
o	-n	Parse the file but don't run commands	
o	-q	Don't return any error if path does not exist	
o	-v	Show the parsed command and line numbers if possible	
a	1	1
@	splitw
o	-b	Create the new pane to the left of or above target-pane	
o	-f	Create a new pane spanning the full window height with -h or width with -v	
o	-h	Set the pane take full height	
o	-I	Create an empty pane and forward stdin to it	
o	-v	Set the pane take full width	
o	-Z	Zoom if the window is not zoomed	
o	-c	Specify a start directory for the pane	v
o	-e	Set environment variables	v
o	-l	Set the size in columns (horizontal split) or rows (vertical split)	v
o	-t	The target pane	v
o	-F	Format output	v
a	1	0
=	splitw	-c
t	folders
=	splitw	-t
d
@	start
@	suspendc
o	-t	The target client	v
=	suspendc	-t
d
@	swapp
o	-d	Do not change the active pane	
o	-D	Swap with the next pane	
o	-U	Swap dst-pane with the previous pane	
o	-Z	Keep the window zoomed if it was zoomed	
o	-s	The source pane	v
o	-t	The destination pane	v
=	swapp	-s
d
=	swapp	-t
d
@	swapw
o	-d	The new window does not become the current window	
o	-s	The source window	v
o	-t	The destination window	v
=	swapw	-s
d
=	swapw	-t
d
@	switchc
o	-E	Do not use update-environment option	
o	-l	Move the client to the last session	
o	-n	Move the client to the next session	
o	-p	Move the client to the previous session	
o	-r	Toggle the client read-only and ignore-size flags	
o	-Z	Keep the window zoomed if it was zoomed	
o	-c	The target client	v
o	-t	Switch the client to the target-session	v
o	-T	Set the client's key table	v
=	switchc	-c
d
=	switchc	-t
d
@	unbind
o	-a	Remove all key-bindings	
o	-n	Alias for -T root	
o	-q	Prevent errors being returned	
o	-T	The key table to use	v
a	1	0
@	unlinkw
o	-k	Destroy the window	
o	-t	The target window	v
=	unlinkw	-t
d
@	wait
o	-L	Lock the channel	
o	-U	Unlock the channel	
a	1	0
