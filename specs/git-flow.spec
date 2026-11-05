@	
s	init	Initialize a new git repo with support for the branching model
s	feature	List all feature branches
s	release	List all release branches
s	hotfix	List all hotfix branches
s	support	List all support branches
@	init
o	-d	Use default branch naming conventions	
o	-f	Force setting of gitflow branches, even if already configured	
@	feature
s	start	Create a new feature branch
s	finish	Merge a feature branch into develop
s	publish	Push a feature branch to the remote repository
s	pull	Pull a feature branch from the remote repository
@	feature start
a	1	0
@	feature finish
a	1	0
#	feature finish	1
d
@	feature publish
a	1	0
@	feature pull
a	2	0
@	release
s	start	Create a new release branch
s	finish	Merge a release branch into develop
@	release start
a	1	0
@	release finish
a	1	0
#	release finish	1
d
@	hotfix
s	start	Create a new hotfix branch
s	finish	Merge a hotfix branch into develop
@	hotfix start
a	1	0
@	hotfix finish
a	1	0
#	hotfix finish	1
d
@	support
s	start	Create a new support branch
@	support start
a	1	0
