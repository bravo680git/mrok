@	
o	--help|-h	Show help for ansible-lint	
o	--list-rules|-L	List all the rules	
o	--list-tags|-T	List all the tags and the rules they cover	
o	--format|-f	Stdout formatting	v
o	-q	Quieter, reduce verbosity, can be specified twice	
o	-p	Parseable output, same as '-f pep8'	
o	--progressive	Return success if it detects a reduction in number of violations compared with previous git…	
o	--project-dir	Location of project/repository, autodetected based on location of configuration file	v
o	--rules-dir|-r	Specify custom rule directories	v
o	-R	Keep using embedded rules when using '-r'	
o	--write	Allow ansible-lint to reformat YAML files and run rule transforms	v
o	--show-relpath	Display path relative to CWD	
o	--tags|-t	Only check rules whose id/tags match these values	
o	-v	Increase verbosity level (-vv for more)	
o	--skip-list|-x	Only check rules whose id/tags do not match these values	v
o	--warn-list|-w	Only warn about these rules, unless overridden in config file defaults to 'experimental'	v
o	--enable-list	Activate optional rules by their tag name	v
o	--nocolor	Disable colored output, same as NO_COLOR=1	
o	--force-color	Force colored output, same as FORCE_COLOR=1	
o	--exclude-paths	Path to directories or files to skip. This option is repeatable	v
o	--config-file	Specify configuration file to use. By default it will look for '.ansible-lint' or…	v
o	--offline	Disable installation of requirements.yml	
o	--version	Show version of ansible-lint	
a	1	1
=		--format
v	rich	
v	plain	
v	md	
v	json	
v	codeclimate	
v	quiet	
v	pep8	
v	sarif	
=		--project-dir
t	folders
=		--rules-dir
t	folders
=		--write
v	all	
v	none	
v	rule1,rule2,...	
=		--exclude-paths
t	folders
=		--config-file
t	filepaths
#		1
t	filepaths
