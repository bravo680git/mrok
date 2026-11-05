@	
s	check	Validate a composition spec
s	start	Launch the GraphQL Server for the specific configuration
s	init	Bootstrap a new TailCall project
s	gen	Generate GraphQL configurations from various sources
@	check
o	--n-plus-one-queries	Detect N+1 issues	p
o	--schema	Display the schema of the composition spec	p
o	--format	Change the format of the input file	v
a	1	1
=	check	--format
v	gql	
v	graphql	
v	yml	
v	yaml	
v	json	
#	check	1
t	filepaths
@	start
a	1	1
#	start	1
t	filepaths,folders
@	init
a	1	0
#	init	1
t	folders
@	gen
a	1	0
#	gen	1
t	filepaths
