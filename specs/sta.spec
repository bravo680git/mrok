@	
s	generate-templates	Generate ".ejs" templates needed for generate api
o	--version|-v	Output the current version	
o	--path|-p	Path/url to swagger scheme	v
o	--output|-o	Output path of typescript api file (default: "./")	v
o	--name|-n	Name of output typescript api file (default: "Api.ts")	v
o	--templates|-t	Path to folder containing templates	v
o	--default-as-success|-d	Use "default" response status code as success response too	
o	--responses|-r	Generate additional information about request responses	
o	--union-enums	Generate all "enum" types as union types (T1 | T2 | TN)	
o	--add-readonly	Generate readonly properties	
o	--route-types	Generate type definitions for API routes	
o	--no-client	Do not generate an API class	
o	--enum-names-as-values	Use values in 'x-enumNames' as enum values (not only as keys)	
o	--extract-request-params	Extract request params to data contract	
o	--extract-request-body	Extract request body type to data contract	
o	--extract-response-body	Extract response body type to data contract	
o	--extract-response-error	Extract response error type to data contract	
o	--modular	Generate separated files for http client, data contracts, and routes	
o	--js	Generate js api module with declaration file	
o	--module-name-index	Determines which path index should be used for routes separation	v
o	--module-name-first-tag	Splits routes based on the first tag	
o	--disableStrictSSL	Disabled strict SSL	
o	--disableProxy	Disabled proxy	
o	--axios	Generate axios http client	
o	--unwrap-response-data	Unwrap the data item from the response	
o	--disable-throw-on-error	Do not throw an error when response.ok is not true (default: false)	
o	--single-http-client	Ability to send HttpClient instance to Api constructor (default: false)	
o	--silent	Output only errors to console	p
o	--default-response	Default type for empty response schema	v
o	--type-prefix	Data contract name prefix	v
o	--type-suffix	Data contract name suffix	v
o	--clean-output	Clean output folder before generate api. WARNING: May cause data loss (default: false)	
o	--api-class-name	Name of the api class	v
o	--patch	Fix up small errors in the swagger source definition (default: false)	
o	--debug	Additional information about processes inside this tool (default: false)	
o	--another-array-type	Generate array types as Array<Type> (by default Type[]) (default: false)	
o	--sort-types	Sort fields and types (default: false)	
o	--extract-enums	Extract all enums from inline interface ype content to typescript enum construction (default: false)	
o	--help|-h	Show help for swagger-typescript-api	p
=		--path
t	filepaths
=		--output
t	folders
=		--templates
t	folders
@	generate-templates
o	--output|-o	Output path of generated templates	v
o	--modular|-m	Generate templates needed to separate files for http client, data contracts, and routes	
o	--http-client	Http client type	v
o	--clean-output|-c	Clean output folder before generate template	
o	--rewrite|-r	Rewrite content in existing templates	
=	generate-templates	--output
t	folders
=	generate-templates	--http-client
v	fetch	
v	axios	
