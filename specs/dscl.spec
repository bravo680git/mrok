@	
s	read|-read	Prints a directory
s	readall|-readall	Prints all the records of a given type
s	readpl|-readpl	Prints the contents of plist_path
s	readpli|-readpli	Prints the contents of plist_path for the plist at value_index of the key
s	list|-list|ls|-ls	Lists the subdirectories of the given directory
s	search|-search	Searches for records that match a pattern
s	create|-create|mk|-mk	Creates a new record
s	createpl|-createpl	Creates a string, or array of strings at plist_path
s	createpli|-createpli	Creates a string, or array of strings at plist_path for the plist at value_index of the key
s	append|-append	Appends one or more values to a property in a given record
s	merge|-merge	Appends one or more values to a property in a given directory if the property does not already…
s	delete|-delete|rm|-rm	Delete a directory, property, or value
s	deletepl|-deletepl	Deletes a value in a plist
s	deletepli|-deletepli	Deletes a value for the plist at value_index of the key
s	change|-change	Replaces the given old value in the list of values of the given key with the new value in the…
s	changei|-changei	Replaces the value at the given index in the list of values of the given key with the new value in…
s	diff|-diff	Compares the data from path1 and path2 looking at the specified keys (or all if no keys are…
s	passwd|-passwd	Changes the password of a user
o	-p	Prompt for password	
o	-u	Authenticate as user	v
o	-P	Authenticate with password	v
o	-f	Targeted local node database file path	v
o	-raw	Don't strip off prefix from DirectoryService API constants	
o	-plist	Print out record(s) or attribute(s) in XML plist format	
o	-url	Print record attribute values in URL-style encoding	
o	-q	Quiet - no interactive prompt	
a	1	0
#		1
v	.	
v	..	
v	localhost	
v	localonly	
@	read
a	2	1
#	read	1
d
@	readall
a	2	1
#	readall	1
d
@	readpl
a	3	0
#	readpl	1
d
@	readpli
a	4	0
#	readpli	1
d
@	list
a	2	0
#	list	1
d
@	search
a	3	0
#	search	1
d
@	create
a	3	1
#	create	1
d
@	createpl
a	5	1
#	createpl	1
d
@	createpli
a	6	1
#	createpli	1
d
@	append
a	3	1
#	append	1
d
@	merge
a	3	1
#	merge	1
d
@	delete
a	3	1
#	delete	1
d
@	deletepl
a	4	1
#	deletepl	1
d
@	deletepli
a	5	1
#	deletepli	1
d
@	change
a	4	0
#	change	1
d
@	changei
a	4	0
#	changei	1
d
@	diff
a	3	1
#	diff	1
d
#	diff	2
d
@	passwd
a	2	0
#	passwd	1
d
