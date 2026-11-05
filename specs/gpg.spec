@	
s	-s|--sign	Make a signature
s	--clearsign	Make a clear text signature
s	-b|--detach-sign	Make a detached signature
s	-e|--encrypt	Encrypt data
s	-c|--symmetric	Encrypt with symmetric cipher only
s	--store	Store only (make a simple RFC1991 packet)
s	--decrypt	Decrypt file (or stdin if no file is specified) and write it to stdout
s	--verify	Assume that sigfile is a signature and verify it without generating any output
s	--verify-files	Special version of --verify which does not work with detached signatures
s	--list-keys|--list-public-keys	List all keys from public keyrings, or just the ones given on the command line
s	--list-secret-keys	List all keys from secret keyrings, or just the ones given on the command line
s	--list-sigs	Same as --list-keys, but the signatures are listed too
s	--check-sigs	Same as --list-sigs, but the signatures are verified
s	--fingerprint	List all keys with their fingerprints
s	--list-packets	List only the sequence of packets
s	--gen-key	Generate a new key pair
s	--edit-key	Present a menu which enables you to do all key related tasks
s	--sign-key	Sign a public key with you secret key
s	--lsign-key	Sign a public key with you secret key but mark it as non-exportable
s	--trusted-key	Assume that the specified key is as trustworthy as one of your own secret keys
s	--delete-key	Remove key from the public keyring
s	--delete-secret-key	Remove key from the secret and public keyring
s	--gen-revoke	Generate a revocation certificate for the complete key
s	--export	Either export all keys from all keyrings or those of the given names
s	--send-keys	Same as --export but sends the keys to a keyserver
s	--export-all	Same as --export, but also exports keys which are not compatible to OpenPGP
s	--export-secret-keys	Same as --export, but exports the secret keys
s	--export-secret-subkeys	Same as --export, but exports the secret subkeys
s	--import	Import/merge keys. This adds the given keys to the keyring
s	--fast-import	--import but does not build the trustdb
s	--recv-keys	Import the keys with the given key IDs from a HKP keyserver
s	--export-ownertrust	List the ownertrust values in ASCII format
s	--import-ownertrust	Update the trustdb with the ownertrust values stored in files
s	--print-md	Print message digest of algorithm ALGO for all given files of stdin
s	--gen-random	Emit COUNT random bytes of the given quality level
s	--gen-prime	Generate prime numbers
s	--version	Print version information
s	--warranty	Print warranty information
s	-h|--help	Print usage information
o	--homedir	Set the name of the home directory	v
o	--options	Read options from file	v
o	-a|--armour	Create ASCII armored output	
o	-o|--output	Write output to file	v
o	-u|--local-user	Use name as the user ID to sign	v
o	--default-key	Use name as default user ID for signatures	v
o	-r|--recipient	Encrypt for user id name	v
o	--default-recipient	Use name as default recipient	v
o	--default-recipient-self	Use the default key as default recipient	
o	--no-default-recipient	Reset --default-recipient and --default-recipient-self	
o	--encrypt-to	Same as --recipient but this one is intended for in the options file	v
o	--no-encrypt-to	Disable the use of all --encrypt-to keys	
o	-v|--verbose	Give more information during processing	
o	-q|--quiet	Try to be as quiet as possible	
o	-Z	Set compression level to n	v
o	-t|--textmode	Use canonical text mode	
o	-n|--dry-run	Don't make any changes	
o	-i|--interactive	Prompt before overwriting any files	
o	--batch	Use batch mode	
o	--no-tty	Make sure that the TTY is never used for any output	
o	--no-batch	Disable batch mode	
o	--yes	Assume "yes" on most questions	
o	--no	Assume "no" on most questions	
o	--always-trust	Skip key validation	
o	--keyserver	Use name to lookup keys which are not yet in your keyring	v
o	--no-auto-key-retrieve	Disables the automatic retrieving of keys	
o	--honor-http-proxy	Try to access the keyserver over the proxy	
o	--keyring	Add file to the list of keyrings	v
o	--secret-keyring	Same as --keyring but for the secret keyrings	v
o	--charset	Set the name of the native character set	v
o	--utf8-strings	Assume that the arguments are already given as UTF8	
o	--no-utf8-strings		
o	--no-options	Shortcut for "--options /dev/null"	
o	--load-extension	Load an extension module	v
o	--debug	Set debugging flags	v
o	--debug-all	Set all useful debugging flags	
o	--status-fd	Write special status strings to the file descriptor n	v
o	--logger-fd	Write log output to file descriptor n and not to stderr	v
o	--no-comment	Do not write comment packets	
o	--comment	Use string as comment string in clear text signatures	v
o	--default-comment	Force to write the standard comment string	
o	--no-version	Omit the version string in clear text signatures	
o	--emit-version	Force to write the version string	
o	-N|--notation-data	Put the name value pair into the signature as notation data	v
o	--set-policy-url	Use string as Policy URL for signatures (rfc2440:5.2.3.19)	v
o	--set-filename	Use string as the name of file which is stored in messages	v
o	--use-embedded-filename	Try to create a file with a name as embedded in the data	
o	--completes-needed	Number of completely trusted users to introduce a new key signer	v
o	--marginals-needed	Number of marginally trusted users to introduce a new key signer	v
o	--max-cert-depth	Maximum depth of a certification chain	v
o	--cipher-algo	Use name as cipher algorithm	v
o	--digest-algo	Use name as message digest algorithm	v
o	--s2k-cipher-algo	Use name as the cipher algorithm used to protect secret keys	v
o	--s2k-digest-algo	Use name as the digest algorithm used to mangle the passphrases	v
o	--s2k-mode	Selects how passphrases are mangled	v
o	--compress-algo	Use compress algorithm n	v
o	--disable-cipher-algo	Never allow the use of name as cipher algorithm	v
o	--disable-pubkey-algo	Never allow the use of name as public key algorithm	v
o	--throw-keyid	Do not put the keyid into encrypted packets	
o	--not-dash-escaped	Makes signatures usable for patch files	
o	--escape-from-lines	Handle "<From" in emails	
o	--passphrase-fd	Read the passphrase from file descriptor n	v
o	--command-fd	This is a replacement for the depreciated shared-memory IPC mode	v
o	--rfc1991	Try to be more RFC1991 (PGP 2.x) compliant	
o	--openpgp	Reset all packet, cipher and digest options to OpenPGP	
o	--force-v3-sigs	Forces v3 signatures for signatures on data	
o	--force-mdc	Force encryption with appended manipulation code	
o	--allow-non-selfsigned-uid	Allow non self-signed user IDs	
o	--allow-freeform-uid	Disable all checks on the form of the user ID	
o	--ignore-time-conflict	Makes time checks just a warning	
o	--lock-once	Do not release the lock until the process terminates	
o	--lock-multiple	Release the locks every time one is no longer needed	
o	--lock-never	Disable locking entirely	
o	--no-random-seed-file	Disable random pool cache	
o	--no-verbose	Reset verbose level to 0	
o	--no-greeting	Suppress the initial copyright message	
o	--no-secmem-warning	Suppress the "using insecure memory" warning	
o	--no-armor	Assume the input data is not in ASCII armored format	
o	--no-default-keyring	Do not add the keyrings to the list of keyrings	
o	--skip-verify	Skip the signature verification step	
o	--with-colons	Print key listings delimited by colons	
o	--with-key-data	--with-colons with the public key data	
o	--with-fingerprint	--fingerprint with a different format	
o	--fast-list-mode	Changes the list commands to work faster	
o	--list-only	Skip the decryption pass	
o	--no-literal	This is not for normal use	
o	--set-filesize	This is not for normal use	
o	--emulate-md-encode-bug	Enables workaround to check faulty signatures	
o	--show-session-key	Display the session key used for one message	
o	--override-session-key	Don't use the public key but the session key string	v
o	--merge-only	Don't insert new keys into the keyrings	
o	--try-all-secrets	Try all secret keys in turn to find the right one	
=		--homedir
t	folders
=		--options
t	filepaths
=		-o
t	filepaths
=		-Z
v	0	
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
=		--keyring
t	filepaths
=		--secret-keyring
t	filepaths
=		--charset
v	iso-8859-1	This is the default Latin 1 set
v	iso-8859-2	The Latin 2 set
v	koi8-r	The usual Russian set (rfc1489)
=		--cipher-algo
d
=		--digest-algo
d
=		--s2k-cipher-algo
d
=		--s2k-digest-algo
d
=		--s2k-mode
v	0	A plain passphrase (which is not recommended) will be used
v	1	Adds a salt to the passphrase
v	3	Iterates the whole process a couple of times
=		--compress-algo
v	1	Use the old zlib version (RFC1951) which is used by PGP
v	2	RFC1950 compression
=		--disable-cipher-algo
d
@	-s
@	--clearsign
@	-b
@	-e
@	-c
@	--store
@	--decrypt
a	1	0
#	--decrypt	1
t	filepaths
@	--verify
a	2	1
#	--verify	1
t	filepaths
#	--verify	2
t	filepaths
@	--verify-files
a	1	1
#	--verify-files	1
t	filepaths
@	--list-keys
a	1	1
@	--list-secret-keys
a	1	1
@	--list-sigs
a	1	1
@	--check-sigs
a	1	1
@	--fingerprint
a	1	1
@	--list-packets
@	--gen-key
@	--edit-key
a	1	0
@	--sign-key
a	1	0
@	--lsign-key
a	1	0
@	--trusted-key
a	1	0
@	--delete-key
a	1	0
@	--delete-secret-key
a	1	0
@	--gen-revoke
@	--export
a	1	1
@	--send-keys
a	1	1
@	--export-all
a	1	1
@	--export-secret-keys
a	1	1
@	--export-secret-subkeys
a	1	1
@	--import
a	1	1
#	--import	1
t	filepaths
@	--fast-import
a	1	1
#	--fast-import	1
t	filepaths
@	--recv-keys
a	1	1
@	--export-ownertrust
@	--import-ownertrust
a	1	1
#	--import-ownertrust	1
t	filepaths
@	--print-md
a	2	1
#	--print-md	1
d
#	--print-md	2
t	filepaths
@	--gen-random
a	2	1
#	--gen-random	1
v	0	
v	1	
v	2	
#	--gen-random	2
t	filepaths
@	--gen-prime
a	3	1
@	--version
@	--warranty
@	-h
