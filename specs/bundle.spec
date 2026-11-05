@	
s	install	Install the gems specified by the Gemfile or Gemfile.lock
s	update	Update dependencies to their latest versions
s	package	Package the .gem files required by your application into the vendor/cache directory
s	exec	Execute a command in the context of the bundle
s	config	
s	help	
s	add	Add gem to the Gemfile and run bundle install
s	binstubs	Install the binstubs of the listed gems
s	check	Determine whether the requirements for your application are installed and available to Bundler
s	show	Show the source location of a particular gem in the bundle
s	outdated	Show all of the outdated gems in the current bundle
s	console	Start an IRB session in the current bundle
s	open	Open an installed gem in the editor
s	lock	Generate a lockfile for your dependencies
s	viz	Generate a visual representation of your dependencies
s	init	Generate a simple Gemfile, placed in the current directory
s	gem	Create a simple gem, suitable for development with Bundler
s	platform	Display platform compatibility information
s	clean	Clean up unused gems in your Bundler directory
s	doctor	Display warnings about common problems
o	--no-color	Print all output without color	
o	--retry|-r	Specify the number of times you wish to attempt network commands	
o	--verbose|-V	Print out additional logging information	
@	install
o	--binstubs	Create binstubs in dir	v
o	--clean	Remove unused gems after install	
o	--deployment	For Production and CI use	
o	--force|--redownload	Redownload all gems	
o	--frozen	Do not allow lock file to update	
o	--full-index	Cache the full index locally	
o	--gemfile	The gemfile to use	v
o	--jobs	Maximum number of parallel installs	v
o	--local	Use only gems already downloaded or cached	
o	--no-cache	Do not use vendor/cache	
o	--no-prune	Do not remove stale gems	
o	--path	Path the install gems too	v
o	--quiet	Do not print to stdout	
o	--retry	Retry failed network requests N times	v
o	--shebang	Uses the specified ruby executable for binstubs	v
o	--standalone	Makes a bundle that can work without depending on Rubygems or Bundler at runtime	v
o	--system	Use system Rubygems location	
o	--trust-policy	Apply the Rubygems security policy	v
o	--with	Groups to install	v
o	--without	Groups to NOT install	v
=	install	--binstubs
t	folders
=	install	--gemfile
t	filepaths
=	install	--path
t	folders
@	update
o	--all	Update all gems specified in Gemfile	
o	--group|-g	Only update the gems in the specified group	v
o	--source	The name of a :git or :path source used in the Gemfile	v
o	--local	Use only gems already downloaded or cached	
o	--ruby	Update the locked version of Ruby to the current version of Ruby	
o	--bundler	Update the locked version of bundler to the invoked bundler version	
o	--full-index	Fall back to using the single-file index of all gems	
o	--jobs|-j	Specify the number of jobs to run in parallel. The default is 1	v
o	--retry	Retry failed network or git requests for number times	v
o	--quiet	Only output warnings and errors	
o	--force|--redownload	Force downloading every gem	
o	--patch	Prefer updating only to next patch version	
o	--minor	Prefer updating only to next minor version	
o	--major	Prefer updating to next major version (default)	
o	--strict	Do not allow any gem to be updated past latest --patch | --minor | --major	
o	--conservative	Do not allow shared dependencies to be updated	
a	1	0
#	update	1
d
@	package
@	exec
o	--keep-file-descriptors	Pass all file descriptors to the new process	
a	1	0
@	config
a	1	0
@	help
@	add
o	--version|-v	Specify version requirements	
o	--group|-g	Specify the group(s) for the added gem	
o	--source|-s	Specify the source	
o	--skip-install	Adds the gem to the Gemfile but does not install it	
o	--optimistic	Adds optimistic declaration of version	
o	--strict	Adds strict declaration of version	
a	1	0
@	binstubs
o	--force	Overwrite existing binstubs	
o	--path	The location to install the specified binstubs to	
o	--standalone	Makes binstubs that can work without depending on Rubygems or Bundler at runtime	
o	--shebang	Specify a different shebang executable name than the default	
a	1	0
@	check
o	--dry-run	Locks the Gemfile before running the command	
o	--gemfile	Use the specified gemfile instead of the Gemfile	
o	--path	Specify a different path than the system default	
@	show
o	--paths	List the paths of all gems that are required by your Gemfile	
a	1	0
#	show	1
d
@	outdated
o	--local	Do not attempt to fetch gems remotely and use the gem cache instead	
o	--pre	Check for newer pre-release gems	
o	--source	Check against a specific source	
o	--strict	Only list newer versions allowed by your Gemfile requirements	
o	--parseable|--porcelain	Use minimal formatting for more parseable output	
o	--group	List gems from a specific group	
o	--groups	List gems organized by groups	
o	--update-strict	Strict conservative resolution, do not allow any gem to be updated past latest --patch | --minor|…	
o	--minor	Prefer updating only to next minor version	
o	--major	Prefer updating to next major version (default)	
o	--patch	Prefer updating only to next patch version	
o	--filter-major	Only list major newer versions	
o	--filter-minor	Only list minor newer versions	
o	--filter-patch	Only list patch newer versions	
o	--only-explicit	Only list gems specified in your Gemfile, not their dependencies	
@	console
@	open
a	1	0
#	open	1
d
@	lock
o	--update	Ignores the existing lockfile	v
o	--local	Do not attempt to connect to rubygems.org	
o	--print	Prints the lockfile to STDOUT instead of writing to the file	
o	--lockfile	The path where the lockfile should be written to	v
o	--full-index	Fall back to using the single-file index of all gems	
o	--add-platform	Add a new platform to the lockfile, re-resolving for the addi-	
o	--remove-platform	Remove a platform from the lockfile	
o	--patch	If updating, prefer updating only to next patch version	
o	--minor	If updating, prefer updating only to next minor version	
o	--major	If updating, prefer updating to next major version (default)	
o	--strict	If updating, do not allow any gem to be updated past latest --patch | --minor | --major	
o	--conservative	If updating, use bundle install conservative update behavior and do not allow shared dependencies…	
@	viz
o	--file|-f	The name to use for the generated file. See --format option	
o	--format|-F	This is output format option	
o	--requirements|-R	Set to show the version of each required dependency	
o	--version|-v	Set to show each gem version	
o	--without|-W	Exclude gems that are part of the specified named group	
@	init
o	--gemspec	Use the specified .gemspec to create the Gemfile	
@	gem
o	--exe|-b|--bin	Specify that Bundler should create a binary executable	
o	--no-exe	Do not create a binary	
o	--coc	Add a CODE_OF_CONDUCT.md file to the root of the generated project	
o	--no-coc	Do not create a CODE_OF_CONDUCT.md	
o	--ext	Add boilerplate for C extension code to the generated project	
o	--no-ext	Do not add C extension code	
o	--mit	Add an MIT license	
o	--no-mit	Do not create a LICENSE.txt	
o	-t|--test	Specify the test framework that Bundler should use	v
o	-e|--edit	Open the resulting gemspec in EDITOR	v
@	platform
o	--ruby	It will display the ruby directive information so you don't have to parse it from the Gemfile	
@	clean
o	--dry-run	Print the changes, but do not clean the unused gems	
o	--force	Force a clean even if --path is not set	
@	doctor
o	--quiet	Only output warnings and errors	
o	--gemfile	The location of the Gemfile which Bundler should use	v
