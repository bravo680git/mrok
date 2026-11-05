@	
s	-listnetworkserviceorder	Displays a list of network services in the order they are contacted for a connection, along with…
s	-listallnetworkservices	Displays a list of all the network services on the server's hardware ports
s	-listallhardwareports	Displays list of hardware ports with corresponding device name and ethernet address
s	-detectnewhardware	Detects new network hardware and creates a default network service on the hardware
s	-getmacaddress	Displays ethernet (or Wi-Fi) address for hardwareport or device specified
s	-getcomputername	Displays the computer name
s	-setcomputername	Sets computer name to <computername>. This name is used by AFP
s	-getinfo	Displays the IP address, subnet mask, router, and hardware address for the <networkservice> that…
s	-setmanual	Set the TCP/IP configuration for <networkservice> to manual with IP address set to <ip>, Subnet…
s	-setdhcp	Use this command to set the TCP/IP configuration for the specified <networkservice> to use DHCP…
s	-setbootp	Use this command to set the TCP/IP configuration for the specified <networkservice> to use BOOTP
s	-setmanualwithdhcprouter	Use this command to specify a manual IP address to use for DHCP for the specified <networkservice>
s	-getadditionalroutes	Use this command to display the list of additional IPv4 routes configured for the service
s	-setadditionalroutes	Use this command to set the list of IPv4 additional routes configured for the service. Each route…
s	-setv4off	Use this command to turn IPv4 off on the specified <networkservice>
s	-setv6off	Use this command to turn IPv6 off on the specified <networkservice>
s	-setv6automatic	Use this command to set IPv6 to get its addresses automatically for <networkservice>
s	-setv6linklocal	Use this command to set IPv6 to only use link local for <networkservice>
s	-setv6manual	Use this command to set IPv6 to get its addresses manually for <networkservice>. Specify the ip…
s	-getv6additionalroutes	Use this command to display the list of additional IPv6 routes configured for the service
s	-setv6additionalroutes	Use this command to set the list of additional routes configured for the service. Each route is…
s	-getdnsservers	Displays DNS info for <networkservice>
s	-setdnsservers	Use this command to specify the IP addresses of servers you want the specified <networkservice> to…
s	-getsearchdomains	Displays Domain Name info for <networkservice>
s	-setsearchdomains	Use this command to designate the search domain for the specified <networkservice>. You can list…
s	-create6to4service	Use this command to create a new 6 to 4 service with name <newnetworkservicename>
s	-set6to4automatic	Use this command to set the 6 to 4 service such that it will get the relay address automatically
s	-set6to4manual	Use this command to set the 6 to 4 service such that it will get the relay address manually…
s	-getwebproxy	Displays Web proxy (server, port, enabled value) info for <networkservice>
s	-setwebproxy	Set Web proxy for <networkservice> with <domain> and <port number>. Turns proxy on. Optionally…
s	-setwebproxystate	Set Web proxy on <networkservice> to either <on> or <off>
s	-getsecurewebproxy	Displays Secure Web proxy (server, port, enabled value) info for <networkservice>
s	-setsecurewebproxy	Set Secure Web proxy for <networkservice> with <domain> and <port number>. Turns proxy on…
s	-setsecurewebproxystate	Set Secure Web proxy on <networkservice> to either <on> or <off>
s	-getsocksfirewallproxy	Displays SOCKS Firewall proxy (server, port, enabled value) info for <networkservice>
s	-setsocksfirewallproxy	Set SOCKS Firewall proxy for <networkservice> with <domain> and <port number>. Turns proxy on…
s	-setsocksfirewallproxystate	Set SOCKS Firewall proxy to either <on> or <off>
s	-getproxybypassdomains	Displays Bypass Domain Names for <networkservice>
s	-setproxybypassdomains	Set the Bypass Domain Name Servers for <networkservice> to <domain1> [domain2] [...]. Any number…
s	-getproxyautodiscovery	Displays Proxy Auto Discover for <networkservice>
s	-setproxyautodiscovery	Set Proxy Auto Discover for <networkservice> to either <on> or <off>
s	-setautoproxyurl	Set proxy auto-config to url for <networkservice> and enable it
s	-getautoproxyurl	Displays proxy auto-config (url, enabled) info for <networkservice>
s	-getairportnetwork	Displays current Wi-Fi Network
s	-setairportnetwork	Set Wi-Fi Network to <network> using optional [password] if specified
s	-getairportpower	Displays whether Wi-Fi power is on or off
s	-setairportpower	Set Wi-Fi power to either <on> or <off>
s	-listpreferredwirelessnetworks	List the preferred wireless networks for <hardwareport>
s	-addpreferredwirelessnetworkatindex	Add wireless network named <network> to preferred list for <hardwareport> at <index>. Store the…
s	-removepreferredwirelessnetwork	Remove <network> from the preferred wireless network list for <hardwareport>
s	-removeallpreferredwirelessnetworks	Remove all networks from the preferred wireless network list for <hardwareport>
s	-getnetworkserviceenabled	Displays whether a service is on or off (enabled or disabled)
s	-setnetworkserviceenabled	Use this command to turn the specified network service on or off (enable or disable)
s	-createnetworkservice	Create a service named <networkservice> on port <hardwareport>. The new service will be enabled by…
s	-renamenetworkservice	Use this command to rename the specified network service <networkservice> to <newnetworkservicename>
s	-duplicatenetworkservice	Use this command to duplicate an existing network service <networkservice> and rename it to the…
s	-removenetworkservice	Use this command to delete a network service <networkservice>. You cannot use this command to…
s	-ordernetworkservices	Use this command to designate the order network services are contacted on the specified hardware…
s	-setMTUAndMediaAutomatically	Set hardwareport or device specified back to automatically setting the MTU and Media
s	-getMTU	Get the MTU value for hardwareport or device specified
s	-setMTU	Set MTU for hardwareport or device specified
s	-listValidMTURange	List the valid MTU range for hardwareport or device specified
s	-getMedia	Show both the current setting for media and the active media on hardwareport or device specified
s	-setMedia	Set media for hardwareport or device specified to subtype. Specify optional [option1] and…
s	-listValidMedia	List valid media options for hardwareport or device name. Enumerates available subtypes and…
s	-createVLAN	Create a VLAN with the name <name> over the parent device <parentdevice> and with the tag <tag>
s	-deleteVLAN	Delete the VLAN with the name <name> over the parent device <parentdevice> and with the tag <tag>
s	-listVLANs	List the VLANs that have been created
s	-listdevicesthatsupportVLAN	List the devices that support VLANs
s	-isBondSupported	Displays YES if the device can be added to a bond. NO if it cannot
s	-createBond	Create a bond with the user-defined-name name and optionally add any listed devices if they…
s	-deleteBond	Delete the bond with the specified device-name
s	-addDeviceToBond	Add device to bond
s	-removeDeviceFromBond	Remove device from bond
s	-listBonds	List of all bonds
s	-showBondStatus	Display the status of the specified bond
s	-listpppoeservices	List all PPPoE services in the current set
s	-showpppoestatus	Display the status of the PPPoE service with the specified name
s	-createpppoeservice	Create a PPPoE service on the specified device with the service name specified
s	-deletepppoeservice	Delete the service
s	-setpppoeaccountname	Set the account name for the service
s	-setpppoepassword	Set the password for the service
s	-connectpppoeservice	Connect the service
s	-disconnectpppoeservice	Disconnect the service
s	-listlocations	List all network locations
s	-getcurrentlocation	Display the name of the current set
s	-createlocation	Create a set with the user-defined-name name and optionally populate it with the default services
s	-deletelocation	Delete the set
s	-switchtolocation	Make the specified set the current set
s	-version	Displays version of networksetup tool
s	-help	Displays a list of all the commands available in the Network Setup Tool, with explanatory…
s	-printcommands	Displays a list of commands with no detail
@	-listnetworkserviceorder
@	-listallnetworkservices
@	-listallhardwareports
@	-detectnewhardware
@	-getmacaddress
a	1	0
#	-getmacaddress	1
d
@	-getcomputername
@	-setcomputername
a	1	0
@	-getinfo
a	1	0
#	-getinfo	1
d
@	-setmanual
a	4	0
#	-setmanual	1
d
@	-setdhcp
a	2	0
#	-setdhcp	1
d
@	-setbootp
a	1	0
#	-setbootp	1
d
@	-setmanualwithdhcprouter
a	2	0
#	-setmanualwithdhcprouter	1
d
@	-getadditionalroutes
a	1	0
#	-getadditionalroutes	1
d
@	-setadditionalroutes
a	2	1
#	-setadditionalroutes	1
d
@	-setv4off
a	1	0
#	-setv4off	1
d
@	-setv6off
a	1	0
#	-setv6off	1
d
@	-setv6automatic
a	1	0
#	-setv6automatic	1
d
@	-setv6linklocal
a	1	0
#	-setv6linklocal	1
d
@	-setv6manual
a	3	0
@	-getv6additionalroutes
a	1	0
#	-getv6additionalroutes	1
d
@	-setv6additionalroutes
a	2	1
#	-setv6additionalroutes	1
d
@	-getdnsservers
a	1	0
#	-getdnsservers	1
d
@	-setdnsservers
a	2	1
#	-setdnsservers	1
d
@	-getsearchdomains
a	1	0
#	-getsearchdomains	1
d
@	-setsearchdomains
a	2	1
#	-setsearchdomains	1
d
@	-create6to4service
a	1	0
@	-set6to4automatic
a	1	0
@	-set6to4manual
a	2	0
@	-getwebproxy
a	1	0
#	-getwebproxy	1
d
@	-setwebproxy
a	6	0
#	-setwebproxy	1
d
#	-setwebproxy	4
v	on	Specify <on> for <authenticated> to enable authenticated proxy support
v	off	Specify <off> for <authenticated> to disable authenticated proxy support
@	-setwebproxystate
a	2	0
#	-setwebproxystate	1
d
#	-setwebproxystate	2
v	on	
v	off	
@	-getsecurewebproxy
a	1	0
#	-getsecurewebproxy	1
d
@	-setsecurewebproxy
a	6	0
#	-setsecurewebproxy	1
d
#	-setsecurewebproxy	4
v	on	Specify <on> for <authenticated> to enable authenticated proxy support
v	off	Specify <off> for <authenticated> to disable authenticated proxy support
@	-setsecurewebproxystate
a	2	0
#	-setsecurewebproxystate	1
d
#	-setsecurewebproxystate	2
v	on	
v	off	
@	-getsocksfirewallproxy
a	1	0
#	-getsocksfirewallproxy	1
d
@	-setsocksfirewallproxy
a	6	0
#	-setsocksfirewallproxy	1
d
#	-setsocksfirewallproxy	4
v	on	Specify <on> for <authenticated> to enable authenticated proxy support
v	off	Specify <off> for <authenticated> to disable authenticated proxy support
@	-setsocksfirewallproxystate
a	2	0
#	-setsocksfirewallproxystate	1
d
#	-setsocksfirewallproxystate	2
v	on	
v	off	
@	-getproxybypassdomains
a	1	0
#	-getproxybypassdomains	1
d
@	-setproxybypassdomains
a	2	1
#	-setproxybypassdomains	1
d
@	-getproxyautodiscovery
a	1	0
#	-getproxyautodiscovery	1
d
@	-setproxyautodiscovery
a	2	0
#	-setproxyautodiscovery	1
d
#	-setproxyautodiscovery	2
v	on	
v	off	
@	-setautoproxyurl
a	2	0
#	-setautoproxyurl	1
d
@	-getautoproxyurl
a	1	0
#	-getautoproxyurl	1
d
@	-getairportnetwork
a	1	0
#	-getairportnetwork	1
d
@	-setairportnetwork
a	3	0
#	-setairportnetwork	1
d
@	-getairportpower
a	1	0
#	-getairportpower	1
d
@	-setairportpower
a	2	0
#	-setairportpower	1
d
#	-setairportpower	2
v	on	
v	off	
@	-listpreferredwirelessnetworks
a	1	0
#	-listpreferredwirelessnetworks	1
d
@	-addpreferredwirelessnetworkatindex
a	5	0
#	-addpreferredwirelessnetworkatindex	1
d
#	-addpreferredwirelessnetworkatindex	4
v	OPEN	No security
v	WPA	WPA Personal
v	WPA2	WPA2 Personal
v	WPA/WPA2	WPA/WPA2 Personal
v	WPAE	WPA Enterprise
v	WPA2E	WPA2 Enterprise
v	WPAE/WPA2E	WPA/WPA2 Enterprise
v	WEP	Plain WEP
v	8021XWEP	802.1X WEP
@	-removepreferredwirelessnetwork
a	2	0
#	-removepreferredwirelessnetwork	1
d
@	-removeallpreferredwirelessnetworks
a	1	0
#	-removeallpreferredwirelessnetworks	1
d
@	-getnetworkserviceenabled
a	1	0
#	-getnetworkserviceenabled	1
d
@	-setnetworkserviceenabled
a	2	0
#	-setnetworkserviceenabled	1
d
#	-setnetworkserviceenabled	2
v	on	
v	off	
@	-createnetworkservice
a	2	0
#	-createnetworkservice	2
d
@	-renamenetworkservice
a	2	0
#	-renamenetworkservice	1
d
@	-duplicatenetworkservice
a	2	0
#	-duplicatenetworkservice	1
d
@	-removenetworkservice
a	1	0
#	-removenetworkservice	1
d
@	-ordernetworkservices
a	1	1
#	-ordernetworkservices	1
d
@	-setMTUAndMediaAutomatically
a	1	0
#	-setMTUAndMediaAutomatically	1
d
@	-getMTU
a	1	0
#	-getMTU	1
d
@	-setMTU
a	2	0
#	-setMTU	1
d
@	-listValidMTURange
a	1	0
#	-listValidMTURange	1
d
@	-getMedia
a	1	0
#	-getMedia	1
d
@	-setMedia
a	3	1
#	-setMedia	1
d
@	-listValidMedia
a	1	0
#	-listValidMedia	1
d
@	-createVLAN
a	3	0
#	-createVLAN	2
d
@	-deleteVLAN
a	3	0
#	-deleteVLAN	2
d
@	-listVLANs
@	-listdevicesthatsupportVLAN
@	-isBondSupported
a	1	0
#	-isBondSupported	1
d
@	-createBond
a	2	1
#	-createBond	2
d
@	-deleteBond
a	1	0
#	-deleteBond	1
d
@	-addDeviceToBond
a	2	0
#	-addDeviceToBond	1
d
#	-addDeviceToBond	2
d
@	-removeDeviceFromBond
a	2	0
#	-removeDeviceFromBond	1
d
#	-removeDeviceFromBond	2
d
@	-listBonds
@	-showBondStatus
a	1	0
#	-showBondStatus	1
d
@	-listpppoeservices
@	-showpppoestatus
a	1	0
#	-showpppoestatus	1
d
@	-createpppoeservice
a	5	0
#	-createpppoeservice	1
d
@	-deletepppoeservice
a	1	0
#	-deletepppoeservice	1
d
@	-setpppoeaccountname
a	2	0
#	-setpppoeaccountname	1
d
@	-setpppoepassword
a	2	0
#	-setpppoepassword	1
d
@	-connectpppoeservice
a	1	0
#	-connectpppoeservice	1
d
@	-disconnectpppoeservice
a	1	0
#	-disconnectpppoeservice	1
d
@	-listlocations
@	-getcurrentlocation
@	-createlocation
a	2	0
@	-deletelocation
a	1	0
#	-deletelocation	1
d
@	-switchtolocation
a	1	0
#	-switchtolocation	1
d
@	-version
@	-help
@	-printcommands
