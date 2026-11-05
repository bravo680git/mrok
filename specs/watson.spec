@	
s	add	Add time to a project with tag(s) that was not tracked live
s	aggregate	Display a report of the time spent on each project aggregated by day
s	cancel	Cancel the last call to the start command. The time will not be recorded
s	config	Get and set configuration options
s	edit	Edit a frame
s	frames	Display the list of all frame IDs
s	help	Display help information
s	log	Display each recorded session during the given timespan
s	merge	Perform a merge of the existing frames with a conflicting frames file. When storing the frames on…
s	projects	Display the list of all the existing projects
s	remove	Remove a frame. You can specify the frame either by id or by position (ex: -1 for the last frame)
s	rename	Rename a project or tag
s	report	Display a report of the time spent on each project
s	restart	Restart monitoring time for a previously stopped project
s	start	Start monitoring time for the given project. You can add tags indicating more specifically what…
s	status	Display when the current project was started and the time spent since
s	stop	Stop monitoring time for the current project
s	sync	Get the frames from the server and push the new ones
s	tags	Display the list of all the tags
o	--help	Show help for watson	p
o	--version	Show the version for watson	
o	--color	Color output	
o	--no-color	No color output	
@	add
o	--from|-f	Date and time of start of tracked activity	v
o	--to|-t	Date and time of end of tracked activity	v
o	--confirm-new-project|-c	Confirm creation of new tag	
a	1	0
#	add	1
d
@	aggregate
o	--current|-c	Include currently running frame in report	
o	--no-current|-C	Don't include currently running frame in report	
o	--from|-f	The date from when the reports should start. Defaults to seven days ago	v
o	--to|-t	The date at which the report should stop (inclusive). Defaults to tomorrow	v
o	--project|-p	Reports activity only for the given project. You can add other projects by using this option…	v
o	--tag|-T	Reports activity only for frames containing the given tag. You can add several tags by using this…	v
o	--json|-j	Format output in JSON instead of plain text	
o	--csv|-s	Format output in CSV instead of plain text	
o	--pager|-g	View output through a pager	
o	--no-pager|-G	Don't view output through a pager	
=	aggregate	--project
d
=	aggregate	--tag
d
@	cancel
@	config
o	--edit|-e	Edit the configuration file with an editor	
a	2	0
#	config	1
v	backend.url	This is the API root url of your repository, e.g. https://my.server.com/api/
v	backend.token	To authenticate watson as an API client, once generated, you will need to set up your API token in…
v	options.confirm_new_project	If true, the user will be asked for confirmation before creating a new project. The option can be…
v	options.confirm_new_tag	If true, the user will be asked for confirmation before creating a new tag. The option can be…
v	options.date_format	Globally configure how dates should be formatted. All python’s strftime directives are supported…
v	options.log_current	If true, the output of the log command will include the currently running frame (if any) by…
v	options.pager	If true, the output of the log and report command will be run through a pager by default. The…
v	options.report_current	If true, the output of the report command will include the currently running frame (if any) by…
v	options.reverse_log	If true, the output of the log command will reverse the order of the days to display the latest…
v	options.stop_on_start	If true, starting a new project will stop running projects. Default false
v	options.stop_on_restart	Similar to the options.stop_on_start option, but for the restart command. Default: false
v	options.time_format	Globally configure how time should be formatted. All python’s strftime directives are supported…
v	options.week_start	Globally configure which day corresponds to the start of a week. Allowable values are monday…
@	edit
o	--confirm-new-project|-c	Confirm addition of new project	
o	--confirm-new-tag|-b	Confirm creation of new tag	
a	1	0
#	edit	1
d
@	frames
@	help
a	1	0
@	log
o	--current|-c	Include currently running frame in report	
o	--no-current|-C	Don't include currently running frame in report	
o	--reverse|-r	Reverse the order of the days in output	
o	--no-reverse|-R	Don't Reverse the order of the days in output	
o	--from|-f	The date from when the log should start. Defaults to seven days ago	v
o	--to|-t	The date at which the log should stop (inclusive). Defaults to tomorrow	v
o	--year|-y	Reports activity for the current year	
o	--month|-m	Reports activity for the current month	
o	--luna|-l	Reports activity for the current moon cycle	
o	--week|-w	Reports activity for the current week	
o	--day|-d	Reports activity for the current day	
o	--all|-a	Reports all activities	
o	--project|-p	Logs activity only for the given project. You can add other projects by using this option several…	v
o	--tag|-T	Logs activity only for frames containing the given tag. You can add several tags by using this…	v
o	--ignore-project	Logs activity for all projects but the given ones. You can ignore several projects by using the…	v
o	--ignore-tag	Logs activity for all tags but the given ones. You can ignore several tags by using the option…	v
o	--json|-j	Format output in JSON instead of plain text	
o	--csv|-s	Format output in CSV instead of plain text	
o	--pager|-g	View output through a pager	
o	--no-pager|-G	Don't view output through a pager	
=	log	--project
d
=	log	--tag
d
=	log	--ignore-project
d
=	log	--ignore-tag
d
@	merge
o	-f|--force	If specified, then the merge will automatically be performed	
a	1	0
@	projects
@	remove
o	-f|--force	Don’t ask for confirmation	
a	1	0
#	remove	1
d
@	rename
a	3	0
#	rename	1
v	project	
v	tag	
#	rename	2
d
@	report
o	--current|-c	Include currently running frame in report	
o	--no-current|-C	Don't include currently running frame in report	
o	--from|-f	The date from when the report should start. Defaults to seven days ago	v
o	--to|-t	The date at which the report should stop (inclusive). Defaults to tomorrow	v
o	--year|-y	Reports activity for the current year	
o	--month|-m	Reports activity for the current month	
o	--luna|-l	Reports activity for the current moon cycle	
o	--week|-w	Reports activity for the current week	
o	--day|-d	Reports activity for the current day	
o	--project|-p	Reports activity only for the given project. You can add other projects by using this option…	v
o	--tag|-T	Reports activity only for frames containing the given tag. You can add several tags by using this…	v
o	--ignore-project	Reports activity for all projects but the given ones. You can ignore several projects by using the…	v
o	--ignore-tag	Reports activity for all tags but the given ones. You can ignore several tags by using the option…	v
o	--json|-j	Format output in JSON instead of plain text	
o	--csv|-s	Format output in CSV instead of plain text	
o	--pager|-g	View output through a pager	
o	--no-pager|-G	Don't view output through a pager	
=	report	--project
d
=	report	--tag
d
=	report	--ignore-project
d
=	report	--ignore-tag
d
@	restart
o	--at	Start frame at this time. Must be in (YYYY-MM-DDT)?HH:MM(:SS)? format	v
o	--stop|-s	Stop an already running project	
o	--no-stop|-S	Don't stop an already running project	
a	1	0
#	restart	1
d
@	start
o	--at	Start frame at this time. Must be in (YYYY-MM-DDT)?HH:MM(:SS)? format	v
o	--gap|-g	Leave gap between end time of previous project and start time of the current	
o	--no-gap|-G	Don't leave gap between end time of previous project and start time of the current	
o	--confirm-new-project|-c	Confirm addition of new project	
o	--confirm-new-tag|-b	Confirm creation of new tag	
a	1	1
#	start	1
d
@	status
o	--project|-p	Only output project	
o	--tags|-t	Only show tags	
o	--elapsed|-e	Only show time elapsed	
@	stop
o	--at	Stop frame at this time. Must be in (YYYY-MM-DDT)?HH:MM(:SS)? format	v
@	sync
@	tags
