@	
s	-l|--list	List all appropriate update labels
s	-d|--download	Download Only
s	-i|--install	Install
s	--list-full-installers	List the available macOS Installers
s	--fetch-full-installer	Install the latest recommended macOS Installer
s	--full-installer-version	The version of macOS to install
s	--install-rosetta	Install Rosetta 2
s	--background	Trigger a background scan and update operation
s	--dump-state	Log the internal state of the SU daemon to /var/log/install.log
s	--evaluate-products	Evaluate a list of product keys specified by the --products option
s	--history	Show the install history. By default, only displays updates installed by softwareupdate
o	--no-scan	Do not scan when listing or installing updates (use available updates previously scanned)	p
o	--product-types	Limit a scan to a particular product type only - ignoring all others	vp
o	--products	A comma-separated (no spaces) list of product keys to operate on	p
o	--force	Force an operation to complete. Use with --background to trigger a background scan regardless of…	p
o	--agree-to-license	Agree to the software license agreement without user interaction	p
o	--verbose	Enable verbose output	p
o	--help|-h	Show help for softwareupdate	
@	-l
@	-d
@	-i
o	-a|--all	All appropriate updates	
o	-R|--restart	Automatically restart (or shut down) if required to complete installation	
o	-r|--recommended	Only recommended updates	
a	1	1
#	-i	1
d
@	--list-full-installers
@	--fetch-full-installer
@	--full-installer-version
a	1	0
@	--install-rosetta
@	--background
@	--dump-state
@	--evaluate-products
@	--history
o	--all	Include all processes in history (including App installs)	
