@	
s	check	Run Ruff on the given files or directories
s	rule	Explain a rule (or all rules)
s	config	List or describe the available configuration options
s	linter	List all supported upstream linters
s	clean	Clear any caches in the current directory and any subdirectories
s	format	Run the Ruff formatter on the given files or directories
s	server	Run the language server
s	analyze	Run analysis over Python source code
s	version	Display Ruff's version
s	help	Print this message or the help of the given subcommand(s)
o	-v|--verbose	Enable verbose logging	p
o	-q|--quiet	Print diagnostics, but nothing else	p
o	-s|--silent	Disable all logging (but still exit with status code "1" upon detecting diagnostics)	p
o	--config	Path to the `pyproject.toml` or `ruff.toml` file to use for configuration	Vp
o	--isolated	Ignore all configuration files	p
o	--help	Print help	p
=		--config
t	filepaths
@	check
o	--fix	Apply fixes to resolve lint violations	
o	--unsafe-fixes	Include fixes that may not retain the original intent of the code	
o	--show-fixes	Show an enumeration of all fixed lint violations	
o	--diff	Avoid writing any fixed files back; instead, output a diff for each changed file to stdout, and…	
o	-w|--watch	Run in watch mode by re-running whenever files change	
o	--fix-only	Apply fixes to resolve lint violations, but don't report on, or exit non-zero for, leftover…	
o	--ignore-noqa	Ignore any `# noqa` comments	
o	--output-format	Output serialization format for violations. The default serialization format is 'full'	V
o	-o|--output-file	Specify file to write the linter output to (default: stdout)	V
o	--target-version	The minimum Python version that should be supported	V
o	--preview	Enable preview mode; checks will include unstable rules and fixes	
o	--extension	List of mappings from file extension to language (one of `python`, `ipynb`, `pyi`). For example…	V
o	--statistics	Show counts for every rule with at least one violation	
o	--add-noqa	Enable automatic additions of `noqa` directives to failing lines	
o	--show-files	See the files Ruff will be run against with the current settings	
o	--show-settings	See the settings Ruff will use to lint a given Python file	
o	-h|--help	Print help	
o	--select	Comma-separated list of rule codes to enable (or ALL, to enable all rules)	V
o	--ignore	Comma-separated list of rule codes to disable	V
o	--extend-select	Like --select, but adds additional rule codes on top of the selected ones	V
o	--per-file-ignores	List of mappings from file pattern to code to exclude	V
o	--extend-per-file-ignores	Like `--per-file-ignores`, but adds additional ignores on top of those already specified	V
o	--fixable	List of rule codes to treat as eligible for fix. Only applicable when fix itself is enabled (e.g…	V
o	--unfixable	List of rule codes to treat as ineligible for fix. Only applicable when fix itself is enabled…	V
o	--extend-fixable	Like --fixable, but adds additional rule codes on top of those already specified	V
o	--exclude	List of paths, used to omit files and/or directories from analysis	V
o	--extend-exclude	Like --exclude, but adds additional files and directories on top of those already excluded	V
o	--respect-gitignore	Respect file exclusions via `.gitignore` and other standard ignore files	
o	--force-exclude	Enforce exclusions, even for paths passed to Ruff directly on the command-line	
o	-n|--no-cache	Disable cache reads	
o	--cache-dir	Path to the cache directory	V
o	--stdin-filename	The name of the file when passing it through stdin	V
o	-e|--exit-zero	Exit with status code "0", even upon detecting lint violations	
o	--exit-non-zero-on-fix	Exit with a non-zero status code if any files were modified via fix, even if no lint violations…	
a	1	1
=	check	--output-format
v	concise	
v	full	
v	json	
v	json-lines	
v	junit	
v	grouped	
v	github	
v	gitlab	
v	pylint	
v	rdjson	
v	azure	
v	sarif	
=	check	-o
t	filepaths
=	check	--target-version
v	py37	
v	py38	
v	py39	
v	py310	
v	py311	
v	py312	
v	py313	
=	check	--cache-dir
t	filepaths
=	check	--stdin-filename
t	filepaths
#	check	1
t	filepaths
@	rule
o	--all	Explain all rules	
o	--output-format	Output format [default: text]	v
a	1	0
=	rule	--output-format
v	text	
v	json	
#	rule	1
v	F401	Unused-import
v	F402	Import-shadowed-by-loop-var
v	F403	Undefined-local-with-import-star
v	F404	Late-future-import
v	F405	Undefined-local-with-import-star-usage
v	F406	Undefined-local-with-nested-import-star-usage
v	F407	Future-feature-not-defined
v	F501	Percent-format-invalid-format
v	F502	Percent-format-expected-mapping
v	F503	Percent-format-expected-sequence
v	F504	Percent-format-extra-named-arguments
v	F505	Percent-format-missing-argument
v	F506	Percent-format-mixed-positional-and-named
v	F507	Percent-format-positional-count-mismatch
v	F508	Percent-format-star-requires-sequence
v	F509	Percent-format-unsupported-format-character
v	F521	String-dot-format-invalid-format
v	F522	String-dot-format-extra-named-arguments
v	F523	String-dot-format-extra-positional-arguments
v	F524	String-dot-format-missing-arguments
v	F525	String-dot-format-mixing-automatic
v	F541	F-string-missing-placeholders
v	F601	Multi-value-repeated-key-literal
v	F602	Multi-value-repeated-key-variable
v	F621	Expressions-in-star-assignment
v	F622	Multiple-starred-expressions
v	F631	Assert-tuple
v	F632	Is-literal
v	F633	Invalid-print-syntax
v	F634	If-tuple
v	F701	Break-outside-loop
v	F702	Continue-outside-loop
v	F704	Yield-outside-function
v	F706	Return-outside-function
v	F707	Default-except-not-last
v	F722	Forward-annotation-syntax-error
v	F811	Redefined-while-unused
v	F821	Undefined-name
v	F822	Undefined-export
v	F823	Undefined-local
v	F841	Unused-variable
v	F842	Unused-annotation
v	F901	Raise-not-implemented
v	E101	Mixed-spaces-and-tabs
v	E111	Indentation-with-invalid-multiple
v	E112	No-indented-block
v	E113	Unexpected-indentation
v	E114	Indentation-with-invalid-multiple-comment
v	E115	No-indented-block-comment
v	E116	Unexpected-indentation-comment
v	E117	Over-indented
v	E201	Whitespace-after-open-bracket
v	E202	Whitespace-before-close-bracket
v	E203	Whitespace-before-punctuation
v	E204	Whitespace-after-decorator
v	E211	Whitespace-before-parameters
v	E221	Multiple-spaces-before-operator
v	E222	Multiple-spaces-after-operator
v	E223	Tab-before-operator
v	E224	Tab-after-operator
v	E225	Missing-whitespace-around-operator
v	E226	Missing-whitespace-around-arithmetic-operator
v	E227	Missing-whitespace-around-bitwise-or-shift-operator
v	E228	Missing-whitespace-around-modulo-operator
v	E231	Missing-whitespace
v	E241	Multiple-spaces-after-comma
v	E242	Tab-after-comma
v	E251	Unexpected-spaces-around-keyword-parameter-equals
v	E252	Missing-whitespace-around-parameter-equals
v	E261	Too-few-spaces-before-inline-comment
v	E262	No-space-after-inline-comment
v	E265	No-space-after-block-comment
v	E266	Multiple-leading-hashes-for-block-comment
v	E271	Multiple-spaces-after-keyword
v	E272	Multiple-spaces-before-keyword
v	E273	Tab-after-keyword
v	E274	Tab-before-keyword
v	E275	Missing-whitespace-after-keyword
v	E301	Blank-line-between-methods
v	E302	Blank-lines-top-level
v	E303	Too-many-blank-lines
v	E304	Blank-line-after-decorator
v	E305	Blank-lines-after-function-or-class
v	E306	Blank-lines-before-nested-definition
v	E401	Multiple-imports-on-one-line
v	E402	Module-import-not-at-top-of-file
v	E501	Line-too-long
v	E502	Redundant-backslash
v	E701	Multiple-statements-on-one-line-colon
v	E702	Multiple-statements-on-one-line-semicolon
v	E703	Useless-semicolon
v	E711	None-comparison
v	E712	True-false-comparison
v	E713	Not-in-test
v	E714	Not-is-test
v	E721	Type-comparison
v	E722	Bare-except
v	E731	Lambda-assignment
v	E741	Ambiguous-variable-name
v	E742	Ambiguous-class-name
v	E743	Ambiguous-function-name
v	E902	Io-error
v	W191	Tab-indentation
v	W291	Trailing-whitespace
v	W292	Missing-newline-at-end-of-file
v	W293	Blank-line-with-whitespace
v	W391	Too-many-newlines-at-end-of-file
v	W505	Doc-line-too-long
v	W605	Invalid-escape-sequence
v	C901	Complex-structure
v	N801	Invalid-class-name
v	N802	Invalid-function-name
v	N803	Invalid-argument-name
v	N804	Invalid-first-argument-name-for-class-method
v	N805	Invalid-first-argument-name-for-method
v	N806	Non-lowercase-variable-in-function
v	N807	Dunder-function-name
v	N811	Constant-imported-as-non-constant
v	N812	Lowercase-imported-as-non-lowercase
v	N813	Camelcase-imported-as-lowercase
v	N814	Camelcase-imported-as-constant
v	N815	Mixed-case-variable-in-class-scope
v	N816	Mixed-case-variable-in-global-scope
v	N817	Camelcase-imported-as-acronym
v	N818	Error-suffix-on-exception-name
v	N999	Invalid-module-name
v	D100	Undocumented-public-module
v	D101	Undocumented-public-class
v	D102	Undocumented-public-method
v	D103	Undocumented-public-function
v	D104	Undocumented-public-package
v	D105	Undocumented-magic-method
v	D106	Undocumented-public-nested-class
v	D107	Undocumented-public-init
v	D200	Fits-on-one-line
v	D201	No-blank-line-before-function
v	D202	No-blank-line-after-function
v	D203	One-blank-line-before-class
v	D204	One-blank-line-after-class
v	D205	Blank-line-after-summary
v	D206	Indent-with-spaces
v	D207	Under-indentation
v	D208	Over-indentation
v	D209	New-line-after-last-paragraph
v	D210	Surrounding-whitespace
v	D211	Blank-line-before-class
v	D212	Multi-line-summary-first-line
v	D213	Multi-line-summary-second-line
v	D214	Section-not-over-indented
v	D215	Section-underline-not-over-indented
v	D300	Triple-single-quotes
v	D301	Escape-sequence-in-docstring
v	D400	Ends-in-period
v	D401	Non-imperative-mood
v	D402	No-signature
v	D403	First-line-capitalized
v	D404	Docstring-starts-with-this
v	D405	Capitalize-section-name
v	D406	New-line-after-section-name
v	D407	Dashed-underline-after-section
v	D408	Section-underline-after-name
v	D409	Section-underline-matches-section-length
v	D410	No-blank-line-after-section
v	D411	No-blank-line-before-section
v	D412	Blank-lines-between-header-and-content
v	D413	Blank-line-after-last-section
v	D414	Empty-docstring-section
v	D415	Ends-in-punctuation
v	D416	Section-name-ends-in-colon
v	D417	Undocumented-param
v	D418	Overload-with-docstring
v	D419	Empty-docstring
v	I001	Unsorted-imports
v	I002	Missing-required-import
v	UP001	Useless-metaclass-type
v	UP003	Type-of-primitive
v	UP004	Useless-object-inheritance
v	UP005	Deprecated-unittest-alias
v	UP006	Non-pep585-annotation
v	UP007	Non-pep604-annotation
v	UP008	Super-call-with-parameters
v	UP009	Utf8-encoding-declaration
v	UP010	Unnecessary-future-import
v	UP011	Lru-cache-without-parameters
v	UP012	Unnecessary-encode-utf8
v	UP013	Convert-typed-dict-functional-to-class
v	UP014	Convert-named-tuple-functional-to-class
v	UP015	Redundant-open-modes
v	UP017	Datetime-timezone-utc
v	UP018	Native-literals
v	UP019	Typing-text-str-alias
v	UP020	Open-alias
v	UP021	Replace-universal-newlines
v	UP022	Replace-stdout-stderr
v	UP023	Deprecated-c-element-tree
v	UP024	Os-error-alias
v	UP025	Unicode-kind-prefix
v	UP026	Deprecated-mock-import
v	UP027	Unpacked-list-comprehension
v	UP028	Yield-in-for-loop
v	UP029	Unnecessary-builtin-import
v	UP030	Format-literals
v	UP031	Printf-string-formatting
v	UP032	F-string
v	UP033	Lru-cache-with-maxsize-none
v	UP034	Extraneous-parentheses
v	UP035	Deprecated-import
v	UP036	Outdated-version-block
v	UP037	Quoted-annotation
v	UP038	Non-pep604-isinstance
v	UP039	Unnecessary-class-parentheses
v	UP040	Non-pep695-type-alias
v	UP041	Timeout-error-alias
v	UP042	Replace-str-enum
v	UP043	Unnecessary-default-type-args
v	UP044	Non-pep646-unpack
v	YTT101	Sys-version-slice3
v	YTT102	Sys-version2
v	YTT103	Sys-version-cmp-str3
v	YTT201	Sys-version-info0-eq3
v	YTT202	Six-py3
v	YTT203	Sys-version-info1-cmp-int
v	YTT204	Sys-version-info-minor-cmp-int
v	YTT301	Sys-version0
v	YTT302	Sys-version-cmp-str10
v	YTT303	Sys-version-slice1
v	ANN001	Missing-type-function-argument
v	ANN002	Missing-type-args
v	ANN003	Missing-type-kwargs
v	ANN201	Missing-return-type-undocumented-public-function
v	ANN202	Missing-return-type-private-function
v	ANN204	Missing-return-type-special-method
v	ANN205	Missing-return-type-static-method
v	ANN206	Missing-return-type-class-method
v	ANN401	Any-type
v	ASYNC100	Cancel-scope-no-checkpoint
v	ASYNC105	Trio-sync-call
v	ASYNC109	Async-function-with-timeout
v	ASYNC110	Async-busy-wait
v	ASYNC115	Async-zero-sleep
v	ASYNC116	Long-sleep-not-forever
v	ASYNC210	Blocking-http-call-in-async-function
v	ASYNC220	Create-subprocess-in-async-function
v	ASYNC221	Run-process-in-async-function
v	ASYNC222	Wait-for-process-in-async-function
v	ASYNC230	Blocking-open-call-in-async-function
v	ASYNC251	Blocking-sleep-in-async-function
v	S101	Assert
v	S102	Exec-builtin
v	S103	Bad-file-permissions
v	S104	Hardcoded-bind-all-interfaces
v	S105	Hardcoded-password-string
v	S106	Hardcoded-password-func-arg
v	S107	Hardcoded-password-default
v	S108	Hardcoded-temp-file
v	S110	Try-except-pass
v	S112	Try-except-continue
v	S113	Request-without-timeout
v	S201	Flask-debug-true
v	S202	Tarfile-unsafe-members
v	S301	Suspicious-pickle-usage
v	S302	Suspicious-marshal-usage
v	S303	Suspicious-insecure-hash-usage
v	S304	Suspicious-insecure-cipher-usage
v	S305	Suspicious-insecure-cipher-mode-usage
v	S306	Suspicious-mktemp-usage
v	S307	Suspicious-eval-usage
v	S308	Suspicious-mark-safe-usage
v	S310	Suspicious-url-open-usage
v	S311	Suspicious-non-cryptographic-random-usage
v	S312	Suspicious-telnet-usage
v	S313	Suspicious-xmlc-element-tree-usage
v	S314	Suspicious-xml-element-tree-usage
v	S315	Suspicious-xml-expat-reader-usage
v	S316	Suspicious-xml-expat-builder-usage
v	S317	Suspicious-xml-sax-usage
v	S318	Suspicious-xml-mini-dom-usage
v	S319	Suspicious-xml-pull-dom-usage
v	S320	Suspicious-xmle-tree-usage
v	S321	Suspicious-ftp-lib-usage
v	S323	Suspicious-unverified-context-usage
v	S324	Hashlib-insecure-hash-function
v	S401	Suspicious-telnetlib-import
v	S402	Suspicious-ftplib-import
v	S403	Suspicious-pickle-import
v	S404	Suspicious-subprocess-import
v	S405	Suspicious-xml-etree-import
v	S406	Suspicious-xml-sax-import
v	S407	Suspicious-xml-expat-import
v	S408	Suspicious-xml-minidom-import
v	S409	Suspicious-xml-pulldom-import
v	S410	Suspicious-lxml-import
v	S411	Suspicious-xmlrpc-import
v	S412	Suspicious-httpoxy-import
v	S413	Suspicious-pycrypto-import
v	S415	Suspicious-pyghmi-import
v	S501	Request-with-no-cert-validation
v	S502	Ssl-insecure-version
v	S503	Ssl-with-bad-defaults
v	S504	Ssl-with-no-version
v	S505	Weak-cryptographic-key
v	S506	Unsafe-yaml-load
v	S507	Ssh-no-host-key-verification
v	S508	Snmp-insecure-version
v	S509	Snmp-weak-cryptography
v	S601	Paramiko-call
v	S602	Subprocess-popen-with-shell-equals-true
v	S603	Subprocess-without-shell-equals-true
v	S604	Call-with-shell-equals-true
v	S605	Start-process-with-a-shell
v	S606	Start-process-with-no-shell
v	S607	Start-process-with-partial-path
v	S608	Hardcoded-sql-expression
v	S609	Unix-command-wildcard-injection
v	S610	Django-extra
v	S611	Django-raw-sql
v	S612	Logging-config-insecure-listen
v	S701	Jinja2-autoescape-false
v	S702	Mako-templates
v	BLE001	Do not catch blind exception
v	B002	Unary-prefix-increment-decrement
v	B003	Assignment-to-os-environ
v	B004	Unreliable-callable-check
v	B005	Strip-with-multi-characters
v	B006	Mutable-argument-default
v	B007	Unused-loop-control-variable
v	B008	Function-call-in-default-argument
v	B009	Get-attr-with-constant
v	B010	Set-attr-with-constant
v	B011	Assert-false
v	B012	Jump-statement-in-finally
v	B013	Redundant-tuple-in-exception-handler
v	B014	Duplicate-handler-exception
v	B015	Useless-comparison
v	B016	Raise-literal
v	B017	Assert-raises-exception
v	B018	Useless-expression
v	B019	Cached-instance-method
v	B020	Loop-variable-overrides-iterator
v	B021	F-string-docstring
v	B022	Useless-contextlib-suppress
v	B023	Function-uses-loop-variable
v	B024	Abstract-base-class-without-abstract-method
v	B025	Duplicate-try-block-exception
v	B026	Star-arg-unpacking-after-keyword-arg
v	B027	Empty-method-without-abstract-decorator
v	B028	No-explicit-stacklevel
v	B029	Except-with-empty-tuple
v	B030	Except-with-non-exception-classes
v	B031	Reuse-of-groupby-generator
v	B032	Unintentional-type-annotation
v	B033	Duplicate-value
v	B034	Re-sub-positional-args
v	B035	Static-key-dict-comprehension
v	B039	Mutable-contextvar-default
v	B901	Return-in-generator
v	B904	Raise-without-from-inside-except
v	B905	Zip-without-explicit-strict
v	B909	Loop-iterator-mutation
v	FBT001	Boolean-typed positional argument in function definition
v	FBT002	Boolean default positional argument in function definition
v	FBT003	Boolean positional value in function call
v	A001	Builtin-variable-shadowing
v	A002	Builtin-argument-shadowing
v	A003	Builtin-attribute-shadowing
v	A004	Builtin-import-shadowing
v	A005	Builtin-module-shadowing
v	A006	Builtin-lambda-argument-shadowing
v	COM812	Missing-trailing-comma
v	COM818	Trailing-comma-on-bare-tuple
v	COM819	Prohibited-trailing-comma
v	CPY001	Missing-copyright-notice
v	C400	Unnecessary-generator-list
v	C401	Unnecessary-generator-set
v	C402	Unnecessary-generator-dict
v	C403	Unnecessary-list-comprehension-set
v	C404	Unnecessary-list-comprehension-dict
v	C405	Unnecessary-literal-set
v	C406	Unnecessary-literal-dict
v	C408	Unnecessary-collection-call
v	C409	Unnecessary-literal-within-tuple-call
v	C410	Unnecessary-literal-within-list-call
v	C411	Unnecessary-list-call
v	C413	Unnecessary-call-around-sorted
v	C414	Unnecessary-double-cast-or-process
v	C415	Unnecessary-subscript-reversal
v	C416	Unnecessary-comprehension
v	C417	Unnecessary-map
v	C418	Unnecessary-literal-within-dict-call
v	C419	Unnecessary-comprehension-in-call
v	C420	Unnecessary-dict-comprehension-for-iterable
v	DTZ001	Call-datetime-without-tzinfo
v	DTZ002	Call-datetime-today
v	DTZ003	Call-datetime-utcnow
v	DTZ004	Call-datetime-utcfromtimestamp
v	DTZ005	Call-datetime-now-without-tzinfo
v	DTZ006	Call-datetime-fromtimestamp
v	DTZ007	Call-datetime-strptime-without-zone
v	DTZ011	Call-date-today
v	DTZ012	Call-date-fromtimestamp
v	DTZ901	Datetime-min-max
v	DJ001	Django-nullable-model-string-field
v	DJ003	Django-locals-in-render-function
v	DJ006	Django-exclude-with-model-form
v	DJ007	Django-all-with-model-form
v	DJ008	Django-model-without-dunder-str
v	DJ012	Django-unordered-body-content-in-model
v	DJ013	Django-non-leading-receiver-decorator
v	EM101	Raw-string-in-exception
v	EM102	F-string-in-exception
v	EM103	Dot-format-in-exception
v	EXE001	Shebang-not-executable
v	EXE002	Shebang-missing-executable-file
v	EXE003	Shebang-missing-python
v	EXE004	Shebang-leading-whitespace
v	EXE005	Shebang-not-first-line
v	FA100	Future-rewritable-type-annotation
v	FA102	Future-required-type-annotation
v	ISC001	Single-line-implicit-string-concatenation
v	ISC002	Multi-line-implicit-string-concatenation
v	ISC003	Explicit-string-concatenation
v	ICN001	Unconventional-import-alias
v	ICN002	Banned-import-alias
v	ICN003	Banned-import-from
v	LOG001	Direct-logger-instantiation
v	LOG002	Invalid-get-logger-argument
v	LOG007	Exception-without-exc-info
v	LOG009	Undocumented-warn
v	LOG015	Root-logger-call
v	G001	Logging-string-format
v	G002	Logging-percent-format
v	G003	Logging-string-concat
v	G004	Logging-f-string
v	G010	Logging-warn
v	G101	Logging-extra-attr-clash
v	G201	Logging-exc-info
v	G202	Logging-redundant-exc-info
v	INP001	Implicit-namespace-package
v	PIE790	Unnecessary-placeholder
v	PIE794	Duplicate-class-field-definition
v	PIE796	Non-unique-enums
v	PIE800	Unnecessary-spread
v	PIE804	Unnecessary-dict-kwargs
v	PIE807	Reimplemented-container-builtin
v	PIE808	Unnecessary-range-start
v	PIE810	Multiple-starts-ends-with
v	T201	Print
v	T203	P-print
v	PYI001	Unprefixed-type-param
v	PYI002	Complex-if-statement-in-stub
v	PYI003	Unrecognized-version-info-check
v	PYI004	Patch-version-comparison
v	PYI005	Wrong-tuple-length-version-comparison
v	PYI006	Bad-version-info-comparison
v	PYI007	Unrecognized-platform-check
v	PYI008	Unrecognized-platform-name
v	PYI009	Pass-statement-stub-body
v	PYI010	Non-empty-stub-body
v	PYI011	Typed-argument-default-in-stub
v	PYI012	Pass-in-class-body
v	PYI013	Ellipsis-in-non-empty-class-body
v	PYI014	Argument-default-in-stub
v	PYI015	Assignment-default-in-stub
v	PYI016	Duplicate-union-member
v	PYI017	Complex-assignment-in-stub
v	PYI018	Unused-private-type-var
v	PYI019	Custom-type-var-return-type
v	PYI020	Quoted-annotation-in-stub
v	PYI021	Docstring-in-stub
v	PYI024	Collections-named-tuple
v	PYI025	Unaliased-collections-abc-set-import
v	PYI026	Type-alias-without-annotation
v	PYI029	Str-or-repr-defined-in-stub
v	PYI030	Unnecessary-literal-union
v	PYI032	Any-eq-ne-annotation
v	PYI033	Type-comment-in-stub
v	PYI034	Non-self-return-type
v	PYI035	Unassigned-special-variable-in-stub
v	PYI036	Bad-exit-annotation
v	PYI041	Redundant-numeric-union
v	PYI042	Snake-case-type-alias
v	PYI043	T-suffixed-type-alias
v	PYI044	Future-annotations-in-stub
v	PYI045	Iter-method-return-iterable
v	PYI046	Unused-private-protocol
v	PYI047	Unused-private-type-alias
v	PYI048	Stub-body-multiple-statements
v	PYI049	Unused-private-typed-dict
v	PYI050	No-return-argument-annotation-in-stub
v	PYI051	Redundant-literal-union
v	PYI052	Unannotated-assignment-in-stub
v	PYI053	String-or-bytes-too-long
v	PYI054	Numeric-literal-too-long
v	PYI055	Unnecessary-type-union
v	PYI056	Unsupported-method-call-on-all
v	PYI057	Byte-string-usage
v	PYI058	Generator-return-from-iter-method
v	PYI059	Generic-not-last-base-class
v	PYI061	Redundant-none-literal
v	PYI062	Duplicate-literal-member
v	PYI063	Pep484-style-positional-only-parameter
v	PYI064	Redundant-final-literal
v	PYI066	Bad-version-info-order
v	PT001	Pytest-fixture-incorrect-parentheses-style
v	PT002	Pytest-fixture-positional-args
v	PT003	Pytest-extraneous-scope-function
v	PT004	Pytest-missing-fixture-name-underscore
v	PT005	Pytest-incorrect-fixture-name-underscore
v	PT006	Pytest-parametrize-names-wrong-type
v	PT007	Pytest-parametrize-values-wrong-type
v	PT008	Pytest-patch-with-lambda
v	PT009	Pytest-unittest-assertion
v	PT010	Pytest-raises-without-exception
v	PT011	Pytest-raises-too-broad
v	PT012	Pytest-raises-with-multiple-statements
v	PT013	Pytest-incorrect-pytest-import
v	PT014	Pytest-duplicate-parametrize-test-cases
v	PT015	Pytest-assert-always-false
v	PT016	Pytest-fail-without-message
v	PT017	Pytest-assert-in-except
v	PT018	Pytest-composite-assertion
v	PT019	Pytest-fixture-param-without-value
v	PT020	Pytest-deprecated-yield-fixture
v	PT021	Pytest-fixture-finalizer-callback
v	PT022	Pytest-useless-yield-fixture
v	PT023	Pytest-incorrect-mark-parentheses-style
v	PT024	Pytest-unnecessary-asyncio-mark-on-fixture
v	PT025	Pytest-erroneous-use-fixtures-on-fixture
v	PT026	Pytest-use-fixtures-without-parameters
v	PT027	Pytest-unittest-raises-assertion
v	Q000	Bad-quotes-inline-string
v	Q001	Bad-quotes-multiline-string
v	Q002	Bad-quotes-docstring
v	Q003	Avoidable-escaped-quote
v	Q004	Unnecessary-escaped-quote
v	RSE102	Unnecessary-paren-on-raise-exception
v	RET501	Unnecessary-return-none
v	RET502	Implicit-return-value
v	RET503	Implicit-return
v	RET504	Unnecessary-assign
v	RET505	Superfluous-else-return
v	RET506	Superfluous-else-raise
v	RET507	Superfluous-else-continue
v	RET508	Superfluous-else-break
v	SLF001	Private-member-access
v	SLOT000	No-slots-in-str-subclass
v	SLOT001	No-slots-in-tuple-subclass
v	SLOT002	No-slots-in-namedtuple-subclass
v	SIM101	Duplicate-isinstance-call
v	SIM102	Collapsible-if
v	SIM103	Needless-bool
v	SIM105	Suppressible-exception
v	SIM107	Return-in-try-except-finally
v	SIM108	If-else-block-instead-of-if-exp
v	SIM109	Compare-with-tuple
v	SIM110	Reimplemented-builtin
v	SIM112	Uncapitalized-environment-variables
v	SIM113	Enumerate-for-loop
v	SIM114	If-with-same-arms
v	SIM115	Open-file-with-context-handler
v	SIM116	If-else-block-instead-of-dict-lookup
v	SIM117	Multiple-with-statements
v	SIM118	In-dict-keys
v	SIM201	Negate-equal-op
v	SIM202	Negate-not-equal-op
v	SIM208	Double-negation
v	SIM210	If-expr-with-true-false
v	SIM211	If-expr-with-false-true
v	SIM212	If-expr-with-twisted-arms
v	SIM220	Expr-and-not-expr
v	SIM221	Expr-or-not-expr
v	SIM222	Expr-or-true
v	SIM223	Expr-and-false
v	SIM300	Yoda-conditions
v	SIM401	If-else-block-instead-of-dict-get
v	SIM905	Split-static-string
v	SIM910	Dict-get-with-none-default
v	SIM911	Zip-dict-keys-and-values
v	TID251	Banned-api
v	TID252	Relative-imports
v	TID253	Banned-module-level-imports
v	TC001	Typing-only-first-party-import
v	TC002	Typing-only-third-party-import
v	TC003	Typing-only-standard-library-import
v	TC004	Runtime-import-in-type-checking-block
v	TC005	Empty-type-checking-block
v	TC006	Runtime-cast-value
v	TC007	Unquoted-type-alias
v	TC008	Quoted-type-alias
v	TC010	Runtime-string-union
v	INT001	F-string-in-get-text-func-call
v	INT002	Format-in-get-text-func-call
v	INT003	Printf-in-get-text-func-call
v	ARG001	Unused-function-argument
v	ARG002	Unused-method-argument
v	ARG003	Unused-class-method-argument
v	ARG004	Unused-static-method-argument
v	ARG005	Unused-lambda-argument
v	PTH100	Os-path-abspath
v	PTH101	Os-chmod
v	PTH102	Os-mkdir
v	PTH103	Os-makedirs
v	PTH104	Os-rename
v	PTH105	Os-replace
v	PTH106	Os-rmdir
v	PTH107	Os-remove
v	PTH108	Os-unlink
v	PTH109	Os-getcwd
v	PTH110	Os-path-exists
v	PTH111	Os-path-expanduser
v	PTH112	Os-path-isdir
v	PTH113	Os-path-isfile
v	PTH114	Os-path-islink
v	PTH115	Os-readlink
v	PTH116	Os-stat
v	PTH117	Os-path-isabs
v	PTH118	Os-path-join
v	PTH119	Os-path-basename
v	PTH120	Os-path-dirname
v	PTH121	Os-path-samefile
v	PTH122	Os-path-splitext
v	PTH123	Builtin-open
v	PTH124	Py-path
v	PTH201	Path-constructor-current-directory
v	PTH202	Os-path-getsize
v	PTH203	Os-path-getatime
v	PTH204	Os-path-getmtime
v	PTH205	Os-path-getctime
v	PTH206	Os-sep-split
v	PTH207	Glob
v	PTH208	Os-listdir
v	TD001	Invalid-todo-tag
v	TD002	Missing-todo-author
v	TD003	Missing-todo-link
v	TD004	Missing-todo-colon
v	TD005	Missing-todo-description
v	TD006	Invalid-todo-capitalization
v	TD007	Missing-space-after-todo-colon
v	FIX001	Line-contains-fixme
v	FIX002	Line-contains-todo
v	FIX003	Line-contains-xxx
v	FIX004	Line-contains-hack
v	ERA001	Commented-out-code
v	PD002	Pandas-use-of-inplace-argument
v	PD003	Pandas-use-of-dot-is-null
v	PD004	Pandas-use-of-dot-not-null
v	PD007	Pandas-use-of-dot-ix
v	PD008	Pandas-use-of-dot-at
v	PD009	Pandas-use-of-dot-iat
v	PD010	Pandas-use-of-dot-pivot-or-unstack
v	PD011	Pandas-use-of-dot-values
v	PD012	Pandas-use-of-dot-read-table
v	PD013	Pandas-use-of-dot-stack
v	PD015	Pandas-use-of-pd-merge
v	PD101	Pandas-nunique-constant-series-check
v	PD901	Pandas-df-variable-name
v	PGH001	Eval
v	PGH002	Deprecated-log-warn
v	PGH003	Blanket-type-ignore
v	PGH004	Blanket-noqa
v	PGH005	Invalid-mock-access
v	PLC0105	Type-name-incorrect-variance
v	PLC0131	Type-bivariance
v	PLC0132	Type-param-name-mismatch
v	PLC0205	Single-string-slots
v	PLC0206	Dict-index-missing-items
v	PLC0208	Iteration-over-set
v	PLC0414	Useless-import-alias
v	PLC0415	Import-outside-top-level
v	PLC1802	Len-test
v	PLC1901	Compare-to-empty-string
v	PLC2401	Non-ascii-name
v	PLC2403	Non-ascii-import-name
v	PLC2701	Import-private-name
v	PLC2801	Unnecessary-dunder-call
v	PLC3002	Unnecessary-direct-lambda-call
v	PLE0100	Yield-in-init
v	PLE0101	Return-in-init
v	PLE0115	Nonlocal-and-global
v	PLE0116	Continue-in-finally
v	PLE0117	Nonlocal-without-binding
v	PLE0118	Load-before-global-declaration
v	PLE0237	Non-slot-assignment
v	PLE0241	Duplicate-bases
v	PLE0302	Unexpected-special-method-signature
v	PLE0303	Invalid-length-return-type
v	PLE0304	Invalid-bool-return-type
v	PLE0305	Invalid-index-return-type
v	PLE0307	Invalid-str-return-type
v	PLE0308	Invalid-bytes-return-type
v	PLE0309	Invalid-hash-return-type
v	PLE0604	Invalid-all-object
v	PLE0605	Invalid-all-format
v	PLE0643	Potential-index-error
v	PLE0704	Misplaced-bare-raise
v	PLE1132	Repeated-keyword-argument
v	PLE1141	Dict-iter-missing-items
v	PLE1142	Await-outside-async
v	PLE1205	Logging-too-many-args
v	PLE1206	Logging-too-few-args
v	PLE1300	Bad-string-format-character
v	PLE1307	Bad-string-format-type
v	PLE1310	Bad-str-strip-call
v	PLE1507	Invalid-envvar-value
v	PLE1519	Singledispatch-method
v	PLE1520	Singledispatchmethod-function
v	PLE1700	Yield-from-in-async-function
v	PLE2502	Bidirectional-unicode
v	PLE2510	Invalid-character-backspace
v	PLE2512	Invalid-character-sub
v	PLE2513	Invalid-character-esc
v	PLE2514	Invalid-character-nul
v	PLE2515	Invalid-character-zero-width-space
v	PLE4703	Modified-iterating-set
v	PLR0124	Comparison-with-itself
v	PLR0133	Comparison-of-constant
v	PLR0202	No-classmethod-decorator
v	PLR0203	No-staticmethod-decorator
v	PLR0206	Property-with-parameters
v	PLR0402	Manual-from-import
v	PLR0904	Too-many-public-methods
v	PLR0911	Too-many-return-statements
v	PLR0912	Too-many-branches
v	PLR0913	Too-many-arguments
v	PLR0914	Too-many-locals
v	PLR0915	Too-many-statements
v	PLR0916	Too-many-boolean-expressions
v	PLR0917	Too-many-positional-arguments
v	PLR1701	Repeated-isinstance-calls
v	PLR1702	Too-many-nested-blocks
v	PLR1704	Redefined-argument-from-local
v	PLR1706	And-or-ternary
v	PLR1711	Useless-return
v	PLR1714	Repeated-equality-comparison
v	PLR1716	Boolean-chained-comparison
v	PLR1722	Sys-exit-alias
v	PLR1730	If-stmt-min-max
v	PLR1733	Unnecessary-dict-index-lookup
v	PLR1736	Unnecessary-list-index-lookup
v	PLR2004	Magic-value-comparison
v	PLR2044	Empty-comment
v	PLR5501	Collapsible-else-if
v	PLR6104	Non-augmented-assignment
v	PLR6201	Literal-membership
v	PLR6301	No-self-use
v	PLW0108	Unnecessary-lambda
v	PLW0120	Useless-else-on-loop
v	PLW0127	Self-assigning-variable
v	PLW0128	Redeclared-assigned-name
v	PLW0129	Assert-on-string-literal
v	PLW0131	Named-expr-without-context
v	PLW0133	Useless-exception-statement
v	PLW0177	Nan-comparison
v	PLW0211	Bad-staticmethod-argument
v	PLW0245	Super-without-brackets
v	PLW0406	Import-self
v	PLW0602	Global-variable-not-assigned
v	PLW0603	Global-statement
v	PLW0604	Global-at-module-level
v	PLW0642	Self-or-cls-assignment
v	PLW0711	Binary-op-exception
v	PLW1501	Bad-open-mode
v	PLW1507	Shallow-copy-environ
v	PLW1508	Invalid-envvar-default
v	PLW1509	Subprocess-popen-preexec-fn
v	PLW1510	Subprocess-run-without-check
v	PLW1514	Unspecified-encoding
v	PLW1641	Eq-without-hash
v	PLW2101	Useless-with-lock
v	PLW2901	Redefined-loop-name
v	PLW3201	Bad-dunder-method-name
v	PLW3301	Nested-min-max
v	TRY002	Raise-vanilla-class
v	TRY003	Raise-vanilla-args
v	TRY004	Type-check-without-type-error
v	TRY200	Reraise-no-cause
v	TRY201	Verbose-raise
v	TRY203	Useless-try-except
v	TRY300	Try-consider-else
v	TRY301	Raise-within-try
v	TRY400	Error-instead-of-exception
v	TRY401	Verbose-log-message
v	FLY002	Static-join-to-f-string
v	NPY001	Numpy-deprecated-type-alias
v	NPY002	Numpy-legacy-random
v	NPY003	Numpy-deprecated-function
v	NPY201	Numpy2-deprecation
v	FAST001	Fast-api-redundant-response-model
v	FAST002	Fast-api-non-annotated-dependency
v	FAST003	Fast-api-unused-path-parameter
v	AIR001	Airflow-variable-name-task-id-mismatch
v	AIR301	Airflow-dag-no-schedule-argument
v	AIR302	Airflow3-removal
v	PERF101	Unnecessary-list-cast
v	PERF102	Incorrect-dict-iterator
v	PERF203	Try-except-in-loop
v	PERF401	Manual-list-comprehension
v	PERF402	Manual-list-copy
v	PERF403	Manual-dict-comprehension
v	FURB101	Read-whole-file
v	FURB103	Write-whole-file
v	FURB105	Print-empty-string
v	FURB110	If-exp-instead-of-or-operator
v	FURB113	Repeated-append
v	FURB116	F-string-number-format
v	FURB118	Reimplemented-operator
v	FURB129	Readlines-in-for
v	FURB131	Delete-full-slice
v	FURB132	Check-and-remove-from-set
v	FURB136	If-expr-min-max
v	FURB140	Reimplemented-starmap
v	FURB142	For-loop-set-mutations
v	FURB145	Slice-copy
v	FURB148	Unnecessary-enumerate
v	FURB152	Math-constant
v	FURB154	Repeated-global
v	FURB156	Hardcoded-string-charset
v	FURB157	Verbose-decimal-constructor
v	FURB161	Bit-count
v	FURB163	Redundant-log-base
v	FURB164	Unnecessary-from-float
v	FURB166	Int-on-sliced-str
v	FURB167	Regex-flag-alias
v	FURB168	Isinstance-type-none
v	FURB169	Type-none-comparison
v	FURB171	Single-item-membership-test
v	FURB177	Implicit-cwd
v	FURB180	Meta-class-abc-meta
v	FURB181	Hashlib-digest-hex
v	FURB187	List-reverse-copy
v	FURB188	Slice-to-remove-prefix-or-suffix
v	FURB189	Subclass-builtin
v	FURB192	Sorted-min-max
v	DOC201	Docstring-missing-returns
v	DOC202	Docstring-extraneous-returns
v	DOC402	Docstring-missing-yields
v	DOC403	Docstring-extraneous-yields
v	DOC501	Docstring-missing-exception
v	DOC502	Docstring-extraneous-exception
v	RUF001	Ambiguous-unicode-character-string
v	RUF002	Ambiguous-unicode-character-docstring
v	RUF003	Ambiguous-unicode-character-comment
v	RUF005	Collection-literal-concatenation
v	RUF006	Asyncio-dangling-task
v	RUF007	Zip-instead-of-pairwise
v	RUF008	Mutable-dataclass-default
v	RUF009	Function-call-in-dataclass-default-argument
v	RUF010	Explicit-f-string-type-conversion
v	RUF011	Ruff-static-key-dict-comprehension
v	RUF012	Mutable-class-default
v	RUF013	Implicit-optional
v	RUF015	Unnecessary-iterable-allocation-for-first-element
v	RUF016	Invalid-index-type
v	RUF017	Quadratic-list-summation
v	RUF018	Assignment-in-assert
v	RUF019	Unnecessary-key-check
v	RUF020	Never-union
v	RUF021	Parenthesize-chained-operators
v	RUF022	Unsorted-dunder-all
v	RUF023	Unsorted-dunder-slots
v	RUF024	Mutable-fromkeys-value
v	RUF026	Default-factory-kwarg
v	RUF027	Missing-f-string-syntax
v	RUF028	Invalid-formatter-suppression-comment
v	RUF029	Unused-async
v	RUF030	Assert-with-print-message
v	RUF031	Incorrectly-parenthesized-tuple-in-subscript
v	RUF032	Decimal-from-float-literal
v	RUF033	Post-init-default
v	RUF034	Useless-if-else
v	RUF035	Unsafe-markup-use
v	RUF036	None-not-at-end-of-union
v	RUF038	Redundant-bool-literal
v	RUF039	Unraw-re-pattern
v	RUF040	Invalid-assert-message-literal-argument
v	RUF041	Unnecessary-nested-literal
v	RUF046	Unnecessary-cast-to-int
v	RUF048	Map-int-version-parsing
v	RUF052	Used-dummy-variable
v	RUF055	Unnecessary-regular-expression
v	RUF100	Unused-noqa
v	RUF101	Redirected-noqa
v	RUF200	Invalid-pyproject-toml
v	--all	Explain all rules
@	config
o	--output-format	Output format [default: text]	v
=	config	--output-format
v	text	
v	json	
@	linter
o	--output-format	Output format	v
=	linter	--output-format
v	text	
v	json	
@	clean
@	format
o	--check	Avoid writing any formatted files back; instead, exit with a non-zero status code if any files…	
o	--diff	Avoid writing any formatted files back; instead, exit with a non-zero status code and the…	
o	--extension	List of mappings from file extension to language (one of `python`, `ipynb`, `pyi`). For example…	V
o	--target-version	The minimum Python version that should be supported	V
o	--preview	Enable preview mode; enables unstable formatting. Use `--no-preview` to disable	
o	-n|--no-cache	Disable cache reads (env: RUFF_NO_CACHE=)	
o	--cache-dir	Path to the cache directory (env: RUFF_CACHE_DIR=)	v
o	--stdin-filename	The name of the file when passing it through stdin	v
o	--respect-gitignore	Respect file exclusions via `.gitignore` and other standard ignore files	
o	--exclude	List of paths, used to omit files and/or directories from analysis	V
o	--force-exclude	Enforce exclusions, even for paths passed to Ruff directly on the command-line	
o	--line-length	Set the line-length	V
o	--range	When specified, Ruff will try to only format the code in the given range	V
a	1	1
=	format	--target-version
v	py37	
v	py38	
v	py39	
v	py310	
v	py311	
v	py312	
v	py313	
=	format	--cache-dir
t	filepaths
=	format	--stdin-filename
t	filepaths
#	format	1
t	filepaths
@	server
o	--preview	Enable preview mode. Use `--no-preview` to disable	
o	--no-preview	Disable preview mode	
@	analyze
s	graph	Generate a map of Python file dependencies or dependents
@	analyze graph
o	--direction	The direction of the import map. By default, generates a dependency map, i.e., a map from file to…	v
o	--detect-string-imports	Attempt to detect imports from string literals	
o	--preview	Enable preview mode. Use `--no-preview` to disable	
o	--no-preview	Disable preview mode	
o	--target-version	The minimum Python version that should be supported	v
a	1	1
=	analyze graph	--direction
v	dependencies	
v	dependents	
=	analyze graph	--target-version
v	py37	
v	py38	
v	py39	
v	py310	
v	py311	
v	py312	
v	py313	
#	analyze graph	1
t	filepaths
@	version
o	--output-format	Output format	v
=	version	--output-format
v	text	
v	json	
@	help
