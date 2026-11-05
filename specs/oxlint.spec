@	
o	-c|--config	Path to Oxlint JSON configuration file	v
o	--tsconfig	Path to tsconfig.json path for reading path aliases and project references for import plugin	v
o	--ignore-path	Specify the file to use as your .eslintignore	v
o	--ignore-pattern	Specify file patterns to ignore (in addition to those in .eslintignore)	v
o	--no-ignore	Disable exluding of files from .eslintignore files, --ignore-path, and --ignore-pattern	
o	--symlinks	Follow symlinks when linting, which are ignored by default	
o	--jsdoc-plugin	Enable the JSDoc plugin	
o	--jest-plugin	Enable the Jest plugin	
o	--vitest-plugin	Enable the Vitest plugin	
o	--nextjs-plugin	Enable the Next.js plugin	
o	--react-perf-plugin	Enable the React Performance plugin	
o	--promise-plugin	Enable the Promise plugin	
o	--disable-react-plugin	Disable the React plugin, which is turned on by default	
o	--disable-unicorn-plugin	Disable the Unicorn plugin, which is turned on by default	
o	--disable-oxc-plugin	Disable the Oxc plugin, which is turned on by default	
o	--disable-typescript-plugin	Disable the TypeScript plugin, which is turned on by default	
o	--disable-import-plugin	Disable the Import plugin, which is turned on by default	
o	-D|--deny	Deny a lint rule or category (enable a lint as an error)	v
o	-W|--warn	Warn about a lint rule or category (enable a lint as a warning)	v
o	-A|--allow	Allow a lint rule or category (suppress a lint)	v
o	--fix	Fix as many issues as possible. Only unfixed issues are reported in the output	
o	--silent	Do not display any diagnostics	
o	--deny-warnings	Exit with a non-zero code if there are any warnings	
o	--max-warnings	Exit with a non-zero code if there are more than `max` warnings	v
o	-f|--format	Use a specific output format	v
o	--threads	Number of threads to use. Set to 1 to use only 1 CPU core	v
o	--rules	List all available rules	
o	-h|--help	Show help	
o	-V|--version	Show version	
a	1	1
=		-c
t	filepaths,history
=		--tsconfig
g	ls	\n
t	filepaths,history
=		--ignore-path
v	.eslintignore	
t	filepaths
=		-D
d
=		-W
d
=		-A
d
=		-f
v	default	
v	json	
v	unix	
v	checkstyle	
v	github	GitHub Actions Annotations
#		1
t	filepaths,folders
