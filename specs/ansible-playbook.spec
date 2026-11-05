@	
o	--ask-vault-pass	Ask for vault password	
o	--flush-cache	Clears the fact cache for every host in inventory	
o	--force-handlers	Run handlers even if a task fails	
o	--list-hosts	Outputs a list of matching hosts; does not execute	
o	--list-tags	List all available tags	
o	--list-tasks	List all tasks that would be executed	
o	--skip-tags	Only run plays and tasks whose tags do not match these values	v
o	--start-at-task	Start the playbook at the task matching this name one-step-at-a-time	v
o	--step	Execute one-step-at-a-time	
o	--syntax-check	Perform a syntax check on the playbook, but do not execute it	
o	--vault-id	Specify the vault identity to use	v
o	--vault-password-file	Specify a vault password file	v
o	--version	Show program's version number, config file location, configured module search path, module…	
o	--check|-C	Don't make any changes; instead, try to predict some of the changes that may occur	
o	--diff|-D	When changing (small) files and templates, show the differences in those files	
o	--module-path|-M	Prepend colon-separated path(s) to module library	v
o	--extra-vars|-e	Set additional variables as key=value or YAML/JSON, if filename prepend with @	v
o	--forks|-f	Specify number of parallel processes to use	v
o	--help|-h	Show help for ansible	
o	--inventory|-i	Specify inventory host path or comma separated host list	v
o	--limit|-l	Limit selected hosts to an additional pattern	v
o	--tags|-t	Only run plays and tasks tagged with these values	v
o	--verbose|-v	Enable verbose mode	
o	-vvv	Enable very verbose mode	
o	-vvvv	Enable connection debug mode	
o	--become-method	Privilege escalation method to use	v
o	--become-user	Privilege escalation user to use	v
o	--ask-become-pass|-K	Prompt for privilege escalation password	
o	--become|-b	Run operations with become	
o	--private-key|--key-file	Use this fole to authenticate the connection	v
o	--scp-extra-args	Extra arguments to pass to (only) scp	v
o	--sftp-extra-args	Extra arguments to pass to (only) sftp	v
o	-ssh-extra-args	Extra arguments to pass to (only) ssh	v
o	--ssh-common-args	Extra arguments to pass to sftp/scp/ssh	v
o	--timeout|-T	Override the connection timeout in seconds	v
o	--connection|-c	Connection type to use	v
o	--ask-pass|-k	Ask for connection password	
o	--user|-u	Connect as this user	v
a	1	1
=		--vault-password-file
t	filepaths
=		--module-path
t	folders
=		--become-method
v	sudo	
v	su	
v	pbrun	
v	pfexec	
v	doas	
v	dzdo	
v	ksu	
v	runas	
v	machinectl	
=		--private-key
t	filepaths
#		1
d
