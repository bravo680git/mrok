@	
s	init	Initial an example StreamFunction
s	build	Build a StreamFunction to WebAssembly
s	run	Run a wasm stream function
o	--help|-h	Show help for yomo	
@	init
o	--rx	Generate Rx code template	
a	1	0
@	build
o	--target	Build to wasm or binary	v
o	-m|--modfile	Custom go.mod filepath	v
a	1	0
=	build	-m
d
#	build	1
d
@	run
o	-z|--zipper	Zipper endpoint this StreamFunction will connect to	
o	-n|--name	Specify the name of this StreamFunction	
a	1	0
#	run	1
d
