@	
o	--display	Specify an X display to use	v
o	--sync	Make X calls synchronous	
o	--g-fatal-warnings	Make all warnings fatal	
o	-h|--help	Print help message and exit	
o	-v|--version	Print version information and exit	
o	--full-version	Print full version information and exit	
o	-P	Specify profile to use	v
o	--profile	Specify profile to use by folder	v
o	--migration	Start with migration wizard	
o	--ProfileManager	Start with ProfileManager	
o	--no-remote	Do not accept or send remote commands; implies --new-instance	
o	--new-instance	Open new instance, not a new window in running instance	
o	--safe-mode	Disables extensions and themes for this session	
o	--allow-downgrade	Allows downgrading a profile	
o	--MOZ_LOG	Treated as MOZ_LOG=<modules> environment variable, overrides it	v
o	--MOZ_LOG_FILE	Treated as MOZ_LOG_FILE=<file> environment variable, overrides it. If MOZ_LOG_FILE is not…	v
o	--headless	Run without a GUI	
o	--jsdebugger	Open the Browser Toolbox. Defaults to the local build but can be overridden by a firefox path	V
o	--wait-for-jsdebugger	Spin event loop until JS debugger connects; enables debugging (some) application startup code paths	
o	--start-debugger-server	Start the devtools server on a TCP port or Unix domain socket path	v
o	--browser	Open a browser window	
o	--new-window	Open a URL in a new window	v
o	--new-tab	Open a URL in a new tab	v
o	--private-window	Open a URL in a new private window	v
o	--preferences	Open the preferences dialog	
o	--screenshot	Take a screenshot	V
o	--window-size	Size of your screenshot	v
o	--search	Search for a term in your default search engine	v
o	--setDefaultBrowser	Set Firefox as the default browser	
o	--first-startup	Run post-install actions before opening a new window	
o	--kiosk	Start the browser in kiosk mode	
o	--disable-pinch	Disable touch-screen and touch-pad pinch gestures	
o	--jsconsole	Open the Browser Console	
o	--devtools	Open DevTools on initial load	
o	--marionette	Enable remote debugging server	
o	--remote-debugging-port	Start the Firefox Remote Agent, which is a low-level remote debugging interface used for WebDriver	V
o	--allow-remote-hosts	Values of the Host header to allow for incoming requests	v
o	--allow-remote-origins	Values of the Origin header to allow for incoming requests	v
a	1	0
=		--profile
t	folders
=		--MOZ_LOG_FILE
t	filepaths
=		--jsdebugger
t	folders
=		--start-debugger-server
t	filepaths
d
=		--screenshot
t	folders
