@	
s	use	Setup current shell to use a specific ruby version
s	reset	Remove default and current settings, exit the shell
s	info	Show information about the current ruby environment
s	list	List currently installed version
s	reload	Reload RVM source itself (useful after changing RVM source)
s	implode	Remove all ruby installations it manages
s	get	Upgrades RVM to the stable or git head branches
s	do	Runs a named ruby file against specified and/or all rubies
s	install	Install one or many ruby versions
s	upgrade	Install new ruby, copy gemsets, make gems pristine, remove old rubies
s	reinstall	Remove ruby, install it, make gems pristine
s	uninstall	Uninstall one or many ruby versions, leaves their sources
s	remove	Remove one or many ruby versions, including their sources
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
o	--help|-h	Show help for rvm	p
@	use
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	use rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	use jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	use ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	use ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	use system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	use default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reset
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	reset rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reset jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reset ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reset ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reset system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reset default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	info
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	info rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	info jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	info ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	info ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	info system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	info default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	list
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	list rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	list jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	list ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	list ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	list system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	list default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reload
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	reload rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reload jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reload ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reload ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reload system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reload default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	implode
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	implode rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	implode jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	implode ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	implode ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	implode system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	implode default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	get
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	get rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	get jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	get ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	get ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	get system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	get default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	do
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	do rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	do jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	do ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	do ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	do system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	do default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	install
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	install rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	install jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	install ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	install ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	install system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	install default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	upgrade
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	upgrade rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	upgrade jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	upgrade ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	upgrade ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	upgrade system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	upgrade default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reinstall
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	reinstall rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reinstall jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reinstall ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reinstall ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reinstall system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	reinstall default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	uninstall
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	uninstall rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	uninstall jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	uninstall ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	uninstall ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	uninstall system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	uninstall default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	remove
s	rbx	Rubinius
s	jruby	JRuby
s	ruby	MRI/YARV Ruby (The Standard), defaults to 1.8.6
s	ree	Ruby Enterprise Edition
s	system	Use the system ruby (eg. pre-RVM state)
s	default	Use RVM set default ruby and system if it hasn't been set
@	remove rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	remove jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	remove ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	remove ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	remove system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	remove default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	rbx
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	jruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	ruby
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	ree
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	system
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
@	default
o	--version|-v	Show version of rvm	
o	--default	When used with ruby selection, sets a default ruby for new shells	
o	--debug	Enable debug mode	
o	--force	Force install, removes old install & source before install	
o	--all	Used with 'rvm list' to display 'most' available versions	
o	--summary	Used with 'do' to print out a summary of the commands run	
o	-C	Custom configure options, comma separated, double quote args that need quoting, default	
