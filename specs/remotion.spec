@	
s	versions	Prints and validates versions of all Remotion packages
s	gpu	Prints information about how Chrome uses the GPU
s	compositions	Prints the list of available compositions
s	lambda	Access functionality of @remotion/lambda
s	bundle	Bundle a Remotion project
s	render	Render a video based on the entry point, the composition ID and save it to the output location
s	still	Render a still frame based on the entry point, the composition ID and save it to the output location
s	preview|studio	Start the Remotion Studio
s	upgrade	Upgrade all Remotion-related dependencies to the newest version
s	benchmark	Try different render configurations and compare them
s	install	Ensure Remotion dependencies
o	--help	Prints the list of commands and flags for quick lookup	
@	versions
@	gpu
@	compositions
o	--props	Pass input props as filename or as JSON	v
o	--env-file	Specify a location for a dotenv file	v
o	--disable-headless	Run Chrome in normal mode rather than headless	
o	--gl	Which OpenGL renderer to use	v
o	--user-agent	User agent to use for Chrome during rendering	
o	--ignore-certificate-errors	Ignore SSL errors	
o	--disable-web-security	Disable CORS and other web security features	
a	1	0
=	compositions	--props
t	filepaths
=	compositions	--env-file
t	filepaths
=	compositions	--gl
v	angle	
v	egl	
v	swiftshader	
v	swangle	
v	vulkan	
#	compositions	1
t	filepaths
@	lambda
s	policies	Manage AWS policies
s	quotas	Show current AWS quota
s	regions	Prints list of supported regions
s	render	Render media on Lambda
s	compositions	Get the list of available compositions on Lambda
s	still	Render a still on Lambda
s	functions	Manage functions on AWS Lambda
s	sites	
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda	--config
t	filepaths
=	lambda	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda policies
s	role	Print policy to be added to the AWS role
s	user	Print policy to be added to the AWS user
s	validate	Validate the user policy was configured correctly
@	lambda policies role
@	lambda policies user
@	lambda policies validate
@	lambda quotas
s	increase	Send a request to AWS to increase concurrency quotas
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda quotas	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda quotas	--config
t	filepaths
=	lambda quotas	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda quotas increase
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda quotas increase	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda quotas increase	--config
t	filepaths
=	lambda quotas increase	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda regions
o	--default-only	Only print the regions enabled by default in a new AWS account	
@	lambda render
o	--max-retries	How many times a chunk can be retried before the render times out	v
o	--privacy		v
o	--frames-per-lambda	How many frames should be rendered per chunk	v
o	--props	Pass input props as filename or as JSON	v
o	--disable-headless	Run Chrome in normal mode rather than headless	
o	--gl	Which OpenGL renderer to use	v
o	--user-agent	User agent to use for Chrome during rendering	
o	--ignore-certificate-errors	Ignore SSL errors	
o	--disable-web-security	Disable CORS and other web security features	
o	--concurrency-per-lambda	Concurrency with which each Lambda function should render	v
o	--overwrite	Overwrite a video if it already exists in the S3 bucket	
o	--function-name	Name of the function that should be invoked	
o	--renderer-function-name	Use a different function to render the video. By default, use the same function as the one to…	
o	--timeout	The time in milisecond that a delayRender() may take before it times out	
o	--quality	Quality for rendered frames, JPEG only, 0-100	v
o	--scale	Upscale or downscale or the dimensions of the video	v
o	--codec	Video or audio codec	v
o	--audio-codec	Codec to be used for the audio	v
o	--every-nth-frame	Render only every nth frame (only for GIFs)	v
o	--number-of-gif-loops	How many times a GIF should loop. 0 = No loop	v
o	--audio-bitrate	Customize the output audio bitrate	
o	--video-bitrate	Customize the output video bitrate. Mutually exclusive with --crf	
o	--crf	FFMPEG CRF value, controls quality, see docs for info	
o	--frames	Render a portion or a still of a video, 0-9, 50	v
o	--prores-profile	ProRes profile, need --codec=prores to be set	v
o	--x264-preset	Presets balance encoding speed and compression quality, with slower presets achieving better…	v
o	--image-format	Format to render the frames in, "jpeg" or "png"	v
o	--pixel-format	Custom pixel format, see docs for available values	v
o	--muted	Outputs no audio	
o	--height	Override the composition height	v
o	--width	Override the composition width	v
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
a	3	0
=	lambda render	--privacy
v	public	
v	private	
=	lambda render	--props
t	filepaths
=	lambda render	--gl
v	angle	
v	egl	
v	swiftshader	
v	swangle	
v	vulkan	
=	lambda render	--quality
v	0	
v	10	
v	20	
v	30	
v	40	
v	50	
v	60	
v	70	
v	80	
v	90	
v	100	
=	lambda render	--scale
v	0.25	
v	0.5	
v	1	
v	1.5	
v	2	
v	4	
=	lambda render	--codec
v	h264	
v	h265	
v	gif	
v	vp8	
v	vp9	
v	mp3	
v	aac	
v	wav	
v	prores	
v	h264-mkv	
=	lambda render	--audio-codec
v	aac	
v	mp3	
v	opus	
v	pcm-16	
=	lambda render	--every-nth-frame
v	2	
v	3	
v	4	
v	5	
=	lambda render	--number-of-gif-loops
v	0	
v	1	
v	2	
v	3	
=	lambda render	--prores-profile
v	4444-xq	
v	4444	
v	hq	
v	standard	
v	light	
v	proxy	
=	lambda render	--x264-preset
v	ultrafast	
v	superfast	
v	veryfast	
v	faster	
v	fast	
v	medium	
v	slow	
v	slower	
v	veryslow	
v	placebo	
=	lambda render	--image-format
v	jpeg	
v	png	
=	lambda render	--pixel-format
v	yuv420p	
v	yuv422p	
v	yuv444p	
v	yuv420p10le	
v	yuv422p10le	
v	yuv444p10le	
v	yuva420p	
=	lambda render	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda render	--config
t	filepaths
=	lambda render	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda compositions
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
o	--props	Pass input props as filename or as JSON	v
o	--env-file	Specify a location for a dotenv file	v
o	--disable-headless	Run Chrome in normal mode rather than headless	
o	--gl	Which OpenGL renderer to use	v
o	--user-agent	User agent to use for Chrome during rendering	
o	--ignore-certificate-errors	Ignore SSL errors	
o	--disable-web-security	Disable CORS and other web security features	
a	1	0
=	lambda compositions	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda compositions	--config
t	filepaths
=	lambda compositions	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
=	lambda compositions	--props
t	filepaths
=	lambda compositions	--env-file
t	filepaths
=	lambda compositions	--gl
v	angle	
v	egl	
v	swiftshader	
v	swangle	
v	vulkan	
@	lambda still
o	--max-retries	How many times a chunk can be retried before the render times out	v
o	--privacy		v
o	--frames-per-lambda	How many frames should be rendered per chunk	v
o	--props	Pass input props as filename or as JSON	v
o	--disable-headless	Run Chrome in normal mode rather than headless	
o	--gl	Which OpenGL renderer to use	v
o	--user-agent	User agent to use for Chrome during rendering	
o	--ignore-certificate-errors	Ignore SSL errors	
o	--disable-web-security	Disable CORS and other web security features	
o	--frame	Which frame to render (default 0)	v
o	--height	Override the composition height	v
o	--width	Override the composition width	v
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
a	3	0
=	lambda still	--privacy
v	public	
v	private	
=	lambda still	--props
t	filepaths
=	lambda still	--gl
v	angle	
v	egl	
v	swiftshader	
v	swangle	
v	vulkan	
=	lambda still	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda still	--config
t	filepaths
=	lambda still	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda functions
s	ls	List deployed functions
s	deploy	Deploy a function if one with the same parameters doesn't exist
s	rmall	Remove all functions in a region
s	rm	Remove a function
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda functions	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda functions	--config
t	filepaths
=	lambda functions	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda functions ls
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda functions ls	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda functions ls	--config
t	filepaths
=	lambda functions ls	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda functions deploy
o	--memory	Amount of memory in MB to allocate	v
o	--disk	Amount of disk space in MB to allocate	v
o	--architecture	Type of CPU architecture to use for the Lambda function	v
o	--disable-cloudwatch	Disable CloudWatch logging	
o	--enable-lambda-insights	Enable Lambda Insights	
o	--custom-role-arn	Set a custom role ARN to be used instead of the default	v
o	--retention-period	CloudWatch log retention period in days	v
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda functions deploy	--architecture
v	x86_64	
v	arm64	
=	lambda functions deploy	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda functions deploy	--config
t	filepaths
=	lambda functions deploy	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda functions rmall
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda functions rmall	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda functions rmall	--config
t	filepaths
=	lambda functions rmall	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda functions rm
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
a	1	0
=	lambda functions rm	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda functions rm	--config
t	filepaths
=	lambda functions rm	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda sites
s	ls	List sites
s	rmall	Remove all sites in a region
s	rm	Remove a site
s	create	Create or update a site
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda sites	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda sites	--config
t	filepaths
=	lambda sites	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda sites ls
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda sites ls	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda sites ls	--config
t	filepaths
=	lambda sites ls	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda sites rmall
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
=	lambda sites rmall	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda sites rmall	--config
t	filepaths
=	lambda sites rmall	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda sites rm
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
a	1	0
=	lambda sites rm	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda sites rm	--config
t	filepaths
=	lambda sites rm	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
@	lambda sites create
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--yes	Skip confirmation	
o	--region	The AWS region specifier	v
o	--site-name		v
a	1	0
=	lambda sites create	--log
v	verbose	
v	info	
v	warn	
v	error	
=	lambda sites create	--config
t	filepaths
=	lambda sites create	--region
v	us-east-1	North Virginia
v	us-east-2	Ohio
v	eu-central-1	Frankfurt
v	eu-west-1	Ireland
v	eu-west-2	London
v	us-west-2	Oregon
v	ap-south-1	Mumbai
v	ap-southeast-1	Singapore
v	ap-southeast-2	Sydney
v	ap-northeast-1	Tokyo
#	lambda sites create	1
t	filepaths
@	bundle
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--public-dir	Location of the public/ directory	v
o	--out-dir	Define the location of the resulting bundle	v
a	1	0
=	bundle	--log
v	verbose	
v	info	
v	warn	
v	error	
=	bundle	--config
t	filepaths
=	bundle	--public-dir
t	folders
=	bundle	--out-dir
t	folders
#	bundle	1
t	filepaths
@	render
o	--disable-headless	Run Chrome in normal mode rather than headless	
o	--gl	Which OpenGL renderer to use	v
o	--user-agent	User agent to use for Chrome during rendering	
o	--ignore-certificate-errors	Ignore SSL errors	
o	--disable-web-security	Disable CORS and other web security features	
o	--timeout	The time in milisecond that a delayRender() may take before it times out	
o	--quality	Quality for rendered frames, JPEG only, 0-100	v
o	--scale	Upscale or downscale or the dimensions of the video	v
o	--codec	Video or audio codec	v
o	--audio-codec	Codec to be used for the audio	v
o	--every-nth-frame	Render only every nth frame (only for GIFs)	v
o	--number-of-gif-loops	How many times a GIF should loop. 0 = No loop	v
o	--audio-bitrate	Customize the output audio bitrate	
o	--video-bitrate	Customize the output video bitrate. Mutually exclusive with --crf	
o	--crf	FFMPEG CRF value, controls quality, see docs for info	
o	--frames	Render a portion or a still of a video, 0-9, 50	v
o	--prores-profile	ProRes profile, need --codec=prores to be set	v
o	--x264-preset	Presets balance encoding speed and compression quality, with slower presets achieving better…	v
o	--image-format	Format to render the frames in, "jpeg" or "png"	v
o	--pixel-format	Custom pixel format, see docs for available values	v
o	--muted	Outputs no audio	
o	--height	Override the composition height	v
o	--width	Override the composition width	v
o	--sequence	Output as an image sequence	
o	--concurrency	How many frames to render in parallel	
o	--enforce-audio-track	Include an audio track even if it's silent	
o	--repro	Collect information that you can submit to Remotion if asked for a reproduction	
o	--env-file	Specify a location for a dotenv file	v
o	--overwrite	Overwrite if file exists, default true	
o	--browser-executable	Custom path for browser executable	v
o	--enable-extensions	Enable Chrome browser extensions while rendering	
o	--ffmpeg-executable	Custom path for FFMPEG executable	v
o	--ffprobe-executable	Custom path for FFProbe executable	v
o	--bundle-cache	Cache webpack bundle, boolean, default true	
o	--port	Custom port to use for the HTTP server	v
o	--public-dir	Location of the public/ directory	v
o	--props	Pass input props as filename or as JSON	v
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
a	3	0
=	render	--gl
v	angle	
v	egl	
v	swiftshader	
v	swangle	
v	vulkan	
=	render	--quality
v	0	
v	10	
v	20	
v	30	
v	40	
v	50	
v	60	
v	70	
v	80	
v	90	
v	100	
=	render	--scale
v	0.25	
v	0.5	
v	1	
v	1.5	
v	2	
v	4	
=	render	--codec
v	h264	
v	h265	
v	gif	
v	vp8	
v	vp9	
v	mp3	
v	aac	
v	wav	
v	prores	
v	h264-mkv	
=	render	--audio-codec
v	aac	
v	mp3	
v	opus	
v	pcm-16	
=	render	--every-nth-frame
v	2	
v	3	
v	4	
v	5	
=	render	--number-of-gif-loops
v	0	
v	1	
v	2	
v	3	
=	render	--prores-profile
v	4444-xq	
v	4444	
v	hq	
v	standard	
v	light	
v	proxy	
=	render	--x264-preset
v	ultrafast	
v	superfast	
v	veryfast	
v	faster	
v	fast	
v	medium	
v	slow	
v	slower	
v	veryslow	
v	placebo	
=	render	--image-format
v	jpeg	
v	png	
=	render	--pixel-format
v	yuv420p	
v	yuv422p	
v	yuv444p	
v	yuv420p10le	
v	yuv422p10le	
v	yuv444p10le	
v	yuva420p	
=	render	--env-file
t	filepaths
=	render	--browser-executable
t	filepaths
=	render	--ffmpeg-executable
t	filepaths
=	render	--ffprobe-executable
t	filepaths
=	render	--public-dir
t	folders
=	render	--props
t	filepaths
=	render	--log
v	verbose	
v	info	
v	warn	
v	error	
=	render	--config
t	filepaths
#	render	1
t	filepaths
#	render	3
v	out.mp4	
t	filepaths
@	still
o	--frame	Which frame to render (default 0)	v
o	--height	Override the composition height	v
o	--width	Override the composition width	v
o	--env-file	Specify a location for a dotenv file	v
o	--overwrite	Overwrite if file exists, default true	
o	--browser-executable	Custom path for browser executable	v
o	--enable-extensions	Enable Chrome browser extensions while rendering	
o	--ffmpeg-executable	Custom path for FFMPEG executable	v
o	--ffprobe-executable	Custom path for FFProbe executable	v
o	--bundle-cache	Cache webpack bundle, boolean, default true	
o	--port	Custom port to use for the HTTP server	v
o	--public-dir	Location of the public/ directory	v
o	--props	Pass input props as filename or as JSON	v
o	--disable-headless	Run Chrome in normal mode rather than headless	
o	--gl	Which OpenGL renderer to use	v
o	--user-agent	User agent to use for Chrome during rendering	
o	--ignore-certificate-errors	Ignore SSL errors	
o	--disable-web-security	Disable CORS and other web security features	
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
a	3	0
=	still	--env-file
t	filepaths
=	still	--browser-executable
t	filepaths
=	still	--ffmpeg-executable
t	filepaths
=	still	--ffprobe-executable
t	filepaths
=	still	--public-dir
t	folders
=	still	--props
t	filepaths
=	still	--gl
v	angle	
v	egl	
v	swiftshader	
v	swangle	
v	vulkan	
=	still	--log
v	verbose	
v	info	
v	warn	
v	error	
=	still	--config
t	filepaths
#	still	1
t	filepaths
#	still	3
v	out.png	
t	filepaths
@	preview
o	--props	Pass input props as filename or as JSON	v
o	--disable-keyboard-shortcuts	Disable all keyboard shortcuts	
o	--webpack-poll	Enable webpack polling instead of file system watchers	v
o	--number-of-shared-audio-tags	Set the number of shared audio tags to prevent autoplay issues	v
o	--no-open	Prevent the browser from opening automatically when the server starts	
a	1	0
=	preview	--props
t	filepaths
#	preview	1
t	filepaths
@	upgrade
o	--package-manager	Force a specific package manager to be used	v
o	--version	Upgrade to a specific version	v
=	upgrade	--package-manager
v	npm	
v	yarn	
v	pnpm	
@	benchmark
o	--disable-headless	Run Chrome in normal mode rather than headless	
o	--gl	Which OpenGL renderer to use	v
o	--user-agent	User agent to use for Chrome during rendering	
o	--ignore-certificate-errors	Ignore SSL errors	
o	--disable-web-security	Disable CORS and other web security features	
o	--timeout	The time in milisecond that a delayRender() may take before it times out	
o	--quality	Quality for rendered frames, JPEG only, 0-100	v
o	--scale	Upscale or downscale or the dimensions of the video	v
o	--codec	Video or audio codec	v
o	--audio-codec	Codec to be used for the audio	v
o	--every-nth-frame	Render only every nth frame (only for GIFs)	v
o	--number-of-gif-loops	How many times a GIF should loop. 0 = No loop	v
o	--audio-bitrate	Customize the output audio bitrate	
o	--video-bitrate	Customize the output video bitrate. Mutually exclusive with --crf	
o	--crf	FFMPEG CRF value, controls quality, see docs for info	
o	--frames	Render a portion or a still of a video, 0-9, 50	v
o	--prores-profile	ProRes profile, need --codec=prores to be set	v
o	--x264-preset	Presets balance encoding speed and compression quality, with slower presets achieving better…	v
o	--image-format	Format to render the frames in, "jpeg" or "png"	v
o	--pixel-format	Custom pixel format, see docs for available values	v
o	--muted	Outputs no audio	
o	--height	Override the composition height	v
o	--width	Override the composition width	v
o	--sequence	Output as an image sequence	
o	--enforce-audio-track	Include an audio track even if it's silent	
o	--repro	Collect information that you can submit to Remotion if asked for a reproduction	
o	--env-file	Specify a location for a dotenv file	v
o	--browser-executable	Custom path for browser executable	v
o	--enable-extensions	Enable Chrome browser extensions while rendering	
o	--ffmpeg-executable	Custom path for FFMPEG executable	v
o	--ffprobe-executable	Custom path for FFProbe executable	v
o	--bundle-cache	Cache webpack bundle, boolean, default true	
o	--port	Custom port to use for the HTTP server	v
o	--public-dir	Location of the public/ directory	v
o	--props	Pass input props as filename or as JSON	v
o	--quiet	Print less output	
o	-q	Print less output	
o	--log	Log level, "error", "warning", "verbose", "info" (default)	v
o	--config	Custom location for a Remotion config file	v
o	--concurrencies	Comma-separated list of concurrency values to include in benchmark	
=	benchmark	--gl
v	angle	
v	egl	
v	swiftshader	
v	swangle	
v	vulkan	
=	benchmark	--quality
v	0	
v	10	
v	20	
v	30	
v	40	
v	50	
v	60	
v	70	
v	80	
v	90	
v	100	
=	benchmark	--scale
v	0.25	
v	0.5	
v	1	
v	1.5	
v	2	
v	4	
=	benchmark	--codec
v	h264	
v	h265	
v	gif	
v	vp8	
v	vp9	
v	mp3	
v	aac	
v	wav	
v	prores	
v	h264-mkv	
=	benchmark	--audio-codec
v	aac	
v	mp3	
v	opus	
v	pcm-16	
=	benchmark	--every-nth-frame
v	2	
v	3	
v	4	
v	5	
=	benchmark	--number-of-gif-loops
v	0	
v	1	
v	2	
v	3	
=	benchmark	--prores-profile
v	4444-xq	
v	4444	
v	hq	
v	standard	
v	light	
v	proxy	
=	benchmark	--x264-preset
v	ultrafast	
v	superfast	
v	veryfast	
v	faster	
v	fast	
v	medium	
v	slow	
v	slower	
v	veryslow	
v	placebo	
=	benchmark	--image-format
v	jpeg	
v	png	
=	benchmark	--pixel-format
v	yuv420p	
v	yuv422p	
v	yuv444p	
v	yuv420p10le	
v	yuv422p10le	
v	yuv444p10le	
v	yuva420p	
=	benchmark	--env-file
t	filepaths
=	benchmark	--browser-executable
t	filepaths
=	benchmark	--ffmpeg-executable
t	filepaths
=	benchmark	--ffprobe-executable
t	filepaths
=	benchmark	--public-dir
t	folders
=	benchmark	--props
t	filepaths
=	benchmark	--log
v	verbose	
v	info	
v	warn	
v	error	
=	benchmark	--config
t	filepaths
@	install
a	1	0
#	install	1
v	ffmpeg	
v	ffprobe	
