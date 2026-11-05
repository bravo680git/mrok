@	
o	-A	Use concatenated aliases to modify classpath	
o	-X		V
o	-T	Invoke tool by name or via aliases ala -X	V
o	-M	Use concatenated aliases to modify classpath or supply main opts	V
o	-P	Prepare deps - download libs, cache classpath, but don't exec	
o	-J	Pass opt through in java_opts	
o	-Sdeps	Pass the deps data on the command line	v
o	-Spath	Compute classpath and echo to stdout only	
o	-Scp	Use specified classpath instead of cached or computed one	v
o	-Sdescribe	Print environment and command parsing information as data	
o	-Sforce	Ignore classpath cache and force recomputation	
o	-Spom	Generate (or update) pom.xml with deps and paths	
o	-Srepro	Ignore the ~/.clojure/deps.edn config file	
o	-Sthreads	Set the number of threads to use when downloading dependencies	
o	-Strace	Write a trace.edn file that traces deps expansion	
o	-Stree	Print dependency tree	
o	-Sverbose	Print all path locations	
o	-version|--version	Print the Clojure CLI version	
o	-i|--init	Load a file or resource	v
o	-e|--eval	Evaluate expressions in string; print non-nil values	v
o	--report	Report uncaught exceptions	v
o	-m|--main	Call the -main function from a namespace with args	v
o	-r|--repl	Run a REPL	
o	-h|-?|--help	Show help for clojure	
=		--report
v	file	
v	stderr	
v	none	
