@	
o	--help|-h	Show help for mkinitcpio	
o	--version|-V	Display version information	
o	--addhooks|-A	Add additional hooks to the image	v
o	--config|-c	Use config file to generate the ramdisk	v
o	--generatedir|-d	Set directory as the location where the initramfs is built	v
o	--hookdir|-D	Set directory as the location where hooks will be searched for when generating the image	v
o	--generate|-g	Generate a CPIO image as filename	v
o	--hookhelp|-H	Output help for hookname	v
o	--kernel|-k	Use kernelversion, instead of the current running kernel	v
o	--listhooks|-L	List all available hooks	
o	--automods|-M	Display modules found via autodetection	
o	--nocolor|-n	Disable color output	
o	--uefi|-U	Generate a UEFI executable as filename	v
o	--allpresets|-P	Process all presets contained in /etc/mkinitcpio.d	
o	--preset|-p	Build initramfs image(s) according to specified preset	v
o	--moduleroot|-r	Specifies the root directory to find modules in	v
o	--skiphooks|-S	Skip hooks when generating the image	v
o	--save|-s	Saves the build directory for the initial ramdisk	
o	--builddir|-t	Use tmpdir as the temporary build directory instead of /tmp	v
o	--verbose|-v	Verbose output	
o	--compress|-z	Override the compression method with the compress program	v
o	--cmdline	Use kernel command line with UEFI executable	v
o	--splash	UEFI executables can show a bitmap file on boot	v
o	--uefistub	UEFI stub image used for UEFI executable generation	v
o	--kernelimage	Include a kernel image for the UEFI executable	v
o	--microcode	Include microcode into the UEFI executable	v
o	--osrelease	Include a os-release file for the UEFI executable	v
=		--addhooks
t	filepaths
=		--config
t	filepaths
=		--generatedir
t	folders
=		--hookdir
t	folders
=		--preset
d
=		--builddir
t	folders
