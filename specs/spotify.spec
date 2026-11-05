@	
s	play	Resume playback where Spotify last left off
s	next	Skip to the next song in a playlist
s	prev	Return to the previous song in a playlist
s	replay	Replay the current track from the beginning
s	pos	Jump to a time (in secs) in the current song
s	pause	Pause (or resume) Spotify playback
s	stop	Stop playback
s	quit	Stop playback and quit Spotify
s	vol	Show the current Spotify volume
s	status	Show the current player status
s	share	Display the current song's Spotify URL and URI
s	toggle	
o	--help|-h	Show help for spotify	
@	play
s	album	Find an album by name and play it
s	artist	Find an artist by name and play it
s	list	Find a playlist by name and plays it
s	uri	Play songs from specific uri
a	1	0
@	play album
a	1	0
@	play artist
a	1	0
@	play list
a	1	0
@	play uri
a	1	0
@	next
@	prev
@	replay
@	pos
a	1	0
@	pause
@	stop
@	quit
@	vol
a	1	0
#	vol	1
v	up	Increase the volume by 10%
v	down	Decrease the volume by 10%
@	status
s	artist	Show the currently playing artist
s	album	Show the currently playing album
s	track	Show the currently playing track
@	status artist
@	status album
@	status track
@	share
s	url	Display the current song's Spotify URL and copies it to the clipboard
s	uri	Display the current song's Spotify URI and copies it to the clipboard
@	share url
@	share uri
@	toggle
s	shuffle	Toggle shuffle playback mode
s	repeat	Toggle repeat playback mode
@	toggle shuffle
@	toggle repeat
