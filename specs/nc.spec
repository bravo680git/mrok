@	
o	-4	Forces nc to use IPv4 addresses only	V
o	-6	Forces nc to use IPv6 addresses only	V
o	-A	Set SO_RECV_ANYIF on socket	V
o	-b	Specifies the interface to bind the socket to	v
o	-c	Send CRLF as line-ending	V
o	-D	Enable debugging on the socket	V
o	-C	Force nc not to use cellular data context	V
o	-d	Do not attempt to read from stdin	V
o	-h	Prints out nc help	V
o	-i	Specifies a delay time interval between lines of text sent and received	v
o	-G	TCP connection timeout in seconds	v
o	-H	Initial TCP keep alive timeout in seconds	v
o	-I	Interval for repeating TCP keep alive timeout in seconds	v
o	-J	Number of times to repeat TCP keep alive packets	v
o	-k	Force nc to stay listening for another connection after its current connection is completed	V
o	-l	Used to specify that nc should listen for an incoming connection rather than initiate a connection…	v
o	-L	Number of prbes to send to the peer before declaring that the peer is not reachable	v
o	-n	Do not do any DNS or service lookups on any specified addresses, hostnames or ports	V
o	-p	Specifies the source port nc should use, subject to privilege restrictions and availability	v
o	-r	Specifies that source and/or destination ports should be chosen randomly instead of sequentially…	V
o	-s	Specifies the IP of the interface which is used to send the packets	v
o	-t	Causes nc to send RFC 854 DON'T and WON'T responses to RFC 854 DO and WILL requests	V
o	-U	Specifies to use Unix Domain Sockets	V
o	-u	Use UDP instead of the default option of TCP	V
o	-v	Have nc give more verbose output	V
o	-w	If a connection and stdin are idle for more than timeout seconds, then the connection is silently…	v
o	-X	Requests that nc should use the specified protocol when talking to the proxy server	v
o	-x	Requests that nc should connect to hostname using a proxy at proxy_address and port	v
o	-z	Specifies that nc should just scan for listening daemons, without sending any data to them	V
o	--apple-delegate-pid	Requests that nc should delegate the socket for the specified PID	V
o	--apple-delegate-uuid	Requests that nc should delegate the socket for the specified UUID	V
o	--apple-ext-bk-idle	Requests that nc marks its socket for extended background idle time when the process becomes…	V
o	--apple-nowakefromsleep	When the parameter n is greater than 0, requests that nc marks its socket to exlude the local port…	V
o	--ecn	Requests that nc marks to use the socket option TCP_ECN_MODE to set the ECN mode	V
a	2	1
=		--ecn
v	default	
v	enable	
v	disable	
