@	
o	-x|--extended	Enables extended-search mode	
o	+x|--no-extended	Disables extended-search mode	
o	-e|--exact	Enables Exact-match	
o	--algo	Fuzzy matching algorithm	v
o	-i	Case-insensitive match (default: smart-case match)	
o	+i	Case-sensitive match (default: smart-case match)	
o	--literal	Do not normalize latin script letters before matching	
o	-n|--nth	Comma-separated list of field index expressions for limiting search scope	v
o	--with-nth	Transform the presentation of each line using field index expressions	v
o	-d|--delimiter	Field delimiter regex (default: AWK-style)	v
o	+s|--no-sort	Do not sort the result	
o	--tac	Reverse the order of the input	
o	--disabled	Do not perform search	
o	--tiebreak	Comma-separated list of sort criteria to apply when the scores are tied	v
o	-m|--multi	Enable multi-select with tab/shift-tab	V
o	--no-mouse	Disable mouse	
o	--bind	Custom key bindings. Refer to the man page	v
o	--cycle	Enable cyclic scroll	
o	--keep-right	Keep the right end of the line visible on overflow	
o	--no-hscroll	Disable horizontal scroll	
o	--hscroll-off	Number of screen columns to keep to the right of the highlighted substring	v
o	--filepath-word	Make word-wise movements respect path separators	
o	--jump-labels	Label characters for jump and jump-accept	v
o	--height	Display fzf window below the cursor with the given height instead of using fullscreen	v
o	--min-height	Minimum height when --height is given in percent	v
o	--layout	Choose layout	v
o	--border	Draw border around the finder	V
o	--margin	Screen margin (TRBL | TB,RL | T,RL,B | T,R,B,L)	v
o	--padding	Padding inside border (TRBL | TB,RL | T,RL,B | T,R,B,L)	v
o	--info	Finder info style	v
o	--prompt	Input prompt	v
o	--pointer	Pointer to the current line	v
o	--marker	Multi-select marker	v
o	--header	String to print as header	v
o	--header-lines	The first N lines of the input are treated as header	v
o	--ansi	Enable processing of ANSI color codes	
o	--tabstop	Number of spaces for a tab character	v
o	--color	Base scheme	v
o	--no-bold	Do not use bold text	
o	--history	History file	v
o	--history-size	Maximum number of history entries	v
o	--preview	Command to preview highlighted line ({})	v
o	--preview-window	Preview window layout	v
o	-q|--query	Start the finder with the given query	v
o	-1|--select-1	Automatically select the only match	
o	-0|--exit-0	Exit immediately when there's no match	
o	-f|--filter	Filter mode. Do not start interactive finder	v
o	--print-query	Print query as the first line	
o	--expect	Comma-separated list of keys to complete fzf	v
o	--read0	Read input delimited by ASCII NUL characters	
o	--print0	Print output delimited by ASCII NUL characters	
o	--sync	Synchronous search for multi-staged filtering	
o	--version	Display version information and exit	
=		--algo
v	v1	
v	v2	
=		--tiebreak
v	length	
v	begin	
v	end	
v	index	
=		--layout
v	default	
v	reverse	
v	reverse-list	
=		--border
v	rounded	
v	sharp	
v	horizontal	
v	vertical	
v	top	
v	bottom	
v	left	
v	right	
v	none	
=		--info
v	default	
v	inline	
v	hidden	
=		--color
v	dark	
v	light	
v	16	
v	bw	
=		--history
t	filepaths
=		--preview-window
v	up	
v	down	
v	left	
v	right	
v	nowrap	
v	wrap	
v	nocycle	
v	cycle	
v	nofollow	
v	follow	
v	nohidden	
v	hidden	
v	default	
