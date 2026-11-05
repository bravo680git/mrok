@	
s	collection	Operate on collections
s	role	Operate on roles
o	--help|-h	Show help and exit	p
o	--verbose	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	p
o	-v	Verbose mode (-vvv for more, -vvvv to enable connection debugging)	p
o	--version	Shows version number, config file location, module search path, module location, executable…	p
@	collection
s	download	Download collections
s	init	Initialize collections
s	build	Build collections
s	publish	Publish collections
s	list	List collections
s	verify	Verify collections
@	collection download
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--clear-response-cache	Clear the existing server response cache	
o	--no-cache	Do not use the server response cache	
o	--no-deps|-n	Don't download collection(s) listed as dependencies	
o	--download-path|-p	The directory to download the collections to	v
o	--requirements-file|-r	A file containing a list of collections to be downloaded	v
o	--pre	Include pre-release versions	
a	1	1
=	collection download	--download-path
t	folders
=	collection download	--requirements-file
t	filepaths
#	collection download	1
v	amazon.aws	
v	ansible.builtin	
v	ansible.netcommon	
v	ansible.posix	
v	ansible.utils	
v	ansible.windows	
v	arista.eos	
v	awx.awx	
v	azure.azcollection	
v	check_point.mgmt	
v	chocolatey.chocolatey	
v	cisco.aci	
v	cisco.asa	
v	cisco.intersight	
v	cisco.ios	
v	cisco.iosxr	
v	cisco.ise	
v	cisco.meraki	
v	cisco.mso	
v	cisco.nso	
v	cisco.nxos	
v	cisco.ucs	
v	cloud.common	
v	cloudscale_ch.cloud	
v	community.aws	
v	community.azure	
v	community.ciscosmb	
v	community.crypto	
v	community.digitalocean	
v	community.dns	
v	community.docker	
v	community.fortios	
v	community.general	
v	community.google	
v	community.grafana	
v	community.hashi_vault	
v	community.hrobot	
v	community.kubernetes	
v	community.kubevirt	
v	community.libvirt	
v	community.mongodb	
v	community.mysql	
v	community.network	
v	community.okd	
v	community.postgresql	
v	community.proxysql	
v	community.rabbitmq	
v	community.routeros	
v	community.sap	
v	community.skydive	
v	community.sops	
v	community.vmware	
v	community.windows	
v	community.zabbix	
v	containers.podman	
v	cyberark.conjur	
v	cyberark.pas	
v	dellemc.enterprise_sonic	
v	dellemc.openmanage	
v	dellemc.os10	
v	dellemc.os6	
v	dellemc.os9	
v	f5networks.f5_modules	
v	fortinet.fortimanager	
v	fortinet.fortios	
v	frr.frr	
v	gluster.gluster	
v	google.cloud	
v	hetzner.hcloud	
v	hpe.nimble	
v	ibm.qradar	
v	infinidat.infinibox	
v	infoblox.nios_modules	
v	inspur.sm	
v	junipernetworks.junos	
v	kubernetes.core	
v	mellanox.onyx	
v	netapp.aws	
v	netapp.azure	
v	netapp.cloudmanager	
v	netapp.elementsw	
v	netapp.ontap	
v	netapp.storagegrid	
v	netapp.um_info	
v	netapp_eseries.santricity	
v	netbox.netbox	
v	ngine_io.cloudstack	
v	ngine_io.exoscale	
v	ngine_io.vultr	
v	openstack.cloud	
v	openvswitch.openvswitch	
v	ovirt.ovirt	
v	purestorage.flasharray	
v	purestorage.flashblade	
v	sensu.sensu_go	
v	servicenow.servicenow	
v	splunk.es	
v	t_systems_mms.icinga_director	
v	theforeman.foreman	
v	vmware.vmware_rest	
v	vyos.vyos	
v	wti.remote	
@	collection init
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--force|-f	Force overwriting an existing role or collection	
o	--init-path	The path in which the skeleton collection will be created	v
o	--collection-skeleton	The path to a collection skeleton that the new collection should be based upon	v
a	1	0
=	collection init	--init-path
t	folders
=	collection init	--collection-skeleton
t	folders
@	collection build
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--force|-f	Force overwriting an existing role or collection	
o	--output-path	The path in which the collection is built to	v
a	1	0
=	collection build	--output-path
t	folders
#	collection build	1
t	folders
@	collection publish
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--no-wait	Don't wait for import validation results	
o	--import-timeout	The time to wait for the collection import process to finish	v
a	1	0
=	collection publish	--import-timeout
v	60	
v	300	
v	600	
v	900	
#	collection publish	1
t	folders
@	collection list
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--collections-path|-p	One or more directories to search for collections in addition to the default COLLECTIONS_PATHS…	v
o	--format	Format to display the list of collections in	v
a	1	0
=	collection list	--collections-path
v	~/.ansible/collections:/usr/share/ansible/collections	
t	folders
=	collection list	--format
v	human	
v	yaml	
v	json	
@	collection verify
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--collections-path|-p	One or more directories to search for collections in addition to the default COLLECTIONS_PATHS…	v
o	--ignore-errors|-i	Ignore errors during verification and continue with the next specified collection	
o	--requirements-file|-r	A file containing a list of collections to be downloaded	v
a	1	0
=	collection verify	--collections-path
v	~/.ansible/collections:/usr/share/ansible/collections	
t	folders
=	collection verify	--requirements-file
t	filepaths
@	role
s	init	Initialize roles
s	remove	Remove roles
s	list	List roles
s	search	Search roles
s	import	Import roles
s	setup	Set up roles
s	info	Role information
s	install	Install roles
@	role init
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--force|-f	Force overwriting an existing role or collection	
o	--offline	Don't query the galaxy API when creating roles	
o	--init-path	The path in which the skeleton collection will be created	v
o	--role-skeleton	The path in which the skeleton role will be created	v
o	--type	Initialize using an alternate role type	v
a	1	0
=	role init	--init-path
t	folders
=	role init	--role-skeleton
t	folders
=	role init	--type
v	container	
v	apb	
v	network	
@	role remove
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--roles-path|--role-path	The path to the directory containing your roles	v
a	1	0
=	role remove	--roles-path
v	~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles	
@	role list
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--roles-path|--role-path	The path to the directory containing your roles	v
a	1	0
=	role list	--roles-path
v	~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles	
@	role search
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--platforms	List of OS platforms to filter by	v
o	--galaxy-tags	List of Galaxy tags to filter by	v
o	--author	GitHub username	v
a	1	0
@	role import
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--branch	The name of a branch to import. Defaults to the repository's default branch (usually master)	v
o	--role-name	The name the role should have, if different than the repo name	v
o	--status	Check the status of the most recent import request for given github_user/github_repo	
a	2	0
=	role import	--branch
v	master	
v	main	
v	develop	
@	role setup
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--roles-path|--role-path	The path to the directory containing your roles	v
o	--remove	Remove the integration matching the provided ID value. Use --list to see ID values	v
o	--list	List all of your integrations	
=	role setup	--roles-path
v	~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles	
@	role info
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--roles-path|--role-path	The path to the directory containing your roles	v
o	--offline	Don't query the galaxy API when creating roles	
=	role info	--roles-path
v	~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles	
@	role install
o	--server|-s	The Galaxy API server URL	v
o	--token|--api-key	The Ansible Galaxy API key which can be found at https://galaxy.ansible.com/me/preferences	v
o	--ignore-certs|-c	Ignore SSL certificate validation errors	
o	--roles-path|--role-path	The path to the directory containing your roles	v
o	--no-deps|-n	Don't download roles listed as dependencies	
o	--force-with-deps	Force overwriting an existing role and its dependencies	
o	--requirements-file|-r	A file containing a list of collections to be downloaded	v
o	--keep-scm-meta|-g	Use tar instead of the scm archive option when packaging the role	
=	role install	--roles-path
v	~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles	
=	role install	--requirements-file
t	filepaths
