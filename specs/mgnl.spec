@	
s	add-availability	This command makes a component available to a page
s	create-app	This command creates a content type and an app
s	create-block	This command creates a block
s	create-component	This command creates a new component template
s	create-content-type	This command creates a content type
s	create-light-module	This command creates a new light module in the form of a set of empty light module folders
s	create-page	This command creates a new page template
s	create-virtual-uri	The command creates a virtual URI mapping configuration file (a YAML definition file) in the light…
s	customize-local-config	Run this command to create a local configuration
s	install	Downloads and installs one or more light modules from npm to the light module directory
s	jumpstart	This command downloads, unpacks and pre-configures a Magnolia Tomcat server together with a…
s	tab-completion	Run the command to install or uninstall autocompletion for Magnolia CLI commands
s	search	Searches for Magnolia-related packages available from npm
s	start	This command starts up Magnolia and displays the main log file
o	--help|-h	Show help for mgnl	p
@	add-availability
o	-p|--path	The path to the light module that contains the page template	v
o	-g	Add this parameter to autogenerate the component instead of providing plain availability	
a	2	0
=	add-availability	-p
t	folders
@	create-app
o	-p|--path	The path to the light module where you want to create the app	v
o	-P|--prototype	The name of the prototype variant to create the app	v
a	1	0
=	create-app	-p
t	folders
@	create-block
o	-p|--path	The path to the light module to add the new block to	v
o	-P|--prototype	The name of the prototype variant to create the block	v
a	1	0
=	create-block	-p
t	folders
@	create-component
o	-p|--path	The path to the light module you want to add the component template to	v
o	-a|--available	The page you want to make the component available to	v
o	-g|--autogenerate	Add this parameter to autogenerate the component instead of providing plain availability	v
o	-P|--prototype	The name of the prototype variant to create the component	v
a	1	0
=	create-component	-p
t	folders
@	create-content-type
o	-a	Creates also a new app that references the content type. With the -a option, the command is…	
o	-p|--path	The path to the light module where you want to create the content type	v
o	-P|--prototype	The name of the prototype variant to create the content type	v
a	1	0
=	create-content-type	-p
t	folders
@	create-light-module
o	-p|--path	The path of the parent directory for the new light module	v
o	-P|--prototype	The name of the prototype variant to create the light module	v
a	1	0
=	create-light-module	-p
t	folders
@	create-page
o	-p|--path	The path to the light module to add the new template to	v
o	-P|--prototype	The name of the prototype variant to create the page	v
a	1	0
=	create-page	-p
t	folders
@	create-virtual-uri
o	-p|--path	The path to the light module	v
o	-f|--formUri	The pattern to be matched in the requested URI. Enclose the <uri> value in quotes	v
o	-t|--toUri	A concrete URI that the request is mapped to. Enclose the <prefix:uri> value in quotes	v
o	-P|--prototype	The name of the prototype variant to create the mapping	v
a	1	0
=	create-virtual-uri	-p
t	folders
@	customize-local-config
o	-p|--path	The path into which the mgnl-cli-prototypes folder and mgnl-cli.json file are installed	v
=	customize-local-config	-p
t	folders
@	install
o	-p|--path	The path to the light-modules folder	v
a	1	1
=	install	-p
t	folders
#	install	1
d
@	jumpstart
o	-p|--path	The path to the light modules root folder which is observed for changes	v
o	-m|--magnolia-version	Use to choose a specific version of the Magnolia webapp. If not provided, the latest stable…	v
o	-i|--install-sample-module	If provided, a sample light module under the light modules root folder with the given name is…	v
o	-s|--snapshot	Downloads the latest snapshot development version of the specified webapp	
o	-w|--webapp	Use to directly specify which Magnolia webapp you want to install	v
=	jumpstart	-p
t	folders
=	jumpstart	-w
v	magnolia-empty-webapp	
v	magnolia-community-webapp	
v	magnolia-community-demo-webapp	
v	magnolia-dx-core-webapp	
v	magnolia-dx-core-demo-webapp	
@	tab-completion
a	1	0
#	tab-completion	1
v	install	
v	uninstall	
@	search
a	1	0
#	search	1
d
@	start
o	-p|--path	The path to the apache-tomcat folder	v
o	-d	Does NOT ignore the open files limit check. The files limit check is ignored by default	
=	start	-p
t	folders
