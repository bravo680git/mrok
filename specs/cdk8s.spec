@	
s	init	Create a new, empty CDK8S project
s	import	Import a CRD schema to generate generate resources
s	synth	Synthesizes Kubernetes manifests for all charts in your app
o	--version	The current version	
o	--help	Show help	
o	--check-upgrade	Check for cdk8s-cli upgrade	
@	init
a	1	0
#	init	1
v	go-app	
v	java-app	
v	python-app	
v	typescript-app	
@	import
o	--language|-l	Output programming language	v
o	--class-prefix	A prefix to add to all generated class names	
o	--no-class-prefix	Does not add a prefix to generated class names	
o	--exclude	Do not import types that match these regular expressions	v
o	--output|-o	Output directory	v
a	1	0
=	import	--language
v	typescript	
v	python	
v	java	
v	go	
=	import	--output
t	folders
#	import	1
t	filepaths
@	synth
o	--app|-a	Command to use in order to execute cdk8s app	
o	--output|-o	Output directory	v
o	--stdout|-s	Write synthesized manifests to STDOUT instead of the output directory	
o	--plugins-dir	Directory to store cdk8s plugins	
o	--validate	Apply validation plugins on the resulting manifests	
o	--no-validate	Disable validation	
o	--validation-reports-output-file	File to write a JSON representation of the validation reports to	v
=	synth	--output
t	folders
=	synth	--validation-reports-output-file
t	filepaths
