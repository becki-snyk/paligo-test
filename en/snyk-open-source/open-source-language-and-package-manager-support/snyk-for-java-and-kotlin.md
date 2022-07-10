::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-language-and-package-manager-support/snyk-for-java-and-kotlin.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420}Snyk for Java and Kotlin {#snyk-for-java-and-kotlin .title}
:::

</div>
:::

Snyk offers security scanning to test your projects for vulnerabilities,
both through your CLI and through different integrations from our UI.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45726181637456}Features {#features .title}
:::

</div>
:::

The following tables provide an outline of the general features Snyk
offers by language. In addition to these features, we offer additional
functionality related to the specific integration configurations.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::

Note

Some features might not be available, depending on your pricing plan.
See [pricing plans](https://snyk.io/plans/){.link} for more details.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::

Note

Gradle projects imported via Git are tested by parsing
`build.gradle`{.code} files. As the only truly reliable way to resolve
Gradle dependencies is to execute the tool itself, this method can
sometimes provide incomplete results.

If possible, enable
[lockfiles](file:///Users/becki/Downloads/user-docs-main/docs/products/snyk-open-source/language-and-package-manager-support/snyk-for-java-gradle-maven.md#git-services-for-gradle-projects){.link}
in your Gradle project to improve the accuracy for Git imports.

However, for the most accurate results, we recommend using the [Snyk
CLI](file:///Users/becki/Downloads/user-docs-main/docs/snyk-cli/){.link}
to test Gradle projects.

 

[ **Java** ]{.bold .bold}

::: {.informaltable .table-responsive}
+-------------+-------------+-------------+-------------+-------------+
| Package     | CLI support | Git support | License     | Fix PRs     |
| managers /  |             |             | scanning    |             |
| Features    |             |             |             |             |
+=============+=============+=============+=============+=============+
| [Maven](htt | ✔︎          | ✔︎          | ✔︎          | ✔︎          |
| ps://maven. |             |             |             |             |
| apache.org) |             |             |             |             |
| {.link}     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| [Gradle](ht | ✔︎          | ✔︎          | ✔︎          | [Fix        |
| tps://gradl |             |             |             | advice](fil |
| e.org){.lin |             |             |             | e:///Users/ |
| k}          |             |             |             | becki/Downl |
|             |             |             |             | oads/user-d |
|             |             |             |             | ocs-main/do |
|             |             |             |             | cs/features |
|             |             |             |             | /fixing-and |
|             |             |             |             | -prioritizi |
|             |             |             |             | ng-issues/s |
|             |             |             |             | tarting-to- |
|             |             |             |             | fix-vulnera |
|             |             |             |             | bilities/fi |
|             |             |             |             | x-your-vuln |
|             |             |             |             | erabilities |
|             |             |             |             | .md){.link} |
|             |             |             |             | only        |
+-------------+-------------+-------------+-------------+-------------+
:::

[ **Kotlin** ]{.bold .bold}

::: {.informaltable .table-responsive}
+-----------+-----------+-----------+-----------+-----------+-----------+
| Package   | CLI       | Git       | License   | Fixing    | Runtime   |
| managers  | support   | support   | scanning  |           | monitorin |
| /         |           |           |           |           | g         |
| Features  |           |           |           |           |           |
+===========+===========+===========+===========+===========+===========+
| [Gradle]( | ✔︎        |           | ✔︎        | [Fix      | ✔︎        |
| https://g |           |           |           | advice](f |           |
| radle.org |           |           |           | ile:///Us |           |
| ){.link}  |           |           |           | ers/becki |           |
|           |           |           |           | /Download |           |
|           |           |           |           | s/user-do |           |
|           |           |           |           | cs-main/d |           |
|           |           |           |           | ocs/featu |           |
|           |           |           |           | res/fixin |           |
|           |           |           |           | g-and-pri |           |
|           |           |           |           | oritizing |           |
|           |           |           |           | -issues/s |           |
|           |           |           |           | tarting-t |           |
|           |           |           |           | o-fix-vul |           |
|           |           |           |           | nerabilit |           |
|           |           |           |           | ies/fix-y |           |
|           |           |           |           | our-vulne |           |
|           |           |           |           | rabilitie |           |
|           |           |           |           | s.md){.li |           |
|           |           |           |           | nk}       |           |
|           |           |           |           | only      |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45726181636528}Supported versions {#supported-versions .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_section-idm4572746412539233129770580105}Maven {#maven .title}
:::

</div>
:::

::: {.itemizedlist}
-   CLI - Maven `3.*`{.code} ([more
    details](https://github.com/snyk/snyk-mvn-plugin#support){.link})

-   Git - Maven `3.*`{.code}
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_section-idm4534824151782433129774130383}Gradle {#gradle .title}
:::

</div>
:::

::: {.itemizedlist}
-   CLI - Gradle `2.*`{.code}, `3.*`{.code}, `4.*`{.code}, `5.*`{.code},
    `6.*`{.code} ([more
    details](https://github.com/snyk/snyk-gradle-plugin#support){.link})

-   Git - Gradle `2.*`{.code}, `3.*`{.code},`4.*`{.code}, `5.*`{.code},
    `6.*`{.code}
:::
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45726181642944}Snyk CLI tool for Java and Kotlin projects (CI/CD) {#snyk-cli-tool-for-java-and-kotlin-projects-cicd .title}
:::

</div>
:::

The way Snyk analyzes and builds the dependencies varies depending on
the language and package manager of the project.

Learn how to use the tool for your Java projects as follows:

::: {.itemizedlist}
-   Snyk CLI with Gradle: To build the dependency graph, Snyk integrates
    with Gradle and inspects the dependencies returned by the build. The
    following manifest files are supported: `build.gradle`{.code} and
    `build.gradle.kts`{.code}

-   Snyk CLI with Maven: To build the dependency tree, Snyk analyzes the
    output of the `pom.xml`{.code} files.
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_UUID-4cef2f60-1a88-c72b-e04a-9a78065edfed}CLI parameters for Java and Kotlin {#cli-parameters-for-java-and-kotlin .title}
:::

</div>
:::

This section describes the unique CLI commands available when working
with Java-based projects as follows:

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_section-idm4602926052396833129780873501}Prerequisites {#prerequisites .title}
:::

</div>
:::

::: {.itemizedlist}
-   Install the relevant package manager before you use the Snyk CLI
    tool.

-   Include the relevant manifest files supported by Snyk before
    testing.

-   Install and authenticate the Snyk CLI to start analyzing projects
    from your local environment. See [Getting started with the
    CLI](file:///Users/becki/Downloads/user-docs-main/docs/snyk-cli/getting-started-with-the-cli/){.link}.
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45726181584656}Snyk CLI parameters {#snyk-cli-parameters .title}
:::

</div>
:::

When working with Gradle projects from our CLI, you can add any of the
following options to further refine the way the scan works:

::: {.informaltable .table-responsive}
+-----------------------------------+-----------------------------------+
| [**Option**]{.bold .bold}         | [**Description**]{.bold .bold}    |
+===================================+===================================+
| `--sub-project=`{.code}           | For Gradle "multi-project"        |
|                                   | configurations, test a specific   |
|                                   | sub-project.                      |
+-----------------------------------+-----------------------------------+
| `--all-sub-projects`{.code}       | For "multi-project"               |
|                                   | configurations, test all          |
|                                   | sub-projects.                     |
+-----------------------------------+-----------------------------------+
| `--configuration-matching=`{.code | Resolve dependencies using only   |
| }                                 | configuration(s) that match the   |
|                                   | provided Java regular expression. |
|                                   | For example:                      |
|                                   | `'^releaseRuntimeClasspath$'`{.co |
|                                   | de}                               |
+-----------------------------------+-----------------------------------+
| `--configuration-attributes=`{.co | Select certain values of          |
| de}                               | configuration attributes to       |
|                                   | resolve the dependencies. For     |
|                                   | example:                          |
|                                   | `'buildtype:release,usage:java-ru |
|                                   | ntime'`{.code}                    |
+-----------------------------------+-----------------------------------+
| `--all-projects`{.code}           | Use for monorepos. This will      |
|                                   | detect all supported manifests.   |
|                                   | For Gradle monorepos Snyk will    |
|                                   | only look for root level          |
|                                   | [**build.gradle /                 |
|                                   | build.gradle.kts**]{.bold .bold}  |
|                                   | files and apply the same logic as |
|                                   | `--all-sub-projects`{.code}       |
|                                   | behind the scenes. This command   |
|                                   | is designed to be run in the root |
|                                   | of your monorepo.                 |
+-----------------------------------+-----------------------------------+
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45726181580816}Pass extra arguments directly to Gradle or Maven via Snyk CLI {#pass-extra-arguments-directly-to-gradle-or-maven-via-snyk-cli .title}
:::

</div>
:::

You can pass any extra Gradle or Maven arguments directly to
[**gradle**]{.bold .bold} or [**mvn**]{.bold .bold} by providing them
after a Snyk command like so:

``` {.programlisting}
snyk test -- --build-cache
```

[**Examples of how you can use Maven arguments with the Snyk
CLI**]{.bold .bold}

Test a specific Maven profile called "prod".

``` {.programlisting}
snyk test -- -prod
```

Add a system property from your pom.xml file.

For example:

The package version appears in your pom.xml

``` {.programlisting}
${pkg_version}
```

Define the system property like this:

``` {.programlisting}
snyk test -- -Dpkg_version=1.4
```
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_UUID-7d1216c3-d709-027a-e7f6-66553f34381d}CLI help for Gradle projects {#cli-help-for-gradle-projects .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_section-idm4572746242496033129794588627}Sub-projects {#sub-projects .title}
:::

</div>
:::

Gradle build can consist of several sub-projects, where each sub-project
has its own build.gradle, while the root project is the only one that
also includes a `settings.gradle`{.code} file. Sub-projects depend on
the root project, but can be configured otherwise.

By default, Snyk CLI scans only the current project (the project in the
root of the current folder), or the project that is specified by
`--file=path/to/build.gradle`{.code}).

::: {.itemizedlist}
-   To scan all projects at once (recommended), use the
    `--all-sub-projects`{.code} flag:

    ``` {.programlisting}
    snyk test --all-sub-projects
    ```
:::

[**Note:**]{.bold .bold} Each of the individual sub-projects appears as
a separate Snyk project in the UI.

::: {.itemizedlist}
-   To scan a specific project (for example, [*myapp*]{.emphasis}):

    ``` {.programlisting}
    snyk test --sub-project=myapp
    ```
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45726181555536}Configurations {#configurations .title}
:::

</div>
:::

Gradle dependencies are declared for a particular scope, each scope is
represented by Gradle with the help of
[Configurations](https://docs.gradle.org/current/userguide/declaring_dependencies.html#sec:what-are-dependency-configurations){.link}.
For example:

::: {.itemizedlist}
-   [**compileOnly**]{.bold .bold} configuration for development
    dependencies

-   [**compile**]{.bold .bold} configuration that includes compile and
    runtime dependencies
:::

By default Snyk merges all configurations returned by Gradle to
dependency graph based on the sum total of the dependencies across all
configurations in the project/projects.

To test a specific configuration:

::: {.itemizedlist}
-   Use the `--configuration-matching`{.code} option with a [Java
    regular
    expression](https://docs.oracle.com/javase/tutorial/essential/regex/){.link}
    (case-insensitive) as its parameter. The configuration that matches
    is then tested. If several configurations match, they are all merged
    and resolved together. For example:
    `'^releaseRuntimeClasspath$|^compile$'`{.code}

-   If the different sub-projects include different configurations, scan
    each sub-project separately.
:::

[ **Examples of how you can use the --configuration-matching:** ]{.bold
.bold}

::: {.itemizedlist}
-   `--configuration-matching=compile`{.code} will match compile,
    testCompile, compileOnly etc;

-   `--configuration-matching=^compile$`{.code} will match only compile;

-   `--configuration-matching='^(debug|release)compile$'`{.code} will
    match debugCompile and releaseCompile

-   `--configuration-matching='^(?!.*test).*$'`{.code} will match all
    configurations [*except*]{.emphasis} those containing the string
    "test"
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45726181556512}Android build variants {#android-build-variants .title}
:::

</div>
:::

Android Gradle supports creating different versions of your app by
configuring [build
variants.](https://developer.android.com/studio/build/build-variants){.link}

Since Snyk defaults to merging all available configurations the variants
will result in a clash of un-mergeable configurations.

In such cases, Snyk scan fails with an error from Gradle which may
contain one of the following messages:

::: {.itemizedlist}
-   [ *Cannot choose between the following configurations of
    `project :mymodulewithvariants`{.code}* ]{.emphasis}

-   [ *Cannot choose between the following variants of
    `project :mymodulewithvariants`{.code}* ]{.emphasis}

-   [ *Could not select value from candidates* ]{.emphasis}
:::

To avoid such conflicts:

::: {.itemizedlist}
-   [**Use a specific configuration(s):**]{.bold .bold} if you know of a
    build configuration that has all the required attributes and the
    configuration is identical across all sub-projects included in the
    test, specify that configuration.For example:

    ``` {.programlisting}
    --configuration-matching=prodReleaseRuntimeClasspath
    ```

-   [**Explicitly specify the dependency configuration:**]{.bold .bold}
    modify intra-project dependencies in your build.gradle file(s) to
    use a specific configuration

    ``` {.programlisting}
      dependencies {
          implementation project(path: ':mymodulewithvariants', configuration: 'default')
      }
    ```

-   [**Suggest configuration attributes:**]{.bold .bold} if you receive
    an error when running the command, the error may indicate which
    attribute values are available, while the error details from Gradle
    also indicate which dependency variants match which attributes.
    Using these details, add the attribute filter option.For example:

    ``` {.programlisting}
    snyk test --configuration-attributes=buildtype:release,usage:java-runtime,mode:demo
    ```

    matches the variants using
    `com.android.build.api.attributes.BuildTypeAttr=release`{.code} and
    `org.gradle.usage=java-runtime`{.code}
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45726181537872}Daemon {#daemon .title}
:::

</div>
:::

By default, Snyk passes `gradle build --no-daemon`{.code} in the
background when running `snyk test`{.code} and `snyk monitor`{.code}. If
for any reason, you run into trouble, try this:

::: {.orderedlist}
1.  Start the Gradle daemon.

2.  Add `--daemon`{.code} to your `snyk test`{.code} or
    `snyk monitor`{.code}.
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45726181525728}Lockfiles {#lockfiles .title}
:::

</div>
:::

If your Gradle project makes use of a single [**gradle.lockfile**]{.bold
.bold} or multiple [**\*.lockfile**]{.bold .bold} per configuration and
you are having the following issue

[ **Gradle Error (short): \> Could not resolve all dependencies for
configuration ':compileOnly'. \> Locking strict mode: Configuration
':compileOnly' is locked but does not have lock state.** ]{.bold .bold}

Bear in mind that [**compileOnly configuration**]{.bold .bold} [**has
been deprecated**]{.bold .bold} and even if your project successfully
generates a lockfile, it will not contain `compileOnly`{.code} state
because this configuration cannot be resolved. Only resolvable
configurations compute a dependency graph. In order to solve this issue
we suggest you [**update your build.gradle containing dependencyLocking
logic with the following instruction**]{.bold .bold}

``` {.programlisting}
compileOnly {resolutionStrategy.deactivateDependencyLocking() }
```

This will [**ignore compileOnly**]{.bold .bold} and save only the
necessary information to analyse your project/projects.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45726181521344}Support {#support .title}
:::

</div>
:::

If you are having any trouble testing your Gradle projects with Snyk,
collect the following details and send them to us at <support@snyk.io>
so we can help you out:

::: {.itemizedlist}
-   `build.gradle`{.code}

-   `settings.gradle`{.code} (especially if we did not pick up a version
    of a package)

-   The output from the following commands:

    ::: {.itemizedlist}
    -   `$ snyk test -d`{.code}

    -   `$ gradle dependencies -q`{.code}
    :::
:::
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_UUID-69fe2b55-8a5f-c6f1-83c8-8596c6fc1429}Git services for Maven projects {#git-services-for-maven-projects .title}
:::

</div>
:::

After you select a project for import, we build the dependency tree
based on the `pom.xml`{.code} file.
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_UUID-097f7109-f8d3-4dae-0f42-46c4a34478f0}Git services for Gradle projects {#git-services-for-gradle-projects .title}
:::

</div>
:::

After you select a project for import, we build the dependency tree
based on the `build.gradle`{.code} file and (optional)
`gradle.lockfile`{.code}.

If a lockfile is present, Snyk will use it to accurately resolve the
final version of dependencies used in the project.

Gradle lockfiles are an opt-in feature that, among other benefits,
enable reproducible builds.Read more about Gradle dependency locking at
<https://docs.gradle.org/current/userguide/dependency_locking.html>

::: {.warning style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Warning\]](../css/image/warning.png)
:::
:::

Warning

[**Kotlin**]{.bold .bold}: `build.gradle.kts`{.code} files are not
currently supported in Git.

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_UUID-ee4facf4-49c0-57e7-55f5-6f3db4f9194f}Git settings for Java {#git-settings-for-java .title}
:::

</div>
:::

From the Snyk UI you can specify mirrors or repositories from which
you'd like to resolve packages in Artifactory for Maven.

See the page below for more details on configuring the Artifactory
integration.

{% content-ref
url="../../../features/integrations/private-registry-integrations/artifactory-registry-for-maven.md"
%}
[artifactory-registry-for-maven.md](file:///Users/becki/Downloads/user-docs-main/docs/features/integrations/private-registry-integrations/artifactory-registry-for-maven.md){.link}
{% endcontent-ref %}
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-524289e3-15e0-2341-ef2b-6f0574cfa420_UUID-77f12c3a-7b0f-d134-facb-863bb9ade3d8}Additional Snyk support for Java {#additional-snyk-support-for-java .title}
:::

</div>
:::

In addition to the CLI and Snyk UI features, you can also check your
Java projects with these integrations.

{% content-ref
url="../../../features/integrations/ci-cd-integrations/maven-plugin-integration.md"
%}
[maven-plugin-integration.md](file:///Users/becki/Downloads/user-docs-main/docs/features/integrations/ci-cd-integrations/maven-plugin-integration.md){.link}
{% endcontent-ref %}
:::
