@	
o	--signal	Signal to send (either number or name)	v
o	-q|--queue	Integer value to be sent with the signal	v
o	-e|--echo	Display what is killed	
o	-f|--full	Use full process name to match	
o	-g|--pgroup	Match listed process group IDs	v
o	-G|--group	Match real group IDs	v
o	-i|--ignore-case	Match case insensitively	
o	-n|--newest	Select most recently started	
o	-o|--oldest	Select least recently started	
o	-O|--older	Select where older than seconds	v
o	-P|--parent	Match only child processes of the given parent	v
o	-s|--session	Match session IDs	v
o	-t|--terminal	Match by controlling terminal	v
o	-u|--euid	Match by effective IDs	v
o	-U|--uid	Match by real IDs	v
o	-x|--exact	Match exactly with the command name	
o	-F|--pidfile	Read PIDs from file	v
o	-L|logpidfile	Fail if PID file is not locked	
o	-r|--runstates	Match runstates	v
o	--ns	Match the processes that belong to a specified PID	v
o	--nslist	List which namespaces will be considered for the --ns option	v
o	-h|--help	Output help message and exit	
o	-V|--version	Output version information and exit	
a	1	0
=		--signal
v	SIGABRT	
v	SIGALRM	
v	SIGBUS	
v	SIGCHLD	
v	SIGCLD	
v	SIGCONT	
v	SIGEMT	
v	SIGFPE	
v	SIGHUP	
v	SIGILL	
v	SIGINFO	
v	SIGINT	
v	SIGIO	
v	SIGIOT	
v	SIGKILL	
v	SIGLOST	
v	SIGPIPE	
v	SIGPOLL	
v	SIGPROF	
v	SIGPWR	
v	SIGQUIT	
v	SIGSEGV	
v	SIGSTKFLT	
v	SIGSTOP	
v	SIGTSTP	
v	SIGSYS	
v	SIGTERM	
v	SIGTRAP	
v	SIGTTIN	
v	SIGTTOU	
v	SIGUNUSED	
v	SIGURG	
v	SIGUSR1	
v	SIGUSR2	
v	SIGVTALRM	
v	SIGXCPU	
v	SIGXFSZ	
v	SIGWINCH	
=		-F
t	filepaths
=		--nslist
v	ipc	
v	mnt	
v	net	
v	pid	
v	user	
v	uts	
