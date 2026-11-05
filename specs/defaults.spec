@	
s	read	Shows defaults
s	write	Writes key for domain
s	delete	Deletes domain or key in domain
s	rename	Renames old_key to new_key
s	domains	Lists all domains
s	find	Lists all entries containing word
s	help	Show help text
s	read-type	Shows the type for the given domain, key
@	read
a	2	0
#	read	1
v	-globalDomain	Global domain
v	-app	Application name
d
@	write
a	3	0
#	write	1
v	-globalDomain	Global domain
v	-app	Application name
d
@	delete
a	2	0
#	delete	1
v	-globalDomain	Global domain
v	-app	Application name
d
@	rename
a	3	0
#	rename	1
v	-globalDomain	Global domain
v	-app	Application name
d
@	domains
@	find
a	1	0
@	help
@	read-type
a	2	0
#	read-type	1
v	-globalDomain	Global domain
v	-app	Application name
d
