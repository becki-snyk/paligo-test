::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-basics/automated-pull-requests-for-known-vulnerabilities--backlog-.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-70dd9a4f-38dd-2850-a8ab-50bbf02d0eb2}Automated pull requests for known vulnerabilities (backlog) {#automated-pull-requests-for-known-vulnerabilities-backlog .title}
:::

</div>
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::

Note

This feature is supported in GitHub and GitHub Enterprise integrations
only. The Autofix PR settings may vary depending on the integration.

[**Known vulnerabilities**]{.bold .bold} retrieve vulnerabilities from
the project's backlog. These are the previously declared
vulnerabilities.

The following rules are applied to automatic PR creation for
vulnerabilities:

::: {.itemizedlist}
-   Pull requests are created based on the [**Test & Automated Pull
    Request Frequency**]{.bold .bold} (see screenshot below) setting

-   If a scan is manually run (you clicked [**Retest now**]{.bold .bold}
    for the project), the 24-hour window is marked as having been run
    and no automatic PR is created until the next automated scan runs

-   One pull request is created per project (priority score of [**700
    and above only**]{.bold .bold})
:::

::: {.mediaobject}
![]()
:::

To know when your last 24-hour window was kicked off, check the project
page for [**Snapshot taken by recurring test**]{.bold .bold}--also check
your email for [**\[snyk\] Vulnerability alert**]{.bold .bold} for
specific scan results:

::: {.mediaobject}
![]()
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-70dd9a4f-38dd-2850-a8ab-50bbf02d0eb2_UUID-053550db-c05a-8d22-1344-441a528f4609}Enable or disable pull requests for a single project {#enable-or-disable-pull-requests-for-a-single-project .title}
:::

</div>
:::

Enabling/disabling at a project level will override this single project
rather than inheriting it from the global integration setting.

::: {.procedure}
1.  Navigate to the project and select [**Settings**]{.bold .bold}

2.  Select [**GitHub integration**]{.bold .bold}

3.  Under the [**Automatic fix pull requests**]{.bold .bold} section:

    ::: {.itemizedlist}
    -   Select to [**Customize for only this project**]{.bold .bold}

    -   Enable [**Known vulnerabilities (backlog)**]{.bold .bold}
    :::
:::

::: {.mediaobject}
![](image/image-missing.png)
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-70dd9a4f-38dd-2850-a8ab-50bbf02d0eb2_UUID-f8e31898-5ec3-be07-ea61-ebc3dd03f562}Enable or disable pull requests for integrations {#enable-or-disable-pull-requests-for-integrations .title}
:::

</div>
:::

To enable at the global integration level:

::: {.procedure}
1.  Click on settings

    ::: {.mediaobject}
    ![](image/image-missing.png)
    :::

    \> [**Integrations**]{.bold .bold}

2.  Select an SCM integration (for example, GitHub)

3.  Enable [**Known vulnerabilities (backlog)**]{.bold .bold}
:::

[**Apply changes to all overridden projects**]{.bold .bold} will update
all of the individual project settings for "Automatic fix pull
requests". If a project previously had its own settings for this,
clicking on this button will override it with the global setting.

::: {.mediaobject}
![](image/image-missing.png)
:::
:::
