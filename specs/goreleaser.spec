@	
s	b|build	Builds the current project
s	c|check	Checks if configuration is valid
s	completion	Generate the autocompletion script for the specified shell
s	hc|healthcheck	Checks if needed tools are installed
s	i|init	Generates a .goreleaser.yaml file
s	schema|jsonschema	Outputs goreleaser's JSON schema
s	r|release	Releases the current project
s	help	Help about any command
o	--debug	Enable verbose mode	p
o	--verbose	Enable verbose mode	p
o	--help|-h	Display help	p
@	b
o	--clean	Remove the dist folder before building	
o	--config|-f	Load configuration from file	v
o	--id	Builds only the specified build ids	v
o	--output|-o	Copy the binary to the path after the build. Only taken into account when using --single-target…	v
o	--parallelism|-p	Amount tasks to run concurrently (default: number of CPUs)	v
o	--single-target	Builds only for current GOOS and GOARCH, regardless of what's set in the configuration file	
o	--skip	Skip the given options (valid options are: before, post-hooks, pre-hooks, validate)	v
o	--snapshot	Generate an unversioned snapshot build, skipping all validations	
o	--timeout	Timeout to the entire build process	v
=	b	--config
t	filepaths
=	b	--output
t	filepaths
@	c
o	--quiet|-q	Quiet mode: no output	
@	completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	completion bash
o	--no-descriptions	Disable completion descriptions	
@	completion fish
o	--no-descriptions	Disable completion descriptions	
@	completion powershell
o	--no-descriptions	Disable completion descriptions	
@	completion zsh
o	--no-descriptions	Disable completion descriptions	
@	hc
o	--config|-f	Configuration file	v
o	--quiet|-q	Quiet mode: no output	
=	hc	--config
t	filepaths
@	i
o	--config|-f	Load configuration from file	v
=	i	--config
t	filepaths
@	schema
o	--output|-o	Where to save the JSONSchema file	v
=	schema	--output
t	filepaths
@	r
o	--auto-snapshot	Automatically sets --snapshot if the repository is dirty	
o	--clean	Removes the dist folder	
o	--config|-f	Load configuration from file	v
o	--fail-fast	Whether to abort the release publishing on the first error	
o	--parallelism|-p	Amount tasks to run concurrently (default: number of CPUs)	v
o	--release-footer	Load custom release notes footer from a markdown file	v
o	--release-footer-tmpl	Load custom release notes footer from a templated markdown file (overrides --release-footer)	v
o	--release-header	Load custom release notes header from a markdown file	v
o	--release-header-tmpl	Load custom release notes header from a templated markdown file (overrides --release-header)	v
o	--release-notes	Load custom release notes from a markdown file (will skip GoReleaser changelog generation)	v
o	--release-notes-tmpl	Load custom release notes from a templated markdown file (overrides --release-notes)	v
o	--skip	Skip the given options (valid options are announce, aur, before, chocolatey, docker, homebrew, ko…	v
o	--snapshot	Generate an unversioned snapshot release, skipping all validations and without publishing any…	
o	--timeout	Timeout to the entire release process	v
=	r	--config
t	filepaths
=	r	--release-footer
t	filepaths
=	r	--release-footer-tmpl
t	filepaths
=	r	--release-header
t	filepaths
=	r	--release-header-tmpl
t	filepaths
=	r	--release-notes
t	filepaths
=	r	--release-notes-tmpl
t	filepaths
@	help
s	b|build	Builds the current project
s	c|check	Checks if configuration is valid
s	completion	Generate the autocompletion script for the specified shell
s	hc|healthcheck	Checks if needed tools are installed
s	i|init	Generates a .goreleaser.yaml file
s	schema|jsonschema	Outputs goreleaser's JSON schema
s	r|release	Releases the current project
@	help b
@	help c
@	help completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh
@	help hc
@	help i
@	help schema
@	help r
