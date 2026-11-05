@	
o	-t	Target website URL. Example: https://ddosify.com	v
o	-n	Total request count. Default: 100	v
o	-d	Test duration in seconds. Default: 10	v
o	-l	Type of the request. Default: linear	v
o	-m	HTTP Methods. Default: GET	v
o	-b	Body for the request	v
o	-a	Basic authentication	v
o	-h	Headers of the request. You can provide multiple headers	v
o	-T	Timeout in seconds. Default: 5	v
o	-P	Proxy address	v
o	-o	Test result output format. Default: stdout	v
o	--config	Config file of the load test i.e example_ddosify_config.json	v
o	--version	Prints version, git commit, built date (utc)	
o	--debug	Iterates the scenario once and prints curl-like verbose result	
o	--help	Prints CLI flags	
=		-l
v	linear	
v	incremental	
v	waved	
=		-m
v	GET	
v	POST	
v	PUT	
v	DELETE	
v	HEAD	
v	PATCH	
v	OPTIONS	
=		-a
v	username:password	
=		-h
v	Content-Type: application/json	
v	User-Agent: DdosifyLoadGenerator/0.8.1	
=		-P
v	http://user:pass@proxy_host.com:port	
=		-o
v	stdout	
v	stdout-json	
