::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-basics/fixing-vulnerabilities.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-f12dc114-4ebb-d291-71ad-48fb1e264d1a}Fixing vulnerabilities {#fixing-vulnerabilities .title}
:::

</div>
:::

Snyk provides actionable fix advice for vulnerabilities: see
[remediate-your-vulnerabilities.md](https://github.com/snyk/user-docs/blob/main/docs/features/fixing-and-prioritizing-issues/issue-management/remediate-your-vulnerabilities.md){.link}
for more details.

Snyk supports workflows to fix vulnerabilities using:

::: {.itemizedlist}
-   [Automatic pull / merge requests (PRs /
    MRs)](https://github.com/snyk/user-docs/blob/main/docs/products/snyk-open-source/open-source-basics/fixing-vulnerabilities.md#automatic-pull-merge-requests){.link}.

-   [Manual pull / merge
    requests](https://github.com/snyk/user-docs/blob/main/docs/products/snyk-open-source/open-source-basics/fixing-vulnerabilities.md#manual-pull-merge-requests-for-a-project-code){.link}.
:::

{% content-ref
url=\"../../../features/fixing-and-prioritizing-issues/starting-to-fix-vulnerabilities/what-languages-do-we-support-fix-pull-requests-or-merge-requests.md\"
%}
[what-languages-do-we-support-fix-pull-requests-or-merge-requests.md](https://github.com/snyk/user-docs/blob/main/docs/features/fixing-and-prioritizing-issues/starting-to-fix-vulnerabilities/what-languages-do-we-support-fix-pull-requests-or-merge-requests.md){.link}
{% endcontent-ref %}

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm46180810921584}Automatic pull / merge requests {#automatic-pull-merge-requests .title}
:::

</div>
:::

For projects imported via an SCM (Source Code Manager), Snyk offers the
following types of automated pull / merge requests:

::: {.itemizedlist}
-   [Fix pull requests for new
    vulnerabilities](https://docs.snyk.io/snyk-open-source/open-source-basics/fix-pull-requests-for-new-vulnerabilities){.link}

-   [Fix pull requests to clear the backlog of vulnerabilities in
    priority
    order](https://github.com/snyk/user-docs/blob/main/docs/products/snyk-open-source/open-source-basics/fix-pull-requests-for-known-vulnerabilities-backlog.md){.link}

-   [Dependency upgrade pull
    requests](https://docs.snyk.io/snyk-open-source/dependency-management/upgrading-dependencies-with-automatic-prs){.link}
:::
:::

::: {.section dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#idm46180810923680}Manual pull / merge requests for a project code {#manual-pull-merge-requests-for-a-project-code .title}
:::

</div>
:::

To generate a PR / MR directly from your project, using the Snyk UI:

::: {.orderedlist}
1.  Navigate to your project from the project list

2.  Select the file

3.  Select [**Open a Fix PR/MR**]{.bold .bold} or [**Fix this
    vulnerability**]{.bold .bold}

4.  A preview screen appears, showing you what fixes will be applied

5.  Click [**Open a Fix PR**]{.bold .bold} on this screen to generate
    the pull request
:::
:::
:::
