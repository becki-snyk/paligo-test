# paligo-test

**Markdown files are in the `en` directory and its subdirectories.**

Paligo's GitHub integration publishes a ZIP of HTML files to this repo. This triggers a GitHub Action that does the following:

- Unzips the files
- Converts them to Markdown using Pandoc
- Moves the files to the root
- Cleans up unneeded files
