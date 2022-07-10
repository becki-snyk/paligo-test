::: {.section lang="en" lang="en" dir="ltr" data-permalink="snyk-open-source/open-source-basics/integrate-snyk-into-your-workflow.html"}
::: {.titlepage}
<div>

::: {.title}
#### []{#UUID-98a97444-1878-e0aa-28bd-5fc5791e3345}Integrate Snyk into your workflow {#integrate-snyk-into-your-workflow .title}
:::

</div>
:::

This example shows how Snyk can integrate into your GitHub-based
workflow.

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-a73e72ba-d6ff-b845-99bb-650c6bb993dc}Step 1: Set up environment {#step-1-set-up-environment .title}
:::

</div>
:::

::: {.procedure}
1.  Open up [Snyk CLI](https://docs.snyk.io/snyk-cli){.link}, and run a
    git clone command on the [**goof**]{.bold .bold} repository.

    ``` {.programlisting}
       git clone https://github.com/snyk/goof.git
    ```

2.  Create a new branch, add vulnerabilities on this branch, then merge
    changes back to GitHub as a Pull Request:

    ``` {.programlisting}
       git branch add_vulns
       git checkout add_vulns
    ```
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-d9c63aee-062e-4d38-dd71-0bee0b83316e}Step 2: Add an open source dependency {#step-2-add-an-open-source-dependency .title}
:::

</div>
:::

Review the [**package.json**]{.bold .bold} manifest file in your cloned
goof application, to see multiple direct dependencies listed:

::: {.mediaobject}
![]()
:::

::: {.note style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Note\]](../css/image/note.png)
:::
:::
:::

Note

These direct dependencies can also have additional transitive
dependencies; libraries that they depend on.

To add the dependency:

::: {.itemizedlist}
-   Add the [**tinymce 4.1.0**]{.bold .bold} library at the bottom of
    the dependencies list:

    ``` {.programlisting .json data-language="json"}
                     { "name": "goof", ... } "dependencies" { ... "typeorm": "^0.2.24", "tinymce": "4.1.0" }, ...
                  
    ```
:::

::: {.tip style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Tip\]](../css/image/tip.png)
:::

Tip

Remember to place a comma after the previous dependency.

::: {.itemizedlist}
-   Create a [lock
    file](https://docs.npmjs.com/files/package-lock.json){.link} for our
    Node application:

    ``` {.programlisting}
                    npm install --package-lock
                  
    ```
:::

::: {.tip style="margin-left: 0.5in; margin-right: 0.5in;"}
![\[Tip\]](../css/image/tip.png)
:::

Tip

If this file already exists, run `rm package-lock.json`{.code} to remove
it.

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-e62200ab-7772-de0f-0dfb-645c288efc81}Step 3: Commit and review changes {#step-3-commit-and-review-changes .title}
:::

</div>
:::

::: {.itemizedlist}
-   Commit your change locally, checking the status of the change in our
    local git repository, then adding the change to our local git, then
    committing it:

    ``` {.programlisting}
    git status git add package* git commit -m "adding tinymce v4.1.0"
    ```
:::

::: {.itemizedlist}
-   Commit your local code change to GitHub, transferring the files and
    history to your upstream git repository on GitHub:

    ``` {.programlisting}
    git push --set-upstream origin add_vulns
    ```

    GitHub has received your changes on your [**add\_vulns**]{.bold
    .bold} branch.
:::

::: {.itemizedlist}
-   In GitHub, click [**Compare & pull request**]{.bold .bold} to
    compare the [**add\_vulns**]{.bold .bold} branch with the
    [**master**]{.bold .bold} branch and generate a pull request:
:::

::: {.mediaobject}
![]()
:::
:::

::: {.section lang="en" lang="en" dir="ltr"}
::: {.titlepage}
<div>

::: {.title}
##### []{#UUID-8c3f86c0-489f-5b0e-b956-ec8df92c70fb}Step 4: Snyk tests pull request checks {#step-4-snyk-tests-pull-request-checks .title}
:::

</div>
:::

Snyk automatically tests your pull request for vulnerability and license
checks in the merge process:

::: {.mediaobject}
![](image/image-missing.png)
:::

As the PR workflow completed, Snyk validated the vulnerability and
license policy set for the project. Based on the policy, the checks
either passed or failed; this is shown in GitHub.

This allows you to establish a security gate and prevent pull requests
from adding new vulnerabilities, or new open source libraries that do
not meet your license policy, to the source code baseline.

For more details on PR checks see the article on our [GitHub
integration](../../){.link}.
:::
