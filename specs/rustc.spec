@	
o	-h|--help	Prints out help info	
o	--cfg	Configures compilation settings	v
o	-L	Adds a directory to the library search path	V
o	--l	Links the generated crate to a native library	V
o	--crate-type	Specify types of crates for the compiler to emit	v
o	--crate-name	Specify the name of the crate being built	v
o	--edition	Specify the edition to use	v
o	--emit	Specify the types of output files to generate	v
o	--print	Prints compiler info	v
o	-g	Synonym for -C debuginfo=2	
o	-O	Synonym for -C opt-level=2	
o	-o	Specify the filename to write output	v
o	--out-dir	Specify directory to write output	v
o	--explain	Provides a detailed explanation of an error message	v
o	--test	Builds a test harness	
o	--target	Selects a target triple to build	v
o	-W|--warn	Sets lint warnings	v
o	-A|--allow	Set lint allowed	v
o	-D|--deny	Set lint denied	v
o	-F|--forbid	Set lint forbid	v
o	--cap-lints	Set the most restrictive lint level	v
o	-C|--codegen	Set a codegen option	v
o	-Z	Set unstable options	v
o	-V|--version	Prints version	
o	-v|--verbose	Use verbose output	
o	--extern	Specify where an external library is located	v
o	--sysroot	Overrides the system root	v
o	--error-format	Controls how errors are produced	v
o	--color	Configures coloring of output	v
a	1	0
=		-L
v	dependency	Only search for transitive dependencies in this directory
v	crate	Only search for this crate's direct dependencies in this directory
v	native	Only search for native libraries in this directory
v	framework	Only search for macOS frameworks in this directory
v	all	Search for all library kinds in this directory
=		--l
v	dylib	A native dynamic library
v	static	A native static library
v	framework	A macOS framework
=		--crate-type
v	bin	A runnable executable program
v	lib	Generates a library kind preferred by the compiler
v	rlib	A Rust static library
v	dylib	A native dynamic library
v	cdylib	A native static library
v	staticlib	A macOS framework
v	proc-macro	Generates a format suitable for a procedural macro library that may be loaded by the compiler
=		--edition
v	2015	
v	2018	
v	2021	
=		--emit
v	asm	Generates a file with the crate's assembly code
v	llvm-bc	Generates a binary file containing the LLVM bitcode
v	llvm-ir	Generates a file containing LLVM IR
v	obj	Generates a native object file
v	metadata	Generates a file containing metadata about the crate
v	link	Generates the crates specified by --crate-type
v	dep-info	Generates a file with Makefile syntax that indicates all the source files that were loaded to…
v	mir	Generates a file containing rustc's mid-level intermediate representation
=		--print
v	crate-name	The name of the crate
v	file-names	The names of the files created by the link emit kind
v	sysroot	Path to the sysroot
v	target-libdir	Path to the target libdir
v	cfg	List of cfg values
v	target-list	List of known targets. The target may be selected with the --target flag
v	target-cpus	List of available CPU values for the current target
v	target-features	List of available target features for the current target
v	relocation-models	List of relocation models. Relocation models may be selected with the -C relocation-model=val flag
v	code-models	List of code models
v	tls-models	List of Thread Local Storage models supported
v	target-spec-json	
v	native-static-libs	This may be used when creating a staticlib crate type
=		--extern
t	folders
=		--error-format
v	human	
v	json	
v	short	
=		--color
v	auto	
v	always	
v	never	
#		1
t	filepaths
