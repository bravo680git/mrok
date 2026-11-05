@	
s	list	List all installed formulae
s	ls	List all installed formulae
s	leaves	List installed formulae that are not dependencies of another installed formula
s	doctor	Check your system for potential problems
s	abv|info	Display brief statistics for your Homebrew installation
s	update	Fetch the newest version of Homebrew and all formulae
s	outdated	List installed casks and formulae that have an updated version available
s	pin	Pin formula, preventing them from being upgraded
s	unpin	Unpin formula, allowing them to be upgraded
s	upgrade	Upgrade outdated casks and outdated, unpinned formulae using the same options they were originally…
s	search	Perform a substring search of cask tokens and formula names
s	config	Show Homebrew and system configuration info
s	postinstall	Rerun the post install step for formula
s	install	Install <formula>
s	reinstall	Uninstall and then reinstall a formula or cask using the same options it was originally installed…
s	uninstall|remove|rm	Uninstall a formula or cask
s	--prefix	Prefix of <formula>
s	cask	Homebrew Cask provides a friendly CLI workflow for the administration of macOS applications…
s	cleanup	Remove stale lock files and outdated downloads for all formulae and casks and remove old versions…
s	services	Manage background services with macOS' launchctl(1) daemon manager
s	analytics	Manages analytics preferences
s	autoremove	Uninstall formulae that were only installed as a dependency of another formula and are now no…
s	tap	Tap a formula repository
s	untap	Remove a tapped formula repository
s	link	Symlink all of formula's installed files into Homebrew's prefix
s	unlink	Remove symlinks for formula from Homebrew's prefix
s	formulae	List all available formulae
s	casks	List all available casks
s	edit	
s	home|homepage	Open a formula, cask's homepage in a browser, or open Homebrew's own homepage if no argument is…
s	alias	Manage custom user created brew aliases
s	developer	Display the current state of Homebrew's developer mode
o	--version	The current Homebrew version	
a	1	0
#		1
d
@	list
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--formula|--formulae	List only formulae, or treat all named arguments as formulae	
o	--cask|--casks	List only casks, or treat all named arguments as casks	
o	--unbrewed	List files in Homebrew's prefix not installed by Homebrew. (disabled; replaced by brew --prefix…	
o	--full-name	Print formulae with fully-qualified names. Unless --full-name, --versions or	
o	--pinned	List only pinned formulae, or only the specified (pinned) formulae if formula are provided	
o	--versions	Show the version number for installed formulae, or only the specified formulae if formula are…	
o	--multiple	Only show formulae with multiple versions installed	
o	--pinned	List only pinned formulae, or only the specified (pinned) formulae if formula are provided. See…	
o	-1	Force output to be one entry per line. This is the default when output is not to a terminal	
o	-l	List formulae and/or casks in long format. Has no effect when a formula or cask name is passed as…	
o	-r	Reverse the order of the formulae and/or casks sort to list the oldest entries first. Has no…	
o	-t	Sort formulae and/or casks by time modified, listing most recently modified first. Has no effect…	
a	1	1
#	list	1
d
@	ls
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--formula	List only formulae, or treat all named arguments as formulae	
o	--cask	List only casks, or treat all named arguments as casks	
o	--unbrewed	List files in Homebrew's prefix not installed by Homebrew. (disabled; replaced by brew --prefix…	
o	--full-name	Print formulae with fully-qualified names. Unless --full-name, --versions or	
o	--pinned	List only pinned formulae, or only the specified (pinned) formulae if formula are provided	
o	--versions	Show the version number for installed formulae, or only the specified formulae if formula are…	
o	--multiple	Only show formulae with multiple versions installed	
o	--pinned	List only pinned formulae, or only the specified (pinned) formulae if formula are provided	
o	-1	Force output to be one entry per line. This is the default when output is not to a terminal	
o	-l	List formulae and/or casks in long format. Has no effect when a formula or cask name is passed as…	
o	-r	Reverse the order of the formulae and/or casks sort to list the oldest entries first. Has no…	
o	-t	Sort formulae and/or casks by time modified, listing most recently modified first. Has no effect…	
a	1	1
#	ls	1
d
@	leaves
o	-r|--installed-on-request	Show manually installed formula	
o	-p|--installed-as-dependency	Show installed formula as dependencies	
@	doctor
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--list-checks	List all audit methods	
o	-D|--audit-debug	Enable debugging and profiling of audit methods	
@	abv
o	--cask|--casks	List only casks, or treat all named arguments as casks	
o	--analytics	List global Homebrew analytics data or, if specified, installation and build error data for formula	
o	--days	How many days of analytics data to retrieve	v
o	--category	Which type of analytics data to retrieve	v
o	--github	Open the GitHub source page for formula in a browser	
o	--json	Print a JSON representation	
o	--installed	Print JSON of formulae that are currently installed	
o	--all	Print JSON of all available formulae	
o	-v|--verbose	Show more verbose analytics data for formulae	
o	--formula	Treat all named arguments as formulae	
o	--cash	Treat all named arguments as casks	
o	-d|--debug	Display any debugging information	
o	-q|--quiet	List only the names of outdated kegs	
o	-h|--help	Get help with services command	
a	1	1
=	abv	--days
v	30	
v	90	
v	365	
=	abv	--category
d
#	abv	1
d
@	update
o	-f|--force	Always do a slower, full update check	
o	-v|--verbose	Print the directories checked and git operations performed	
o	-d|--debug	Display a trace of all shell commands as they are executed	
o	-h|--help	Show help message	
o	--merge	Use git merge to apply updates (rather than git rebase)	
o	--preinstall	Run on auto-updates (e.g. before brew install). Skips some slower steps	
@	outdated
o	-d|--debug	Display any debugging information	
o	-q|--quiet	List only the names of outdated kegs	
o	-v|--verbose	Include detailed version information	
o	-h|--help	Show help message for the outdated command	
o	--cask	List only outdated casks	
o	--fetch-HEAD	Fetch the upstream repository to detect if the HEAD installation of the formula is outdated	
o	--formula	List only outdated formulae	
o	--greedy	Print outdated casks with auto_updates or version :latest	
o	--greedy-latest	Print outdated casks including those with version :latest	
o	--greedy-auto-updates	Print outdated casks including those with auto_updates true	
o	--json	Print output in JSON format	
@	pin
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
a	1	1
#	pin	1
d
@	unpin
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
a	1	1
#	unpin	1
d
@	upgrade
o	-d|--debug	If brewing fails, open an interactive debugging session with access to IRB or a shell inside the…	
o	-f|--force	Install formulae without checking for previously installed keg-only or non-migrated versions. When…	
o	-v|--verbose	Print the verification and postinstall steps	
o	-n|--dry-run	Show what would be upgraded, but do not actually upgrade anything	
o	-s|--build-from-source	Compile formula from source even if a bottle is provided. Dependencies will still be installed…	
o	-i|--interactive	Download and patch formula, then open a shell	
o	-g|--git	Create a Git repository	
o	-q|--quiet	Make some output more quiet	
o	-h|--help	Show this message	
o	--formula|--formulae	Treat all named arguments as formulae. If no named arguments are specified, upgrade only outdated…	
o	--env	Disabled other than for internal Homebrew use	
o	--ignore-dependencies	An unsupported Homebrew development flag to skip installing any dependencies of any kind. If the…	
o	--only-dependencies	Install the dependencies with specified options but do not install the formula itself	
o	--cc	Attempt to compile using the specified compiler, which should be the name of the compiler's…	v
o	--force-bottle	Install from a bottle if it exists for the current or newest version of macOS, even if it would…	
o	--include-test	Install testing dependencies required to run brew test formula	
o	--HEAD	If formula defines it, install the HEAD version, aka. main, trunk, unstable, master	
o	--fetch-HEAD	Fetch the upstream repository to detect if the HEAD installation of the formula is outdated…	
o	--ignore-pinned	Set a successful exit status even if pinned formulae are not upgraded	
o	--keep-tmp	Retain the temporary files created during installation	
o	--build-bottle	Prepare the formula for eventual bottling during installation, skipping any post-install steps	
o	--bottle-arch	Optimise bottles for the specified architecture rather than the oldest architecture supported by…	
o	--display-times	Print install times for each formula at the end of the run	
o	--cask|--casks	Treat all named arguments as casks. If no named arguments are specified, upgrade only outdated casks	
o	--binaries	Disable/enable linking of helper executables (default: enabled)	
o	--no-binaries	Disable/enable linking of helper executables (default: enabled)	
o	--require-sha	Require all casks to have a checksum	
o	--quarantine	Disable/enable quarantining of downloads (default: enabled)	
o	--no-quarantine	Disable/enable quarantining of downloads (default: enabled)	
o	--skip-cask-deps	Skip installing cask dependencies	
o	--greedy	Also include casks with auto_updates true or version :latest	
o	--greedy-latest	Also include casks with version :latest	
o	--greedy-auto-updates	Also include casks with auto_updates true	
o	--appdir	Target location for Applications (default: /Applications)	v
o	--colorpickerdir	Target location for Color Pickers (default: ~/Library/ColorPickers)	v
o	--prefpanedir	Target location for Preference Panes (default: ~/Library/PreferencePanes)	v
o	--qlplugindir	Target location for QuickLook Plugins (default: ~/Library/QuickLook)	v
o	--mdimporterdir	Target location for Spotlight Plugins (default: ~/Library/Spotlight)	v
o	--dictionarydir	Target location for Dictionaries (default: ~/Library/Dictionaries)	v
o	--fontdir	Target location for Fonts (default: ~/Library/Fonts)	v
o	--servicedir	Target location for Services (default: ~/Library/Services)	v
o	--input-methoddir	Target location for Input Methods (default: ~/Library/Input Methods)	v
o	--internet-plugindir	Target location for Internet Plugins (default: ~/Library/Internet Plug-Ins)	v
o	--audio-unit-plugindir	Target location for Audio Unit Plugins (default: ~/Library/Audio/Plug-Ins/Components)	v
o	--vst-plugindir	Target location for VST Plugins (default: ~/Library/Audio/Plug-Ins/VST)	v
o	--vst3-plugindir	Target location for VST3 Plugins (default: ~/Library/Audio/Plug-Ins/VST3)	v
o	--screen-saverdir	Target location for Screen Savers (default: ~/Library/Screen Savers)	v
o	--language	Comma-separated list of language codes to prefer for cask installation. The first matching…	
a	1	1
=	upgrade	--cc
v	gcc-7	
v	llvm_clang	
v	clang	
=	upgrade	--appdir
t	folders
=	upgrade	--colorpickerdir
t	folders
=	upgrade	--prefpanedir
t	folders
=	upgrade	--qlplugindir
t	folders
=	upgrade	--mdimporterdir
t	folders
=	upgrade	--dictionarydir
t	folders
=	upgrade	--fontdir
t	folders
=	upgrade	--servicedir
t	folders
=	upgrade	--input-methoddir
t	folders
=	upgrade	--internet-plugindir
t	folders
=	upgrade	--audio-unit-plugindir
t	folders
=	upgrade	--vst-plugindir
t	folders
=	upgrade	--vst3-plugindir
t	folders
=	upgrade	--screen-saverdir
t	folders
#	upgrade	1
d
@	search
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--formula	Search online and locally for formulae	
o	--cask	Search online and locally for casks	
o	--desc	Search for formulae with a description matching text and casks with a name matching text	
o	--pull-request	Search for GitHub pull requests containing text	
o	--open	Search for only open GitHub pull requests	
o	--closed	Search for only closed GitHub pull requests	
o	--repology|--macports	Search for text in the given database	
o	--fink|--opensuse	Search for text in the given database	
o	--fedora|--debian	Search for text in the given database	
o	--ubuntu	Search for text in the given database	
@	config
@	postinstall
o	-d|--debug	Display any debugging information	
o	-v|--verbose	Make some output more verbose	
o	-q|--quiet	Make some output more quiet	
o	-h|--help	Show this message	
a	1	1
#	postinstall	1
d
@	install
o	-f|--force	Install formulae without checking for previously installed keg-only or non-migrated versions. When…	
o	-v|--verbose	Print the verification and postinstall steps	
o	-s|--build-from-source	Compile formula from source even if a bottle is provided. Dependencies will still be installed…	
o	-i|--interactive	Download and patch formula	
o	-g|--git	Create a Git repository	
o	-q|--quiet	Make some output more quiet	
o	-h|--help	Show this message	
o	--formula	Treat all named arguments as formulae	
o	--env	Disabled other than for internal Homebrew use	
o	--ignore-dependencies	An unsupported Homebrew development flag to skip installing any dependencies of any kind. If the…	
o	--only-dependencies	Install the dependencies with specified options but do not install the formula itself	
o	--cc	Attempt to compile using the specified compiler, which should be the name of the compiler's…	v
o	--force-bottle	Install from a bottle if it exists for the current or newest version of macOS, even if it would…	
o	--include-test	Install testing dependencies required to run brew test formula	
o	--HEAD	If formula defines it, install the HEAD version, aka. main, trunk, unstable, master	
o	--fetch-HEAD	Fetch the upstream repository to detect if the HEAD installation of the formula is outdated…	
o	--keep-tmp	Retain the temporary files created during installation	
o	--build-bottle	Prepare the formula for eventual bottling during installation, skipping any post-install steps	
o	--bottle-arch	Optimise bottles for the specified architecture rather than the oldest architecture supported by…	
o	--display-times	Print install times for each formula at the end of the run	
o	--cask	--casks Treat all named arguments as casks	
o	--binaries	Disable/enable linking of helper executables (default: enabled)	
o	--no-binaries	Disable/enable linking of helper executables (default: enabled)	
o	--require-sha	Require all casks to have a checksum	
o	--quarantine	Disable/enable quarantining of downloads (default: enabled)	
o	--no-quarantine	Disable/enable quarantining of downloads (default: enabled)	
o	--skip-cask-deps	Skip installing cask dependencies	
o	--appdir	Target location for Applications (default: /Applications)	v
o	--colorpickerdir	Target location for Color Pickers (default: ~/Library/ColorPickers)	v
o	--prefpanedir	Target location for Preference Panes (default: ~/Library/PreferencePanes)	v
o	--qlplugindir	Target location for QuickLook Plugins (default: ~/Library/QuickLook)	v
o	--mdimporterdir	Target location for Spotlight Plugins (default: ~/Library/Spotlight)	v
o	--dictionarydir	Target location for Dictionaries (default: ~/Library/Dictionaries)	v
o	--fontdir	Target location for Fonts (default: ~/Library/Fonts)	v
o	--servicedir	Target location for Services (default: ~/Library/Services)	v
o	--input-methoddir	Target location for Input Methods (default: ~/Library/Input Methods)	v
o	--internet-plugindir	Target location for Internet Plugins (default: ~/Library/Internet Plug-Ins)	v
o	--audio-unit-plugindir	Target location for Audio Unit Plugins (default: ~/Library/Audio/Plug-Ins/Components)	v
o	--vst-plugindir	Target location for VST Plugins (default: ~/Library/Audio/Plug-Ins/VST)	v
o	--vst3-plugindir	Target location for VST3 Plugins (default: ~/Library/Audio/Plug-Ins/VST3)	v
o	--screen-saverdir	Target location for Screen Savers (default: ~/Library/Screen Savers)	v
o	--language	Comma-separated list of language codes to prefer for cask installation. The first matching…	
a	1	1
=	install	--cc
v	gcc-7	
v	llvm_clang	
v	clang	
=	install	--appdir
t	folders
=	install	--colorpickerdir
t	folders
=	install	--prefpanedir
t	folders
=	install	--qlplugindir
t	folders
=	install	--mdimporterdir
t	folders
=	install	--dictionarydir
t	folders
=	install	--fontdir
t	folders
=	install	--servicedir
t	folders
=	install	--input-methoddir
t	folders
=	install	--internet-plugindir
t	folders
=	install	--audio-unit-plugindir
t	folders
=	install	--vst-plugindir
t	folders
=	install	--vst3-plugindir
t	folders
=	install	--screen-saverdir
t	folders
#	install	1
d
@	reinstall
o	-d|--debug	If brewing fails, open an interactive debugging session with access to IRB or a shell inside the…	
o	-f|--force	Install formulae without checking for previously installed keg-only or non-migrated versions. When…	
o	-v|--verbose	Print the verification and postinstall steps	
o	-s|--build-from-source	Compile formula from source even if a bottle is provided. Dependencies will still be installed…	
o	-i|--interactive	Download and patch formula	
o	-g|--git	Create a Git repository	
o	--formula	Treat all named arguments as formulae	
o	--force-bottle	Install from a bottle if it exists for the current or newest version of macOS, even if it would…	
o	--keep-tmp	Retain the temporary files created during installation	
o	--display-times	Print install times for each formula at the end of the run	
o	--cask	--casks Treat all named arguments as casks	
o	--binaries	Disable/enable linking of helper executables (default: enabled)	
o	--no-binaries	Disable/enable linking of helper executables (default: enabled)	
o	--require-sha	Require all casks to have a checksum	
o	--quarantine	Disable/enable quarantining of downloads (default: enabled)	
o	--no-quarantine	Disable/enable quarantining of downloads (default: enabled)	
o	--skip-cask-deps	Skip installing cask dependencies	
a	1	1
#	reinstall	1
d
@	uninstall
a	1	1
#	uninstall	1
d
@	--prefix
o	--unbrewed	List files in Homebrew's prefix not installed by Homebrew	
o	--installed	Outputs nothing and returns a failing status code if formula is not installed	
a	1	1
#	--prefix	1
d
@	cask
s	install	Installs the given cask
s	uninstall	Uninstalls the given cask
@	cask install
a	1	0
@	cask uninstall
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--zap	Remove all files associated with a cask. May remove files which are shared between applications	
o	--ignore-dependencies	Don't fail uninstall, even if formula is a dependency of any installed formulae	
o	--formula	Treat all named arguments as formulae	
o	--cask	Treat all named arguments as casks	
a	1	1
#	cask uninstall	1
d
@	cleanup
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--prune|--prune=all	Remove all cache files older than specified days	
o	-n|--dry-run	Show what would be removed, but do not actually remove anything	
o	-s	Scrub the cache, including downloads for even the latest versions	
o	--prune-prefix	Only prune the symlinks and directories from the prefix and remove no other files	
a	1	1
#	cleanup	1
d
@	services
s	cleanup	Remove all unused services
s	list	List all services
s	run	Run the service formula without registering to launch at login (or boot)
s	start	Start the service formula immediately and register it to launch at login
s	stop	Stop the service formula immediately and unregister it from launching at
s	restart	Stop (if necessary) and start the service formula immediately and register it to launch at login…
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--file	Use the plist file from this location to start or run the service	
o	--all	Run subcommand on all services	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Get help with services command	
@	services cleanup
@	services list
@	services run
o	--all	Start all services	
a	1	1
#	services run	1
d
@	services start
o	--all	Start all services	
a	1	1
#	services start	1
d
@	services stop
o	--all	Start all services	
a	1	1
#	services stop	1
d
@	services restart
o	--all	Start all services	
a	1	1
#	services restart	1
d
@	analytics
s	on	Turns on analytics
s	off	Turns off analytics
s	regenerate-uuid	Regenerate the UUID used for analytics
@	analytics on
@	analytics off
@	analytics regenerate-uuid
@	autoremove
o	-n|--dry-run	List what would be uninstalled, but do not actually uninstall anything	
@	tap
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--full	Convert a shallow clone to a full clone without untapping	
o	--shallow	Fetch tap as a shallow clone rather than a full clone	
o	--force-auto-update	Auto-update tap even if it is not hosted on GitHub	
o	--repair	Migrate tapped formulae from symlink-based to directory-based structure	
o	--list-pinned	List all pinned taps	
a	1	0
@	untap
o	-f|--force	Untap even if formulae or casks from this tap are currently installed	
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
a	1	0
#	untap	1
d
@	link
o	--overwrite	Delete files that already exist in the prefix while linking	
o	-n|--dry-run	List files which would be linked or deleted by brew link --overwrite without actually linking or…	
o	-f|--force	Allow keg-only formulae to be linked	
o	--HEAD	Link the HEAD version of the formula if it is installed	
a	1	1
#	link	1
d
@	unlink
o	-n|--dry-run	List files which would be unlinked without actually unlinking or deleting any files	
a	1	1
#	unlink	1
d
@	formulae
@	casks
@	edit
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--formula|--formulae	Treat all named arguments as formulae	
o	--cask|--casks	Treat all named arguments as casks	
a	1	1
#	edit	1
d
@	home
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
o	--formula|--formulae	Treat all named arguments as formulae	
o	--cask|--casks	Treat all named arguments as casks	
a	1	1
#	home	1
d
@	alias
o	--edit	Edit aliases in a text editor	
o	-d|--debug	Display any debugging information	
o	-q|--quiet	Make some output more quiet	
o	-v|--verbose	Make some output more verbose	
o	-h|--help	Show help message	
a	1	0
#	alias	1
d
@	developer
a	1	0
#	developer	1
v	on	
v	off	
