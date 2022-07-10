::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/getting-started-with-snyk-open-source.html"}
::: {.titlepage}
<div>

::: {.title}
### []{#UUID-76c3b43c-5a70-f804-8b59-3e85f89fd90e}Getting started with Snyk Open Source {#getting-started-with-snyk-open-source .title}
:::

</div>
:::

Get started with Snyk Open Source to inspect, find and fix
vulnerabilities in your application\'s Open Source libraries.

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

This process describes getting started using the Snyk Web UI and a SCM
(source code management) system.

::: {.itemizedlist}
-   You can also use an [IDE
    tool](https://docs.snyk.io/integrations/ide-tools){.link} or a
    [CI/CD
    integration](https://docs.snyk.io/integrations/ci-cd-integrations){.link}.
    See [Integrations](https://docs.snyk.io/integrations){.link}.

-   You can get started with the
    [snyk-cli](https://github.com/snyk/user-docs/blob/main/docs/snyk-cli){.link};
    see
    [getting-started-with-the-cli](https://github.com/snyk/user-docs/blob/main/docs/snyk-cli/getting-started-with-the-cli){.link}.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
#### []{#idm46180811010128}Prerequisites {#prerequisites .title}
:::

</div>
:::

Ensure you have:

::: {.itemizedlist}
-   A code project using open source packages, on a supported SCM system
    such as GitHub. See
    [git-repository-scm-integrations](https://github.com/snyk/user-docs/blob/main/docs/features/integrations/git-repository-scm-integrations){.link}.

-   A supported language and package manager, such as Java. See
    [language-and-package-manager-support](https://github.com/snyk/user-docs/blob/main/docs/products/snyk-open-source/language-and-package-manager-support){.link}.

-   A Snyk account (go to [https://snyk.io/](https://snyk.io){.link} and
    sign up - see
    [getting-started.md](https://github.com/snyk/user-docs/blob/main/docs/getting-started.md){.link}).
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
#### []{#idm46180811014752}Stage 1: Add source control integration {#stage-1-add-source-control-integration .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

If you already have an integration set up, go to Step 3.

Choose a source code integration, to allow Snyk to work on a project.

::: {.orderedlist}
1.  Log in to the Snyk Web UI
    ([app.snyk.io](https://app.snyk.io){.link}).

2.  Select Integrations \> Source control.

3.  Click the source control system (for example, GitHub) to integrate
    with Snyk.

4.  Fill in the account credentials as prompted (or authenticate with
    your account in GitHub), to grant Snyk access permissions for
    integration.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
#### []{#idm46180811042208}Stage 2: Add Projects {#stage-2-add-projects .title}
:::

</div>
:::

Add projects to test with Snyk, by choosing repositories for Snyk to
test and monitor.

In the Snyk Web UI, first select Projects from the Snyk Web UI, then
click Add Project, selecting where to add the project repos from (for
example GitHub).
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
#### []{#idm46180810996368}Add a repo {#add-a-repo .title}
:::

</div>
:::

Select the repositories to use, then click Add selected repositories to
import the selected repositories into your projects:

::: {.mediaobject}
  ----------------------------------------------------------------------------------
  ![open-source-add-repo.png](image/uuid-a375df8c-c085-3c25-19c0-779404564871.png)
  ----------------------------------------------------------------------------------
:::

This also:

::: {.itemizedlist}
-   Sets Snyk to run a regular check ([daily by
    default](https://github.com/snyk/user-docs/blob/main/docs/features/user-and-group-management/managing-settings/usage-page-details.md#projects){.link})
    for vulnerabilities.

-   Creates a
    [Webhook](https://github.com/snyk/user-docs/blob/main/docs/features/integrations/snyk-webhooks){.link},
    so when you change code, Snyk tests your pull / merge requests, to
    check that new dependencies do not introduce more vulnerabilities.
:::

In Settings, optionally choose to: \*\*\*\*

::: {.itemizedlist}
-   Use Add custom file location to add any additional dependencies from
    custom paths.

-   Use Exclude folders to list up to 10 folders to exclude from
    scanning during the import; for example, to shorten scanning time.
:::

::: {.orderedlist}
**Import progress**

1.  A progress bar appears: click View last import log to see log
    results.

2.  Project import completes, with a status error message:
:::

::: {.mediaobject}
  ----------------------------------------------------------------------------------------
  ![open-source-status-message.png](image/uuid-3bcfadda-514e-ec61-014c-87dced9ccd6b.png)
  ----------------------------------------------------------------------------------------
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

If you see any errors during import, see [Project import
errors](https://support.snyk.io/hc/en-us/articles/360001373118){.link}.

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
#### []{#idm46180810993760}Stage 3: View vulnerabilities {#stage-3-view-vulnerabilities .title}
:::

</div>
:::

You can now view vulnerability results for imported projects. The
Projects tab appears by default after import, showing vulnerability
information for project you\'ve imported.

You can expand an imported project to see vulnerability information for
that project, including the number of issues found, grouped by severity
level:

::: {.mediaobject}
  -----------------------------------------------------------------------------
  ![projects-import.png](image/uuid-5065efcc-b8ba-14b6-3409-f8afd7c806db.png)
  -----------------------------------------------------------------------------
:::

Click on an entry to open the issues view for that entry, including the
module, where it was introduced, and how to fix it, plus more details
about the vulnerability itself:

::: {.mediaobject}
  -----------------------------------------------------------------------------
  ![project-details.png](image/uuid-d19aae49-27bc-ee2d-d3e5-77283988c49f.png)
  -----------------------------------------------------------------------------
:::

See
[view-project-information](https://github.com/snyk/user-docs/blob/main/docs/introducing-snyk/introduction-to-snyk-projects/view-project-information){.link}
for more details.
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
#### []{#idm46180811050016}Stage 4: Fix vulnerabilities {#stage-4-fix-vulnerabilities .title}
:::

</div>
:::

For some languages, Snyk can fix your vulnerabilities using fix
pull/merge requests.

::: {.note .notice style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

See
[what-languages-do-we-support-fix-pull-requests-or-merge-requests.md](https://github.com/snyk/user-docs/blob/main/docs/features/fixing-and-prioritizing-issues/starting-to-fix-vulnerabilities/what-languages-do-we-support-fix-pull-requests-or-merge-requests.md){.link}

Navigate to the Issues view for a project:

::: {.mediaobject}
  -------------------------------------------------------------------------
  ![Issues-view.png](image/uuid-75a3c01e-e70b-5e6a-bcf0-f05740a9ea59.png)
  -------------------------------------------------------------------------
:::

To fix vulnerabilities:

::: {.orderedlist}
1.  Click Fix this vulnerability to raise a fix PR for that issue (or
    click Fix these vulnerabilities to to fix multiple issues).

2.  The Open a Fix PR screen opens and indicates the vulnerabilities you
    selected.

3.  Check any additional issues you want to fix, or uncheck items to
    remove them from the fix.

4.  Scroll down to the bottom of the screen and click Open a Fix PR.

5.  Snyk now actions this PR, then a results screen appears.

6.  Optionally, select the Files changed tab to see details of the
    changes made.
:::

::: {.mediaobject}
  ---------------------------------------------------------------------------
  ![files-changed.png](image/uuid-240611de-61d8-cb02-51e7-9a61f4d453ec.png)
  ---------------------------------------------------------------------------
:::

See
[remediate-your-vulnerabilities.md](https://github.com/snyk/user-docs/blob/main/docs/features/fixing-and-prioritizing-issues/issue-management/remediate-your-vulnerabilities.md){.link}
for more details.
