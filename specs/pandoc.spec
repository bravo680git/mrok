@	
o	-f|-r|--from|--read	Specify input format	v
o	-t|-w|--to|--write	Specify output format	v
o	-o|--output	Write output to FILE instead of stdout	v
o	--data-dir	Specify the user data directory to search for pandoc data files	v
o	-d|--defaults	Specify a set of default option settings	v
o	--bash-completion	Generate a bash completion script	
o	--verbose	Give verbose debugging output	
o	--quiet	Suppress warning messages	
o	--fail-if-warnings	Exit with error status if there are any warnings	
o	--log	Write log messages in machine-readable JSON format to FILE	v
o	--list-input-formats	List supported input formats, one per line	
o	--list-output-formats	List supported output formats, one per line	
o	--list-extensions	List supported extensions for FORMAT, one per line, preceded by a + or - indicating whether it is…	V
o	--list-highlight-languages	List supported languages for syntax highlighting, one per line	
o	--list-highlight-styles	List supported styles for syntax highlighting, one per line	
o	-v|--version	Print version	
o	-h|--help	Show usage message	
o	--shift-heading-level-by	Shift heading levels by a positive or negative integer	v
o	--indented-code-classes	Specify classes to use for indented code blocks–for example, perl,numberLines or haskell. Multiple…	v
o	--default-image-extension	Specify a default extension to use when image paths/URLs have no extension. This allows you to use…	v
o	--file-scope	Parse each file individually before combining for multifile documents. This will allow footnotes…	
o	-F|--filter	Specify an executable to be used as a filter transforming the pandoc AST after the input is parsed…	v
o	-L|--lua-filter	Transform the document in a similar fashion as JSON filters, but use pandoc’s built-in Lua…	v
o	-M|--metadata	Set the metadata field KEY to the value VAL	v
o	--metadata-file	Read metadata from the supplied YAML (or JSON) file	v
o	-p|--preserve-tabs	Preserve tabs instead of converting them to spaces	
o	--tab-stop	Specify the number of spaces per tab	v
o	--track-changes	Specifies what to do with insertions, deletions, and comments produced by the MS Word `Track…	v
o	--extract-media	Extract images and other media contained in or linked from the source document to the path DIR…	v
o	--abbreviations	Specifies a custom abbreviations file, with abbreviations one to a line. If this option is not…	v
o	-s|--standalone	Produce output with an appropriate header and footer (e.g. a standalone HTML, LaTeX, TEI, or RTF…	
o	--template	Use the specified file as a custom template for the generated document	v
o	-V|--variable	Set the template variable KEY to the value VAL when rendering the document in standalone mode. If…	v
o	-D|--print-default-template	Print the system default template for an output FORMAT. Templates in the user data directory are…	v
o	--print-default-data-file	Print a system default data file. Files in the user data directory are ignored	v
o	--eol	Manually specify line endings: crlf (Windows), lf (macOS/Linux/UNIX), or native (line endings…	v
o	--dpi	Specify the default dpi (dots per inch) value for conversion from pixels to inch/centimeters and…	v
o	--wrap	Determine how text is wrapped in the output (the source code, not the rendered version)	v
o	--columns	Specify length of lines in characters. This affects text wrapping in the generated source code	v
o	--toc|--table-of-contents	Include an automatically generated table of contents (or, in the case of latex, context, docx…	
o	--toc-depth	Specify the number of section levels to include in the table of contents	v
o	--strip-comments	Strip out HTML comments in the Markdown or Textile source, rather than passing them on to…	
o	--no-highlight	Disables syntax highlighting for code blocks and inlines, even when a language attribute is given	
o	--highlight-style	Specifies the coloring style to be used in highlighted source code	v
o	--print-highlight-style	Prints a JSON version of a highlighting style, which can be modified, saved with a .theme…	v
o	--syntax-definition	Instructs pandoc to load a KDE XML syntax definition file, which will be used for syntax…	v
o	-H|--include-in-header	Include contents of FILE, verbatim, at the end of the header	v
o	-B|--include-before-body	Include contents of FILE, verbatim, at the beginning of the document body	v
o	-A|--include-after-body	Include contents of FILE, verbatim, at the end of the document body	v
o	--resource-path	List of paths to search for images and other resources. If --resource-path is not specified, the…	v
o	--request-header	Set the request header NAME to the value VAL when making HTTP requests. If you’re behind a proxy…	v
o	--no-check-certificate	Disable the certificate verification to allow access to unsecure HTTP resources	
o	--self-contained	Produce a standalone HTML file with no external dependencies, using data: URIs to incorporate the…	
o	--html-q-tags	Use <q> tags for quotes in HTML. This option only has an effect if the smart extension is enabled	
o	--ascii	Use only ASCII characters in output. Currently supported for XML, HTML formats, CommonMark, gfm…	
o	--reference-links	Use reference-style links, rather than inline links, in writing Markdown or reStructuredText	
o	--reference-location	Specify whether footnotes (and references, if reference-links is set) are placed at the end of the…	v
o	--markdown-headings	Specify whether to use ATX-style (#-prefixed) or Setext-style (underlined) headings for level 1…	v
o	--atx-headers	Deprecated synonym for --markdown-headings=atx	
o	--top-level-division	Treat top-level headings as the given division type in LaTeX, ConTeXt, DocBook, and TEI output	v
o	-N|--number-sections	Number section headings in LaTeX, ConTeXt, HTML, Docx, ms, or EPUB output. By default, sections…	
o	--number-offset	Offset for section headings in HTML output (ignored in other output formats)	v
o	--listings	Use the listings package for LaTeX code blocks. The package does not support multi-byte encoding…	
o	-i|--incremental	Make list items in slide shows display incrementally	
o	--slide-level	Specifies that headings with the specified level create slides (for beamer, s5, slidy, slideous…	v
o	--section-divs	Wrap sections in <section> tags (or <div> tags for html4), and attach identifiers to the enclosing…	
o	--email-obfuscation	Specify a method for obfuscating mailto: links in HTML documents references . The default is none	v
o	--id-prefix	Specify a prefix to be added to all identifiers and internal links in HTML and DocBook output, and…	v
o	-T|--title-prefix	Specify STRING as a prefix at the beginning of the title that appears in the HTML header (but not…	v
o	-c|--css	Link to a CSS style sheet. This option can be used repeatedly to include multiple files. They will…	v
o	--reference-doc	Use the specified file as a style reference in producing a docx or ODT file	v
o	--epub-cover-image	Use the specified image as the EPUB cover. It is recommended that the image be less than 1000px in…	v
o	--epub-metadata	Look in the specified XML file for metadata for the EPUB. The file should contain a series of…	v
o	--epub-embed-font	Embed the specified font in the EPUB. This option can be repeated to embed multiple fonts…	v
o	--pdf-engine	Use the specified engine when producing PDF output	v
o	--pdf-engine-opt	Use the given string as a command-line argument to the pdf-engine	v
o	-C|--citeproc	Process the citations in the file, replacing them with rendered citations and adding a…	
o	--bibliography	Set the bibliography field in the document’s metadata to FILE, overriding any value set in the…	v
o	--csl	Set the csl field in the document’s metadata to FILE, overriding any value set in the metadata…	v
o	--citation-abbreviations	Set the citation-abbreviations field in the document’s metadata to FILE, overriding any value set…	v
o	--natbib	Use natbib for citations in LaTeX output. It is intended for use in producing a LaTeX file that…	
o	--biblatex	Use biblatex for citations in LaTeX output. It is intended for use in producing a LaTeX file that…	
o	--mathjax	Use MathJax to display embedded TeX math in HTML output. TeX math will be put between (...) (for…	v
o	--mathml	Convert TeX math to MathML (in epub3, docbook4, docbook5, jats, html4 and html5). This is the…	
o	--webtex	Convert TeX formulas to <img> tags that link to an external script that converts formulas to…	v
o	--katex	Use KaTeX to display embedded TeX math in HTML output. The URL is the base URL for the KaTeX…	v
o	--gladtex	Enclose TeX math in <eq> tags in HTML output. The resulting HTML can then be processed by GladTeX…	
o	--dump-args	Print information about command-line arguments to stdout, then exit. This option is intended…	
o	--ignore-args	Ignore command-line arguments (for use in wrapper scripts). Regular pandoc options are not ignored	
a	1	1
=		-f
d
=		-t
d
=		-o
t	filepaths
=		--data-dir
t	folders
=		-d
d
=		--log
t	filepaths
=		--list-extensions
d
=		-F
t	filepaths
=		-L
t	filepaths
=		--metadata-file
d
=		--track-changes
v	accept	Processes all the insertions and deletions and ignores comments
v	reject	Ignores all the insertions and deletions and ignores comments
v	all	Includes all insertions, deletions, and comments, wrapped in spans with insertion, deletion…
=		--extract-media
t	folders
=		--abbreviations
t	filepaths
=		--template
t	filepaths
=		-D
d
=		--print-default-data-file
t	filepaths
=		--eol
v	crlf	Windows
v	lf	MacOS/Linux/UNIX
v	native	Line endings appropriate to the OS on which Pandoc is being run
=		--wrap
v	auto	Attempts to wrap lines to the column width specified by --columns (default 72)
v	none	Will not wrap lines at all
v	preserve	Attempts to preserve the wrapping from the source document
=		--highlight-style
v	pygments	
v	kate	
v	monochrome	
v	breezeDark	
v	espresso	
v	zenburn	
v	haddock	
v	tango	
t	filepaths
=		--print-highlight-style
v	pygments	
v	kate	
v	monochrome	
v	breezeDark	
v	espresso	
v	zenburn	
v	haddock	
v	tango	
t	filepaths
=		--syntax-definition
t	filepaths
=		-H
t	filepaths
=		-B
t	filepaths
=		-A
t	filepaths
=		--resource-path
t	folders
=		--reference-location
v	block	
v	section	
v	document	
=		--markdown-headings
v	setext	
v	atx	
=		--top-level-division
v	default	
v	section	
v	chapter	
v	part	
=		--email-obfuscation
v	none	Leaves mailto: links as they are
v	javascript	Obfuscates mailto: links using JavaScript
v	references	Obfuscates mailto: links by printing their letters as decimal or hexadecimal character references
=		--reference-doc
t	filepaths
=		--epub-cover-image
t	filepaths
=		--epub-metadata
t	filepaths
=		--epub-embed-font
t	filepaths
=		--pdf-engine
v	pdflatex	
v	lualatex	
v	xelatex	
v	latexmk	
v	tectonic	
v	wkhtmltopdf	
v	weasyprint	
v	prince	
v	context	
v	pdfroff	
=		--bibliography
t	filepaths
=		--csl
t	filepaths
=		--citation-abbreviations
t	filepaths
#		1
t	filepaths
