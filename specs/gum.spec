@	
s	choose	Choose an option from a list of choices
s	confirm	Ask a user to confirm an action
s	filter	Filter items from a list
s	format	Format a string using a template
s	input	Prompt for some input
s	join	Join text vertically or horizontally
s	spin	Display spinner while running a command
s	style	Apply coloring, borders, spacing to text
s	write	Prompt for long-form text
s	file	Pick a file from a folder
s	table	Render a table of data
s	pager	Scroll through a file
o	--help|-h	Show context-sensitive help	p
o	--version|-v	Print the version number	p
@	choose
o	--height	Height of the list	v
o	--cursor	Prefix to show on item that corresponds to the cursor position	v
o	--cursor-prefix	Prefix to show on the cursor item	v
o	--selected-prefix	Prefix to show on selected items	v
o	--unselected-prefix	Prefix to show on unselected items	v
o	--selected	Options that should start as selected	v
o	--limit	Maximum number of options to pick	v
o	--no-limit	Pick unlimited number of options (ignores limit)	
o	--cursor.background	Background Color for cursor	v
o	--cursor.foreground	Foreground Color for cursor	v
o	--cursor.border	Border Style for cursor	v
o	--cursor.border-background	Border Background Color for cursor	v
o	--cursor.border-foreground	Border Foreground Color for cursor	v
o	--cursor.align	Text Alignment for cursor	v
o	--cursor.height	Text height for cursor	v
o	--cursor.width	Text width for cursor	v
o	--cursor.margin	Text margin for cursor	v
o	--cursor.padding	Text padding for cursor	v
o	--cursor.bold	Bold text for cursor	
o	--cursor.faint	Faint text for cursor	
o	--cursor.italic	Italicize text for cursor	
o	--cursor.strikethrough	Strikethrough text for cursor	
o	--cursor.underline	Underline text for cursor	
o	--item.background	Background Color for item	v
o	--item.foreground	Foreground Color for item	v
o	--item.border	Border Style for item	v
o	--item.border-background	Border Background Color for item	v
o	--item.border-foreground	Border Foreground Color for item	v
o	--item.align	Text Alignment for item	v
o	--item.height	Text height for item	v
o	--item.width	Text width for item	v
o	--item.margin	Text margin for item	v
o	--item.padding	Text padding for item	v
o	--item.bold	Bold text for item	
o	--item.faint	Faint text for item	
o	--item.italic	Italicize text for item	
o	--item.strikethrough	Strikethrough text for item	
o	--item.underline	Underline text for item	
o	--selected.background	Background Color for selected	v
o	--selected.foreground	Foreground Color for selected	v
o	--selected.border	Border Style for selected	v
o	--selected.border-background	Border Background Color for selected	v
o	--selected.border-foreground	Border Foreground Color for selected	v
o	--selected.align	Text Alignment for selected	v
o	--selected.height	Text height for selected	v
o	--selected.width	Text width for selected	v
o	--selected.margin	Text margin for selected	v
o	--selected.padding	Text padding for selected	v
o	--selected.bold	Bold text for selected	
o	--selected.faint	Faint text for selected	
o	--selected.italic	Italicize text for selected	
o	--selected.strikethrough	Strikethrough text for selected	
o	--selected.underline	Underline text for selected	
a	1	1
=	choose	--cursor.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	choose	--cursor.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	choose	--item.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	choose	--item.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	choose	--selected.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	choose	--selected.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	confirm
o	--affirmative	The title of the affirmative action	v
o	--negative	The title of the negative action	v
o	--default	Default confirmation action	
o	--timeout	Timeout for confirmation	v
o	--prompt.background	Background Color for prompt	v
o	--prompt.foreground	Foreground Color for prompt	v
o	--prompt.border	Border Style for prompt	v
o	--prompt.border-background	Border Background Color for prompt	v
o	--prompt.border-foreground	Border Foreground Color for prompt	v
o	--prompt.align	Text Alignment for prompt	v
o	--prompt.height	Text height for prompt	v
o	--prompt.width	Text width for prompt	v
o	--prompt.margin	Text margin for prompt	v
o	--prompt.padding	Text padding for prompt	v
o	--prompt.bold	Bold text for prompt	
o	--prompt.faint	Faint text for prompt	
o	--prompt.italic	Italicize text for prompt	
o	--prompt.strikethrough	Strikethrough text for prompt	
o	--prompt.underline	Underline text for prompt	
o	--selected.background	Background Color for selected	v
o	--selected.foreground	Foreground Color for selected	v
o	--selected.border	Border Style for selected	v
o	--selected.border-background	Border Background Color for selected	v
o	--selected.border-foreground	Border Foreground Color for selected	v
o	--selected.align	Text Alignment for selected	v
o	--selected.height	Text height for selected	v
o	--selected.width	Text width for selected	v
o	--selected.margin	Text margin for selected	v
o	--selected.padding	Text padding for selected	v
o	--selected.bold	Bold text for selected	
o	--selected.faint	Faint text for selected	
o	--selected.italic	Italicize text for selected	
o	--selected.strikethrough	Strikethrough text for selected	
o	--selected.underline	Underline text for selected	
o	--unselected.background	Background Color for unselected	v
o	--unselected.foreground	Foreground Color for unselected	v
o	--unselected.border	Border Style for unselected	v
o	--unselected.border-background	Border Background Color for unselected	v
o	--unselected.border-foreground	Border Foreground Color for unselected	v
o	--unselected.align	Text Alignment for unselected	v
o	--unselected.height	Text height for unselected	v
o	--unselected.width	Text width for unselected	v
o	--unselected.margin	Text margin for unselected	v
o	--unselected.padding	Text padding for unselected	v
o	--unselected.bold	Bold text for unselected	
o	--unselected.faint	Faint text for unselected	
o	--unselected.italic	Italicize text for unselected	
o	--unselected.strikethrough	Strikethrough text for unselected	
o	--unselected.underline	Underline text for unselected	
a	1	0
=	confirm	--prompt.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	confirm	--prompt.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	confirm	--selected.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	confirm	--selected.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	confirm	--unselected.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	confirm	--unselected.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	filter
o	--indicator	Character for selection	v
o	--selected-prefix	Character to indicate selected items	v
o	--unselected-prefix	Character to indicate unselected items	v
o	--placeholder	Placeholder value	v
o	--prompt	Prompt to display	v
o	--width	Input width	v
o	--height	Input height	v
o	--value	Initial filter	v
o	--reverse	Display from the bottom of the screen	
o	--indicator.background	Background Color for indicator	v
o	--indicator.foreground	Foreground Color for indicator	v
o	--indicator.border	Border Style for indicator	v
o	--indicator.border-background	Border Background Color for indicator	v
o	--indicator.border-foreground	Border Foreground Color for indicator	v
o	--indicator.align	Text Alignment for indicator	v
o	--indicator.height	Text height for indicator	v
o	--indicator.width	Text width for indicator	v
o	--indicator.margin	Text margin for indicator	v
o	--indicator.padding	Text padding for indicator	v
o	--indicator.bold	Bold text for indicator	
o	--indicator.faint	Faint text for indicator	
o	--indicator.italic	Italicize text for indicator	
o	--indicator.strikethrough	Strikethrough text for indicator	
o	--indicator.underline	Underline text for indicator	
o	--selected-indicator.background	Background Color for selected-indicator	v
o	--selected-indicator.foreground	Foreground Color for selected-indicator	v
o	--selected-indicator.border	Border Style for selected-indicator	v
o	--selected-indicator.border-background	Border Background Color for selected-indicator	v
o	--selected-indicator.border-foreground	Border Foreground Color for selected-indicator	v
o	--selected-indicator.align	Text Alignment for selected-indicator	v
o	--selected-indicator.height	Text height for selected-indicator	v
o	--selected-indicator.width	Text width for selected-indicator	v
o	--selected-indicator.margin	Text margin for selected-indicator	v
o	--selected-indicator.padding	Text padding for selected-indicator	v
o	--selected-indicator.bold	Bold text for selected-indicator	
o	--selected-indicator.faint	Faint text for selected-indicator	
o	--selected-indicator.italic	Italicize text for selected-indicator	
o	--selected-indicator.strikethrough	Strikethrough text for selected-indicator	
o	--selected-indicator.underline	Underline text for selected-indicator	
o	--unselected-prefix.background	Background Color for unselected-prefix	v
o	--unselected-prefix.foreground	Foreground Color for unselected-prefix	v
o	--unselected-prefix.border	Border Style for unselected-prefix	v
o	--unselected-prefix.border-background	Border Background Color for unselected-prefix	v
o	--unselected-prefix.border-foreground	Border Foreground Color for unselected-prefix	v
o	--unselected-prefix.align	Text Alignment for unselected-prefix	v
o	--unselected-prefix.height	Text height for unselected-prefix	v
o	--unselected-prefix.width	Text width for unselected-prefix	v
o	--unselected-prefix.margin	Text margin for unselected-prefix	v
o	--unselected-prefix.padding	Text padding for unselected-prefix	v
o	--unselected-prefix.bold	Bold text for unselected-prefix	
o	--unselected-prefix.faint	Faint text for unselected-prefix	
o	--unselected-prefix.italic	Italicize text for unselected-prefix	
o	--unselected-prefix.strikethrough	Strikethrough text for unselected-prefix	
o	--unselected-prefix.underline	Underline text for unselected-prefix	
o	--text.background	Background Color for text	v
o	--text.foreground	Foreground Color for text	v
o	--text.border	Border Style for text	v
o	--text.border-background	Border Background Color for text	v
o	--text.border-foreground	Border Foreground Color for text	v
o	--text.align	Text Alignment for text	v
o	--text.height	Text height for text	v
o	--text.width	Text width for text	v
o	--text.margin	Text margin for text	v
o	--text.padding	Text padding for text	v
o	--text.bold	Bold text for text	
o	--text.faint	Faint text for text	
o	--text.italic	Italicize text for text	
o	--text.strikethrough	Strikethrough text for text	
o	--text.underline	Underline text for text	
o	--match.background	Background Color for match	v
o	--match.foreground	Foreground Color for match	v
o	--match.border	Border Style for match	v
o	--match.border-background	Border Background Color for match	v
o	--match.border-foreground	Border Foreground Color for match	v
o	--match.align	Text Alignment for match	v
o	--match.height	Text height for match	v
o	--match.width	Text width for match	v
o	--match.margin	Text margin for match	v
o	--match.padding	Text padding for match	v
o	--match.bold	Bold text for match	
o	--match.faint	Faint text for match	
o	--match.italic	Italicize text for match	
o	--match.strikethrough	Strikethrough text for match	
o	--match.underline	Underline text for match	
o	--prompt.background	Background Color for prompt	v
o	--prompt.foreground	Foreground Color for prompt	v
o	--prompt.border	Border Style for prompt	v
o	--prompt.border-background	Border Background Color for prompt	v
o	--prompt.border-foreground	Border Foreground Color for prompt	v
o	--prompt.align	Text Alignment for prompt	v
o	--prompt.height	Text height for prompt	v
o	--prompt.width	Text width for prompt	v
o	--prompt.margin	Text margin for prompt	v
o	--prompt.padding	Text padding for prompt	v
o	--prompt.bold	Bold text for prompt	
o	--prompt.faint	Faint text for prompt	
o	--prompt.italic	Italicize text for prompt	
o	--prompt.strikethrough	Strikethrough text for prompt	
o	--prompt.underline	Underline text for prompt	
=	filter	--indicator.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	filter	--indicator.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	filter	--selected-indicator.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	filter	--selected-indicator.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	filter	--unselected-prefix.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	filter	--unselected-prefix.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	filter	--text.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	filter	--text.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	filter	--match.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	filter	--match.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	filter	--prompt.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	filter	--prompt.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	format
o	--type|-t	Format to use	v
a	1	1
=	format	--type
v	markdown	
v	template	
v	code	
v	emoji	
@	input
o	--placeholder	Placeholder value	v
o	--prompt	Prompt to display	v
o	--value	Initial value	v
o	--char-limit	Maximum value length	v
o	--width	Input width	v
o	--password	Mask input characters	
o	--prompt.background	Background Color for prompt	v
o	--prompt.foreground	Foreground Color for prompt	v
o	--prompt.border	Border Style for prompt	v
o	--prompt.border-background	Border Background Color for prompt	v
o	--prompt.border-foreground	Border Foreground Color for prompt	v
o	--prompt.align	Text Alignment for prompt	v
o	--prompt.height	Text height for prompt	v
o	--prompt.width	Text width for prompt	v
o	--prompt.margin	Text margin for prompt	v
o	--prompt.padding	Text padding for prompt	v
o	--prompt.bold	Bold text for prompt	
o	--prompt.faint	Faint text for prompt	
o	--prompt.italic	Italicize text for prompt	
o	--prompt.strikethrough	Strikethrough text for prompt	
o	--prompt.underline	Underline text for prompt	
o	--cursor.background	Background Color for cursor	v
o	--cursor.foreground	Foreground Color for cursor	v
o	--cursor.border	Border Style for cursor	v
o	--cursor.border-background	Border Background Color for cursor	v
o	--cursor.border-foreground	Border Foreground Color for cursor	v
o	--cursor.align	Text Alignment for cursor	v
o	--cursor.height	Text height for cursor	v
o	--cursor.width	Text width for cursor	v
o	--cursor.margin	Text margin for cursor	v
o	--cursor.padding	Text padding for cursor	v
o	--cursor.bold	Bold text for cursor	
o	--cursor.faint	Faint text for cursor	
o	--cursor.italic	Italicize text for cursor	
o	--cursor.strikethrough	Strikethrough text for cursor	
o	--cursor.underline	Underline text for cursor	
=	input	--prompt.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	input	--prompt.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	input	--cursor.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	input	--cursor.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	join
o	--align	Text alignment	v
o	--horizontal	Join (potentially multi-line) strings horizontally	
o	--vertical	Join (potentially multi-line) strings vertically	
a	1	1
=	join	--align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	spin
o	--show-output	Show output of command	
o	--spinner|-s	Spinner type	v
o	--title	Text to display to user while spinning	v
o	--align|-a	Alignment of spinner with regard to the title	v
o	--spinner.background	Background Color for spinner	v
o	--spinner.foreground	Foreground Color for spinner	v
o	--spinner.border	Border Style for spinner	v
o	--spinner.border-background	Border Background Color for spinner	v
o	--spinner.border-foreground	Border Foreground Color for spinner	v
o	--spinner.align	Text Alignment for spinner	v
o	--spinner.height	Text height for spinner	v
o	--spinner.width	Text width for spinner	v
o	--spinner.margin	Text margin for spinner	v
o	--spinner.padding	Text padding for spinner	v
o	--spinner.bold	Bold text for spinner	
o	--spinner.faint	Faint text for spinner	
o	--spinner.italic	Italicize text for spinner	
o	--spinner.strikethrough	Strikethrough text for spinner	
o	--spinner.underline	Underline text for spinner	
o	--title.background	Background Color for title	v
o	--title.foreground	Foreground Color for title	v
o	--title.border	Border Style for title	v
o	--title.border-background	Border Background Color for title	v
o	--title.border-foreground	Border Foreground Color for title	v
o	--title.align	Text Alignment for title	v
o	--title.height	Text height for title	v
o	--title.width	Text width for title	v
o	--title.margin	Text margin for title	v
o	--title.padding	Text padding for title	v
o	--title.bold	Bold text for title	
o	--title.faint	Faint text for title	
o	--title.italic	Italicize text for title	
o	--title.strikethrough	Strikethrough text for title	
o	--title.underline	Underline text for title	
=	spin	--spinner
v	line	
v	dot	
v	minidot	
v	jump	
v	pulse	
v	points	
v	globe	
v	moon	
v	monkey	
v	meter	
v	hamburger	
=	spin	--align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	spin	--spinner.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	spin	--spinner.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	spin	--title.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	spin	--title.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	style
o	--background	Background Color	v
o	--foreground	Foreground Color	v
o	--border	Border Style	v
o	--border-background	Border Background Color	v
o	--border-foreground	Border Foreground Color	v
o	--align	Text Alignment	v
o	--height	Text height	v
o	--width	Text width	v
o	--margin	Text margin	v
o	--padding	Text padding	v
o	--bold	Bold text	
o	--faint	Faint text	
o	--italic	Italicize text	
o	--strikethrough	Strikethrough text	
o	--underline	Underline text	
a	1	1
=	style	--border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	style	--align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	write
o	--width	Text area width	v
o	--height	Text area height	v
o	--placeholder	Placeholder value	v
o	--prompt	Prompt to display	v
o	--show-cursor-line	Show cursor line	
o	--show-line-numbers	Show line numbers	
o	--value	Initial value (can be passed via stdin)	v
o	--char-limit	Maximum value length (0 for no limit)	v
o	--header	Header value	v
o	--base.background	Background Color for base	v
o	--base.foreground	Foreground Color for base	v
o	--base.border	Border Style for base	v
o	--base.border-background	Border Background Color for base	v
o	--base.border-foreground	Border Foreground Color for base	v
o	--base.align	Text Alignment for base	v
o	--base.height	Text height for base	v
o	--base.width	Text width for base	v
o	--base.margin	Text margin for base	v
o	--base.padding	Text padding for base	v
o	--base.bold	Bold text for base	
o	--base.faint	Faint text for base	
o	--base.italic	Italicize text for base	
o	--base.strikethrough	Strikethrough text for base	
o	--base.underline	Underline text for base	
o	--cursor-line-number.background	Background Color for cursor-line-number	v
o	--cursor-line-number.foreground	Foreground Color for cursor-line-number	v
o	--cursor-line-number.border	Border Style for cursor-line-number	v
o	--cursor-line-number.border-background	Border Background Color for cursor-line-number	v
o	--cursor-line-number.border-foreground	Border Foreground Color for cursor-line-number	v
o	--cursor-line-number.align	Text Alignment for cursor-line-number	v
o	--cursor-line-number.height	Text height for cursor-line-number	v
o	--cursor-line-number.width	Text width for cursor-line-number	v
o	--cursor-line-number.margin	Text margin for cursor-line-number	v
o	--cursor-line-number.padding	Text padding for cursor-line-number	v
o	--cursor-line-number.bold	Bold text for cursor-line-number	
o	--cursor-line-number.faint	Faint text for cursor-line-number	
o	--cursor-line-number.italic	Italicize text for cursor-line-number	
o	--cursor-line-number.strikethrough	Strikethrough text for cursor-line-number	
o	--cursor-line-number.underline	Underline text for cursor-line-number	
o	--cursor-line.background	Background Color for cursor-line	v
o	--cursor-line.foreground	Foreground Color for cursor-line	v
o	--cursor-line.border	Border Style for cursor-line	v
o	--cursor-line.border-background	Border Background Color for cursor-line	v
o	--cursor-line.border-foreground	Border Foreground Color for cursor-line	v
o	--cursor-line.align	Text Alignment for cursor-line	v
o	--cursor-line.height	Text height for cursor-line	v
o	--cursor-line.width	Text width for cursor-line	v
o	--cursor-line.margin	Text margin for cursor-line	v
o	--cursor-line.padding	Text padding for cursor-line	v
o	--cursor-line.bold	Bold text for cursor-line	
o	--cursor-line.faint	Faint text for cursor-line	
o	--cursor-line.italic	Italicize text for cursor-line	
o	--cursor-line.strikethrough	Strikethrough text for cursor-line	
o	--cursor-line.underline	Underline text for cursor-line	
o	--cursor.background	Background Color for cursor	v
o	--cursor.foreground	Foreground Color for cursor	v
o	--cursor.border	Border Style for cursor	v
o	--cursor.border-background	Border Background Color for cursor	v
o	--cursor.border-foreground	Border Foreground Color for cursor	v
o	--cursor.align	Text Alignment for cursor	v
o	--cursor.height	Text height for cursor	v
o	--cursor.width	Text width for cursor	v
o	--cursor.margin	Text margin for cursor	v
o	--cursor.padding	Text padding for cursor	v
o	--cursor.bold	Bold text for cursor	
o	--cursor.faint	Faint text for cursor	
o	--cursor.italic	Italicize text for cursor	
o	--cursor.strikethrough	Strikethrough text for cursor	
o	--cursor.underline	Underline text for cursor	
o	--end-of-buffer.background	Background Color for end-of-buffer	v
o	--end-of-buffer.foreground	Foreground Color for end-of-buffer	v
o	--end-of-buffer.border	Border Style for end-of-buffer	v
o	--end-of-buffer.border-background	Border Background Color for end-of-buffer	v
o	--end-of-buffer.border-foreground	Border Foreground Color for end-of-buffer	v
o	--end-of-buffer.align	Text Alignment for end-of-buffer	v
o	--end-of-buffer.height	Text height for end-of-buffer	v
o	--end-of-buffer.width	Text width for end-of-buffer	v
o	--end-of-buffer.margin	Text margin for end-of-buffer	v
o	--end-of-buffer.padding	Text padding for end-of-buffer	v
o	--end-of-buffer.bold	Bold text for end-of-buffer	
o	--end-of-buffer.faint	Faint text for end-of-buffer	
o	--end-of-buffer.italic	Italicize text for end-of-buffer	
o	--end-of-buffer.strikethrough	Strikethrough text for end-of-buffer	
o	--end-of-buffer.underline	Underline text for end-of-buffer	
o	--line-number.background	Background Color for line-number	v
o	--line-number.foreground	Foreground Color for line-number	v
o	--line-number.border	Border Style for line-number	v
o	--line-number.border-background	Border Background Color for line-number	v
o	--line-number.border-foreground	Border Foreground Color for line-number	v
o	--line-number.align	Text Alignment for line-number	v
o	--line-number.height	Text height for line-number	v
o	--line-number.width	Text width for line-number	v
o	--line-number.margin	Text margin for line-number	v
o	--line-number.padding	Text padding for line-number	v
o	--line-number.bold	Bold text for line-number	
o	--line-number.faint	Faint text for line-number	
o	--line-number.italic	Italicize text for line-number	
o	--line-number.strikethrough	Strikethrough text for line-number	
o	--line-number.underline	Underline text for line-number	
o	--placeholder.background	Background Color for placeholder	v
o	--placeholder.foreground	Foreground Color for placeholder	v
o	--placeholder.border	Border Style for placeholder	v
o	--placeholder.border-background	Border Background Color for placeholder	v
o	--placeholder.border-foreground	Border Foreground Color for placeholder	v
o	--placeholder.align	Text Alignment for placeholder	v
o	--placeholder.height	Text height for placeholder	v
o	--placeholder.width	Text width for placeholder	v
o	--placeholder.margin	Text margin for placeholder	v
o	--placeholder.padding	Text padding for placeholder	v
o	--placeholder.bold	Bold text for placeholder	
o	--placeholder.faint	Faint text for placeholder	
o	--placeholder.italic	Italicize text for placeholder	
o	--placeholder.strikethrough	Strikethrough text for placeholder	
o	--placeholder.underline	Underline text for placeholder	
o	--prompt.background	Background Color for prompt	v
o	--prompt.foreground	Foreground Color for prompt	v
o	--prompt.border	Border Style for prompt	v
o	--prompt.border-background	Border Background Color for prompt	v
o	--prompt.border-foreground	Border Foreground Color for prompt	v
o	--prompt.align	Text Alignment for prompt	v
o	--prompt.height	Text height for prompt	v
o	--prompt.width	Text width for prompt	v
o	--prompt.margin	Text margin for prompt	v
o	--prompt.padding	Text padding for prompt	v
o	--prompt.bold	Bold text for prompt	
o	--prompt.faint	Faint text for prompt	
o	--prompt.italic	Italicize text for prompt	
o	--prompt.strikethrough	Strikethrough text for prompt	
o	--prompt.underline	Underline text for prompt	
=	write	--base.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	write	--base.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	write	--cursor-line-number.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	write	--cursor-line-number.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	write	--cursor-line.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	write	--cursor-line.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	write	--cursor.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	write	--cursor.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	write	--end-of-buffer.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	write	--end-of-buffer.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	write	--line-number.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	write	--line-number.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	write	--placeholder.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	write	--placeholder.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	write	--prompt.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	write	--prompt.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	file
o	--cursor|-c	The cursor character	v
o	--all|-a	Show hidden and 'dot' files	
o	--height	Maximum number of files to display	v
o	--cursor.background	Background Color for cursor	v
o	--cursor.foreground	Foreground Color for cursor	v
o	--cursor.border	Border Style for cursor	v
o	--cursor.border-background	Border Background Color for cursor	v
o	--cursor.border-foreground	Border Foreground Color for cursor	v
o	--cursor.align	Text Alignment for cursor	v
o	--cursor.height	Text height for cursor	v
o	--cursor.width	Text width for cursor	v
o	--cursor.margin	Text margin for cursor	v
o	--cursor.padding	Text padding for cursor	v
o	--cursor.bold	Bold text for cursor	
o	--cursor.faint	Faint text for cursor	
o	--cursor.italic	Italicize text for cursor	
o	--cursor.strikethrough	Strikethrough text for cursor	
o	--cursor.underline	Underline text for cursor	
o	--symlink.background	Background Color for symlink	v
o	--symlink.foreground	Foreground Color for symlink	v
o	--symlink.border	Border Style for symlink	v
o	--symlink.border-background	Border Background Color for symlink	v
o	--symlink.border-foreground	Border Foreground Color for symlink	v
o	--symlink.align	Text Alignment for symlink	v
o	--symlink.height	Text height for symlink	v
o	--symlink.width	Text width for symlink	v
o	--symlink.margin	Text margin for symlink	v
o	--symlink.padding	Text padding for symlink	v
o	--symlink.bold	Bold text for symlink	
o	--symlink.faint	Faint text for symlink	
o	--symlink.italic	Italicize text for symlink	
o	--symlink.strikethrough	Strikethrough text for symlink	
o	--symlink.underline	Underline text for symlink	
o	--directory.background	Background Color for directory	v
o	--directory.foreground	Foreground Color for directory	v
o	--directory.border	Border Style for directory	v
o	--directory.border-background	Border Background Color for directory	v
o	--directory.border-foreground	Border Foreground Color for directory	v
o	--directory.align	Text Alignment for directory	v
o	--directory.height	Text height for directory	v
o	--directory.width	Text width for directory	v
o	--directory.margin	Text margin for directory	v
o	--directory.padding	Text padding for directory	v
o	--directory.bold	Bold text for directory	
o	--directory.faint	Faint text for directory	
o	--directory.italic	Italicize text for directory	
o	--directory.strikethrough	Strikethrough text for directory	
o	--directory.underline	Underline text for directory	
o	--file.background	Background Color for file	v
o	--file.foreground	Foreground Color for file	v
o	--file.border	Border Style for file	v
o	--file.border-background	Border Background Color for file	v
o	--file.border-foreground	Border Foreground Color for file	v
o	--file.align	Text Alignment for file	v
o	--file.height	Text height for file	v
o	--file.width	Text width for file	v
o	--file.margin	Text margin for file	v
o	--file.padding	Text padding for file	v
o	--file.bold	Bold text for file	
o	--file.faint	Faint text for file	
o	--file.italic	Italicize text for file	
o	--file.strikethrough	Strikethrough text for file	
o	--file.underline	Underline text for file	
o	--permissions.background	Background Color for permissions	v
o	--permissions.foreground	Foreground Color for permissions	v
o	--permissions.border	Border Style for permissions	v
o	--permissions.border-background	Border Background Color for permissions	v
o	--permissions.border-foreground	Border Foreground Color for permissions	v
o	--permissions.align	Text Alignment for permissions	v
o	--permissions.height	Text height for permissions	v
o	--permissions.width	Text width for permissions	v
o	--permissions.margin	Text margin for permissions	v
o	--permissions.padding	Text padding for permissions	v
o	--permissions.bold	Bold text for permissions	
o	--permissions.faint	Faint text for permissions	
o	--permissions.italic	Italicize text for permissions	
o	--permissions.strikethrough	Strikethrough text for permissions	
o	--permissions.underline	Underline text for permissions	
o	--selected.background	Background Color for selected	v
o	--selected.foreground	Foreground Color for selected	v
o	--selected.border	Border Style for selected	v
o	--selected.border-background	Border Background Color for selected	v
o	--selected.border-foreground	Border Foreground Color for selected	v
o	--selected.align	Text Alignment for selected	v
o	--selected.height	Text height for selected	v
o	--selected.width	Text width for selected	v
o	--selected.margin	Text margin for selected	v
o	--selected.padding	Text padding for selected	v
o	--selected.bold	Bold text for selected	
o	--selected.faint	Faint text for selected	
o	--selected.italic	Italicize text for selected	
o	--selected.strikethrough	Strikethrough text for selected	
o	--selected.underline	Underline text for selected	
o	--file-size.background	Background Color for file-size	v
o	--file-size.foreground	Foreground Color for file-size	v
o	--file-size.border	Border Style for file-size	v
o	--file-size.border-background	Border Background Color for file-size	v
o	--file-size.border-foreground	Border Foreground Color for file-size	v
o	--file-size.align	Text Alignment for file-size	v
o	--file-size.height	Text height for file-size	v
o	--file-size.width	Text width for file-size	v
o	--file-size.margin	Text margin for file-size	v
o	--file-size.padding	Text padding for file-size	v
o	--file-size.bold	Bold text for file-size	
o	--file-size.faint	Faint text for file-size	
o	--file-size.italic	Italicize text for file-size	
o	--file-size.strikethrough	Strikethrough text for file-size	
o	--file-size.underline	Underline text for file-size	
a	1	0
=	file	--cursor.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	file	--cursor.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	file	--symlink.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	file	--symlink.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	file	--directory.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	file	--directory.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	file	--file.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	file	--file.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	file	--permissions.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	file	--permissions.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	file	--selected.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	file	--selected.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	file	--file-size.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	file	--file-size.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	table
o	--separator|-s	Row separator	v
o	--columns|-c	Column names	v
o	--widths|-w	Column widths	v
o	--height	Table height	v
o	--file|-f	File path	v
o	--cell.background	Background Color for cell	v
o	--cell.foreground	Foreground Color for cell	v
o	--cell.border	Border Style for cell	v
o	--cell.border-background	Border Background Color for cell	v
o	--cell.border-foreground	Border Foreground Color for cell	v
o	--cell.align	Text Alignment for cell	v
o	--cell.height	Text height for cell	v
o	--cell.width	Text width for cell	v
o	--cell.margin	Text margin for cell	v
o	--cell.padding	Text padding for cell	v
o	--cell.bold	Bold text for cell	
o	--cell.faint	Faint text for cell	
o	--cell.italic	Italicize text for cell	
o	--cell.strikethrough	Strikethrough text for cell	
o	--cell.underline	Underline text for cell	
o	--header.background	Background Color for header	v
o	--header.foreground	Foreground Color for header	v
o	--header.border	Border Style for header	v
o	--header.border-background	Border Background Color for header	v
o	--header.border-foreground	Border Foreground Color for header	v
o	--header.align	Text Alignment for header	v
o	--header.height	Text height for header	v
o	--header.width	Text width for header	v
o	--header.margin	Text margin for header	v
o	--header.padding	Text padding for header	v
o	--header.bold	Bold text for header	
o	--header.faint	Faint text for header	
o	--header.italic	Italicize text for header	
o	--header.strikethrough	Strikethrough text for header	
o	--header.underline	Underline text for header	
o	--selected.background	Background Color for selected	v
o	--selected.foreground	Foreground Color for selected	v
o	--selected.border	Border Style for selected	v
o	--selected.border-background	Border Background Color for selected	v
o	--selected.border-foreground	Border Foreground Color for selected	v
o	--selected.align	Text Alignment for selected	v
o	--selected.height	Text height for selected	v
o	--selected.width	Text width for selected	v
o	--selected.margin	Text margin for selected	v
o	--selected.padding	Text padding for selected	v
o	--selected.bold	Bold text for selected	
o	--selected.faint	Faint text for selected	
o	--selected.italic	Italicize text for selected	
o	--selected.strikethrough	Strikethrough text for selected	
o	--selected.underline	Underline text for selected	
=	table	--cell.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	table	--cell.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	table	--header.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	table	--header.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	table	--selected.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	table	--selected.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
@	pager
o	--show-line-numbers	Show line numbers	
o	--background	Background Color	v
o	--foreground	Foreground Color	v
o	--border	Border Style	v
o	--border-background	Border Background Color	v
o	--border-foreground	Border Foreground Color	v
o	--align	Text Alignment	v
o	--height	Text height	v
o	--width	Text width	v
o	--margin	Text margin	v
o	--padding	Text padding	v
o	--bold	Bold text	
o	--faint	Faint text	
o	--italic	Italicize text	
o	--strikethrough	Strikethrough text	
o	--underline	Underline text	
o	--help.background	Background Color for help	v
o	--help.foreground	Foreground Color for help	v
o	--help.border	Border Style for help	v
o	--help.border-background	Border Background Color for help	v
o	--help.border-foreground	Border Foreground Color for help	v
o	--help.align	Text Alignment for help	v
o	--help.height	Text height for help	v
o	--help.width	Text width for help	v
o	--help.margin	Text margin for help	v
o	--help.padding	Text padding for help	v
o	--help.bold	Bold text for help	
o	--help.faint	Faint text for help	
o	--help.italic	Italicize text for help	
o	--help.strikethrough	Strikethrough text for help	
o	--help.underline	Underline text for help	
o	--line-number.background	Background Color for line-number	v
o	--line-number.foreground	Foreground Color for line-number	v
o	--line-number.border	Border Style for line-number	v
o	--line-number.border-background	Border Background Color for line-number	v
o	--line-number.border-foreground	Border Foreground Color for line-number	v
o	--line-number.align	Text Alignment for line-number	v
o	--line-number.height	Text height for line-number	v
o	--line-number.width	Text width for line-number	v
o	--line-number.margin	Text margin for line-number	v
o	--line-number.padding	Text padding for line-number	v
o	--line-number.bold	Bold text for line-number	
o	--line-number.faint	Faint text for line-number	
o	--line-number.italic	Italicize text for line-number	
o	--line-number.strikethrough	Strikethrough text for line-number	
o	--line-number.underline	Underline text for line-number	
a	1	0
=	pager	--border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	pager	--align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	pager	--help.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	pager	--help.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
=	pager	--line-number.border
v	none	
v	hidden	
v	normal	
v	rounded	
v	thick	
v	double	
=	pager	--line-number.align
v	left	
v	center	
v	right	
v	bottom	
v	middle	
v	top	
