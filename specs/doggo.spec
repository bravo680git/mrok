@	
o	--version	Output version	
o	--help|-h	Output help	
o	-q|--query	Hostname to query the DNS records for (e.g., example.com)	
o	-t|--type	Type of the DNS Record (A, MX, NS, etc.)	
o	-n|--nameserver	Address of a specific nameserver to send queries to (e.g., 9.9.9.9, 8.8.8.8)	
o	-c|--class	Network class of the DNS record (IN, CH, HS, etc.)	
o	-x|--reverse	Performs a reverse DNS lookup for an IPv4 or IPv6 address	
o	--any	Query all supported DNS record types (A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, TXT, CAA)	
o	--strategy	Specify strategy to query nameservers (all, random, first)	=
o	--ndots	Specify ndots parameter	=
o	--search	Use the search list defined in resolv.conf (default: true)	
o	--timeout	Specify timeout (in seconds) for the resolver to return a response	
o	-4|--ipv4	Use IPv4 only	
o	-6|--ipv6	Use IPv4 only	
o	--tls-hostname	Provide a hostname for TLS certificate verification	=
o	--skip-hostname-verification	Skip TLS Hostname Verification for DoT lookups	
o	--aa	Set Authoritative Answer flag	
o	--ad	Set Authenticated Data flag	
o	--cd	Set Checking Disabled flag	
o	--rd	Set Recursion Desired flag (default: true)	
o	--z	Set Z flag (reserved for future use)	
o	--do	Set DNSSEC OK flag	
o	-J|--json	Format the output as JSON	
o	--short	Short output format (shows only the response section)	
o	--color	Enable/disable colored output (default: true)	
o	--debug	Enable debug logging	
o	--time	Show query response time	
a	3	0
