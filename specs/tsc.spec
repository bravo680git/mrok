@	
o	--all	Show all compiler options	
o	--generateTrace	Generates an event trace and a list of types	
o	--help	Gives local information for help on the CLI	
o	--init	Initializes a TypeScript project and creates a tsconfig.json file	
o	--listFilesOnly	Print names of files that are part of the compilation and then stop processing	
o	--locale	Set the language of the messaging from TypeScript. This does not affect emit	
o	--project	Compile the project given the path to its configuration file, or to a folder with a tsconfig.json	v
o	--showConfig	Print the final configuration instead of building	
o	--version	Print the compiler's version	
o	--build	Build one or more projects and their dependencies, if out of date	
o	--clean	Delete the outputs of all projects	
o	--dry	Show what would be built (or deleted, if specified with '--clean')	
o	--force	Build all projects, including those that appear to be up to date	
o	--verbose	Enable verbose logging	
o	--excludeDirectories	Remove a list of directories from the watch process	v
o	--excludeFiles	Remove a list of files from the watch mode's processing	v
o	--fallbackPolling	Specify what approach the watcher should use if the system runs out of native file watchers	v
o	--synchronousWatchDirectory	Synchronously call callbacks and update the state of directory watchers on platforms that don`t…	
o	--watch	Watch input files	
o	--watchDirectory	Specify how directories are watched on systems that lack recursive file-watching functionality	v
o	--watchFile	Specify how the TypeScript watch mode works	v
o	--allowJs	Allow JavaScript files to be a part of your program. Use the checkJS option to get errors from…	
o	--allowSyntheticDefaultImports	Allow 'import x from y' when a module doesn't have a default export	
o	--allowUmdGlobalAccess	Allow accessing UMD globals from modules	
o	--allowUnreachableCode	Disable error reporting for unreachable code	
o	--allowUnusedLabels	Disable error reporting for unused label	
o	--alwaysStrict	Ensure 'use strict' is always emitted	
o	--assumeChangesOnlyAffectDirectDependencies	Have recompiles in projects that use incremental and watch mode assume that changes within a file…	
o	--baseUrl	Specify the base directory to resolve non-relative module names	v
o	--checkJs	Enable error reporting in type-checked JavaScript files	
o	--composite	Enable constraints that allow a TypeScript project to be used with project references	
o	--declaration	Generate .d.ts files from TypeScript and JavaScript files in your project	
o	--declarationDir	Specify the output directory for generated declaration files	v
o	--declarationMap	Create sourcemaps for d.ts files	
o	--diagnostics	Output compiler performance information after building	
o	--disableReferencedProjectLoad	Reduce the number of projects loaded automatically by TypeScript	
o	--disableSizeLimit	Remove the 20mb cap on total source code size for JavaScript files in the TypeScript language server	
o	--disableSolutionSearching	Opt a project out of multi-project reference checking when editing	
o	--disableSourceOfProjectReferenceRedirect	Disable preferring source files instead of declaration files when referencing composite projects	
o	--downlevelIteration	Emit more compliant, but verbose and less performant JavaScript for iteration	
o	--emitBOM	Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files	
o	--emitDeclarationOnly	Only output d.ts files and not JavaScript files	
o	--emitDecoratorMetadata	Emit design-type metadata for decorated declarations in source files	
o	--esModuleInterop	Emit additional JavaScript to ease support for importing CommonJS modules. This enables…	
o	--exactOptionalPropertyTypes	Differentiate between undefined and not present when type checking	
o	--experimentalDecorators	Enable experimental support for TC39 stage 2 draft decorators	
o	--explainFiles	Print files read during the compilation including why it was included	
o	--extendedDiagnostics	Output more detailed compiler performance information after building	
o	--forceConsistentCasingInFileNames	Ensure that casing is correct in imports	
o	--generateCpuProfile	Emit a v8 CPU profile of the compiler run for debugging	
o	--importHelpers	Allow importing helper functions from tslib once per project, instead of including them per-file	
o	--importsNotUsedAsValues	Specify emit/checking behavior for imports that are only used for types	v
o	--incremental	Save .tsbuildinfo files to allow for incremental compilation of projects	
o	--inlineSourceMap	Include sourcemap files inside the emitted JavaScript	
o	--inlineSources	Include source code in the sourcemaps inside the emitted JavaScript	
o	--isolatedModules	Ensure that each file can be safely transpiled without relying on other imports	
o	--jsx	Specify what JSX code is generated	v
o	--jsxFactory	Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or…	v
o	--jsxFragmentFactory	Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g…	v
o	--jsxImportSource	Specify module specifier used to import the JSX factory functions when using jsx: react-jsx*	v
o	--keyofStringsOnly	Make keyof only return strings instead of string, numbers or symbols. Legacy option	
o	--lib	Specify a set of bundled library declaration files that describe the target runtime environment	v
o	--listEmittedFiles	Print the names of emitted files after a compilation	
o	--listFiles	Print all of the files read during the compilation	
o	--mapRoot	Specify the location where debugger should locate map files instead of generated locations	v
o	--maxNodeModuleJsDepth	Specify the maximum folder depth used for checking JavaScript files from node_modules. Only…	v
o	--module	Specify what module code is generated	v
o	--moduleResolution	Specify how TypeScript looks up a file from a given module specifier	v
o	--newLine	Set the newline character for emitting files	v
o	--noEmit	Disable emitting file from a compilation	
o	--noEmitHelpers	Disable generating custom helper functions like __extends in compiled output	
o	--noEmitOnError	Disable emitting files if any type checking errors are reported	
o	--noErrorTruncation	Disable truncating types in error messages	
o	--noFallthroughCasesInSwitch	Enable error reporting for fallthrough cases in switch statements	
o	--noImplicitAny	Enable error reporting for expressions and declarations with an implied any type	
o	--noImplicitOverride	Ensure overriding members in derived classes are marked with an override modifier	
o	--noImplicitReturns	Enable error reporting for codepaths that do not explicitly return in a function	
o	--noImplicitThis	Enable error reporting when this is given the type any	
o	--noImplicitUseStrict	Disable adding 'use strict' directives in emitted JavaScript files	
o	--noLib	Disable including any library files, including the default lib.d.ts	
o	--noPropertyAccessFromIndexSignature	Enforces using indexed accessors for keys declared using an indexed type	
o	--noResolve	Disallow imports, requires or <reference>s from expanding the number of files TypeScript should…	
o	--noStrictGenericChecks	Disable strict checking of generic signatures in function types	
o	--noUncheckedIndexedAccess	Add undefined to a type when accessed using an index	
o	--noUnusedLocals	Enable error reporting when a local variables aren't read	
o	--noUnusedParameters	Raise an error when a function parameter isn't read	
o	--outDir	Specify an output folder for all emitted files	v
o	--outFile	Specify a file that bundles all outputs into one JavaScript file. If declaration is true, also…	v
o	--paths	Specify a set of entries that re-map imports to additional lookup locations	v
o	--plugins	Specify a list of language service plugins to include	v
o	--preserveConstEnums	Disable erasing const enum declarations in generated code	
o	--preserveSymlinks	Disable resolving symlinks to their realpath. This correlates to the same flag in node	
o	--preserveWatchOutput	Disable wiping the console in watch mode	
o	--pretty	Enable color and formatting in output to make compiler errors easier to read	
o	--reactNamespace	Specify the object invoked for createElement. This only applies when targeting react JSX emit	v
o	--removeComments	Disable emitting comments	
o	--resolveJsonModule	Enable importing .json files	
o	--rootDir	Specify the root folder within your source files	v
o	--rootDirs	Allow multiple folders to be treated as one when resolving modules	v
o	--skipDefaultLibCheck	Skip type checking .d.ts files that are included with TypeScript	
o	--skipLibCheck	Skip type checking all .d.ts files	
o	--sourceMap	Create source map files for emitted JavaScript files	
o	--sourceRoot	Specify the root path for debuggers to find the reference source code	v
o	--strict	Enable all strict type checking options	
o	--strictBindCallApply	Check that the arguments for bind, call, and apply methods match the original function	
o	--strictFunctionTypes	When assigning functions, check to ensure parameters and the return values are subtype-compatible	
o	--strictNullChecks	When type checking, take into account null and undefined	
o	--strictPropertyInitialization	Check for class properties that are declared but not set in the constructor	
o	--stripInternal	Disable emitting declarations that have @internal in their JSDoc comments	
o	--suppressExcessPropertyErrors	Disable reporting of excess property errors during the creation of object literals	
o	--suppressImplicitAnyIndexErrors	Suppress noImplicitAny errors when indexing objects that lack index signatures	
o	--target	Set the JavaScript language version for emitted JavaScript and include compatible library…	v
o	--traceResolution	Log paths used during the moduleResolution process	
o	--tsBuildInfoFile	Specify the folder for .tsbuildinfo incremental compilation files	v
o	--typeRoots	Specify multiple folders that act like ./node_modules/@types	v
o	--types	Specify type package names to be included without being referenced in a source file	v
o	--useDefineForClassFields	Emit ECMAScript-standard-compliant class fields	
o	--useUnknownInCatchVariables	Default catch clause variables as unknown instead of any	
a	1	0
=		--project
t	filepaths,folders
=		--excludeDirectories
t	folders
=		--excludeFiles
t	filepaths
=		--fallbackPolling
v	fixedPollingInterval	
v	priorityPollingInterval	
v	dynamicPriorityPolling	
=		--watchDirectory
v	fixedPollingInterval	
v	dynamicPriorityPolling	
v	useFsEvents	
=		--watchFile
v	fixedPollingInterval	
v	priorityPollingInterval	
v	dynamicPriorityPolling	
v	useFsEvents	
v	useFsEventsOnParentDirectory	
=		--baseUrl
t	filepaths
=		--declarationDir
t	folders
=		--importsNotUsedAsValues
v	remove	
v	preserve	
v	error	
=		--jsx
v	react	
v	react-jsx	
v	react-jsxdev	
v	react-native	
v	preserve	
=		--lib
t	filepaths
=		--mapRoot
t	folders
=		--module
v	ES6	
v	ES2015	
v	ES2020	
v	None	
v	UMD	
v	AMD	
v	System	
v	ESNext	
v	CommonJS	
=		--outDir
t	folders
=		--outFile
t	filepaths
=		--rootDir
t	folders
=		--rootDirs
t	folders
=		--sourceRoot
t	filepaths,folders
=		--target
v	ES3	
v	ES5	
v	ES6	
v	ES2015	
v	ES7	
v	ES2016	
v	ES2017	
v	ES2018	
v	ES2019	
v	ES2020	
v	ESNext	
=		--tsBuildInfoFile
t	folders
=		--typeRoots
t	folders
#		1
d
