::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-language-and-package-manager-support/snyk-for-javascript.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-0a5c8df0-a97a-cb60-4d06-7ed4588bd0b7}Snyk for JavaScript {#snyk-for-javascript .title}
:::

</div>
:::

You can use Snyk to scan your JavaScript projects.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm46180810297792}Features {#features .title}
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
| npm         | ✔︎          | ✔︎          | ✔︎          | ✔           |
+-------------+-------------+-------------+-------------+-------------+
| Yarn        | ✔︎          | ✔︎          | ✔︎          | ✔︎          |
+-------------+-------------+-------------+-------------+-------------+
| Yarn        | ✔︎          | ✔︎          | ✔           | ✖️          |
| Workspaces  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm46180810296864}How it works {#how-it-works .title}
:::

</div>
:::

After Snyk builds a dependency tree, we use our [vulnerability
database](https://snyk.io/vuln){.link} to find vulnerabilities in any of
the packages anywhere in that tree.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

To scan your dependencies, ensure you install the relevant package
manager, and that your project contains the supported manifest files.

The way Snyk analyzes and builds the tree varies depending on the
language and package manager of the project, as well as the location of
your project.

See:

::: {.itemizedlist}
-   [Snyk CLI tool for JavaScript
    projects](snyk-for-javascript.html#UUID-0a5c8df0-a97a-cb60-4d06-7ed4588bd0b7_UUID-5e8d5cb6-41f3-9a82-cff5-c75f4953f39c "Snyk CLI tool for JavaScript projects"){.link}

-   [Git services for JavaScript
    projects](snyk-for-javascript.html#UUID-0a5c8df0-a97a-cb60-4d06-7ed4588bd0b7_UUID-2e09910b-a75f-537b-3d63-7da069a4cde0 "Git services for JavaScript projects"){.link}
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-0a5c8df0-a97a-cb60-4d06-7ed4588bd0b7_UUID-5e8d5cb6-41f3-9a82-cff5-c75f4953f39c}Snyk CLI tool for JavaScript projects {#snyk-cli-tool-for-javascript-projects .title}
:::

</div>
:::

The way Snyk analyzes and builds the tree varies based on the package
manager of the project.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm46180810283168}npm {#npm .title}
:::

</div>
:::

npm versions 6.x, 7.x are supported in the Snyk CLI.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::

Note

Workspaces npm 7.x is not supported.

We analyze your `package.json`{.code} and `package-lock.json`{.code}
files, to build a full structured dependency tree. If the
`package-lock.json`{.code} is missing, we analyze your
`node_modules`{.code} folder.

Snyk can apply previously selected patches using the GNU patch utility.
Patches are saved to the .snyk policy file.

[**Peer dependencies**]{.bold .bold} are scanned by default in npm v7.x
[*unless*]{.emphasis} they are explicitly marked as optional in the
`peerDependenciesMeta`{.code} object of the `package.json`{.code} (In
npm v6.x add `--peer-dependencies`{.code} to your command, as these are
not installed by default).

``` {.programlisting}
"peerDependenciesMeta": {
        "cache-manager": {
          "optional": true
        },
```

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm46180810281920}Yarn {#yarn .title}
:::

</div>
:::

Yarn versions 1 & 2 are supported in the Snyk CLI.

We analyze your `package.json`{.code} and `yarn.lock`{.code} files, to
build a full structured dependency tree. If the `yarn.lock`{.code} is
missing, we analyze your `node_modules`{.code} folder.

Snyk supports resolutions only in Yarn v2. We do not support resolutions
for Yarn v1.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm46180810282800}Yarn workspaces {#yarn-workspaces .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

Yarn v1 & 2 workspaces support is for `snyk test`{.code} and
`snyk monitor`{.code} commands only at this time.

::: {.warning .danger style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Warning\]](../css/image/warning.png)
:::

Warning

nohoist is [**not**]{.bold .bold} supported for Yarn workspaces.

For Yarn workspaces use the `--all-projects`{.code} flag to test and
monitor your packages alongside other projects or
`--yarn-workspaces`{.code} to specifically scan Yarn workspaces projects
only. The root lock file is referenced when scanning all the packages.
Use the `--detection-depth`{.code} parameter to find sub-folders that
are not auto-discovered by default.

Example
usage:`snyk test --all-projects --strict-out-of-sync=false --detection-depth=6`{.code}
which will scan the packages that belong to any discovered workspaces
this directly and 5 sub-directories deep as well as any other projects
detected.

`snyk test --yarn-workspaces --strict-out-of-sync=false --detection-depth=6`{.code}
which will scan only the Yarn workspace packages that belong to any
discovered workspaces this directly and 5 sub-directories deep.

You may use a common [**.snyk**]{.bold .bold} policy file if you
maintain ignores/patches in one place to be applied for all detected
workspaces by providing the policy path:

`snyk test --all-projects --strict-out-of-sync=false --policy-path=src/.snyk`{.code}

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm46180810271296}Lerna {#lerna .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

We currently do [**not**]{.bold .bold} support Lerna. However, if your
Lerna project is using Yarn Workspaces then the project can be scanned
with the standard Yarn Workspaces support. You [*might*]{.emphasis} be
able to run Snyk test/monitor with the following workaround commands to
help you unblock the Snyk CLI integration.

For each example-package you can do:

`snyk monitor --file=packages/example-package/package.json`{.code}

Alternatively, you can specify a script to automate scanning nested
\``` package.json` ``{.code}files:

`ls packages | xargs -I PKG_NAME snyk monitor --file=packages/PKG_NAME/package.json`{.code}

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm46180810282240}CLI parameters for JavaScript {#cli-parameters-for-javascript .title}
:::

</div>
:::

Prerequisites

::: {.itemizedlist}
-   Install the relevant package manager.

-   Include the relevant manifest files supported by Snyk.

-   Install and authenticate [the Snyk
    CLI](https://docs.snyk.io/snyk-cli/install-the-snyk-cli){.link} to
    start analyzing projects from your local environment.
:::

Run `npm install`{.code} or `yarn install,`{.code} depending on the
package manager you use for your JavaScript projects.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

As snyk test looks at the locally installed modules, it needs to be run
after npm install or yarn install, and will seamlessly work with
shrinkwrap, npm enterprise or any other custom installation logic you
have.

[ **Parameters** ]{.bold .bold}

Use the following options to refine the scan:

::: {.informaltable .table-responsive}
+-----------------------+-----------------------+-----------------------+
| [ **Option** ]{.bold  |                       | [ **Description**     |
| .bold}                |                       | ]{.bold .bold}        |
+=======================+=======================+=======================+
| `--strict-out-of-sync | [**true**]{.bold      | Prevent testing       |
| `{.code}              | .bold},false          | out-of-sync lockfiles |
|                       |                       | (test fails when set  |
|                       |                       | to true if there are  |
|                       |                       | out-of-sync lockfiles |
|                       |                       | in the project)       |
+-----------------------+-----------------------+-----------------------+
| `--fail-on`{.code}    | [**all**]{.bold       | Configure when a test |
|                       | .bold}, upgradable,   | should be failed if   |
|                       | patchable             | there are             |
|                       |                       | vulnerabilities as    |
|                       |                       | follows:              |
|                       |                       |                       |
|                       |                       | ::: {.itemizedlist}   |
|                       |                       | -   All-fail for all  |
|                       |                       |     projects          |
|                       |                       |     containing        |
|                       |                       |     vulnerabilities   |
|                       |                       |                       |
|                       |                       | -   Upgradable-fail   |
|                       |                       |     only for projects |
|                       |                       |     with              |
|                       |                       |     vulnerabilities   |
|                       |                       |     that can be fixed |
|                       |                       |     with package      |
|                       |                       |     upgrades          |
|                       |                       |                       |
|                       |                       | -   Patchable-fail    |
|                       |                       |     for projects with |
|                       |                       |     vulnerabilities   |
|                       |                       |     that can be fixed |
|                       |                       |     with either       |
|                       |                       |     upgrades or       |
|                       |                       |     patches           |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| `--prune-repeated-sub | true,                 | Use this flag if any  |
| dependencies`{.code}  | [**false**]{.bold     | big projects fail to  |
|                       | .bold}                | be tested. Default is |
|                       |                       | [*false*]{.emphasis}  |
+-----------------------+-----------------------+-----------------------+
| `--dev`{.code}        | true,                 | Set to true if Snyk   |
|                       | [**false**]{.bold     | should scan dev       |
|                       | .bold}                | dependencies          |
+-----------------------+-----------------------+-----------------------+
| `--yarn-workspaces`{. | [ **n/a** ]{.bold     | Provide this flag to  |
| code}                 | .bold}                | only scan a Yarn      |
|                       |                       | workspace project     |
|                       |                       | where lockfile is in  |
|                       |                       | the root. By default  |
|                       |                       | `--all-projects`{.cod |
|                       |                       | e}                    |
|                       |                       | automatically detects |
|                       |                       | and scans Yarn        |
|                       |                       | workspaces projects.  |
|                       |                       |                       |
|                       |                       | Note:                 |
|                       |                       | `snyk test`{.code}    |
|                       |                       | and                   |
|                       |                       | `snyk monitor`{.code} |
|                       |                       | commands only.        |
+-----------------------+-----------------------+-----------------------+
| `--all-projects`{.cod | [ **n/a** ]{.bold     | Provide this flag to  |
| e}                    | .bold}                | detect and scan all   |
|                       |                       | Node and other        |
|                       |                       | projects.             |
|                       |                       |                       |
|                       |                       | Note:                 |
|                       |                       | `snyk test`{.code}    |
|                       |                       | and                   |
|                       |                       | `snyk monitor`{.code} |
|                       |                       | commands only.        |
+-----------------------+-----------------------+-----------------------+
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-0a5c8df0-a97a-cb60-4d06-7ed4588bd0b7_UUID-2e09910b-a75f-537b-3d63-7da069a4cde0}Git services for JavaScript projects {#git-services-for-javascript-projects .title}
:::

</div>
:::

JavaScript projects can be imported from any of the Git services we
support. After import, Snyk analyzes your projects based on their
supported manifest files.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm46180810307056}npm {#npm-1 .title}
:::

</div>
:::

npm versions 6.x, 7.x are supported in Git services.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::

Note

Workspaces npm 7.x is not supported.

We build the dependency tree based on these files:

::: {.itemizedlist}
-   `package.json`{.code}

-   `package-lock.json`{.code}
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm46180810271696}Yarn {#yarn-1 .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

Yarn version 1 is supported in Git services.

We build the dependency tree based on these files:

::: {.itemizedlist}
-   `package.json`{.code}

-   `yarn.lock`{.code}
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm46180810227664}Yarn Workspaces {#yarn-workspaces-1 .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

Git support for Yarn Workspaces is enabled for all projects in
organizations created after March 3rd 2021. To enable this feature for
organizations created before this date [contact our Support
team](https://support.snyk.io/hc/en-us/requests/new){.link}. Yarn
version 1 is supported in Git services.

For Yarn Workspaces we scan each `package.json`{.code} that matches the
`packages`{.code} pattern from the root level `package.json`{.code} and
root level `yarn.lock`{.code}

Fix Pull/Merge Requests are not supported for Yarn Workspaces. The fix
advice can be used to manually generate PRs.

Commit status checks always use the root level `yarn.lock`{.code} and
workspace `package.json`{.code} for tests.

::: {.warning style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Warning\]](../css/image/warning.png)
:::

Warning

If your `package.json`{.code} and root `yarn.lock`{.code} are
out-of-sync, we will have issues re-testing the projects. Snyk shows
errors on project page and import logs when this happens.If you
reference the locally installed packages which do not appear in a
lockfile, you can disable the [**Require package.json and yarn.lock
files to be in sync**]{.bold .bold} setting, on the [**Languages
Settings**]{.bold .bold} page for JavaScript.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
###### []{#idm46180810224624}Git settings for JavaScript {#git-settings-for-javascript .title}
:::

</div>
:::

[**Preferences**]{.bold .bold}

From the Snyk UI, use these parameters to customize your language
preferences for JavaScript-based projects:

::: {.informaltable .table-responsive}
+-----------------------------------+-----------------------------------+
| Option                            | Description                       |
+===================================+===================================+
| [**Scan and fix                   | If selected, Snyk reads the       |
| devDependencies**]{.bold .bold}   | `devDependencies`{.code} property |
|                                   | on the package.json and reports & |
|                                   | fixes any vulnerabilities         |
|                                   | accordingly.                      |
+-----------------------------------+-----------------------------------+
| [**Require package.json and       | When selected if the package.json |
| package-lock.json to be in        | and package.lock files are        |
| sync**]{.bold .bold}              | out-of-sync, Snyk fails the       |
|                                   | import.                           |
+-----------------------------------+-----------------------------------+
| [**Exclude package-lock.json from | If you are using private mirrors  |
| being generated when fixing       | or registries, a Snyk generated   |
| vulnerabilities**]{.bold .bold}   | lockfile might not be appropriate |
|                                   | for you because Snyk uses the npm |
|                                   | registry to update the lockfile.  |
|                                   | This setting allows you to        |
|                                   | opt-out of getting lockfiles      |
|                                   | generated for you in our fix pull |
|                                   | requests / merge requests.        |
+-----------------------------------+-----------------------------------+
:::

::: {.orderedlist}
**Update language preferences**

1.  Log in to your account and navigate to the relevant group and
    organization that you want to manage

2.  Click on settings
    [![cog\_icon.png](image/uuid-3408a45a-8e5a-70aa-7e67-796708f1364e.png)]{.inlinemediaobject} \>
    [**Languages**]{.bold .bold}

3.  Click [**Edit settings**]{.bold .bold} for JavaScript to configure
    preferences for your JavaScript (npm and Yarn) projects in this
    organization
:::
:::
