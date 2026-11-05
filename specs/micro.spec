@	
s	--plugin	Manage plugins
o	--clean	Cleans the configuration directory	
o	--config-dir	Specify a custom location for the configuration directory	v
o	--options	Show all option help	
o	--debug	Enable debug mode	
o	--version	Show the version number and information	
o	--autoindent	When creating a new line, use the same indentation as the previous line	v
o	--autosave	Automatically save the buffer every <n> seconds. If set to 0, no autosaving is performed	v
o	--autosu	Automatically attempt to use super user privileges to save without asking	v
o	--backup	Automatically keep backups of all open buffers	v
o	--backupdir	The directory to place backups in	v
o	--basename	In the infobar and tabbar, show only the basename of the file being edited rather than the full path	v
o	--clipboard	Apecifies how the system clipboard should be accessed	v
o	--colorcolumn	Display a color at the specified column if not set to 0	v
o	--colorscheme	Loads the colorscheme stored in $(configDir)/colorschemes/<scheme>.micro	v
o	--cursorline	Highlight the line that the cursor is on in a different color	v
o	--diffgutter	Display diff indicators before lines	v
o	--divchars	Specifies the divider characters used for the dividing line between vertical/horizontal splits…	v
o	--divreverse	Reverse colors specified by the colorscheme	v
o	--encoding	The encoding to open and save files with	v
o	--eofnewline	Automatically add a newline to the end of the file if one does not exist	v
o	--fastdirty	Use 'fast dirty' algorithm to determine if a buffer is modified or not	v
o	--fileformat	Type of line endings to be used for the file	v
o	--filetype	File type for the current buffer	v
o	--ignorecase	Perform case-insensitive searches	v
o	--incsearch	Enable incremental search in "Find" prompt	v
o	--indentchar	Sets the indentation character	v
o	--infobar	Enables the line at the bottom of the editor where messages are printed	v
o	--keepautoindent	Remove trailing whitespace from a line with no insertions when moving to the next line	v
o	--keymenu	Display the nano-style key menu at the bottom of the screen	v
o	--matchbrace	Underline matching braces for '()', '{}', '[]' when the cursor is on a brace character	v
o	--mkparents	Allow parent directories to be created automatically when opening a file on a path that doesn't…	v
o	--mouse	Enable mouse support	v
o	--paste	Treat characters sent from the terminal in a single chunk as a paste event rather than a series of…	v
o	--parsecursor	Parse filenames such as file.txt:10:5 as requesting to open file.txt with the cursor at line 10…	v
o	--permbackup	Cause backups to be permanently saved	v
o	--pluginchannels	List of URLs pointing to plugin channels for downloading and installing plugins	v
o	--pluginrepos	A list of links to plugin repositories	v
o	--readonly	Disallow edits to the buffer	v
o	--relativeruler	Make line numbers display relatively	v
o	--rmtrailingws	Automatically trim trailing whitespaces at ends of lines	v
o	--ruler	Display line numbers	v
o	--savecursor	Remember where the cursor was last time the file was opened and put it there when re-opened	v
o	--savehistory	Remember command history between closing and re-opening micro	v
o	--saveundo	Remember undo state between closing and re-opening a file	v
o	--scrollbar	Display a scroll bar	v
o	--scrollmargin	Margin at which the view starts scrolling when the cursor approaches the edge of the view	v
o	--scrollspeed	Number of lines to scroll for one scroll event	v
o	--smartpaste	Add leading whitespace when pasting multiple lines	v
o	--softwrap	Wrap lines that are too long to fit on the screen	v
o	--splitbottom	When a horizontal split is created, create it below the current split	v
o	--splitright	When a vertical split is created, create it to the right of the current split	v
o	--statusformatl	Format string definition for the left-justified part of the statusline	v
o	--statusformatr	Format string definition for the right-justified part of the statusline	v
o	--statusline	Display the status line at the bottom of the screen	v
o	--sucmd	The super user command	v
o	--syntax	Enables syntax highlighting	v
o	--tabmovement	Navigate spaces at the beginning of lines as if they are tabs	v
o	--tabsize	The size in spaces that a tab character should be displayed with	v
o	--tabstospaces	Use spaces instead of tabs	v
o	--useprimary	Use the primary clipboard to copy selections in the background	v
o	--wordwrap	Wrap long lines by words	v
o	--xterm	Assume that the terminal conforms to xterm-256color regardless of what the $TERM variable actually…	v
a	1	0
=		--autoindent
v	true	
v	false	
=		--autosave
v	0	
v	60	
v	120	
v	300	
v	600	
v	1800	
=		--autosu
v	true	
v	false	
=		--backup
v	true	
v	false	
=		--backupdir
v	~/.config/micro.backups	
t	folders
=		--basename
v	true	
v	false	
=		--clipboard
v	external	Accesses clipboard via an external tool, such as xclip/xsel or wl-clipboard on Linux…
v	terminal	Accesses the clipboard via your terminal emulator
v	internal	Uses an internal clipboard
=		--colorcolumn
v	0	
v	1	
=		--colorscheme
v	default	
=		--cursorline
v	true	
v	false	
=		--diffgutter
v	true	
v	false	
=		--divchars
v	|-	
=		--divreverse
v	true	
v	false	
=		--encoding
v	utf-8	
=		--eofnewline
v	true	
v	false	
=		--fastdirty
v	true	
v	false	
=		--fileformat
v	unix	
v	dos	
=		--filetype
v	unknown	Automatically overridden depending on type of file opened
v	off	Disable file type detection
=		--ignorecase
v	true	
v	false	
=		--incsearch
v	true	
v	false	
=		--indentchar
v		
v	\t	
=		--infobar
v	true	
v	false	
=		--keepautoindent
v	true	
v	false	
=		--keymenu
v	true	
v	false	
=		--matchbrace
v	true	
v	false	
=		--mkparents
v	true	
v	false	
=		--mouse
v	true	
v	false	
=		--paste
v	true	
v	false	
=		--parsecursor
v	true	
v	false	
=		--permbackup
v	true	
v	false	
=		--pluginchannels
v	https://raw.githubusercontent.com/micro-editor/plugin-channel/master/channel.json	
=		--readonly
v	true	
v	false	
=		--relativeruler
v	true	
v	false	
=		--rmtrailingws
v	true	
v	false	
=		--ruler
v	true	
v	false	
=		--savecursor
v	true	
v	false	
=		--savehistory
v	true	
v	false	
=		--saveundo
v	true	
v	false	
=		--scrollbar
v	true	
v	false	
=		--scrollmargin
v	0	
v	1	
v	2	
v	3	
v	5	
v	10	
=		--scrollspeed
v	1	
v	2	
v	3	
v	4	
v	5	
=		--smartpaste
v	true	
v	false	
=		--softwrap
v	true	
v	false	
=		--splitbottom
v	true	
v	false	
=		--splitright
v	true	
v	false	
=		--statusline
v	true	
v	false	
=		--sucmd
v	sudo	
v	doas	
=		--syntax
v	true	
v	false	
=		--tabmovement
v	true	
v	false	
=		--tabsize
v	2	
v	4	
v	8	
v	16	
=		--tabstospaces
v	true	
v	false	
=		--useprimary
v	true	
v	false	
=		--wordwrap
v	true	
v	false	
=		--xterm
v	true	
v	false	
#		1
t	filepaths
@	--plugin
o	remove	Remove plugin(s)	v
o	update	Update plugin(s) (if no argument is given, updates all plugins)	v
o	search	Search for a plugin	v
o	list	List installed plugins	
o	available	List available plugins	
