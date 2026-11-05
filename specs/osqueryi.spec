@	
o	--flagfile	Line-delimited file of additional flags	v
o	--D	Run as a daemon process	
o	--S	Run as a shell process	
o	--alarm_timeout	Seconds to allow for shutdown. Minimum is 10	v
o	--carver_block_size	Size of blocks used for POSTing data back to remote endpoints	v
o	--carver_compression	Compress archives using zstd prior to upload (default false)	
o	--carver_continue_endpoint	TLS/HTTPS endpoint that receives carved content after session creation	v
o	--carver_disable_function	Disable the osquery file carver function (default true)	
o	--carver_expiry	Seconds to store successful carve result metadata (in carves table)	v
o	--carver_start_endpoint	TLS/HTTPS init endpoint for forensic carver	v
o	--config_accelerated_refresh	Interval to wait if reading a configuration fails	v
o	--config_check	Check the format of an osquery config and exit	
o	--config_dump	Dump the contents of the configuration, then exit	
o	--config_enable_backup	Backup config and use it when refresh fails	
o	--config_path	Path to JSON config file	v
o	--config_plugin	Config plugin name	v
o	--config_refresh	Optional interval in seconds to re-read configuration	v
o	--config_tls_endpoint	TLS/HTTPS endpoint for config retrieval	v
o	--config_tls_max_attempts	Number of attempts to retry a TLS config request	v
o	--daemonize	Attempt to daemonize (POSIX only)	
o	--database_dump	Dump the contents of the backing store	
o	--database_path	If using a disk-based backing store, specify a path	v
o	--disable_carver	Disable the osquery file carver (default true)	
o	--disable_enrollment	Disable enrollment functions on related config/logger plugins	
o	--disable_extensions	Disable extension API	
o	--disable_reenrollment	Disable re-enrollment attempts if related plugins return invalid	
o	--disable_tables	Comma-delimited list of table names to be disabled	v
o	--disable_watchdog	Disable userland watchdog process	
o	--enable_extensions_watchdog	Enable userland watchdog for extensions processes	
o	--enable_tables	Comma-delimited list of table names to be enabled	v
o	--enroll_always	On startup, send a new enrollment request	
o	--enroll_secret_env	Name of environment variable holding enrollment-auth secret	v
o	--enroll_secret_path	Path to an optional client enrollment-auth secret	v
o	--enroll_tls_endpoint	TLS/HTTPS endpoint for client enrollment	v
o	--extensions_autoload	Optional path to a list of autoloaded & managed extensions	v
o	--extensions_interval	Seconds delay between connectivity checks	v
o	--extensions_require	Comma-separated list of required extensions	v
o	--extensions_socket	Path to the extensions UNIX domain socket	v
o	--extensions_timeout	Seconds to wait for autoloaded extensions	v
o	--force	Force osqueryd to kill previously-running daemons	
o	--install	Install osqueryd as a service	
o	--logger_mode	Octal mode for log files (default '0640')	v
o	--logger_plugin	Logger plugin name	v
o	--logger_stderr	Write status logs to stderr	
o	--logtostderr	Log messages to stderr in addition to the logger plugin(s)	
o	--pidfile	Path to the daemon pidfile mutex	v
o	--proxy_hostname	Optional HTTP proxy hostname	v
o	--stderrthreshold	Stderr log level threshold	v
o	--tls_client_cert	Optional path to a TLS client-auth PEM certificate	v
o	--tls_client_key	Optional path to a TLS client-auth PEM private key	v
o	--tls_enroll_max_attempts	The total number of attempts that will be made to the enroll endpoint if a request fails, 0 for…	v
o	--tls_enroll_max_interval	Maximum wait time in seconds between enroll retry attempts	v
o	--tls_hostname	TLS/HTTPS hostname for Config, Logger, and Enroll plugins	v
o	--tls_server_certs	Optional path to a TLS server PEM certificate(s) bundle	v
o	--tls_session_reuse	Reuse TLS session sockets	
o	--tls_session_timeout	TLS session keep alive timeout in seconds	v
o	--uninstall	Uninstall osqueryd as a service	
o	--watchdog_delay	Initial delay in seconds before watchdog starts	v
o	--watchdog_forced_shutdown_delay	Seconds that the watchdog will wait to do a forced shutdown after a graceful shutdown request…	v
o	--watchdog_latency_limit	Override watchdog profile CPU utilization latency limit	v
o	--watchdog_level	Performance limit level	v
o	--watchdog_memory_limit	Override watchdog profile memory limit (e.g., 300, for 300MB)	v
o	--watchdog_utilization_limit	Override watchdog profile CPU utilization limit	v
o	--audit_allow_config	Allow the audit publisher to change auditing configuration	
o	--audit_allow_fim_events	Allow the audit publisher to install filesystem-related rules	
o	--audit_allow_process_events	Allow the audit publisher to install process-related rules	
o	--audit_allow_sockets	Allow the audit publisher to install socket-related rules	
o	--audit_allow_user_events	Allow the audit publisher to install user-related rules	
o	--augeas_lenses	Directory that contains augeas lenses files	v
o	--aws_access_key_id	AWS access key ID	v
o	--aws_debug	Enable AWS SDK debug logging	
o	--aws_enable_proxy	Enable proxying of HTTP/HTTPS requests in AWS client config	
o	--aws_firehose_endpoint	Custom Firehose endpoint	v
o	--aws_firehose_period	Seconds between flushing logs to Firehose (default 10)	v
o	--aws_firehose_stream	Name of Firehose stream for logging	v
o	--aws_kinesis_disable_log_status	Disable status logs processing	
o	--aws_kinesis_endpoint	Custom Kinesis endpoint	v
o	--aws_kinesis_period	Seconds between flushing logs to Kinesis (default 10)	v
o	--aws_kinesis_random_partition_key	Enable random kinesis partition keys	
o	--aws_kinesis_stream	Name of Kinesis stream for logging	v
o	--aws_profile_name	AWS profile for authentication and region configuration	v
o	--aws_proxy_host	Proxy host for use in AWS client config	v
o	--aws_proxy_password	Proxy password for use in AWS client config	v
o	--aws_proxy_port	Proxy port for use in AWS client config	v
o	--aws_proxy_scheme	Proxy HTTP scheme for use in AWS client config (http or https, default https)	v
o	--aws_proxy_username	Proxy username for use in AWS client config	v
o	--aws_region	AWS region	v
o	--aws_secret_access_key	AWS secret access key	v
o	--aws_session_token	AWS STS session token	v
o	--aws_sts_arn_role	AWS STS ARN role	v
o	--aws_sts_region	AWS STS region	v
o	--aws_sts_session_name	AWS STS session name	v
o	--aws_sts_timeout	AWS STS assume role credential validity in seconds (default 3600)	v
o	--buffered_log_max	Maximum number of logs in buffered output plugins (0 = unlimited)	v
o	--decorations_top_level	Add decorators as top level JSON objects	
o	--disable_audit	Disable receiving events from the audit subsystem	
o	--disable_caching	Disable scheduled query caching	
o	--disable_database	Disable the persistent RocksDB storage	
o	--disable_decorators	Disable log result decoration	
o	--disable_distributed	Disable distributed queries (default true)	
o	--disable_endpointsecurity	Disable receiving events from the EndpointSecurity subsystem	
o	--disable_endpointsecurity_fim	Disable file events from the EndpointSecurity subsystem	
o	--disable_events	Disable osquery publish/subscribe system	
o	--disable_hash_cache	Cache calculated file hashes, re-calculate only if inode times change	
o	--disable_logging	Disable ERROR/INFO logging	
o	--distributed_interval	Seconds between polling for new queries (default 60)	v
o	--distributed_loginfo	Log the running distributed queries name at INFO level	
o	--distributed_plugin	Distributed plugin name	v
o	--distributed_tls_max_attempts	Number of times to attempt a request	v
o	--distributed_tls_read_endpoint	TLS/HTTPS endpoint for distributed query retrieval	v
o	--distributed_tls_write_endpoint	TLS/HTTPS endpoint for distributed query results	v
o	--docker_socket	Docker UNIX domain socket path	v
o	--enable_file_events	Enables the file_events publisher	
o	--enable_foreign	Enable no-op foreign virtual tables	
o	--enable_keyboard_events	Enable listening for keyboard events	
o	--enable_mouse_events	Enable listening for mouse events	
o	--enable_numeric_monitoring	Enable numeric monitoring system	
o	--ephemeral	Skip pidfile and database state checks	
o	--es_fim_mute_path_literal	Comma delimited list of path literals to be muted for FIM	v
o	--es_fim_mute_path_prefix	Comma delimited list of path prefxes to be muted for FIM	v
o	--events_expiry	Timeout to expire event subscriber results	v
o	--events_max	Maximum number of event batches per type to buffer	v
o	--events_optimize	Optimize subscriber select queries (scheduler only)	
o	--extensions_default_index	Enable INDEX on all extension table columns (default true)	
o	--hash_cache_max	Size of LRU file hash cache	v
o	--host_identifier	Field used to identify the host running osquery (hostname, uuid, instance, ephemeral, specified)	v
o	--logger_event_type	Log scheduled results as events	
o	--logger_kafka_acks	The number of acknowledgments the leader has to receive (0, 1, 'all')	v
o	--logger_kafka_brokers	Bootstrap broker(s) as a comma-separated list of host or host:port (default port 9092)	v
o	--logger_kafka_compression	Compression codec to use for compressing message sets ('none' or 'gzip')	v
o	--logger_kafka_topic	Kafka topic to publish logs under	v
o	--logger_min_status	Minimum level for status log recording	v
o	--logger_min_stderr	Minimum level for statuses written to stderr	v
o	--logger_numerics	Use numeric JSON syntax for numeric values	
o	--logger_path	Directory path for ERROR/WARN/INFO and results logging	v
o	--logger_rotate	Use filesystem log rotation	
o	--logger_rotate_max_files	Max number of files to keep in rotation	v
o	--logger_rotate_size	Size for each filesystem log in bytes	v
o	--logger_snapshot_event_type	Log scheduled snapshot results as events	
o	--logger_syslog_facility	Syslog facility for status and results logs (0-23, default 19)	v
o	--logger_syslog_prepend_cee	Prepend @cee: tag to logged JSON messages	
o	--logger_tls_compress	GZip compress TLS/HTTPS request body	
o	--logger_tls_endpoint	TLS/HTTPS endpoint for results logging	v
o	--logger_tls_max_lines	Max number of logs to send per period	v
o	--logger_tls_max_linesize	Max size in bytes allowed per log line	v
o	--logger_tls_period	Seconds between flushing logs over TLS/HTTPS	v
o	--nullvalue	Set string for NULL values, default ''	v
o	--numeric_monitoring_filesystem_path	File to dump numeric monitoring records one per line. The format of the line is…	v
o	--numeric_monitoring_plugins	Comma separated numeric monitoring plugins names	v
o	--numeric_monitoring_pre_aggregation_time	Time period in seconds for numeric monitoring pre-aggregation buffer	v
o	--pack_delimiter	Delimiter for pack and query names	v
o	--pack_refresh_interval	Cache expiration for a packs discovery queries	v
o	--read_max	Maximum file read size	v
o	--schedule_default_interval	Query interval to use if none is provided	v
o	--schedule_epoch	Epoch for scheduled queries	v
o	--schedule_lognames	Log the running scheduled query name at INFO level	
o	--schedule_max_drift	Max time drift in seconds	v
o	--schedule_reload	Interval in seconds to reload database arenas	v
o	--schedule_splay_percent	Percent to splay config times	v
o	--schedule_timeout	Limit the schedule to a duration in seconds, 0 for no limit	v
o	--specified_identifier	Field used to specify the host_identifier when set to 'specified'	v
o	--table_delay	Add an optional microsecond delay between table scans	v
o	--table_exceptions	Allow tables to throw exceptions	
o	--thrift_string_size_limit	Sets the maximum string size allowed in a thrift message, use 0 for unlimited	v
o	--thrift_timeout	Timeout for thrift socket operations	v
o	--thrift_verbose	Enable the thrift log handler	
o	--tls_disable_status_log	Disable sending status logs	
o	--verbose	Enable verbose informational messages	
o	--worker_threads	Number of work dispatch threads	v
o	--yara_delay	Time in ms to sleep after scan of each file (default 50) to reduce memory spikes	v
o	--A	Select all from a table	v
o	--L	List all table names	
o	--connect	Connect to an extension socket	v
o	--csv	Set output mode to 'csv'	
o	--extension	Path to a single extension to autoload	v
o	--header	Toggle column headers true/false	
o	--json	Set output mode to 'json'	
o	--json_pretty	Set output mode to 'json_pretty'	
o	--line	Set output mode to 'line'	
o	--list	Set output mode to 'list'	
o	--pack	Run all queries in a pack	v
o	--planner	Enable osquery runtime planner output	
o	--profile	Enable profile mode when non-0, set number of iterations	v
o	--separator	Set output field separator, default '|'	v
=		--flagfile
t	filepaths
=		--config_path
t	filepaths
=		--database_path
t	filepaths
=		--disable_tables
d
=		--enable_tables
d
=		--enroll_secret_path
t	filepaths
=		--extensions_autoload
t	filepaths
=		--extensions_socket
t	filepaths
=		--pidfile
t	filepaths
=		--tls_client_cert
t	filepaths
=		--tls_client_key
t	filepaths
=		--tls_server_certs
t	filepaths
=		--watchdog_level
v	0	Normal
v	1	Restrictive
v	-1	Off
=		--docker_socket
t	filepaths
=		--logger_kafka_acks
v	0	
v	1	
v	all	
=		--logger_kafka_compression
v	none	
v	gzip	
=		--logger_path
t	filepaths
=		--extension
t	filepaths,folders
