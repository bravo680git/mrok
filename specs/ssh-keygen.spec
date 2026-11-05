@	
o	-A	For each of the key types (rsa, dsa, ecdsa and ed25519) for which host keys do not exist, generate…	
o	-a	When saving a private key, this option specifies the number of KDF	V
o	-B	Show the bubblebabble digest of specified private or public key file	
o	-b	Specifies the number of bits in the key to create	v
o	-C	Provides a new comment	v
o	-c	Requests changing the comment in the private and public key files	
o	-D	Download the public keys provided by the PKCS#11	v
o	-E	Specifies the hash algorithm used	v
o	-e	Read a OpenSSH key file and print to stdout	
o	-F	Search for the specified hostname (with optional port number)	v
o	-f	Specifies the filename of the key file	v
o	-g	Use generic DNS format when printing fingerprint resource records	
o	-H	Hash a known_hosts file	
o	-h	Create a host certificate instead of a user	
o	-I	Specify the key identity when signing a public key	v
o	-i	Read an unencrypted private (or public) key file	
o	-K	Download resident keys from a FIDO authenticator	
o	-k	Generate a KRL file	
o	-L	Generate a KRL file	
o	-l	Show fingerprint of specified public key file	
o	-M	Use for Moduli generation	v
o	-m	Specify a key format for key generation	v
o	-N	Provides the new passphrase	v
o	-n	Specify one or more principals (user or host names) to be included in a certificate when signing a…	v
o	-O	Specify a key/value option	v
o	-P	Provides the (old) passphrase	v
o	-p	Requests changing the passphrase of a private key file instead of creating a new private key	
o	-Q	Test whether keys have been revoked in a KRL	
o	-q	Silence ssh-keygen	
o	-R	Removes all keys belonging to hostname	v
o	-r	Print the SSHFP fingerprint resource record named hostname for the specified public key file	v
o	-s	Certify (sign) a public key using the specified CA key	v
o	-t	Specifies the type of key to create	v
o	-U	When used in combination with -s, this option indicates that a CA key resides in a ssh-agent(1)	
o	-u	Update a KRL	
o	-V	Specify a validity interval when signing a certificate	v
o	-v	Verbose mode	
o	-w	Specifies a path to a library that will be used when creating FIDO authenticator-hosted keys	v
o	-Y	Multiple functions: find principals, match principals, check novalidate, sign, verify	v
o	-y	Read a private OpenSSH format file and print an OpenSSH public key to stdout	
o	-Z	Specifies the cipher to use for encryption when writing an OpenSSH-format private key file	v
o	-z	Specifies a serial number to be embedded in the certificate to distinguish this certificate from…	v
=		-a
v	16	
=		-b
v	3072	
=		-E
v	md5	
v	sha256	
=		-f
t	filepaths
=		-I
t	filepaths
=		-M
v	generate	
v	screen	
=		-t
v	dsa	
v	ecdsa-sk	
v	ed25519	
v	ed25519-sk	
v	rsa	
=		-Y
v	find-principals	Find the principal(s) associated with the public key of a signature
v	check-novalidate	Checks that a signature generated using ssh-keygen -Y sign has a valid structure
v	sign	Cryptographically sign a file or some data using a SSH key
v	verify	Request to verify a signature generated using ssh-keygen -Y
