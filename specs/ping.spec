@	
o	-A	Audible. Output a bell (ASCII 0x07) character when no packet is received before the next packet is…	
o	-a	Audible. Include a bell (ASCII 0x07) character in the output when any packet is received. This…	
o	-b	Bind the socket to interface boundif for sending. This option is an Apple addition	v
o	-C	Prohibit the socket from using the cellular network interface. This option is an Apple addition	
o	-c	Stop after sending (and receiving) count ECHO_RESPONSE packets. If this option is not specified…	v
o	-D	Set the Don't Fragment bit	
o	-d	Set the SO_DEBUG option on the socket being used	
o	-f	Flood ping. Outputs packets as fast as they come back or one hundred times per second, whichever…	
o	-G	Sweepmaxsize Specify the maximum size of ICMP payload when sending sweeping pings. This option is…	v
o	-g	Specify the size of ICMP payload to start with when sending sweeping pings	v
o	-h	Specify the number of bytes to increment the size of ICMP payload after each sweep when sending…	v
o	-I	Source multicast packets with the given interface address. This flag only applies if the ping…	v
o	-i	Wait wait seconds between sending each packet. The default is to wait for one second between each…	v
o	-k	Specifies the traffic class to use for sending ICMP packets. By default ping uses the control…	v
o	-K	Specifies the network service type to use for sending ICMP pack- ets. Note this overrides the…	v
o	-L	Suppress loopback of multicast packets. This flag only applies if the ping destination is a…	
o	-l	If preload is specified, ping sends that many packets as fast as possible before falling into its…	v
o	-M	Use ICMP_MASKREQ or ICMP_TSTAMP instead of ICMP_ECHO. For mask, print the netmask of the remote…	v
o	-m	Set the IP Time To Live for outgoing packets. If not specified, the kernel uses the value of the…	v
o	-n	Numeric output only. No attempt will be made to lookup symbolic names for host addresses	
o	-o	Exit successfully after receiving one reply packet	
o	-P	Policy specifies IPsec policy for the ping session. For details please refer to ipsec(4) and…	v
o	-p	You may specify up to 16 'pad' bytes to fill out the packet you send. This is useful for…	v
o	-Q	Somewhat quiet output. Don't display ICMP error messages that are in response to our query…	
o	-q	Quiet output. Nothing is displayed except the summary lines at startup time and when finished	
o	-R	Record route. Includes the RECORD_ROUTE option in the ECHO_REQUEST packet and displays the route…	
o	-r	Bypass the normal routing tables and send directly to a host on an attached network. If the host…	
o	-S	Use the following IP address as the source address in outgoing packets. On hosts with more than…	v
o	-s	Specify the number of data bytes to be sent. The default is 56, which translates into 64 ICMP data…	v
o	-T	Set the IP Time To Live for multicasted packets. This flag only applies if the ping destination is…	v
o	-t	Specify a timeout, in seconds, before ping exits regardless of how many packets have been received	v
o	-v	Verbose output. ICMP packets other than ECHO_RESPONSE that are received are listed	
o	-W	Time in milliseconds to wait for a reply for each packet sent. If a reply arrives later, the…	v
o	-z	Use the specified type of service	v
o	--apple-connect	Connects the socket to the destination address	
o	--apple-time	Prints the time a packet was received	
a	1	0
=		-k
v	BK_SYS	
v	BK	
v	BE	
v	RD	
v	OAM	
v	AV	
v	RV	
v	VI	
v	VO	
v	CTL	
=		-K
v	BK_SYS	
v	BK	
v	BE	
v	RV	
v	AV	
v	RD	
v	OAM	
v	VI	
v	SIG	
v	VO	
