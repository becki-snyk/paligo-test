::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-language-and-package-manager-support/snyk-for-c---c--.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509}Snyk for C / C++ {#snyk-for-c-c .title}
:::

</div>
:::

You can use Snyk to scan C / C++ projects.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45417500990112}Features {#features .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::

Note

Some features may not be available, depending on your subscription plan.

::: {.informaltable .table-responsive}
+-------------+-------------+-------------+-------------+-------------+
| Package     | CLI support | Git support | License     | Fix PRs     |
| managers /  |             |             | scanning    |             |
| Features    |             |             |             |             |
+=============+=============+=============+=============+=============+
| C/C++       | ✔︎          |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45417500988384}How it works {#how-it-works .title}
:::

</div>
:::

Scans are powered by an open source database, periodically updated with
the latest source code from different online sources.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

To navigate through the vulnerabilities for C/C++, use the [Snyk Vuln
DB](https://security.snyk.io){.link}.

When you run the `snyk test --unmanaged`{.code} command, Snyk:

::: {.orderedlist}
1.  Converts all files from your current folder into a list of hashes.

2.  Sends the hashes to Snyk scan server.

3.  Queries the database to find a list of potentially matching
    dependencies.

4.  Links the dependencies to the known vulnerabilities.

5.  Displays the results.
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::

Note

To scan the project, the dependencies must be available as source code
in the scanned directory. If the dependencies are in a different
location, that location must be scanned.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500983264}Scanning archives {#scanning-archives .title}
:::

</div>
:::

By default, archives are not scanned. However, Snyk CLI can recursively
extract archives to analyze the source code inside.

To enable archive extraction, specify the depth of the extraction using
the `--max-depth`{.code} option.

The supported archive formats are:

::: {.itemizedlist}
-   zip-like archives

-   tar

-   tar with gzip compression algorithm
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509_UUID-b076a521-aff4-6a3c-dff0-36cdcd743aee}Constraints and limitations {#constraints-and-limitations .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509_section-idm4572746349641633129395774572}Dependencies source code needs to be available {#dependencies-source-code-needs-to-be-available .title}
:::

</div>
:::

For Snyk CLI to be able to find dependencies in your source code, enough
of the full dependencies source code needs to be present in the scanned
folder.

Having a large percentage of files in their original (unchanged) form is
critical to accurately identify dependencies and report the correct set
of vulnerabilities back. Modifying that source code reduces the
confidence of the scanning engine resulting in less accurate results.
Other potential issues could include dependencies not being identified
or being identified incorrectly (as a different version or even a
different package).

The example below shows a typical package with dependencies listed:

``` {.programlisting}
c-example
├── deps
│   ├── curl-7.58.0
│   │   ├── include
│   │   │   ├── Makefile.am
│   │   │   ├── Makefile.in
│   │   │   ├── README
│   │   │   └── curl
│   │   ├── install-sh
│   │   ├── lib
│   │   │   ├── asyn.h
│   │   │   ├── base64.c
│   │   │   ├── checksrc.pl
│   │   │   ├── config-amigaos.h
│   │   │   ├── conncache.c
│   │   │   ├── conncache.h
│   │   ├── src
│   │   │   ├── tool_binmode.c
│   │   │   ├── tool_binmode.h
│   │   │   ├── tool_bname.c
│   │   │   ├── tool_xattr.c
...
```
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500974560}Data collection note {#data-collection-note .title}
:::

</div>
:::

When you scan C++ projects, the following data is collected and may be
stored for troubleshooting purposes:

::: {.informaltable .table-responsive}
+-----------------------------------+-----------------------------------+
| Category                          | Description                       |
+===================================+===================================+
| Hashes of the scanned files       | All files are converted to a list |
|                                   | of irreversible hashes.           |
+-----------------------------------+-----------------------------------+
| Relative paths to scanned files   | The paths to files relative to    |
|                                   | the directory being scanned are   |
|                                   | included for better               |
|                                   | identification and matching.      |
|                                   |                                   |
|                                   | Example:                          |
|                                   | `./project-name/vendor/bzip2-1.0. |
|                                   | 6/blocksort.c`{.code}             |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509_UUID-9c6d3cc6-0f07-6ae8-45ca-16b545949188}Snyk CLI for C / C++ projects {#snyk-cli-for-c-c-projects .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500974752}Install the Snyk CLI {#install-the-snyk-cli .title}
:::

</div>
:::

C/C++ scanning is available in [Snyk
CLI](file:///Users/becki/Downloads/user-docs-main/docs/snyk-cli/){.link}.
See [Install the
CLI](file:///Users/becki/Downloads/user-docs-main/docs/snyk-cli/install-the-snyk-cli/){.link}
for details.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::

Note

The minimum version of Snyk CLI with C/C++ scanning is 1.857.0.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500961760}Run the test {#run-the-test .title}
:::

</div>
:::

To test your project for vulnerabilities, run:

``` {.programlisting}
$ snyk test --unmanaged
```

::: {.warning style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Warning\]](../css/image/warning.png)
:::
:::

Warning

If you scan a Linux project on Windows, make sure the repository is
cloned with Linux line endings. See the [Known
Issues](snyk-for-c---c--.html#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509_UUID-fd022da0-b15a-0c3d-9d02-77b33992ddf6 "Known issues"){.link}
section for more details.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500958848}Displaying dependencies {#displaying-dependencies .title}
:::

</div>
:::

To display dependencies, use the `--print-deps`{.code} option:

``` {.programlisting}
$ snyk test --unmanaged --print-deps

Dependencies:

  cpython|https://github.com/python/cpython/archive/v3.7.2.zip@3.7.2
  confidence: 1.000
  
  zip|http://ftp.debian.org/debian/pool/main/z/zip/zip_3.0.orig.tar.gz@3.0
  confidence: 0.993
```

To learn what files contributed to each dependency being identified, use
the `--print-dep-paths`{.code} option:

``` {.programlisting}
$ snyk test --unmanaged --print-dep-paths

Dependencies:

  curl|https://github.com/curl/curl/releases/download/curl-7_58_0/curl-7.58.0.tar.xz@7.58.0
  confidence: 1.000
  matching files:
    - c-example/deps/curl-7.58.0/CHANGES
    - c-example/deps/curl-7.58.0/CMake/CMakeConfigurableFile.in
    - c-example/deps/curl-7.58.0/CMake/CurlSymbolHiding.cmake
    ... and 2857 more files
```
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500955664}Understanding the confidence level {#understanding-the-confidence-level .title}
:::

</div>
:::

You may need to change the source code of the dependencies that you use
in your software. As Snyk uses file signatures to find the closest
possible match to an open source library, your changes may decrease the
accuracy of the identification of the actual library.

To learn how confident Snyk is about the identified dependency and its
version, use the `--print-deps`{.code} or `--print-dep-paths`{.code}
command line option:

``` {.programlisting}
curl|https://github.com/curl/curl/releases/download/curl-7_58_0/curl-7.58.0.tar.xz@7.58.0
confidence: 0.993
```

This confidence level shows how confident Snyk is about the actual
identification of the dependency. The number can be between 0 and 1 and
the higher it is, the more accurate the identification is. So a
confidence of [**1**]{.bold .bold} means that all the files in the
source tree fully matched all the expected files in our database.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500952352}JSON output {#json-output .title}
:::

</div>
:::

To get a machine-readable output in JSON, use the `--json`{.code}
option:

``` {.programlisting}
$ snyk test --unmanaged --json
[
  {
    "issues": [
      {
        "pkgName": "curl|https://github.com/curl/curl/releases/download/curl-7_58_0/curl-7.58.0.tar.xz",
        "pkgVersion": "7.58.0",
        "issueId": "CVE-2019-5481",
        "fixInfo": {
          "isPatchable": false,
          "isPinnable": false
        }
      }
    ],
    "issuesData": {
      "CVE-2019-5481": {
        "severity": "high",
        "CVSSv3": "",
        "originalSeverity": "high",
        "severityWithCritical": "high",
        "type": "vuln",
        "alternativeIds": [
          ""
        ],
        "creationTime": "2019-09-16T19:15:00.000Z",
        "disclosureTime": "2019-09-16T19:15:00.000Z",
        "modificationTime": "2020-10-20T22:15:00.000Z",
        "publicationTime": "2019-09-16T19:15:00.000Z",
        "credit": [
          ""
        ],
        "id": "CVE-2019-5481",
        "packageManager": "cpp",
        "packageName": "curl|https://github.com/curl/curl/releases/download/curl-7_58_0/curl-7.58.0.tar.xz",
        "language": "cpp",
        "fixedIn": [
          ""
        ],
        "patches": [],
        "exploit": "No Data",
        "functions": [
          ""
        ],
        "semver": {
          "vulnerable": [
            "7.58.0"
          ],
          "vulnerableHashes": [
            ""
          ],
          "vulnerableByDistro": {}
        },
        "references": [
          {
            "title": "https://curl.haxx.se/docs/CVE-2019-5481.html",
            "url": "https://curl.haxx.se/docs/CVE-2019-5481.html"
          },
        ],
        "internal": {},
        "identifiers": {
          "CVE": [
            "CVE-2019-5481"
          ],
          "CWE": [],
          "ALTERNATIVE": [
            ""
          ]
        },
        "title": "CVE-2019-5481",
        "description": "",
        "license": "",
        "proprietary": true,
        "nearestFixedInVersion": ""
      }
    },
    "fileSignaturesDetails": {
      "curl|https://github.com/curl/curl/releases/download/curl-7_58_0/curl-7.58.0.tar.xz@7.58.0": {
        "filePaths": [
          "deps/curl-7.58.0/CHANGES",
          "c-example/deps/curl-7.58.0/CMake/CMakeConfigurableFile.in",
          "c-example/deps/curl-7.58.0/CMake/CurlSymbolHiding.cmake"
        ],
        "confidence": 1
      }
    }
  }
]
```
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509_UUID-c4e112ee-216e-b6f9-dd0b-2fcfac9630f8}Command line options {#command-line-options .title}
:::

</div>
:::

The following `snyk`{.code} command line options are supported with the
`snyk test --unmanaged`{.code} and `snyk monitor --unmanaged`{.code}
commands:

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500937920}ORG\_ID {#org_id .title}
:::

</div>
:::

`--org=<ORG_ID>`{.code}

Specify the `<ORG_ID>`{.code} to run Snyk commands tied to a specific
organization. This defines where new projects are created after running
the `snyk monitor`{.code} command. Some features have availability and
private testing limits. If you have multiple organizations, you can set
a default from the CLI using:

``` {.programlisting}
snyk config set org=ORG_ID
```

Setting a default ensures all newly monitored projects are created under
your default organization. To override the default, use the
`--org=<ORG_ID>`{.code} argument.

Default: `<ORG_ID>`{.code} that is the current preferred organization in
your [Account settings](https://app.snyk.io/account){.link}.

For more information see the article [How to select the organization to
use in the
CLI](https://support.snyk.io/hc/en-us/articles/360000920738-How-to-select-the-organization-to-use-in-the-CLI){.link}.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500937488}json {#json .title}
:::

</div>
:::

`--json`{.code}

Prints results in JSON format.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500930304}OUTPUT\_FILE\_PATH {#output_file_path .title}
:::

</div>
:::

`--json-file-output=<OUTPUT_FILE_PATH>`{.code}

(only in test command) Save test output in JSON format directly to the
specified file, regardless of whether or not you use the `--json`{.code}
option.

This is useful to display the human-readable test output via stdout and
at the same time save the JSON format output to a file.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500928368}target-dir {#target-dir .title}
:::

</div>
:::

`--target-dir <directory>`{.code}

Scan the path specified in the argument instead of the current
directory.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::

Note

Alternatively, you can run just
`snyk test --unmanaged <directory>`{.code}

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500926064}max-depth {#max-depth .title}
:::

</div>
:::

`--max-depth=1`{.code}

Specify the maximum level of archive extraction. Use `0`{.code} to
disable archive extraction completely.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500923664}project-name {#project-name .title}
:::

</div>
:::

`--project-name=c-project`{.code}

When used with the `snyk monitor --unmanaged`{.code} command, you can
override the default name Snyk gives your snapshots by entering your
desired name using the `--project-name`{.code} flag.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500921744}remote-repo-url {#remote-repo-url .title}
:::

</div>
:::

`--remote-repo-url=<URL>`{.code}

Set or override the remote URL for the repository that you would like to
monitor.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500919248}target-reference {#target-reference .title}
:::

</div>
:::

`--target-reference=<TARGET_REFERENCE>`{.code}

When used with the `snyk monitor --unmanaged`{.code} command, you can
specify a reference which differentiates this project, for example, a
branch name or version. Projects having the same reference can be
grouped based on that reference.
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509_UUID-19923b0f-9350-c2d6-97c5-1a452cfa2862}Import scan results in the Snyk Web UI {#import-scan-results-in-the-snyk-web-ui .title}
:::

</div>
:::

To import the test results (issues and dependencies) in the Snyk Web UI,
run the `snyk monitor --unmanaged`{.code} command:

``` {.programlisting}
$ snyk monitor --unmanaged
Monitoring /c-example (c-example)...

Explore this snapshot at https://app.snyk.io/org/example-org/project/8ac0e233-d0f9-403e-b422-5970e7a37443/history/5de4616d-3967-485f-bf21-bbbe91068029

Notifications about newly disclosed issues related to these dependencies will be emailed to you.
```

This creates a snapshot of dependencies and vulnerabilities and imports
them into the Snyk Web UI, where you can review the issues and see them
included in your reports.

Importing a project with unmanaged dependencies creates a new project:

::: {.informalfigure}
[]{#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509_figure-idm4572746260835233129413821753}

::: {.mediaobject}
![Project with unmanaged
dependencies](image/uuid-50daa495-7e8f-4b39-0dc2-0829886b97e7.png)

::: {.caption}
Project with unmanaged dependencies
:::
:::
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509_UUID-fd022da0-b15a-0c3d-9d02-77b33992ddf6}Known issues {#known-issues .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500900976}Scanning on Windows {#scanning-on-windows .title}
:::

</div>
:::

Many open source projects in git use Unix line endings. By default, git
on Windows converts Unix line endings to Windows line endings and only
converts them back for the actual commits. The Snyk database contains
source code signatures with the original line endings (as defined in the
individual projects), so when you scan on Windows, the signatures
generated for the files with Windows line endings are different from the
signatures in the Snyk database. In that case, it is very likely no
dependencies will be found.

To scan a project with Unix line endings on Windows, disable git line
endings conversion. To configure this globally, run:

``` {.programlisting}
git config --global core.autocrlf false
```
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-d8e93f23-8d71-b7e1-a36c-c8832351c509_UUID-75860dc8-d7af-9ecc-eab6-2fd5dfbc4ff7}Frequently asked questions {#frequently-asked-questions .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500893888}Is my source code sent to Snyk servers? {#is-my-source-code-sent-to-snyk-servers .title}
:::

</div>
:::

No. The files are converted to a list of hashes before they are sent for
scanning.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45417500893536}Why did Snyk not find any dependencies? {#why-did-snyk-not-find-any-dependencies .title}
:::

</div>
:::

Snyk stores the official releases of many of open source components in
the Snyk database but it is possible that the source code you scanned is
not there or is not found. If your scan does not find any dependencies
[submit a request to
support](https://snyk.zendesk.com/agent/dashboard){.link}.

Here are a few things that you can check on your own:

::: {.itemizedlist}
-   The source code of the dependencies you scanned is actually
    available as source code (unpacked) in the folder that you scanned.
    If you use a package manager, such as Conan, the source code is
    likely to be in the Conan cache, along with the source code of other
    dependencies of your other projects. To scan dependencies managed by
    a package manager, we recommend that you do that in a clean
    environment (for example during a build).

-   The source code of the dependencies is not from an official release
    of the OSS component, and Snyk does not have it in the database

-   The source code of the OSS has been modified too much, so Snyk
    cannot detect it. If there are too few files and you modify most of
    them, Snyk cannot match them to a component from our database.
    Examples of common modifications are whitespace formatting and
    adding license or copyright headers.

-   You are on Windows, and git converted line endings to Windows line
    endings. Currently Snyk can recognize files that have retained their
    original line endings.

-   The source code of the OSS components is too new. The Snyk database
    is refreshed monthly but it takes time for the latest releases to
    get processed.
:::
:::
:::
