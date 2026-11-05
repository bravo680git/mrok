@	
o	-a|--all-sites	Use all sites for scan	
o	--version	Display version information and dependencies	
o	--timeout	Time in seconds to wait for response to requests (default {settings.timeout}s). A longer timeout…	v
o	--retries	Attempts to restart temporarily failed requests	v
o	-n|--max-connections	Allowed number of concurrent connections (default {settings.max_connections})	v
o	--no-recursion	Disable recursive search by additional data extracted from pages	
o	--no-extracting	Disable parsing pages for additional data and other usernames	
o	--id-type	Specify identifier(s) type (default: username)	v
o	--db	Load Maigret database from a JSON file or HTTP web resource	v
o	--cookies-jar-file	File with cookies	v
o	--ignore-ids	Do not make search by the specified username or other ids	v
o	-fo|--folderoutput	If using multiple usernames, the output of the results will be saved to this folder	v
o	-p|--proxy	Make requests over a proxy. e.g. socks5://127.0.0.1:1080	v
o	--tor-proxy	Specify URL of your Tor gateway. Default is socks5://127.0.0.1:9050	v
o	--i2p-proxy	Specify URL of your I2P gateway. Default is http://127.0.0.1:4444	v
o	--with-domains	Enable (experimental) feature of checking domains on usernames	
o	--tags	Specify tags of sites (see `--stats`)	v
o	--site	Limit analysis to just the specified sites (multiple option)	v
o	--use-disabled-sites	Use disabled sites to search (may cause many false positives)	
o	--parse	Parse page by URL and extract username and IDs to use for search	v
o	--submit	URL of existing profile in new site to submit	v
o	--self-check	Do self check for sites and database and disable non-working ones	
o	--stats	Show database statistics (most frequent sites engines and tags)	
o	--print-not-found	Print sites where the username was not found	
o	--print-errors	Print errors messages: connection, captcha, site country ban, etc	
o	-v|--verbose	Display extra information and metrics	
o	-info|--vv	Display extra/service information and metrics	
o	--debug|-vvv|-d	Display extra/service/debug information and metrics, save responses in debug.log	
o	--no-color	Don't color terminal output	
o	--no-progressbar	Don't show progressbar	
o	-T|--txt	Create a TXT report (one report per username)	
o	-C|--csv	Create a CSV report (one report per username)	
o	-H|--html	Create an HTML report (one report per username)	
o	-X|--xmind	Create a XMind 8 mindmap report (one report per username)	
o	-P|--pdf	Create a PDF report (one report per username)	
o	-G|--graph	Create a graph report (one report per username)	
o	-J|--json	Generate a JSON report of specific type: simple, ndjson (one report per username)	v
o	--reports-sorting	Method of results sorting in reports (default: in order of getting the result)	v
a	1	1
=		--id-type
v	username	
v	yandex_public_id	
v	gaia_id	
v	vk_id	
v	ok_id	
v	wikimapia_uid	
v	steam_id	
v	uidme_uguid	
v	yelp_userid	
=		--db
t	filepaths
=		--cookies-jar-file
t	filepaths
=		-fo
t	folders
=		-J
v	simple	
v	ndjson	
=		--reports-sorting
v	default	
v	data	
