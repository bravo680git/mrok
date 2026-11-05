@	
o	--help|-h	Show help for ts-node	
o	-v|--version	Print version information of the ts-node module	
o	-e|--eval	Evaluate script	v
o	-p|--print	Evaluate script and print result	
o	-r|--require	Require module before executing	v
o	-i|--interactive	Always open interactive REPL	
o	--show-config	Print resolved Typescript config to the terminal	
o	--cwd-mode	Resolve Typescript config based on the current working directory	
o	-T|--transpile-only	Use the Typescript transpile module mode	
o	-H|--compiler-host	Use the Typescript compiler host API	
o	-I|--ignore	Ignore patterns from Typescript compilation	v
o	-P|--project	Specify TypeScript project location	v
o	-C|--compiler	Use a custom compiler	v
o	--transpiler	Use a custom transpiler	v
o	-D|--ignore-diagnostics	Specify Typescript diagnostic code to ignore	v
o	-O|--compiler-options	JSON object that will be merged with the compiler options	v
o	--cwd	Specify working directory	v
o	--files	Load files, include and exclude from Typescript config on startup	
o	--pretty	Use the pretty formatter for diagnostic errors	
o	--skip-project	Skip reading Typescript config	
o	--scope	Scope compilation to scope directory specified	
o	--scope-dir	Directory for scope parameter	v
o	--skip-ignore	Skip --ignore checks	
o	--prefer-ts-exts	Prefer Typescript files over JavaScript files when importing files	
o	--log-error	Pipe Typescript errors to stderr instead of throwing exceptions	
o	--no-experimental-repl-await	Disable the top-level await function in REPL	
a	1	0
=		-r
d
=		-P
t	filepaths
=		--cwd
t	folders
=		--scope-dir
t	folders
#		1
d
