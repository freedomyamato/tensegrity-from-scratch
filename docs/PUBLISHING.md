# Publish the repository on GitHub

Source repository: [freedomyamato/tensegrity-from-scratch](https://github.com/freedomyamato/tensegrity-from-scratch). The instructions below describe publishing a source-package copy to a new empty repository. For an existing clone, commit your changes and use a normal fast-forward push.

## Create the destination

In your GitHub account, create a new empty repository with the name above. Choose the audience deliberately; keep personal learner records private. For command-line upload, leave automatic README/license creation disabled because this package already includes those files.

## Upload with Git

Extract the package, open a terminal in the extracted root and run these commands. If your folder is already a Git repository, skip `git init`. Replace the URL with your actual destination if its owner/name differs. Authenticate using your normal local Git/GitHub setup; do not put tokens into these files.

```bash
git init -b main
git add .
git commit -m "Add complete tensegrity teaching course"
git remote add origin https://github.com/freedomyamato/tensegrity-from-scratch.git
git push -u origin main
```

If `origin` already exists, inspect `git remote -v` before changing it. Do not force-push. If Git requests author identity, configure your own chosen name/email locally rather than copying an invented identity.

## After upload

Check that README.md, COURSE.md and the phase folders appear. The included GitHub Actions workflow runs numerical tests and repository checks on pushes and pull requests. A passing CI run validates these software/content checks; it is not a physical engineering approval.

For readers on phones, GitHub’s Markdown lesson pages work without downloading the offline HTML reader. To use the offline reader, download and extract the full folder so diagrams and file links remain available.

If using an assistant with this GitHub connector for another copy, provide its existing repository URL. The connected tools can write an accessible repository but do not expose a create-repository operation.
