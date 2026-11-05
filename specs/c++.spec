@	
o	-###	Print (but do not run) the commands to run for this compilation	
o	--analyzer-output	Static analyzer report output format	v
o	--analyze	Run the static analyzer	
o	-arcmt-migrate-emit-errors	Emit ARC errors even if the migrator can fix them	
o	-arcmt-migrate-report-output	Output path for the plist report	v
o	-B	Add <dir> to search path for binaries and object files used implicitly	v
o	-CC	Include comments from within macros in preprocessed output	
o	-cl-denorms-are-zero	OpenCL only. Allow denormals to be flushed to zero	
o	-cl-fast-relaxed-math	OpenCL only. Sets -cl-finite-math-only and -cl-unsafe-math-optimizations, and defines…	
o	-cl-finite-math-only	OpenCL only. Allow floating-point optimizations that assume arguments and results are not NaNs or…	
o	-cl-fp32-correctly-rounded-divide-sqrt	OpenCL only. Specify that single precision floating-point divide and sqrt used in the program…	
o	-cl-kernel-arg-info	OpenCL only. Generate kernel argument metadata	
o	-cl-mad-enable	OpenCL only. Allow use of less precise MAD computations in the generated binary	
o	-cl-no-signed-zeros	OpenCL only. Allow use of less precise no signed zeros computations in the generated binary	
o	-cl-opt-disable	OpenCL only. This option disables all optimizations. By default optimizations are enabled	
o	-cl-single-precision-constant	OpenCL only. Treat double precision floating-point constant as single precision constant	
o	-cl-std	OpenCL language standard to compile for	v=
o	-cl-strict-aliasing	OpenCL only. This option is added for compatibility with OpenCL 1.0	
o	-cl-uniform-work-group-size	OpenCL only. Defines that the global work-size be a multiple of the work-group size specified to…	
o	-cl-unsafe-math-optimizations	OpenCL only. Allow unsafe floating-point optimizations. Also implies -cl-no-signed-zeros and…	
o	--config	Specifies configuration file	v
o	--cuda-compile-host-device	Compile CUDA code for both host and device (default). Has no effect on non-CUDA compilations	
o	--cuda-device-only	Compile CUDA code for device only	
o	--cuda-host-only	Compile CUDA code for host only. Has no effect on non-CUDA compilations	
o	--cuda-include-ptx	Include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more than…	v=
o	--cuda-noopt-device-debug	Enable device-side debug info generation. Disables ptxas optimizations	
o	--cuda-path-ignore-env	Ignore environment variables to detect CUDA installation	
o	--cuda-path	CUDA installation path	v=
o	-cxx-isystem	Add directory to the C++ SYSTEM include search path	v
o	-C	Include comments in preprocessed output	
o	-c	Only run preprocess, compile, and assemble steps	
o	-dD	Print macro definitions in -E mode in addition to normal output	
o	-dependency-dot	Filename to write DOT-formatted header dependencies to	v
o	-dependency-file	Filename (or -) to write dependency output to	v
o	-dI	Print include directives in -E mode in addition to normal output	
o	-dM	Print macro definitions in -E mode instead of normal output	
o	-dsym-dir	Directory to output dSYM's (if any) to	v
o	-D	=<value> Define <macro> to <value> (or 1 if <value> omitted)	v
o	-emit-ast	Emit Clang AST files for source inputs	
o	-emit-interface-stubs	Generate Interface Stub Files	
o	-emit-llvm	Use the LLVM representation for assembler and object files	
o	-emit-merged-ifs	Generate Interface Stub Files, emit merged text not binary	
o	--emit-static-lib	Enable linker job to emit a static library	
o	-enable-trivial-auto-var-init-zero-knowing-it-will-be-removed-from-clang	Trivial automatic variable initialization to zero is only here for benchmarks, it'll eventually be…	
o	-E	Only run the preprocessor	
o	-faapcs-bitfield-load	Follows the AAPCS standard that all volatile bit-field write generates at least one load. (ARM only)	
o	-faapcs-bitfield-width	Follow the AAPCS standard requirement stating that volatile bit-field width is dictated by the…	
o	-faccess-control		
o	-faddrsig	Emit an address-significance table	
o	-faligned-allocation	Enable C++17 aligned allocation functions	
o	-fallow-editor-placeholders	Treat editor placeholders as valid source code	
o	-fansi-escape-codes	Use ANSI escape codes for diagnostics	
o	-fapinotes-cache-path	Does nothing; API notes are no longer cached separately from modules	v=
o	-fapinotes-modules	Enable module-based external API notes support	
o	-fapinotes-swift-version	Specify the Swift version to use when filtering API notes	v=
o	-fapinotes	Enable external API notes support	
o	-fapple-kext	Use Apple's kernel extensions ABI	
o	-fapple-link-rtlib	Force linking the clang builtins runtime library	
o	-fapple-pragma-pack	Enable Apple gcc-compatible #pragma pack handling	
o	-fapplication-extension	Restrict code to those available for App Extensions	
o	-fasm-blocks		
o	-fautolink		
o	-fbasic-block-sections	Place each function's basic blocks in unique sections (ELF Only) : all | labels | none | list=<file>	v=
o	-fblocks	Enable the 'blocks' language feature	
o	-fborland-extensions	Accept non-standard constructs supported by the Borland compiler	
o	-fbranch-target-identification	Emit branch target identification instructions for indirect branch destinations	
o	-fbuild-session-file	Use the last modification time of <file> as the build session timestamp	v=
o	-fbuild-session-timestamp	Time when the current build session started	v=
o	-fbuiltin-module-map	Load the clang builtins module map file	
o	-fc++-static-destructors		
o	-fcall-saved-x10	Make the x10 register call-saved (AArch64 only)	
o	-fcall-saved-x11	Make the x11 register call-saved (AArch64 only)	
o	-fcall-saved-x12	Make the x12 register call-saved (AArch64 only)	
o	-fcall-saved-x13	Make the x13 register call-saved (AArch64 only)	
o	-fcall-saved-x14	Make the x14 register call-saved (AArch64 only)	
o	-fcall-saved-x15	Make the x15 register call-saved (AArch64 only)	
o	-fcall-saved-x18	Make the x18 register call-saved (AArch64 only)	
o	-fcall-saved-x8	Make the x8 register call-saved (AArch64 only)	
o	-fcall-saved-x9	Make the x9 register call-saved (AArch64 only)	
o	-fcaret-diagnostics		
o	-fcf-protection	Instrument control-flow architecture protection	V=
o	-fchar8_t	Enable C++ builtin type char8_t	
o	-fclang-abi-compat	Attempt to match the ABI of Clang <version>	v=
o	-fcolor-diagnostics	Enable colors in diagnostics	
o	-fcomment-block-commands	Treat each comma separated argument in <arg> as a documentation comment block command	v=
o	-fcommon	Place uninitialized global variables in a common block	
o	-fcomplete-member-pointers	Require member pointer base types to be complete if they would be significant under the Microsoft…	
o	-fconstant-cfstrings		
o	-fconvergent-functions	Assume functions may be convergent	
o	-fcoroutines-ts	Enable support for the C++ Coroutines TS	
o	-fcoverage-mapping	Generate coverage mapping to enable code coverage analysis	
o	-fcs-profile-generate	Generate instrumented code to collect context sensitive execution counts into…	V=
o	-fcuda-approx-transcendentals	Use approximate transcendental functions	
o	-fcuda-flush-denormals-to-zero	Flush denormal floating point values to zero in CUDA device mode	
o	-fcuda-short-ptr	Use 32-bit pointers for accessing const/local/shared address spaces	
o	-fcxx-exceptions	Enable C++ exceptions	
o	-fdata-sections	Place each data in its own section	
o	-fdebug-compilation-dir	The compilation directory to embed in the debug info	v
o	-fdebug-default-version	Default DWARF version to use, if a -g option caused DWARF debug info to be produced	v=
o	-fdebug-info-for-profiling	Emit extra debug info to make sample profile more accurate	
o	-fdebug-macro	Emit macro debug information	
o	-fdebug-prefix-map	Remap file source paths in debug info	v=
o	-fdebug-ranges-base-address	Use DWARF base address selection entries in .debug_ranges	
o	-fdebug-types-section	Place debug types in their own section (ELF Only)	
o	-fdeclspec	Allow __declspec as a keyword	
o	-fdelayed-template-parsing	Parse templated function definitions at the end of the translation unit	
o	-fdelete-null-pointer-checks	Treat usage of null pointers as undefined behavior (default)	
o	-fdiagnostics-absolute-paths	Print absolute paths in diagnostics	
o	-fdiagnostics-hotness-threshold	Prevent optimization remarks from being output if they do not have at least this profile count…	v=
o	-fdiagnostics-parseable-fixits	Print fix-its in machine parseable form	
o	-fdiagnostics-print-source-range-info	Print source range spans in numeric form	
o	-fdiagnostics-show-hotness	Enable profile hotness information in diagnostic line	
o	-fdiagnostics-show-note-include-stack	Display include stacks for diagnostic notes	
o	-fdiagnostics-show-option	Print option name with mappable diagnostics	
o	-fdiagnostics-show-template-tree	Print a template comparison tree for differing templates	
o	-fdigraphs	Enable alternative token representations '<:', ':>', '<%', '%>', '%:', '%:%:' (default)	
o	-fdiscard-value-names	Discard value names in LLVM IR	
o	-fdollars-in-identifiers	Allow '$' in identifiers	
o	-fdouble-square-bracket-attributes	Enable '[[]]' attributes in all C and C++ language modes	
o	-fdwarf-directory-asm		
o	-fdwarf-exceptions	Use DWARF style exceptions	
o	-felide-constructors		
o	-feliminate-unused-debug-types	Do not emit debug info for defined but unused types	
o	-fembed-bitcode-marker	Embed placeholder LLVM IR data as a marker	
o	-fembed-bitcode	Embed LLVM bitcode	V=
o	-femit-all-decls	Emit all declarations, even if unused	
o	-femulated-tls	Use emutls functions to access thread_local variables	
o	-fenable-matrix	Enable matrix data type and related builtin functions	
o	-fescaping-block-tail-calls		
o	-fexceptions	Enable support for exception handling	
o	-fexperimental-new-constant-interpreter	Enable the experimental new constant interpreter	
o	-fexperimental-relative-c++-abi-vtables	Use the experimental C++ class ABI for classes with virtual tables	
o	-fexperimental-strict-floating-point	Enables experimental strict floating point in LLVM	
o	-ffast-math	Allow aggressive, lossy floating-point optimizations	
o	-ffile-prefix-map	Remap file source paths in debug info and predefined preprocessor macros	v=
o	-ffine-grained-bitfield-accesses	Use separate accesses for consecutive bitfield runs with legal widths and alignments	
o	-ffinite-loops	Assume all loops are finite	
o	-ffinite-math-only		
o	-ffixed-point	Enable fixed point types	
o	-ffixed-r19	Reserve register r19 (Hexagon only)	
o	-ffixed-r9	Reserve the r9 register (ARM only)	
o	-ffixed-x10	Reserve the x10 register (AArch64/RISC-V only)	
o	-ffixed-x11	Reserve the x11 register (AArch64/RISC-V only)	
o	-ffixed-x12	Reserve the x12 register (AArch64/RISC-V only)	
o	-ffixed-x13	Reserve the x13 register (AArch64/RISC-V only)	
o	-ffixed-x14	Reserve the x14 register (AArch64/RISC-V only)	
o	-ffixed-x15	Reserve the x15 register (AArch64/RISC-V only)	
o	-ffixed-x16	Reserve the x16 register (AArch64/RISC-V only)	
o	-ffixed-x17	Reserve the x17 register (AArch64/RISC-V only)	
o	-ffixed-x18	Reserve the x18 register (AArch64/RISC-V only)	
o	-ffixed-x19	Reserve the x19 register (AArch64/RISC-V only)	
o	-ffixed-x1	Reserve the x1 register (AArch64/RISC-V only)	
o	-ffixed-x20	Reserve the x20 register (AArch64/RISC-V only)	
o	-ffixed-x21	Reserve the x21 register (AArch64/RISC-V only)	
o	-ffixed-x22	Reserve the x22 register (AArch64/RISC-V only)	
o	-ffixed-x23	Reserve the x23 register (AArch64/RISC-V only)	
o	-ffixed-x24	Reserve the x24 register (AArch64/RISC-V only)	
o	-ffixed-x25	Reserve the x25 register (AArch64/RISC-V only)	
o	-ffixed-x26	Reserve the x26 register (AArch64/RISC-V only)	
o	-ffixed-x27	Reserve the x27 register (AArch64/RISC-V only)	
o	-ffixed-x28	Reserve the x28 register (AArch64/RISC-V only)	
o	-ffixed-x29	Reserve the x29 register (AArch64/RISC-V only)	
o	-ffixed-x2	Reserve the x2 register (AArch64/RISC-V only)	
o	-ffixed-x30	Reserve the x30 register (AArch64/RISC-V only)	
o	-ffixed-x31	Reserve the x31 register (AArch64/RISC-V only)	
o	-ffixed-x3	Reserve the x3 register (AArch64/RISC-V only)	
o	-ffixed-x4	Reserve the x4 register (AArch64/RISC-V only)	
o	-ffixed-x5	Reserve the x5 register (AArch64/RISC-V only)	
o	-ffixed-x6	Reserve the x6 register (AArch64/RISC-V only)	
o	-ffixed-x7	Reserve the x7 register (AArch64/RISC-V only)	
o	-ffixed-x8	Reserve the x8 register (AArch64/RISC-V only)	
o	-ffixed-x9	Reserve the x9 register (AArch64/RISC-V only)	
o	-fforce-dwarf-frame	Always emit a debug frame section	
o	-fforce-emit-vtables	Emits more virtual tables to improve devirtualization	
o	-fforce-enable-int128	Enable support for int128_t type	
o	-ffp-contract	Form fused FP ops (e.g. FMAs): fast (fuses across statements disregarding pragmas) | on (only…	v=
o	-ffp-exception-behavior	Specifies the exception behavior of floating-point operations	v=
o	-ffp-model	Controls the semantics of floating-point calculations	v=
o	-ffreestanding	Assert that the compilation takes place in a freestanding environment	
o	-ffunction-sections	Place each function in its own section	
o	-fglobal-isel	Enables the global instruction selector	
o	-fgnu-inline-asm		
o	-fgnu-keywords	Allow GNU-extension keywords regardless of language standard	
o	-fgnu-runtime	Generate output compatible with the standard GNU Objective-C runtime	
o	-fgnu89-inline	Use the gnu89 inline semantics	
o	-fgnuc-version	Sets various macros to claim compatibility with the given GCC version (default is 4.2.1)	v=
o	-fgpu-allow-device-init	Allow device side init function in HIP	
o	-fgpu-defer-diag	Defer host/device related diagnostic messages for CUDA/HIP	
o	-fgpu-rdc	Generate relocatable device code, also known as separate compilation mode	
o	-fhip-new-launch-api	Use new kernel launching API for HIP	
o	-fignore-exceptions	Enable support for ignoring exception handling constructs	
o	-fimplicit-module-maps	Implicitly search the file system for module map files	
o	-fimplicit-modules		
o	-finline-functions	Inline suitable functions	
o	-finline-hint-functions	Inline functions which are (explicitly or implicitly) marked inline	
o	-finstrument-function-entry-bare	Instrument function entry only, after inlining, without arguments to the instrumentation call	
o	-finstrument-functions-after-inlining	Like -finstrument-functions, but insert the calls after inlining	
o	-finstrument-functions	Generate calls to instrument function entry and exit	
o	-fintegrated-as	Enable the integrated assembler	
o	-fintegrated-cc1	Run cc1 in-process	
o	-fjump-tables	Use jump tables for lowering switches	
o	-fkeep-static-consts	Keep static const variables if unused	
o	-flax-vector-conversions	Enable implicit vector bit-casts	v=
o	-flegacy-pass-manager	Use the legacy pass manager in LLVM	
o	-flto-jobs	Controls the backend parallelism of -flto=thin (default of 0 means the number of threads will be…	v=
o	-flto	Set LTO mode to either 'full' or 'thin'	V=
o	-fmacro-prefix-map	Remap file source paths in predefined preprocessor macros	v=
o	-fmath-errno	Require math functions to indicate errors by setting errno	
o	-fmax-tokens	Max total number of preprocessed tokens for -Wmax-tokens	v=
o	-fmax-type-align	Specify the maximum alignment to enforce on pointers lacking an explicit alignment	v=
o	-fmemory-profile	Enable heap memory profiling and dump results into <directory>	V=
o	-fmerge-all-constants	Allow merging of constants	
o	-fmessage-length	Format message diagnostics so that they fit within N columns	v=
o	-fmodule-file	[<name>=]<file> Specify the mapping of module name to precompiled module file, or load a module…	=
o	-fmodule-map-file	Load this module map file	v=
o	-fmodule-name	Specify the name of the module to build	v=
o	-fmodules-cache-path	Specify the module cache path	v=
o	-fmodules-decluse	Require declaration of modules used within a module	
o	-fmodules-disable-diagnostic-validation	Disable validation of the diagnostic options when loading the module	
o	-fmodules-ignore-macro	Ignore the definition of the given macro when building and loading modules	v=
o	-fmodules-prune-after	Specify the interval (in seconds) after which a module file will be considered unused	v=
o	-fmodules-prune-interval	Specify the interval (in seconds) between attempts to prune the module cache	v=
o	-fmodules-search-all	Search even non-imported modules to resolve references	
o	-fmodules-strict-decluse	Like -fmodules-decluse but requires all headers to be in modules	
o	-fmodules-ts	Enable support for the C++ Modules TS	
o	-fmodules-user-build-path	Specify the module user build path	v
o	-fmodules-validate-input-files-content	Validate PCM input files based on content if mtime differs	
o	-fmodules-validate-once-per-build-session	Don't verify input files for the modules if the module has been successfully validated or loaded…	
o	-fmodules-validate-system-headers	Validate the system headers that a module depends on when loading the module	
o	-fmodules	Enable the 'modules' language feature	
o	-fms-compatibility-version	Dot-separated value representing the Microsoft compiler version number to report in _MSC_VER (0 =…	v=
o	-fms-compatibility	Enable full Microsoft Visual C++ compatibility	
o	-fms-extensions	Accept some non-standard constructs supported by the Microsoft compiler	
o	-fmsc-version	Microsoft compiler version number to report in _MSC_VER (0 = don't define it (default))	v=
o	-fnew-alignment	Specifies the largest alignment guaranteed by '::operator new(size_t)'	v=
o	-fno-aapcs-bitfield-width	Do not follow the AAPCS standard requirement stating that volatile bit-field width is dictated by…	
o	-fno-access-control	Disable C++ access control	
o	-fno-addrsig	Don't emit an address-significance table	
o	-fno-allow-editor-placeholders		
o	-fno-apinotes-modules	Disable module-based external API notes support	
o	-fno-apinotes	Disable external API notes support	
o	-fno-apple-pragma-pack		
o	-fno-application-extension		
o	-fno-asm-blocks		
o	-fno-assume-sane-operator-new	Don't assume that C++'s global operator new can't alias any pointer	
o	-fno-autolink	Disable generation of linker directives for automatic library linking	
o	-fno-blocks		
o	-fno-borland-extensions		
o	-fno-builtin-value	Disable implicit builtin knowledge of a specific function	v
o	-fno-builtin	Disable implicit builtin knowledge of functions	
o	-fno-c++-static-destructors	Disable C++ static destructor registration	
o	-fno-caret-diagnostics		
o	-fno-char8_t	Disable C++ builtin type char8_t	
o	-fno-color-diagnostics	Disable colors in diagnostics	
o	-fno-common	Compile common globals like normal definitions	
o	-fno-complete-member-pointers	Do not require member pointer base types to be complete if they would be significant under the…	
o	-fno-constant-cfstrings	Disable creation of CodeFoundation-type constant strings	
o	-fno-constant-nsarray-literals	Disable creation of CodeFoundation-type constant initializer `NSArray`s from array literals	
o	-fno-constant-nsdictionary-literals	Disable creation of CodeFoundation-type constant initializer `NSDictionary`s from dictionary…	
o	-fno-constant-nsnumber-literals	Disable creation of CodeFoundation-type constant initializer `NSNumber`s from number literals	
o	-fno-coroutines-ts		
o	-fno-coverage-mapping	Disable code coverage analysis	
o	-fno-crash-diagnostics	Disable auto-generation of preprocessed source files and a script for reproduction during a clang…	
o	-fno-cuda-approx-transcendentals	Don't use approximate transcendental functions	
o	-fno-cuda-short-ptr		
o	-fno-cxx-exceptions		
o	-fno-cxx-modules	Disable modules for C++	
o	-fno-data-sections		
o	-fno-debug-info-for-profiling		
o	-fno-debug-macro	Do not emit macro debug information	
o	-fno-debug-ranges-base-address		
o	-fno-declspec	Disallow __declspec as a keyword	
o	-fno-delayed-template-parsing	Disable delayed template parsing	
o	-fno-delete-null-pointer-checks	Do not treat usage of null pointers as undefined behavior	
o	-fno-diagnostics-fixit-info	Do not include fixit information in diagnostics	
o	-fno-diagnostics-show-hotness		
o	-fno-digraphs	Disallow alternative token representations '<:', ':>', '<%', '%>', '%:', '%:%:'	
o	-fno-discard-value-names	Do not discard value names in LLVM IR	
o	-fno-dollars-in-identifiers	Disallow '$' in identifiers	
o	-fno-double-square-bracket-attributes	Disable '[[]]' attributes in all C and C++ language modes	
o	-fno-dwarf-directory-asm		
o	-fno-elide-constructors	Disable C++ copy constructor elision	
o	-fno-elide-type	Do not elide types when printing diagnostics	
o	-fno-eliminate-unused-debug-types	Emit debug info for defined but unused types	
o	-fno-escaping-block-tail-calls		
o	-fno-exceptions	Disable support for exception handling	
o	-fno-experimental-relative-c++-abi-vtables	Do not use the experimental C++ class ABI for classes with virtual tables	
o	-fno-fast-math		
o	-fno-fine-grained-bitfield-accesses	Use large-integer access for consecutive bitfield runs	
o	-fno-finite-loops	Do not assume that any loop is finite	
o	-fno-finite-math-only		
o	-fno-fixed-point	Disable fixed point types	
o	-fno-force-dwarf-frame		
o	-fno-force-emit-vtables		
o	-fno-force-enable-int128	Disable support for int128_t type	
o	-fno-function-sections		
o	-fno-global-isel	Disables the global instruction selector	
o	-fno-gnu-inline-asm	Disable GNU style inline asm	
o	-fno-gnu89-inline		
o	-fno-gpu-allow-device-init	Don't allow device side init function in HIP	
o	-fno-gpu-defer-diag	Don't defer host/device related diagnostic messages for CUDA/HIP	
o	-fno-gpu-rdc		
o	-fno-hip-new-launch-api	Don't use new kernel launching API for HIP	
o	-fno-implicit-modules		
o	-fno-integrated-as	Disable the integrated assembler	
o	-fno-integrated-cc1	Spawn a separate process for each cc1	
o	-fno-jump-tables	Do not use jump tables for lowering switches	
o	-fno-keep-static-consts	Don't keep static const variables if unused	
o	-fno-legacy-pass-manager	Use the new pass manager in LLVM	
o	-fno-lto	Disable LTO mode (default)	
o	-fno-math-errno		
o	-fno-memory-profile	Disable heap memory profiling	
o	-fno-merge-all-constants	Disallow merging of constants	
o	-fno-modules-validate-system-headers		
o	-fno-objc-arc-exceptions		
o	-fno-objc-convert-messages-to-runtime-calls		
o	-fno-objc-encode-cxx-class-template-spec		
o	-fno-objc-exceptions		
o	-fno-objc-infer-related-result-type	Do not infer Objective-C related result type based on method family	
o	-fno-operator-names	Do not treat C++ operator name keywords as synonyms for operators	
o	-fno-pascal-strings		
o	-fno-pch-codegen	Do not generate code for uses of this PCH that assumes an explicit object file will be built for…	
o	-fno-pch-debuginfo	Do not generate debug info for types in an object file built from this PCH and do not generate…	
o	-fno-pch-instantiate-templates		
o	-fno-plt	Use GOT indirection instead of PLT to make external function calls (x86 only)	
o	-fno-prebuilt-implicit-modules		
o	-fno-preserve-as-comments	Do not preserve comments in inline assembly	
o	-fno-profile-arcs		
o	-fno-profile-generate	Disable generation of profile instrumentation	
o	-fno-profile-instr-generate	Disable generation of profile instrumentation	
o	-fno-profile-instr-use	Disable using instrumentation data for profile-guided optimization	
o	-fno-pseudo-probe-for-profiling	Do not emit pseudo probes for sample profiler	
o	-fno-ptrauth-abi-version	Disable Pointer Authentication ABI versioning	
o	-fno-ptrauth-kernel-abi-version	Disable Pointer Authentication kernel ABI versioning	
o	-fno-reciprocal-math		
o	-fno-register-global-dtors-with-atexit	Don't use atexit or __cxa_atexit to register global destructors	
o	-fno-relaxed-template-template-args		
o	-fno-reroll-loops		
o	-fno-rewrite-imports		
o	-fno-rewrite-includes		
o	-fno-ropi		
o	-fno-rtlib-add-rpath	Do not add -rpath with architecture-specific resource directory to the linker flags	
o	-fno-rtti-data	Disable generation of RTTI data	
o	-fno-rtti	Disable generation of rtti information	
o	-fno-rwpi		
o	-fno-sanitize-address-poison-custom-array-cookie	Disable poisoning array cookies when using custom operator new[] in AddressSanitizer	
o	-fno-sanitize-address-use-after-scope	Disable use-after-scope detection in AddressSanitizer	
o	-fno-sanitize-address-use-odr-indicator	Disable ODR indicator globals	
o	-fno-sanitize-blacklist	Don't use blacklist file for sanitizers	
o	-fno-sanitize-cfi-canonical-jump-tables	Do not make the jump table addresses canonical in the symbol table	
o	-fno-sanitize-cfi-cross-dso	Disable control flow integrity (CFI) checks for cross-DSO calls	
o	-fno-sanitize-coverage	Disable specified features of coverage instrumentation for Sanitizers	v=
o	-fno-sanitize-memory-track-origins	Disable origins tracking in MemorySanitizer	
o	-fno-sanitize-memory-use-after-dtor	Disable use-after-destroy detection in MemorySanitizer	
o	-fno-sanitize-minimal-runtime		
o	-fno-sanitize-recover	Disable recovery for specified sanitizers	v=
o	-fno-sanitize-stats	Disable sanitizer statistics gathering	
o	-fno-sanitize-thread-atomics	Disable atomic operations instrumentation in ThreadSanitizer	
o	-fno-sanitize-thread-func-entry-exit	Disable function entry/exit instrumentation in ThreadSanitizer	
o	-fno-sanitize-thread-memory-access	Disable memory access instrumentation in ThreadSanitizer	
o	-fno-sanitize-trap	Disable trapping for sanitizers	V=
o	-fno-semantic-interposition		
o	-fno-short-enums		
o	-fno-short-wchar	Force wchar_t to be an unsigned int	
o	-fno-show-column	Do not include column number on diagnostics	
o	-fno-show-source-location	Do not include source location information with diagnostics	
o	-fno-signed-char	Char is unsigned	
o	-fno-signed-zeros	Allow optimizations that ignore the sign of floating point zeros	
o	-fno-sized-deallocation		
o	-fno-spell-checking	Disable spell-checking	
o	-fno-split-dwarf-inlining		
o	-fno-split-lto-unit		
o	-fno-split-machine-functions	Disable late function splitting using profile information (x86 ELF)	
o	-fno-stack-check	Disable stack checking	
o	-fno-stack-clash-protection	Disable stack clash protection	
o	-fno-stack-protector	Disable the use of stack protectors	
o	-fno-stack-size-section		
o	-fno-standalone-debug	Limit debug information produced to reduce size of debug binary	
o	-fno-strict-float-cast-overflow	Relax language rules and try to match the behavior of the target's native float-to-int conversion…	
o	-fno-strict-return	Don't treat control flow paths that fall off the end of a non-void function as unreachable	
o	-fno-strict-vtable-pointers		
o	-fno-sycl	Disable SYCL kernels compilation for device	
o	-fno-temp-file	Directly create compilation output files. This may lead to incorrect incremental builds if the…	
o	-fno-test-coverage		
o	-fno-threadsafe-statics	Do not emit code to make initialization of local statics thread safe	
o	-fno-trigraphs	Do not process trigraph sequences	
o	-fno-unique-basic-block-section-names		
o	-fno-unique-internal-linkage-names		
o	-fno-unique-section-names	Don't use unique names for text and data sections	
o	-fno-unroll-loops	Turn off loop unroller	
o	-fno-use-cxa-atexit	Don't use __cxa_atexit for calling destructors	
o	-fno-use-init-array	Use .ctors/.dtors instead of .init_array/.fini_array	
o	-fno-use-line-directives		
o	-fno-virtual-function-elimination		
o	-fno-visibility-from-dllstorageclass		
o	-fno-visibility-inlines-hidden-static-local-var	Disables -fvisibility-inlines-hidden-static-local-var (this is the default on non-darwin targets)	
o	-fno-whole-program-vtables		
o	-fno-xray-always-emit-customevents		
o	-fno-xray-always-emit-typedevents		
o	-fno-xray-function-index	Omit function index section at the expense of single-function patching performance	
o	-fno-xray-ignore-loops		
o	-fno-xray-instrument		
o	-fno-zero-initialized-in-bss	Don't place zero initialized data in BSS	
o	-fno-zvector		
o	-fobjc-arc-exceptions	Use EH-safe code when synthesizing retains and releases in -fobjc-arc	
o	-fobjc-arc	Synthesize retain and release calls for Objective-C pointers	
o	-fobjc-convert-messages-to-runtime-calls		
o	-fobjc-disable-direct-methods-for-testing	Ignore attribute objc_direct so that direct methods can be tested	
o	-fobjc-encode-cxx-class-template-spec	Fully encode c++ class template specialization	
o	-fobjc-exceptions	Enable Objective-C exceptions	
o	-fobjc-infer-related-result-type		
o	-fobjc-relative-method-lists	Enable relative method lists	
o	-fobjc-runtime	Specify the target Objective-C runtime kind and version	v=
o	-fobjc-weak	Enable ARC-style weak references in Objective-C	
o	-fopenmp-simd	Emit OpenMP code only for SIMD-based constructs	
o	-fopenmp-targets	Specify comma-separated list of triples OpenMP offloading targets to be supported	v=
o	-fopenmp	Parse OpenMP pragmas and generate parallel code	
o	-foptimization-record-file	Specify the output name of the file containing the optimization remarks. Implies…	v=
o	-foptimization-record-passes	Only include passes which match a specified regular expression in the generated optimization…	v=
o	-forder-file-instrumentation	Generate instrumented code to collect order file into default.profraw file (overridden by '=' form…	
o	-fpack-struct	Specify the default maximum struct packing alignment	v=
o	-fpascal-strings	Recognize and construct Pascal-style string literals	
o	-fpass-plugin	Load pass plugin from a dynamic shared object file (only with new pass manager)	v=
o	-fpatchable-function-entry	Generate M NOPs before function entry and N-M NOPs after function entry	v=
o	-fpcc-struct-return	Override the default ABI to return all structs on the stack	
o	-fpch-codegen	Generate code for uses of this PCH that assumes an explicit object file will be built for the PCH	
o	-fpch-debuginfo	Generate debug info for types in an object file built from this PCH and do not generate them…	
o	-fpch-instantiate-templates	Instantiate templates already while building a PCH	
o	-fpch-validate-input-files-content	Validate PCH input files based on content if mtime differs	
o	-fplt		
o	-fplugin	Load the named plugin (dynamic shared object)	v=
o	-fprebuilt-implicit-modules	Look up implicit modules in the prebuilt module path	
o	-fprebuilt-module-path	Specify the prebuilt module path	v=
o	-fpreserve-as-comments		
o	-fproc-stat-report	Save subprocess statistics to the given file	v=
o	-fproc-stat-reportvalue	Print subprocess statistics	v
o	-fprofile-arcs		
o	-fprofile-exclude-files	Instrument only functions from files where names don't match all the regexes separated by a…	v=
o	-fprofile-filter-files	Instrument only functions from files where names match any regex separated by a semi-colon	v=
o	-fprofile-generate	Generate instrumented code to collect execution counts into <directory>/default.profraw…	V=
o	-fprofile-instr-generate	Generate instrumented code to collect execution counts into <file> (overridden by…	V=
o	-fprofile-instr-use	Use instrumentation data for profile-guided optimization	v=
o	-fprofile-remapping-file	Use the remappings described in <file> to match the profile data against names in the program	v=
o	-fprofile-sample-accurate	Specifies that the sample profile is accurate	
o	-fprofile-sample-use	Enable sample-based profile guided optimizations	v=
o	-fprofile-update	Set update method of profile counters (atomic,prefer-atomic,single)	v=
o	-fprofile-use	Use instrumentation data for profile-guided optimization. If pathname is a directory, it reads…	v=
o	-fpseudo-probe-for-profiling	Emit pseudo probes for sample profiler	
o	-fptrauth-abi-version	Pointer Authentication ABI version	v=
o	-fptrauth-auth-traps	Enable traps on authentication failures	
o	-fptrauth-block-descriptor-pointers	Enable signing block descriptors	
o	-fptrauth-calls	Enable signing and authentication of all indirect calls	
o	-fptrauth-function-pointer-type-discrimination	Enabling type discrimination on C function pointers	
o	-fptrauth-indirect-gotos	Enable signing and authentication of indirect goto targets	
o	-fptrauth-intrinsics	Enable pointer-authentication intrinsics	
o	-fptrauth-kernel-abi-version	Enable Pointer Authentication kernel ABI version	
o	-fptrauth-objc-isa-masking	Pre- and post-authentication masking mode of objective-c isa pointers	
o	-fptrauth-objc-isa-mode	Authentication mode for ObjC isa field. Full auth if unspecified	v=
o	-fptrauth-objc-isa	Enable signing and authentication of Objective-C object's 'isa' field	
o	-fptrauth-returns	Enable signing and authentication of return addresses	
o	-fptrauth-soft	Enable software lowering of pointer authentication	
o	-fptrauth-vtable-pointer-address-discrimination	Enable address discrimination of vtable pointers	
o	-fptrauth-vtable-pointer-type-discrimination	Enable type discrimination of vtable pointers	
o	-freciprocal-math	Allow division operations to be reassociated	
o	-freg-struct-return	Override the default ABI to return small structs in registers	
o	-fregister-global-dtors-with-atexit	Use atexit or __cxa_atexit to register global destructors	
o	-frelaxed-template-template-args	Enable C++17 relaxed template template argument matching	
o	-freroll-loops	Turn on loop reroller	
o	-frewrite-imports		
o	-frewrite-includes		
o	-fropi	Generate read-only position independent code (ARM only)	
o	-frtlib-add-rpath	Add -rpath with architecture-specific resource directory to the linker flags	
o	-frtti-data		
o	-frtti		
o	-frwpi	Generate read-write position independent code (ARM only)	
o	-fsanitize-address-field-padding	Level of field padding for AddressSanitizer	v=
o	-fsanitize-address-globals-dead-stripping	Enable linker dead stripping of globals in AddressSanitizer	
o	-fsanitize-address-poison-custom-array-cookie	Enable poisoning array cookies when using custom operator new[] in AddressSanitizer	
o	-fsanitize-address-use-after-scope	Enable use-after-scope detection in AddressSanitizer	
o	-fsanitize-address-use-odr-indicator	Enable ODR indicator globals to avoid false ODR violation reports in partially sanitized programs…	
o	-fsanitize-blacklist	Path to blacklist file for sanitizers	v=
o	-fsanitize-cfi-canonical-jump-tables	Make the jump table addresses canonical in the symbol table	
o	-fsanitize-cfi-cross-dso	Enable control flow integrity (CFI) checks for cross-DSO calls	
o	-fsanitize-cfi-icall-generalize-pointers	Generalize pointers in CFI indirect call type signature checks	
o	-fsanitize-coverage-allowlist	Restrict sanitizer coverage instrumentation exclusively to modules and functions that match the…	v=
o	-fsanitize-coverage-blacklist	Deprecated, use -fsanitize-coverage-blocklist= instead	v=
o	-fsanitize-coverage-blocklist	Disable sanitizer coverage instrumentation for modules and functions that match the provided…	v=
o	-fsanitize-coverage-whitelist	Deprecated, use -fsanitize-coverage-allowlist= instead	v=
o	-fsanitize-coverage	Specify the type of coverage instrumentation for Sanitizers	v=
o	-fsanitize-hwaddress-abi	Select the HWAddressSanitizer ABI to target (interceptor or platform, default interceptor). This…	v=
o	-fsanitize-memory-track-origins	Enable origins tracking in MemorySanitizer	V=
o	-fsanitize-memory-use-after-dtor	Enable use-after-destroy detection in MemorySanitizer	
o	-fsanitize-minimal-runtime		
o	-fsanitize-recover	Enable recovery for specified sanitizers	v=
o	-fsanitize-stats	Enable sanitizer statistics gathering	
o	-fsanitize-system-blacklist	Path to system blacklist file for sanitizers	v=
o	-fsanitize-thread-atomics	Enable atomic operations instrumentation in ThreadSanitizer (default)	
o	-fsanitize-thread-func-entry-exit	Enable function entry/exit instrumentation in ThreadSanitizer (default)	
o	-fsanitize-thread-memory-access	Enable memory access instrumentation in ThreadSanitizer (default)	
o	-fsanitize-trap	Enable trapping for sanitizers	v=
o	-fsanitize-undefined-strip-path-components	Strip (or keep only, if negative) a given number of path components when emitting check metadata	v=
o	-fsanitize	Turn on runtime checks for various forms of undefined or suspicious behavior. See user manual for…	v=
o	-fsave-optimization-record	Generate an optimization record file in a specific format	V=
o	-fseh-exceptions	Use SEH style exceptions	
o	-fsemantic-interposition		
o	-fshort-enums	Allocate to an enum type only as many bytes as it needs for the declared range of possible values	
o	-fshort-wchar	Force wchar_t to be a short unsigned int	
o	-fshow-column		
o	-fshow-overloads	Which overload candidates to show when overload resolution fails: best|all; defaults to all	v=
o	-fsigned-char	Char is signed	
o	-fsigned-zeros		
o	-fsized-deallocation	Enable C++14 sized global deallocation functions	
o	-fsjlj-exceptions	Use SjLj style exceptions	
o	-fslp-vectorize	Enable the superword-level parallelism vectorization passes	
o	-fsmall-block-descriptors	Enable small block descriptors	
o	-fspell-checking		
o	-fsplit-dwarf-inlining	Provide minimal debug info in the object/executable to facilitate online symbolication/stack…	
o	-fsplit-lto-unit	Enables splitting of the LTO unit	
o	-fsplit-machine-functions	Enable late function splitting using profile information (x86 ELF)	
o	-fstack-check	Enable stack checking	
o	-fstack-clash-protection	Enable stack clash protection	
o	-fstack-protector-all	Enable stack protectors for all functions	
o	-fstack-protector-strong	Enable stack protectors for some functions vulnerable to stack smashing. Compared to…	
o	-fstack-protector	Enable stack protectors for some functions vulnerable to stack smashing. This uses a loose…	
o	-fstack-size-section	Emit section containing metadata on function stack sizes	
o	-fstandalone-debug	Emit full debug info for all types used by the program	
o	-fstrict-enums	Enable optimizations based on the strict definition of an enum's value range	
o	-fstrict-float-cast-overflow	Assume that overflowing float-to-int casts are undefined (default)	
o	-fstrict-return		
o	-fstrict-vtable-pointers	Enable optimizations based on the strict rules for overwriting polymorphic C++ objects	
o	-fsycl	Enable SYCL kernels compilation for device	
o	-fsystem-module	Build this module as a system module. Only used with -emit-module	
o	-ftarget-variant-availability-checks	Enable availability checks for the target variant platform	
o	-ftest-coverage		
o	-fthin-link-bitcode	Write minimized bitcode to <file> for the ThinLTO thin link only	v=
o	-fthinlto-index	Perform ThinLTO importing using provided function summary index	v=
o	-fthreadsafe-statics		
o	-ftime-report	(For new pass manager) "per-pass": one report for each pass; "per-pass-run": one report for each…	v=
o	-ftime-trace-granularity	Minimum time granularity (in microseconds) traced by time profiler	v=
o	-ftime-trace	Turn on time profiler. Generates JSON file based on output filename	
o	-ftrap-function	Issue call to specified function rather than a trap instruction	v=
o	-ftrapv-handler	Specify the function to be called on overflow	v=
o	-ftrapv	Trap on integer overflow	
o	-ftrigraphs	Process trigraph sequences	
o	-ftrivial-auto-var-init-stop-after	Stop initializing trivial automatic stack variables after the specified number of instances	v=
o	-ftrivial-auto-var-init	Initialize trivial automatic stack variables: uninitialized (default) | pattern	v=
o	-funique-basic-block-section-names	Use unique names for basic block sections (ELF Only)	
o	-funique-internal-linkage-names	Uniqueify Internal Linkage Symbol Names by appending the MD5 hash of the module path	
o	-funique-section-names		
o	-funroll-loops	Turn on loop unroller	
o	-fuse-cxa-atexit		
o	-fuse-init-array		
o	-fuse-line-directives	Use #line in preprocessed output	
o	-fvalidate-ast-input-files-content	Compute and store the hash of input files used to build an AST. Files with mismatching mtime's are…	
o	-fveclib	Use the given vector functions library	v=
o	-fvectorize	Enable the loop vectorization passes	
o	-fverbose-asm	Generate verbose assembly output	
o	-fvirtual-function-elimination	Enables dead virtual function elimination optimization. Requires -flto=full	
o	-fvisibility-dllexport	The visibility for dllexport definitions [-fvisibility-from-dllstorageclass]	v=
o	-fvisibility-externs-dllimport	The visibility for dllimport external declarations [-fvisibility-from-dllstorageclass]	v=
o	-fvisibility-externs-nodllstorageclass	The visibility for external declarations without an explicit DLL dllstorageclass…	v=
o	-fvisibility-from-dllstorageclass	Set the visibility of symbols in the generated code from their DLL storage class	
o	-fvisibility-global-new-delete-hidden	Give global C++ operator new and delete declarations hidden visibility	
o	-fvisibility-inlines-hidden-static-local-var	When -fvisibility-inlines-hidden is enabled, static variables in inline C++ member functions will…	
o	-fvisibility-inlines-hidden	Give inline C++ member functions hidden visibility by default	
o	-fvisibility-ms-compat	Give global types 'default' visibility and global functions and variables 'hidden' visibility by…	
o	-fvisibility-nodllstorageclass	The visibility for defintiions without an explicit DLL export class…	v=
o	-fvisibility	Set the default symbol visibility for all global declarations	v=
o	-fwasm-exceptions	Use WebAssembly style exceptions	
o	-fwhole-program-vtables	Enables whole-program vtable optimization. Requires -flto	
o	-fwrapv	Treat signed integer overflow as two's complement	
o	-fwritable-strings	Store string literals as writable data	
o	-fxray-always-emit-customevents	Always emit __xray_customevent(...) calls even if the containing function is not always instrumented	
o	-fxray-always-emit-typedevents	Always emit __xray_typedevent(...) calls even if the containing function is not always instrumented	
o	-fxray-always-instrument	DEPRECATED: Filename defining the whitelist for imbuing the 'always instrument' XRay attribute	v=
o	-fxray-attr-list	Filename defining the list of functions/types for imbuing XRay attributes	v=
o	-fxray-function-groups	Only instrument 1 of N groups	v=
o	-fxray-function-index		
o	-fxray-ignore-loops	Don't instrument functions with loops unless they also meet the minimum function size	
o	-fxray-instruction-threshold	Sets the minimum function size to instrument with XRay	v=
o	-fxray-instrumentation-bundle	Select which XRay instrumentation points to emit. Options: all, none, function-entry…	v=
o	-fxray-instrument	Generate XRay instrumentation sleds on function entry and exit	
o	-fxray-link-deps	Tells clang to add the link dependencies for XRay	
o	-fxray-modes	List of modes to link in by default into XRay instrumented binaries	v=
o	-fxray-never-instrument	DEPRECATED: Filename defining the whitelist for imbuing the 'never instrument' XRay attribute	v=
o	-fxray-selected-function-group	When using -fxray-function-groups, select which group of functions to instrument. Valid range is 0…	v=
o	-fzero-initialized-in-bss		
o	-fzvector	Enable System z vector language extension	
o	-F	Add directory to framework include search path	v
o	--gcc-toolchain	Use the gcc toolchain at the given directory	v=
o	-gcodeview-ghash	Emit type record hashes in a .debug$H section	
o	-gcodeview	Generate CodeView debug information	
o	-gcolumn-info		
o	-gdwarf-2	Generate source-level debug information with dwarf version 2	
o	-gdwarf-3	Generate source-level debug information with dwarf version 3	
o	-gdwarf-4	Generate source-level debug information with dwarf version 4	
o	-gdwarf-5	Generate source-level debug information with dwarf version 5	
o	-gdwarf	Generate source-level debug information with the default dwarf version	
o	-gembed-source	Embed source text in DWARF debug sections	
o	-ginline-line-tables		
o	-gline-directives-only	Emit debug line info directives only	
o	-gline-tables-only	Emit debug line number tables only	
o	-gmodules	Generate debug info with external references to clang modules or precompiled headers	
o	-gno-codeview-ghash		
o	-gno-column-info		
o	-gno-embed-source	Restore the default behavior of not embedding source text in DWARF debug sections	
o	-gno-inline-line-tables	Don't emit inline line tables	
o	--gpu-instrument-lib	Instrument device library for HIP, which is a LLVM bitcode containing __cyg_profile_func_enter and…	v=
o	--gpu-max-threads-per-block	Default max threads per block for kernel launch bounds for HIP	v=
o	-gsplit-dwarf	Set DWARF fission mode to either 'split' or 'single'	v=
o	-gz	DWARF debug sections compression type	v=
o	-G	Put objects of at most <size> bytes into small data section (MIPS / Hexagon)	v
o	-g	Generate source-level debug information	
o	--help-hidden	Display help for hidden options	
o	-help	Display available options	
o	--hip-device-lib	HIP device library	v=
o	--hip-link	Link clang-offload-bundler bundles for HIP	
o	--hip-version	HIP version in the format of major.minor.patch	v=
o	-H	Show header includes and nesting depth	
o	-I-	Restrict all prior -I flags to double-quoted inclusion and remove current directory from include…	
o	-iapinotes-modules	Add directory to the API notes search path referenced by module name	v
o	-ibuiltininc	Enable builtin #include directories even when -nostdinc is used before or after -ibuiltininc…	
o	-idirafter	Add directory to AFTER include search path	v
o	-iframeworkwithsysroot	Add directory to SYSTEM framework search path, absolute paths are relative to -isysroot	v
o	-iframework	Add directory to SYSTEM framework search path	v
o	-imacros	Include macros from file before parsing	v
o	-include-pch	Include precompiled header file	v
o	-include	Include file before parsing	v
o	-index-header-map	Make the next included directory (-I or -F) an indexer header map	
o	-index-ignore-macros	Ignore macros during indexing	
o	-index-ignore-system-symbols	Ignore symbols from system headers	
o	-index-record-codegen-name	Record the codegen name for symbols	
o	-index-store-path	Enable indexing with the specified data store path	v
o	-index-unit-output-path	Use <path> as the output path for this compilation unit in the index unit file	v
o	-iprefix	Set the -iwithprefix/-iwithprefixbefore prefix	v
o	-iquote	Add directory to QUOTE include search path	v
o	-isysroot	Set the system root directory (usually /)	v
o	-isystem-after	Add directory to end of the SYSTEM include search path	v
o	-isystem	Add directory to SYSTEM include search path	v
o	-ivfsoverlay	Overlay the virtual filesystem described by file over the real file system	v
o	-iwithprefixbefore	Set directory to include search path with prefix	v
o	-iwithprefix	Set directory to SYSTEM include search path with prefix	v
o	-iwithsysroot	Add directory to SYSTEM include search path, absolute paths are relative to -isysroot	v
o	-I	Add directory to include search path. If there are multiple -I options, these directories are…	v
o	--libomptarget-nvptx-path	Path to libomptarget-nvptx libraries	v=
o	-L	Add directory to library search path	v
o	-mabi		v=
o	-mabicalls	Enable SVR4-style position-independent code (Mips only)	
o	-maix-struct-return	Return all structs in memory (PPC32 only)	
o	-malign-branch-boundary	Specify the boundary's size to align branches	v=
o	-malign-branch	Specify types of branches to align	v=
o	-malign-double	Align doubles to two words in structs (x86 only)	
o	-mbackchain	Link stack frames through backchain on System Z	
o	-mbranch-protection	Enforce targets of indirect branches and function returns	v=
o	-mbranches-within-32B-boundaries	Align selected branches (fused, jcc, jmp) within 32-byte boundary	
o	-mcmodel		v=
o	-mcmse	Allow use of CMSE (Armv8-M Security Extensions)	
o	-mcode-object-v3	Legacy option to specify code object ABI V2 (-mnocode-object-v3) or V3 (-mcode-object-v3) (AMDGPU…	
o	-mcode-object-version	Specify code object ABI version. Defaults to 3. (AMDGPU only)	v=
o	-mcrc	Allow use of CRC instructions (ARM/Mips only)	
o	-mcumode	Specify CU (-mcumode) or WGP (-mno-cumode) wavefront execution mode (AMDGPU only)	
o	-mdouble	Force double to be 32 bits or 64 bits	v=
o	-MD	Write a depfile containing user and system headers	
o	-meabi	Set EABI type, e.g. 4, 5 or gnu (default depends on triple)	v
o	-membedded-data	Place constants in the .rodata section instead of the .sdata section even if they meet the -G…	
o	-menable-experimental-extensions	Enable use of experimental RISC-V extensions	
o	-menable-unsafe-fp-math	Allow unsafe floating-point math optimizations which may decrease precision	
o	-mexec-model	Execution model (WebAssembly only)	v=
o	-mexecute-only	Disallow generation of data access to code sections (ARM only)	
o	-mextern-sdata	Assume that externally defined data is in the small data if it meets the -G <size> threshold (MIPS)	
o	-mfentry	Insert calls to fentry at function entry (x86/SystemZ only)	
o	-mfix-cortex-a53-835769	Workaround Cortex-A53 erratum 835769 (AArch64 only)	
o	-mfp32	Use 32-bit floating point registers (MIPS only)	
o	-mfp64	Use 64-bit floating point registers (MIPS only)	
o	-MF	Write depfile output from -MMD, -MD, -MM, or -M to <file>	v
o	-mgeneral-regs-only	Generate code which only uses the general purpose registers (AArch64 only)	
o	-mglobal-merge	Enable merging of globals	
o	-mgpopt	Use GP relative accesses for symbols known to be in a small data section (MIPS)	
o	-MG	Add missing headers to depfile	
o	-mharden-sls	Select straight-line speculation hardening scope	v=
o	-mhvx-length	Set Hexagon Vector Length	v=
o	-mhvx	Enable Hexagon Vector eXtensions	V=
o	-miamcu	Use Intel MCU ABI	
o	-mignore-xcoff-visibility	Not emit the visibility attribute for asm in AIX OS or give all symbols 'unspecified' visibility…	
o	--migrate	Run the migrator	
o	-mincremental-linker-compatible	(integrated-as) Emit an object file which can be used with an incremental linker	
o	-mindirect-jump	Change indirect jump instructions to inhibit speculation	v=
o	-mios-version-min	Set iOS deployment target	v=
o	-MJ	Write a compilation database entry per input	v
o	-mllvm	Additional arguments to forward to LLVM's option processing	v
o	-mlocal-sdata	Extend the -G behaviour to object local data (MIPS)	
o	-mlong-calls	Generate branches with extended addressability, usually via indirect jumps	
o	-mlong-double-128	Force long double to be 128 bits	
o	-mlong-double-64	Force long double to be 64 bits	
o	-mlong-double-80	Force long double to be 80 bits, padded to 128 bits for storage	
o	-mlvi-cfi	Enable only control-flow mitigations for Load Value Injection (LVI)	
o	-mlvi-hardening	Enable all mitigations for Load Value Injection (LVI)	
o	-mmacosx-version-min	Set Mac OS X deployment target	v=
o	-mmadd4	Enable the generation of 4-operand madd.s, madd.d and related instructions	
o	-mmark-bti-property	Add .note.gnu.property with BTI to assembly files (AArch64 only)	
o	-MMD	Write a depfile containing user headers	
o	-mmemops	Enable generation of memop instructions	
o	-mms-bitfields	Set the default structure layout to be compatible with the Microsoft compiler standard	
o	-mmsa	Enable MSA ASE (MIPS only)	
o	-mmt	Enable MT ASE (MIPS only)	
o	-MM	Like -MMD, but also implies -E and writes to stdout by default	
o	-mno-abicalls	Disable SVR4-style position-independent code (Mips only)	
o	-mno-backchain		
o	-mno-crc	Disallow use of CRC instructions (Mips only)	
o	-mno-embedded-data	Do not place constants in the .rodata section instead of the .sdata if they meet the -G <size>…	
o	-mno-execute-only	Allow generation of data access to code sections (ARM only)	
o	-mno-extern-sdata	Do not assume that externally defined data is in the small data if it meets the -G <size>…	
o	-mno-fix-cortex-a53-835769	Don't workaround Cortex-A53 erratum 835769 (AArch64 only)	
o	-mno-global-merge	Disable merging of globals	
o	-mno-gpopt	Do not use GP relative accesses for symbols known to be in a small data section (MIPS)	
o	-mno-hvx	Disable Hexagon Vector eXtensions	
o	-mno-implicit-float	Don't generate implicit floating point instructions	
o	-mno-incremental-linker-compatible	(integrated-as) Emit an object file which cannot be used with an incremental linker	
o	-mno-local-sdata	Do not extend the -G behaviour to object local data (MIPS)	
o	-mno-long-calls	Restore the default behaviour of not generating long calls	
o	-mno-lvi-cfi	Disable control-flow mitigations for Load Value Injection (LVI)	
o	-mno-lvi-hardening	Disable mitigations for Load Value Injection (LVI)	
o	-mno-madd4	Disable the generation of 4-operand madd.s, madd.d and related instructions	
o	-mno-memops	Disable generation of memop instructions	
o	-mno-movt	Disallow use of movt/movw pairs (ARM only)	
o	-mno-ms-bitfields	Do not set the default structure layout to be compatible with the Microsoft compiler standard	
o	-mno-msa	Disable MSA ASE (MIPS only)	
o	-mno-mt	Disable MT ASE (MIPS only)	
o	-mno-neg-immediates	Disallow converting instructions with negative immediates to their negation or inversion	
o	-mno-nvj	Disable generation of new-value jumps	
o	-mno-nvs	Disable generation of new-value stores	
o	-mno-outline-atomics	Don't generate local calls to out-of-line atomic operations	
o	-mno-outline	Disable function outlining (AArch64 only)	
o	-mno-packets	Disable generation of instruction packets	
o	-mno-pie-copy-relocations		
o	-mno-relax	Disable linker relaxation	
o	-mno-restrict-it	Allow generation of deprecated IT blocks for ARMv8. It is off by default for ARMv8 Thumb mode	
o	-mno-save-restore	Disable using library calls for save and restore	
o	-mno-seses	Disable speculative execution side effect suppression (SESES)	
o	-mno-speculative-load-hardening		
o	-mno-stack-arg-probe	Disable stack probes which are enabled by default	
o	-mno-tls-direct-seg-refs	Disable direct TLS access through segment registers	
o	-mno-unaligned-access	Force all memory accesses to be aligned (AArch32/AArch64 only)	
o	-mno-wavefrontsize64	Specify wavefront size 32 mode (AMDGPU only)	
o	-mnocrc	Disallow use of CRC instructions (ARM only)	
o	-mnop-mcount	Generate mcount/__fentry__ calls as nops. To activate they need to be patched in	
o	-mnvj	Enable generation of new-value jumps	
o	-mnvs	Enable generation of new-value stores	
o	-module-dependency-dir	Directory to dump module dependencies to	v
o	-module-file-info	Provide information about a particular module file	
o	-momit-leaf-frame-pointer	Omit frame pointer setup for leaf functions	
o	-moutline-atomics	Generate local calls to out-of-line atomic operations	
o	-moutline	Enable function outlining (AArch64 only)	
o	-mpacked-stack	Use packed stack layout (SystemZ only)	
o	-mpackets	Enable generation of instruction packets	
o	-mpad-max-prefix-size	Specify maximum number of prefixes to use for padding	v=
o	-mpie-copy-relocations	Use copy relocations support for PIE builds	
o	-mprefer-vector-width	Specifies preferred vector width for auto-vectorization. Defaults to 'none' which allows target…	v=
o	-MP	Create phony target for each dependency (other than main file)	
o	-mqdsp6-compat	Enable hexagon-qdsp6 backward compatibility	
o	-MQ	Specify name of main file output to quote in depfile	v
o	-mrecord-mcount	Generate a __mcount_loc section entry for each __fentry__ call	
o	-mrelax-all	(integrated-as) Relax all machine instructions	
o	-mrelax	Enable linker relaxation	
o	-mrestrict-it	Disallow generation of deprecated IT blocks for ARMv8. It is on by default for ARMv8 Thumb mode	
o	-mrtd	Make StdCall calling convention the default	
o	-msave-restore	Enable using library calls for save and restore	
o	-mseses	Enable speculative execution side effect suppression (SESES). Includes LVI control flow integrity…	
o	-msign-return-address	Select return address signing scope	v=
o	-msmall-data-limit	Put global and static data smaller than the limit into a special section	v=
o	-msoft-float	Use software floating point	
o	-mspeculative-load-hardening		
o	-mstack-alignment	Set the stack alignment	v=
o	-mstack-arg-probe	Enable stack probes	
o	-mstack-probe-size	Set the stack probe size	v=
o	-mstack-protector-guard-offset	Use the given offset for addressing the stack-protector guard	v=
o	-mstack-protector-guard-reg	Use the given reg for addressing the stack-protector guard	v=
o	-mstack-protector-guard	Use the given guard (global, tls) for addressing the stack-protector guard	v=
o	-mstackrealign	Force realign the stack at entry to every function	
o	-msve-vector-bits	Specify the size in bits of an SVE vector register. Defaults to the vector length agnostic value…	v=
o	-msvr4-struct-return	Return small structs in registers (PPC32 only)	
o	-mthread-model	The thread model to use, e.g. posix, single (posix by default)	v
o	-mtls-direct-seg-refs	Enable direct TLS access through segment registers (default)	
o	-mtls-size	Specify bit size of immediate TLS offsets (AArch64 ELF only): 12 (for 4KB) | 24 (for 16MB…	v=
o	-mtp	Thread pointer access method (AArch32/AArch64 only)	v=
o	-mtune	Only supported on X86 and RISC-V. Otherwise accepted for compatibility with GCC	v=
o	-MT	Specify name of main file output in depfile	v
o	-munaligned-access	Allow memory accesses to be unaligned (AArch32/AArch64 only)	
o	-munsafe-fp-atomics	Enable unsafe floating point atomic instructions (AMDGPU only)	
o	-MV	Use NMake/Jom format for the depfile	
o	-mwavefrontsize64	Specify wavefront size 64 mode (AMDGPU only)	
o	-M	Like -MD, but also implies -E and writes to stdout by default	
o	--no-cuda-include-ptx	Do not include PTX for the following GPU architecture (e.g. sm_35) or 'all'. May be specified more…	v=
o	--no-cuda-version-check	Don't error out if the detected version of the CUDA install is too low for the requested CUDA gpu…	
o	--no-offload-arch	Remove CUDA/HIP offloading device architecture (e.g. sm_35, gfx906) from the list of devices to…	v=
o	-no-pthread		
o	--no-system-header-prefix	Treat all #include paths starting with <prefix> as not including a system header	v=
o	-nobuiltininc	Disable builtin #include directories	
o	-nogpuinc	Do not add include paths for CUDA/HIP and do not include the default CUDA/HIP wrapper headers	
o	-nogpulib	Do not link device library for CUDA/HIP device compilation	
o	-nostdinc++	Disable standard #include directories for the C++ standard library	
o	-ObjC++	Treat source input files as Objective-C++ inputs	
o	-objcmt-atomic-property	Make migration to 'atomic' properties	
o	-objcmt-migrate-all	Enable migration to modern ObjC	
o	-objcmt-migrate-annotation	Enable migration to property and method annotations	
o	-objcmt-migrate-designated-init	Enable migration to infer NS_DESIGNATED_INITIALIZER for initializer methods	
o	-objcmt-migrate-instancetype	Enable migration to infer instancetype for method result type	
o	-objcmt-migrate-literals	Enable migration to modern ObjC literals	
o	-objcmt-migrate-ns-macros	Enable migration to NS_ENUM/NS_OPTIONS macros	
o	-objcmt-migrate-property-dot-syntax	Enable migration of setter/getter messages to property-dot syntax	
o	-objcmt-migrate-property	Enable migration to modern ObjC property	
o	-objcmt-migrate-protocol-conformance	Enable migration to add protocol conformance on classes	
o	-objcmt-migrate-readonly-property	Enable migration to modern ObjC readonly property	
o	-objcmt-migrate-readwrite-property	Enable migration to modern ObjC readwrite property	
o	-objcmt-migrate-subscripting	Enable migration to modern ObjC subscripting	
o	-objcmt-ns-nonatomic-iosonly	Enable migration to use NS_NONATOMIC_IOSONLY macro for setting property's 'atomic' attribute	
o	-objcmt-returns-innerpointer-property	Enable migration to annotate property with NS_RETURNS_INNER_POINTER	
o	-objcmt-whitelist-dir-path	Only modify files with a filename contained in the provided directory path	v=
o	-ObjC	Treat source input files as Objective-C inputs	
o	--offload-arch	CUDA offloading device architecture (e.g. sm_35), or HIP offloading target ID in the form of a…	v=
o	-o	Write output to <file>	v
o	-pg	Enable mcount instrumentation	
o	-pipe	Use pipes between commands, when possible	
o	--precompile	Only precompile the input	
o	-print-effective-triple	Print the effective target triple	
o	-print-file-name	Print the full library path of <file>	v=
o	-print-ivar-layout	Enable Objective-C Ivar layout bitmap print trace	
o	-print-libgcc-file-name	Print the library path for the currently used compiler runtime library ("libgcc.a" or…	
o	-print-prog-name	Print the full program path of <name>	v=
o	-print-resource-dir	Print the resource directory pathname	
o	-print-search-dirs	Print the paths used for finding libraries and programs	
o	-print-supported-cpus	Print supported cpu models for the given target (if target is not specified, it will print the…	
o	-print-target-triple	Print the normalized target triple	
o	-print-targets	Print the registered targets	
o	-pthread	Support POSIX threads in generated code	
o	--ptxas-path	Path to ptxas (used for compiling CUDA code)	v=
o	-P	Disable linemarker output in -E mode	
o	-Qn	Do not emit metadata containing compiler name and version	
o	-Qunused-arguments	Don't emit warning for unused driver arguments	
o	-Qy	Emit metadata containing compiler name and version	
o	-relocatable-pch	Whether to build a relocatable precompiled header	
o	-rewrite-legacy-objc	Rewrite Legacy Objective-C source to C++	
o	-rewrite-objc	Rewrite Objective-C source to C++	
o	--rocm-device-lib-path	ROCm device library path. Alternative to rocm-path	v=
o	--rocm-path	ROCm installation path, used for finding and automatically linking required bitcode libraries	v=
o	-Rpass-analysis	Report transformation analysis from optimization passes whose name matches the given POSIX regular…	v=
o	-Rpass-missed	Report missed transformations by optimization passes whose name matches the given POSIX regular…	v=
o	-Rpass	Report transformations performed by optimization passes whose name matches the given POSIX regular…	v=
o	-rtlib	Compiler runtime library to use	v=
o	-Rremark	Enable the specified remark	v
o	-save-stats	Save llvm statistics	V=
o	-save-temps	Save intermediate compilation results	V=
o	-serialize-diagnostics	Serialize compiler diagnostics to a file	v
o	-shared-libsan	Dynamically link the sanitizer runtime	
o	-static-libsan	Statically link the sanitizer runtime	
o	-static-openmp	Use the static host OpenMP runtime while linking	
o	-stdlib++-isystem	Use directory as the C++ standard library include path	v
o	-stdlib	C++ standard library to use	v=
o	-sycl-std	SYCL language standard to compile for	v=
o	--system-header-prefix	Treat all #include paths starting with <prefix> as including a system header	v=
o	-S	Only run preprocess and compilation steps	
o	-target-variant	Generate code that may run on a particular variant of the deployment target	v
o	--target	Generate code for the given target	v=
o	-Tbss	Set starting address of BSS to <addr>	v
o	-Tdata	Set starting address of DATA to <addr>	v
o	-time	Time individual commands	
o	-traditional-cpp	Enable some traditional CPP emulation	
o	-trigraphs	Process trigraph sequences	
o	-Ttext	Set starting address of TEXT to <addr>	v
o	-T	Specify <script> as linker script	v
o	-undef	Undef all system defines	
o	-unwindlib	Unwind library to use	v=
o	-U	Undefine macro <macro>	v
o	--verify-debug-info	Verify the binary representation of debug output	
o	-verify-pch	Load and verify that a pre-compiled header file is not stale	
o	--version	Print version information	
o	-v	Show commands to run and use verbose output	
o	-Wa	Pass the comma separated arguments in <arg> to the assembler	v
o	-Wdeprecated	Enable warnings for deprecated constructs and define __DEPRECATED	
o	-Wl	Pass the comma separated arguments in <arg> to the linker	v
o	-working-directory	Resolve file paths relative to the specified directory	v
o	-Wp	Pass the comma separated arguments in <arg> to the preprocessor	v
o	-Wwarning	Enable the specified warning	v
o	-w	Suppress all warnings	
o	-Xanalyzer	Pass <arg> to the static analyzer	v
o	-Xarch_device	Pass <arg> to the CUDA/HIP device compilation	v
o	-Xarch_host	Pass <arg> to the CUDA/HIP host compilation	v
o	-Xassembler	Pass <arg> to the assembler	v
o	-Xclang	Pass <arg> to the clang compiler	v
o	-Xcuda-fatbinary	Pass <arg> to fatbinary invocation	v
o	-Xcuda-ptxas	Pass <arg> to the ptxas assembler	v
o	-Xlinker	Pass <arg> to the linker	v
o	-Xopenmp-target	Pass <arg> to the target offloading toolchain identified by <triple>	V
o	-Xpreprocessor	Pass <arg> to the preprocessor	v
o	-x	Treat subsequent input files as having type <language>	v
o	-z	Pass -z <arg> to the linker	v
o	-std	Language standard to compile for	v=
a	1	1
=		--analyzer-output
v	html	
v	plist	
v	plist-multi-file	
v	plist-html	
v	sarif	
v	text	
=		-B
t	folders
=		-cxx-isystem
t	folders
=		-dsym-dir
t	folders
=		-fapinotes-cache-path
t	folders
=		-fcf-protection
v	return	
v	branch	
v	full	
v	none	
=		-fcs-profile-generate
t	folders
=		-fembed-bitcode
v	off	
v	all	
v	bitcode	
v	marker	
=		-flto
v	full	
v	thin	
=		-fmodules-cache-path
t	folders
=		-fmodules-user-build-path
t	folders
=		-fprebuilt-module-path
t	folders
=		-fprofile-instr-generate
t	filepaths
=		-iapinotes-modules
t	folders
=		-iframeworkwithsysroot
t	folders
=		-iprefix
t	folders
=		-iquote
t	folders
=		-isysroot
t	folders
=		-isystem-after
t	folders
=		-isystem
t	folders
=		-iwithprefixbefore
t	folders
=		-iwithprefix
t	folders
=		-iwithsysroot
t	folders
=		-I
t	folders
=		-L
t	folders
=		-mabi
v	vec-default	Enable the default Altivec ABI on AIX (AIX only). Uses only volatile vector registers
v	vec-extabi	Enable the extended Altivec ABI on AIX (AIX only). Uses volatile and nonvolatile vector registers
=		-mcmodel
v	small	
v	medium	
v	medany	
v	medlow	
=		-stdlib++-isystem
t	folders
=		-std
v	c++98	ISO C++ 1998 with amendments
v	c++03	ISO C++ 1998 with amendments
v	gnu++98	ISO C++ 1998 with amendments and GNU extensions
v	gnu++03	ISO C++ 1998 with amendments and GNU extensions
v	c++11	ISO C++ 2011 with amendments
v	gnu++11	ISO C++ 2011 with amendments and GNU extensions
v	c++14	ISO C++ 2014 with amendments
v	gnu++14	ISO C++ 2014 with amendments and GNU extensions
v	c++17	ISO C++ 2017 with amendments
v	gnu++17	ISO C++ 2017 with amendments and GNU extensions
v	c++20	ISO C++ 2020 DIS
v	gnu++20	ISO C++ 2020 DIS with GNU extensions
v	c++2b	Working draft for ISO C++ 2023 DIS
v	gnu++2b	Working draft for ISO C++ 2023 DIS with GNU extensions
v	clc++	C++ for OpenCL 1.0
v	clc++1.0	C++ for OpenCL 1.0
v	clc++2021	C++ for OpenCL 2021
v	cuda	NVIDIA CUDA(tm)
v	hip	HIP
v	hlsl	High Level Shader Language
v	hlsl2015	High Level Shader Language 2015
v	hlsl2016	High Level Shader Language 2016
v	hlsl2017	High Level Shader Language 2017
v	hlsl2018	High Level Shader Language 2018
v	hlsl2021	High Level Shader Language 2021
v	hlsl202x	High Level Shader Language 202x
#		1
t	filepaths
