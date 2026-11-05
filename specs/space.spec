@	
s	completion	Generate the autocompletion script for the specified shell
s	link	Link code to project
s	login	Login to space
s	new	Create new project
s	open	Open current project in browser
s	push	Push code for project
s	release	Create release for a project
s	validate	Validate spacefile in dir
s	version	Space CLI version
s	help	Help about any command
o	--help|-h	Display help	p
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
@	link
o	--dir|-d	Src of project to link	v
o	--id|-i	Project id of project to link	v
=	link	--dir
t	folders
@	login
@	new
o	--blank|-b	Create blank project	
o	--dir|-d	Src of project to release	v
o	--name|-n	Project name	v
=	new	--dir
t	folders
@	open
o	--dir|-d	Src of project to open	v
o	--id|-i	Project id of project to open	v
=	open	--dir
t	folders
@	push
o	--dir|-d	Src of project to push	v
o	--id|-i	Project id of project to push	v
o	--open|-o	Open builder instance/project in browser after push	
o	--skip-logs	Skip following logs after push	
o	--tag|-t	Tag to identify this push	v
=	push	--dir
t	folders
@	release
o	--confirm|-c	Release latest revision	
o	--dir|-d	Src of project to release	v
o	--id|-i	Project id of an existing project	v
o	--listed|-l	Listed on discovery	
o	--notes|-n	Release notes	v
o	--rid|-r	Revision id for release	v
o	--version|-v	Version for the release	v
=	release	--dir
t	folders
@	validate
o	--dir|-d	Src of project to validate	v
=	validate	--dir
t	folders
@	version
s	upgrade	Upgrade Space CLI version
@	version upgrade
o	--version|-v	Version number	v
@	help
s	completion	Generate the autocompletion script for the specified shell
s	link	Link code to project
s	login	Login to space
s	new	Create new project
s	open	Open current project in browser
s	push	Push code for project
s	release	Create release for a project
s	validate	Validate spacefile in dir
s	version	Space CLI version
@	help completion
s	bash	Generate the autocompletion script for bash
s	fish	Generate the autocompletion script for fish
s	powershell	Generate the autocompletion script for powershell
s	zsh	Generate the autocompletion script for zsh
@	help completion bash
@	help completion fish
@	help completion powershell
@	help completion zsh
@	help link
@	help login
@	help new
@	help open
@	help push
@	help release
@	help validate
@	help version
s	upgrade	Upgrade Space CLI version
@	help version upgrade
