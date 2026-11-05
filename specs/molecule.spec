@	
s	check	Use the provisioner to perform a Dry-Run (destroy, dependency, create, prepare, converge)
s	cleanup	Use the provisioner to cleanup any changes made to external systems during the stages of testing
s	converge	Use the provisioner to configure instances (dependency, create, prepare converge)
s	create	Use the provisioner to start the instances
s	dependency	Manage the role's dependencies
s	destroy	Use the provisioner to destroy the instances
s	drivers	List drivers
s	idempotence	Use the provisioner to configure the instances and parse the output to determine idempotence
s	init	Initialize a new role or scenario
s	lint	Lint the role (dependency, lint)
s	list	List status of instances
s	login	Log in to one instance
s	matrix	List matrix of steps used to test instances
s	prepare	Use the provisioner to prepare the instances into a particular starting state
s	reset	Reset molecule temporary folders
s	side-effect	Use the provisioner to perform side-effects to the instances
s	syntax	Use the provisioner to syntax check the role
s	test	Test (dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence…
o	--help	Show help	p
o	--version	Show molecule version	
@	check
o	--scenario-name|-s	Name of the scenario to target. (default)	v
o	--parallel	Enable parallel mode	
o	--no-parallel	Disable parallel mode	
@	cleanup
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	converge
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	create
o	--scenario-name|-s	Name of the scenario to target. (default)	v
o	--driver-name|-d	Name of driver to use. (delegated)	v
=	create	--driver-name
v	delegated	
v	docker	
v	podman	
v	vagrant	
v	azure	
v	hetzner	
@	dependency
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	destroy
o	--scenario-name|-s	Name of the scenario to target. (default)	v
o	--driver-name|-d	Name of driver to use. (delegated)	v
o	--all	Destroy all scenarios. Default is False	
o	--no-all	Do not destroy all scenarios	
o	--parallel	Enable parallel mode	
o	--no-parallel	Disable parallel mode	
=	destroy	--driver-name
v	delegated	
v	docker	
v	podman	
v	vagrant	
v	azure	
v	hetzner	
@	drivers
o	--format|-f	Change output format. (simple)	v
=	drivers	--format
v	simple	
v	plain	
@	idempotence
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	init
s	role	Initialize a new role for use with Molecule, namespace is required outside collections, like…
s	scenario	Initialize a new scenario for use with Molecule
@	init role
o	--dependency-name	Name of dependency to initialize. (galaxy)	v
o	--driver-name|-d	Name of driver to use. (delegated)	v
o	--lint-name	Name of lint to initialize. (yamllint)	v
o	--provisioner-name	Name of provisioner to initialize. (ansible)	v
o	--verifier-name	Name of verifier to initialize. (ansible)	v
a	1	0
=	init role	--dependency-name
v	galaxy	
=	init role	--driver-name
v	delegated	
v	docker	
v	podman	
v	vagrant	
v	azure	
v	hetzner	
=	init role	--lint-name
v	yamllint	
=	init role	--provisioner-name
v	ansible	
=	init role	--verifier-name
v	ansible	
v	testinfra	
@	init scenario
o	--dependency-name	Name of dependency to initialize. (galaxy)	v
o	--driver-name|-d	Name of driver to use. (delegated)	v
o	--lint-name	Name of lint to initialize. (yamllint)	v
o	--provisioner-name	Name of provisioner to initialize. (ansible)	v
o	--role-name|-r	Name of the role to create	v
o	--verifier-name	Name of verifier to initialize. (ansible)	v
a	1	0
=	init scenario	--dependency-name
v	galaxy	
=	init scenario	--driver-name
v	delegated	
v	docker	
v	podman	
v	vagrant	
v	azure	
v	hetzner	
=	init scenario	--lint-name
v	yamllint	
=	init scenario	--provisioner-name
v	ansible	
=	init scenario	--verifier-name
v	ansible	
v	testinfra	
@	lint
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	list
o	--scenario-name|-s	Name of the scenario to target. (default)	v
o	--format|-f	Change output format. (simple)	v
=	list	--format
v	simple	
v	plain	
v	yaml	
@	login
o	--host|-h	Host to access	v
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	matrix
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	prepare
o	--scenario-name|-s	Name of the scenario to target. (default)	v
o	--driver-name|-d	Name of driver to use. (delegated)	v
o	--force	Enable force mode. Default is disabled	
o	--no-force	Disable force mode	
=	prepare	--driver-name
v	delegated	
v	docker	
v	podman	
v	vagrant	
v	azure	
v	hetzner	
@	reset
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	side-effect
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	syntax
o	--scenario-name|-s	Name of the scenario to target. (default)	v
@	test
o	--scenario-name|-s	Name of the scenario to target. (default)	v
o	--driver-name|-d	Name of driver to use. (delegated)	v
o	--all	Test all scenarios. Default is False	
o	--no-all	Do not test all scenarios	
o	--destroy	The destroy strategy used at the conclusion of a Molecule run (always)	v
o	--parallel	Enable parallel mode	
o	--no-parallel	Disable parallel mode	
=	test	--driver-name
v	delegated	
v	docker	
v	podman	
v	vagrant	
v	azure	
v	hetzner	
=	test	--destroy
v	always	
v	never	
