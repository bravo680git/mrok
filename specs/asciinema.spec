@	
s	rec	Start a recording
s	play	Replay recorded asciicast in a terminal
s	cat	Print full output of recorded asciicast to a terminal
s	upload	Upload recorded asciicast to asciinema.org site
s	auth	Link and manage your install ID with your asciinema.org user account
o	--version	Ouput version information and exit	
o	-h|--help	Output help message and exit	p
@	rec
o	--stdin	Enable stdin (keyboard) recording	
o	--append	Append to existing recording	
o	--raw	Save raw output, without timing or other metadata	
o	--overwrite	Overwrite the recording if it already exists	
o	-c|--command	Specify command to record, defaults to $SHELL	v=
o	-e|--env	List of environment variables to capture	v=
o	-t|--title	Specify the title of the asciicast	v=
o	-i|--idle-time-limit	Limit recorded terminal inactivity to max amount of seconds	v=
o	--cols	Override terminal columns for recorded process	v=
o	--rows	Override terminal rows for recorded process	v=
o	-y|--yes	Answer “yes” to all prompts (e.g. upload confirmation)	
o	-q|--quiet	Be quiet, suppress all notices/warnings (implies -y)	
a	1	0
@	play
o	-i|--idle-time-linit	Limit replayed terminal inactivity	v=
o	-s|--speed	Playback speed	v=
a	1	0
#	play	1
v	-	Stdin
t	filepaths
@	cat
a	1	0
#	cat	1
v	-	Stdin
t	filepaths
@	upload
a	1	0
#	upload	1
v	-	Stdin
t	filepaths
@	auth
