@	
o	--also-make|-am	Also build projects required by project list	
o	--also-make-dependents|-amd	Also build projects that depend on projects in the project list	
o	--batch-mode|-B	Run in non-interactive (batch)	
o	--builder|-b	Specify the build strategy to use	v
o	--strict-checksums|-C	Fail if checksums do not match	
o	--lax-checksums|-c	Warn if checksums do not match	
o	--color	Specify the color mode of the output	v
o	--check-plugin-updates|-cpu	Ineffective. Only kept for backward compatibility	
o	--define|-D	Define a system property	v
o	--errors|-e	Produce execution error messages	
o	--encrypt-master-password|-emp	Encrypt the master security password	v
o	--encrypt-password|-ep	Encrypt the server password	v
o	--file|-f	Force the use of an alternate POM file (or directory with pom.xml)	v
o	--fail-at-end|-fae	Only fail the build afterwards; allow all non-impacted builds to continue	
o	--fail-fast|-ff	Stop at first failure in reactorized builds	
o	--fail-never|-fn	Never fail the build, regardless of project result	
o	--global-settings|-gs	Specify the global settings file to use	v
o	--global-toolchains|-gt	Specify the global toolchains file to use	v
o	--help|-h	Display help information	
o	--log-file|-l	Specify the file to log to	v
o	--legacy-local-repository|-llr	Use the Maven2 legacy local repository behaviour	
o	--non-recursive|-N	Do not recurse into sub-projects	
o	--no-plugin-registry|-npr	Ineffective. Only kept for backward compatibility	
o	--no-plugin-updates|-npu	Ineffective. Only kept for backward compatibility	
o	--no-snapshot-updates|-nsu	Suppress SNAPSHOT updates	
o	--no-transfer-progress|-ntp	Do not display transfer progress when downloading or uploading	
o	--offline|-o	Work offline	
o	--activate-profiles|-P	Activate the specified profiles (comma delimited)	v
o	--projects|-pl	Specify the projects to build	v
o	--quiet|-q	Quiet output - only shows errors	
o	--resume-from|-rf	Resume from the specified project	v
o	--settings|-s	Specify the user settings file to use	v
o	--toolchains|-t	Specify the toolchains file to use	v
o	--threads|-T	Specify the number of threads to use	v
o	--update-snapshots|-U	Forces a check for missing releases and updated snapshots on remote repositories	
o	--update-plugins|-up	Ineffective. Only kept for backward compatibility	
o	--version|-v	Display version information	
o	--show-version|-V	Display version information	
o	--debug|-X	Produce execution debug output	
a	1	1
=		--color
v	always	
v	never	
v	auto	
=		--file
t	filepaths,folders
=		--global-settings
t	filepaths
=		--global-toolchains
t	filepaths
=		--log-file
t	filepaths
=		--settings
t	filepaths
=		--toolchains
t	filepaths
#		1
v	pre-clean	
v	clean	
v	post-clean	
v	validate	
v	initialize	
v	generate-sources	
v	process-sources	
v	generate-resources	
v	process-resources	
v	compile	
v	process-classes	
v	generate-test-sources	
v	process-test-sources	
v	generate-test-resources	
v	process-test-resources	
v	test-compile	
v	process-test-classes	
v	test	
v	prepare-package	
v	package	
v	pre-integration-test	
v	integration-test	
v	post-integration-test	
v	verify	
v	install	
v	deploy	
v	pre-site	
v	site	
v	post-site	
v	site-deploy	
