@	
s	develop	Start the Gatsby development server
s	build	Compile your application and make it ready for deployment
s	serve	Serve the production build of your site for testing
s	clean	Wipe out the cache (.cache folder) and public directories
s	info	Get helpful environment information
s	plugin	Run commands pertaining to gatsby plugins
s	repl	Gatsby will prompt you to type in commands and explore
o	-v|--version	View your current Gatsby CLI version	
@	develop
o	-H|--host	Set host. Defaults to localhost	v
o	-p|--port	Set port. Defaults to env.PORT or 8000	v
o	-o|--open	Open the site in your (default) browser for you	
o	-S|--https	Use HTTPS	
o	--inspect	Opens a port for debugging	
@	build
o	--prefix-paths	Build site with link paths prefixed (set pathPrefix in your config)	
o	--no-uglify	Build site without uglifying JS bundles (for debugging)	
o	--profile	Build site with react profiling	
o	--open-tracing-config-file	Use Tracer configuration file	
o	--graphql-tracing	Trace every graphql resolver, may have performance implications	
o	--no-color|--no-colors	Disables colored terminal output	
@	serve
o	-H|--host	Set host. Defaults to localhost	v
o	-p|--port	Set port. Defaults to env.PORT or 8000	v
o	-o|--open	Open the site in your (default) browser for you	
o	--prefix-paths	Serve site with link paths prefixed	
@	clean
@	info
o	-C|--clipboard	Copy environment information to your clipboard	
@	plugin
o	docs	Documentation about using and creating plugins	
@	repl
