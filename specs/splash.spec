@	
s	settings	Manage settings
s	aliases	Manage aliases
s	collection	Manage collections
s	dir	Manage SplashCLI download directory
s	user	
o	--help|-h	Help Message	
o	--version|-v	Prints `splash-cli` version	
o	--scale	Scale of the image	v
o	--screen	Set wallpaper on selected screen	v
o	-s|--save	Save photo without setting as wallpaper	V
o	--set	Set wallpaper from local file	v
o	-i|--info	Show image exif data	
o	-q|--quiet	Hide output	
o	--rotate	Rotate image	v
o	--colorspace	Define image colorspace	v
o	--flip	Flip image on the Y axis	
o	-f|--featured	Limit to only featured photos	
o	--query	Filter by keywords	v
o	--orientation	Filter by orientation	v
o	-c|--curated	Random Curated photo	
o	-u|--user	Random photo from user	v
o	--collection	Random photo from collection	v
o	--id	Get photo by ID	v
o	--day	Photo of the day	
=		--scale
v	auto	
v	fill	
v	fit	
v	stretch	
v	center	
=		--screen
v	all	
v	main	
=		-s
t	folders
=		--set
t	filepaths
=		--rotate
v	90	
v	180	
v	270	
=		--colorspace
v	srgb	
v	rgb	
v	cmyk	
v	lab	
v	b-w	
=		--orientation
v	landscape	
v	portrait	
v	squarish	
@	settings
s	get	
s	set	Setup the configuration
s	restore	Restore default settings
@	settings get
a	1	0
@	settings set
@	settings restore
@	aliases
s	get	Get an alias
s	set	Set an alias
s	help	Show help menu
@	aliases get
a	1	0
@	aliases set
a	2	0
@	aliases help
@	collection
s	get	Get a collection
s	delete	Delete a collection
s	create	Create a collection
s	photos:add	Add photos to a collection
s	photos:remove	Remove photos to a collection
s	help	Show help for this command
@	collection get
a	1	0
@	collection delete
a	1	0
@	collection create
@	collection photos:add
@	collection photos:remove
@	collection help
@	dir
s	get	Get the download directory path
s	set	Set the download directory path
s	clean	Delete all the downloaded photos
s	count	Count all the downloaded photos
s	help	Show help for this command
@	dir get
@	dir set
a	1	0
@	dir clean
@	dir count
@	dir help
@	user
s	login	Login with your Unsplash account
s	logout	Removes all user data
s	liked	List last 10 liked photos
s	collections	List all user's collections
s	get	Get user infos
s	edit|update	Update user infos
s	help	Help Menu
@	user login
@	user logout
@	user liked
@	user collections
@	user get
@	user edit
@	user help
