@	
s	init	Initialize a new project using Spring Initializr
s	encodepassword	Encode a password for use with Spring Security
s	shell	Start a nested shell
s	help	Show help for other commands
o	--help	Show help for spring	
o	--version	Get spring CLI version	
o	--debug	Print additional status information for the command you are running	p
@	init
o	-a|---artifact-id	Project coordinates	v
o	-b|--boot-version	Spring Boot version	v
o	--build	Build system to use	v
o	-d|--dependencies	Comma-separated list of dependency identifiers to include in the generated project	v
o	--description	Project description	v
o	-f|--force	Force overwrite of existing files	
o	--format	Format of the generated content	v
o	-g|--group-id	Project coordinates	v
o	-j|--java-version	Language level	v
o	--list	List the capabilities of the service	
o	-n|--name	Project name	v
o	-p|--packaging	Project packaging	v
o	--package-name	Package name	v
o	-t|--type	Project type	v
o	--target	URL of the service to use	v
o	-v|--version	Project version	v
o	-x|--extract	Extract the project archive. Inferred if a location is specified without an extension	
=	init	-b
d
=	init	--build
v	maven	
v	gradle	
=	init	-d
d
=	init	--format
v	build	
v	project	
=	init	-j
d
=	init	-p
v	jar	
v	war	
=	init	-t
v	gradle-build	Generate a Gradle build file
v	gradle-project	Generate a Gradle based project archive using the Groovy DSL
v	gradle-project-kotlin	Generate a Gradle based project archive using the Kotlin DSL
v	maven-build	Generate a Maven pom.xml
v	maven-project	Generate a Maven based project archive
@	encodepassword
o	-a|--algorithm	The algorithm to use	v
a	1	0
=	encodepassword	-a
v	default	
v	bcrypt	
v	pbkdf2	
@	shell
@	help
a	1	0
#	help	1
t	help
