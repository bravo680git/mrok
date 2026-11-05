@	
o	-h|--help	Help ('-H' for extended help)	
o	--viewport	Set the viewport size. If -f is also supplied, will attempt to set the video mode to this also…	v
o	-f	Fullscreen	
o	--screen	Set the number of the screen to display on	v
o	--high-dpi	Request a high DPI display when creating the window. On some platforms such as MacOS, the window…	
o	--window-position	Initial window position on your desktop which may be made up of multiple monitors. This will…	v
o	--frameless	Frameless window	
o	--transparent	Make the background transparent. Only really useful for screenshots	
o	--start-date	Start with the first entry after the supplied date and optional time. If a time zone offset isn't…	v
o	--stop-date	Stop at the last entry prior to the supplied date and optional time. Uses the same format as…	v
o	-p|--start-position	Begin at some position in the log (between 0.0 and 1.0 or 'random')	v
o	--stop-position	Stop (exit) at some position in the log (does not work with STDIN)	v
o	-t|--stop-at-time	Stop (exit) after a specified number of seconds	v
o	--stop-at-end	Stop (exit) at the end of the log / stream	
o	--loop	Loop back to the start of the log when the end is reached	
o	--loop-delay-seconds	Seconds to delay before looping	v
o	-a|--auto-skip-seconds	Automatically skip to next entry if nothing happens for a specified number of seconds	v
o	-s|--seconds-per-day	Speed of simulation in seconds per day	v
o	--realtime	Realtime playback speed	
o	--no-time-travel	Use the time of the last commit if the time of a commit is in the past	
o	-c|--time-scale	Change simulation time scale	
o	-i|--file-idle-time	Time in seconds files remain idle before they are removed or 0 for no limit	
o	--file-idle-time-at-end	Time in seconds files remain idle at the end before they are removed	v
o	-e|--elasticity	Elasticity of nodes	v
o	-b|--background-colour	Background colour in hex	v
o	--background-image	Set a background image	v
o	--title	Set a title	v
o	--font-file	Specify the font. Should work with most font file formats supported by FreeType, such as TTF and…	v
o	--font-scale	Scale the size of all fonts	v
o	--font-size	Font size used by the date and title	v
o	--file-font-size	Font size of filenames	v
o	--dir-font-size	Font size of directory names	v
o	--user-font-size	Font size of user names	v
o	--font-colour	Font colour used by the date and title in hex	v
o	--key	Show file extension key	
o	--logo	Logo to display in the foreground	v
o	--logo-offset	Offset position of the logo	v
o	--date-format	Specify display date string (strftime format)	v
o	--log-command	Show the log command used by gource (git,svn,hg,bzr,cvs2cl)	v
o	--log-format	Specify format of the log being read (git,svn,hg,bzr,cvs2cl,custom). Required when reading from…	v
o	--git-branch	Get the git log of a branch other than the current one	v
o	--follow-user	Have the camera automatically follow a particular user	v
o	--highlight-dirs	Highlight the names of all directories	
o	--highlight-user	Highlight the names of a particular user	v
o	--highlight-users	Highlight the names of all users	
o	--highlight-colour	Font colour for highlighted users in hex	v
o	--selection-colour	Font colour for selected users and files	v
o	--filename-colour	Font colour for filenames	v
o	--dir-colour	Font colour for directories	v
o	--dir-name-depth	Draw names of directories down to a specific depth in the tree	v
o	--dir-name-position	Position along edge of the directory name (between 0.1 and 1.0, default is 0.5)	v
o	--filename-time	Duration to keep filenames on screen (>= 2.0)	v
o	--file-extensions	Show filename extensions only	
o	--file-extension-fallback	Use filename as extension if the extension is missing or empty	
o	--file-filter	Filter out file paths matching the specified regular expression	v
o	--file-show-filter	Show only file paths matching the specified regular expression	v
o	--user-filter	Filter usernames matching the specified regular expression	v
o	--user-show-filter	Show only usernames matching the specified regular expression	v
o	--user-image-dir	Directory containing .jpg or .png images of users (eg 'Full Name.png') to use as avatars	v
o	--default-user-image	Path of .jpg to use as the default user image	v
o	--fixed-user-size	Forces the size of the user image to remain fixed throughout	
o	--colour-images	Colourize user images	
o	--crop	Crop view on an axis (vertical,horizontal)	v
o	--padding	Camera view padding	v
o	--multi-sampling	Enable multi-sampling	
o	--no-vsync	Disable vsync	
o	--bloom-multiplier	Adjust the amount of bloom	v
o	--bloom-intensity	Adjust the intensity of the bloom	v
o	--max-files	Set the maximum number of files or 0 for no limit. Excess files will be discarded	v
o	--max-file-lag	Max time files of a commit can take to appear. Use -1 for no limit	v
o	--max-user-speed	Max speed users can travel per second	v
o	--user-friction	Time users take to come to a halt	v
o	--user-scale	Change scale of user avatars	v
o	--camera-mode	Camera mode (overview,track)	v
o	--disable-auto-rotate	Disable automatic camera rotation	
o	--disable-input	Disable keyboard and mouse input	
o	--hide	Hide one or more display elements from the list below: bloom - bloom effect date - current date…	v
o	--hash-seed	Change the seed of hash function	v
o	--caption-file	Caption file (see Caption Log Format)	v
o	--caption-size	Caption size	v
o	--caption-colour	Caption colour in hex	v
o	--caption-duration	Caption duration	v
o	--caption-offset	Caption horizontal offset (0 to centre captions)	v
o	-o|--output-ppm-stream	Output a PPM image stream to a file ('-' for STDOUT). This will automatically hide the progress…	v
o	-r|--output-framerate	Framerate of output (25,30,60). Used with --output-ppm-stream	v
o	--output-custom-log	Output a custom format log file ('-' for STDOUT)	v
o	--load-config	Load a config file	v
o	--save-config	Save a config file with the current options	v
o	--path	Either a supported version control directory, a pre-generated log file (see log commands or the…	v
=		--viewport
v	3840x2160	
v	2560x1440	
v	1920x1080	
v	1280x720	
v	800x600	
=		--screen
d
=		-p
v	random	
v	0.0	
v	0.1	
v	0.2	
v	0.3	
v	0.4	
v	0.5	
v	0.6	
v	0.7	
v	0.8	
v	0.9	
v	1.0	
=		--stop-position
v	random	
v	0.0	
v	0.1	
v	0.2	
v	0.3	
v	0.4	
v	0.5	
v	0.6	
v	0.7	
v	0.8	
v	0.9	
v	1.0	
=		--background-image
t	filepaths
=		--font-file
t	filepaths
=		--logo
t	filepaths
=		--log-command
v	git	
v	svn	
v	hg	
v	bzr	
v	cvs2cl	
=		--log-format
v	git	
v	svn	
v	hg	
v	bzr	
v	cvs2cl	
v	custom	
=		--dir-name-position
v	0.1	
v	0.2	
v	0.3	
v	0.4	
v	0.5	
v	0.6	
v	0.7	
v	0.8	
v	0.9	
v	1.0	
=		--user-image-dir
t	folders
=		--default-user-image
t	filepaths
=		--camera-mode
v	overview	
v	track	
=		--hide
v	bloom	
v	date	
v	dirnames	
v	files	
v	filenames	
v	mouse	
v	progress	
v	root	
v	tree	
v	users	
v	usernames	
=		--caption-file
t	filepaths
=		-o
t	filepaths
=		-r
v	25	
v	30	
v	60	
v	120	
=		--output-custom-log
t	filepaths
=		--load-config
t	filepaths
=		--save-config
t	filepaths
=		--path
t	filepaths
