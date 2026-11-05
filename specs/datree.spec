@	
s	completion	Generate completion script for bash,zsh,fish,powershell
s	config	Internal configuration management for datree config file
s	help	Help about any command
s	kustomize	Generate kustomization files from manifests
s	publish	Publish policies configuration for given <fileName>. Input should be the path to the…
s	test	Trigger a policy check, provide a Kubernetes configuration file path or a glob pattern
s	version	Print the version number
o	--help|-h	Show help for datree	
@	completion
@	config
s	get	Get configuration value
s	set	Set configuration value
o	-h|--help	Help for config	
@	config get
o	-h|--help	Get value for specific key from datree config.yaml file. Defaults to $HOME/.datree/config.yaml	
@	config set
o	-h|--help	Apply value for specific key in datree config.yaml file. Defaults to $HOME/.datree/config.yaml	
@	help
a	1	0
#	help	1
t	help
@	kustomize
s	test	Test kustomization files
o	-h|--help	Help for kustomize	
@	kustomize test
o	--help|-h	Help for 'test'	
o	--ignore-missing-schemas	Ignore missing schemas when executing schema validation step	
o	--no-record	Do not send policy checks metadata to the backend	
o	--only-k8s-files	Evaluate only valid yaml files with the properties 'apiVersion' and 'kind'. Ignore everything else	
o	-o|--output	Define output format (simple, yaml, json, xml, JUnit)	v
o	-p|--policy	Policy name to run against	v
o	--policy-config	Path for local policies configuration file	v
o	--schema-location	Override schemas location search path (can be specified multiple times)	v
o	-s|--schema-version	Set kubernetes version to validate against. Defaults to 1.19.0	
o	--verbose	Display 'How to Fix' link	
=	kustomize test	-o
v	simple	Simple output without colors
v	yaml	YAML output
v	json	JSON output
v	xml	XML output
v	junit	JUnit output
=	kustomize test	--policy-config
t	filepaths
@	publish
o	-h|--help	Help for publish	
a	1	0
#	publish	1
t	filepaths
@	test
o	--help|-h	Help for 'test'	
o	--ignore-missing-schemas	Ignore missing schemas when executing schema validation step	
o	--no-record	Do not send policy checks metadata to the backend	
o	--only-k8s-files	Evaluate only valid yaml files with the properties 'apiVersion' and 'kind'. Ignore everything else	
o	-o|--output	Define output format (simple, yaml, json, xml, JUnit)	v
o	-p|--policy	Policy name to run against	v
o	--policy-config	Path for local policies configuration file	v
o	--schema-location	Override schemas location search path (can be specified multiple times)	v
o	-s|--schema-version	Set kubernetes version to validate against. Defaults to 1.19.0	
o	--verbose	Display 'How to Fix' link	
a	1	0
=	test	-o
v	simple	Simple output without colors
v	yaml	YAML output
v	json	JSON output
v	xml	XML output
v	junit	JUnit output
=	test	--policy-config
t	filepaths
#	test	1
t	filepaths
@	version
