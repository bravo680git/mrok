@	
o	--help|-h	Show help for dust	
o	--version|-V	Print version information	
o	--no-percent-bars|-b	No percent bars or percentages will be displayed	
o	--no-colors|-c	No colors will be printed (Useful for commands like: watch)	
o	--depth|-d	Depth to show	v
o	--filter|-e	Only include filepaths matching this regex. For png files type: -e "\.png$"	v
o	--filecount|-f	Directory 'size' is number of child files/dirs not disk size	
o	--si|-H	Print sizes in powers of 1000 (e.g., 1.1G)	
o	--ignore_hidden|-i	Do not display hidden files	
o	--number-of-lines|-n	Number of lines of output to show. (Default is terminal_height - 10)	v
o	--full-paths|-p	Subdirectories will not have their path shortened	
o	--reverse|-r	Print tree upside down (biggest highest)	
o	--apparent-size|-s	Use file length instead of blocks	
o	--skip-total	No total row will be displayed	
o	--file_types|-t	Show only these file types	
o	--invert-filter|-v	Exclude filepaths matching this regex. To ignore png files type: -v "\.png$"	v
o	--terminal_width|-w	Specify width of output overriding the auto detection of terminal width	v
o	--limit-filesystem|-x	Only count the files and directories on the same filesystem as the supplied directory	
o	--ignore-directory|-X	Exclude any file or directory with this name	v
o	--min-size|-z	Minimum size file to include in output	v
a	1	0
=		--ignore-directory
t	folders
#		1
t	filepaths,folders
