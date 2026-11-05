@	
s	attach	Connect an Ubuntu Pro support contract to this machine
s	collect-logs	Create a tarball with all relevant logs and debug data
s	detach	Remove Ubuntu Pro from this machine
s	disable	Disable this machine's access to an Ubuntu Pro service
s	enable	Activate and configure this machine's access to an Ubuntu Pro service
s	fix	Fix a CVE or USN on the system by upgrading the appropriate package(s)
s	refresh	Refresh contract and service details from Canonical
s	security-status	Show security updates for packages in the system, including all available ESM related content
s	status	Report current status of Ubuntu Pro services on system
@	attach
o	--no-auto-enable	Disable the automatic enablement of recommended entitlements	
o	--attach-config	Provide a file with configuration options	v=
a	1	0
=	attach	--attach-config
t	filepaths
@	collect-logs
o	-o|--output	Path for tarball. Uses ua_logs.tar.gz in current directory if not specified	v
=	collect-logs	-o
t	filepaths
@	detach
@	disable
a	1	0
#	disable	1
v	cc-eal	
v	cis	
v	esm	
v	fips	
v	fips-updates	
v	livepatch	
v	ros	
v	ros-updates	
@	enable
a	1	0
#	enable	1
v	cc-eal	
v	cis	
v	esm	
v	fips	
v	fips-updates	
v	livepatch	
v	ros	
v	ros-updates	
@	fix
a	1	0
@	refresh
@	security-status
@	status
o	--format	Output format	v=
o	--simulate-with-token		v
o	--all	Include beta and unavailable services	
=	status	--format
v	tabular	
v	json	
v	yaml	
