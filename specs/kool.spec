@	
s	create	Create a new project using a preset
s	deploy	Deploy a local application to a Kool Cloud environment
s	docker	Create a new container (a powered up 'docker run')
s	exec	Execute a command inside a running service container
s	info	Print out information about the local environment
s	logs	Display log output from running service containers
s	preset	Install configuration files customized for Kool in the current directory
s	recipe	Adds configuration for some recipe in the current work directory
s	restart	Restart running service containers (the same as 'kool stop' followed by 'kool start')
s	run	Execute a script defined in kool.yml
s	self-update	Update kool to the latest version
s	share	Live share your local environment on the Internet using an HTTP tunnel
s	start	Start service containers defined in docker-compose.yml
s	status	Show the status of all service containers
s	stop	Stop and destroy running service containers
o	--verbose	Increases output verbosity	
o	--help|-h	Help for kool	
@	create
o	--verbose	Increases output verbosity	
o	--help|-h	Help for create	
a	2	0
#	create	2
t	folders
@	deploy
s	destroy	Destroy an environment deployed to Kool Cloud
s	exec	Execute a command inside a running service container deployed to Kool Cloud
s	logs	See the logs of running service container deployed to Kool Cloud
o	--verbose	Increases output verbosity	
o	--help|-h	Help for deploy	
@	deploy destroy
o	--verbose	Increases output verbosity	
o	--help|-h	Help for destroy	
@	deploy exec
o	--verbose	Increases output verbosity	
o	--container|-c	Container target	v
o	--help|-h	Help for exec	
@	deploy logs
o	--verbose	Increases output verbosity	
o	--container|-c	Container target	v
o	--follow|-f	Follow log output	
o	--tail|-t	Number of lines to show from the end of the logs for each container. A value equal to 0 will show…	v
o	--help|-h	Help for logs	
@	docker
o	--verbose	Increases output verbosity	
o	--env|-e	Environment variables	v
o	--network|-n	Connect a container to a network	v
o	--publish|-p	Publish a container's port(s) to the host	v
o	--volume|-v	Bind mount a volume	v
o	--help|-h	Help for docker	
a	2	1
@	exec
o	--verbose	Increases output verbosity	
o	--detach|-d	Detached mode: Run command in the background	
o	--env|-e	Environment variables	v
o	--help|-h	Help for exec	
a	2	1
@	info
o	--verbose	Increases output verbosity	
o	--help|-h	Help for info	
@	logs
o	--verbose	Increases output verbosity	
o	--follow|-f	Follow log output	
o	--tail|-t	Number of lines to show from the end of the logs for each container. A value equal to 0 will show…	v
o	--help|-h	Help for logs	
a	1	1
@	preset
o	--verbose	Increases output verbosity	
o	--help|-h	Help for preset	
a	1	0
@	recipe
o	--verbose	Increases output verbosity	
o	--help|-h	Help for recipe	
a	1	0
@	restart
o	--verbose	Increases output verbosity	
o	--purge	Remove all persistent data from volume mounts on containers	
o	--rebuild	Updates and builds service's images	
o	--help|-h	Help for restart	
a	1	1
#	restart	1
g	docker-compose config --services	\n
@	run
o	--verbose	Increases output verbosity	
o	--env|-e	Environment variables	v
o	--help|-h	Help for run	
a	1	0
#	run	1
d
@	self-update
o	--verbose	Increases output verbosity	
o	--help|-h	Help for self-update	
@	share
o	--verbose	Increases output verbosity	
o	--port	The port from the target service that should be shared. If not provided, it will default to port 80	v
o	--service	The name of the local service container you want to share	v
o	--subdomain	The subdomain used to generate your public https://subdomain.kool.live URL	v
o	--help|-h	Help for share	
@	start
o	--verbose	Increases output verbosity	
o	--foreground|-f	Start containers in foreground mode	
o	--profile	Specify a profile to enable	v
o	--rebuild|-b	Updates and builds service's images	
o	--help|-h	Help for start	
a	1	1
#	start	1
g	docker-compose config --services	\n
@	status
o	--verbose	Increases output verbosity	
o	--help|-h	Help for status	
@	stop
o	--verbose	Increases output verbosity	
o	--purge	Remove all persistent data from volume mounts on containers	
o	--help|-h	Help for stop	
a	1	1
#	stop	1
g	docker-compose config --services	\n
