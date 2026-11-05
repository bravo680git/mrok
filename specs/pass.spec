@	
s	init	Initialize new password storage and use gpg-id for encryption
s	insert	Insert a new password into the password store called pass-name
s	git	Password store git functions
s	version	Show version information
s	help	Show usage message
s	cp	Copies the password or directory named old-path to new-path
s	mv	Renames the password or directory named old-path to new-path
s	rm	Remove the password named pass-name from the password store
s	generate	Generate a new password of length pass-length and insert into pass-name
s	ls|list	List names of passwords inside the tree at subfolder by using the tree
s	find	List names of passwords inside the tree that match pass-names
s	show	Decrypt and print a password
s	edit	Insert a new password or edit an existing password using the default text editor specified by the…
s	grep	Searches inside each decrypted password file for search-string. Grep options can be used
o	--clip|-c	Copy the password to the clipboard	
o	--qrcode|-q	Display a QRcode of the password	
o	--help	Show help for pass	
a	1	0
#		1
d
@	init
o	--path|-p	A specific gpg-id or set of gpg-ids is assigned for that specific sub folder of the password store	v
a	1	0
=	init	--path
t	folders
@	insert
o	--echo|-e	Disable keyboard echo when the password is entered and confirm the password by asking for it twice	
o	--multi-line|-m	Lines will be read until EOF or Ctrl+D is reached. Otherwise, only a single line from standard in…	
o	--force|-f	Don't prompt before overwriting an existing password	
a	1	0
@	git
@	version
@	help
@	cp
o	--force|-f	Do not interactively prompt before moving	
a	2	0
#	cp	1
d
@	mv
o	--force|-f	Do not interactively prompt before moving	
a	2	0
#	mv	1
d
@	rm
o	--recursive|-r	Delete pass-name recursively if it is a directory	
o	--force|-f	Do not interactively prompt before removal	
a	1	0
#	rm	1
d
@	generate
o	--no-symbols|-n	Do not use any non-alphanumeric characters in the generated password	
o	--clip|-c	Do not print the password but instead copy it to the clipboard	
o	--in-place|-i	Do not interactively prompt, and only replace the first line of the password file with the new…	
o	--force|-f	Overwrite the existing password	
a	2	0
@	ls
a	1	0
#	ls	1
d
@	find
a	1	0
@	show
o	--clip|-c	Copy the password to the clipboard	
o	--qrcode|-q	Display a QRcode of the password	
a	1	0
#	show	1
d
@	edit
a	1	0
#	edit	1
d
@	grep
a	1	0
