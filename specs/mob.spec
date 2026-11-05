@	
s	start|s	Start session from base branch in wip branch
s	next|n	Handover changes in wip branch to next person
s	done|d	Squashes all changes in wip branch to index in base branch
s	reset	Removes local and remote wip branch
s	clean	Removes all orphan wip branches
s	timer|t	Start a <minutes> timer
s	break	Start a <minutes> break timer
s	status	Show the status of the current session
s	fetch	Fetch remote state
s	branch|b	Show remote wip branches
s	config	Show all configuration options
s	version	Show the version
s	help	Show help
s	moo	Moo!
o	--debug	Enable verbose logging	
@	start
o	--include-uncommitted-changes|-i	Move uncommitted changes to wip branch	
o	--branch|-b	Set wip branch to 'mob/<base-branch>/<branch-postfix>'	v
a	1	0
@	next
o	--stay|-s	Stay on wip branch (default)	
o	--return-to-base-branch|-r	Return to base branch	
o	--message|-m	Override commit message	v
@	done
o	--no-squash	Squash no commits from wip branch, only merge wip branch	
o	--squash	Squash all commits from wip branch	
o	--squash-wip	Squash wip commits from wip branch, maintaining manual commits	
@	reset
o	--branch|-b	Set wip branch to 'mob/<base-branch>/<branch-postfix>'	v
@	clean
@	timer
a	1	0
@	break
a	1	0
@	status
@	fetch
@	branch
@	config
@	version
@	help
@	moo
