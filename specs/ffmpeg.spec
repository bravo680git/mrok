@	
o	-i	Input file	v
o	-L	Show license	
o	-h	Show help	v
o	-?	Show help	v
o	-help	Show help	v
o	--help	Show help	v
o	-version	Show version	
o	-buildconf	Show build configuration	
o	-formats	Show available formats	
o	-muxers	Show available muxers	
o	-demuxers	Show available demuxers	
o	-devices	Show available devices	
o	-codecs	Show available codecs	
o	-decoders	Show available decoders	
o	-encoders	Show available encoders	
o	-bsfs	Show available bit stream filters	
o	-protocols	Show available protocols	
o	-filters	Show available filters	
o	-pix_fmts	Show available pixel formats	
o	-layouts	Show standard channel layouts	
o	-sample_fmts	Show available audio sample formats	
o	-dispositions	Show available stream dispositions	
o	-colors	Show available color names	
o	-sources	List sources of the input device	v
o	-sinks	List sinks of the output device	v
o	-hwaccels	Show available HW acceleration methods	
o	-loglevel	Set logging level	v
o	-v	Set logging level	v
o	-report	Generate a report	
o	-max_alloc	Set maximum size of a single allocated block	v
o	-y	Overwrite output files	
o	-n	Never overwrite output files	
o	-ignore_unknown	Ignore unknown stream types	
o	-filter_threads	Number of non-complex filter threads	
o	-filter_complex_threads	Number of threads for -filter_complex	
o	-stats	Print progress report during encoding	
o	-max_error_rate	Ratio of decoding errors (0.0: no errors, 1.0: 100% errors) above which ffmpeg returns an error…	v
o	-vol	Change audio volume (256=normal)	v
o	-cpuflags	Force specific cpu flags	v
o	-cpucount	Force specific cpu count	v
o	-hide_banner	Do not show program banner	v
o	-copy_unknown	Copy unknown stream types	
o	-recast_media	Allow recasting stream type in order to force a decoder of different media type	
o	-benchmark	Add timings for benchmarking	
o	-benchmark_all	Add timings for each task	
o	-progress	Write program-readable progress information	v
o	-stdin	Enable or disable interaction on standard input	
o	-timelimit	Set max runtime in seconds in CPU user time	v
o	-dump	Dump each input packet	
o	-hex	When dumping packets, also dump the payload	
o	-vsync	Set video sync method globally; deprecated, use -fps_mode	
o	-frame_drop_threshold	Frame drop threshold	
o	-async	Audio sync method	
o	-adrift_threshold	Audio drift threshold	v
o	-copyts	Copy timestamps	
o	-start_at_zero	Shift input timestamps to start at 0 when using copyts	
o	-copytb	Copy input stream time base when stream copying	v
o	-dts_delta_threshold	Timestamp discontinuity delta threshold	v
o	-dts_error_threshold	Timestamp error delta threshold	v
o	-xerror	Exit on error	v
o	-abort_on	Abort on the specified condition flags	v
o	-filter_complex	Create a complex filtergraph	v
o	-lavfi	Create a complex filtergraph	v
o	-filter_complex_script	Read complex filtergraph description from a file	v
o	-auto_conversion_filters	Enable automatic conversion filters globally	
o	-stats_period	Set the period at which ffmpeg updates stats and -progress output	v
o	-debug_ts	Print timestamp debugging info	
o	-psnr	Calculate PSNR of compressed frames	
o	-vstats	Dump video coding statistics to file	
o	-vstats_file	Dump video coding statistics to file	v
o	-vstats_version	Version of the vstats format to use	
o	-qphist	Show QP histogram	
o	-sdp_file	Specify a file in which to print sdp information	v
o	-init_hw_device	Initialise hardware device	v
o	-filter_hw_device	Set hardware device used when filtering	v
o	-f	Force format	v
o	-c	Codec name	v
o	-codec	Codec name	v
o	-pre	Preset name	v
o	-map_metadata	Set metadata information of outfile from infile	v
o	-t	Record or transcode "duration" seconds of audio/video	v
o	-to	Record or transcode stop time	v
o	-fs	Set the limit file size in bytes	v
o	-ss	Set the start time offset	v
o	-sseof	Set the start time offset relative to EOF	v
o	-seek_timestamp	Enable/disable seeking by timestamp with -ss	
o	-timestamp	Set the recording timestamp ('now' to set the current time)	v
o	-metadata	Add metadata	v
o	-program	Add program with specified streams	v
o	-target	Specify target file type ("vcd", "svcd", "dvd", "dv" or "dv50" with optional prefixes "pal-"…	v
o	-apad	Audio pad	
o	-frames	Set the number of frames to output	v
o	-filter	Set stream filtergraph	v
o	-filter_script	Read stream filtergraph description from a file	v
o	-reinit_filter	Reinit filtergraph on input parameter changes	
o	-discard	Discard	
o	-disposition	Disposition	
o	-map	Set input stream mapping	v
o	-map_channel	Map an audio channel from one stream to another	v
o	-map_chapters	Set chapters mapping	v
o	-accurate_seek	Enable/disable accurate seeking with -ss	
o	-isync	Indicate the input index for sync reference	v
o	-itsoffset	Set the input ts offset	v
o	-itsscale	Set the input ts scale	v
o	-dframes	Set the number of data frames to output	v
o	-re	Read input at native frame rate; equivalent to -readrate 1	
o	-readrate	Read input at specified rate	v
o	-shortest	Finish encoding within shortest input	
o	-bitexact	Bitexact mode	
o	-copyinkf	Copy initial non-keyframes	
o	-copypriorss	Copy or discard frames before start time	
o	-tag	Force codec tag/fourcc	v
o	-q	Use fixed quality scale (VBR)	v
o	-qscale	Use fixed quality scale (VBR)	v
o	-profile	Set profile	v
o	-attach	Add an attachment to the output file	v
o	-dump_attachment	Extract an attachment into a file	v
o	-stream_loop	Set number of times input stream shall be looped	v
o	-thread_queue_size	Set the maximum number of queued packets from the demuxer	
o	-find_stream_info	Read and decode the streams to fill missing information with heuristics	
o	-bits_per_raw_sample	Set the number of bits per raw sample	v
o	-autorotate	Automatically insert correct rotate filters	
o	-autoscale	Automatically insert a scale filter at the end of the filter graph	
o	-muxdelay	Set the maximum demux-decode delay	v
o	-muxpreload	Set the initial demux-decode delay	v
o	-time_base	Set the desired time base hint for output stream (1:24, 1:48000 or 0.04166, 2.0833e-5)	v
o	-enc_time_base	Set the desired time base for the encoder (1:24, 1:48000 or 0.04166, 2.0833e-5). two special…	v
o	-bsf	A comma-separated list of bitstream filters	v
o	-fpre	Set options from indicated preset file	v
o	-max_muxing_queue_size	Maximum number of packets that can be buffered while waiting for all streams to initialize	v
o	-muxing_queue_data_threshold	Set the threshold after which max_muxing_queue_size is taken into account	v
o	-dcodec	Force data codec ('copy' to copy stream)	v
o	-vframes	Set the number of video frames to output	v
o	-r	Set frame rate (Hz value, fraction or abbreviation)	v
o	-fpsmax	Set max frame rate (Hz value, fraction or abbreviation)	v
o	-s	Set frame size (WxH or abbreviation)	v
o	-aspect	Set aspect ratio (4:3, 16:9 or 1.3333, 1.7777)	v
o	-vn	Disable video	
o	-vcodec	Force video codec ('copy' to copy stream)	v
o	-timecode	Set initial TimeCode value	v
o	-pass	Select the pass number (1 to 3)	v
o	-vf	Set video filters	v
o	-ab	Audio bitrate (please use -b:a)	v
o	-b	Video bitrate (please use -b:v)	v
o	-dn	Disable data	
o	-pix_fmt	Set pixel format	v
o	-rc_override	Rate control override for specific intervals	v
o	-passlogfile	Select two pass log file name prefix	v
o	-intra_matrix	Specify intra matrix coeffs	v
o	-inter_matrix	Specify inter matrix coeffs	v
o	-chroma_intra_matrix	Specify intra matrix coeffs	v
o	-top	Top=1/bottom=0/auto=-1 field first	
o	-vtag	Force video tag/fourcc	v
o	-fps_mode	Set framerate mode for matching video streams; overrides vsync	
o	-force_fps	Force the selected framerate, disable the best supported framerate selection	
o	-streamid	Set the value of an outfile streamid	v
o	-force_key_frames	Force key frames at specified timestamps	v
o	-hwaccel	Use HW accelerated decoding	v
o	-hwaccel_device	Select a device for HW acceleration	v
o	-hwaccel_output_format	Select output format used with HW accelerated decoding	v
o	-vbsf	Deprecated	v
o	-vpre	Set the video options to the indicated preset	v
o	-aframes	Set the number of audio frames to output	v
o	-aq	Set audio quality (codec-specific)	v
o	-ar	Set audio sampling rate (in Hz)	v
o	-ac	Set number of audio channels	v
o	-an	Disable audio	
o	-acodec	Force audio codec ('copy' to copy stream)	v
o	-af	Set audio filters	v
o	-atag	Force audio tag/fourcc	v
o	-sample_fmt	Set sample format	v
o	-channel_layout	Set channel layout	v
o	-ch_layout	Set channel layout	v
o	-guess_layout_max	Set the maximum number of channels to try to guess the channel layout	
o	-absf	Deprecated	v
o	-apre	Set the audio options to the indicated preset	v
o	-sn	Disable subtitle	
o	-scodec	Force subtitle codec ('copy' to copy stream)	v
o	-stag	Force subtitle tag/fourcc	v
o	-fix_sub_duration	Fix subtitles duration	
o	-canvas_size	Set canvas size (WxH or abbreviation)	v
o	-spre	Set the subtitle options to the indicated preset	v
a	1	0
=		-i
t	filepaths
=		-sources
d
=		-sinks
d
=		-filter_hw_device
d
=		-c
d
=		-codec
d
=		-dcodec
d
=		-vcodec
d
=		-acodec
d
=		-scodec
d
#		1
t	filepaths
