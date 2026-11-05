@	
s	login	Log in to LastPass
s	logout	Log out of LastPass
s	ls	List names in groups in a tree structure
s	passwd	Change LastPass password and reencrypt all entries
s	show	Show password or selected field
s	mv	Move LastPass entry to a different group
s	add	Add a new entry
s	edit	Edit existing entry
s	generate	Create randomly generated password
s	duplicate	Duplicate existing entry
s	rm	Removes existing entry
s	status	Show the LastPass login status
s	sync	Sync the local cache against the LastPass server
s	import	Import account information from an unencrypted CSV
s	export	Export account information to an unencrypted CSV
s	share	LastPass Sharing Center functionality
o	--help|-h	Display the help for lpass	
o	--version	Display the version of lpass	
@	login
o	--trust	Subsequent logins will not require multifactor authentication	
o	--plaintext-key	Save decryption key to the hard disk in plaintext	V
o	--color	Control colored output to the terminal	V
a	1	0
=	login	--color
v	auto	
v	never	
v	always	
@	logout
o	--force	Skip user confirmation	
@	ls
o	--color	Control colored output to the terminal	V=
o	--long|-l	Show the last modification time	
o	-m	Show the last modified time	
o	-u	Show the last used time	
a	1	0
=	ls	--color
v	auto	
v	never	
v	always	
@	passwd
@	show
o	--sync	When the current operation syncs to server	V=
o	--clip|-c	Copy to the clipboard	
o	--quiet|-q	Display no output and only sets return code	
o	--expand-multi|-x	Show information from all matching sites	
o	--json|-j	Generate json output instead of human-readable text	
o	--all	Show all fields	
o	--username	Show only the username	
o	--password	Show only the password	
o	--url	Show only the URL	
o	--notes	Show only the notes	
o	--field	Show only the field	v
o	--id	Show only the ID	
o	--name	Show only the name	
o	--attach	Show only the attachment	v
o	--basic-regexp|-G	Show sites matching case-insensitive regular expression	
o	--fixed-strings|-F	Show sites matching this exact substring	
o	--color	Control colored output to the terminal	V
a	1	0
=	show	--sync
v	auto	
v	now	
v	no	
=	show	--color
v	auto	
v	never	
v	always	
@	mv
o	--color	Control colored output to the terminal	V
a	2	0
=	mv	--color
v	auto	
v	never	
v	always	
@	add
o	--sync	When the current operation syncs to server	V=
o	--non-interactive	Accept data until EOF or, unless the notes field is being edited, the first new line	
o	--color	Control colored output to the terminal	V
o	--username	Add only the username	
o	--password	Add only the password	
o	--url	Add only the URL	
o	--notes	Add only the notes	
o	--field	Add only the field	v
o	--note-type	Add only the note	v
a	1	0
=	add	--sync
v	auto	
v	now	
v	no	
=	add	--color
v	auto	
v	never	
v	always	
=	add	--note-type
v	amex	
v	bank	
v	credit	
v	database	
v	drivers_license	
v	email	
v	health_insurance	
v	im	
v	mastercard	
v	membership	
v	passport	
v	server	
v	software_license	
v	ssh_key	
v	ssn	
v	visa	
v	wifi	
@	edit
o	--sync	When the current operation syncs to server	V=
o	--non-interactive	Accept data until EOF or, unless the notes field is being edited, the first new line	
o	--color	Control colored output to the terminal	V
o	--name|--username	Edit only the name (or username)	
o	--password	Edit only the password	
o	--url	Edit only the URL	
o	--notes	Edit only the notes	
o	--field	Edit only the field	v
a	1	0
=	edit	--sync
v	auto	
v	now	
v	no	
=	edit	--color
v	auto	
v	never	
v	always	
@	generate
o	--sync	When the current operation syncs to server	V=
o	--color	Control colored output to the terminal	V
o	--clip|-c	Copy the text to the clipboard	
o	--username	Generate password for this username	v
o	--url	Generate password for this URL	v
o	--no-symbols	Generate password without symbols	
a	2	0
=	generate	--sync
v	auto	
v	now	
v	no	
=	generate	--color
v	auto	
v	never	
v	always	
@	duplicate
o	--sync	When the current operation syncs to server	V=
o	--color	Control colored output to the terminal	V
a	1	0
=	duplicate	--sync
v	auto	
v	now	
v	no	
=	duplicate	--color
v	auto	
v	never	
v	always	
@	rm
o	--sync	When the current operation syncs to server	V=
o	--color	Control colored output to the terminal	V
a	1	0
=	rm	--sync
v	auto	
v	now	
v	no	
=	rm	--color
v	auto	
v	never	
v	always	
@	status
o	--quiet|-q	Display no output and only sets return code	
o	--color	Control colored output to the terminal	V
=	status	--color
v	auto	
v	never	
v	always	
@	sync
o	--background|-b	Syncronization occurs in a daemonized process	
o	--color	Control colored output to the terminal	V
=	sync	--color
v	auto	
v	never	
v	always	
@	import
o	--sync	When the current operation syncs to server	V=
o	--keep-dupes	Keeps any duplicate entries	
a	1	0
=	import	--sync
v	auto	
v	now	
v	no	
@	export
o	--sync	When the current operation syncs to server	V=
o	--color	Control colored output to the terminal	V
o	--fields	Comma-separated subset of: id, url, username, password, extra, name, fav, id, grouping, group…	v
a	1	0
=	export	--sync
v	auto	
v	now	
v	no	
=	export	--color
v	auto	
v	never	
v	always	
=	export	--fields
v	id,url,username,password,extra,name,fav,id,grouping,group,fullname,last_touch,last_modified_gmt,attachpresent	
@	share
s	userls	List the LastPass users which have access to the Shared Folders
s	useradd	Add user to Shared Folders
s	usermod	Modify user on Shared Folders
s	userdel	Remove user from Shared Folders
s	create	Create new LastPass Shared Folder
s	rm	LastPass Shared Folder to remove
s	limit	Manipulate LastPass Shared Folder access
a	1	0
@	share userls
@	share useradd
o	--read-only	Control read or write access	v
o	--hidden	Share user view permission	v
o	--admin	Share user administer permission	v
a	2	0
@	share usermod
o	--read-only	Control read or write access	v
o	--hidden	Share user view permission	v
o	--admin	Share user administer permission	v
a	2	0
@	share userdel
a	2	0
@	share create
a	1	0
@	share rm
a	1	0
@	share limit
o	--deny|--allow	Deny or allow access	
o	--add|--rm|--clear	Add, remove, or clear acces	
a	3	0
