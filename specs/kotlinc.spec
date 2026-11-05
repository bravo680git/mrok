@	
s	-version	Display the compiler version
s	-nowarn	Suppress the compiler from displaying warnings during compilation
s	-Werror	Turn any warnings into a compilation error
s	-verbose	Enable verbose logging output which includes details of the compilation process
s	-script	Evaluate a Kotlin script file. When called with this option, the compiler executes the first…
s	-help|-h	Display usage information and exit. Only standard options are shown. To show advanced options, use…
s	-X	Display information about the advanced options and exit. These options are currently unstable…
s	-kotlin-home	Specify a custom path to the Kotlin compiler used for the discovery of runtime libraries
s	-P	Pass an option to a Kotlin compiler plugin. Available plugins and their options are listed in the…
s	-language-version	Provide source compatibility with the specified version of Kotlin
s	-api-version	Allow using declarations only from the specified version of Kotlin bundled libraries
s	-progressive	Enable the progressive mode for the compiler. In the progressive mode, deprecations and bug fixes…
s	-opt-in	Enable usages of API that requires opt-in with a requirement annotation specified by the given…
s	-classpath|-cp	Search for class files in the specified paths. Separate elements of the classpath with system path…
s	-d	Place the generated class files into the specified location. The location can be a directory, a…
s	-include-runtime	Include the Kotlin runtime into the resulting JAR file. Makes the resulting archive runnable on…
s	-jdk-home	Use a custom JDK home directory to include into the classpath if it differs from the default…
s	-jvm-target	Specify the target version of the generated JVM bytecode. Possible values are 1.8, 9, 10, ..., 21…
s	-java-parameters	Generate metadata for Java 1.8 reflection on method parameters
s	-module-name	Set a custom name for the generated .kotlin_module file
s	-no-jdk	Don't automatically include the Java runtime into the classpath
s	-no-reflect	Don't automatically include the Kotlin reflection (kotlin-reflect.jar) into the classpath
s	-no-stdlib	Don't automatically include the Kotlin/JVM stdlib (kotlin-stdlib.jar) and Kotlin reflection…
s	-script-templates	Script definition template classes. Use fully qualified class names and separate them with commas…
@	-version
@	-nowarn
@	-Werror
@	-verbose
@	-script
a	1	0
#	-script	1
t	filepaths
@	-help
@	-X
@	-kotlin-home
a	1	0
#	-kotlin-home	1
t	filepaths
@	-P
a	1	0
@	-language-version
a	1	0
@	-api-version
a	1	0
@	-progressive
@	-opt-in
a	1	0
@	-classpath
a	1	0
#	-classpath	1
t	filepaths
@	-d
a	1	0
#	-d	1
t	filepaths
@	-include-runtime
@	-jdk-home
a	1	0
#	-jdk-home	1
t	folders
@	-jvm-target
a	1	0
@	-java-parameters
@	-module-name
a	1	0
@	-no-jdk
@	-no-reflect
@	-no-stdlib
@	-script-templates
a	1	0
