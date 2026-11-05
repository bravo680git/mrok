@	
s	serve	Start ollama
s	create	Create a model from a Modelfile
s	show	Show information for a model
s	run	Run a model
s	stop	Stop the ollama server
s	pull	Pull a model from a registry
s	push	Push a model to a registry
s	list|ls	List models
s	ps	List running models
s	cp	Copy a model
s	rm	Remove a model
s	help	Help about any command
o	--help|-h	Show help for ollama	p
o	--version|-v	Show version information	
@	serve
@	create
o	-f	Specify Modelfile	v
=	create	-f
t	filepaths
@	show
a	1	0
#	show	1
d
@	run
o	--verbose	Enable verbose output	
a	1	0
#	run	1
d
@	stop
a	1	0
#	stop	1
d
@	pull
@	push
@	list
@	ps
@	cp
a	1	0
#	cp	1
d
@	rm
a	1	0
#	rm	1
d
@	help
s	serve	Start ollama
s	create	Create a model from a Modelfile
s	show	Show information for a model
s	run	Run a model
s	stop	Stop the ollama server
s	pull	Pull a model from a registry
s	push	Push a model to a registry
s	list	List models
s	ps	List running models
s	cp	Copy a model
s	rm	Remove a model
@	help serve
@	help create
@	help show
@	help run
@	help stop
@	help pull
@	help push
@	help list
@	help ps
@	help cp
@	help rm
