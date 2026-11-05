@	
s	install	Install homebridge as a service
s	uninstall	Remove the homebridge service
s	start	Start the homebridge service
s	stop	Stop the homebridge service
s	restart	Restart the homebridge service
s	rebuild	Rebuild UI
s	run	Run homebridge daemon
s	logs	Tails the homebridge service logs
s	update-node	Update Node.js
o	--help|-h	Display help for command	
o	--version|-v	Output the version number	
o	--service-name|-S	The name of the homebridge service to install or control	vp
o	--port	The port to set to the Homebridge UI when installing as a service	vp
o	--user	The user account the Homebridge service will be installed as (Linux, macOS only)	vp
o	--plugin-path|-P		vp
o	--user-storage-path|-U		vp
o	--no-timestamp|-T		p
o	--gid		vp
o	--uid		vp
o	--docker		p
o	--allow-root		p
o	--stdout		p
o	--strict-plugin-resolution		p
@	install
@	uninstall
@	start
@	stop
@	restart
@	rebuild
o	--all	Rebuild all npm modules (use after updating Node.js)	
@	run
@	logs
@	update-node
a	1	0
