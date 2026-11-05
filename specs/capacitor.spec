@	
s	add	Add a native platform project to your app
s	copy	Copy the web app build and Capacitor configuration file into the native platform project. Run this…
s	ls	List all installed Cordova and Capacitor plugins
s	open	Opens the native project workspace in the specified native IDE (Xcode for iOS, Android Studio for…
s	run	Opens the native project workspace in the specified native IDE (Xcode for iOS, Android Studio for…
s	sync	This command runs copy and then update
s	update	Updates the native plugins and dependencies referenced in package.json
o	--help|-h	Output usage information. Can be used with individual commands too	p
o	--version|-V	Output the version number	
@	add
a	1	0
#	add	1
v	android	
v	ios	
@	copy
a	1	0
#	copy	1
v	android	
v	ios	
@	ls
a	1	0
#	ls	1
v	android	
v	ios	
@	open
a	1	0
#	open	1
v	android	
v	ios	
@	run
o	--list	Print a list of target devices available to the given platform	
o	--target	Run on a specific target device	v
a	1	0
=	run	--target
d
#	run	1
v	android	
v	ios	
@	sync
o	--deployment	Podfile.lock won't be deleted and pod install will use --deployment option	
o	--inline	After syncing, all JS source maps will be inlined allowing for debugging an Android Web View in…	
a	1	0
#	sync	1
v	android	
v	ios	
@	update
o	--deployment	Podfile.lock won't be deleted and pod install will use --deployment option	
a	1	0
#	update	1
v	android	
v	ios	
