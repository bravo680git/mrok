@	
o	--noGit	Explicitly tell the CLI to not initialize a new git repo in the project (default: false)	
o	--noInstall	Explicitly tell the CLI to not run the package manager's install command (default: false)	
o	-y|--default	Bypass the CLI and use all default options to bootstrap a new t3-app (default: false)	
o	--CI	Boolean value if we're running in CI (default: false)	
o	--tailwind	Experimental: Boolean value if we should install Tailwind CSS. Must be used in conjunction with…	v
o	--nextAuth	Experimental: Boolean value if we should install NextAuth.js. Must be used in conjunction with…	v
o	--prisma	Experimental: Boolean value if we should install Prisma. Must be used in conjunction with `--CI`	v
o	--trpc	Experimental: Boolean value if we should install tRPC. Must be used in conjunction with `--CI`	v
o	-i|--import-alias	Explicitly tell the CLI to use a custom import alias	v
o	-v|--version	Display the version number	
o	--help|-h	Display help for command	
a	1	0
=		--tailwind
v	true	Install Tailwind CSS
v	false	Do not install Tailwind CSS
=		--nextAuth
v	true	Install NextAuth.js
v	false	Do not install NextAuth.js
=		--prisma
v	true	Install Prisma
v	false	Do not install Prisma
=		--trpc
v	true	Install tRPC
v	false	Do not install tRPC
=		-i
v	~/	Use the ~/ alias
v	@/	Use the @/ alias
#		1
t	folders
