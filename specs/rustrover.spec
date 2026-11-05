@	
s	diff	Open the diff viewer to see the differences between two specified files
s	merge	Open the Merge dialog to merge the specified files
s	format	Apply code style formatting to the specified files
s	inspect	Perform code inspection on the specified project
s	installPlugins	Install plugins by plugin ID from JetBrains Marketplace or a custom plugin repository
o	nosplash	Do not show the splash screen when loading RustRover	
o	dontReopenProjects	Do not reopen projects and show the welcome screen	
o	disableNonBundledPlugins	Do not load manually installed plugins	
o	--wait	Wait for the files to be closed before returning to the command prompt	
a	1	0
#		1
t	filepaths
@	diff
a	3	0
#	diff	1
t	filepaths
#	diff	2
t	filepaths
#	diff	3
t	filepaths
@	merge
a	3	0
#	merge	1
t	filepaths
#	merge	2
t	filepaths
#	merge	3
t	filepaths
@	format
o	-h	Show help for format command	
o	-m|-mask	Specify a comma-separated list of file masks that define the files to be processed	
o	-r|-R	Process specified directories recursively	
o	-s|-settings	Specify the code style settings file to use for formatting	
o	-allowDefaults	Use the default code style settings when the code style is not defined for a file or a group of…	
o	-charset	Preserve encoding and enforce the charset for reading and writing source files	
o	-d|-dry	Run the formatter in the validation mode	
a	1	0
#	format	1
t	filepaths
@	inspect
o	-changes	Run inspections only on local uncommitted changes	
o	-d	Specify the full path to the subdirectory if you don't want to inspect the whole project	
o	-format	Specify the format of the output file with inspection results	
o	-v	Set the verbosity level of the output	
a	3	0
#	inspect	1
t	folders
#	inspect	2
t	filepaths
#	inspect	3
t	filepaths
@	installPlugins
a	2	0
