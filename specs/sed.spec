@	
s	a	Appends `text` after a line
s	b	Branch unconditionally to `label`
s	c	Replace (change) lines with `text`
s	d	Delete the pattern space; immediately start next cycle
s	D	If pattern space contains newlines, delete text in the pattern space up to the first newline, and…
s	e	Executes the command that is found in pattern space and replaces the pattern space with the…
s	F	Prints the file name of the current input file
s	g	Replaces the contents of the pattern space with the contents of the hold space
s	G	Appends a newline to the contents of the pattern space, and then appends the contents of the hold…
s	h	Replaces the contents of the hold space with the contents of the pattern space
s	H	Appends a newline to the contents of the hold space, and then appends the contents of the pattern…
s	i	Insert text before a line
s	l	Prints the pattern space in an unambiguous form
s	n	Prints the pattern space, then, regardless, replaces the pattern space with the next line of…
s	N	Adds a newline to the pattern space, then appends the next line of input to the pattern space. If…
s	p	Prints the pattern space
s	P	Prints the pattern space up to the first newline
s	q	Exit sed without processing any more commands or input
s	Q	This command is the same as q, but will not print the contents of pattern space
s	r	Reads file
s	R	Queue a line of filename to be read and inserted into the output stream at the end of the current…
s	s|regexp|replacement	Match the regular-expression against the content of the pattern space. If found, replace matched…
s	t	(test) Branch to label only if there has been a successful substitution since the last input line…
s	T	(test) Branch to label only if there have been no successful substitutions since the last input…
s	v	Makes sed fail if GNU sed extensions are not supported, or if the requested version is not available
s	w	Writes the pattern space to the file
s	W	Writes to the given filename the portion of the pattern space up to the first newline
s	x	Exchanges the contents of the hold and pattern spaces
s	y|src|dst	Transliterate any characters in the pattern space which match any of the source-chars with the…
s	z	(zap) Empties the content of pattern space
s	#	Comment until the next newline
o	-E	Interprets regular expressions as extended (modern) regular expressions rather than basic regular…	
o	-a	Causes sed to delay opening each file until a command containing the related ``w'' function is…	
o	-e	Appends the editing commands specified by the command argument to the list of commands	v
o	-f	Appends the editing commands found in the file command_file to the list of commands. The editing…	v
o	-I	Edits files in-place, saving backups with the specified extension. If a zero-length extension is…	v
o	-i	Edits files in-place similarly to `-I`, but treats each file independently from other files. In…	v
o	-l	Makes output line buffered	
o	-n	By default, each line of input is echoed to the standard output after all of the commands have…	
o	-r	Same as `-E` for compatibility with GNU sed	
o	-u	Makes output unbuffered	
a	2	1
=		-f
t	filepaths
#		2
t	filepaths
@	a
a	1	0
@	b
a	1	0
@	c
a	1	0
@	d
@	D
@	e
a	1	0
@	F
@	g
@	G
@	h
@	H
@	i
a	1	0
@	l
@	n
@	N
@	p
@	P
@	q
a	1	0
@	Q
a	1	0
@	r
a	1	0
#	r	1
t	filepaths
@	R
a	1	0
#	R	1
t	filepaths
@	s
@	t
a	1	0
@	T
a	1	0
@	v
a	1	0
@	w
a	1	0
#	w	1
t	filepaths
@	W
a	1	0
#	W	1
t	filepaths
@	x
@	y
@	z
@	#
