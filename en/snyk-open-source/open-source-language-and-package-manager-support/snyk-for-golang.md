::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-language-and-package-manager-support/snyk-for-golang.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-1a7f79b1-15ed-3d2b-204c-a2ba42527763}Snyk for Golang {#snyk-for-golang .title}
:::

</div>
:::

Snyk supports testing and monitoring of Go projects that have their
dependencies managed by [Go Modules](https://golang.org/ref/mod){.link},
[dep](https://github.com/golang/dep){.link} and
[govendor](https://github.com/kardianos/govendor){.link}.

The following describes how to use Snyk to scan your Go projects:

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45877869617168}Features {#features .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::

Note

Features might not be available, depending on your subscription plan.

::: {.informaltable .table-responsive}
+-------------+-------------+-------------+-------------+-------------+
| Package     | CLI support | Git support | License     | Fix PRs     |
| managers /  |             |             | scanning    |             |
| Features    |             |             |             |             |
+=============+=============+=============+=============+=============+
| [Go         | ✔︎          | ✔︎          | ✔︎          |             |
| Modules](ht |             |             |             |             |
| tps://golan |             |             |             |             |
| g.org/ref/m |             |             |             |             |
| od){.link}  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| [dep](https | ✔︎          | ✔︎          | ✔︎          |             |
| ://github.c |             |             |             |             |
| om/golang/d |             |             |             |             |
| ep){.link}  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| [govendor]( | ✔︎          | ✔︎          | ✔︎          |             |
| https://git |             |             |             |             |
| hub.com/kar |             |             |             |             |
| dianos/gove |             |             |             |             |
| ndor){.link |             |             |             |             |
| }           |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45877869614080}How it works {#how-it-works .title}
:::

</div>
:::

Once we've built the tree, we can use our [vulnerability
database](https://snyk.io/vuln){.link} to find vulnerabilities in any of
the modules or packages anywhere in the dependency tree.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

In order to scan your dependencies in the CLI, you must ensure you have
first installed the relevant package manager, and that your project
contains the supported manifest files.

The way by which Snyk analyzes and builds the tree varies depending on
the language and package manager of the project, as well as the location
of your project.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45877869648160}Snyk CLI tool for Go projects {#snyk-cli-tool-for-go-projects .title}
:::

</div>
:::

[ **Go Modules** ]{.bold .bold}

In order to build the dependency tree Snyk uses the
`go list -json -deps`{.code} command.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

Snyk scans Go Modules projects in the CLI at the [*package*]{.emphasis}
level rather than on the [*module*]{.emphasis} level, as we have full
access to your project source code.This is beneficial since you might
use a vulnerable module but not the vulnerable package.

When testing Go Modules projects via the CLI Snyk does not require
dependencies to be installed, but you must have a `go.mod`{.code} file
at the root of your project, `go list`{.code} uses this and your project
source code to build a complete dependency tree.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::

Note

Different versions of the Go generate different results for the [**go
list -json -deps**]{.bold .bold} command. This can affect the dependency
tree and the vulnerabilities that the Snyk CLI will find.

[ **Dep** ]{.bold .bold}

In order to build the dependency tree Snyk analyzes your
`Gopkg.lock`{.code} files.

When testing dep projects via the CLI Snyk requires dependencies to be
installed, run `dep ensure`{.code} to achieve this.

[ **Govendor** ]{.bold .bold}

In order to build the dependency tree Snyk analyzes your
`vendor/vendor.json`{.code} files.

When testing Govendor projects via the CLI Snyk requires dependencies to
be installed, run `govendor sync`{.code} to achieve this.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45877869604544}Git services for Go projects {#git-services-for-go-projects .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-1a7f79b1-15ed-3d2b-204c-a2ba42527763_section-idm4572746381846433129443708238}Go Modules {#go-modules .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::

Note

For Go Modules projects imported via Git, dependencies are resolved at
the [*module*]{.emphasis} level rather than the [*package*]{.emphasis}
level, as we do not have full access to your project source code.This
means you may see more issues (including potential false positives)
reported than for projects tested in the CLI, as we report all
vulnerabilities for each module not just the package(s) referenced in
your source code.

In order to build the dependency tree Snyk runs the
`go mod graph`{.code} command using the `go.mod`{.code} files in the
selected repository.

[ **Private modules** ]{.bold .bold}

Go Modules projects that depend on modules from private Git repositories
are supported where the private repositories are in the same Git
organization as the main project repository.

Imports for projects with private modules from repos in other Git
organizations will fail. Support for private module dependencies from
other Git organizations is planned for the future.

Private modules are supported for GitHub and Bitbucket Cloud. GitLab,
GitHub Enterprise and Bitbucket Server are not currently supported.

[ **Broker** ]{.bold .bold}

Projects imported via the new [Snyk
Broker](https://docs.snyk.io/integrations/snyk-broker/broker-introduction){.link}
clients should work as expected.

To add support to existing clients created before Dec 30th 2020, you
should add `go.mod`{.code} and `go.sum`{.code} to your
`accept.json`{.code} file, as per the changes in this [pull
request](https://github.com/snyk/broker/pull/299/files){.link}.

If you are using private Go Modules (repositories) integrated via the
broker, note that we require each private module to have a
`go.mod`{.code} file defined.

[ **Dep** ]{.bold .bold}

In order to build the dependency tree Snyk analyzes the
`Gopkg.lock`{.code} files in the selected repository.

[ **Govendor** ]{.bold .bold}

In order to build the dependency tree Snyk analyzes the
`vendor/vendor.json`{.code} files in the selected repository.
