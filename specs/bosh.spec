@	
s	add-blob	Add blob
s	unignore	Unignore an instance
s	update-cloud-config	Update current cloud config
s	update-config	Update config
s	update-cpi-config	Update current CPI config
s	update-resurrection	Enable/disable resurrection
s	update-runtime-config	Update current runtime config
s	upload-blobs	Upload blobs
s	upload-release	Upload release
s	upload-stemcell	Upload stemcell
s	variables	List variables
s	vendor-package	Vendor package
s	vms	List all VMs in all deployments
s	orphan-disk	Orphan disk
s	networks	List networks
s	manifest	Show deployment manifest
s	tasks	List running or recent tasks
s	task	Show task status and start tracking its output
s	take-snapshot	Take snapshot
s	sync-blobs	Sync blobs
s	stop-env	Stop BOSH environment
s	stop	Stop instance(s)
s	stemcells	List stemcells
s	start-env	Start BOSH environment
s	start	Start instance(s)
s	ssh	SSH into instance(s)
s	snapshots	List snapshots
s	sha2ify-release	Convert release tarball to use SHA256
s	sha1ify-release	Convert release tarball to use SHA1
s	runtime-config	Show current runtime config
s	run-errand	Run errand
s	restart	Restart instance(s)
s	reset-release	Reset release
s	repack-stemcell	Repack stemcell
s	remove-blob	Remove blob
s	releases	List releases
s	recreate	Recreate instance(s)
s	orphaned-vms	List all the orphaned VMs in all deployments
s	scp	SCP to/from instance(s)
s	help	Show this help message
s	ignore	Ignore an instance
s	init-release	Initialize release
s	inspect-local-release	Display information from release metadata
s	inspect-local-stemcell	Display information from stemcell metadata
s	inspect-release	List release contents such as jobs
s	instances	List all instances in a deployment
s	interpolate	Interpolates variables into a manifest
s	locks	List current locks
s	log-in	Login
s	log-out	Log out
s	logs	Fetch logs from instance(s)
s	deployment	Show deployment information
s	deployments	List deployments
s	diff-config	Diff two configs by ID or content
s	disks	List disks
s	environment	Show environment
s	environments	List environments
s	errands	List errands
s	event	Show event details
s	events	List events
s	export-release	Export the compiled release to a tarball
s	finalize-release	Create final release from dev release tarball
s	generate-job	Generate job
s	generate-package	Generate package
s	create-release	Create release
s	curl	Make an HTTP request to the Director
s	delete-config	Delete config
s	delete-deployment	Delete deployment
s	delete-disk	Delete disk
s	delete-env	Delete BOSH environment
s	delete-network	Delete network
s	delete-release	Delete release
s	delete-snapshot	Delete snapshot
s	delete-snapshots	Delete all snapshots in a deployment
s	delete-stemcell	Delete stemcell
s	delete-vm	Delete VM
s	deploy	Update deployment
s	alias-env	Alias environment to save URL and CA certificate
s	attach-disk	Attach disk to an instance
s	blobs	List blobs
s	cancel-task	Cancel task at its next checkpoint
s	cancel-tasks	Cancel tasks at their next checkpoints
s	clean-up	Clean up old unused resources except orphaned disks
s	cloud-check	Cloud consistency check and interactive repair
s	cloud-config	Show current cloud config
s	config	Show current config for either ID or both type and name
s	configs	List configs
s	cpi-config	Show current CPI config
s	create-env	Create or update BOSH environment
o	--version	Show CLI version	
o	--config	Config file path (default: ~/.bosh/config)	v
o	-e|--environment	Director environment name or URL	v
o	--ca-cert	Director CA certificate path or value	v
o	--sha2	Use SHA256 checksums	
o	--parallel	The max number of parallel operations (default: 5)	v
o	--client	Override username or UAA client [$BOSH_CLIENT]	v
o	--client-secret	Override password or UAA client secret [$BOSH_CLIENT_SECRET]	v
o	--deployment	Deployment name [$BOSH_DEPLOYMENT]	v
o	--column	Filter to show only given column(s)	v
o	--json	Output as JSON	
o	--tty	Force TTY-like output	
o	--no-color	Toggle colorized output	
o	-n|--non-interactive	Don't ask for user input [$BOSH_NON_INTERACTIVE]	
=		--config
t	filepaths
=		--ca-cert
t	filepaths
=		--parallel
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
v	8	
v	9	
v	10	
v	11	
v	12	
v	13	
v	14	
v	15	
v	16	
v	17	
v	18	
v	19	
v	20	
=		--deployment
d
@	add-blob
a	2	0
#	add-blob	1
t	filepaths
#	add-blob	2
t	filepaths
@	unignore
a	1	0
@	update-cloud-config
a	1	0
#	update-cloud-config	1
t	filepaths
@	update-config
a	1	0
#	update-config	1
t	filepaths
@	update-cpi-config
a	1	0
#	update-cpi-config	1
t	filepaths
@	update-resurrection
a	1	0
#	update-resurrection	1
v	on	
v	off	
@	update-runtime-config
a	1	0
#	update-runtime-config	1
t	filepaths
@	upload-blobs
@	upload-release
a	1	0
@	upload-stemcell
a	1	0
#	upload-stemcell	1
t	filepaths
@	variables
@	vendor-package
a	2	0
#	vendor-package	2
t	folders
@	vms
@	orphan-disk
a	1	0
@	networks
@	manifest
@	tasks
a	1	0
@	task
@	take-snapshot
a	1	0
@	sync-blobs
@	stop-env
@	stop
a	1	0
@	stemcells
@	start-env
@	start
a	1	0
@	ssh
a	1	0
@	snapshots
a	1	0
@	sha2ify-release
@	sha1ify-release
@	runtime-config
@	run-errand
a	1	0
@	restart
a	1	0
@	reset-release
@	repack-stemcell
a	2	0
#	repack-stemcell	1
t	filepaths
#	repack-stemcell	2
t	filepaths
@	remove-blob
@	releases
@	recreate
a	1	0
@	orphaned-vms
@	scp
a	1	1
#	scp	1
t	filepaths
@	help
@	ignore
a	1	0
@	init-release
@	inspect-local-release
a	1	0
#	inspect-local-release	1
t	filepaths
@	inspect-local-stemcell
a	1	0
#	inspect-local-stemcell	1
t	filepaths
@	inspect-release
a	1	0
@	instances
@	interpolate
a	1	0
#	interpolate	1
t	filepaths
@	locks
@	log-in
@	log-out
@	logs
a	1	0
@	deployment
@	deployments
@	diff-config
@	disks
@	environment
@	environments
@	errands
@	event
a	1	0
@	events
@	export-release
a	2	0
@	finalize-release
a	1	0
#	finalize-release	1
t	filepaths
@	generate-job
a	1	0
@	generate-package
a	1	0
@	create-release
a	1	0
#	create-release	1
t	filepaths
@	curl
a	1	0
#	curl	1
t	filepaths
@	delete-config
a	1	0
@	delete-deployment
@	delete-disk
a	1	0
@	delete-env
a	1	0
#	delete-env	1
t	filepaths
@	delete-network
a	1	0
@	delete-release
a	1	0
@	delete-snapshot
a	1	0
@	delete-snapshots
@	delete-stemcell
a	1	0
@	delete-vm
a	1	0
@	deploy
a	1	0
#	deploy	1
t	filepaths
@	alias-env
a	1	0
@	attach-disk
a	2	0
@	blobs
@	cancel-task
a	1	0
@	cancel-tasks
@	clean-up
@	cloud-check
@	cloud-config
@	config
a	1	0
@	configs
@	cpi-config
@	create-env
a	1	0
#	create-env	1
t	filepaths
