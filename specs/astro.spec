@	
s	add	Add an integration
s	build	Build your project and write it to disk
s	check	Check your project for errors
s	dev	Starts the development server
s	docs	Open documentation in your web browser
s	preview	Preview your build locally
s	sync	Generate content collection types
s	telemetry	Configure telemetry settings
o	--config	Specify your config file	vp
o	--root	Specify your project root folder	vp
o	--site	Specify your project site	vp
o	--base	Specify your project base	vp
o	--verbose	Enable verbose logging	p
o	--silent	Disable all logging	p
o	--version	Show the version number and exit	p
o	--help	Show help for astro	p
=		--config
t	filepaths
=		--root
t	folders
=		--base
t	folders
@	add
o	--yes	Accept all prompts	
a	1	0
@	build
o	--drafts	Include Markdown draft pages in the build	
@	check
o	--watch	Watch Astro files for changes and re-run checks	
@	dev
o	--port	Specify a port to listen on	v
o	--host	Listen on all addresses, including LAN and public addresses	V
o	--open	Automatically open the app in the browser on server start	
@	docs
@	preview
o	--open	Automatically open the app in the browser on server start	
@	sync
@	telemetry
s	enable	Enable anonymous data collection
s	disable	Disable anonymous data collection
s	reset	Reset anonymous data collection settings
@	telemetry enable
@	telemetry disable
@	telemetry reset
