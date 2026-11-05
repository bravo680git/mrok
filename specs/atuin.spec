@	
s	history	Manipulate shell history
s	import	Import shell history from file
s	stats	Calculate statistics for your history
s	search	Interactive history search
s	sync	Sync with the configured server
s	login	Login to the configured server
s	logout	Log out
s	register	Register with the configured server
s	key	Print the encryption key for transfer to another machine
s	status	
s	account	
s	kv	
s	server	Start an atuin server
s	init	Output shell setup
s	uuid	Generate a UUID
s	contributors	
s	gen-completions	Generate shell completions
o	--help|-h	Print help	p
o	--version|-V	Print version	
@	history
s	start	Begins a new command in the history
s	end	Finishes a new command in the history (adds time, exit code)
s	list	List all items in history
s	last	Get the last command ran
@	history start
a	1	1
@	history end
o	--exit|-e		v
a	1	0
@	history list
o	--cwd|-c		
o	--session|-s		
o	--human		
o	--cmd-only	Show only the text of the command	
o	--format|-f		v
@	history last
o	--human		
o	--cmd-only	Show only the text of the command	
o	--format|-f		v
@	import
s	auto	Import history for the current shell
s	zsh	Import history from the zsh history file
s	zsh-hist-db	Import history from the zsh history file
s	bash	Import history from the bash history file
s	resh	Import history from the resh history file
s	fish	Import history from the fish history file
s	nu	Import history from the nu history file
s	nu-hist-db	Import history from the nu history file
@	import auto
@	import zsh
@	import zsh-hist-db
@	import bash
@	import resh
@	import fish
@	import nu
@	import nu-hist-db
@	stats
o	--count|-c	How many top commands to list	v
a	1	1
@	search
o	--cwd|-c	Filter search result by directory	v
o	--exclude-cwd	Exclude directory from results	v
o	--exit|-e	Filter search result by exit code	v
o	--exclude-exit	Exclude results with this exit code	v
o	--before|-b	Only include results added before this date	v
o	--after	Only include results after this date	v
o	--limit	How many entries to return at most	v
o	--offset	Offset from the start of the results	v
o	--interactive|-i	Open interactive search UI	
o	--filter-mode	Allow overriding filter mode over config	v
o	--search-mode	Allow overriding search mode over config	v
o	--human	Use human-readable formatting for time	
o	--cmd-only	Show only the text of the command	
o	--delete	Delete anything matching this query. Will not print out the match	
o	--delete-it-all	Delete EVERYTHING!	
o	--reverse|-r	Reverse the order of results, oldest first	
o	--format|-f		v
o	--inline-height	Set the maximum number of lines Atuin's interface should take up	v
a	1	1
=	search	--filter-mode
v	global	
v	host	
v	session	
v	directory	
v	workspace	
=	search	--search-mode
v	prefix	
v	full-text	
v	fuzzy	
v	skim	
@	sync
o	--force|-f	Force re-download everything	
@	login
o	--username|-u		v
o	--password|-p		v
o	--key|-k	The encryption key for your account	v
@	logout
@	register
o	--username|-u		v
o	--password|-p		v
o	--email|-e		v
@	key
o	--base64	Switch to base64 output of the key	
@	status
@	account
s	login	Login to the configured server
s	register	
s	logout	Log out
s	delete	
@	account login
o	--username|-u		v
o	--password|-p		v
o	--key|-k	The encryption key for your account	v
@	account register
o	--username|-u		v
o	--password|-p		v
o	--email|-e		v
@	account logout
@	account delete
@	kv
s	set	
s	get	
@	kv set
o	--key|-k		v
o	--namespace|-n		v
a	1	0
@	kv get
o	--namespace|-n		v
a	1	0
@	server
s	start	Start the server
@	server start
o	--host	The host address to bind	v
o	--port|-p	The port to bind	v
@	init
o	--disable-ctrl-r	Disable the binding of CTRL-R to atuin	
o	--disable-up-arrow	Disable the binding of the Up Arrow key to atuin	
a	1	0
#	init	1
v	zsh	
v	bash	
v	fish	
v	nu	
@	uuid
@	contributors
@	gen-completions
o	--shell|-s	Set the shell for generating completions	v
o	--out-dir|-o	Set the output directory	v
=	gen-completions	--shell
v	bash	
v	elvish	
v	fish	
v	powershell	
v	zsh	
