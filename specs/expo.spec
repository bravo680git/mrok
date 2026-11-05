@	
s	login|signin	Login to an Expo account
s	logout	Logout of an Expo account
s	register	Sign up for a new Expo account
s	whoami|w	Return the currently authenticated account
s	build:ios|bi	Build and sign a standalone IPA for the Apple App Store
s	build:android|ba	Build and sign a standalone APK or App Bundle for the Google Play Store
s	build:web	Build the web app for production
s	build:status|bs	Get the status of the latest build for the project
s	client:ios	Deprecated in favor of Expo Dev Clients
s	client:install:ios	Install Expo Go for iOS on the simulator
s	client:install:android	Install Expo Go for Android on a connected device or emulator
s	credentials:manager	Manage your credentials
s	customize:web	Eject the default web files for customization
s	eject	Create native iOS and Android project files. Learn more: https://docs.expo.dev/workflow/customizing/
s	prebuild	Create native iOS and Android project files before building natively. Learn more…
s	export	Export the static files of the app for hosting it on a web server
s	fetch:ios:certs	Download the project's iOS standalone app signing credentials
s	fetch:android:keystore	Download the project's Android keystore
s	fetch:android:hashes	Compute and log the project's Android key hashes
s	fetch:android:upload-cert	Download the project's Android keystore
s	config	Show the project config
s	diagnostics	Log environment info to the console
s	doctor	Diagnose issues with the project
s	upgrade|update	Upgrade the project packages and config for the given SDK version
s	init|i	Create a new Expo project
s	install|add	Install a module or other package to a project
s	publish|p	Deploy a project to Expo hosting
s	publish:set|ps	Specify the channel to serve a published release
s	publish:rollback|pr	Undo an update to a channel
s	publish:history|ph	Log the project's releases
s	publish:details|pd	Log details of a published release
s	push:android:upload	Upload an FCM key for Android push notifications
s	push:android:show	Log the value currently in use for FCM notifications for this project
s	push:android:clear	Delete a previously uploaded FCM credential
s	run:android	Run the Android app binary locally
s	run:ios	Run the iOS app binary locally
s	send	Share the project's URL to an email address
s	start|r	Start a local dev server for the app
s	start:web|web	Start a Webpack dev server for the web app
s	upload:android|ua	Moved to eas submit in eas-cli
s	upload:ios|ui	Moved to eas submit in eas-cli
s	url|u	Log a URL for opening the project in Expo Go
s	url:ipa	Log the download URL for the standalone iOS binary
s	url:apk	Log the download URL for the standalone Android binary
s	webhooks	List all webhooks for a project
s	webhooks:add	Add a webhook to a project
s	webhooks:remove	Delete a webhook
s	webhooks:update	Update an existing webhook
o	-h|--help	Output usage information	
o	-V|--version	Output the version number	
@	login
o	-h|--help	Output usage information	
o	-u|--username	Username	V
o	-p|--password	Password	V
o	--otp	One-time password from your 2FA device	V
@	logout
o	-h|--help	Output usage information	
@	register
o	-h|--help	Output usage information	
@	whoami
o	-h|--help	Output usage information	
@	build:ios
o	-h|--help	Output usage information	
o	-c|--clear-credentials	Clear all credentials stored on Expo servers	v
o	--clear-dist-cert	Remove Distribution Certificate stored on Expo servers	v
o	--clear-push-key	Remove Push Notifications Key stored on Expo servers	v
o	--clear-push-cert	Remove Push Notifications Certificate stored on Expo servers. Use of Push Notifications…	v
o	--clear-provisioning-profile	Remove Provisioning Profile stored on Expo servers	v
o	-r|--revoke-credentials	Revoke credentials on developer.apple.com, select appropriate using --clear-* options	v
o	--apple-id	Apple ID username (please also set the Apple ID password as EXPO_APPLE_PASSWORD environment…	v
o	-t|--type	Type of build: [archive|simulator]	v
o	--release-channel	Pull from specified release channel	v
o	--no-publish	Disable automatic publishing before building	v
o	--no-wait	Exit immediately after scheduling build	v
o	--team-id	Apple Team ID	v
o	--dist-p12-path	Path to your Distribution Certificate P12 (set password as EXPO_IOS_DIST_P12_PASSWORD environment…	v
o	--push-id	Push Key ID (ex: 123AB4C56D)	v
o	--push-p8-path	Path to your Push Key .p8 file	v
o	--provisioning-profile-path	Path to your Provisioning Profile	v
o	--public-url	The URL of an externally hosted manifest (for self-hosted apps)	v
o	--skip-credentials-check	Skip checking credentials	v
o	--skip-workflow-check	Skip warning about build service bare workflow limitations	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	build:ios	-c
v	true	
v	false	
=	build:ios	--clear-dist-cert
v	true	
v	false	
=	build:ios	--clear-push-key
v	true	
v	false	
=	build:ios	--clear-push-cert
v	true	
v	false	
=	build:ios	--clear-provisioning-profile
v	true	
v	false	
=	build:ios	-r
v	true	
v	false	
=	build:ios	-t
v	archive	
v	simulator	
=	build:ios	--no-publish
v	true	
v	false	
=	build:ios	--no-wait
v	true	
v	false	
=	build:ios	--team-id
v	true	
v	false	
=	build:ios	--dist-p12-path
t	filepaths
=	build:ios	--push-id
v	true	
v	false	
=	build:ios	--push-p8-path
t	filepaths
=	build:ios	--provisioning-profile-path
t	filepaths
=	build:ios	--skip-credentials-check
v	true	
v	false	
=	build:ios	--skip-workflow-check
v	true	
v	false	
=	build:ios	--config
t	filepaths
#	build:ios	1
t	folders
@	build:android
o	-h|--help	Output usage information	
o	-c|--clear-credentials	Clear stored credentials	v
o	--release-channel	Pull from specified release channel	v
o	--no-publish	Disable automatic publishing before building	v
o	--no-wait	Exit immediately after triggering build	v
o	--keystore-path	Path to your Keystore: *.jks	v
o	--keystore-alias	Keystore Alias	v
o	--generate-keystore	[deprecated] Generate Keystore if one does not exist	v
o	--public-url	The URL of an externally hosted manifest (for self-hosted apps)	v
o	--skip-workflow-check	Skip warning about build service bare workflow limitations	v
o	-t|--type	Type of build: [app-bundle|apk]	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	build:android	-c
v	true	
v	false	
=	build:android	--no-publish
v	true	
v	false	
=	build:android	--no-wait
v	true	
v	false	
=	build:android	--keystore-path
t	filepaths
=	build:android	--generate-keystore
v	true	
v	false	
=	build:android	--skip-workflow-check
v	true	
v	false	
=	build:android	-t
v	true	
v	false	
=	build:android	--config
t	filepaths
#	build:android	1
t	folders
@	build:web
o	-h|--help	Output usage information	
o	-c|--clear	Clear all cached build files and assets	v
o	--no-pwa	Prevent webpack from generating the manifest.json and injecting meta into the index.html head	v
o	-d|--dev	Turns dev flag on before bundling	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	build:web	-c
v	true	
v	false	
=	build:web	--no-pwa
v	true	
v	false	
=	build:web	-d
v	true	
v	false	
=	build:web	--config
t	filepaths
#	build:web	1
t	folders
@	build:status
o	-h|--help	Output usage information	
o	--public-url	The URL of an externally hosted manifest (for self-hosted apps)	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	build:status	--config
t	filepaths
#	build:status	1
t	folders
@	client:ios
o	-h|--help	Output usage information	
o	--apple-id	Apple ID username (please also set the Apple ID password as EXPO_APPLE_PASSWORD environment…	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	client:ios	--config
t	filepaths
#	client:ios	1
t	folders
@	client:install:ios
o	-h|--help	Output usage information	
o	--latest	Install the latest version of Expo Go, ignoring the current project version	v
=	client:install:ios	--latest
v	true	
v	false	
@	client:install:android
o	-h|--help	Output usage information	
o	-d|--device	Device name to install the client on	V
o	--latest	Install the latest version of Expo Go, ignore the current project version	v
=	client:install:android	--latest
v	true	
v	false	
@	credentials:manager
o	-h|--help	Output usage information	
o	-p|--platform	Platform: [android|ios]	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	credentials:manager	-p
v	android	
v	ios	
=	credentials:manager	--config
t	filepaths
#	credentials:manager	1
t	folders
@	customize:web
o	-h|--help	Output usage information	
o	-f|--force	Allows replacing existing files	v
o	--offline	Allows this command to run while offline	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	customize:web	-f
v	true	
v	false	
=	customize:web	--offline
v	true	
v	false	
=	customize:web	--config
t	filepaths
#	customize:web	1
t	folders
@	eject
o	-h|--help	Output usage information	
o	--no-install	Skip installing npm packages and CocoaPods	v
o	--npm	Use npm to install dependencies. (default when Yarn is not installed)	v
o	-p|--platform	Platforms to sync: ios, android, all. Default: all	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	eject	--no-install
v	true	
v	false	
=	eject	--npm
v	true	
v	false	
=	eject	-p
v	all	
v	android	
v	ios	
=	eject	--config
t	filepaths
#	eject	1
t	folders
@	prebuild
o	-h|--help	Output usage information	
o	--no-install	Skip installing npm packages and CocoaPods	v
o	--clean	Delete the native folders and regenerate them before applying changes	v
o	--npm	Use npm to install dependencies. (default when Yarn is not installed)	v
o	--template	Project template to clone from. File path pointing to a local tar file or a github repo	v
o	-p|--platform	Platforms to sync: ios, android, all. Default: all	v
o	--skip-dependency-update	Preserves versions of listed packages in package.json (comma separated list)	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	prebuild	--no-install
v	true	
v	false	
=	prebuild	--clean
v	true	
v	false	
=	prebuild	--npm
v	true	
v	false	
=	prebuild	-p
v	all	
v	android	
v	ios	
=	prebuild	--config
t	filepaths
#	prebuild	1
t	folders
@	export
o	-h|--help	Output usage information	
o	--platform	Platforms: android, ios, all	v
o	-p|--public-url	The public url that will host the static files (required)	v
o	-c|--clear	Clear the Metro bundler cache	v
o	--output-dir	The directory to export the static files to	v
o	-a|--asset-url	The absolute or relative url that will host the asset files	v
o	-d|--dump-assetmap	Dump the asset map for further processing	v
o	--dev	Configure static files for developing locally using a non-https server	v
o	-s|--dump-sourcemap	Dump the source map for debugging the JS bundle	v
o	-q|--quiet	Suppress verbose output	v
o	-t|--target	Target environment for which this export is intended	v
o	--merge-src-dir	A repeatable source dir to merge in	v
o	--merge-src-url	A repeatable source tar.gz file URL to merge in	v
o	--max-workers	Maximum number of tasks to allow Metro to spawn	v
o	--experimental-bundle	Export bundles for use with EAS updates	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	export	--platform
v	all	
v	android	
v	ios	
=	export	-c
v	true	
v	false	
=	export	--output-dir
t	folders
=	export	-d
v	true	
v	false	
=	export	--dev
v	true	
v	false	
=	export	-s
v	true	
v	false	
=	export	-q
v	true	
v	false	
=	export	-t
v	managed	
v	bare	
=	export	--merge-src-dir
t	folders
=	export	--max-workers
d
=	export	--experimental-bundle
v	true	
v	false	
=	export	--config
t	filepaths
#	export	1
t	folders
@	fetch:ios:certs
o	-h|--help	Output usage information	
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	fetch:ios:certs	--config
t	filepaths
#	fetch:ios:certs	1
t	folders
@	fetch:android:keystore
o	-h|--help	Output usage information	
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	fetch:android:keystore	--config
t	filepaths
#	fetch:android:keystore	1
t	folders
@	fetch:android:hashes
o	-h|--help	Output usage information	
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	fetch:android:hashes	--config
t	filepaths
#	fetch:android:hashes	1
t	folders
@	fetch:android:upload-cert
o	-h|--help	Output usage information	
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	fetch:android:upload-cert	--config
t	filepaths
#	fetch:android:upload-cert	1
t	folders
@	config
o	-h|--help	Output usage information	
o	-t|--type	Type of config to show	v
o	--full	Include all project config data	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	config	-t
v	public	
v	prebuild	
v	introspect	
=	config	--full
v	true	
v	false	
=	config	--config
t	filepaths
#	config	1
t	folders
@	diagnostics
o	-h|--help	Output usage information	
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	diagnostics	--config
t	filepaths
#	diagnostics	1
t	folders
@	doctor
o	-h|--help	Output usage information	
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	doctor	--config
t	filepaths
#	doctor	1
t	folders
@	upgrade
o	-h|--help	Output usage information	
o	--npm	Use npm to install dependencies. (default when package-lock.json exists)	v
o	--yarn	Use Yarn to install dependencies. (default when yarn.lock exists)	v
a	1	0
=	upgrade	--npm
v	true	
v	false	
=	upgrade	--yarn
v	true	
v	false	
@	init
o	-h|--help	Output usage information	
o	-t|--template	Specify which template to use. Valid options are "blank", "tabs", "bare-minimum" or a package on…	V
o	--npm	Use npm to install dependencies. (default when Yarn is not installed)	v
o	--yarn	Use Yarn to install dependencies. (default when Yarn is installed)	v
o	--no-install	Skip installing npm packages or CocoaPods	v
o	--name	The name of your app visible on the home screen	V
o	--yes	Use default options. Same as "expo init . --template blank	v
a	1	0
=	init	--npm
v	true	
v	false	
=	init	--yarn
v	true	
v	false	
=	init	--no-install
v	true	
v	false	
=	init	--yes
v	true	
v	false	
@	install
o	-h|--help	Output usage information	
o	--npm	Use npm to install dependencies. (default when package-lock.json exists)	v
o	--yarn	Use Yarn to install dependencies. (default when yarn.lock exists)	v
a	1	1
=	install	--npm
v	true	
v	false	
=	install	--yarn
v	true	
v	false	
#	install	1
d
@	publish
o	-h|--help	Output usage information	
o	-q|--quiet	Suppress verbose output from the Metro bundler	v
o	-s|--send-to	A phone number or email address to send a link to	V
o	-c|--clear	Clear the Metro bundler cache	v
o	-t|--target	Target environment for which this publish is intended. Options are `managed` or `bare`	v
o	--max-workers	Maximum number of tasks to allow Metro to spawn	v
o	--release-channel	The release channel to publish to. Default is 'default'	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	publish	-q
v	true	
v	false	
=	publish	-c
v	true	
v	false	
=	publish	-t
v	managed	
v	bare	
=	publish	--max-workers
d
=	publish	--config
t	filepaths
#	publish	1
t	folders
@	publish:set
o	-h|--help	Output usage information	
o	-c|--release-channel	The channel to set the published release. (Required)	v
o	-p|--publish-id	The id of the published release to serve from the channel. (Required)	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	publish:set	-p
v	true	
v	false	
=	publish:set	--config
t	filepaths
#	publish:set	1
t	folders
@	publish:rollback
o	-h|--help	Output usage information	
o	--channel-id	This flag is deprecated	v
o	-c|--release-channel	The channel to rollback from. (Required)	v
o	-s|--sdk-version	The sdk version to rollback. (Required)	v
o	-p|--platform	The platform to rollback	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	publish:rollback	--channel-id
v	true	
v	false	
=	publish:rollback	-p
v	android	
v	ios	
=	publish:rollback	--config
t	filepaths
#	publish:rollback	1
t	folders
@	publish:history
o	-h|--help	Output usage information	
o	-c|--release-channel	Filter by release channel. If this flag is not included, the most recent publications will be shown	v
o	--count	Number of logs to view, maximum 100, default 5	v
o	-p|--platform	Filter by platform, android or ios. Defaults to both platforms	v
o	-s|--sdk-version	Filter by SDK version e.g. 35.0.0	v
o	-r|--raw	Produce some raw output	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	publish:history	--count
v	true	
v	false	
=	publish:history	-p
v	android	
v	ios	
=	publish:history	-r
v	true	
v	false	
=	publish:history	--config
t	filepaths
#	publish:history	1
t	folders
@	publish:details
o	-h|--help	Output usage information	
o	--publish-id	Publication id. (Required)	v
o	-r|--raw	Produce some raw output	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	publish:details	--publish-id
v	true	
v	false	
=	publish:details	-r
v	true	
v	false	
=	publish:details	--config
t	filepaths
#	publish:details	1
t	folders
@	push:android:upload
o	-h|--help	Output usage information	
o	--api-key	Server API key for FCM	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	push:android:upload	--api-key
v	true	
v	false	
=	push:android:upload	--config
t	filepaths
#	push:android:upload	1
t	folders
@	push:android:show
o	-h|--help	Output usage information	
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	push:android:show	--config
t	filepaths
#	push:android:show	1
t	folders
@	push:android:clear
o	-h|--help	Output usage information	
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	push:android:clear	--config
t	filepaths
#	push:android:clear	1
t	folders
@	run:android
o	-h|--help	Output usage information	
o	--no-bundler	Skip starting the Metro bundler	v
o	-d|--device	Device name to build the app on	V
o	-p|--port	Port to start the Metro bundler on. Default: 8081	v
o	--variant	(Android) build variant	V
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	run:android	--no-bundler
v	true	
v	false	
=	run:android	--config
t	filepaths
#	run:android	1
t	folders
@	run:ios
o	-h|--help	Output usage information	
o	--no-build-cache	Clear the native derived data before building	v
o	--no-install	Skip installing dependencies	v
o	--no-bundler	Skip starting the Metro bundler	v
o	-d|--device	Device name or UDID to build the app on	v
o	-p|--port	Port to start the Metro bundler on. Default: 8081	v
o	--scheme	Scheme to build	V
o	--configuration	Xcode configuration to use. Debug or Release. Default: Debug	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	run:ios	--no-build-cache
v	true	
v	false	
=	run:ios	--no-install
v	true	
v	false	
=	run:ios	--no-bundler
v	true	
v	false	
=	run:ios	-d
d
=	run:ios	--scheme
d
=	run:ios	--configuration
d
=	run:ios	--config
t	filepaths
#	run:ios	1
t	folders
@	send
o	-h|--help	Output usage information	
o	-s|--send-to	Email address to send the URL to	V
o	--dev-client	Experimental: Starts the bundler for use with the expo-development-client	v
o	--scheme	Custom URI protocol to use with a development build	v
o	-a|--android	Opens your app in Expo Go on a connected Android device	v
o	-i|--ios	Opens your app in Expo Go in a currently running iOS simulator on your computer	v
o	-w|--web	Opens your app in a web browser	v
o	-m|--host	Lan (default), tunnel, localhost. Type of host to use. "tunnel" allows you to view your link on…	V
o	--tunnel	Same as --host tunnel	v
o	--lan	Same as --host lan	v
o	--localhost	Same as --host localhost	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	send	--dev-client
v	true	
v	false	
=	send	-a
v	true	
v	false	
=	send	-i
v	true	
v	false	
=	send	-w
v	true	
v	false	
=	send	--tunnel
v	true	
v	false	
=	send	--lan
v	true	
v	false	
=	send	--localhost
v	true	
v	false	
=	send	--config
t	filepaths
#	send	1
t	folders
@	start
o	-h|--help	Output usage information	
o	-s|--send-to	An email address to send a link to	V
o	-c|--clear	Clear the Metro bundler cache	v
o	--max-workers	Maximum number of tasks to allow Metro to spawn	v
o	--dev	Turn development mode on	v
o	--no-dev	Turn development mode off	v
o	--minify	Minify code	v
o	--no-minify	Do not minify code	v
o	--https	To start webpack with https protocol	v
o	--force-manifest-type	Override auto detection of manifest type	v
o	-p|--port	Port to start the native Metro bundler on (does not apply to web or tunnel). Default: 19000	v
o	--no-https	To start webpack with http protocol	v
o	--dev-client	Experimental: Starts the bundler for use with the expo-development-client	v
o	--scheme	Custom URI protocol to use with a development build	v
o	-a|--android	Opens your app in Expo Go on a connected Android device	v
o	-i|--ios	Opens your app in Expo Go in a currently running iOS simulator on your computer	v
o	-w|--web	Opens your app in a web browser	v
o	-m|--host	Lan (default), tunnel, localhost. Type of host to use. "tunnel" allows you to view your link on…	V
o	--tunnel	Same as --host tunnel	v
o	--lan	Same as --host lan	v
o	--localhost	Same as --host localhost	v
o	--offline	Allows this command to run while offline	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	start	-c
v	true	
v	false	
=	start	--max-workers
d
=	start	--dev
v	true	
v	false	
=	start	--no-dev
v	true	
v	false	
=	start	--minify
v	true	
v	false	
=	start	--no-minify
v	true	
v	false	
=	start	--https
v	true	
v	false	
=	start	--force-manifest-type
v	true	
v	false	
=	start	--no-https
v	true	
v	false	
=	start	--dev-client
v	true	
v	false	
=	start	-a
v	true	
v	false	
=	start	-i
v	true	
v	false	
=	start	-w
v	true	
v	false	
=	start	--tunnel
v	true	
v	false	
=	start	--lan
v	true	
v	false	
=	start	--localhost
v	true	
v	false	
=	start	--offline
v	true	
v	false	
=	start	--config
t	filepaths
#	start	1
t	folders
@	start:web
o	-h|--help	Output usage information	
o	--dev	Turn development mode on	v
o	--no-dev	Turn development mode off	v
o	--minify	Minify code	v
o	--no-minify	Do not minify code	v
o	--https	To start webpack with https protocol	v
o	--no-https	To start webpack with http protocol	v
o	--force-manifest-type	Override auto detection of manifest type	v
o	-p|--port	Port to start the Webpack bundler on. Default: 19006	v
o	-s|--send-to	An email address to send a link to	V
o	--dev-client	Experimental: Starts the bundler for use with the expo-development-client	v
o	--scheme	Custom URI protocol to use with a development build	v
o	-a|--android	Opens your app in Expo Go on a connected Android device	v
o	-i|--ios	Opens your app in Expo Go in a currently running iOS simulator on your computer	v
o	-w|--web	Opens your app in a web browser	v
o	-m|--host	Lan (default), tunnel, localhost. Type of host to use. "tunnel" allows you to view your link on…	V
o	--tunnel	Same as --host tunnel	v
o	--lan	Same as --host lan	v
o	--localhost	Same as --host localhost	v
o	--offline	Allows this command to run while offline	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	start:web	--dev
v	true	
v	false	
=	start:web	--no-dev
v	true	
v	false	
=	start:web	--minify
v	true	
v	false	
=	start:web	--no-minify
v	true	
v	false	
=	start:web	--https
v	true	
v	false	
=	start:web	--no-https
v	true	
v	false	
=	start:web	--force-manifest-type
v	true	
v	false	
=	start:web	--dev-client
v	true	
v	false	
=	start:web	-a
v	true	
v	false	
=	start:web	-i
v	true	
v	false	
=	start:web	-w
v	true	
v	false	
=	start:web	--tunnel
v	true	
v	false	
=	start:web	--lan
v	true	
v	false	
=	start:web	--localhost
v	true	
v	false	
=	start:web	--offline
v	true	
v	false	
=	start:web	--config
t	filepaths
#	start:web	1
t	folders
@	upload:android
o	-h|--help	Output usage information	
o	--verbose	Migrate to eas submit --verbose	v
o	--latest	Migrate to eas submit --latest	v
o	--id	Migrate to eas submit --id <id>	v
o	--path	Migrate to eas submit --path <path>	V
o	--url	Migrate to eas submit --url <url>	v
o	--android-package	Migrate to eas submit (android-package is auto inferred)	v
o	--type	Migrate to eas submit (type is auto inferred)	v
o	--key	Migrate to eas.json's serviceAccountKeyPath property	v
o	--track	Migrate to eas.json's track property	v
o	--release-status	Migrate to eas.json's releaseStatus property	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	upload:android	--verbose
v	true	
v	false	
=	upload:android	--latest
v	true	
v	false	
=	upload:android	--path
t	filepaths
=	upload:android	--android-package
v	true	
v	false	
=	upload:android	--type
v	true	
v	false	
=	upload:android	--release-status
v	true	
v	false	
=	upload:android	--config
t	filepaths
#	upload:android	1
t	folders
@	upload:ios
o	-h|--help	Output usage information	
o	--verbose	Migrate to eas submit --verbose	v
o	--latest	Migrate to eas submit --latest	v
o	--id	Migrate to eas submit --id <id>	v
o	--path	Migrate to eas submit --path <path>	V
o	--url	Migrate to eas submit --url <url>	v
o	--apple-id	Migrate to eas.json's appleId property	v
o	--itc-team-id	Migrate to eas.json's appleTeamId property	v
o	--app-name	Migrate to eas.json's appName property	v
o	--company-name	Migrate to eas.json's companyName property	v
o	--sku	Migrate to eas.json's sku property	v
o	--language	Migrate to eas.json's language property	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	upload:ios	--verbose
v	true	
v	false	
=	upload:ios	--latest
v	true	
v	false	
=	upload:ios	--path
t	filepaths
=	upload:ios	--apple-id
v	true	
v	false	
=	upload:ios	--itc-team-id
v	true	
v	false	
=	upload:ios	--app-name
v	true	
v	false	
=	upload:ios	--company-name
v	true	
v	false	
=	upload:ios	--config
t	filepaths
#	upload:ios	1
t	folders
@	url
o	-h|--help	Output usage information	
o	--dev-client	Experimental: Starts the bundler for use with the expo-development-client	v
o	--scheme	Custom URI protocol to use with a development build	v
o	-a|--android	Opens your app in Expo Go on a connected Android device	v
o	-i|--ios	Opens your app in Expo Go in a currently running iOS simulator on your computer	v
o	-w|--web	Opens your app in a web browser	v
o	-m|--host	Lan (default), tunnel, localhost. Type of host to use. "tunnel" allows you to view your link on…	V
o	--tunnel	Same as --host tunnel	v
o	--lan	Same as --host lan	v
o	--localhost	Same as --host localhost	v
o	--offline	Allows this command to run while offline	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	url	--dev-client
v	true	
v	false	
=	url	-a
v	true	
v	false	
=	url	-i
v	true	
v	false	
=	url	-w
v	true	
v	false	
=	url	--tunnel
v	true	
v	false	
=	url	--lan
v	true	
v	false	
=	url	--localhost
v	true	
v	false	
=	url	--offline
v	true	
v	false	
=	url	--config
t	filepaths
#	url	1
t	folders
@	url:ipa
o	-h|--help	Output usage information	
o	--public-url	The URL of an externally hosted manifest (for self-hosted apps)	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	url:ipa	--config
t	filepaths
#	url:ipa	1
t	folders
@	url:apk
o	-h|--help	Output usage information	
o	--public-url	The URL of an externally hosted manifest (for self-hosted apps)	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	url:apk	--config
t	filepaths
#	url:apk	1
t	folders
@	webhooks
o	-h|--help	Output usage information	
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	webhooks	--config
t	filepaths
#	webhooks	1
t	folders
@	webhooks:add
o	-h|--help	Output usage information	
o	--url	URL to request. (Required)	v
o	--event	Event type that triggers the webhook. [build] (Required)	v
o	--secret	Secret used to create a hash signature of the request payload, provided in the 'Expo-Signature'…	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	webhooks:add	--event
v	true	
v	false	
=	webhooks:add	--config
t	filepaths
#	webhooks:add	1
t	folders
@	webhooks:remove
o	-h|--help	Output usage information	
o	--id	ID of the webhook to remove	v
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	webhooks:remove	--config
t	filepaths
#	webhooks:remove	1
t	folders
@	webhooks:update
o	-h|--help	Output usage information	
o	--id	ID of the webhook to update	v
o	--url	URL the webhook will request	V
o	--event	Event type that triggers the webhook. [build]	v
o	--secret	Secret used to create a hash signature of the request payload, provided in the 'Expo-Signature'…	V
o	--config	Deprecated: Use app.config.js to switch config files instead	V
a	1	0
=	webhooks:update	--event
v	true	
v	false	
=	webhooks:update	--config
t	filepaths
#	webhooks:update	1
t	folders
