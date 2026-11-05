@	
o	--help|-h	Show help for neofetch	
o	--disable	Disable information line	v
o	--title_fqdn	Hide/Show Fully Qualified Domain Name in title	v
o	--package_managers	Hide/Show Package Manager names	v
o	--os_arch	Hide/Show OS architecture	v
o	--speed_type	Change the type of cpu speed to display	v
o	--speed_shorthand	Whether or not to show decimals in CPU speed	v
o	--cpu_brand	Enable/Disable CPU brand in output	v
o	--cpu_cores	Whether or not to display the number of CPU cores	v
o	--cpu_speed	Hide/Show cpu speed	v
o	--cpu_temp	Hide/Show cpu temperature	v
o	--distro_shorthand	Shorten the output of distro	v
o	--kernel_shorthand	Shorten the output of kernel	v
o	--uptime_shorthand	Shorten the output of uptime	v
o	--refresh_rate	Whether to display the refresh rate of each monitor	v
o	--gpu_brand	Enable/Disable GPU brand in output	v
o	--gpu_type	Which GPU to display	v
o	--de_version	Show/Hide Desktop Environment version	v
o	--gtk_shorthand	Shorten output of gtk theme/icons	v
o	--gtk2	Enable/Disable gtk2 theme/font/icons output	v
o	--gtk3	Enable/Disable gtk3 theme/font/icons output	v
o	--shell_path	Enable/Disable showing $SHELL path	v
o	--shell_version	Enable/Disable showing $SHELL version	v
o	--disk_show	Which disks to display	v
o	--disk_subtitle	What information to append to the Disk subtitle	v
o	--disk_percent	Hide/Show disk percent	v
o	--ip_host	URL to query for public IP	v
o	--ip_timeout	Public IP timeout	v
o	--memory_percent	Display memory percentage	v
o	--memory_unit	Memory output unit	v
o	--colors	Changes the text colors	v
o	--underline	Enable/Disable the underline	v
o	--underline_char	Character to use when underlining title	v
o	--bold	Enable/Disable bold text	v
o	--separator	Changes the default ':' separator to the specified string	v
o	--color_blocks	Enable/Disable the color blocks	v
o	--col_offset	Left-padding of color blocks	v
o	--block_width	Width of color blocks in spaces	v
o	--block_height	Height of color blocks in lines	v
o	--block_range	Range of colors to print as blocks	v
o	--bar_char	Characters to use when drawing bars	v
o	--bar_border	Whether or not to surround the bar with '[]'	v
o	--bar_length	Length in spaces to make the bars	v
o	--bar_colors	Colors to make the bar	v
o	--cpu_display	CPU bar mode	v
o	--memory_display	Memory display mode	v
o	--battery_display	Battery display mode	v
o	--disk_display	Disk display mode	v
o	--backend	Which image backend to use	v
o	--source	Which image or ascii file to use	v
o	--ascii	Same as --backend ascii	
o	--caca	Same as --backend caca	
o	--chafa	Same as --backend chafa	
o	--iterm2	Same as --backend iterm2	
o	--jp2a	Same as --backend jp2a	
o	--kitty	Same as --backend kitty	
o	--pot	Same as --backend pot	
o	--pixterm	Same as --backend pixterm	
o	--sixel	Same as --backend sixel	
o	--termpix	Same as --backend termpix	
o	--tycat	Same as --backend tycat	
o	--w3m	Same as --backend w3m	
o	--off	Same as --backend off	
o	--ascii_colors	Colors to print the ascii art	v
o	--ascii_distro	Which Distro's ascii art to print	v
o	--ascii_bold	Whether or not to bold the ascii logo	v
o	-L|--logo	Hide the info text and only show the ascii logo	
o	--loop	Redraw the image constantly until Ctrl+C is used	
o	--size	How to size the image	v
o	--crop_mode	Which crop mode to use	v
o	--crop_offset	Change the crop offset for normal mode	v
o	--xoffset	How close the image will be to the left edge of the window. This only works with w3m	v
o	--yoffset	How close the image will be to the top edge of the window. This only works with w3m	v
o	--gap	Gap between image and text	v
o	--clean	Delete cached files and thumbnails	
o	--config	Specify a path to a custom config file	v
o	--no_config	Don't create the user config file	
o	--print_config	Print the default config file to stdout	
o	--stdout	Turn off all colors and disables any ASCII/image backend	
o	--version	Show neofetch version	
o	-v	Display error messages	
o	-vv	Display a verbose log for error reporting	
o	--gen-man	Generate a manpage for neofetch in your PWD	
a	1	1
=		--disable
v	os	
v	host	
v	kernel	
v	uptime	
v	packages	
v	shell	
v	term	
v	cpu	
v	gpu	
v	memory	
v	disk	
v	battery	
v	resolution	
v	wm	
v	de	
v	theme	
v	wm_theme	
v	icons	
=		--title_fqdn
v	on	
v	off	
=		--package_managers
v	on	
v	off	
v	tiny	
=		--os_arch
v	on	
v	off	
=		--speed_type
v	current	
v	min	
v	bios	
v	scaling_current	
v	scaling_min	
v	scaling_max	
=		--speed_shorthand
v	on	
v	off	
=		--cpu_brand
v	on	
v	off	
=		--cpu_cores
v	logical	
v	physical	
v	off	
=		--cpu_speed
v	on	
v	off	
=		--cpu_temp
v	C	
v	F	
v	off	
=		--distro_shorthand
v	on	
v	off	
v	tiny	
=		--kernel_shorthand
v	on	
v	off	
=		--uptime_shorthand
v	on	
v	off	
v	tiny	
=		--refresh_rate
v	on	
v	off	
=		--gpu_brand
v	on	
v	off	
=		--gpu_type
v	all	
v	dedicated	
v	integrated	
=		--de_version
v	on	
v	off	
=		--gtk_shorthand
v	on	
v	off	
=		--gtk2
v	on	
v	off	
=		--gtk3
v	on	
v	off	
=		--shell_path
v	on	
v	off	
=		--shell_version
v	on	
v	off	
=		--disk_show
v	/dev/sd	
v	/dev/nvme	
v	/dev/mmcblk	
v	/dev/mapper	
v	/mnt	
v	/run/media	
=		--disk_subtitle
v	name	
v	mount	
v	dir	
v	none	
=		--disk_percent
v	on	
v	off	
=		--memory_percent
v	on	
v	off	
=		--memory_unit
v	kib	
v	mib	
v	gib	
=		--underline
v	on	
v	off	
=		--bold
v	on	
v	off	
=		--color_blocks
v	on	
v	off	
=		--col_offset
v	auto	
v	[0-9]+	
=		--bar_border
v	on	
v	off	
=		--cpu_display
v	bar	
v	infobar	
v	barinfo	
v	off	
=		--memory_display
v	bar	
v	infobar	
v	barinfo	
v	off	
=		--battery_display
v	bar	
v	infobar	
v	barinfo	
v	off	
=		--disk_display
v	bar	
v	infobar	
v	barinfo	
v	off	
=		--backend
v	ascii	
v	caca	
v	chafa	
v	jp2a	
v	iterm2	
v	off	
v	pixterm	
v	pot	
v	sixel	
v	termpix	
v	tycat	
v	w3m	
v	kitty	
=		--source
v	auto	
v	ascii	
v	wallpaper	
t	filepaths
=		--ascii_bold
v	on	
v	off	
=		--size
v	auto	
v	[0-9]+px	
v	[0-9]+%	
=		--crop_mode
v	normal	
v	fit	
v	fill	
=		--crop_offset
v	northwest	
v	north	
v	northeast	
=		--config
v	none	
t	filepaths
#		1
v	os	
v	host	
v	kernel	
v	uptime	
v	packages	
v	shell	
v	term	
v	cpu	
v	gpu	
v	memory	
v	disk	
v	battery	
v	resolution	
v	wm	
v	de	
v	theme	
v	wm_theme	
v	icons	
