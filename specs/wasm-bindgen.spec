@	
o	--help|-h	Show help for wasm-bindgen	
o	--version|-v	Show version for wasm-bindgen	
o	--out-dir	Output directory	v
o	--out-name	Set a custom output filename (Without extension. Defaults to crate name)	v
o	--target	What type of output to generate	v
o	--no-modules-global	Name of global to assign generated bindings to	v
o	--browser	Hint that JS should only be compatible with a browser	
o	--typescript	Output a TypeScript definition file (on by default)	
o	--no-typescript	Don't emit a *.d.ts file	
o	--omit-imports	Don't emit imports in generated JavaScript	
o	--debug	Include otherwise-extraneous debug checks in output	
o	--no-demangle	Don't demangle Rust symbol names	
o	--keep-debug	Keep debug sections in wasm files	
o	--remove-name-section	Remove the debugging `name` section of the file	
o	--remove-producers-section	Remove the telemetry `producers` section	
o	--omit-default-module-path	Don't add WebAssembly fallback imports in generated JavaScript	
o	--encode-into	Whether or not to use TextEncoder#encodeInto()	v
o	--nodejs	Deprecated, use `--target nodejs`	
o	--web	Deprecated, use `--target web`	
o	--no-modules	Deprecated, use `--target no-modules`	
o	--weak-refs	Enable usage of the JS weak references proposal	
o	--reference-types	Enable usage of WebAssembly reference types	
a	1	0
=		--out-dir
t	folders
=		--out-name
t	filepaths
=		--target
v	web	Directly loadable in a web browser
v	bundler	Suitable for loading in bundlers like Webpack
v	nodejs	Loadable via require as a Node.js module
v	no-modules	Like web, but older and doesn't use ES modules
v	deno	Loadable using imports from Deno modules
=		--encode-into
v	test	
v	always	Always use TextEncoder#encodeInto()
v	never	Never use TextEncoder#encodeInto()
#		1
d
