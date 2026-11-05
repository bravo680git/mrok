@	
o	--all-architectures	When verifying a code signature on code that has a universal ('fat') Mach-O binary, separately…	
o	-a|--architecture	When verifying or displaying signatures, explicitly select the Mach-O architecture given	v
o	--bundle-version	When handling versioned bundles such as frameworks, explicitly specify the version to operate on	v
o	-d|--display	Display information about the code at the path(s) given	
o	-D|--detached	When signing, designates that a detached signature should be written to the specified file	v
o	--deep	When signing a bundle, specifies that nested code content such as helpers, frameworks, and…	
o	--detached-database	When signing, specifies that a detached signature should be generated as with the --detached…	
o	-f|--force	When signing, causes codesign to replace any existing signature on the path(s) given	
o	-h|--hosting	Constructs and prints the hosting chain of a running program	
o	-i|--identifier	During signing, explicitly specify the unique identifier string that is embedded in code signatures	v
o	-o|--options	During signing, specifies a set of option flags to be embedded in the code signature	v
o	-P|--pagesize	Indicates the granularity of code signing. Pagesize must be a power of two	v
o	-r|--requirements	During signing, indicates that internal requirements should be embedded in the code path(s) as…	v
o	-R|--test-requirement	During verification, indicates that the path(s) given should be verified against the code…	v
o	-s|--sign	Sign the code at the path(s) given using this identity	v
o	-v|--verify	Requests verification of code signatures	
o	--continue	Instructs codesign to continue processing path arguments even if processing one fails	
o	--dryrun	During signing, performs almost all signing operations, but does not actually write the result…	
o	--entitlements	When signing, take the file at the given path and embed its contents in the signature as…	v
o	--extract-certificates	When displaying a signature, extract the certificates in the embedded certificate chain and write…	v
o	--file-list	When signing or displaying a signature, codesign writes to the given path a list of files that may…	v
o	--ignore-resources	During static validation, do not validate the contents of the code's resources	
o	--keychain	During signing, only search for the signing identity in the keychain file specified	v
o	--prefix	If no explicit unique identifier is specified (using the -i option), and if the implicitly…	v
o	--preserve-metadata=list	When re-signing code that is already signed, reuse some information from the old signature	
o	--resource-rules	During signing, this option overrides the default rules for identifying and collecting bundle…	v
o	--timestamp	During signing, requests that a timestamp authority server be contacted to authenticate the time…	V=
=		-D
t	filepaths
=		-o
d
=		--file-list
t	filepaths
=		--resource-rules
d
