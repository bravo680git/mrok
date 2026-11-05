@	
o	--code|-c	Format the code passed in as a string	v
o	--line-length|-l	How many characters per line to allow	v
o	--target-version|-t	Python versions that should be supported	v
o	--pyi	Format all input files regardless of file extension	
o	--ipynb	Format all input files like Jupyter Notebooks regardless of file extension	
o	--python-cell-magics	Add the given magic to the list of known python-magics	v
o	--skip-string-normalization|-S	Don't normalize string quotes or prefixes	
o	--skip-magic-trailing-comma|-C	Don't use trailing commas as a reason to split lines	
o	--preview	Enable potentially disruptive style changes	
o	--check	Don't write the files back, just return the status	
o	--diff	Don't write the files back, just output a diff for each file on stdout	
o	--color	Show colored diff	
o	--no-color	Show uncolored diff	
o	--fast	Skip temporary sanity checks	
o	--safe	Run temporary sanity checks	
o	--required-version	Require a specific version of Black	v
o	--include	Regex that matches files and directories that should be included on recursive searches	v
o	--exclude	Regex that matches files and directories that should be excluded on recursive searches	v
o	--extend-exclude	Additional exlusions	v
o	--force-exclude	Exlude matching files and folders even when passed explicitly	v
o	--stdin-filename	The name of the file when passing it through stdin	v
o	--workers|-W	Number of parallel workers	v
o	--quiet|-q	Don't emit non-error messages to stderr	
o	--verbose|-v	Also emit messages about files that were not changed or were ignored due to exclusion patterns	
o	--version	Show the version	
o	--config	Read configuration from filepath	v
o	--help|-h	Show usage information	
a	1	1
=		--target-version
v	py33	
v	py34	
v	py35	
v	py36	
v	py37	
v	py38	
v	py39	
v	py310	
=		--python-cell-magics
v	python	
v	python3	
v	timeit	
v	prun	
v	time	
v	pypy	
v	capture	
=		--required-version
d
=		--stdin-filename
t	filepaths
=		--config
t	filepaths
#		1
t	filepaths
