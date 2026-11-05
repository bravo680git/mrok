@	
s	new	Create a new Angular app
s	generate	Generate new files
s	version	View your Angular CLI version (update for Angular 14+)
o	--version	View your Angular CLI version	
@	new
o	--create-application	Create a default application?	v
a	1	0
=	new	--create-application
v	true	
v	false	
@	generate
s	application	Generates a new application
s	component	Generate a new component
s	library	Generates a new library
s	class	Generates a class
a	1	0
@	generate application
o	--style		v
a	1	0
=	generate application	--style
v	css	
v	scss	
v	sass	
v	less	
v	styl	
@	generate component
o	--project	Project name	v
o	--change-detection|-c	The change detection strategy to use	v
o	--display-block|-b	Add :host block to styles	v
o	--flat	Create at the top level	v
a	1	0
=	generate component	--project
d
=	generate component	--change-detection
v	Default	
v	OnPush	
=	generate component	--display-block
v	true	
v	false	
=	generate component	--flat
v	true	
v	false	
@	generate library
a	1	0
@	generate class
o	--project	Project name	v
a	1	0
=	generate class	--project
d
@	version
