@	
s	alias	Create command shortcuts
s	api	Make an authenticated GitHub API request
s	auth	Login, logout, and refresh your authentication
s	gpg-key	Manage GPG keys registered with your GitHub account
s	browse	Open the repository in the browser
s	completion	Generate shell completion scripts
s	config	Manage configuration for gh
s	extensions	Manage gh extensions
s	gist	Manage gists
s	issue	Manage issues
s	pr	Manage pull requests
s	release	Manage GitHub releases
s	repo	Work with GitHub repositories
s	run	View details about workflow runs
s	secret	Manage GitHub secrets
s	ssh-key	Manage SSH keys
s	workflow	View details about GitHub Actions workflows
s	codespace|cs	Connect to and manage codespaces
s	project	Manage projects
o	--help	Show help for command	p
a	1	0
#		1
d
@	alias
s	delete	Delete an alias
s	list	List available aliases
s	set	Set an alias for a gh command
@	alias delete
a	1	0
#	alias delete	1
d
@	alias list
@	alias set
o	-s|--shell	Declare an alias to be passed through a shell interpreter	
a	2	0
@	api
@	auth
s	login	Authenticate with a GitHub host
s	logout	Log out of a GitHub host
s	refresh	Refresh stored authentication credentials
s	setup-git	Configure git to use GitHub CLI as a credential helper
s	status	View authentication status
@	auth login
o	-h|--hostname	The hostname of the GitHub instance to authenticate with	v
o	-s|--scopes	Additional authentication scopes for gh to have	v
o	-w|--web	Open a browser to authenticate	
o	--with-token	Read token from standard input	v
@	auth logout
o	-h|--hostname	The hostname of the GitHub instance to authenticate with	v
@	auth refresh
o	-h|--hostname	The hostname of the GitHub instance to authenticate with	v
o	-s|--scopes	Additional authentication scopes for gh to have	v
@	auth setup-git
o	-h|--hostname	The hostname of the GitHub instance to authenticate with	v
@	auth status
o	-h|--hostname	The hostname of the GitHub instance to authenticate with	v
o	--with-token	Read token from standard input	v
@	gpg-key
s	add	Add a GPG key to your GitHub account
s	list	Lists GPG keys in your GitHub account
@	gpg-key add
@	gpg-key list
@	browse
o	-b|--branch	Select another branch by passing in the branch name	v
o	-c|--commit	Open the last commit	
o	-n|--no-browser	Print destination URL instead of opening the browser	
o	-p|--projects	Open repository projects	
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
o	-s|--settings	Open repository settings	
o	-w|--wiki	Open repository wiki	
a	1	0
=	browse	-b
d
#	browse	1
d
@	completion
o	-s|--shell		v
=	completion	-s
v	bash	
v	zsh	
v	fish	
v	powershell	
@	config
s	get	Print the value of a given configuration key
s	set	Update configuration with a value for the given key
@	config get
o	-h|--host	Get per-host setting	v
a	1	0
#	config get	1
v	git_protocol	
v	editor	
v	prompt	
v	pager	
v	http_unix_socket	
@	config set
s	git_protocol	The protocol to use for git clone and push operations
s	editor	The text editor program to use for authoring text
s	prompt	Toggle interactive prompting in the terminal
s	pager	The terminal pager program to send standard output to
s	http_unix_socket	The path to a unix socket through which to make HTTP connection
o	-h|--host	Get per-host setting	v
@	config set git_protocol
a	1	0
#	config set git_protocol	1
v	https	
v	ssh	
@	config set editor
a	1	0
#	config set editor	1
v	vim	
v	nano	
@	config set prompt
a	1	0
#	config set prompt	1
v	enable	
v	disable	
@	config set pager
a	1	0
@	config set http_unix_socket
a	1	0
@	extensions
s	create	Create a new extension
s	install	Install a gh extension from a repository
s	list	List installed extension commands
s	remove	Remove an installed extension
s	upgrade	Upgrade installed extensions
@	extensions create
a	1	0
@	extensions install
a	1	0
@	extensions list
@	extensions remove
a	1	0
@	extensions upgrade
o	--all	Upgrade all extensions	
o	--force	Force upgrade extensions	
a	1	0
@	gist
s	clone	Clone a gist locally
s	create	Create a new gist
s	delete	Delete a gist
s	edit	Edit one of your gists
s	list	List your gists
s	view	View a gist
@	gist clone
a	2	0
#	gist clone	2
t	folders
@	gist create
o	-d|--desc	A description for this gist	v
o	-f|--filename	Provide a filename to be used when reading from STDIN	v
o	-p|--public	List the gist publicly (default: secret)	
o	-w|--web	Open the web browser with created gist	
a	1	0
=	gist create	-f
t	filepaths
#	gist create	1
t	filepaths
@	gist delete
a	1	0
@	gist edit
o	-a|--add	Add a new file to the gist	v
o	-f|--filename	Select a file to edit	
a	1	0
=	gist edit	-a
t	filepaths
@	gist list
o	-L|--limit	Maximum number of gists to fetch (default 10)	v
o	--public	Show only public gists	
o	--secret	Show only secret gists	
@	gist view
o	-f|--filename	Display a single file from the gist	
o	--files	List file names from the gist	
o	-r|--raw	Print raw instead of rendered gist contents	
o	-w|--web	Open gist in the browser	
a	1	0
@	issue
s	close	Close issue
s	comment	Create a new issue comment
s	create	Create a new issue
s	delete	Delete issue
s	edit	Edit an issue
s	list	List and filter issues in this repository
s	reopen	Reopen issue
s	status	Show status of relevant issues
s	transfer	Transfer issue to another repository
s	view	View an issue
@	issue close
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
a	1	0
@	issue comment
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
o	-b|--body	Supply a body. Will prompt for one otherwise	v
o	-F|--body-file	Read body text from file	v
o	-e|--editor	Add body using editor	v
o	-w|--web	Add body in browser	
a	1	0
=	issue comment	-F
t	filepaths
@	issue create
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
o	-a|--assignee	Assign people by their login. Use "@me" to self-assign	v
o	-b|--body	Supply a body. Will prompt for one otherwise	v
o	-F|--body-file	Read body text from file	v
o	-l|--label	Add labels by name	v
o	-m|--milestone	Add the issue to a milestone by name	v
o	-p|--project	Add the issue to projects by name	v
o	--recover	Recover input from a failed run of create	v
o	-t|--title	Supply a title. Will prompt for one otherwise	v
o	-w|--web	Open the browser to create an issue	
=	issue create	-F
t	filepaths
@	issue delete
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
@	issue edit
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
o	--add-assignee	Add assigned users by their login. Use "@me" to assign yourself	v
o	--add-label	Add labels by name	v
o	-b|--body	Set the new body	v
o	-F|--body-file	Read body text from file	v
o	-m|--milestone	Edit the milestone the issue belongs to by name	v
o	--remove-assignee	Remove assigned users by their login. Use "@me" to unassign yourself	v
o	--remove-label	Remove labels by name	v
o	--remove-project	Remove the issue from projects by name	v
o	-t|--title	Set the new title	v
a	1	0
=	issue edit	-F
t	filepaths
@	issue list
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
o	-a|--assignee	Filter by assignee	v
o	-A|--author	Filter by author	v
o	-q|--jq	Filter JSON output using a jq expression	v
o	--json	Output JSON with the specified fields	v
o	-l|--label	Filter by labels	v
o	-L|--limit	Maximum number of issues to fetch (default 30)	v
o	--mention	Filter by mention	v
o	-m|--milestone	Filter by milestone number or `title`	v
o	-S|--search	Search issues with query	v
o	-s|--state	Filter by state (default "open")	v
o	-t|--template	Format JSON output using a Go template	v
o	-w|--web	Open the browser to list the issue(s)	
=	issue list	-s
v	open	
v	closed	
v	all	
@	issue reopen
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
@	issue status
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
o	-q|--jq	Filter JSON output using a jq expression	v
o	--json	Output JSON with the specified fields	v
o	-t|--template	Format JSON output using a Go template	v
@	issue transfer
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
a	2	0
@	issue view
o	-R|--repo	Select another repository using the [HOST/]OWNER/REPO format	v
o	-c|--comments	View issue comments	
o	-q|--jq	Filter JSON output using a jq expression	v
o	--json	Output JSON with the specified fields	v
o	-t|--template	Format JSON output using a Go template	v
o	-w|--web	Open an issue in the browser	
a	1	0
@	pr
s	checkout	Check out a pull request in git
s	checks	Show CI status for a single pull request
s	close	Close a pull request
s	edit	Edit a pull request. Without an argument, the pull request that belongs to the current branch is…
s	comment	Create a new pr comment
s	create	Create a pull request
s	diff	View changes in a pull request
s	list	List and filter pull requests in this repository
s	merge	Merge a pull request
s	ready	Mark a pull request as ready for review
s	reopen	Reopen a pull request
s	review	Add a review to a pull request
s	status	Show status of relevant pull requests
s	view	View a pull request
@	pr checkout
o	--recurse-submodules	Update all active submodules (recursively)	
a	1	0
#	pr checkout	1
d
@	pr checks
o	-w|--web	Open the web browser to show details about checks	
a	1	0
#	pr checks	1
d
@	pr close
o	-d|--delete-branch	Delete the local and remote branch after close	
a	1	0
#	pr close	1
d
@	pr edit
o	--add-assignee	Add assigned users by their login. Use "@me" to assign yourself	v
o	--add-label	Add labels by name	v
o	--add-project	Add the pull request to projects by name	v
o	--add-reviewer	Add reviewers by their login	v
o	-B|--base	Change the base branch for this pull request	v
o	-b|--body	Set the new body	v
o	-F|--body-file	Read body text from file (use "-" to read from standard input)	v
o	-m|--milestone	Edit the milestone the pull request belongs to by name	v
o	--remove-assignee	Remove assigned users by their login. Use "@me" to unassign yourself	v
o	--remove-label	Remove labels by name	v
o	--remove-project	Remove the pull request from projects by name	v
o	--remove-reviewer	Remove reviewers by their login	v
o	-t|--title	Set the new title	v
o	--repo|-R	Select another repository	v
a	1	0
#	pr edit	1
d
@	pr comment
o	-b|--body	Supply a body. Will prompt for one otherwise	v
o	-e|--editor	Add body using editor	
o	-w|--web	Add body in browser	
a	1	0
#	pr comment	1
d
@	pr create
o	-a|--assignee	Assign people by their login	v
o	-B|--base	The branch into which you want your code merged	v
o	-b|--body	Body for the pull request	v
o	-d|--draft	Mark pull request as a draft	
o	-f|--fill	Do not prompt for title/body and just use commit info	
o	-H|--head	The branch that contains commits for your pull request (default: current branch)	v
o	-l|--label	The branch that contains commits for your pull request (default: current branch)	v
o	-m|--milestone	Add the pull request to a milestone by name	v
o	--no-maintainer-edit	Disable maintainer's ability to modify pull request	
o	-p|--project	Add the pull request to projects by name	v
o	-recover	Recover input from a failed run of create	v
o	-r|--reviewer	Request reviews from people or teams by their handle	v
o	-t|--title	Title for the pull request	v
o	-w|--web	Open the web browser to create a pull request	
=	pr create	-B
d
@	pr diff
o	--color	Use color in diff output: {always|never|auto}	v
a	1	0
#	pr diff	1
d
@	pr list
o	-a|--assignee	Filter by assignee	v
o	-B|--base	Filter by base branch	v
o	-l|--label	Filter by labels	v
o	-L|--limit	Maximum number of items to fetch	v
o	-s|--state	Filter by state: {open|closed|merged|all}	v
o	-w|--web	Open the browser to list the pull requests	v
@	pr merge
o	-d|--delete-branch	Delete the local and remote branch after merge	
o	-m|--merge	Merge the commits with the base branch	
o	-r|--rebase	Rebase the commits onto the base branch	
o	-s|--squash	Squash the commits into one commit and merge it into the base branch	
a	1	0
#	pr merge	1
d
@	pr ready
a	1	0
#	pr ready	1
d
@	pr reopen
a	1	0
#	pr reopen	1
d
@	pr review
o	-a|--approve	Approve pull request	
o	-b|--body	Specify the body of a review	v
o	-c|--comment	Comment on a pull request	
o	-r|--request-changes	Request changes on a pull request	
a	1	0
#	pr review	1
d
@	pr status
@	pr view
o	-c|--comments	View pull request comments	
o	-w|--web	Open a pull request in the browser	
a	1	0
#	pr view	1
d
@	release
@	repo
s	archive	Archive a GitHub repository. With no argument, archives the current repository
s	clone	Clone a GitHub repository locally.
s	create	Create a new GitHub repository.
s	deploy-key	Manage deploy keys in a repository
s	delete	Delete a GitHub repository.
s	edit	Edit repository settings
s	fork	Create a fork of a repository.
s	list	List repositories owned by user or organization.
s	rename	Rename a GitHub repository.
s	set-default	Sets the default remote repository to use when querying the GitHub API for the locally cloned…
s	sync	Sync destination repository from source repository. Syncing uses the main branch
s	view	Display the description and the README of a GitHub repository.
@	repo archive
o	-y|--confirm	Skip the confirmation prompt	
a	1	0
#	repo archive	1
d
@	repo clone
o	--	Flags to pass to git when cloning	v
o	-u|--upstream-remote-name	Upstream remote name when cloning a fork (default "upstream")	v
a	2	0
#	repo clone	1
d
@	repo create
o	-y|--confirm	Skip the confirmation prompt	
o	-d|--description	Description of the repository	v
o	-h|--homepage	Repository home page URL	v
o	--public	Make the repository public	
o	--private	Make the repository private	
o	--internal	Make the repository internal	
o	-p|--template	Make the new repository based on a template repository	v
o	-c|--clone	Clone the new repository to the current directory	
o	--disable-issues	Disable issues in the new repository	
o	--disable-wiki	Disable wiki in the new repository	
o	-g|--gitignore	Specify a gitignore template for the repository	v
o	-l|--license	Specify an Open Source License for the repository	v
o	-r|--remote	Specify remote name for the new repository	v
o	-s|--source	Specify path to local repository to use as source	v
o	-t|--team	The name of the organization team to be granted access	v
o	--include-all-branches	Include all branches from template repository	
o	--push	Push local commits to the new repository	
o	--add-readme	Add a README file to the new repository	
a	1	0
@	repo deploy-key
s	add	Add a deploy key to a GitHub repository
s	delete	Delete a deploy key from a GitHub repository
s	list	List deploy keys in a GitHub repository
o	-R|--repo	Select another repository using the `[HOST/]OWNER/REPO` format	v
@	repo deploy-key add
o	-w|--allow-write	Allow write access for the key	
o	-t|--title	Title of the new key	v
a	1	0
#	repo deploy-key add	1
t	filepaths
@	repo deploy-key delete
a	1	0
@	repo deploy-key list
@	repo delete
o	-y|--confirm	Skip the confirmation prompt	
a	1	0
#	repo delete	1
d
@	repo edit
o	--clone	Clone the fork {true|false}	
o	--add-topic	Add repository topic	v
o	--allow-forking	Allow forking of an organization repository	
o	--default-branch	Set the default branch name for the repository	v
o	--delete-branch-on-merge	Delete head branch when pull requests are merged	
o	-d|--description	Description of the repository	v
o	--enable-auto-merge	Enable auto-merge functionality	
o	--enable-issues	Enable issues in the repository	
o	--enable-merge-commit	Enable merging pull requests via merge commit	
o	--enable-projects	Enable projects in the repository	
o	--enable-rebase-merge	Enable merging pull requests via rebase	
o	--enable-squash-merge	Enable merging pull requests via squashed commit	
o	--enable-wiki	Enable wiki in the repository	
o	-h|--homepage	Repository home page URL	v
o	--remove-topic	Remove repository topic	v
o	--template	Make the repository available as a template repository	
o	--visibility	Change the visibility of the repository to {public,private,internal}	v
a	1	0
=	repo edit	--visibility
v	public	
v	private	
v	internal	
#	repo edit	1
d
@	repo fork
o	--	Flags to pass to git when cloning	v
o	--clone	Clone the fork	
o	--remote	Add remote for fork {true|false}	
o	--remote-name	Specify a name for a fork's new remote. (default "origin")	v
o	--org	Create the fork in an organization	v
o	--fork-name	Rename the forked repository	v
a	1	0
#	repo fork	1
d
@	repo list
o	--visibility	Filter repositories by visibility	v
o	--archived	Show only archived repositories	
o	--fork	Show only forked repositories	
o	-l|--language	Filter by primary coding language	
o	-L|--limit	Maximum number of repositories to list (default 30)	v
o	--no-archived	Omit archived repositories	
o	--source	Show only non-forks	
o	-q|--jq	Filter JSON output using a jq expression	
o	--json	Output JSON with the specified fields	
o	-t|--template	Format JSON output using a Go template	
o	--topic	Filter by topic	v
o	--private	Show only private repositories	
o	--public	Show only public repositories	
a	1	0
=	repo list	--visibility
v	public	
v	private	
v	internal	
@	repo rename
o	-y|--confirm	Skip the confirmation prompt	
o	--repo|-R	Select another repository	v
o	-R|--repo	Select another repository using the `[HOST/]OWNER/REPO` format	v
a	1	0
@	repo set-default
o	-u|--unset	Unset the current default repository	
o	-v|--view	View the current default repository	
a	1	0
#	repo set-default	1
d
@	repo sync
o	-b|--branch	Branch to sync	v
o	--force	Hard reset the branch of the destination repository to match the source repository	
o	-s|--source	Source repository	v
a	1	0
@	repo view
o	-b|--branch	View a specific branch of the repository	v
o	-w|--web	Open a repository in the browser	
o	-q|--jq	Filter JSON output using a jq expression	v
o	--json	Output JSON with the specified fields	v
o	-t|--template	Format JSON output using a Go template	v
a	1	0
#	repo view	1
d
@	run
s	download	Download artifacts generated by a workflow run
s	list	List recent workflow runs
s	rerun	Rerun a failed run
s	view	View a summary of a workflow run
s	watch	Watch a run until it completes, showing its progress
o	--repo|-R	Select another repository	v
@	run download
a	1	0
@	run list
o	--repo|-R	Select another repository	v
o	-L|--limit	Maximum number of runs to fetch (default 20)	v
o	-w|--workflow	Filter runs by workflow	v
@	run rerun
o	--repo|-R	Select another repository	v
a	1	0
@	run view
o	--repo|-R	Select another repository	v
o	--exit-status	Exit with non-zero status if run failed	
o	-j|--job	View a specific job ID from a run	v
o	--log	View full log for either a run or specific job	
o	--log-failed	View the log for any failed steps in a run or specific job	
o	-v|--verbose	Show job steps	
o	-w|--web	Open run in the browser	
a	1	0
@	run watch
o	--repo|-R	Select another repository	v
o	--exit-status	Exit with non-zero status if run fails	
o	-i|--interval	Refresh interval in seconds (default 3)	v
@	secret
s	list	List secrets for a repository, environment, or organization
s	remove	Remove secrets
s	set	Create or update secrets
o	--repo|-R	Select another repository	v
@	secret list
o	--repo|-R	Select another repository	v
o	-e|--env	List secrets for an environment	v
o	-o|--org	List secrets for an environment	v
@	secret remove
o	--repo|-R	Select another repository	v
o	-e|--env	List secrets for an environment	v
o	-o|--org	List secrets for an environment	v
@	secret set
o	--repo|-R	Select another repository	v
o	-e|--env	List secrets for an environment	v
o	-o|--org	List secrets for an environment	v
o	-b|--body	A value for the secret. Reads from STDIN if not specified	v
o	-v|--visibility	Set visibility for an organization secret: all, `private`, or `selected` (default 'private')	v
=	secret set	-v
v	private	
v	selected	
v	all	
@	ssh-key
s	add	Add an SSH key to your GitHub account
s	list	Lists SSH keys in your GitHub account
@	ssh-key add
o	--repo|-R	Select another repository	v
o	-t|--title	Title for the new key	
a	1	0
#	ssh-key add	1
t	filepaths
@	ssh-key list
o	--repo|-R	Select another repository	v
@	workflow
s	disable	Disable a workflow
s	enable	Enable a workflow
s	list	List workflows
s	run	Run a workflow by creating a workflow_dispatch event
s	view	View the summary of a workflow
o	--repo|-R	Select another repository	v
@	workflow disable
o	--repo|-R	Select another repository	v
a	1	0
@	workflow enable
o	--repo|-R	Select another repository	v
a	1	0
@	workflow list
o	--repo|-R	Select another repository	v
o	-a|--all	Show all workflows, including disabled workflows	
o	-L|--limit	Show all workflows, including disabled workflows	v
a	1	0
@	workflow run
o	--repo|-R	Select another repository	v
o	-F|--field	Add a string parameter in key=value format, respecting @ syntax	v
o	--json	Read workflow inputs as JSON via STDIN	
o	-f|--raw-field	Add a string parameter in key=value format	v
o	-r|--ref	The branch or tag name which contains the version of the workflow file you'd like to run	v
a	1	0
@	workflow view
o	--repo|-R	Select another repository	v
o	-r|--ref	The branch or tag name which contains the version of the workflow file you'd like to view	v
o	-w|--web	Open workflow in the browser	
o	-y|--yaml	View the workflow yaml file	
a	3	0
#	workflow view	3
t	filepaths
@	codespace
s	code	Open a codespace in Visual Studio Code
s	cp	The cp command copies files between the local and remote file systems
s	create	Create a codespace
s	delete	Delete codespaces based on selection criteria. All codespaces for the authenticated user can be…
s	edit	Edit a codespace
s	jupyter	Open a codespace in JupyterLab
s	list	List codespaces of the authenticated user. Alternatively, organization administrators may list all…
s	logs	Access codespace logs
s	ports	List ports in a codespace
s	rebuild	Rebuild a codespace
s	ssh	SSH into a codespace
s	stop	Stop running a codespace
@	codespace code
o	-c|--codespace	Name of the codespace	v
o	--insiders	Use the insiders version of Visual Studio Code	
o	-w|--web	Use the web version of Visual Studio Code	
@	codespace cp
o	-c|--codespace	Name of the codespace	v
o	-e|--expand	Expand remote file names on remote shell	
o	-p|--profile	Name of the SSH profile to use	v
o	-r|--recursive	Recursively copy directories	
a	2	0
@	codespace create
o	-b|--branch	Repository branch	
o	--default-permissions	Do not prompt to accept additional permissions requested by the codespace	
o	--devcontainer-path	Path to the devcontainer.json file to use when creating codespace	v
o	-d|--display-name	Display name for the codespace	v
o	--idle-timeout	Allowed inactivity before codespace is stopped	v
o	-l|--location	Determined automatically if not provided	v
o	-m|--machine	Hardware specifications for the VM	v
o	-R|--repo	Repository name with owner: user/repo	v
o	--retention-period	Allowed time after shutting down before the codespace is automatically deleted (maximum 30 days)	v
o	-s|--status	Show status of post-create command and dotfiles	
=	codespace create	--devcontainer-path
d
=	codespace create	-l
v	EastUs	
v	SouthEastAsia	
v	WestEurope	
v	WestUs2	
@	codespace delete
o	-c|--codespace	Name of the codespace	v
o	--all	Delete all codespaces	
o	--days	Delete codespaces older than N days	v
o	-f|--force	Skip confirmation for codespaces that contain unsaved changes	
o	-o|--org	The login handle of the organization (admin-only)	v
o	-r|--repo	Delete codespaces for a repository	v
o	-u|--user	The username to delete codespaces for	v
@	codespace edit
o	-c|--codespace	Name of the codespace	v
o	-d|--display-name	Set the display name	v
o	-m|--machine	Set hardware specifications for the VM	v
@	codespace jupyter
o	-c|--codespace	Name of the codespace	v
@	codespace list
o	-q|--jq	Filter JSON output using a jq expression	v
o	--json	Output JSON with the specified fields	v
o	-L|--limit	Maximum number of codespaces to list	v
o	-o|--org	The login handle of the organization to list codespaces for (admin-only)	v
o	-R|--repo	Repository name with owner: user/repo	v
o	-t|--template	Format JSON output using a Go template; see 'gh help formatting'	v
o	-u|--user	The username to list codespaces for	v
@	codespace logs
o	-c|--codespace	Name of the codespace	v
o	-f|--follow	Tail and follow the logs	
@	codespace ports
s	forward	Forward ports
s	visibility	Change the visibility of the forwarded port
o	-c|--codespace	Name of the codespace	v
o	-q|--jq	Filter JSON output using a jq expression	v
o	--json	Output JSON with the specified fields	v
o	-t|--template	Format JSON output using a Go template; see 'gh help formatting'	v
@	codespace ports forward
o	-c|--codespace	Name of the codespace	v
a	1	1
#	codespace ports forward	1
d
@	codespace ports visibility
o	-c|--codespace	Name of the codespace	v
a	1	1
#	codespace ports visibility	1
d
@	codespace rebuild
o	-c|--codespace	Name of the codespace	v
@	codespace ssh
o	-c|--codespace	Name of the codespace	v
o	--config	Write OpenSSH configuration to stdout	
o	-d|--debug	Log debug data to a file	
o	--debug-file	Path of the file log to	v
o	--profile	Name of the SSH profile to use	v
o	--server-port	SSH server port number (0 => pick unused)	v
a	1	0
=	codespace ssh	--debug-file
t	filepaths
@	codespace stop
o	-c|--codespace	Name of the codespace	v
o	-o|--org	The login handle of the organization (admin-only)	v
o	-u|--user	The username to delete codespaces for	v
@	project
s	create	Create a project
s	edit	Edit a project
s	list	List projects
s	delete	Delete a project
s	close	Close a project
s	view	View a project
s	copy	Copy a project
s	field-create	Create a project field
s	field-delete	Delete a project field
s	field-list	List project fields
s	item-create	Create a draft issue item in a project
s	item-edit	Edit a project item
s	item-delete	Delete a project item
s	item-list	List project items
s	item-add	Add a pull request or an issue to a project
s	item-archive	Archive a project item
@	project create
o	--title	Title for the project	v
o	--owner	Login of the owner. Use "@me" for the current user	v
o	--format	Output format: {json}	v
@	project edit
o	--title	New title of the project	v
o	-d|--description	New description of the project	v
o	--owner	Login of the owner. Use "@me" for the current user	v
o	--readme	New readme for the project	v
o	--visibility	Change project visibility	v
=	project edit	--visibility
v	PUBLIC	
v	PRIVATE	
@	project list
o	--closed	Include closed projects	v
o	--owner	Login of the owner	v
o	-L|--limit	Maximum number of projects to fetch	v
o	--format	Output format: {json}	v
o	--web	Open projects list in the browser	
@	project delete
o	--owner	Login of the owner. Use @me for the current user	v
o	--format	Output format: {json}	v
@	project close
o	--owner	Login of the owner. Use @me for the current user	v
o	--format	Output format: {json}	v
o	--undo	Reopen a closed project	
@	project view
o	--owner	Login of the owner. Use @me for the current user	v
o	--format	Output format: {json}	v
o	-w|--web	Open project in the browser	
@	project copy
o	--title	Title for the new project	v
o	--target-owner	Login of the target owner. Use @me for the current user	v
o	--source-owner	Login of the source owner. Use @me for the current user	v
o	--format	Output format: {json}	v
o	--drafts	Include draft issues when copying	
@	project field-create
o	--name	Name of the field	v
o	--data-type	DataType of the new field	v
o	--owner	Login of the owner. Use @me for the current user	v
o	--format	Output format: {json}	v
o	--single-select-options	Options for SINGLE_SELECT data type	v
=	project field-create	--data-type
v	TEXT	
v	SINGLE_SELECT	
v	DATE	
v	NUMBER	
@	project field-delete
o	--id	ID of the field to delete	v
o	--format	Output format: {json}	
@	project field-list
o	--owner	Login of the owner. Use @me for the current user	v
o	--format	Output format: {json}	
o	-L|--limit	Maximum number of fields to fetch	v
@	project item-create
o	--title	Title for the draft issue	v
o	--body	Body for the draft issue	v
o	--format	Output format: {json}	v
o	--owner	Login of the owner. Use @me for the current user	v
@	project item-edit
o	--id	ID of the item to edit	v
o	--project-id	ID of the project to which the field belongs to	v
o	--title	Title of the draft issue item	v
o	--body	Body of the draft issue item	v
o	--format	Output format: {json}	v
o	--field-id	ID of the field to update	v
o	--iteration-id	ID of the iteration value to set on the field	v
o	--text	Text value for the field	v
o	--number	Number value for the field	v
o	--single-select-option-id	ID of the single select option value to set on the field	v
o	--date	Date value for the field (YYYY-MM-DD)	v
@	project item-delete
o	--id	ID of the item to delete	v
o	--format	Output format: {json}	v
o	--owner	Login of the owner. Use @me for the current user	v
@	project item-list
o	--format	Output format: {json}	v
o	-L|--limit	Maximum number of items to fetch	v
o	--owner	Login of the owner. Use @me for the current user	v
@	project item-add
o	--url	URL of the issue or pull request to add to the project	v
o	--owner	Login of the owner. Use @me for the current user	v
o	--format	Output format: {json}	v
@	project item-archive
o	--id	ID of the item to archive	v
o	--format	Output format: {json}	v
o	--owner	Login of the owner. Use @me for the current user	v
o	--undo	Unarchive a project item	
