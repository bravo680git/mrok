@	
o	--help|-h	Print the help text and exit	
o	--version	Print program version and exit	
o	-U|--update	Update this program to latest version. Make sure you have sufficient permissions (run with sudo if…	
o	--ignore-errors|-i	Continue on download errors, for example to skip unavailable videos in a playlist	
o	--abort-on-error	Abort downloading of further videos (in the playlist or the command line) if an error occurs	
o	--dump-user-agent	Display the current browser identification	
o	--list-extractors	List all supported extractors	
o	--extractor-descriptions	Output descriptions of all supported extractors	
o	--default-search	Use this prefix for unqualified URLs. For example "gvsearch2:" downloads two videos from google…	v
o	--config-location	Location of the configuration file; either the path to the config or its containing directory	v
o	--force-generic-extractor	Force extraction to use the generic extractor	
o	--ignore-config	Do not read configuration files	
o	--flat-playlist	Do not extract the videos of a playlist, only list them	
o	--mark-watched	Mark videos watched (YouTube only)	
o	--no-mark-watched	Do not mark videos watched (YouTube only)	
o	--no-color	Do not emit color codes in output	
o	--proxy	Use the specified HTTP/HTTPS/SOCKS proxy. Pass in an empty string for direct connection	v
o	--socket-timeout	Time to wait before giving up, in seconds	v
o	--source-address	Client-side IP address to bind to	v
o	-4|--force-ipv4	Make all connections via IPv4	
o	-6|--force-ipv6	Make all connections via IPv6	
o	--geo-verification-proxy	Use this proxy to verify the IP address for some geo-restricted sites	v
o	--geo-bypass	Bypass geographic restriction via faking X-Forwarded-For HTTP header	
o	--no-geo-bypass	Do not bypass geographic restriction via faking X-Forwarded-For HTTP header	
o	--geo-bypass-country	Force bypass geographic restriction with explicitly provided two-letter ISO 3166-2 county code	v
o	--geo-bypass-ip-block	Force bypass geographic restriction with explicitly provided IP block in CIDR notation	v
o	--playlist-start	Playlist video to start at (default is 1)	v
o	--playlist-end	Playlist video to end at (default is last)	v
o	--playlist-items	Playlist video to end at (default is last)	v
o	--match-title	Download only matching titles (regex or caseless sub-string)	v
o	--reject-title	Skip download for matching titles (regex or caseless sub-string)	v
o	--max-downloads	Abort after downloading NUMBER files	v
o	--min-filesize	Do not download any videos smaller than SIZE (e.g. 50k or 44.6)	v
o	--max-filesize	Do not download any videos larger than SIZE (e.g. 50k or 44.6)	v
o	--date	Download only videos uploaded in this date	v
o	--datebefore	Download only videos uploaded on or before this date (i.e. inclusive)	v
o	--dateafter	Download only videos uploaded on or after this date (i.e. inclusive)	v
o	--min-views	Do not download any videos with less than COUNT views	v
o	--max-views	Do not download any videos with more than COUNT views	v
o	--match-filter	Generic video filter	v
o	--no-playlist	Download only the video, if the URL refers to a video and a playlist	
o	--yes-playlist	Download the playlist, if the URL refers to a video and a playlist	
o	--age-limit	Download only videos suitable for the given age	v
o	--download-archive	Download only videos not listed in the archive file. Record the IDs of all downloaded videos in it	v
o	--include-ads	Download advertisements as well (experimental)	
o	-r|--limit-rate	Maximum download rate in bytes per second (e.g. 50K or 4.2M)	v
o	-R|--retries	Number of retries or "infinite"	v
o	--fragment-retries	Number of retries for a fragment or "infinite"	v
o	--skip-unavailable-fragments	Skip unavailable fragments	
o	--abort-on-unavailable-fragments	Abort downloading when some fragment is not available	
o	--keep-fragments	Keep downloaded fragments on disk after downloading is finished; fragments are erased by default	
o	--buffer-size	Size of download buffer (e.g. 1024 or 16K)	v
o	--no-resize-buffer	Do not automatically adjust the buffer size	
o	--http-chunk-size	Size of a chunk for chunk-based HTTP downloading (e.g. 10385760 or 10M)	v
o	--playlist-reverse	Download playlist videos in reverse order	
o	--playlist-random	Download playlist videos in random order	
o	--xattr-set-filesize	Set file xattribute ytdl.filesize with expected file size	
o	--hls-prefer-native	Use the native HLS downloader instead of ffmpeg	
o	--hls-prefer-ffmpeg	Use ffmpeg instead of the native HLS downloader	
o	--hls-prefer-mpegts	Use the mpegts container for HLS videos, allowing to play the video while downloading	
o	--external-downloader	Use the specified external downloader	v
o	--external-downloader-args	Give these arguments to the external downloader	v
o	-a|--batch-file	File containing URLs to download ('-' for stdin), one URL per line. Lines starting with '#', ';'…	v
o	--id	Use only video ID in file name	
o	-o|--output	Output filename template	v
o	--output-na-placeholder	Placeholder value for unavailable meta fields in output filename template	v
o	--autonumber-start	Specify the start value for %(autonumber)s	v
o	--restrict-filenames	Restrict filenames to only ASCII characters, and avoid "&" and spaces in filenames	
o	-w|--no-overwrites	Do not overwrite files	
o	-c|--continue	Do not resume partially downloaded files (restart from beginning)	
o	--no-part	Do not use .part files - write directly into output file	
o	--no-mtime	Do not use the Last-modified header to set the file modification time	
o	--write-description	Write video descriptions to a .description file	
o	--write-info-json	Write video metadata to a .info.json file	
o	--write-annotations	Write video annotations to a .annotations.xml file	
o	--load-info-json	JSON file containing the video information (created with the "--write-info-json" option	v
o	--cookies	File to read cookies from and dump cookie jar in	v
o	--cache-dir	Location in the filesystem where youtube-dl can store some downloaded information permanently	v
o	--no-cache-dir	Disable filesystem caching	
o	--rm-cache-dir	Delete all filesystem cache files	
o	--write-thumbnail	Write thumbnail image to disk	
o	--write-all-thumbnail	Write all thumbnail image formats to disk	
o	--list-thumbnails	Simulate and list all available thumbnail formats	
o	-q|--quiet	Activate quite mode	
o	--no-warnings	Ignore warnings	
o	-s|--simulate	Do not download the video and do note write anything to disk	
o	--skip-download	Do not download the video	
o	-g|--get-url	Simulate, quiet but print URL	
o	-e|--get-title	Simulate, quiet but print title	
o	--get-id	Simulate, quiet but print id	
o	--get-thumbnail	Simulate, quiet but print thumbnail URL	
o	--get-description	Simulate, quiet but print video description	
o	--get-duration	Simulate, quiet but print video length	
o	--get-filename	Simulate, quiet but print output filename	
o	--get-format	Simulate, quiet but print output format	
o	-j|--dump-json	Simulate, quiet but JSON information	
o	-J|--dump-single-json	Simulate, quiet but JSON information for each command-line argument	
o	--print-json	Be quiet and print the video information as JSON (video is still being downloaded)	
o	--newline	Output the progress bar as new lines	
o	--no-progress	Do not print the progress bar	
o	--console-title	Display progress in console titlebar	
o	-v|--verbose	Print various debugging information	
o	--dump-pages	Print downloaded pages encoded using base64 to debug problems (very verbose)	
o	--write-pages	Write downloaded intermediary pages to files in the current directory to debug problems	
o	--print-traffic	Display sent and read HTTP traffic	
o	-C|--call-home	Contact the youtube-dl server for debugging	
o	--no-call-home	Do NOT contact the youtube-dl server for debugging	
o	--encoding	Force the specified encoding (experimental)	v
o	--no-check-certificate	Suppress HTTPS certificate validation	
o	--prefer-insecure	Use an unencrypted connection to retrieve information about the video. (Currently supported only…	
o	--user-agent	Specify a custom user agent	v
o	--referer	Specify a custom referer, use if the video access is restricted to one domain	v
o	--add-header	Specify a custom HTTP header and its value, separated by a colon ':'	v
o	--bidi-workaround	Work around terminals that lack bidirectional text support. Requires bidiv or fribidi executable…	
o	--sleep-interval	Number of seconds to sleep before each download when used alone or a lower bound of a range for…	v
o	--max-sleep-interval	Upper bound of a range for randomized sleep before each download. Must only be used along with…	v
o	-f|--format	Video format code	v
o	--all-formats	Download all available video formats	
o	--prefer-free-formats	Prefer free video formats unless a specific one is requested	
o	-F|--list-formats	List all available formats of requested videos	
o	--youtube-skip-dash-manifest	Do not download the DASH manifests and related data on YouTube videos	
o	--merge-output-format	If a merge is required (e.g. bestvideo+bestaudio), output to given container format	v
o	--write-sub	Write subtitle file	
o	--write-auto-sub	Write automatically generated subtitle file (YouTube only)	
o	--all-subs	Download all the available subtitles of the video	
o	--list-subs	List all available subtitles for the video	
o	--sub-format	Subtitle format, accepts formats preference, for example: "srt" or "ass/srt/best"	v
o	--sub-lang	Languages of the subtitles to download (optional) separated by commas	v
o	-u|--username	Login with this account ID	v
o	-p|--password	Account password. If this option is left out, youtube-dl will ask interactively	v
o	-2|--twofactor	Two-factor authentication code	v
o	-n|--netrc	Use .netrc authentication data	
o	--video-password	Video password (vimeo, youku)	v
o	--ap-mso	Adobe Pass multiple-system operator (TV provider) identifier	v
o	--ap-username	Multiple-system operator account login	v
o	--ap-password	Multiple-system operator account password. If this option is left out, youtube-dl will ask…	v
o	--ap-list-mso	List all supported multiple-system operators	
o	-x|--extract-audio	Convert audio files to audio-only files (requires ffmpeg/avconv and ffprobe/avprobe)	
o	--audio-format	Specify audio format	v
o	--audio-quality	Specify ffmpeg/avconv audio quality, insert a value between 0 (better) and 9 (worse) for VBR or a…	v
o	--recode-video	Encode the video to another format if necessary	v
o	--postprocessor-args	Give these arguments to the postprocessor	v
o	-k|--keep-video	Keep the video file on disk after the post-processing; the video is erased by default	
o	--no-post-overwrites	Do not overwrite post-processed files; the post-processed files are overwritten by default	
o	--embed-subs	Embed subtitles in the video (only for mp4, webm and mkv videos)	
o	--embed-thumbnail	Embed thumbnail in the audio as cover art	
o	--embed-metadata	Write metadata to the video file	
o	--metadata-from-title	Parse additional metadata like song title / artist from the video title. The format syntax is the…	v
o	--xattrs	Write metadata to the video file's xattrs (using dublin core and xdg standards)	
o	--fixup	Automatically correct known faults of the file	v
o	--prefer-avconv	Prefer avconv over ffmpeg for running the postprocessors	
o	--prefer-ffmpeg	Prefer ffmpeg over avconv for running the postprocessors (default)	
o	--ffmpeg-location	Location of the ffmpeg/avconv binary; either the path to the binary or its containing directory	v
o	--exec	Execute a command on the file after downloading and post-processing, similar to find's -exec syntax	v
o	--convert-subs	Convert the subtitles to other format	v
a	1	1
=		--config-location
t	filepaths,folders
=		--playlist-start
d
=		--playlist-end
d
=		--playlist-items
d
=		--external-downloader
v	aria2c	
v	avconv	
v	axel	
v	curl	
v	ffmpeg	
v	httpie	
v	wget	
=		-a
v	-	
t	filepaths
=		--load-info-json
t	filepaths
=		--cookies
t	filepaths
=		--cache-dir
t	folders
=		--merge-output-format
v	mkv	
v	mp4	
v	ogg	
v	webm	
v	flv	
=		--sub-lang
v	af	
v	sq	
v	am	
v	ar	
v	hy	
v	az	
v	bn	
v	eu	
v	be	
v	bs	
v	bg	
v	my	
v	ca	
v	ceb	
v	zh-Hans	
v	zh-Hant	
v	co	
v	hr	
v	cs	
v	da	
v	nl	
v	en	
v	eo	
v	et	
v	fil	
v	fi	
v	fr	
v	gl	
v	ka	
v	de	
v	el	
v	gu	
v	ht	
v	ha	
v	haw	
v	iw	
v	hi	
v	hmn	
v	hu	
v	is	
v	ig	
v	id	
v	ga	
v	it	
v	ja	
v	jv	
v	kn	
v	kk	
v	km	
v	rw	
v	ko	
v	ku	
v	ky	
v	lo	
v	la	
v	lv	
v	lt	
v	lb	
v	mk	
v	mg	
v	ms	
v	ml	
v	mt	
v	mi	
v	mr	
v	mn	
v	ne	
v	no	
v	ny	
v	or	
v	ps	
v	fa	
v	pl	
v	pt	
v	pa	
v	ro	
v	ru	
v	sm	
v	gd	
v	sr	
v	sn	
v	sd	
v	si	
v	sk	
v	sl	
v	so	
v	st	
v	es	
v	su	
v	sw	
v	sv	
v	tg	
v	ta	
v	tt	
v	te	
v	th	
v	tr	
v	tk	
v	uk	
v	ur	
v	ug	
v	uz	
v	vi	
v	cy	
v	fy	
v	xh	
v	yi	
v	yo	
v	zu	
=		--ap-mso
d
=		--audio-format
v	best	
v	aac	
v	flac	
v	mp3	
v	m4a	
v	opus	
v	vorbis	
v	wav	
=		--recode-video
v	mp4	
v	flv	
v	ogg	
v	webm	
v	mkv	
v	avi	
=		--fixup
v	never	Do nothing
v	warn	Only emit a warning
v	detect_or_warn	Fix file if we can, warn otherwise
=		--ffmpeg-location
t	folders,filepaths
=		--convert-subs
v	srt	
v	ass	
v	vtt	
v	lrc	
#		1
d
