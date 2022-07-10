::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-language-and-package-manager-support/snyk-for-elixir.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-2956ce47-6662-3100-8d26-172718348d1c}Snyk for Elixir {#snyk-for-elixir .title}
:::

</div>
:::

Snyk offers security scanning to test your Elixir projects for
vulnerabilities using the CLI.

::: {.table .table-responsive}
[]{#idm45192790178896}

**Table 1. Features**

::: {.table .table-responsive-contents}
+-------------+-------------+-------------+-------------+-------------+
| Package     | CLI support | Git support | License     | Fix PRs     |
| managers /  |             |             | scanning    |             |
| Features    |             |             |             |             |
+=============+=============+=============+=============+=============+
| [Mix](https | ✔︎          |             |             |             |
| ://hexdocs. |             |             |             |             |
| pm/mix/Mix. |             |             |             |             |
| html){.link |             |             |             |             |
| }/[Hex](htt |             |             |             |             |
| ps://hex.pm |             |             |             |             |
| ){.link}    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
:::
:::

\

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45192790175184}How it works {#how-it-works .title}
:::

</div>
:::

Snyk builds a dependency tree for your project by analyzing your
manifest and lock files.

After Snyk builds the tree, Snyk uses our [vulnerability
database](https://snyk.io/vuln){.link} to find vulnerabilities in the
packages anywhere in the dependency tree.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45192790177808}Snyk CLI tool for Elixir projects {#snyk-cli-tool-for-elixir-projects .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-2956ce47-6662-3100-8d26-172718348d1c_section-idm4602926128864033129432274794}Mix/Hex {#mixhex .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::
:::

Note

To scan your dependencies, first install Elixir and Mix. For details,
[see here](https://elixir-lang.org/install.html){.link}.

Mix is a build tool that provides tasks for creating, compiling, and
testing Elixir projects, managing its dependencies, and more.

Mix manages dependencies by integrating with the Hex package manager.

To build the dependency tree, Snyk analyzes your `mix.exs`{.code} and
`mix.lock`{.code} files. The `mix.lock`{.code} file must be present and
in sync with the `mix.exs`{.code} file.

[**Project naming**]{.bold .bold}

Projects in the Snyk UI are named according to the `app`{.code} keyword
from the `project/0`{.code} function exported by `Mix.Project`{.code} in
the main `mix.exs`{.code} file.

To override the name, use the `--project-name`{.code} CLI parameter.

[**Umbrella projects**]{.bold .bold}

If you test a Mix Umbrella project, Snyk detects that this is an
umbrella project and includes all the child apps automatically.

Along with the main `mix.exs`{.code}, each app `mix.exs`{.code} appears
as a separate project in the Snyk UI, named according to the path to the
app.

[**Dependency types**]{.bold .bold}

Snyk fully supports all `:hex`{.code} packages listed in the Mix
project, including all their transitive dependencies and any
vulnerabilities.

Hex support includes both Elixir and Erlang packages.

Snyk also has limited support for `:path`{.code}, `:git`{.code} and
`:github`{.code} dependencies, but not their transitive dependencies or
vulnerabilities.

::: {.itemizedlist}
-   `:path`{.code} dependencies appear in the dependency tree by name

-   `:git`{.code} and `:github`{.code} dependencies appear in the
    dependency tree by repository URL and version (either
    `:branch`{.code}, `:tag`{.code} or `:ref`{.code}, as defined in the
    `mix.exs`{.code} file)
:::
