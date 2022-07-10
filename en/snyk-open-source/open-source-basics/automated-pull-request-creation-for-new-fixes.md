::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-basics/automated-pull-request-creation-for-new-fixes.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-ce533b5f-ceb8-748a-a93b-b769615cc47c}Automated pull request creation for new fixes {#automated-pull-request-creation-for-new-fixes .title}
:::

</div>
:::

The following rules are applied to automatic PR creation for
vulnerabilities:

::: {.itemizedlist}
-   Pull requests are created based on the [**Test & Automated Pull
    Request Frequency**]{.bold .bold} (see screenshot below) setting

-   If a scan is manually run (you clicked [**Retest now**]{.bold .bold}
    for the project), the 24-hour window is marked as having been run
    and no automatic PR is created until the next automated scan runs

-   One pull request is created per project (priority score of 700 and
    above only)

-   If [**either**]{.bold .bold} the vulnerability itself is new and has
    a fix available [**or**]{.bold .bold} if the fix is new and is not
    ignored

-   For known vulnerabilities see
    [fix-pull-requests-for-known-vulnerabilities-backlog.md](../../){.link}
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

Pull requests for new vulnerabilities are enabled by default for new
integrations.

See [Git repository SCM
integrations](https://support.snyk.io/hc/en-us/sections/360001138098-Git-repository-SCM-integrations){.link}
for full details of supported integrations.

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-ce533b5f-ceb8-748a-a93b-b769615cc47c_UUID-1d4d70a3-e92d-d2dc-fbaf-a26124977255}Enable or disable pull requests for an integration {#enable-or-disable-pull-requests-for-an-integration .title}
:::

</div>
:::

Enable at the global integration level:

::: {.procedure}
1.  Navigate to settings

    ::: {.mediaobject}
    ![](image/image-missing.png)
    :::

    \> [**Integrations**]{.bold .bold}.

2.  Select an SCM integration (for example, GitHub).

3.  Enable [**New vulnerabilities**]{.bold .bold}
:::

[**Apply changes to all overridden projects**]{.bold .bold} will update
all of the individual project settings for "Automatic fix pull
requests". If a project previously had its own settings for this,
clicking on this button will override it with the global setting.

::: {.mediaobject}
![](image/image-missing.png)
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-ce533b5f-ceb8-748a-a93b-b769615cc47c_UUID-d5bba19f-0418-e927-9d23-37b68a89df01}Enable or disable pull requests for a single project {#enable-or-disable-pull-requests-for-a-single-project .title}
:::

</div>
:::

Enabling/disabling at a project level will override this single project
rather than inheriting it from the global integration setting.

::: {.procedure}
1.  Under [**Projects**]{.bold .bold} select a project and select
    [**Settings**]{.bold .bold} (top right-hand corner)

2.  Select [**GitHub integration**]{.bold .bold}

3.  Under the [**Automatic fix pull requests**]{.bold .bold} section:

    ::: {.itemizedlist}
    -   Select [**Customize for only this project**]{.bold .bold}

    -   Enable [**New vulnerabilities**]{.bold .bold}

    -   Select [**Save changes**]{.bold .bold}
    :::
:::

::: {.mediaobject}
![](image/image-missing.png)
:::
:::
:::
