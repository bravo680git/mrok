@	
s	ls	Lists all the files that will be published
s	package	Packages an extension
s	publish	Publishes an extension
s	unpublish	Unpublishes an extension. Example extension id: microsoft.csharp
s	ls-publishers	List all known publishers
s	delete-publisher	Deletes a publisher
s	login	Add a publisher to the known publishers list
s	logout	Remove a publisher from the known publishers list
s	verify-pat	Verify if the Personal Access Token has publish rights for the publisher
s	show	Show extension metadata
s	search	Search extension gallery
s	help	Display help for command
o	-h|--help	Display help for command	p
o	-V|--version	Output the version number	
@	ls
o	--yarn	Use yarn instead of npm (default inferred from presence of yarn.lock or .yarnrc)	
o	--no-yarn	Use npm instead of yarn (default inferred from lack of yarn.lock or .yarnrc)	
o	--packagedDependencies	Select packages that should be published only (includes dependencies)	v
o	--ignoreFile	Indicate alternative .vscodeignore	v
o	--no-dependencies	Disable dependency detection via npm or yarn	
=	ls	--packagedDependencies
t	filepaths
=	ls	--ignoreFile
t	filepaths
@	package
o	-o|--out	Output .vsix extension file to <path> location (defaults to <name>-<version>.vsix)	v
o	-t|--target	Target architecture	v
o	-m|--message	Commit message used when calling `npm version`	v
o	--no-git-tag-version	Do not create a version commit and tag when calling `npm version`. Valid only when [version] is…	
o	--no-update-package-json	Do not update `package.json`. Valid only when [version] is provided	
o	--githubBranch	The GitHub branch used to infer relative links in README.md. Can be overridden by --baseContentUrl…	v
o	--gitlabBranch	The GitLab branch used to infer relative links in README.md. Can be overridden by --baseContentUrl…	v
o	--no-rewrite-relative-links	Skip rewriting relative links	
o	--baseContentUrl	Prepend all relative links in README.md with this url	v
o	--baseImagesUrl	Prepend all relative image links in README.md with this url	v
o	--yarn	Use yarn instead of npm (default inferred from presence of yarn.lock or .yarnrc)	
o	--no-yarn	Use npm instead of yarn (default inferred from lack of yarn.lock or .yarnrc)	
o	--ignoreFile	Indicate alternative .vscodeignore	v
o	--no-gitHubIssueLinking	Disable automatic expansion of GitHub-style issue syntax into links	
o	--no-gitLabIssueLinking	Disable automatic expansion of GitLab-style issue syntax into links	
o	--no-dependencies	Disable dependency detection via npm or yarn	
o	--pre-release	Mark this package as a pre-release	
=	package	-o
d
=	package	-t
v	win32-x64	
v	win32-ia32	
v	win32-arm64	
v	linux-x64	
v	linux-arm64	
v	linux-armhf	
v	alpine-x64	
v	alpine-arm64	
v	darwin-x64	
v	darwin-arm64	
=	package	--githubBranch
d
=	package	--gitlabBranch
d
=	package	--ignoreFile
t	filepaths
@	publish
o	-p|--pat	Personal Access Token (defaults to VSCE_PAT environment variable)	v
o	-t|--target	Target architecture	v
o	-m|--message	Commit message used when calling `npm version`	v
o	--no-git-tag-version	Do not create a version commit and tag when calling `npm version`. Valid only when [version] is…	
o	--no-update-package-json	Do not update `package.json`. Valid only when [version] is provided	
o	-i|--packagePath	Publish the provided VSIX packages	v
o	--githubBranch	The GitHub branch used to infer relative links in README.md. Can be overridden by --baseContentUrl…	v
o	--gitlabBranch	The GitLab branch used to infer relative links in README.md. Can be overridden by --baseContentUrl…	v
o	--baseContentUrl	Prepend all relative links in README.md with this url	v
o	--baseImagesUrl	Prepend all relative image links in README.md with this url	v
o	--yarn	Use yarn instead of npm (default inferred from presence of yarn.lock or .yarnrc)	
o	--no-yarn	Use npm instead of yarn (default inferred from lack of yarn.lock or .yarnrc)	
o	--noVerify		
o	--ignoreFile	Indicate alternative .vscodeignore	v
o	--no-dependencies	Disable dependency detection via npm or yarn	
o	--pre-release	Mark this package as a pre-release	
=	publish	-t
v	win32-x64	
v	win32-ia32	
v	win32-arm64	
v	linux-x64	
v	linux-arm64	
v	linux-armhf	
v	alpine-x64	
v	alpine-arm64	
v	darwin-x64	
v	darwin-arm64	
=	publish	-i
d
=	publish	--githubBranch
d
=	publish	--gitlabBranch
d
=	publish	--ignoreFile
t	filepaths
@	unpublish
o	-p|--pat	Personal Access Token	v
o	-f|--force	Forces Unpublished Extension	
@	ls-publishers
@	delete-publisher
a	1	0
@	login
a	1	0
@	logout
a	1	0
@	verify-pat
o	-p|--pat	Personal Access Token (defaults to VSCE_PAT environment variable)	v
a	1	0
@	show
o	--json	Output data in json format (default: false)	
a	1	0
@	search
o	--json	Output data in json format (default: false)	
a	1	0
@	help
a	1	0
#	help	1
v	ls	
v	package	
v	publish	
v	unpublish	
v	ls-publishers	
v	delete-publishers	
v	login	
v	logout	
v	verify-pat	
v	show	
v	search	
