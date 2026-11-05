@	
s	airdrop	Manage AirDrop
s	appearance	Manage appearance
s	battery	Manage battery
s	bluetooth	Manage Bluetooth
s	dir	Manage directories
s	disk	Manage disks
s	display	Manage displays
s	dns	Manage dns
s	dock	Manage dock
s	finder	Manage finder
s	firewall	Manage firewall
s	flightmode	Manage flight mode
s	gatekeeper	Manage gatekeeper
s	group	Manage groups
s	hostname	Manage hostname
s	info	Show system information
s	help	Show help
s	itunes	Manage iTunes
s	localhost	Manage localhost
s	lock	Lock session
s	network	Manage network
s	nosleep	Manage no sleep
s	notification	Manage notification
s	ntp	Manage ntp
s	printer	Manage printer
s	restart	Restart computer (needs confirmation)
s	safeboot	Manage safe boot
s	screensaver	Manage screensaver
s	service	Manage service
s	shutdown	Shutdown computer (needs confirmation)
s	sleep	Put computer to sleep
s	timezone	Get current timezone
s	touchbar	Manage touchbar
s	trash	Manage trash
s	user	Manage user
s	volume	Manage volume level
s	vpn	Manage VPN connections
s	wallpaper	Change wallpaper
s	wifi	Manage wifi
o	--update	Update m-cli to the latest version	
o	--uninstall	Uninstall m-cli	
@	airdrop
s	status	Show AirDrop status
s	on	Enable AirDrop
s	enable	Enable AirDrop
s	off	Disable AirDrop
s	disable	Disable AirDrop
s	help	Show help
@	airdrop status
@	airdrop on
@	airdrop enable
@	airdrop off
@	airdrop disable
@	airdrop help
@	appearance
s	darkmode	Manage dark mode
s	transparency	Manage transparency
s	antialiasthreshold	Manage antialiasing threshold
s	sidebariconsize	Manage sidebar icon size
s	maincolor	Manage main color
s	highlightcolor	Manage highlight color
s	help	Show help
@	appearance darkmode
a	1	0
#	appearance darkmode	1
v	YES	
v	NO	
@	appearance transparency
a	1	0
#	appearance transparency	1
v	YES	
v	NO	
@	appearance antialiasthreshold
a	1	0
@	appearance sidebariconsize
a	1	0
#	appearance sidebariconsize	1
v	small	
v	medium	
v	large	
@	appearance maincolor
a	1	0
#	appearance maincolor	1
v	blue	
v	graphite	
@	appearance highlightcolor
a	1	0
#	appearance highlightcolor	1
v	graphite	
v	cayenne	
v	asparagus	
v	clover	
v	teal	
v	midnight	
v	plum	
v	tin	
v	nickel	
v	mocha	
v	fern	
v	moss	
v	ocean	
v	eggplant	
v	maroon	
v	steel	
v	aluminum	
v	maraschino	
v	lemon	
v	spring	
v	turquoise	
v	blueberry	
v	magenta	
v	iron	
v	magnesium	
v	tangerine	
v	lime	
v	seafoam	
v	aqua	
v	grape	
v	strawberry	
v	tungsten	
v	silver	
v	salmon	
v	banana	
v	flora	
v	ice	
v	orchid	
v	bubblegum	
v	lead	
v	mercery	
v	cantaloupe	
v	honeydew	
v	spindrift	
v	sky	
v	lavender	
v	carnation	
v	licorice	
v	snow	
@	appearance help
@	battery
s	status	Show battery status
s	help	Show help
@	battery status
@	battery help
@	bluetooth
s	status	Show bluetooth status
s	on	Enable bluetooth
s	enable	Enable bluetooth
s	off	Disable bluetooth
s	disable	Disable bluetooth
s	help	Show help
@	bluetooth status
@	bluetooth on
@	bluetooth enable
@	bluetooth off
@	bluetooth disable
@	bluetooth help
@	dir
s	tree	Show tree view of folders in the current path
s	delete	Delete folders
s	dsfiles	Manage .DS_Store files
s	size	Calculate current folder size
s	help	Show help
@	dir tree
a	1	0
#	dir tree	1
t	folders
@	dir delete
s	empty	Delete empty folders recursively in the current path
s	dsfiles	Delete .DS_Store files recursively in the current path
@	dir delete empty
a	1	0
#	dir delete empty	1
t	folders
@	dir delete dsfiles
a	1	0
#	dir delete dsfiles	1
t	folders
@	dir dsfiles
s	on	Restore generation of .DS_Store
s	off	Prohibit generation of .DS_Store
@	dir dsfiles on
@	dir dsfiles off
@	dir size
a	1	0
#	dir size	1
t	folders
@	dir help
@	disk
s	ls|list	List disk partitions
s	info	Show disk information
s	ejectall	Eject all mountable volumes
s	verify	Verify disk
s	repair	Repair disk
s	format	Format disk
s	reformat	Reformat a volume
s	rename	Rename a volume
s	help	Show help
@	disk ls
a	1	0
#	disk ls	1
t	filepaths
d
@	disk info
a	1	0
#	disk info	1
t	filepaths
d
@	disk ejectall
@	disk verify
s	volume	Verify volume
s	disk	Verify disk
@	disk verify volume
a	1	0
#	disk verify volume	1
t	filepaths
d
@	disk verify disk
a	1	0
#	disk verify disk	1
t	filepaths
d
@	disk repair
s	volume	Repair volume
s	disk	Repair disk
@	disk repair volume
a	1	0
#	disk repair volume	1
t	filepaths
d
@	disk repair disk
a	1	0
#	disk repair disk	1
t	filepaths
d
@	disk format
s	MS-DOS	Format the entire disk with a windows format (MS-DOS)
s	volume	Format the volume with a windows format (MS-DOS)
@	disk format MS-DOS
a	2	0
#	disk format MS-DOS	2
t	filepaths
d
@	disk format volume
a	2	0
#	disk format volume	2
t	filepaths
d
@	disk reformat
a	1	0
#	disk reformat	1
t	filepaths
d
@	disk rename
a	2	0
#	disk rename	1
t	filepaths
d
@	disk help
@	display
s	status	Show display status
s	help	Show usage
s	up	Turn up the brightness
s	down	Turn down the brightness
@	display status
@	display help
@	display up
@	display down
@	dns
s	flush	Flush local DNS cache
s	help	Show help
@	dns flush
@	dns help
@	dock
s	showdelay	Changes how long the Dock takes to show up when auto-hide is enabled
s	autohide	Enable or disable Dock's auto hide feature
s	autohidedelay	Changes how long it takes to detect you want to show up the dock
s	magnification	Turn magnification on or off
s	position	Change Dock's position
s	addblankspace	Add a blank space (separator) to the Dock
s	addrecentitems	Add a stack containg your recent items to the Dock
s	prune	Remove all items from dock
s	help	Show help
@	dock showdelay
a	1	0
@	dock autohide
a	1	0
#	dock autohide	1
v	YES	
v	NO	
@	dock autohidedelay
a	1	0
@	dock magnification
a	1	0
#	dock magnification	1
v	YES	
v	NO	
@	dock position
a	1	0
#	dock position	1
v	BOTTOM	
v	LEFT	
v	RIGHT	
@	dock addblankspace
@	dock addrecentitems
@	dock prune
@	dock help
@	finder
s	showhiddenfiles	Show hidden files Status
s	showextensions	Show all file extensions Status
s	showdesktop	Show the desktop Status
s	showpath	Show the current opened folder path on the top bar of the Finder window
s	help	Show help
@	finder showhiddenfiles
a	1	0
#	finder showhiddenfiles	1
v	YES	
v	NO	
@	finder showextensions
a	1	0
#	finder showextensions	1
v	YES	
v	NO	
@	finder showdesktop
a	1	0
#	finder showdesktop	1
v	YES	
v	NO	
@	finder showpath
a	1	0
#	finder showpath	1
v	YES	
v	NO	
@	finder help
@	firewall
s	status	Show status
s	enable	Enable firewall
s	disable	Disable firewall
s	list	List applications handled by firewall
s	add	Add app to firewall
s	remove	Remove app from firewall
s	help	Show help
@	firewall status
@	firewall enable
@	firewall disable
@	firewall list
@	firewall add
a	1	0
#	firewall add	1
t	filepaths
@	firewall remove
a	1	0
@	firewall help
@	flightmode
s	off	Turn flight mode off
s	on	Turn flight mode on
s	help	Show help
@	flightmode off
@	flightmode on
@	flightmode help
@	gatekeeper
s	status	Show status
s	enable	Enable gatekeeper
s	disable	Disable gatekeeper
s	list	List rules
s	create	Create a rule for the application
s	help	Show help
@	gatekeeper status
@	gatekeeper enable
a	1	0
@	gatekeeper disable
a	1	0
@	gatekeeper list
@	gatekeeper create
a	2	0
@	gatekeeper help
@	group
s	list	List groups
s	info	Get group information
s	adduser	Add user to group
s	removeuser	Remove user from group
s	ismember	Check if user is a member of group
s	help	Show help
@	group list
@	group info
a	1	0
@	group adduser
a	2	0
#	group adduser	1
d
#	group adduser	2
d
@	group removeuser
a	2	0
#	group removeuser	1
d
#	group removeuser	2
d
@	group ismember
a	2	0
#	group ismember	1
d
#	group ismember	2
d
@	group help
@	hostname
s	newhostname	Set new hostname
s	help	Show help
@	hostname newhostname
@	hostname help
@	info
@	help
@	itunes
s	status	Show status
s	play	Play track
s	pause	Pause track
s	next	Play next track
s	prev	Play previous track
s	mute	Mute iTunes
s	unmute	Unmute iTunes
s	vol	Volume
s	stop	Stop track
s	quit	Quit iTunes
s	help	Show help
@	itunes status
@	itunes play
@	itunes pause
@	itunes next
@	itunes prev
@	itunes mute
@	itunes unmute
@	itunes vol
a	1	0
#	itunes vol	1
v	up	
v	down	
@	itunes stop
@	itunes quit
@	itunes help
@	localhost
s	ls|list	List current records in localhost
s	add	Add a new host to the localhost file
s	remove	Remove a host from the localhost file
s	help	Show help
@	localhost ls
@	localhost add
a	2	0
@	localhost remove
a	1	0
@	localhost help
@	lock
@	network
s	ls|list	List network interfaces
s	location	Manage location
s	help	Show help
@	network ls
@	network location
s	ls|list	List locations
s	create	Create a location
s	delete	Delete a location
s	switch	Switch location
@	network location ls
@	network location create
a	1	0
@	network location delete
a	1	0
#	network location delete	1
g	bash -c 'm network location list | tail -n +2'	\n
@	network location switch
a	1	0
@	network help
@	nosleep
s	until	No sleep until
s	help	Show help
@	nosleep until
s	pid	No sleep until process id ends
a	1	0
#	nosleep until	1
t	filepaths
@	nosleep until pid
a	1	0
#	nosleep until pid	1
d
@	nosleep help
@	notification
s	showcenter	Show notification center
s	help	Show help
@	notification showcenter
a	1	0
#	notification showcenter	1
v	YES	
v	NO	
@	notification help
@	ntp
s	status	Status of the network time service
s	enable	Enable clock to use network time
s	disable	Disable clock to use network time
s	set	Set network time server
s	help	Show help
@	ntp status
@	ntp enable
@	ntp disable
@	ntp set
a	1	0
@	ntp help
@	printer
s	settings	Printer settings
s	name	Display printer names on system
s	queue	Display items in printer queue on system
s	drivers	Display all printer drivers
s	web	Enable and show web interface
s	help	Show help
@	printer settings
@	printer name
@	printer queue
@	printer drivers
@	printer web
@	printer help
@	restart
s	-f|--force	Restart computer (without confirmation)
s	help	Show help
@	restart -f
@	restart help
@	safeboot
s	status	Get the boot args
s	enable	Enable safe boot
s	disable	Disable safeboot
s	help	Show help
@	safeboot status
@	safeboot enable
@	safeboot disable
@	safeboot help
@	screensaver
s	status	Get the current status
s	askforpassword	Get password requirement to unlock
s	help	Show help
@	screensaver status
@	screensaver askforpassword
a	1	0
#	screensaver askforpassword	1
v	YES	
v	NO	
@	screensaver help
@	service
s	--status-all	List all services
s	--ls|--list	List all services
s	start	Start a service
s	stop	Stop a service
s	load	Load a service
s	unload	Unload a service
s	help	Show help
@	service --status-all
@	service --ls
a	1	0
@	service start
a	1	0
#	service start	1
g	bash -c 'launchctl list | awk '\''{ print $3 }'\'''	\n
@	service stop
a	1	0
#	service stop	1
g	bash -c 'launchctl list | awk '\''{ print $3 }'\'''	\n
@	service load
a	1	0
#	service load	1
g	bash -c 'launchctl list | awk '\''{ print $3 }'\'''	\n
@	service unload
a	1	0
#	service unload	1
g	bash -c 'launchctl list | awk '\''{ print $3 }'\'''	\n
@	service help
@	shutdown
s	-f	Shutdown computer (without confirmation)
s	help	Show help
@	shutdown -f
@	shutdown help
@	sleep
s	help	Show help
@	sleep help
@	timezone
s	ls|list	List available timezones
s	set	Set timezone
s	help	Show help
@	timezone ls
@	timezone set
a	1	0
#	timezone set	1
v	Africa/Abidjan	
v	Africa/Accra	
v	Africa/Addis_Ababa	
v	Africa/Algiers	
v	Africa/Asmara	
v	Africa/Bamako	
v	Africa/Bangui	
v	Africa/Banjul	
v	Africa/Bissau	
v	Africa/Blantyre	
v	Africa/Brazzaville	
v	Africa/Bujumbura	
v	Africa/Cairo	
v	Africa/Casablanca	
v	Africa/Ceuta	
v	Africa/Conakry	
v	Africa/Dakar	
v	Africa/Dar_es_Salaam	
v	Africa/Djibouti	
v	Africa/Douala	
v	Africa/El_Aaiun	
v	Africa/Freetown	
v	Africa/Gaborone	
v	Africa/Harare	
v	Africa/Johannesburg	
v	Africa/Juba	
v	Africa/Kampala	
v	Africa/Khartoum	
v	Africa/Kigali	
v	Africa/Kinshasa	
v	Africa/Lagos	
v	Africa/Libreville	
v	Africa/Lome	
v	Africa/Luanda	
v	Africa/Lubumbashi	
v	Africa/Lusaka	
v	Africa/Malabo	
v	Africa/Maputo	
v	Africa/Maseru	
v	Africa/Mbabane	
v	Africa/Mogadishu	
v	Africa/Monrovia	
v	Africa/Nairobi	
v	Africa/Ndjamena	
v	Africa/Niamey	
v	Africa/Nouakchott	
v	Africa/Ouagadougou	
v	Africa/Porto-Novo	
v	Africa/Sao_Tome	
v	Africa/Tripoli	
v	Africa/Tunis	
v	Africa/Windhoek	
v	America/Adak	
v	America/Anchorage	
v	America/Anguilla	
v	America/Antigua	
v	America/Araguaina	
v	America/Argentina/Buenos_Aires	
v	America/Argentina/Catamarca	
v	America/Argentina/Cordoba	
v	America/Argentina/Jujuy	
v	America/Argentina/La_Rioja	
v	America/Argentina/Mendoza	
v	America/Argentina/Rio_Gallegos	
v	America/Argentina/Salta	
v	America/Argentina/San_Juan	
v	America/Argentina/San_Luis	
v	America/Argentina/Tucuman	
v	America/Argentina/Ushuaia	
v	America/Aruba	
v	America/Asuncion	
v	America/Atikokan	
v	America/Bahia	
v	America/Bahia_Banderas	
v	America/Barbados	
v	America/Belem	
v	America/Belize	
v	America/Blanc-Sablon	
v	America/Boa_Vista	
v	America/Bogota	
v	America/Boise	
v	America/Cambridge_Bay	
v	America/Campo_Grande	
v	America/Cancun	
v	America/Caracas	
v	America/Cayenne	
v	America/Cayman	
v	America/Chicago	
v	America/Chihuahua	
v	America/Costa_Rica	
v	America/Creston	
v	America/Cuiaba	
v	America/Curacao	
v	America/Danmarkshavn	
v	America/Dawson	
v	America/Dawson_Creek	
v	America/Denver	
v	America/Detroit	
v	America/Dominica	
v	America/Edmonton	
v	America/Eirunepe	
v	America/El_Salvador	
v	America/Fort_Nelson	
v	America/Fortaleza	
v	America/Glace_Bay	
v	America/Godthab	
v	America/Goose_Bay	
v	America/Grand_Turk	
v	America/Grenada	
v	America/Guadeloupe	
v	America/Guatemala	
v	America/Guayaquil	
v	America/Guyana	
v	America/Halifax	
v	America/Havana	
v	America/Hermosillo	
v	America/Indiana/Indianapolis	
v	America/Indiana/Knox	
v	America/Indiana/Marengo	
v	America/Indiana/Petersburg	
v	America/Indiana/Tell_City	
v	America/Indiana/Vevay	
v	America/Indiana/Vincennes	
v	America/Indiana/Winamac	
v	America/Inuvik	
v	America/Iqaluit	
v	America/Jamaica	
v	America/Juneau	
v	America/Kentucky/Louisville	
v	America/Kentucky/Monticello	
v	America/Kralendijk	
v	America/La_Paz	
v	America/Lima	
v	America/Los_Angeles	
v	America/Lower_Princes	
v	America/Maceio	
v	America/Managua	
v	America/Manaus	
v	America/Marigot	
v	America/Martinique	
v	America/Matamoros	
v	America/Mazatlan	
v	America/Menominee	
v	America/Merida	
v	America/Metlakatla	
v	America/Mexico_City	
v	America/Miquelon	
v	America/Moncton	
v	America/Monterrey	
v	America/Montevideo	
v	America/Montreal	
v	America/Montserrat	
v	America/Nassau	
v	America/New_York	
v	America/Nipigon	
v	America/Nome	
v	America/Noronha	
v	America/North_Dakota/Beulah	
v	America/North_Dakota/Center	
v	America/North_Dakota/New_Salem	
v	America/Nuuk	
v	America/Ojinaga	
v	America/Panama	
v	America/Pangnirtung	
v	America/Paramaribo	
v	America/Phoenix	
v	America/Port-au-Prince	
v	America/Port_of_Spain	
v	America/Porto_Velho	
v	America/Puerto_Rico	
v	America/Punta_Arenas	
v	America/Rainy_River	
v	America/Rankin_Inlet	
v	America/Recife	
v	America/Regina	
v	America/Resolute	
v	America/Rio_Branco	
v	America/Santa_Isabel	
v	America/Santarem	
v	America/Santiago	
v	America/Santo_Domingo	
v	America/Sao_Paulo	
v	America/Scoresbysund	
v	America/Shiprock	
v	America/Sitka	
v	America/St_Barthelemy	
v	America/St_Johns	
v	America/St_Kitts	
v	America/St_Lucia	
v	America/St_Thomas	
v	America/St_Vincent	
v	America/Swift_Current	
v	America/Tegucigalpa	
v	America/Thule	
v	America/Thunder_Bay	
v	America/Tijuana	
v	America/Toronto	
v	America/Tortola	
v	America/Vancouver	
v	America/Whitehorse	
v	America/Winnipeg	
v	America/Yakutat	
v	America/Yellowknife	
v	Antarctica/Casey	
v	Antarctica/Davis	
v	Antarctica/DumontDUrville	
v	Antarctica/Macquarie	
v	Antarctica/Mawson	
v	Antarctica/McMurdo	
v	Antarctica/Palmer	
v	Antarctica/Rothera	
v	Antarctica/South_Pole	
v	Antarctica/Syowa	
v	Antarctica/Troll	
v	Antarctica/Vostok	
v	Arctic/Longyearbyen	
v	Asia/Aden	
v	Asia/Almaty	
v	Asia/Amman	
v	Asia/Anadyr	
v	Asia/Aqtau	
v	Asia/Aqtobe	
v	Asia/Ashgabat	
v	Asia/Atyrau	
v	Asia/Baghdad	
v	Asia/Bahrain	
v	Asia/Baku	
v	Asia/Bangkok	
v	Asia/Barnaul	
v	Asia/Beirut	
v	Asia/Bishkek	
v	Asia/Brunei	
v	Asia/Calcutta	
v	Asia/Chita	
v	Asia/Choibalsan	
v	Asia/Chongqing	
v	Asia/Colombo	
v	Asia/Damascus	
v	Asia/Dhaka	
v	Asia/Dili	
v	Asia/Dubai	
v	Asia/Dushanbe	
v	Asia/Famagusta	
v	Asia/Gaza	
v	Asia/Harbin	
v	Asia/Hebron	
v	Asia/Ho_Chi_Minh	
v	Asia/Hong_Kong	
v	Asia/Hovd	
v	Asia/Irkutsk	
v	Asia/Jakarta	
v	Asia/Jayapura	
v	Asia/Jerusalem	
v	Asia/Kabul	
v	Asia/Kamchatka	
v	Asia/Karachi	
v	Asia/Kashgar	
v	Asia/Kathmandu	
v	Asia/Katmandu	
v	Asia/Khandyga	
v	Asia/Krasnoyarsk	
v	Asia/Kuala_Lumpur	
v	Asia/Kuching	
v	Asia/Kuwait	
v	Asia/Macau	
v	Asia/Magadan	
v	Asia/Makassar	
v	Asia/Manila	
v	Asia/Muscat	
v	Asia/Nicosia	
v	Asia/Novokuznetsk	
v	Asia/Novosibirsk	
v	Asia/Omsk	
v	Asia/Oral	
v	Asia/Phnom_Penh	
v	Asia/Pontianak	
v	Asia/Pyongyang	
v	Asia/Qatar	
v	Asia/Qostanay	
v	Asia/Qyzylorda	
v	Asia/Rangoon	
v	Asia/Riyadh	
v	Asia/Sakhalin	
v	Asia/Samarkand	
v	Asia/Seoul	
v	Asia/Shanghai	
v	Asia/Singapore	
v	Asia/Srednekolymsk	
v	Asia/Taipei	
v	Asia/Tashkent	
v	Asia/Tbilisi	
v	Asia/Tehran	
v	Asia/Thimphu	
v	Asia/Tokyo	
v	Asia/Tomsk	
v	Asia/Ulaanbaatar	
v	Asia/Urumqi	
v	Asia/Ust-Nera	
v	Asia/Vientiane	
v	Asia/Vladivostok	
v	Asia/Yakutsk	
v	Asia/Yangon	
v	Asia/Yekaterinburg	
v	Asia/Yerevan	
v	Atlantic/Azores	
v	Atlantic/Bermuda	
v	Atlantic/Canary	
v	Atlantic/Cape_Verde	
v	Atlantic/Faroe	
v	Atlantic/Madeira	
v	Atlantic/Reykjavik	
v	Atlantic/South_Georgia	
v	Atlantic/St_Helena	
v	Atlantic/Stanley	
v	Australia/Adelaide	
v	Australia/Brisbane	
v	Australia/Broken_Hill	
v	Australia/Currie	
v	Australia/Darwin	
v	Australia/Eucla	
v	Australia/Hobart	
v	Australia/Lindeman	
v	Australia/Lord_Howe	
v	Australia/Melbourne	
v	Australia/Perth	
v	Australia/Sydney	
v	Europe/Amsterdam	
v	Europe/Andorra	
v	Europe/Astrakhan	
v	Europe/Athens	
v	Europe/Belgrade	
v	Europe/Berlin	
v	Europe/Bratislava	
v	Europe/Brussels	
v	Europe/Bucharest	
v	Europe/Budapest	
v	Europe/Busingen	
v	Europe/Chisinau	
v	Europe/Copenhagen	
v	Europe/Dublin	
v	Europe/Gibraltar	
v	Europe/Guernsey	
v	Europe/Helsinki	
v	Europe/Isle_of_Man	
v	Europe/Istanbul	
v	Europe/Jersey	
v	Europe/Kaliningrad	
v	Europe/Kiev	
v	Europe/Kirov	
v	Europe/Kyiv	
v	Europe/Lisbon	
v	Europe/Ljubljana	
v	Europe/London	
v	Europe/Luxembourg	
v	Europe/Madrid	
v	Europe/Malta	
v	Europe/Mariehamn	
v	Europe/Minsk	
v	Europe/Monaco	
v	Europe/Moscow	
v	Europe/Oslo	
v	Europe/Paris	
v	Europe/Podgorica	
v	Europe/Prague	
v	Europe/Riga	
v	Europe/Rome	
v	Europe/Samara	
v	Europe/San_Marino	
v	Europe/Sarajevo	
v	Europe/Saratov	
v	Europe/Simferopol	
v	Europe/Skopje	
v	Europe/Sofia	
v	Europe/Stockholm	
v	Europe/Tallinn	
v	Europe/Tirane	
v	Europe/Ulyanovsk	
v	Europe/Uzhgorod	
v	Europe/Vaduz	
v	Europe/Vatican	
v	Europe/Vienna	
v	Europe/Vilnius	
v	Europe/Volgograd	
v	Europe/Warsaw	
v	Europe/Zagreb	
v	Europe/Zaporozhye	
v	Europe/Zurich	
v	GMT	
v	Indian/Antananarivo	
v	Indian/Chagos	
v	Indian/Christmas	
v	Indian/Cocos	
v	Indian/Comoro	
v	Indian/Kerguelen	
v	Indian/Mahe	
v	Indian/Maldives	
v	Indian/Mauritius	
v	Indian/Mayotte	
v	Indian/Reunion	
v	Pacific/Apia	
v	Pacific/Auckland	
v	Pacific/Bougainville	
v	Pacific/Chatham	
v	Pacific/Chuuk	
v	Pacific/Easter	
v	Pacific/Efate	
v	Pacific/Enderbury	
v	Pacific/Fakaofo	
v	Pacific/Fiji	
v	Pacific/Funafuti	
v	Pacific/Galapagos	
v	Pacific/Gambier	
v	Pacific/Guadalcanal	
v	Pacific/Guam	
v	Pacific/Honolulu	
v	Pacific/Johnston	
v	Pacific/Kanton	
v	Pacific/Kiritimati	
v	Pacific/Kosrae	
v	Pacific/Kwajalein	
v	Pacific/Majuro	
v	Pacific/Marquesas	
v	Pacific/Midway	
v	Pacific/Nauru	
v	Pacific/Niue	
v	Pacific/Norfolk	
v	Pacific/Noumea	
v	Pacific/Pago_Pago	
v	Pacific/Palau	
v	Pacific/Pitcairn	
v	Pacific/Pohnpei	
v	Pacific/Ponape	
v	Pacific/Port_Moresby	
v	Pacific/Rarotonga	
v	Pacific/Saipan	
v	Pacific/Tahiti	
v	Pacific/Tarawa	
v	Pacific/Tongatapu	
v	Pacific/Truk	
v	Pacific/Wake	
v	Pacific/Wallis	
@	timezone help
@	touchbar
s	reset	Reset touchbar
s	help	Show help
@	touchbar reset
@	touchbar help
@	trash
s	status	Get trash info
s	clean	Clean trash
s	help	Show help
@	trash status
@	trash clean
@	trash help
@	user
s	ls|list	List all users
s	info	Get user info
s	create	Create a new user
s	delete	Delete a user
s	help	Show help
@	user ls
@	user info
a	1	0
#	user info	1
d
@	user create
@	user delete
a	1	0
#	user delete	1
d
@	user help
@	volume
s	mute	Set mute
s	unmute	Unset mute
s	ismute	Check the volume status
s	up	Increase the volume by 6.25
s	down	Decrease the volume by 6.25
s	help	Show help
a	1	0
@	volume mute
@	volume unmute
@	volume ismute
@	volume up
@	volume down
@	volume help
@	vpn
s	ls|list	List VPN connections
s	start	Start a VPN connection
s	stop	Stop a VPN connection
s	status	Get the status of a VPN connection
s	help	Show help
@	vpn ls
@	vpn start
a	4	0
@	vpn stop
a	1	0
@	vpn status
a	1	0
@	vpn help
@	wallpaper
s	help	Show help
a	1	0
#	wallpaper	1
t	filepaths
@	wallpaper help
@	wifi
s	status	Get wifi status
s	scan	Scan wifi
s	showpassword	Show wifi network password
s	ls|list	List known wifi networks
s	forget	Forget a wifi network
s	history	Wifi connection history
s	off	Turn off your wifi
s	on	Turn on your wifi
s	connect	Join a wifi network
s	help	Show help
@	wifi status
@	wifi scan
@	wifi showpassword
a	1	0
#	wifi showpassword	1
d
@	wifi ls
@	wifi forget
a	1	0
#	wifi forget	1
d
@	wifi history
@	wifi off
@	wifi on
@	wifi connect
a	2	0
@	wifi help
