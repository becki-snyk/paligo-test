::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-language-and-package-manager-support/snyk-for-php.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-387be396-85ed-eaf9-17fc-da850c517731}Snyk for PHP {#snyk-for-php .title}
:::

</div>
:::

Snyk offers security scanning to test your projects for vulnerabilities,
both through your CLI and through different integrations from our UI.

The following describes how to use Snyk to scan your PHP projects:

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45481204665680}Features {#features .title}
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
| [Composer]( | ✔︎          | ✔︎          | ✔︎          |             |
| https://get |             |             |             |             |
| composer.or |             |             |             |             |
| g){.link}   |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| [Composer]( | ✔︎          | ✔︎          | ✔︎          |             |
| https://get |             |             |             |             |
| composer.or |             |             |             |             |
| g){.link}   |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm45481204673168}How it works {#how-it-works .title}
:::

</div>
:::

Once we've built the tree, we can use our [vulnerability
database](https://snyk.io/vuln){.link} to find vulnerabilities in any of
the packages anywhere in the dependency tree.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

In order to scan your dependencies, you must ensure you have first
installed the relevant package manager, and that your project contains
the supported manifest files.

The way by which Snyk analyzes and builds the tree varies depending on
the language and package manager of the project, as well as the location
of your project:

::: {.itemizedlist}
-   [Snyk CLI tool for PHP
    projects](snyk-for-php.html#UUID-387be396-85ed-eaf9-17fc-da850c517731_N1657252523908 "Snyk CLI tool for PHP projects"){.link}

-   [Git settings for PHP
    projects](snyk-for-php.html#UUID-387be396-85ed-eaf9-17fc-da850c517731_section-idm461305475914563314503645092 "Git services for PHP projects"){.link}
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-387be396-85ed-eaf9-17fc-da850c517731_N1657252523908}Snyk CLI tool for PHP projects {#snyk-cli-tool-for-php-projects .title}
:::

</div>
:::

The way by which Snyk analyzes and builds the tree varies depending on
the language and package manager of the project.

In order to build the dependency tree Snyk analyzes the
`composer.json`{.code} and `composer.lock`{.code} files that it finds to
analyze the dependencies and their versions.
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-387be396-85ed-eaf9-17fc-da850c517731_UUID-26b8c425-6b67-028e-4a49-48982bb329cf}CLI parameters for PHP {#cli-parameters-for-php .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-387be396-85ed-eaf9-17fc-da850c517731_section-idm4613054401284833145033520691}Prerequisites {#prerequisites .title}
:::

</div>
:::

::: {.itemizedlist}
-   Ensure you've installed the relevant package manager before you
    begin using the Snyk CLI tool.

-   Ensure you've included the relevant manifest files supported by Snyk
    before testing.

-   Install and authenticate the Snyk CLI to start analyzing projects
    from your local environment.
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm45481204649984}Parameters {#parameters .title}
:::

</div>
:::

There are no unique parameters when running Snyk for PHP.

Read more about Snyk CLI in [Getting started with the
CLI](file:///Users/becki/Downloads/user-docs-main/docs/snyk-cli/getting-started-with-the-cli/){.link}.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-387be396-85ed-eaf9-17fc-da850c517731_section-idm461305475914563314503645092}Git services for PHP projects {#git-services-for-php-projects .title}
:::

</div>
:::

PHP projects can be imported from any of the Git services we support.
Once imported, Snyk analyzes your projects based on their supported
manifest files.

Once you select a project for import, we build the dependency tree based
on these manifest files:

::: {.itemizedlist}
-   composer.json

-   composer.lock
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-387be396-85ed-eaf9-17fc-da850c517731_section-idm4501246838078433145037318243}Git settings for PHP {#git-settings-for-php .title}
:::

</div>
:::

By default, Snyk scans your production dependencies. From the Snyk UI
you can configure whether to include your development dependencies
(`require_dev`{.code}) in the scan for vulnerabilities.

To update language preferences:

::: {.procedure}
1.  Log in to your account and navigate to the relevant group and
    organization that you want to manage

2.  Click on settings
    [![cog\_icon.png](image/uuid-3408a45a-8e5a-70aa-7e67-796708f1364e.png)]{.inlinemediaobject} \>
    [**Languages**]{.bold .bold}.

3.  Click [**Edit settings**]{.bold .bold} for PHP and select [**Scan
    dev dependencies**]{.bold .bold} to set for your PHP projects in the
    specific organization to include both development and production
    dependencies.

4.  Click [**Update settings**]{.bold .bold}.
:::

These settings will then be applied to all newly imported projects, and
once re-tested, to all existing projects.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-387be396-85ed-eaf9-17fc-da850c517731_section-idm4536643521556833145037440571}Troubleshooting for your PHP projects {#troubleshooting-for-your-php-projects .title}
:::

</div>
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-387be396-85ed-eaf9-17fc-da850c517731_section-idm4613054377131233145041935191}Error messages {#error-messages .title}
:::

</div>
:::

The following error messages may appear for you when working with your
PHP projects:

::: {.itemizedlist}
-   composer.json or composer.lock not found in path

-   Manifest file not found in path

-   Lockfile missing packages property

-   Lockfile or manifest file is not a valid JSON
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#UUID-387be396-85ed-eaf9-17fc-da850c517731_section-idm4536643523984033145042404161}Support {#support .title}
:::

</div>
:::

If you run across any of these, or other issues, send the following
files to us at <support@snyk.io> and we'll help you out:

::: {.itemizedlist}
-   `composer.json`{.code}

-   `composer.lock`{.code}
:::
:::
:::
:::
