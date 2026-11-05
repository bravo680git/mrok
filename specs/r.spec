@	
s	RHOME	Print path to R home directory and exit
s	CMD	Invoke an R tool
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--encoding	Specify encoding to be used for stdin	v=
o	--save	Save workspace at the end of the session	
o	--no-save	Do not save workspace at the end of the session	
o	--no-environ	Do not read the site and user environment files	
o	--no-site-file	Do not read the site-wide Rprofile	
o	--no-init-file	Do not read the user R profile	
o	--restore	Do restore previously saved objects at startup	
o	--no-restore-data	Do not restore previously saved objects	
o	--no-restore-history	Do not restore the R history file	
o	--no-restore	Do not restore anything	
o	--vanilla	Combine --no-save, --no-restore, --no-site-file, --no-init-file and --no-environ	
o	--no-readline	Do not use readline for command-line editing	
o	--max-ppsize	Set max size of protect stack	v=
o	--min-nsize	Set min number of fixed size obj's ('cons cells')	v=
o	--min-vsize	Set vector heap minimum (in bytes or '4M' = 4 MegaB)	v=
o	--quiet|--silent|-q	Do not print startup message	
o	--no-echo|-s	Make R run as quietly as possible	
o	--interactive	Force an interactive session	
o	--verbose	Print more information about progress	
o	--debugger|-d	Run R through a debugger	v=
o	--debugger-args	Pass arguments to the debugger	v=
o	--gui|-g	Type of GUI to use	v=
o	--arch	Specify a sub-architecture	v=
o	--args	Skip the rest of the command line	
o	--file|-f	Take input from a file	v=
o	-e	Execute and R expression and exit	v=
=		--encoding
v	UTF-8	
=		--gui
v	X11	
v	Tk	
=		--file
d
@	RHOME
@	CMD
s	BATCH	Batch Execution of R
s	COMPILE	Compile files for use with R (not available on Windows)
s	SHLIB	Compile the given source files and then link all specified object files
s	INSTALL	Utility for installing add-on packages
s	REMOVE	Remove add-on packages
s	build	Build R packages from package sources
s	check	Check R packages from package sources
s	LINK	Perform the specified linkcmd
s	rprof	Post-process profiling information from `Rprof()`
s	Rdconv	Convert R documentation to other formats
s	Rd2pdf	Generate PDF output from R documentation files
s	Rd2txt	Convert R documentation to text
s	Stangle	A front-end for Stangle and other vignette engines
s	Sweave	A front-end for Sweave and other vignette engines
s	Rdiff	Diff R output files, discarding the R startup message
s	config	Get the value of a basic R configure variable
s	javareconf	Detect current Java setup and update the corresponding configuration in R
s	rtags	Tag C, R, and Rd files under a directory
@	CMD BATCH
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--no-timing	Do not report the timings	
o	--	End processing of options	
a	2	0
#	CMD BATCH	1
d
@	CMD COMPILE
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
a	1	1
#	CMD COMPILE	1
d
@	CMD SHLIB
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--clean|-c	Remove files created during compilation	
o	--preclean	Remove files created during a previous run	
o	--output|-o	Name for the built library	v=
o	--dry-run|-n	Dry run; shows commands that would be used	
o	--use-LTO	Use Link-Time Optimization	
o	--no-use-LTO	Do not use Link-Time Optimization	
o	--debug|-d	Build a debug DLL (Windows only)	
a	1	1
#	CMD SHLIB	1
d
@	CMD INSTALL
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--clean|-c	Remove files created during compilation	
o	--preclean	Remove files created during a previous run	
o	--debug|-d	Turn on debugging messages	
o	--library|-l	Install packages to library tree LIB	v=
o	--no-configure	Do not use the package's configure script	
o	--no-docs	Do not install HTML, LaTeX or examples help	
o	--html	Build HTML help	
o	--no-html	Do not build HTML help	
o	--latex	Install LaTeX help	
o	--example	Install R code for help examples	
o	--fake	Do minimal install for testing purposes	
o	--no-lock	Install on top of any existing installation without using a lock directory	
o	--lock	Use a per-library lock directory (default)	
o	--pkglock	Use a per-package lock directory (default for a single package)	
o	--build	Build binaries of the installed package(s)	
o	--install-tests	Install package-specific tests (if any)	
o	--no-R	Suppress installation of the package R code	
o	--no-libs	Suppress installation of the package libs	
o	--no-data	Suppress installation of the package data	
o	--no-help	Suppress installation of the package help	
o	--no-demo	Suppress installation of the package demo	
o	--no-exec	Suppress installation of the 'exec' directory	
o	--no-inst	Suppress installation of the 'inst' directory	
o	--no-multiarch	Build only the main architecture	
o	--libs-only	Only install the libs directory	
o	--data-compress	Compression to be used for lazy-loading of data	v=
o	--resave-data	Re-save data files as compactly as possible	
o	--compact-docs	Re-compress PDF files under inst/doc	
o	--with-keep.source	'keep.source' for R code	
o	--without-keep.source	Do not use 'keep.source' for R code	
o	--with-keep.parse.data	Use 'keep.parse.data' for R code	
o	--without-keep.parse.data	Do not 'keep.parse.data' for R code	
o	--byte-compile	Byte-compile R code	
o	--no-byte-compile	Do not byte-compile R code	
o	--staged-install	Install to a temporary directory and then move to the target directory (default)	
o	--no-staged-install	Install directly to the target directory	
o	--no-test-load	Skip test of loading installed package	
o	--no-clean-on-error	Do not remove installed package on error	
o	--merge-multiarch	Multi-arch by merging (from a single tarball only)	
o	--use-vanilla	Do not read any Renviron or Rprofile files	
o	--use-LTO	Use Link-Time Optimization	
o	--no-use-LTO	Do not use Link-Time Optimization	
o	--configure-args	Set arguments for the configure scripts	v=
o	--configure-vars	Set variables for the configure scripts	v=
o	--strip	Strip shared object(s) (Unix only)	
o	--strip-lib	Strip static/dynamic libraries under 'lib/' (Unix only)	
o	--dsym	Generate dSYM directory (macOS only)	
o	--built-timestamp	Set timestamp for 'Built' entry in DESCRIPTION (Unix only)	v=
o	--force-biarch	Attempt to build both architectures (Windows only)	
o	--compile-both	Compile both architectures on 32-bit Windows (Windows only)	
a	1	0
=	CMD INSTALL	--library
d
=	CMD INSTALL	--data-compress
v	gzip	
v	none	
v	bzip2	
v	xz	
#	CMD INSTALL	1
t	folders
@	CMD REMOVE
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--library|-l	The library tree to remove from	v=
a	1	1
=	CMD REMOVE	--library
d
@	CMD build
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--force	Force removal of INDEX file	
o	--keep-empty-dirs	Do not remove empty dirs	
o	--no-build-vignettes	Do not (re)build package vignettes	
o	--no-manual	Do not build the PDF manual	
o	--resave-data	Re-save data files as compactly as possible	V=
o	--no-resave-data	Do not save data	
o	--compact-vignettes	Try to compact PDF files under 'inst/doc'	V=
o	--compression	Type of compression to be used on tarball	V=
o	--md5	Add MD5 sums	
o	--log	Log to file 'pkg-00build.log' when processing the pkgdir with basename 'pkg'	
a	1	1
=	CMD build	--resave-data
v	best	
v	gzip	
v	no	
=	CMD build	--compact-vignettes
v	no	
v	qpdf	
v	gs	
v	gs+qpdf	
v	both	
=	CMD build	--compression
v	gzip	
v	none	
v	bzip2	
v	xz	
#	CMD build	1
t	folders
@	CMD check
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--library|-lib	Library used for test installation of packages	v
o	--output|-o	Directory for output	v=
o	--no-clean	Do not clean 'outdir' before using it	
o	--no-codoc	Do not check for code/documentation mismatches	
o	--no-examples	Do not run the examples in the Rd files	
o	--no-install	Skip installation and associated tests	
o	--no-tests	Do not run code in 'tests' subdirectory	
o	--no-manual	Do not produce the PDF manual	
o	--no-vignettes	Do not run R code in vignettes nor build outputs	
o	--no-build-vignettes	Do not build vignette outputs	
o	--ignore-vignettes	Skip all tests on vignettes	
o	--run-dontrun	Do run `dontrun{}` sections in the Rd files	
o	--run-donttest	Do run `donttest{}` sections in the Rd files	
o	--use-gct	Use `gctorture(TRUE)` when running examples, tests	
o	--use-valgrind	Use `valgrind` when running examples, tests, vignettes	
o	--timings	Record timings for examples	
o	--install-args	Command-line args to be passed to INSTALL	v=
o	--test-dir	Look in this subdirectory for test scripts	v=
o	--no-stop-on-test-error	Do not stop running tests after first error	
o	--check-subdirs	Run checks on the package subdirectories	v=
o	--as-cran	Select customizations similar to those used by CRAN	
o	--extra-arch	Do only runtime tests needed for an additional sub-architecture	
o	--multiarch	Do runtime tests on all installed sub-archs	
o	--no-multiarch	Do runtime tests only on the main sub-architecture	
o	--force-multiarch	Run tests on all sub-archs even for packages with no compiled code	
a	1	1
=	CMD check	--library
t	folders
=	CMD check	--output
t	folders
=	CMD check	--test-dir
t	folders
=	CMD check	--check-subdirs
v	default	
v	yes	
v	no	
#	CMD check	1
d
@	CMD LINK
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
a	1	0
@	CMD rprof
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--lines	Print line information	
o	--total	Print only by total	
o	--self	Print only by self	
o	--linesonly	Print only by line	
o	--min%total	Minimum % to print for 'by total'	v=
o	--min%self	Minimum % to print for 'by self'	v=
a	1	0
=	CMD rprof	--min%total
v	1	
v	10	
v	50	
=	CMD rprof	--min%self
v	1	
v	10	
v	50	
#	CMD rprof	1
t	filepaths
@	CMD Rdconv
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--type|-t	Output format type	v=
o	--encoding	Encoding of the output	v=
o	--package	Package name	v=
o	--output|-o	The output file	v=
o	--os|--OS	Set name of OS ('unix' or 'windows')	v=
o	--RdMacros	Packages from which to get Rd macros	v=
a	1	0
=	CMD Rdconv	--type
v	txt	
v	html	
v	latex	
v	example	
=	CMD Rdconv	--output
v	""	
v	-	
=	CMD Rdconv	--os
v	unix	
v	windows	
#	CMD Rdconv	1
d
@	CMD Rd2pdf
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--batch	No interaction between files	
o	--no-clean	Do not remove created temporary files	
o	--no-preview	Do not preview generated PDF file	
o	--encoding	Set the default input encoding	v=
o	--outputEncoding	Set the default output encoding	v=
o	--os|--OS	Set name of OS ('unix' or 'windows')	v=
o	--output|-o	Write output to a file	v=
o	--force	Overwrite output file if it exists	
o	--title	Set the title of the document	v=
o	--no-index	Do not index output	
o	--no-description	Do not typeset the description of a package	
o	--internals	Typeset 'internal' documentation (usually skipped)	
o	--build_dir	Set the working directory	v=
o	--RdMacros	Packages from which to get Rd macros	v=
a	1	0
=	CMD Rd2pdf	--os
v	unix	
v	windows	
=	CMD Rd2pdf	--build_dir
t	folders
#	CMD Rd2pdf	1
t	folders
@	CMD Rd2txt
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--type|-t	Output format type	v=
o	--encoding	Encoding of the output	v=
o	--package	Package name	v=
o	--output|-o	The output file	v=
o	--os|--OS	Set name of OS ('unix' or 'windows')	v=
o	--RdMacros	Packages from which to get Rd macros	v=
a	1	0
=	CMD Rd2txt	--type
v	txt	
v	html	
v	latex	
v	example	
=	CMD Rd2txt	--output
v	""	
v	-	
=	CMD Rd2txt	--os
v	unix	
v	windows	
#	CMD Rd2txt	1
d
@	CMD Stangle
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--engine	Use named vignette engine	v=
o	--encoding	Set the encoding for file	v=
o	--options	Comma-separated list of Stangle options	v=
a	1	0
=	CMD Stangle	--engine
v	Stangle	
v	knitr::knit	
v	utils::Sweave	
#	CMD Stangle	1
t	folders
@	CMD Sweave
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--driver	Use named Sweave driver	v=
o	--engine	Use named vignette engine	v=
o	--encoding=enc	Default encoding 'enc' for file	v=
o	--clean	Remove some of the created files	V=
o	--options	Comma-separated list of Sweave/engine options	v=
o	--pdf	Convert to PDF document	
o	--compact	Try to compact PDF document	V=
a	1	0
=	CMD Sweave	--clean
v	default	
v	keepOuts	
=	CMD Sweave	--compact
v	no	
v	qpdf	
v	gs	
v	gs+qpdf	
v	both	
#	CMD Sweave	1
t	filepaths
@	CMD Rdiff
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
a	2	0
#	CMD Rdiff	1
t	filepaths
#	CMD Rdiff	2
t	filepaths
@	CMD config
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--cppflags	Print pre-processor flags required to compile a C/C++ file as part of a front-end using R as a…	
o	--ldflags	Print linker flags needed for linking a front-end against the R library	
o	--no-user-files	Ignore customization files under '~/.R'	
o	--no-site-files	Ignore site customization files under 'R_HOME/etc'	
o	--all	Print names and values of all variables	
a	1	0
#	CMD config	1
v	AR	
v	BLAS_LIBS	
v	CC	
v	CFLAGS	
v	CPICFLAGS	
v	CPPFLAGS	
v	CXX	
v	CXXFLAGS	
v	CXXPICFLAGS	
v	CXX11	
v	CXX11STD	
v	CXX11FLAGS	
v	CXX11PICFLAGS	
v	CXX14	
v	CXX14STD	
v	CXX14FLAGS	
v	CXX14PICFLAGS	
v	CXX17	
v	CXX17STD	
v	CXX17FLAGS	
v	CXX17PICFLAGS	
v	CXX20	
v	CXX20STD	
v	CXX20FLAGS	
v	CXX20PICFLAGS	
v	DYLIB_EXT	
v	DYLIB_LD	
v	DYLIB_LDFLAGS	
v	FC	
v	FFLAGS	
v	FCFLAGS	
v	FLIBS	
v	FPICFLAGS	
v	JAR	
v	JAVA	
v	JAVAC	
v	JAVAH	
v	JAVA_HOME	
v	JAVA_LIBS	
v	JAVA_CPPFLAGS	
v	LAPACK_LIBS	
v	LIBnn	
v	LDFLAGS	
v	LTO	
v	MAKE	
v	NM	
v	OBJC	
v	OBJCFLAGS	
v	RANLIB	
v	SAFE_FFLAGS	
v	SHLIB_CFLAGS	
v	SHLIB_CXXFLAGS	
v	SHLIB_CXXLD	
v	SHLIB_CXXLDFLAGS	
v	SHLIB_EXT	
v	SHLIB_FFLAGS	
v	SHLIB_LD	
v	SHLIB_LDFLAGS	
v	TCLTK_CPPFLAGS	
v	TCLTK_LIBS	
@	CMD javareconf
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	-n|--dry-run	Perform Java detection, but don't touch any configuration files	
o	-e	Same as -n but exports all detected variables and runs '<prog>'	v
a	1	0
#	CMD javareconf	1
v	JAVA_HOME=/usr/lib/java	
v	JAVAC=/usr/bin/javac	
v	JAR=/usr/bin/jar	
@	CMD rtags
o	--help|-h	Print help message and exit	
o	--version|-v	Print version info and exit	
o	--output|-o	Write output to a file	V
o	--no-c	Do not tag C (.c, .h) files	
o	--no-R	Do not tag R (.R, .r, .S, .s) files	
o	--no-Rd	Do not tag Rd (.Rd) files	
o	--ctags	Write Ctags format (default is Etags)	
o	--append|-a	Append to output file (overwrites by default)	
o	--verbose|-V	Echo the name of files processed	
a	1	0
