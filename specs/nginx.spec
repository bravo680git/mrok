@	
o	-c	Use an alternative configuration file	v
o	-e	Use an alternative error log file. Special value stderr indicates that the standard error output…	v
o	-g	Set global configuration directives	v
o	-p	Set the prefix path. The default value is %%PREFIX%%	v
o	-q	Suppress non-error messages during configuration testing	
o	-T	Same as -t, but additionally dump configuration files to standard output	
o	-t	Do not run, just test the configuration file. nginx checks the configuration file syntax and then…	
o	-V	Print the nginx version, compiler version, and configure script parameters	
o	-v	Print the nginx version	
o	-?|-h	Print help	
o	-s	Send a signal to the master process. The argument signal can be one of: stop, quit, reopen, reload	v
a	1	1
=		-c
t	filepaths
=		-e
v	stderr	
=		-s
v	stop	Sends SIGTERM
v	quit	Sends SIGQUIT
v	reopen	Sends SIGUSR1
v	reload	Sends SIGHUP
