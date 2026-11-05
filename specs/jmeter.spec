@	
o	-v|--version	Print the JMeter version information and exit	
o	-h|--help	Print usage information and exit	
o	-p|--propfile	The jmeter property file to use	v
o	-q|--addprop	Additional JMeter property file(s)	v
o	-t|--testfile	The JMeter test(.jmx) file to run. "-t LAST" will load last used file	v
o	-l|--logfile	The file to log samples to	v
o	-i|--jmeterlogconf	JMeter logging configuration file	v
o	-j|--jmeterlogfile	JMeter run log file	v
o	-n|--nongui	Run JMeter in nongui mode	
o	-s|--server	Run the JMeter server	
o	-E|--proxyScheme	Set a proxy scheme to use for the proxy server	v
o	-H|--proxyHost	Set a proxy server for JMeter to use	v
o	-P|--proxyPort	Set proxy server port for JMeter to use	v
o	-N|--nonProxyHosts	Set nonproxy host list (e.g. *.apache.org|localhost)	v
o	-u|--username	Set username for proxy server that JMeter is to use	v
o	-a|--password	Set password for proxy server that JMeter is to use	v
o	-J|--jmeterproperty	Define additional JMeter properties <argument>=<value>	v
o	-G|--globalproperty	Define Global properties (sent to servers) e.g. -Gport=123 or -Gglobal.properties	v
o	-D|--systemproperty	Define additional system properties <argument>=<value>	v
o	-S|--systemPropertyFile	Additional system property file(s)	v
o	-f|--forceDeleteResultFile	Force delete existing results files and web report folder	
o	-L|--loglevel	[category=]level e.g. jorphan=INFO, jmeter.util=DEBUG or com.example.foo=WARN	v
o	-r|--runremote	Start remote servers (as defined in remote_hosts)	
o	-R|--remotestart	Start these remote servers (overrides remote_hosts)	v
o	-d|--homedir	The JMeter home directory to use	v
o	-X|--remoteexit	Exit the remote servers at end of test (non-GUI)	
o	-g|--reportonly	Generate report dashboard only, from a test results file	
o	-e|--reportatendofloadtests	Generate report dashboard after load test	
o	-o|--reportoutputfolder	Output folder for report dashboard	v
=		-p
t	filepaths
=		-q
t	filepaths
=		-t
t	filepaths
=		-l
t	filepaths
=		-i
t	filepaths
=		-j
t	filepaths
=		-S
t	filepaths
=		-L
v	OFF	
v	FATAL	
v	WARN	
v	INFO	
v	DEBUG	
v	TRACE	
v	ALL	
=		-o
t	folders
