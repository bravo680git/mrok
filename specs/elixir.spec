@	
o	-e|--eval	Evaluates the given command	v
o	-h|--help	Prints this message and exits	
o	-r	Requires the given files/patterns	v
o	-S	Finds and executes the given script in $PATH	v
o	-pr	Requires the given files/patterns in parallel	v
o	-pa	Prepends the given path to Erlang code path	v
o	-pz	Appends the given path to Erlang code path	v
o	-v|--version	Prints Elixir version and exits	
o	--app	Starts the given app and its dependencies	v
o	--erl	Switches to be passed down to Erlang	v
o	--logger-otp-reports	Enables or disables OTP reporting	v
o	--logger-sasl-reports	Enables or disables SASL reporting	v
o	--no-halt	Does not halt the Erlang VM after execution	
o	--werl	Uses Erlang's Windows shell GUI (Windows only)	
o	--cookie	Sets a cookie for this distributed node	v
o	--hidden	Makes a hidden node	
o	--name	Makes and assigns a name to the distributed node	v
o	--rpc-eval	Evaluates the given command on the given remote node	v
o	--sname	Makes and assigns a short name to the distributed node	v
o	--boot	Uses the given FILE.boot to start the system	v
o	--boot-var	Makes $VAR available as VALUE to FILE.boot	v
o	--erl-config	Loads configuration in FILE.config written in Erlang	v
o	--pipe-to	Starts the Erlang VM as a named PIPEDIR and LOGDIR	v
o	--vm-args	Passes the contents in file as arguments to the VM	v
a	2	0
=		-r
t	filepaths
=		-pr
t	filepaths
=		-pa
t	filepaths
=		-pz
t	filepaths
=		--boot
t	filepaths
=		--vm-args
t	filepaths
#		1
d
