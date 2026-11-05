@	
s	devices	List connected devices
s	help	Show this help message
s	get-state	Print offline | bootloader | device
s	get-serialno	Print <serial-number>
s	get-devpath	Print <device-path>
s	remount	Remount partitions read-write. if a reboot is required, -R will automatically reboot the device
s	jdwp	List pids of processes hosting a JDWP transport
s	root	Restart adbd with root permissions
s	unroot	Restart adbd without root permissions
s	usb	Restart adbd listening on USB
s	sideload	Sideload the given full OTA package
s	start-server	Ensure that there is a server running
s	kill-server	Kill the server if it is running
s	reconnect	Kick connection from host side to force reconnect
s	tcpip	Restart adbd listening on TCP on PORT
s	reboot	Reboot the device; defaults to booting system image but supports bootloader and recovery too…
s	disable-verity	Disable dm-verity checking on userdebug builds
s	enable-verity	Re-enable dm-verity checking on userdebug builds
s	wait-for-device	Wait for state=device
s	wait-for-recovery	Wait for state=recovery
s	wait-for-rescue	Wait for state=rescue
s	wait-for-sideload	Wait for state=sideload
s	wait-for-bootloader	Wait for state=bootloader
s	wait-for-disconnect	Wait for state=disconnect
s	wait-for-usb-device	Wait for usb in state=device
s	wait-for-usb-recovery	Wait for usb in state=recovery
s	wait-for-usb-rescue	Wait for usb in state=rescue
s	wait-for-usb-sideload	Wait for usb in state=sideload
s	wait-for-usb-bootloader	Wait for usb in state=bootloader
s	wait-for-usb-disconnect	Wait for usb in state=disconnect
s	wait-for-local-device	Wait for local in state=device
s	wait-for-local-recovery	Wait for local in state=recovery
s	wait-for-local-rescue	Wait for local in state=rescue
s	wait-for-local-sideload	Wait for local in state=sideload
s	wait-for-local-bootloader	Wait for local in state=bootloader
s	wait-for-local-disconnect	Wait for local in state=disconnect
s	wait-for-any-device	Wait for any in state=device
s	wait-for-any-recovery	Wait for any in state=recovery
s	wait-for-any-rescue	Wait for any in state=rescue
s	wait-for-any-sideload	Wait for any in state=sideload
s	wait-for-any-bootloader	Wait for any in state=bootloader
s	wait-for-any-disconnect	Wait for any in state=disconnect
s	keygen	Generate adb public/private key; private key stored in FILE
s	logcat	Show device log (logcat --help for more)
s	version	Show version num
s	connect	Connect to a device via TCP/IP [default port=5555]
s	disconnect	Disconnect from given TCP/IP device [default port=5555], or all
s	uninstall	Remove this app package from the device
s	bugreport	Write bugreport to given PATH [default=bugreport.zip];
s	pair	Pair with a device for secure TCP/IP communication
s	ppp	Run PPP over USB
s	emu	Run emulator console command
s	install	Push a single package to the device and install it
s	install-multiple	Push multiple APKs to the device for a single package and install them
s	install-multi-package	Push one or more packages to the device and install them atomically
s	shell	Run remote shell command (interactive shell if no command given)
s	mdns	Mdns utils
s	push	Copy local files/directories to device
s	sync	Sync a local build from $ANDROID_PRODUCT_OUT to the device (default all)
s	pull	Copy files/dirs from device
s	forward	Forward connection
s	reverse	Reverse connection
o	-a	Listen on all network interfaces, not just localhost	
o	-d	Use USB device (error if multiple devices connected)	
o	-e	Use TCP/IP device (error if multiple TCP/IP devices available)	
o	-s	Use device with given serial (overrides $ANDROID_SERIAL)	v
o	-t	Use device with given transport id	v
o	-H	Name of adb server host [default=localhost]	v
o	-P	Port of adb server [default=5037]	v
o	-L	Listen on given socket for adb server [default=tcp:localhost:5037]	v
@	devices
o	-l	Long output	
@	help
@	get-state
@	get-serialno
@	get-devpath
@	remount
o	-R	Reboot device	
@	jdwp
@	root
@	unroot
@	usb
@	sideload
a	1	0
@	start-server
@	kill-server
@	reconnect
s	device	Kick connection from device side to force reconnect
s	offline	Reset offline/unauthorized devices to force reconnect`
@	reconnect device
@	reconnect offline
@	tcpip
a	1	0
@	reboot
a	1	0
#	reboot	1
v	bootloader	
v	recovery	
v	sideload	
v	sideload-auto-reboot	
@	disable-verity
@	enable-verity
@	wait-for-device
@	wait-for-recovery
@	wait-for-rescue
@	wait-for-sideload
@	wait-for-bootloader
@	wait-for-disconnect
@	wait-for-usb-device
@	wait-for-usb-recovery
@	wait-for-usb-rescue
@	wait-for-usb-sideload
@	wait-for-usb-bootloader
@	wait-for-usb-disconnect
@	wait-for-local-device
@	wait-for-local-recovery
@	wait-for-local-rescue
@	wait-for-local-sideload
@	wait-for-local-bootloader
@	wait-for-local-disconnect
@	wait-for-any-device
@	wait-for-any-recovery
@	wait-for-any-rescue
@	wait-for-any-sideload
@	wait-for-any-bootloader
@	wait-for-any-disconnect
@	keygen
a	1	0
#	keygen	1
t	filepaths
@	logcat
@	version
@	connect
a	1	0
@	disconnect
a	1	0
@	uninstall
o	-k	Keep the data and cache directories	
@	bugreport
a	1	0
@	pair
a	2	0
@	ppp
a	2	1
@	emu
a	1	0
@	install
o	-l	Forward-lock the app	
o	-r	Replace existing application	
o	-t	Allow test packages	
o	-d	Allow version code downgrade (debuggable packages only)	
o	-s	Install on SD card instead of internal storage	
o	-g	Grant all runtime permissions	
o	--abi	Override platform's default ABI	v
o	--instant	Cause the app to be installed as an ephemeral install app	
o	--no-streaming	Always push APK to device and invoke Package Manager as separate steps	
o	--streaming	Force streaming APK directly into Package Manager	
o	--fastdeploy	Use fast deploy	
o	--no-fastdeploy	Prevent use of fast deploy	
o	--force-agent	Force update of deployment agent when using fast deploy	
o	--date-check-agent	Update deployment agent when local version is newer and using fast deploy	
o	--version-check-agent	Update deployment agent when local version has different version code and using fast deploy	
o	--local-agent	Locate agent files from local source build (instead of SDK location)	
a	1	0
#	install	1
t	filepaths
@	install-multiple
o	-p	Partial application install (install-multiple only)	
o	-l	Forward-lock the app	
o	-r	Replace existing application	
o	-t	Allow test packages	
o	-d	Allow version code downgrade (debuggable packages only)	
o	-s	Install on SD card instead of internal storage	
o	-g	Grant all runtime permissions	
o	--abi	Override platform's default ABI	v
o	--instant	Cause the app to be installed as an ephemeral install app	
o	--no-streaming	Always push APK to device and invoke Package Manager as separate steps	
o	--streaming	Force streaming APK directly into Package Manager	
o	--fastdeploy	Use fast deploy	
o	--no-fastdeploy	Prevent use of fast deploy	
o	--force-agent	Force update of deployment agent when using fast deploy	
o	--date-check-agent	Update deployment agent when local version is newer and using fast deploy	
o	--version-check-agent	Update deployment agent when local version has different version code and using fast deploy	
o	--local-agent	Locate agent files from local source build (instead of SDK location)	
a	1	1
#	install-multiple	1
t	filepaths
@	install-multi-package
o	-p	Partial application install (install-multiple only)	
o	-l	Forward-lock the app	
o	-r	Replace existing application	
o	-t	Allow test packages	
o	-d	Allow version code downgrade (debuggable packages only)	
o	-s	Install on SD card instead of internal storage	
o	-g	Grant all runtime permissions	
o	--abi	Override platform's default ABI	v
o	--instant	Cause the app to be installed as an ephemeral install app	
o	--no-streaming	Always push APK to device and invoke Package Manager as separate steps	
o	--streaming	Force streaming APK directly into Package Manager	
o	--fastdeploy	Use fast deploy	
o	--no-fastdeploy	Prevent use of fast deploy	
o	--force-agent	Force update of deployment agent when using fast deploy	
o	--date-check-agent	Update deployment agent when local version is newer and using fast deploy	
o	--version-check-agent	Update deployment agent when local version has different version code and using fast deploy	
o	--local-agent	Locate agent files from local source build (instead of SDK location)	
a	1	1
#	install-multi-package	1
t	filepaths
@	shell
o	-e	Choose escape character, or `none` default '~'	
o	-n	Don't read from stdin	
o	-T	Disable pty allocation	
o	-t	Allocate a pty if on a tty	
o	-tt	-tt: force pty allocation	
o	-x	Disable remote exit codes and stdout/stderr separation	
a	1	1
@	mdns
s	check	Check if mdns discovery is available
s	services	List all discovered services
@	mdns check
@	mdns services
@	push
o	--sync	Only push files that are newer on the host than the device	
o	-n	Dry run: push files to device without storing to the filesystem	
o	-z	Enable compression with a specified algorithm (any, none, brotli)	v
o	-Z	Disable compression	
a	2	0
=	push	-z
v	any	
v	none	
v	brotli	
#	push	1
t	filepaths
@	sync
o	-n	Dry run: push files to device without storing to the filesystem	
o	-l	List files that would be copied, but don't copy them	
o	-z	Enable compression with a specified algorithm (any, none, brotli)	v
o	-Z	Disable compression	
a	1	0
=	sync	-z
v	any	
v	none	
v	brotli	
#	sync	1
v	all	
v	data	
v	odm	
v	oem	
v	product	
v	system	
v	system_ext	
v	vendor	
@	pull
o	-a	Preserve file timestamp and mode	
o	-z	Enable compression with a specified algorithm (any, none, brotli)	v
o	-Z	Disable compression	
a	2	0
=	pull	-z
v	any	
v	none	
v	brotli	
#	pull	1
t	filepaths
@	forward
o	--list	List all forward socket connections	
o	--remove	Remove specific forward socket connection	v
o	--remove-all	Remove all forward socket connections	
o	--no-rebind	Reversal fails if the specified socket is already bound through a previous reverse command	
a	2	0
#	forward	1
v	tcp	
v	localabstract	
v	localreserved	
v	localfilesystem	
v	dev	
v	jdwp	
v	acceptfd	
#	forward	2
v	tcp	
v	localabstract	
v	localreserved	
v	localfilesystem	
v	dev	
v	jdwp	
v	acceptfd	
@	reverse
o	--list	List all reverse socket connections from device	
o	--remove	Remove specific reverse socket connection	v
o	--remove-all	Remove all reverse socket connections from device	
o	--no-rebind	Reversal fails if the specified socket is already bound through a previous reverse command	
a	2	0
#	reverse	1
v	tcp	
v	localabstract	
v	localreserved	
v	localfilesystem	
#	reverse	2
v	tcp	
v	localabstract	
v	localreserved	
v	localfilesystem	
