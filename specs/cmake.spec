@	
s	--build	Project binary directory to be built and must be first. This is required unless a preset is…
s	--install	Project binary directory to install. This is required and must be first
s	--open	Open the generated project in the associated application. This is only supported by some generators
s	-P	Process the given cmake file as a script written in the CMake language. No configure or generate…
s	-E	CMake provides builtin command-line tools through the signature
o	-S	Path to root directory of the CMake project to build	v
o	--help		
o	-B	Path to directory which CMake will use as the root of build directory. If the directory doesn't…	v
o	-C	Pre-load a script to populate the cache	v
o	-D	Create or update a CMake CACHE entry	v
o	-U	Remove matching entries from CMake CACHE	v
o	-G	Specify a build system generator	v
o	-T	Toolset specification for the generator, if supported	v
o	-A	Specify platform name if supported by generator	v
o	toolchain	Specify the cross compiling toolchain file, equivalent to setting CMAKE_TOOLCHAIN_FILE variable	v
o	--install-prefix	Specify the installation directory, used by the CMAKE_INSTALL_PREFIX variable. Must be an absolute…	v
o	-Wno-dev	Suppress developer warnings	
o	-Wdev	Enable developer warnings	
o	-Werror	Enable the type of warnings	v=
o	-Wno-error	Disable the type of warnings	v=
o	-Wdeprecated	Enable deprecated functionality warnings	
o	-Wno-deprecated	Suppress deprecated functionality warnings	
o	-L	List non-advanced cached-variables	
o	-N	View mode only	
o	--graphviz	Generate graphviz of dependencies	V
o	--system-information	Dump information about this system	V
o	--log-level	Set log-level	v
o	--log-context	Enable the message() command outputting context attached to each message	
o	--debug-trycompile	Do not delete the try_compile() build tree	
o	--debug-output	Put cmake in a debug mode	
o	--debug-find	Put cmake find commands in a debug mode	
o	--trace	Put cmake in trace mode	
o	--trace-expand	Put cmake in trace mode with variables expanded	
o	--trace-format	Put cmake in trace mode and sets the trace output format	v
o	--trace-source	Put cmake in trace mode, but output only lines of a specified file	v
o	--trace-redirect	Put cmake in trace mode and redirect trace output to a file instead of stderr	v
o	--warn-uninitialized	Warn about uninitialized values	
o	--warn-unused-vars	Does nothing. In CMake versions 3.2 and below this enabled warnings about unused variables. In…	
o	--no-warn-unused-cli	Don't warn about command line options. Don't find variables that are declared on the command line…	
o	--check-system-vars	Find problems with variable usage in system files	
o	--preset	Reads a preset from <path-to-source>/CMakePresets.json and <path-to-source>/CMakeUserPresets.json…	v
o	--list-presets	Lists the available presets	V
a	1	0
=		-S
t	folders
=		-B
t	folders
=		-C
t	filepaths
=		toolchain
t	filepaths
=		--install-prefix
t	folders
=		-Werror
v	dev	Make developer warnings errors
v	deprecated	Make deprecated macro and function warnings errors
=		-Wno-error
v	dev	Make developer warnings not errors
v	deprecated	Make deprecated macro and function warnings not errors
=		--graphviz
t	filepaths
=		--system-information
t	filepaths
=		--log-level
v	ERROR	
v	WARNING	
v	NOTICE	
v	STATUS	
v	VERBOSE	
v	DEBUG	
v	TRACE	
=		--trace-format
v	human	
v	json-v1	
=		--trace-source
t	filepaths
=		--trace-redirect
t	filepaths
=		--list-presets
v	configure	
v	build	
v	test	
v	all	
#		1
t	folders
@	--build
o	--preset	Use a build preset to specify build options	v
o	--list-presets	Lists the available presets. If no option is specified only configure presets will be listed. The…	
o	--parallel|-j	The maximum number of concurrent processes to use when building. If <jobs> is omitted the native…	V
o	--target|-t	Build <tgt> instead of the default target. Multiple targets may be given, separated by spaces	v
o	--config	For multi-configuration tools, choose configuration <cfg>	v
o	--clean-first	Build target clean first, then build	
o	--use-stderr	Ignored. Behavior is default in CMake >= 3.0	
o	--verbose|-v	Enable verbose output - if supported - including the build commands to be executed	
o	--	Pass remaining options to the native tool	
a	1	0
#	--build	1
t	folders
@	--install
o	--config	For multi-configuration generators	v
o	--component	Component-based install. Only install component specified	v
o	--default-directory-permissions	Default directory install permissions	v
o	--prefix	Override the installation prefix	v
o	--strip	Strip before installing	
o	--verbose|-v	Enable verbose output	
a	1	0
#	--install	1
t	folders
@	--open
a	1	0
#	--open	1
t	folders
@	-P
a	1	0
#	-P	1
t	filepaths
@	-E
s	capabilities	Report cmake capabilities in JSON format. The output is a JSON object with the following keys
s	cat	Concatenate files and print on the standard output
s	chdir	Change the current working directory and run a command
s	compare_files	Check if file1 is the same as file2. If fails are the same, then returns 0, if not returns 1. In…
s	copy	Copy files to <destination> (either file or directory). If multiple files are specified, the…
s	copy_directory	Copy content of <dir>... directories to <destination> directory. If <destination> directory does…
s	copy_if_different	Copy files to <destination> (either file or directory) if they have changed. If multiple files are…
s	create_symlink	Create a symbolic link <new> naming <old>
s	create_hardlink	Create a hard link <new> naming <old>
s	echo	Displays arguments as text
s	echo_append	Displays arguments as text but no new line
s	env	Run command in a modified environment
s	environment	Display the current environment variables
s	false	Do nothing, with an exit code of 1
s	make_directory	Create <dir> directories. If necessary, create parent directories too. If a directory already…
s	md5sum	Create MD5 checksum of files in md5sum compatible format
s	sha1sum	Create SHA1 checksum of files in sha1sum compatible format
s	sha224sum	Create SHA224 checksum of files in sha224sum compatible format
s	sha226sum	Create SHA226 checksum of files in sha226sum compatible format
s	sha384sum	Create SHA384 checksum of files in sha384sum compatible format
s	sha512sum	Create SHA512 checksum of files in sha512sum compatible format
s	remove	Remove the file(s). The planned behavior was that if any of the listed files already do not exist…
s	remove_directory	Remove <dir> directories and their contents. If a directory does not exist it will be silently…
s	rm	Remove the files <file> or directories dir
s	server	Launch cmake-server(7) mode
s	sleep	Sleep for given number of seconds
s	tar	Create or extract a tar or zip archive
s	time	Run command and display elapsed time
s	touch	Creates <file> if file do not exist. If <file> exists, it is changing <file> access and…
s	touch_nocreate	Touch a file if it exists but do not create it. If a file does not exist it will be silently ignored
s	true	Do nothing, with an exit code of 0
@	-E capabilities
@	-E cat
a	1	1
#	-E cat	1
t	filepaths
@	-E chdir
a	2	0
#	-E chdir	1
t	folders
@	-E compare_files
o	--ignore-eol	Implies line-wise comparison and ignores LF/CRLF differences	
a	2	0
#	-E compare_files	1
t	filepaths
#	-E compare_files	2
t	filepaths
@	-E copy
a	2	0
#	-E copy	1
t	filepaths
#	-E copy	2
t	folders
@	-E copy_directory
a	2	0
#	-E copy_directory	1
t	folders
#	-E copy_directory	2
t	folders
@	-E copy_if_different
a	2	0
#	-E copy_if_different	1
t	filepaths
#	-E copy_if_different	2
t	folders
@	-E create_symlink
a	2	0
@	-E create_hardlink
a	2	0
@	-E echo
a	1	0
@	-E echo_append
a	1	0
@	-E env
o	--unset		v
a	2	0
@	-E environment
@	-E false
@	-E make_directory
a	1	1
#	-E make_directory	1
t	folders
@	-E md5sum
a	1	1
#	-E md5sum	1
t	filepaths
@	-E sha1sum
a	1	1
#	-E sha1sum	1
t	filepaths
@	-E sha224sum
a	1	1
#	-E sha224sum	1
t	filepaths
@	-E sha226sum
a	1	1
#	-E sha226sum	1
t	filepaths
@	-E sha384sum
a	1	1
#	-E sha384sum	1
t	filepaths
@	-E sha512sum
a	1	1
#	-E sha512sum	1
t	filepaths
@	-E remove
o	-f	The -f option changes the behavior to return a zero exit code (i.e. success) in such situations…	
a	1	1
#	-E remove	1
t	filepaths
@	-E remove_directory
a	1	1
#	-E remove_directory	1
t	folders
@	-E rm
o	-r|-R	Use -r or -R to remove directories and their contents recursively. If any of the listed…	
o	-f	The -f option changes the behavior to return a zero exit code (i.e. success) in such situations…	
a	2	1
#	-E rm	1
t	filepaths
#	-E rm	2
t	folders
@	-E server
@	-E sleep
a	1	1
@	-E tar
o	c	Create a new archive containing the specified files. If used, the pathname argument is mandatory	
o	x	Extract to disk from the archive. The <pathname>... argument could be used to extract only…	
o	t	List archive contents. The <pathname>... argument could be used to list only selected files or…	
o	v	Produce verbose output	
o	z	Compress the resulting archive with gzip	
o	j	Compress the resulting archive with bzip2	
o	J	Compress the resulting archive with XZ	
o	--zstd	Compress the resulting archive with Zstandard	
o	--files-from	Read file names from the given file, one per line. Blank lines are ignored. Lines may not start in…	v
o	--format	Specify the format of the archive to be created	v
o	--mtime	Specify modification time recorded in tarball entries	v
o	--	Stop interpreting options and treat all remaining arguments as file names, even if they start with -	
a	1	0
=	-E tar	--files-from
t	filepaths
=	-E tar	--format
v	7zip	
v	gnutar	
v	pax	
v	paxr	
v	zip	
@	-E time
a	1	0
@	-E touch
a	1	1
#	-E touch	1
t	filepaths
@	-E touch_nocreate
a	1	1
#	-E touch_nocreate	1
t	filepaths
@	-E true
