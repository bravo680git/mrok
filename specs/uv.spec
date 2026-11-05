@	
s	run	Run a command or script
s	init	Create a new project
s	add	Add dependencies to the project
s	remove	Remove dependencies from the project
s	sync	Update the project's environment
s	lock	Update the project's lockfile
s	export	Export the project's lockfile to an alternate format
s	tree	Display the project's dependency tree
s	tool	Run and install commands provided by Python packages
s	python	Manage Python versions and installations
s	pip	Manage Python packages with a pip-compatible interface
s	venv	Create a virtual environment
s	build	Build Python packages into source distributions and wheels
s	publish	Upload distributions to an index
s	cache	Manage uv's cache
s	self	Manage the uv executable
s	version	Display uv's version
s	help	Display documentation for a command
o	-q|--quiet	Do not print any output	p
o	-v|--verbose	Use verbose output	p
o	--color	Control colors in output	vp
o	--native-tls	Whether to load TLS certificates from the platform's native certificate store	vp
o	--offline	Disable network access	p
o	--allow-insecure-host	Allow insecure connections to a host	vp
o	--no-progress	Hide all progress outputs	p
o	--directory	Change to the given directory prior to running the command	vp
o	--project	Run the command within the given project directory	vp
o	--config-file	The path to a `uv.toml` file to use for configuration	vp
o	--no-config	Avoid discovering configuration files (`pyproject.toml`, `uv.toml`)	p
o	-h|--help	Display the concise help for this command	p
o	-V|--version	Display the uv version	p
=		--color
v	auto	
v	always	
v	never	
@	run
o	--extra	Include optional dependencies from the specified extra name	v
o	--all-extras	Include all optional dependencies	
o	--no-extra	Exclude the specified optional dependencies, if `--all-extras` is supplied	v
o	--no-dev	Omit the development dependency group	
o	--group	Include dependencies from the specified dependency group	v
o	--no-group	Exclude dependencies from the specified dependency group	v
o	--only-group	Only include dependencies from the specified dependency group	v
o	--all-groups	Include dependencies from all dependency groups	
o	-m|--module	Run a Python module	
o	--only-dev	Only include the development dependency group	
o	--no-editable	Install any editable dependencies, including the project and any workspace members, as non-editable	
o	--env-file	Load environment variables from a `.env` file	v
o	--no-env-file	Avoid reading environment variables from a `.env` file	
o	--with	Run with the given packages installed	v
o	--with-editable	Run with the given packages installed as editables	v
o	--with-requirements	Run with all packages listed in the given `requirements.txt` files	v
o	--isolated	Run the command in an isolated virtual environment	
o	--no-sync	Avoid syncing the virtual environment	
o	--locked	Assert that the `uv.lock` will remain unchanged	
o	--frozen	Run without updating the `uv.lock` file	
o	-s|--script	Run the given path as a Python script	
o	--all-packages	Run the command with all workspace members installed	
o	--package	Run the command in a specific package in the workspace	v
o	--no-project	Avoid discovering the project or workspace	
a	1	0
#	run	1
d
@	init
o	--name	The name of the project	v
o	--package	Set up the project to be built as a Python package	
o	--no-package	Do not set up the project to be built as a Python package	
o	--app	Create a project for an application	
o	--lib	Create a project for a library	
o	--script	Create a script	
o	--vcs	Initialize a version control system for the project	v
o	--build-backend	Initialize a build-backend of choice for the project	v
o	--no-readme	Do not create a `README.md` file	
o	--author-from	Fill in the `authors` field in the `pyproject.toml`	v
o	--no-pin-python	Do not create a `.python-version` file for the project	
o	--no-workspace	Avoid discovering a workspace and create a standalone project	
o	-n	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
a	1	0
=	init	--vcs
v	git	
v	none	
=	init	--build-backend
v	hatch	
v	flit	
v	pdm	
v	setuptools	
v	maturin	
v	scikit	
=	init	--author-from
v	auto	
v	git	
v	none	
#	init	1
t	filepaths
@	add
o	-r|--requirements	Add all packages listed in the given `requirements.txt` files	v
o	--dev	Add the requirements to the development dependency group	
o	--optional	Add the requirements to the package's optional dependencies for the specified extra	v
o	--group	Add the requirements to the specified dependency group	v
o	--editable	Add the requirements as editable	
o	--raw-sources	Add source requirements to `project.dependencies`, rather than `tool.uv.sources`	
o	--rev	Commit to use when adding a dependency from Git	v
o	--tag	Tag to use when adding a dependency from Git	v
o	--branch	Branch to use when adding a dependency from Git	v
o	--extra	Extras to enable for the dependency	v
o	--no-sync	Avoid syncing the virtual environment	v
o	--locked	Assert that the `uv.lock` will remain unchanged	v
o	--frozen	Add dependencies without re-locking the project	v
o	--package	Add the dependency to a specific package in the workspace	v
o	--script	Add the dependency to the specified Python script, rather than to a project	v
o	--index	The URLs to use when resolving dependencies, in addition to the default index	v
o	--default-index	The URL of the default package index (by default: <https://pypi.org/simple>)	v
o	--index-url	The URL of the Python package index (by default: <https://pypi.org/simple>)	v
o	--extra-index-url	Extra URLs of package indexes to use, in addition to `--index-url`	v
o	--find-links	Locations to search for candidate distributions, in addition to those found in the registry indexes	v
o	--no-index	Ignore the registry index (e.g., PyPI), instead relying on direct URL dependencies and those…	
o	--index-strategy	The strategy to use when resolving against multiple index URLs	v
o	--keyring-provider	Attempt to use `keyring` for authentication for index URLs	v
o	-U	Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh`	
o	--upgrade-package	Allow upgrades for a specific package, ignoring pinned versions in any existing output file…	v
o	--resolution	The strategy to use when selecting between the different compatible versions for a given package…	v
o	--prerelease	The strategy to use when considering pre-release versions	v
o	--exclude-newer	Limit candidate packages to those that were uploaded prior to the given date	v
o	--no-sources	Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the…	
o	--reinstall	Reinstall all packages, regardless of whether they're already installed. Implies `--refresh`	
o	--reinstall-package	Reinstall a specific package, regardless of whether it's already installed. Implies…	v
o	--link-mode	The method to use when installing packages from the global cache	v
o	--compile-bytecode	Compile Python files to bytecode after installation	
o	-C	Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs	v
o	--no-build-isolation	Disable isolation when building source distributions	v
o	--no-build-isolation-package	Disable isolation when building source distributions for a specific package	v
o	--no-build	Don't build source distributions	
o	--no-build-package	Don't build source distributions for a specific package	v
o	--no-binary	Don't install pre-built wheels	
o	--no-binary-package	Don't install pre-built wheels for a specific package	v
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--refresh	Refresh all cached data	
o	--refresh-package	Refresh cached data for a specific package	v
a	1	1
=	add	--index-strategy
v	first-index	
v	unsafe-first-match	
v	unsafe-best-match	
=	add	--keyring-provider
v	disabled	
v	subprocess	
=	add	--resolution
v	highest	
v	lowest	
v	lowest-direct	
=	add	--prerelease
v	disallow	
v	allow	
v	if-necessary	
v	explicit	
v	if-necessary-or-explicit	
=	add	--link-mode
v	clone	
v	copy	
v	hardlink	
v	symlink	
@	remove
o	--dev	Remove the packages from the development dependency group	
o	--optional	Remove the packages from the project's optional dependencies for the specified extra	v
o	--group	Remove the packages from the specified dependency group	v
o	--no-sync	Avoid syncing the virtual environment after re-locking the project	v
o	--locked	Assert that the `uv.lock` will remain unchanged	v
o	--frozen	Remove dependencies without re-locking the project	v
o	--package	Remove the dependencies from a specific package in the workspace	v
o	--script	Remove the dependency from the specified Python script, rather than from a project	v
o	--index	The URLs to use when resolving dependencies, in addition to the default index	v
o	--default-index	The URL of the default package index (by default: <https://pypi.org/simple>)	v
o	--index-url	The URL of the Python package index (by default: <https://pypi.org/simple>)	v
o	--extra-index-url	Extra URLs of package indexes to use, in addition to `--index-url`	v
o	--find-links	Locations to search for candidate distributions, in addition to those found in the registry indexes	v
o	--no-index	Ignore the registry index (e.g., PyPI), instead relying on direct URL dependencies and those…	
o	--index-strategy	The strategy to use when resolving against multiple index URLs	v
o	--keyring-provider	Attempt to use `keyring` for authentication for index URLs	v
o	-U	Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh`	
o	--upgrade-package	Allow upgrades for a specific package, ignoring pinned versions in any existing output file…	v
o	--resolution	The strategy to use when selecting between the different compatible versions for a given package…	v
o	--prerelease	The strategy to use when considering pre-release versions	v
o	--exclude-newer	Limit candidate packages to those that were uploaded prior to the given date	v
o	--no-sources	Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the…	
o	--reinstall	Reinstall all packages, regardless of whether they're already installed. Implies `--refresh`	
o	--reinstall-package	Reinstall a specific package, regardless of whether it's already installed. Implies…	v
o	--link-mode	The method to use when installing packages from the global cache	v
o	--compile-bytecode	Compile Python files to bytecode after installation	
o	-C	Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs	v
o	--no-build-isolation	Disable isolation when building source distributions	v
o	--no-build-isolation-package	Disable isolation when building source distributions for a specific package	v
o	--no-build	Don't build source distributions	
o	--no-build-package	Don't build source distributions for a specific package	v
o	--no-binary	Don't install pre-built wheels	
o	--no-binary-package	Don't install pre-built wheels for a specific package	v
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--refresh	Refresh all cached data	
o	--refresh-package	Refresh cached data for a specific package	v
a	1	1
=	remove	--index-strategy
v	first-index	
v	unsafe-first-match	
v	unsafe-best-match	
=	remove	--keyring-provider
v	disabled	
v	subprocess	
=	remove	--resolution
v	highest	
v	lowest	
v	lowest-direct	
=	remove	--prerelease
v	disallow	
v	allow	
v	if-necessary	
v	explicit	
v	if-necessary-or-explicit	
=	remove	--link-mode
v	clone	
v	copy	
v	hardlink	
v	symlink	
#	remove	1
d
@	sync
o	--extra	Include optional dependencies from the specified extra name	v
o	--all-extras	Include all optional dependencies	
o	--no-extra	Exclude the specified optional dependencies, if `--all-extras` is supplied	v
o	--no-dev	Omit the development dependency group	
o	--only-dev	Only include the development dependency group	
o	--group	Include dependencies from the specified dependency group	v
o	--no-group	Exclude dependencies from the specified dependency group	v
o	--only-group	Only include dependencies from the specified dependency group	v
o	--all-groups	Include dependencies from all dependency groups	
o	--no-editable	Install any editable dependencies, including the project and any workspace members, as non-editable	
o	--inexact	Do not remove extraneous packages present in the environment	
o	--no-install-project	Do not install the current project	
o	--no-install-workspace	Do not install any workspace members, including the root project	
o	--no-install-package	Do not install the given package(s)	v
o	--locked	Assert that the `uv.lock` will remain unchanged	v
o	--frozen	Sync without updating the `uv.lock` file	v
o	--all-packages	Sync all packages in the workspace	
o	--package	Sync for a specific package in the workspace	v
o	--index	The URLs to use when resolving dependencies, in addition to the default index	v
o	--default-index	The URL of the default package index (by default: <https://pypi.org/simple>)	v
o	--index-url	The URL of the Python package index (by default: <https://pypi.org/simple>)	v
o	--extra-index-url	Extra URLs of package indexes to use, in addition to `--index-url`	v
o	--find-links	Locations to search for candidate distributions, in addition to those found in the registry indexes	v
o	--no-index	Ignore the registry index (e.g., PyPI), instead relying on direct URL dependencies and those…	
o	--index-strategy	The strategy to use when resolving against multiple index URLs	v
o	--keyring-provider	Attempt to use `keyring` for authentication for index URLs	v
o	-U	Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh`	
o	--upgrade-package	Allow upgrades for a specific package, ignoring pinned versions in any existing output file…	v
o	--resolution	The strategy to use when selecting between the different compatible versions for a given package…	v
o	--prerelease	The strategy to use when considering pre-release versions	v
o	--exclude-newer	Limit candidate packages to those that were uploaded prior to the given date	v
o	--no-sources	Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the…	
o	--reinstall	Reinstall all packages, regardless of whether they're already installed. Implies `--refresh`	
o	--reinstall-package	Reinstall a specific package, regardless of whether it's already installed. Implies…	v
o	--link-mode	The method to use when installing packages from the global cache	v
o	--compile-bytecode	Compile Python files to bytecode after installation	
o	-C	Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs	v
o	--no-build-isolation	Disable isolation when building source distributions	v
o	--no-build-isolation-package	Disable isolation when building source distributions for a specific package	v
o	--no-build	Don't build source distributions	
o	--no-build-package	Don't build source distributions for a specific package	v
o	--no-binary	Don't install pre-built wheels	
o	--no-binary-package	Don't install pre-built wheels for a specific package	v
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--refresh	Refresh all cached data	
o	--refresh-package	Refresh cached data for a specific package	v
=	sync	--index-strategy
v	first-index	
v	unsafe-first-match	
v	unsafe-best-match	
=	sync	--keyring-provider
v	disabled	
v	subprocess	
=	sync	--resolution
v	highest	
v	lowest	
v	lowest-direct	
=	sync	--prerelease
v	disallow	
v	allow	
v	if-necessary	
v	explicit	
v	if-necessary-or-explicit	
=	sync	--link-mode
v	clone	
v	copy	
v	hardlink	
v	symlink	
@	lock
o	--locked	Assert that the `uv.lock` will remain unchanged	
o	--frozen	Assert that a `uv.lock` exists, without updating it	
o	--dry-run	Perform a dry run, without writing the lockfile	
o	--index	The URLs to use when resolving dependencies, in addition to the default index	v
o	--default-index	The URL of the default package index (by default: <https://pypi.org/simple>)	v
o	--index-url	The URL of the Python package index (by default: <https://pypi.org/simple>)	v
o	--extra-index-url	Extra URLs of package indexes to use, in addition to `--index-url`	v
o	--find-links	Locations to search for candidate distributions, in addition to those found in the registry indexes	v
o	--no-index	Ignore the registry index (e.g., PyPI), instead relying on direct URL dependencies and those…	
o	--index-strategy	The strategy to use when resolving against multiple index URLs	v
o	--keyring-provider	Attempt to use `keyring` for authentication for index URLs	v
o	-U	Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh`	
o	--upgrade-package	Allow upgrades for a specific package, ignoring pinned versions in any existing output file…	v
o	--resolution	The strategy to use when selecting between the different compatible versions for a given package…	v
o	--prerelease	The strategy to use when considering pre-release versions	v
o	--exclude-newer	Limit candidate packages to those that were uploaded prior to the given date	v
o	--no-sources	Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the…	
o	-C	Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs	v
o	--no-build-isolation	Disable isolation when building source distributions	v
o	--no-build-isolation-package	Disable isolation when building source distributions for a specific package	v
o	--no-build	Don't build source distributions	
o	--no-build-package	Don't build source distributions for a specific package	v
o	--no-binary	Don't install pre-built wheels	
o	--no-binary-package	Don't install pre-built wheels for a specific package	v
o	--link-mode	The method to use when installing packages from the global cache	v
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--refresh	Refresh all cached data	
o	--refresh-package	Refresh cached data for a specific package	v
=	lock	--index-strategy
v	first-index	
v	unsafe-first-match	
v	unsafe-best-match	
=	lock	--keyring-provider
v	disabled	
v	subprocess	
=	lock	--resolution
v	highest	
v	lowest	
v	lowest-direct	
=	lock	--prerelease
v	disallow	
v	allow	
v	if-necessary	
v	explicit	
v	if-necessary-or-explicit	
=	lock	--link-mode
v	clone	
v	copy	
v	hardlink	
v	symlink	
@	export
o	--format	The format to which `uv.lock` should be exported	v
o	--all-packages	Export the entire workspace	
o	--package	Export the dependencies for a specific package in the workspace	v
o	--prune	Prune the given package from the dependency tree	v
o	--extra	Include optional dependencies from the specified extra name	v
o	--all-extras	Include all optional dependencies	
o	--no-extra	Exclude the specified optional dependencies, if `--all-extras` is supplied	v
o	--no-dev	Omit the development dependency group	
o	--only-dev	Only include the development dependency group	
o	--group	Include dependencies from the specified dependency group	v
o	--no-group	Exclude dependencies from the specified dependency group	v
o	--only-group	Only include dependencies from the specified dependency group	v
o	--all-groups	Include dependencies from all dependency groups	
o	--no-header	Exclude the comment header at the top of the generated output file	
o	--no-editable	Install any editable dependencies, including the project and any workspace members, as non-editable	
o	--no-hashes	Omit hashes in the generated output	
o	-o	Write the exported requirements to the given file	v
o	--no-emit-project	Do not emit the current project	
o	--no-emit-workspace	Do not emit any workspace members, including the root project	
o	--no-emit-package	Do not emit the given package(s)	v
o	--locked	Assert that the `uv.lock` will remain unchanged	v
o	--frozen	Do not update the `uv.lock` before exporting	v
o	--index	The URLs to use when resolving dependencies, in addition to the default index	v
o	--default-index	The URL of the default package index (by default: <https://pypi.org/simple>)	v
o	--index-url	The URL of the Python package index (by default: <https://pypi.org/simple>)	v
o	--extra-index-url	Extra URLs of package indexes to use, in addition to `--index-url`	v
o	--find-links	Locations to search for candidate distributions, in addition to those found in the registry indexes	v
o	--no-index	Ignore the registry index (e.g., PyPI), instead relying on direct URL dependencies and those…	
o	--index-strategy	The strategy to use when resolving against multiple index URLs	v
o	--keyring-provider	Attempt to use `keyring` for authentication for index URLs	v
o	-U	Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh`	
o	--upgrade-package	Allow upgrades for a specific package, ignoring pinned versions in any existing output file…	v
o	--resolution	The strategy to use when selecting between the different compatible versions for a given package…	v
o	--prerelease	The strategy to use when considering pre-release versions	v
o	--exclude-newer	Limit candidate packages to those that were uploaded prior to the given date	v
o	--no-sources	Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the…	
o	-C	Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs	v
o	--no-build-isolation	Disable isolation when building source distributions	v
o	--no-build-isolation-package	Disable isolation when building source distributions for a specific package	v
o	--no-build	Don't build source distributions	
o	--no-build-package	Don't build source distributions for a specific package	v
o	--no-binary	Don't install pre-built wheels	
o	--no-binary-package	Don't install pre-built wheels for a specific package	v
=	export	--index-strategy
v	first-index	
v	unsafe-first-match	
v	unsafe-best-match	
=	export	--keyring-provider
v	disabled	
v	subprocess	
=	export	--resolution
v	highest	
v	lowest	
v	lowest-direct	
=	export	--prerelease
v	disallow	
v	allow	
v	if-necessary	
v	explicit	
v	if-necessary-or-explicit	
@	tree
o	--universal	Show a platform-independent dependency tree	
o	-d	Maximum display depth of the dependency tree	v
o	--prune	Prune the given package from the display of the dependency tree	v
o	--package	Display only the specified packages	v
o	--no-dedupe	Do not de-duplicate repeated dependencies. Usually, when a package has already displayed its…	
o	--invert	Show the reverse dependencies for the given package. This flag will invert the tree and display…	
o	--outdated	Show the latest available version of each package in the tree	
o	--only-dev	Only include the development dependency group	
o	--no-dev	Omit the development dependency group	
o	--group	Include dependencies from the specified dependency group	v
o	--no-group	Exclude dependencies from the specified dependency group	v
o	--only-group	Only include dependencies from the specified dependency group	v
o	--all-groups	Include dependencies from all dependency groups	
o	--locked	Assert that the `uv.lock` will remain unchanged	v
o	--frozen	Display the requirements without locking the project	v
o	--python-version	The Python version to use when filtering the tree	v
o	--python-platform	The platform to use when filtering the tree	v
o	--index	The URLs to use when resolving dependencies, in addition to the default index	v
o	--default-index	The URL of the default package index (by default: <https://pypi.org/simple>)	v
o	--index-url	The URL of the Python package index (by default: <https://pypi.org/simple>)	v
o	--extra-index-url	Extra URLs of package indexes to use, in addition to `--index-url`	v
o	--find-links	Locations to search for candidate distributions, in addition to those found in the registry indexes	v
o	--no-index	Ignore the registry index (e.g., PyPI), instead relying on direct URL dependencies and those…	
o	--index-strategy	The strategy to use when resolving against multiple index URLs	v
o	--keyring-provider	Attempt to use `keyring` for authentication for index URLs	v
o	-U	Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh`	
o	--upgrade-package	Allow upgrades for a specific package, ignoring pinned versions in any existing output file…	v
o	--resolution	The strategy to use when selecting between the different compatible versions for a given package…	v
o	--prerelease	The strategy to use when considering pre-release versions	v
o	--exclude-newer	Limit candidate packages to those that were uploaded prior to the given date	v
o	--no-sources	Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the…	
o	--link-mode	The method to use when installing packages from the global cache	v
o	-p|--python	The Python interpreter to use to determine the minimum supported Python version	v
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--refresh	Refresh all cached data	
o	--refresh-package	Refresh cached data for a specific package	v
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
=	tree	--python-platform
v	windows	
v	linux	
v	macos	
v	x86_64-pc-windows-msvc	
v	i686-pc-windows-msvc	
v	x86_64-unknown-linux-gnu	
v	aarch64-apple-darwin	
v	x86_64-apple-darwin	
v	aarch64-unknown-linux-gnu	
v	aarch64-unknown-linux-musl	
v	x86_64-unknown-linux-musl	
v	x86_64-manylinux_2_17	
v	x86_64-manylinux_2_28	
v	x86_64-manylinux_2_31	
v	x86_64-manylinux_2_32	
v	x86_64-manylinux_2_33	
v	x86_64-manylinux_2_34	
v	x86_64-manylinux_2_35	
v	x86_64-manylinux_2_36	
v	x86_64-manylinux_2_37	
v	x86_64-manylinux_2_38	
v	x86_64-manylinux_2_39	
v	x86_64-manylinux_2_40	
v	aarch64-manylinux_2_17	
v	aarch64-manylinux_2_28	
v	aarch64-manylinux_2_31	
v	aarch64-manylinux_2_32	
v	aarch64-manylinux_2_33	
v	aarch64-manylinux_2_34	
v	aarch64-manylinux_2_35	
v	aarch64-manylinux_2_36	
v	aarch64-manylinux_2_37	
v	aarch64-manylinux_2_38	
v	aarch64-manylinux_2_39	
v	aarch64-manylinux_2_40	
=	tree	--index-strategy
v	first-index	
v	unsafe-first-match	
v	unsafe-best-match	
=	tree	--keyring-provider
v	disabled	
v	subprocess	
=	tree	--resolution
v	highest	
v	lowest	
v	lowest-direct	
=	tree	--prerelease
v	disallow	
v	allow	
v	if-necessary	
v	explicit	
v	if-necessary-or-explicit	
=	tree	--link-mode
v	clone	
v	copy	
v	hardlink	
v	symlink	
=	tree	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
@	tool
s	run	Run a command provided by a Python package
s	install	Install commands provided by a Python package
s	upgrade	Upgrade installed tools
s	list	List installed tools
s	uninstall	Uninstall a tool
s	update-shell	Ensure that the tool executable directory is on the `PATH`
s	dir	Show the path to the uv tools directory
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
=	tool	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
@	tool run
o	--from	Use the given package to provide the command	v
o	--with	Run with the given packages installed	v
o	--with-editable	Run with the given packages installed as editables	v
o	--with-requirements	Run with all packages listed in the given `requirements.txt` files	v
o	--isolated	Run the tool in an isolated virtual environment	
@	tool install
o	--editable	Install the package in editable mode	
o	--with	Include the following extra requirements	v
o	--with-editable	Include the given packages as editables	v
o	--with-requirements	Run all requirements listed in the given `requirements.txt` files	v
o	--isolated	Install the tool in an isolated virtual environment	
@	tool upgrade
o	--all	Upgrade all tools	
@	tool list
o	--show-paths	Whether to display the path to each tool environment and installed executable	
o	--show-version-specifiers	Whether to display the version specifier(s) used to install each tool	
@	tool uninstall
o	--all	Uninstall all tools	
@	tool update-shell
@	tool dir
o	--bin	Show the directory into which `uv tool` will install executables	
@	python
s	list	List the available Python installations
s	install	Download and install Python versions
s	find	Search for a Python installation
s	pin	Pin to a specific Python version
s	dir	Show the uv Python installation directory
s	uninstall	Uninstall Python versions
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
=	python	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
@	python list
o	--all-versions	List all Python versions, including old patch versions	
o	--all-platforms	List Python downloads for all platforms	
o	--only-installed	Only show installed Python versions, exclude available downloads	
@	python install
o	--mirror	Set the URL to use as the source for downloading Python installations	v
o	--pypy-mirror	Set the URL to use as the source for downloading PyPy installations	v
o	--reinstall	Reinstall the requested Python version, if it's already installed	
o	--force	Replace existing Python executables during installation	
o	--default	Use as the default Python version	
a	1	0
@	python find
o	--no-project	Avoid discovering the project or workspace	
o	--system	Only find system Python interpreters [env: UV_SYSTEM_PYTHON=]	
a	1	0
@	python pin
o	--resolved	Write the resolved Python interpreter path instead of the request	
o	--no-project	Avoid discovering the project or workspace	
a	1	0
@	python dir
o	--bin	Show the directory into which `uv python` will install Python executables	
@	python uninstall
o	--all	Uninstall all Python versions	
a	1	0
@	pip
s	compile	Compile a `requirements.in` file to a `requirements.txt` file
s	sync	Sync an environment with a `requirements.txt` file
s	install	Install packages into an environment
s	uninstall	Uninstall packages from an environment
s	freeze	List, in requirements format, packages installed in an environment
s	list	List, in tabular format, packages installed in an environment
s	show	Show information about one or more installed packages
s	tree	Display the dependency tree for an environment
s	check	Verify installed packages have compatible dependencies
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
=	pip	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
@	pip compile
@	pip sync
a	1	0
@	pip install
a	1	1
@	pip uninstall
a	1	1
@	pip freeze
@	pip list
@	pip show
a	1	1
@	pip tree
@	pip check
@	venv
o	-p|--python	The Python interpreter to use to determine the minimum supported Python version	v
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
o	--no-project	Avoid discovering a project or workspace	
o	--seed	Install seed packages (one or more of: `pip`, `setuptools`, and `wheel`) into the virtual…	
o	--allow-existing	Preserve any existing files or directories at the target path	
o	--prompt	Provide an alternative prompt prefix for the virtual environment	v
o	--system-site-packages	Give the virtual environment access to the system site packages directory	
o	--relocatable	Make the virtual environment relocatable	
o	--index-strategy	The strategy to use when resolving against multiple index URLs	v
o	--keyring-provider	Attempt to use `keyring` for authentication for index URLs	v
o	--exclude-newer	Limit candidate packages to those that were uploaded prior to the given date	v
o	--link-mode	The method to use when installing packages from the global cache	v
o	--index	The URLs to use when resolving dependencies, in addition to the default index	v
o	--default-index	The URL of the default package index (by default: <https://pypi.org/simple>)	v
o	--index-url	The URL of the Python package index (by default: <https://pypi.org/simple>)	v
o	--extra-index-url	Extra URLs of package indexes to use, in addition to `--index-url`	v
o	--find-links	Locations to search for candidate distributions, in addition to those found in the registry indexes	v
o	--no-index	Ignore the registry index (e.g., PyPI), instead relying on direct URL dependencies and those…	
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
=	venv	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
=	venv	--index-strategy
v	first-index	
v	unsafe-first-match	
v	unsafe-best-match	
=	venv	--keyring-provider
v	disabled	
v	subprocess	
=	venv	--link-mode
v	clone	
v	copy	
v	hardlink	
v	symlink	
@	build
o	--package	Build a specific package in the workspace	v
o	--all-packages	Build all packages in the workspace	
o	-o	The output directory to which distributions should be written	v
o	--sdist	Build a source distribution ('sdist') from the given directory	
o	--wheel	Build a binary distribution ('wheel') from the given directory	
o	--no-build-logs	Hide logs from the build backend	
o	--force-pep517	Always build through PEP 517, don't use the fast path for the uv build backend	
o	-b	Constrain build dependencies using the given requirements files when building distributions	v
o	--require-hashes	Require a matching hash for each requirement	
o	--no-verify-hashes	Disable validation of hashes in the requirements file	
o	-p|--python	The Python interpreter to use to determine the minimum supported Python version	v
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
o	--index	The URLs to use when resolving dependencies, in addition to the default index	v
o	--default-index	The URL of the default package index (by default: <https://pypi.org/simple>)	v
o	--index-url	The URL of the Python package index (by default: <https://pypi.org/simple>)	v
o	--extra-index-url	Extra URLs of package indexes to use, in addition to `--index-url`	v
o	--find-links	Locations to search for candidate distributions, in addition to those found in the registry indexes	v
o	--no-index	Ignore the registry index (e.g., PyPI), instead relying on direct URL dependencies and those…	
o	--index-strategy	The strategy to use when resolving against multiple index URLs	v
o	--keyring-provider	Attempt to use `keyring` for authentication for index URLs	v
o	-U	Allow package upgrades, ignoring pinned versions in any existing output file. Implies `--refresh`	
o	--upgrade-package	Allow upgrades for a specific package, ignoring pinned versions in any existing output file…	v
o	--resolution	The strategy to use when selecting between the different compatible versions for a given package…	v
o	--prerelease	The strategy to use when considering pre-release versions	v
o	--exclude-newer	Limit candidate packages to those that were uploaded prior to the given date	v
o	--no-sources	Ignore the `tool.uv.sources` table when resolving dependencies. Used to lock against the…	
o	-C	Settings to pass to the PEP 517 build backend, specified as `KEY=VALUE` pairs	v
o	--no-build-isolation	Disable isolation when building source distributions	v
o	--no-build-isolation-package	Disable isolation when building source distributions for a specific package	v
o	--no-build	Don't build source distributions	
o	--no-build-package	Don't build source distributions for a specific package	v
o	--no-binary	Don't install pre-built wheels	
o	--no-binary-package	Don't install pre-built wheels for a specific package	v
o	--link-mode	The method to use when installing packages from the global cache	v
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--refresh	Refresh all cached data	
o	--refresh-package	Refresh cached data for a specific package	v
a	1	0
=	build	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
=	build	--index-strategy
v	first-index	
v	unsafe-first-match	
v	unsafe-best-match	
=	build	--keyring-provider
v	disabled	
v	subprocess	
=	build	--resolution
v	highest	
v	lowest	
v	lowest-direct	
=	build	--prerelease
v	disallow	
v	allow	
v	if-necessary	
v	explicit	
v	if-necessary-or-explicit	
=	build	--link-mode
v	clone	
v	copy	
v	hardlink	
v	symlink	
@	publish
o	--publish-url	The URL of the upload endpoint (not the index URL)	v
o	-u	The username for the upload	v
o	-p	The password for the upload	v
o	-t	The token for the upload	v
o	--trusted-publishing	Configure using trusted publishing through GitHub Actions	v
o	--keyring-provider	Attempt to use `keyring` for authentication for remote requirements files	v
o	--check-url	Check an index URL for existing files to skip duplicate uploads	v
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
a	1	1
=	publish	--trusted-publishing
v	automatic	
v	always	
v	never	
=	publish	--keyring-provider
v	disabled	
v	subprocess	
=	publish	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
@	cache
s	clean	Clear the cache
s	prune	Prune all unreachable objects from the cache
s	dir	Show the cache directory
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
=	cache	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
@	cache clean
a	1	1
@	cache prune
@	cache dir
@	self
s	update	Update uv
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
=	self	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
@	self update
o	--token	A GitHub token for authentication. A token is not required but can be used to reduce the chance of…	
a	1	0
@	version
o	--output-format	The output format to use	v
o	--no-cache	Avoid reading from or writing to the cache, instead using a temporary directory for the duration…	
o	--cache-dir	Path to the cache directory	v
o	--python-preference	Whether to prefer uv-managed or system Python installations	v
o	--no-python-downloads	Disable automatic downloads of Python	
=	version	--output-format
v	text	
v	json	
=	version	--python-preference
v	only-managed	
v	managed	
v	system	
v	only-system	
@	help
o	--no-pager	Disable pager when printing help	
