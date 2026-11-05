@	
o	--help|-h	Show help for traceroute	
o	-a	Turn on AS# lookups for each hop encountered	
o	-A	Turn on AS# lookups and use the given server instead of the default	v
o	-d	Enable socket level debugging	
o	-D	When an ICMP response to our probe datagram is received, print the differences between the…	
o	-e	Firewall evasion mode. Use fixed destination ports for UDP and TCP probes. The destination port…	
o	-f	Set the initial time-to-live used in the first outgoing probe packet	v
o	-F	Set the `don't fragment` bit	
o	-g	Specify a loose source route gateway (8 maximum)	v
o	-i	Specify a network interface to obtain the source IP address for outgoing probe packets. This is…	v
o	-I	Use ICMP ECHO instead of UDP datagrams. (A synonym for `-P icmp`)	
o	-M	Set the initial time-to-live value used in outgoing probe packets. The default is 1, i.e., start…	v
o	-m	Set the max time-to-live (max number of hops) used in outgoing probe packets. The default is…	v
o	-n	Print hop addresses numerically rather than symbolically and numerically (saves a nameserver…	
o	-P	Send packets of specified IP protocol. The currently supported protocols are: UDP, TCP, GRE and…	v
o	-p	Protocol specific. For UDP and TCP, sets the base port number used in probes (default is 33434)…	v
o	-q	Set the number of probes per ``ttl'' to nqueries (default is three probes)	v
o	-r	Bypass the normal routing tables and send directly to a host on an attached network. If the host…	
o	-s	Use the following IP address (which must be given as an IP number, not a hostname) as the source…	v
o	-S	Print a summary of how many probes were not answered for each hop	
o	-t	Set the type-of-service in probe packets to the following value (default zero). The value must be…	v
o	-v	Verbose output. Received ICMP packets other than TIME_EXCEEDED and UNREACHABLEs are listed	
o	-w	Set the time (in seconds) to wait for a response to a probe (default 5 sec.)	
o	-x	Toggle IP checksums. Normally, this prevents traceroute from calculating IP checksums. In some…	
o	-z	Set the time (in milliseconds) to pause between probes (default 0). Some systems such as Solaris…	v
a	1	0
