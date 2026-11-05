@	
s	run	Runs the specified target
s	test	Builds and runs the specified test targets
s	build	Builds the specified targets
o	--autodetect_server_javabase	Back to the local JDK for running the bazel server and instead exits	
o	--noautodetect_server_javabase	Does not fall back to the local JDK for running the bazel server and instead exits	
o	--batch	Run as just a client process without a server	
o	--nobatch	Run with a server	
o	--batch_cpu_scheduling	Only on Linux; use 'batch' CPU scheduling for Bazel	
o	--nobatch_cpu_scheduling	Only on Linux; Bazel does not perform a system call	
o	--bazelrc	The location of the user .bazelrc file containing default values of Bazel options	v
o	--block_for_lock	Wait for a running command to complete	
o	--noblock_for_lock	Bazel does not wait for a running command to complete, but instead exits immediately	
o	--client_debug	Log debug information from the client to stderr. Changing this option will not cause the server to…	
o	--noclient_debug	Don't log debug information from the client to stderr	
o	--connect_timeout_secs	The amount of time the client waits for each attempt to connect to the server	v
o	--expand_configs_in_place	Changed the expansion of --config flags to be done in-place	
o	--noexpand_configs_in_place	--config flags in a fixed point expansion between normal rc options and command-line specified…	
o	--failure_detail_out	Specifies a location to write a failure_detail protobuf message if the server experiences a…	v
o	--home_rc	Look for the home bazelrc file at $HOME/.bazelrc	
o	--nohome_rc	Don't look for the home bazelrc file at $HOME/.bazelrc	
o	--idle_server_tasks	Run System.gc() when the server is idle	
o	--noidle_server_tasks	Don't run System.gc() when the server is idle	
o	--ignore_all_rc_files	Disables all rc files, regardless of the values of other rc-modifying flags, even if these flags…	
o	--noignore_all_rc_files	Enables all rc files	
o	--io_nice_level	Only on Linux; set a level from 0-7 for best-effort IO scheduling using the sys_ioprio_set system…	v
o	--local_startup_timeout_secs	The maximum amount of time the client waits to connect to the server	v
o	--macos_qos_class	Sets the QoS service class of the bazel server when running on macOS	v
o	--max_idle_secs	The number of seconds the build server will wait idling before shutting down	v
o	--output_base	Specifies the output location to which all build output will be written	v
o	--output_base_root	The user-specific directory beneath which all build outputs are written	v
o	--preemptible	If true, the command can be preempted if another command is started	
o	--nopreemptible	If true, the command can be preempted if another command is started	
o	--server_jvm_out	The location to write the server's JVM's output	v
o	--shutdown_on_low_sys_mem	Linux only. If max_idle_secs is set and the build server has been idle for a while, shut down the…	
o	--noshutdown_on_low_sys_mem	Linux only. Don't shut down the server when the system is low on free RAM	
o	--system_rc	Look for the system-wide bazelrc	
o	--nosystem_rc	Don't look for the system-wide bazelrc	
o	--unlimit_coredumps	Raises the soft coredump limit to the hard limit to make coredumps of the server (including the…	
o	--nounlimit_coredumps	Don't raise the soft coredump limit to the hard limit to make coredumps of the server (including…	
o	--watchfs	Use the operating system's file watch service for local changes instead of scanning every file for…	
o	--nowatchfs	Scan every file for a change	
o	--windows_enable_symlinks	Real symbolic links will be created on Windows instead of file copying	
o	--nowindows_enable_symlinks	Real symbolic links will be created via file copying	
o	--workspace_rc	Look for the workspace bazelrc file at $workspace/.bazelrc	
o	--noworkspace_rc	Don't look for the workspace bazelrc file at $workspace/.bazelrc	
=		--bazelrc
t	filepaths
=		--failure_detail_out
t	filepaths
=		--io_nice_level
v	0	
v	1	
v	2	
v	3	
v	4	
v	5	
v	6	
v	7	
=		--output_base
t	filepaths
=		--output_base_root
t	filepaths
=		--server_jvm_out
t	filepaths
@	run
a	1	0
#	run	1
d
@	test
a	1	0
#	test	1
d
@	build
a	1	0
#	build	1
d
