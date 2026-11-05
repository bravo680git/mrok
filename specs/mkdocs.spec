@	
s	build	Build the MkDocs documentation
s	gh-deploy	Deploy your documentation to GitHub Pages
s	new	Create a new MkDocs project
s	serve	Run the builtin development server
o	-h|--help	Show help message and exit	
o	-V|--version	Show the version and exit	
@	build
o	-h|--help	help for build	
o	-q|--quiet	Silence warnings	
o	-v|--verbose	Enable verbose output	
o	-f|--config-file	Provide a specific MkDocs config	v
o	-s|--strict	Enable strict mode. This will cause MkDocs to abort the build on any warnings	
o	-t|--theme	The theme to use when building your documentation	v
o	--use-directory-urls	Use directory URLs when building pages (the default)	
o	--no-directory-urls	Don't use directory URLs when building pages	
o	-c|--clean	Remove old files from the site directory before building (the default)	
o	--dirty	Only rebuild pages that have been modified since last build	
o	-d|--site-dir	The directory to output the result of the documentation build	v
=	build	-f
t	filepaths
=	build	-d
t	folders
@	gh-deploy
o	-h|--help	help for gh-deploy	
o	-q|--quiet	Silence warnings	
o	-v|--verbose	Enable verbose output	
o	-f|--config-file	Provide a specific MkDocs config	v
o	-s|--strict	Enable strict mode. This will cause MkDocs to abort the build on any warnings	
o	-t|--theme	The theme to use when building your documentation	v
o	--use-directory-urls	Use directory URLs when building pages (the default)	
o	--no-directory-urls	Don't use directory URLs when building pages	
o	-c|--clean	Remove old files from the site directory before building (the default)	
o	--dirty	Only rebuild pages that have been modified since last build	
o	-m|--message	A commit message to use when committing to the GitHub Pages remote branch. Commit {sha} and MkDocs…	v
o	-b|--remote-branch	The remote branch to commit to for GitHub Pages. This overrides the value specified in config	v
o	-r|--remote-name	The remote name to commit to for GitHub Pages. This overrides the value specified in config	v
o	--force	Force the push to the repository	
o	--no-history	Replace the whole Git history with one new commit	
o	--ignore-version	Ignore check that build is not being deployed with an older version of MkDocs	
o	--shell	Use the shell when invoking Git	
=	gh-deploy	-f
t	filepaths
@	new
o	-h|--help	help for new	
o	-q|--quiet	Silence warnings	
o	-v|--verbose	Enable verbose output	
a	1	0
#	new	1
t	folders
@	serve
o	-h|--help	help for serve	
o	-q|--quiet	Silence warnings	
o	-v|--verbose	Enable verbose output	
o	-f|--config-file	Provide a specific MkDocs config	v
o	-s|--strict	Enable strict mode. This will cause MkDocs to abort the build on any warnings	
o	-t|--theme	The theme to use when building your documentation	v
o	--use-directory-urls	Use directory URLs when building pages (the default)	
o	--no-directory-urls	Don't use directory URLs when building pages	
o	-a|--dev-addr	IP address and port to serve documentation locally (default: localhost:8000)	v
o	--live-reload	Enable the live reloading in the development server (this is the default)	
o	--no-reload	Disable the live reloading in the development server	
o	--dirtyreload	Enable the live reloading in the development server, but only re-build files that have changed	
o	--watch-theme	Include the theme in list of files to watch for live reloading. Ignored when live reload is not used	
o	-w|--watch	A directory or file to watch for live reloading. Can be supplied multiple times	v
=	serve	-f
t	filepaths
=	serve	-w
t	folders,filepaths
