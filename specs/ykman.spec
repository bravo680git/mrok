@	
s	info	Displays information about the attached YubiKey such as serial number, firmware version…
s	list	List connected YubiKeys
s	config	Enable or disable applications
s	fido	Manage the FIDO applications
s	oath	Manage the OATH applications
s	openpgp	Manage the OpenPGP applications
s	otp	Manage the YubiOTP applications
s	piv	Manage the PIV applications
o	-d|--device	Specify which YubiKey to interact with by serial number	v
o	-r|--reader	Use an exteral smart card reader. Conflicts with --device and list	v
o	-l|--log-level	Enable logging at given verbosity level	v
o	--log-file	Write logs to the given FILE instead of standard error; ignore unless --log-level is also set	v
o	--diagnose	Show diagnostics information useful for troubleshooting	
o	-v|--version	Show version information about the app	
o	--full-help	Show --help, including hidden commands, and exit	
o	-h|--help	Show usage information	
=		-d
d
=		-r
d
=		-l
v	DEBUG	
v	INFO	
v	WARNING	
v	ERROR	
v	CRITICAL	
=		--log-file
t	filepaths
@	info
o	-c|--check-fips	Check if YubiKey is in FIPS Approved mode (available on YubiKey 4 FIPS only)	
o	-h|--help	Show info usage information	
@	list
o	-s|--serials	Output only serial numbers, one per line (devices without serial will be omitted)	
o	-r|--readers	List available smart card readers	
o	-h|--help	Show list usage information	
@	config
s	mode	Manage connection modes (USB Interfaces)
s	nfc	Enable or disable applications over NFC
s	set-lock-code	Set or change the configuration lock code
s	usb	Enable or disable applications over USB
o	-h|--help	Show config usage information	
@	config mode
o	--touch-eject	When set, the button toggles the state of the smartcard between ejected and inserted (CCID mode…	
o	--autoeject-timeout	When set, the button toggles the state of the smartcard between ejected and inserted (CCID mode…	v
o	--chalresp-timeout	When set, the smartcard will automatically eject after the given time. Implies --touch-eject (CCID…	v
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show config mode usage information	
a	1	0
#	config mode	1
d
@	config nfc
o	-f|--force	Confirm the action without prompting	
o	-e|--enable	Enable applications	v
o	-d|--disable	Disable applications	v
o	-a|--enable-all	Enable all applications	
o	-D|--disable-all	Disable all applications	
o	-l|--list	List enabled applications	
o	-L|--lock-code	Current application configuration lock code	v
o	-h|--help	Show config nfc usage information	
=	config nfc	-e
v	OTP	
v	U2F	
v	FIDO2	
v	OATH	
v	PIV	
v	OPENPGP	
v	HSMAUTH	
=	config nfc	-d
v	OTP	
v	U2F	
v	FIDO2	
v	OATH	
v	PIV	
v	OPENPGP	
v	HSMAUTH	
@	config set-lock-code
o	-f|--force	Confirm the action without prompting	
o	-L|--lock-code	Current lock code	v
o	-n|--new-lock-code	New lock code. Conflicts with --generate	v
o	-c|--clear	Clear the lock code	
o	-g|--generate	Generate a random lock code. Conflicts with --new-lock-code	
o	-h|--help	Show config set-lock-code usage information	
@	config usb
o	-f|--force	Confirm the action without prompting	
o	-e|--enable	Enable applications	v
o	-d|--disable	Disable applications	v
o	-l|--list	List enabled applications	
o	-a|--enable-all	Enable all applications	
o	-D|--disable-all	Disable all applications	
o	-L|--lock-code	Current application configuration lock code	v
o	--touch-eject	When set, the button toggles the state of the smartcard between ejected and inserted (CCID mode…	
o	--no-touch-eject	Disable touch eject (CCID only)	
o	--autoeject-timeout	When set, the smartcard will automatically eject after the given time. Implies --touch-eject	v
o	--chalresp-timeout	Sets the timeout when waiting for touch for challenge-response in the OTP application	v
o	-h|--help	Show config usb usage information	
=	config usb	-e
v	OTP	
v	U2F	
v	FIDO2	
v	OATH	
v	PIV	
v	OPENPGP	
v	HSMAUTH	
=	config usb	-d
v	OTP	
v	U2F	
v	FIDO2	
v	OATH	
v	PIV	
v	OPENPGP	
v	HSMAUTH	
@	fido
s	info	Display general status of the FIDO2 application
s	reset	Reset all FIDO applications. This action will wipe all FIDO credentials, including FIDO U2F…
s	access	Manage the PIN for FIDO
s	credentials	Manage discoverable (resident) credentials. This command lets you manage credentials stored on…
s	fingerprints	Manage fingerprints
o	-h|--help	Show fido usage information	
@	fido info
o	-h|--help	Show fido info usage information	
@	fido reset
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show fido reset usage information	
@	fido access
s	change-pin	Set or change PIN code
s	verify-pin	Verify the PIN against a YubiKey
o	-h|--help	Show fido access usage information	
@	fido access change-pin
o	-P|--pin	Current PIN code	v
o	-n|--new-pin	Current PIN code	v
o	-u|--u2f	Set FIDO U2F pin instead of FIDO2 PIN	
o	-h|--help	Show fido access change-pin usage information	
@	fido access verify-pin
o	-P|--pin	Current PIN code	v
o	-h|--help	Show fido access verify-pin usage information	
@	fido credentials
s	delete	Delete a credential
s	list	List credentials
o	-h|--help	Show fido credentials usage information	
@	fido credentials delete
o	-P|--pin	PIN code	v
o	-f|--force	Confirm deletion without prompting	
o	-h|--help	Show fido credentials delete usage information	
a	1	0
@	fido credentials list
o	-P|--pin	PIN code	v
o	-h|--help	Show fido credentials list usage information	
@	fido fingerprints
s	add	Add a new fingerprint
s	delete	Delete a fingerprint. Delete a fingerprint from the YubiKey by its ID, which can be seen by…
s	list	List registered fingerprint. Lists fingerprints by ID and (if available) label
s	rename	Set the label for a fingerprint
o	-h|--help	Show fido fingerprints usage information	
@	fido fingerprints add
o	-P|--pin	PIN code	v
o	-h|--help	Show fido fingerprints add usage information	
a	1	0
@	fido fingerprints delete
o	-P|--pin	PIN code	v
o	-f|--force	Confirm deletion without prompting	
o	-h|--help	Show fido fingerprints delete usage information	
a	1	0
@	fido fingerprints list
o	-P|--pin	PIN code	v
o	-h|--help	Show fido fingerprints list usage information	
@	fido fingerprints rename
o	-P|--pin	PIN code	v
o	-h|--help	Show fido rename usage information	
a	2	0
@	oath
s	info	Display general status of OATH application
s	reset	Reset all OATH data. This action will delete all accounts and restore factory settings for the…
s	access	Manage password protection for OATH
s	accounts	Manage and use OATH accounts
o	-h|--help	Show oath usage information	
@	oath info
o	-h|--help	Show oath info usage information	
@	oath reset
o	-h|--help	Show oath reset usage information	
o	-f|--force	Confirm the action without prompting	
@	oath access
s	change	Change the password used to protect OATH accounts. Alows you to set or change a password that will…
s	forget	Remove a stored password from this computer
s	remember	Store the YubiKeys password on this computer to avoid having to enter it on each use
o	-h|--help	Show oath access usage information	
@	oath access change
o	-p|--password	Provide a password to unlock the YubiKey	v
o	-c|--clear	Clear the current password	
o	-n|--new-password	Provide a new password as an argument	v
o	-h|--help	Show oath access change usage information	
@	oath access forget
o	-a|--all	Remove all stored passwords	
o	-h|--help	Show oath forget usage information	
@	oath access remember
o	-P|--password	Provide a password to unlock the YubiKey	v
o	-h|--help	Show oath remember usage information	
@	oath accounts
s	add	Add a new account
s	code	Generate codes
s	delete	Delete an account
s	list	List all accounts
s	rename	Rename an account (Requires YubiKey 5.3 or later)
s	uri	Add a new account from an otpauth:// URI
o	-h|--help	Show oath accounts usage information	
@	oath accounts add
o	-o|--oath-type	Time-based (TOTP) or counter-based (HOTP) account	v
o	-d|--digits	Number of digits in generated code	v
o	-a|--algorithm	Algorithm to use for code generation	v
o	-c|--counter	Initial counter value for HOTP accounts	v
o	-i|--issuer	Issuer of the account	v
o	-P|--period	Number of seconds a TOTP code is valid	v
o	-t|--touch	Require touch on YubiKey to generate code	
o	-f|--force	Confirm the action without prompting	
o	-p|--password	Provide a password to unlock the YubiKey	v
o	-r|--remember	Remember the password on this machine	
o	-h|--help	Show oath accounts add usage information	
a	2	0
=	oath accounts add	-o
v	HOTP	
v	TOTP	
=	oath accounts add	-d
v	6	
v	7	
v	8	
=	oath accounts add	-a
v	SHA1	
v	SHA256	
v	SHA512	
@	oath accounts code
o	-H|--show-hidden	Include hidden accounts	
o	-s|--single	Ensure only a single match, and output only the code	
o	-p|--password	Provide a password to unlock the YubiKey	v
o	-r|--remember	Remember the password on this machine	
o	-h|--help	Show oath accounts code usage information	
a	1	0
@	oath accounts delete
o	-f|--force	Confirm deletion without prompting	
o	-p|--password	Provide a password to unlock the YubiKey	v
o	-r|--remember	Remember the password on this machine	
o	-h|--help	Show oath accounts delete usage information	
a	1	0
@	oath accounts list
o	-H|--show-hidden	Include hidden accounts	
o	-o|--oath-type	Display the OATH type	
o	-P|--period	Display the period	
o	-p|--password	Provide a password to unlock the YubiKey	v
o	-r|--remember	Remember the password on this machine	
o	-h|--help	Show oath accounts list usage information	
@	oath accounts rename
o	-f|--force	Confirm rename without prompting	
o	-p|--password	Provide a password to unlock the YubiKey	v
o	-r|--remember	Remember the password on this machine	
o	-h|--help	Show oath accounts rename usage information	
a	2	0
@	oath accounts uri
o	-t|--touch	Require touch on YubiKey to generate code	
o	-f|--force	Confirm the action without prompting	
o	-p|--password	Provide a password to unlock the YubiKey	v
o	-r|--remember	Remember the password on this machine	
o	-h|--help	Show oath accounts uri usage information	
a	1	0
@	openpgp
s	info	Display general status of the OpenPGP application
s	reset	Reset all the OpenPGP data
s	access	Manage PIN, Reset Code, and Admin PIN
s	certificates	Manage certificates
s	keys	Manage private keys
o	-h|--help	Show openpgp usage information	
@	openpgp info
o	-h|--help	Show openpgp info usage information	
@	openpgp reset
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show openpgp reset usage information	
@	openpgp access
s	set-retries	Set PIN, Reset Code and Admin PIN retries
o	-h|--help	Show openpgp access usage information	
@	openpgp access set-retries
o	-a|--admin-pin	Admin PIN for OpenPGP	v
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show openpgp access set-retries usage information	
a	3	0
@	openpgp certificates
s	delete	Delete an OpenPGP certificate
s	export	Export an OpenPGP certificate
s	import	Import an OpenPGP certificate
o	-h|--help	Show openpgp certificates usage information	
@	openpgp certificates delete
o	-a|--admin-pin	Admin PIN for OpenPGP	v
o	-h|--help	Show openpgp certificates delete usage information	
a	1	0
@	openpgp certificates export
o	-F|--format	Encoding format	v
o	-h|--help	Show openpgp certificates export usage information	
a	2	0
=	openpgp certificates export	-F
v	PEM	
v	DER	
#	openpgp certificates export	2
t	filepaths
@	openpgp certificates import
o	-a|--admin-pin	Admin PIN for OpenPGP	v
o	-h|--help	Show openpgp certificates export usage information	
a	2	0
#	openpgp certificates import	2
t	filepaths
@	openpgp keys
s	attest	Generate a attestation certificate for a key. Attestation is used to show that an asymmetric key…
s	import	Import a private key (ONLY SUPPORTS ATTESTATION KEY)
s	set-touch	Set touch policy for OpenPGP key
o	-h|--help	Show openpgp keys usage information	
@	openpgp keys attest
o	-P|--pin	PIN code	v
o	-F|--format	Encoding format	v
o	-h|--help	Show openpgp keys attest usage information	
a	2	0
=	openpgp keys attest	-F
v	PEM	
v	DER	
#	openpgp keys attest	2
t	filepaths
@	openpgp keys import
o	-a|--admin-pin	Admin PIN for OpenPGP	v
o	-h|--help	Show openpgp keys import usage information	
a	2	0
@	openpgp keys set-touch
o	-a|--admin-pin	Admin PIN for OpenPGP	v
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show openpgp set-touch usage information	
a	2	0
@	otp
s	calculate	Perform a challenge-response operation. Send a challenge (in hex) to a YubiKey slot with a…
s	chalresp	Program a challenge-response operation
s	delete	Deletes the configuration stored in a slot
s	hotp	Program an HMAC-SHA1 OATH-HOTP credential
s	info	Display general status of the YubiKey OTP slots
s	ndef	Configure a slot to be used over NDEF (NFC)
s	settings	Update the settings for a slot
s	static	Configure a static password
s	swap	Swaps the two slot configurations
s	yubiotp	Program a Yubico OTP credential
o	--access-code	A 6 byte access code. Use "-" as a value to prompt for input	v
o	-h|--help	Show otp usage information	
@	otp calculate
o	-T|--totp	Generate a TOTP code, use the current time if challenge is omitted	
o	-d|--digits	Number of digits in generated TOTP code	v
o	-h|--help	Show otp calculate usage information	
=	otp calculate	-d
v	6	
v	8	
@	otp chalresp
o	-t|--touch	Require touch on the YubiKey to generate a response	
o	-T|--totp	Use a base32 encoded key (optionally padded) for TOTP credentials	
o	-g|--generate	Generate a random secret key. Conflicts with KEY argument	
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show otp chalresp usage information	
a	2	0
#	otp chalresp	1
v	1	
v	2	
@	otp delete
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show otp delete usage information	
a	1	0
#	otp delete	1
v	1	
v	2	
@	otp hotp
o	-d|--digits	Number of digits in generated code	v
o	-c|--counter	Initial counter value	v
o	-i|--identifier	Token identifier	v
o	--no-enter	Don't send an Enter keystroke after outputting the code	
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show otp hotp usage information	
a	2	0
=	otp hotp	-d
v	6	
v	8	
#	otp hotp	1
v	1	
v	2	
@	otp info
o	-h|--help	Show otp info usage information	
@	otp ndef
o	--prefix	Added before the NDEF payload. Typically a URI	v
o	-t|--ndef-type	NDEF payload type	v
o	-h|--help	Show otp ndef usage information	
a	1	0
=	otp ndef	-t
v	TEXT	
v	URI	
#	otp ndef	1
v	1	
v	2	
@	otp settings
o	-f|--force	Confirm the action without prompting	
o	-A|--new-access-code	Set a new 6 byte access code for the slot. Use "-" as a value to prompt for input	v
o	--delete-access-code	Remove access code from the slot	
o	--enter|--no-enter	Should send 'Enter' keystroke after slot output. (default: enter)	
o	-p|--pacing	Throttle output speed by adding a delay (in ms) between characters emitted	v
o	--use-numeric-keypad	Use scancodes for numeric keypad when sending digits. Helps with some keyboard layouts	
o	-h|--help	Show otp settings usage information	
=	otp settings	-p
v	0	
v	20	
v	40	
v	60	
@	otp static
o	-g|--generate	Generate a random password	
o	-l|--length	Length of generated password	v
o	-k|--keyboard-layout	Keyboard layout to use for the static password	v
o	--no-enter	Don't send an Enter keystroke after outputting the password	
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show otp chalresp usage information	
a	2	0
=	otp static	-k
v	MODHEX	
v	US	
v	UK	
v	DE	
v	FR	
v	BEPO	
v	NORMAN	
#	otp static	1
v	1	
v	2	
@	otp swap
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show otp swap usage information	
@	otp yubiotp
o	-P|--public-id	Public identifier prefix	v
o	-p|--private-id	6 byte private identifier	v
o	-k|--key	16 byte secret key	v
o	--no-enter	Don't send an Enter keystroke after emitting the OTP	
o	-S|--serial-public-id	Use YubiKey serial number as public ID. Conflicts with --public-id	
o	-g|--generate-private-id	Generate a random private ID. Conflicts with --private-id	
o	-G|--generate-key	Generate a random secret key. Conflicts with --key	
o	-u|--upload	Upload credential to YubiCloud (opens in browser). Conflicts with --force	
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show otp yubiotp usage information	
a	1	0
#	otp yubiotp	1
v	1	
v	2	
@	piv
s	info	Display general status of the PIV application
s	reset	Reset all PIV data
s	access	Manage PIN, PUK, and Management Key
s	certificates	Manage certificates
s	keys	Manage private keys
s	objects	Manage PIV data objects
o	-h|--help	Show piv usage information	
@	piv info
o	-h|--help	Show piv info usage information	
@	piv reset
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show piv reset usage information	
@	piv access
s	change-management-key	Change the management key
s	change-pin	Change the PIN code
s	change-puk	Change the PUK code
s	set-retries	Set the number of PIN and PUK retry attempts
s	unblock-pin	Unblock the PIN (using PUK)
o	-h|--help	Show piv access usage information	
@	piv access change-management-key
o	-P|--pin	PIN code	v
o	-t|--touch	Require touch on YubiKey to generate code	
o	-n|--new-management-key	A new management key	v
o	-m|--management-key	Current management key	v
o	-a|--algorithm	Management key algorithm	v
o	-p|--protect	Store new management key on the YubiKey, protected by PIN. A random key will be used if no key is…	
o	-g|--generate	Generate a random management key. Implied by --protect unless --new-management-key is also given…	
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show piv access change-management-key usage information	
=	piv access change-management-key	-a
v	TDES	
v	AES128	
v	AES192	
v	AES256	
@	piv access change-pin
o	-P|--pin	Current PIN code	v
o	-n|--new-pin	A new PIN	v
o	-h|--help	Show piv access change-pin usage information	
@	piv access change-puk
o	-P|--puk	Current PUK code	v
o	-n|--new-puk	A new PUK	v
o	-h|--help	Show piv access change-puk usage information	
@	piv access set-retries
o	-m|--management-key	The management key	v
o	-P|--pin	PIN code	v
o	-f|--force	Confirm the action without prompting	
o	-h|--help	Show piv access set-retries usage information	
a	2	0
@	piv access unblock-pin
o	-p|--puk		v
o	-n|--new-pin		v
o	-h|--help	Show piv access unblock-pin usage information	
@	piv certificates
s	delete	Delete a certificate
s	export	Export an X.509 certificate
s	generate	Generate a self-signed X.509 certificate
s	import	Import an X.509 certificate
s	request	Generate a Certificate Signing Request (CSR)
o	-h|--help	Show piv certificates usage information	
@	piv certificates delete
o	-m|--management-key	The management key	v
o	-P|--pin	PIN code	v
o	-h|--help	Show piv certificates delete usage information	
a	1	0
@	piv certificates export
o	-F|--format	Encoding format	v
o	-h|--help	Show piv certificates export usage information	
a	2	0
=	piv certificates export	-F
v	PEM	
v	DER	
#	piv certificates export	2
t	filepaths
@	piv certificates generate
o	-m|--management-key	The management key	v
o	-P|--pin	PIN code	v
o	-s|--subject	Subject for the certificate, as an RFC 4514 string	v
o	-d|--valid-days	Number of days until the certificate expires	v
o	-a|--hash-algorithm	Hash algorithm	v
o	-h|--help	Show piv certificates generate usage information	
a	2	0
=	piv certificates generate	-a
v	SHA1	
v	SHA256	
v	SHA384	
@	piv certificates import
o	-m|--management-key	The management key	v
o	-P|--pin	PIN code	v
o	-p|--password	A password may be needed to decrypt the data	v
o	-v|--verify	Verify that the certificate matches the private key in the slot	
o	-h|--help	Show piv certificates import usage information	
a	2	0
@	piv certificates request
o	-P|--pin	PIN code	v
o	-s|--subject	Subject for the certificate, as an RFC 4514 string	v
o	-a|--hash-algorithm	Hash algorithm	v
o	-h|--help	Show piv certificates request usage information	
a	3	0
=	piv certificates request	-a
v	SHA1	
v	SHA256	
v	SHA384	
v	SHA512	
#	piv certificates request	2
t	filepaths
#	piv certificates request	3
t	filepaths
@	piv keys
s	attest	Generate an attestation certificate for a key pair
s	export	Export a public key corresponding to a stored private key
s	generate	Generate an asymmetric key pair
s	import	Import a private key from file
o	-h|--help	Show piv keys usage information	
@	piv keys attest
o	-F|--format	Encoding format	v
o	-h|--help	Show piv keys attest usage information	
a	2	0
=	piv keys attest	-F
v	PEM	
v	DER	
#	piv keys attest	2
t	filepaths
@	piv keys export
o	-F|--format	Encoding format	v
o	-v|--verify	Verify that the public key matches the private key in the slot	
o	-P|--pin	PIN code (used for --verify)	v
o	-h|--help	Show piv keys attest usage information	
a	2	0
=	piv keys export	-F
v	PEM	
v	DER	
#	piv keys export	2
t	filepaths
@	piv keys generate
o	-m|--management-key	The management key	v
o	-P|--pin	PIN code	v
o	-a|--algorithm	Algorithm to use in key generation	v
o	-F|--format	Encoding format	v
o	--pin-policy	PIN policy for slot	v
o	--touch-policy	Touch policy for slot	v
o	-h|--help	Show piv keys generate usage information	
a	2	0
=	piv keys generate	-a
v	RSA1024	
v	RSA2048	
v	ECCP256	
v	ECCP384	
=	piv keys generate	-F
v	PEM	
v	DER	
=	piv keys generate	--pin-policy
v	DEFAULT	
v	NEVER	
v	ONCE	
v	ALWAYS	
=	piv keys generate	--touch-policy
v	DEFAULT	
v	NEVER	
v	ALWAYS	
v	ONCE	
#	piv keys generate	2
t	filepaths
@	piv keys import
o	-P|--pin	PIN code	v
o	-m|--management-key	The management key	v
o	--pin-policy	PIN policy for slot	v
o	--touch-policy	Touch policy for slot	v
o	-p|--password	Password used to decrypt the private key	v
o	-h|--help	Show piv keys import usage information	
a	2	0
=	piv keys import	--pin-policy
v	DEFAULT	
v	NEVER	
v	ONCE	
v	ALWAYS	
=	piv keys import	--touch-policy
v	DEFAULT	
v	NEVER	
v	ALWAYS	
v	ONCE	
#	piv keys import	2
t	filepaths
@	piv objects
s	export	Export an arbitrary PIV data object
s	generate	Generate and write data for a supported data object
s	import	Write an arbitrary PIV object
o	-h|--help	Show piv objects usage information	
@	piv objects export
o	-P|--pin	PIN code	v
o	-h|--help	Show piv objects export usage information	
a	2	0
#	piv objects export	2
t	filepaths
@	piv objects generate
o	-P|--pin	PIN code	v
o	-m|--management-key	The management key	v
o	-h|--help	Show piv objects generate usage information	
a	1	0
@	piv objects import
o	-P|--pin	PIN code	v
o	-m|--management-key	The management key	v
o	-h|--help	Show piv objects import usage information	
a	2	0
