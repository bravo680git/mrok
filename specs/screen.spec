@	
s	-d	Does not start screen, but detaches the elsewhere running screen session
s	-D	Does not start screen, but detaches the elsewhere running screen session
s	-r	Resumes a detached screen session
s	-R	Attempts to resume the first detached screen session it finds
s	-dmS	Start as daemon: Screen session in detached mode
o	-a	Force all capabilities into each window's termcap	
o	-A	Adapt all windows to the new display width & height	
o	-c	Read configuration file instead of '.screenrc'	v
o	-e	Change command characters	v
o	-f	Flow control on	
o	-fn	Flow control off	
o	-fa	Flow control automatic	
o	-h	Set the size of the scrollback history buffer	v
o	-i	Interrupt output sooner when flow control is on	
o	-list|-ls	Do nothing, just list our SockDir	
o	-L	Turn on output logging	
o	-m	Ignore $STY variable, do create a new screen session	
o	-O	Choose optimal output rather than exact vt100 emulation	
o	-p	Preselect the named window if it exists	v
o	-q	Quiet startup. Exits with non-zero return code if unsuccessful	
o	-s	Shell to execute rather than $SHELL	v
o	-S	Name this session <pid>.sockname instead of <pid>.<tty>.<host>	v
o	-t	Set title. (window's name)	v
o	-T	Use term as $TERM for windows, rather than 'screen'	v
o	-U	Tell screen to use UTF-8 encoding	
o	-v	Print 'Screen version 4.00.03 (FAU) 23-Oct-06'	
o	-wipe	Do nothing, just clean up SockDir	V
o	-x	Attach to a not detached screen. (Multi display mode)	
o	-X	Execute <cmd> as a screen command in the specified session	
a	2	1
=		-c
t	filepaths
=		-wipe
v	sessionowner/[pid.tty.host]	
@	-d
s	-r	Reattach a session and if necessary detach it first
s	-R	Reattach a session and if necessary detach or even create it first
s	-RR	Reattach a session and if necessary detach or create it. Use the first session if more than one…
@	-d -r
a	1	0
#	-d -r	1
v	pid	
v	pid.tty	
v	pid.tty.host	
v	sessionowner/pid	
v	sessionowner/pid.tty	
v	sessionowner/pid.tty.host	
@	-d -R
a	1	0
#	-d -R	1
v	pid	
v	pid.tty	
v	pid.tty.host	
v	sessionowner/pid	
v	sessionowner/pid.tty	
v	sessionowner/pid.tty.host	
@	-d -RR
a	1	0
#	-d -RR	1
v	pid	
v	pid.tty	
v	pid.tty.host	
v	sessionowner/pid	
v	sessionowner/pid.tty	
v	sessionowner/pid.tty.host	
@	-D
s	-r	Reattach a session. If necessary detach and logout remotely first
s	-R	Attach here and now. In detail this means: If a session is running, then reattach. If necessary…
s	-RR	Attach here and now. Whatever that means, just do it
@	-D -r
a	1	0
#	-D -r	1
v	pid	
v	pid.tty	
v	pid.tty.host	
v	sessionowner/pid	
v	sessionowner/pid.tty	
v	sessionowner/pid.tty.host	
@	-D -R
a	1	0
#	-D -R	1
v	pid	
v	pid.tty	
v	pid.tty.host	
v	sessionowner/pid	
v	sessionowner/pid.tty	
v	sessionowner/pid.tty.host	
@	-D -RR
a	1	0
#	-D -RR	1
v	pid	
v	pid.tty	
v	pid.tty.host	
v	sessionowner/pid	
v	sessionowner/pid.tty	
v	sessionowner/pid.tty.host	
@	-r
a	1	0
#	-r	1
v	pid	
v	pid.tty	
v	pid.tty.host	
v	sessionowner/pid	
v	sessionowner/pid.tty	
v	sessionowner/pid.tty.host	
@	-R
a	1	0
#	-R	1
v	pid	
v	pid.tty	
v	pid.tty.host	
v	sessionowner/pid	
v	sessionowner/pid.tty	
v	sessionowner/pid.tty.host	
@	-dmS
a	1	0
