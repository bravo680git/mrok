@	
s	init	Generates a basic .agripparc.json file, with some default values for options that agrippa accepts
s	generate|gen	This is the core of the CLI - this command generates a new React component, based on the name and…
a	1	0
@	init
@	generate
o	--props	Determines which prop declaration/validation solution to generate. Defaults to `ts` if…	v
o	--children	Whether the component is meant to have children or not. Defaults to `false`	v
o	--typescript|--ts	Option to generate Typescript components, defaults to `true` if the CLI manages to find a…	v
o	--import-react	Option to import React at the top of the component. Defaults to `true` if the CLI manages to find…	v
o	--export-type	Whether to export the component as a named export or a default export. Defaults to `named`	v
o	--declaration	Whether to declare the component as a `const` with an arrow function, or as a `function`…	v
o	--memo	Generates a component as a memo component. Defaults to `false`	v
o	--react-native	Generates a React Native component. Defaults to `true` if `react-native` is a dependency in the…	v
o	--styling	Which styling solution to generate. Defaults to `none`	v
o	--styling-module	Whether to generate a scoped `module` stylesheet. This option is only relevant for `css` or `scss`…	v
o	--base-dir	Path to a base directory which components should be generated inside of (directly or nested)…	V
o	--dest|--destination	Allows the user to generate the component at a path relative to `baseDir`. It's mostly used to…	V
o	--allow-outside-base	Overrides default Agrippa behaviour to allow components to be specified outside `baseDir`…	V
o	--flat	By default, Agrippa generates a dedicated directory for the generated component; this directory…	v
o	--separate-index	In the `separateIndex` generation scheme, Agrippa creates one file for the component's code, and…	v
o	--post-command|--postCommand	Allows a custom command to be run after having generated a component. This allows for some cool…	v
o	--overwrite	By default, Agrippa prevents the generation of a component over an existing components, to prevent…	v
o	--debug	The `debug` flag makes Agrippa print out additional debug information. It's quite useful when…	v
a	1	0
=	generate	--props
v	ts	Generate a TypeScript interface for props (this requires the typescript option to be true)
v	jsdoc	Generates JSDoc type hints for props (a @typedef and a @type)
v	prop-types	Generates prop-types for props
v	none	Generates no props
=	generate	--export-type
v	named	
v	default	
=	generate	--declaration
v	const	
v	function	
=	generate	--styling
v	none	Generates no style
v	css	Generates a `css` file
v	scss	Generates a `scss` file
v	jss	Generates a `useStyles` hook above the component with `react-jss`'s `createUseStyles`
v	mui	Generates a `useStyles` hook above the component with `material-ui`'s `makeStyles`. Note that this…
v	react-native	Generates a React Native `StyleSheet`
=	generate	--base-dir
t	folders
=	generate	--dest
t	folders
=	generate	--allow-outside-base
t	folders
