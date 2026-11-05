@	
s	init	Initialise cli
s	clear	Clear the files stored locally
s	send	Send mail
s	template	Manage templates
o	-v|--version	Output cli version	
o	-h|--help	Output cli help	
@	init
o	-h|--help	Get help regarding init command	
a	1	0
#	init	1
t	filepaths
@	clear
o	-h|--help	Get help regarding clear command	
o	-j|--justdoit	Clear entire cli storage including token	
@	send
o	-h|--help	Get help regarding send command	
o	-r|--receiver	Receiver's email address	v
o	-sub|--subject	Subject of mail	v
o	-t|--template	Templates for mail body	V
o	-b|--body	Body of the mail	V
o	-a|--attachment	Path to attachment file	V
o	-l|--lessgo	Skip confirmation, and send mail	
=	send	-t
d
=	send	-a
t	filepaths
@	template
s	add	Add a new template
s	listall	List all templates stored
s	edit	Edit any particular template
o	-h|--help	Get help regarding template command	
@	template add
o	-h|--help	Get help regarding template add subcommand	
o	-n	Set template id	v
@	template listall
o	-h|--help	Get help regarding template listall subcommand	
@	template edit
o	-h|--help	Get help regarding template edit subcommand	
o	-n	Edit template by id	v
=	template edit	-n
d
