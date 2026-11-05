@	
s	run	Run a shortcut
s	list	List your shortcuts
s	view	View a shortcut in Shortcuts
s	sign	Sign a shortcut file
s	help	Show help information
@	run
o	-i|--input-path	The input to provide to the shortcut	v
o	-o|--output-path	Where to write the shortcut output, if applicable	v
o	--output-type	What type to output data in, in Universal Type Identifier format	v
a	1	0
=	run	-i
t	filepaths
=	run	-o
t	filepaths
=	run	--output-type
v	public.json	JavaScript Object Notation (JSON)
v	public.plain-text	Plain text
v	public.html	HTML
v	public.xml	XML
v	com.adobe.pdf	Adobe PDF
v	public.vcard	VCard
#	run	1
d
@	list
o	--folder-name|-f	The name of the folder to list	v
o	--folders	List folders instead of shortcuts	
=	list	--folder-name
d
@	view
a	1	0
#	view	1
d
@	sign
o	--input|-i	The shortcut file to sign	v
o	--output|-o	Output path for the signed shortcut file	v
o	--mode|-m	The signing mode. (default: people-who-know-me)	v
=	sign	--input
d
=	sign	--output
t	filepaths
=	sign	--mode
v	people-who-know-me	
v	anyone	
@	help
s	run	Run a shortcut
s	list	List your shortcuts
s	view	View a shortcut in Shortcuts
s	sign	Sign a shortcut file
@	help run
@	help list
@	help view
@	help sign
