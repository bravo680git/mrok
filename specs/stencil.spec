@	
s	build	Build components for development or production
s	test	Run unit and end-to-end tests
s	generate|g	Bootstrap components
s	telemetry	Opt in or out of telemetry
o	--help	Display the help output explaining the different flags	
o	--version	Prints the current Stencil version	
@	build
o	--ci	Run a build using recommended settings for a Continuous Integration (CI) environment	
o	--config|-c	Set stencil config file	v
o	--debug	Set the log level to debug	
o	--dev	Development build	
o	--docs-readme	Generate component readme.md docs	
o	--es5	Creates an ES5 compatible build	
o	--log	Write stencil-build.log file	
o	--prerender	Prerender the application	
o	--prod	Runs a production build	
o	--max-workers	Max number of workers the compiler should use	v
o	--next	Opt-in to test the 'next' Stencil compiler features	
o	--no-cache	Disables using the cache	
o	--no-open	Do not automatically open the browser window	
o	--port|--p	Port for the Integrated Dev Server	v
o	--serve	Start the dev-server	
o	--stats	Write stencil-stats.json file	
o	--verbose	Logs additional information about each step of the build	
o	--watch	Rebuild when files update	
=	build	--config
t	filepaths
@	test
o	--spec	Run unit tests with Jest	
o	--e2e	Run e2e tests with Puppeteer	
o	--no-build	Skips build process before running the tests	
@	generate
a	1	1
@	telemetry
a	1	0
#	telemetry	1
v	off	Disable sharing anonymous usage data
v	on	Enable sharing anonymous usage data
