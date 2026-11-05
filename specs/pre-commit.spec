@	
s	autoupdate	Auto-update pre-commit config to the latest repos' versions
s	clean	Clean out pre-commit files
s	gc	Clean unused cached repos
s	init-templatedir	Install hook script in a directory intended for use with `git config init.templateDir`
s	install	Install the pre-commit script
s	migrate-config	Migrate list configuration to new map configuration
s	run	Run hooks
s	sample-config	Produce a sample .pre-commit-config.yaml file
s	try-repo	Try the hooks in a repository, useful for developing new hooks
s	uninstall	Uninstall the pre-commit script
s	help	Show help for a specific command
o	-h|--help	Show help message and exit	
o	-V|--version	Show program's version number and exit	
a	1	0
@	autoupdate
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
o	--bleeding-edge	Update to the bleeding edge of `master` instead of the latest tagged version (the default behavior)	
o	--freeze	Store 'frozen' hashes in `rev` instead of tag names	
o	--repo	Only update this repository -- may be specified multiple times	v
=	autoupdate	--color
v	auto	
v	always	
v	never	
=	autoupdate	--config
t	filepaths
@	clean
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
=	clean	--color
v	auto	
v	always	
v	never	
=	clean	--config
t	filepaths
@	gc
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
=	gc	--color
v	auto	
v	always	
v	never	
=	gc	--config
t	filepaths
@	init-templatedir
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
o	-t|--hook-type	Type of hook to install	v
o	--no-allow-missing-config	Assume cloned repos should have a `pre-commit` config	
=	init-templatedir	--color
v	auto	
v	always	
v	never	
=	init-templatedir	--config
t	filepaths
=	init-templatedir	-t
v	pre-commit	
v	pre-merge-commit	
v	pre-push	
v	prepare-commit-msg	
v	commit-msg	
v	post-commit	
v	post-checkout	
v	post-merge	
v	post-rewrite	
@	install
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
o	-f|--overwrite	Overwrite existing hooks / remove migration mode	
o	install-hooks	Whether to install hook environments for all environments in the config file	
o	-t|--hook-type	Type of hook to install	v
o	--allow-missing-config	Whether to allow a missing `pre-commit` configuration file or exit with a failure code	
=	install	--color
v	auto	
v	always	
v	never	
=	install	--config
t	filepaths
=	install	-t
v	pre-commit	
v	pre-merge-commit	
v	pre-push	
v	prepare-commit-msg	
v	commit-msg	
v	post-commit	
v	post-checkout	
v	post-merge	
v	post-rewrite	
@	migrate-config
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
=	migrate-config	--color
v	auto	
v	always	
v	never	
=	migrate-config	--config
t	filepaths
@	run
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
o	--verbose|-v		
o	--all-files|-a	Run all files in the repo	
o	--files	Specific filenames to run hooks on	v
o	--show-diff-on-failure	When hooks fail, run `git diff` directly afterward	
o	--hook-stage	The stage during which the hook is fired	v
o	--remote-branch	Remote branch ref used by `git push`	v
o	--local-branch	Local branch ref used by `git push`	v
o	--from-ref|--source|-s	Represents the original ref in a `from_ref...to_ref` diff expression. For `pre-push` hooks, this…	v
o	--to-ref|--origin|-o	Represents the destination ref in a `from_ref...to_ref` diff expression. For `pre-push` hooks…	v
o	--commit-msg-filename	Filename to check when running during `commit-msg`	v
o	--remote-name	Remote name used by `git push`	v
o	--remote-url	Remote URL used by `git push`	v
o	--checkout-type	Indicates whether the checkout was a branch checkout (changing branches, flag=1) or a file…	v
o	--is-squash-merge	During a post-merge hook, indicates whether the merge was a squash merge	v
o	--rewrite-command	During a post-rewrite hook, specifies the command that invoked the rewrite	v
a	1	0
=	run	--color
v	auto	
v	always	
v	never	
=	run	--config
t	filepaths
=	run	--files
t	filepaths,folders
=	run	--hook-stage
v	pre-commit	
v	pre-merge-commit	
v	pre-push	
v	prepare-commit-msg	
v	commit-msg	
v	post-commit	
v	post-checkout	
v	post-merge	
v	post-rewrite	
=	run	--remote-branch
d
=	run	--local-branch
d
=	run	--from-ref
d
=	run	--to-ref
d
=	run	--remote-name
d
#	run	1
d
@	sample-config
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
=	sample-config	--color
v	auto	
v	always	
v	never	
=	sample-config	--config
t	filepaths
@	try-repo
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
o	--verbose|-v		
o	--all-files|-a	Run all files in the repo	
o	--files	Specific filenames to run hooks on	v
o	--show-diff-on-failure	When hooks fail, run `git diff` directly afterward	
o	--hook-stage	The stage during which the hook is fired	v
o	--remote-branch	Remote branch ref used by `git push`	v
o	--local-branch	Local branch ref used by `git push`	v
o	--from-ref|--source|-s	Represents the original ref in a `from_ref...to_ref` diff expression. For `pre-push` hooks, this…	v
o	--to-ref|--origin|-o	Represents the destination ref in a `from_ref...to_ref` diff expression. For `pre-push` hooks…	v
o	--commit-msg-filename	Filename to check when running during `commit-msg`	v
o	--remote-name	Remote name used by `git push`	v
o	--remote-url	Remote URL used by `git push`	v
o	--checkout-type	Indicates whether the checkout was a branch checkout (changing branches, flag=1) or a file…	v
o	--is-squash-merge	During a post-merge hook, indicates whether the merge was a squash merge	v
o	--rewrite-command	During a post-rewrite hook, specifies the command that invoked the rewrite	v
o	--ref|--rev	Manually select a rev to run against, otherwise the `HEAD` revision will be used	v
a	2	0
=	try-repo	--color
v	auto	
v	always	
v	never	
=	try-repo	--config
t	filepaths
=	try-repo	--files
t	filepaths,folders
=	try-repo	--hook-stage
v	pre-commit	
v	pre-merge-commit	
v	pre-push	
v	prepare-commit-msg	
v	commit-msg	
v	post-commit	
v	post-checkout	
v	post-merge	
v	post-rewrite	
=	try-repo	--remote-branch
d
=	try-repo	--local-branch
d
=	try-repo	--from-ref
d
=	try-repo	--to-ref
d
=	try-repo	--remote-name
d
#	try-repo	2
d
@	uninstall
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
o	-t|--hook-type	Type of hook to install	v
=	uninstall	--color
v	auto	
v	always	
v	never	
=	uninstall	--config
t	filepaths
=	uninstall	-t
v	pre-commit	
v	pre-merge-commit	
v	pre-push	
v	prepare-commit-msg	
v	commit-msg	
v	post-commit	
v	post-checkout	
v	post-merge	
v	post-rewrite	
@	help
o	-h|--help	Show help message and exit	
o	--color	Whether to use color in output. Defaults to `auto`	v
o	--config|-c	Path to alternate config file	v
=	help	--color
v	auto	
v	always	
v	never	
=	help	--config
t	filepaths
