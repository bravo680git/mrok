@	
s	aliases	Edit your command aliases
s	auth	Add your auth token to enable Graphite CLI to create and update your PRs on GitHub
s	bottom|b	Switch to the first branch from trunk in the current stack
s	changelog	Show the Graphite CLI changelog
s	checkout|co	Switch to a branch. If no branch is provided, opens an interactive selector
s	children	Show the children of the current branch
s	completion	Set up bash or zsh tab completion
s	config	Configure the Graphite CLI
s	continue|cont	Continues the most recent Graphite command halted by a merge conflict
s	create|c	Create a new branch stacked on top of the current branch and commit staged changes. If no branch…
s	dash	Open the web dashboard
s	delete|dl	Delete a branch and its corresponding Graphite metadata
s	docs	Show the Graphite CLI docs
s	down|d	Switch to the parent of the current branch
s	feedback	Commands for providing feedback and debug state
s	fish	Set up 'fish' tab completion
s	fold|f	Fold a branch's changes into its parent, update dependencies of descendants of the new combined…
s	get	Get branches from trunk to the specified branch from remote, prompting the user to resolve…
s	info|i	Display information about the current branch
s	init	Initialize Graphite in this repository by selecting a trunk branch. Can also be used to change the…
s	log|l	Commands that log your stacks
s	merge	Merge the pull requests associated with all branches from trunk to the current branch via Graphite
s	modify|m	Modify the current branch by amending its commit or creating a new commit. Automatically restacks…
s	move	Rebase the current branch onto the target branch and restack all of its descendants. If no branch…
s	parent	Show the parent of the current branch
s	pop	Delete the current branch but reaint the state of files in the working tree
s	pr	Opens the pull request page for a branch or PR number. If no branch is passed, the current…
s	rename|rn	Rename a branch and update metadata referencing it. If no branch name is supplied, you will be…
s	reorder	Reorder branches between trunk and the current branch, restacking all of their descendants. Opens…
s	restack|r	Ensure the current branch is based on its parent, rebasing if necessary. If conflicts are…
s	revert	Create a branch that reverts a commit on the trunk branch. Currently experimental
s	split|sp	Split the current branch into multiple single-commit branches
s	squash|sq	Squash all commits in the current branch and restack upstack branches
s	submit|s	Idempotently force push the current branch to GitHub, creating or updating a pull request. Opens…
s	sync	Pull the trunk branch from remote and prompt to delete any branches that have been merged…
s	top|t	Switch to the tip branch of the current stack. Prompts if ambiguous
s	track|tr	Start tracking the current (or provided) branch with Graphite by selecting its parent. This…
s	trunk	Switch to the trunk branch
s	untrack|utr	Stop tracking a branch with Graphite. If the branch has children, they will also be untracked…
s	up|u	Switch to the child of the current branch. Prompts if ambiguous
o	--version	Show Graphite CLI version	p
o	--help|-h	Show help for Graphite CLI	p
o	--interactive	Prompt the user. Disable with --no-interactive	p
o	--no-interactive	Run non interactive	p
o	--quiet|-q	Minimize output to the terminal. Implies --no-interactive	p
o	--verify	Run git hooks. Disable with --no-verify	p
o	--no-verify	Disable git hooks	p
o	--debug	Display debug output	p
o	--cwd	Working directory in which to perform operations	p
@	aliases
o	--reset	Reset your alias configuration	
@	auth
o	--token|-t	Auth token. Get it from: https://app.graphite.dev/activate	v
@	bottom
@	changelog
@	checkout
o	--show-untracked|-u	Include untracked branched in interactive selection	
a	1	0
@	children
@	completion
@	config
@	continue
o	--all|-a	Stage all changes before continuing	
@	create
o	--message|-m	Commit staged changes on the new branch with this message	v
o	--all|-a	Stage all unstaged changes on the new branch with this message	
o	--patch|-p	Pick hunks to stage before committing	
o	--insert|-i	When true, any existing children of the current branch will become children of the new branch	
a	1	0
@	dash
@	delete
o	--force|-f	Delete the branch even if it is not merged or closed	
a	1	0
@	docs
@	down
o	--steps|-n	The number of levels to traverse downstack	v
a	1	0
@	feedback
o	--print-debug-context	Print a debug summary of your repository. Useful for creating bug report details	
o	--with-debug-context	Include a blob of json describing your repo's state to help with debugging. Run 'gt feedback…	
a	1	0
@	fish
@	fold
o	--keep|-k	Keeps the name of the current branch instead of using the name of its parent	
@	get
o	--force|-f	Overwrite all fetched branches with remote source of truth	
a	1	0
@	info
o	--patch|-p	Show the changes made by each commit	
o	--diff|-d	Show the diff between this branch and its parent. Takes precedence over patch	
o	--body|-b	Show the PR body, if it exists	
o	--stat|-s	Show a diffstat instead of a full diff. Modifies either --patch or --diff. If neither is passed…	
@	init
o	--reset	Untrack all branches	
o	--trunk	The name of your trunk branch. If no name is passed, you will be prompted to select one…	V
@	log
s	long	Display a graph of the commit ancestry of all branches
s	short	Log all stacks tracked by Graphite, arranged to show dependencies
o	--classic	Use the old short logging style, which runs out of screen real estate more quickly. Other options…	
o	--reverse|-r	Print the log upside down. Handy when you have a lot of branches	
o	--show-untracked|-u	Include untracked branched in interactive selection	
o	--stack|-s	Only show ancestors and descendants of the current branch	
o	--steps|-n	Only show this many levels upstack and downstack. Implies --stack	v
@	log long
@	log short
@	merge
o	--confirm|-c	Asks for confirmation before merging branches. Prompts for confirmation if the local branches…	
o	--dry-run	Reports the PRs that would be merged and terminates. No branches are merged	
@	modify
o	--all|-a	Stage all changes before committing	
o	--commit|-c	Create a new commit instead of amending the current commit. If this branch has no commits, this…	
o	--edit|-e	If passed, open an editor to edit the commit message. When creating a new commit, this flag is…	
o	--interactive-rebase	Ignore all other flags and start a git interactive rebase on the commits in this branch	
o	--message|-m	The message for the new or amended commit. If passed, no editor is opened	v
o	--patch|-p	Pick hunks to stage before committing	
@	move
o	--onto|-o	Branch to move the current branch onto	v
o	--source	Branch to move (defaults to current branch)	v
@	parent
@	pop
@	pr
a	1	0
@	rename
o	--force|-f	Allow renaming a branch that is already associated with an open GitHub pull request	
a	1	0
@	reorder
@	restack
o	--branch	Which branch to run this command from. Defaults to the current branch	v
o	--downstack	Only restack this branch and its ancestors	
o	--only	Only restack this branch	
o	--upstack	Only restack this branch and its descendants	
@	revert
o	--edit|-e	Edit the commit message	
a	1	0
@	split
o	--by-commit|--commit|-c	Split by commit - slice up the history of this branch	
o	--by-hunk|--hunk|-h	Split by hunk - split into new single-commit branches	
@	squash
o	--message|-m	The updated message for the commit	v
o	--edit	Modify the existing commit message	
o	--no-edit|-n	Don't modify the existing commit message. Takes precedence over --edit	
@	submit
o	--always	Always push updates, even if the branch has not changed. Can be helpful for fixing an inconsistent…	
o	--branch	Which branch to run this command from. Defaults to the current branch	v
o	--confirm|-c	Reports the PRs that would be submitted and asks for confirmation before pushing branches and…	
o	--draft|-d	If set, marks PR as draft. If --no-interactive is true, new PRs will be created in draft mode	
o	--dry-run	Reports the PRs that would be submitted and terminates. No branches are pushed and no PRs are…	
o	--edit|-e	Input metadata for all PRs interactively. If neither --edit nor --no-edit is passed, only prompts…	
o	--force|-f	Force push: overwrites the remote branch with your local branch. Otherwise defaults to…	
o	--merge-when-ready|-m	If set, marks all PRs being submitted as merge when ready, which will let them automatically merge…	
o	--no-edit|-n	Don't edit PR fields inline. Takes precedence over --edit	
o	--publish|-p	If set, publishes PR. If --no-interactive is true, new PRs will be created in draft mode	
o	--rerequest-review	Rerequest review from current reviewers	
o	--restack	Restack branches before submitting. If there are conflicts, output the branch names that could not…	
o	--reviewers|-r	If set without an argument, prompt to manually set reviewers. Alternatively, accepts a comma…	V
o	--stack|-s	Submit descendants of the current branch in addition to its ancestors	
o	--update-only|-u	Only update the PRs that have been already been submitted	
@	sync
o	--delete	Delete merged branches (true by default; skip with --no-delete)	
o	--force|-f	Don't prompt for confirmation before deleting a branch or overwriting trunk to match remote if it…	
o	--pull	Pull the trunk branch from remote (true by default; skip with --no-pull)	
o	--restack	Restack any branches that can be restacked without conflicts (true by default; skip with…	
o	--show-delete-progress	Show progress through merged branches	
@	top
@	track
o	--parent|-p	The tracked branch's parent. If unset, prompts for a parent branch	v
o	--force|-f	Sets the parent to the most recent tracked ancestor of the branch being tracked. Takes precedence…	
a	1	0
@	trunk
@	untrack
o	--force|-f	Will not prompt for confirmation before untracking a branch with children	
a	1	0
@	up
o	--steps|-n	The number of levels to traverse upstack	v
a	1	0
