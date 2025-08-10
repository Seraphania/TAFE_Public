

| Command | Purpose | Usage Example |
|---------|---------|---------------|
| `git init` | Initializes a new Git repository. This creates a new `.git` directory in your project, which Git uses to track and manage the project's history. | `git init` |
| `git add` | Adds changes in the working directory to the staging area. It tells Git you want to include updates to a specific file(s) in the next commit. However, `git add` doesn't affect the repository until you commit the changes. | `git add <file>`<br>`git add .` (to add all changes) |
| `git commit` | Saves the staged changes to the repository. Each commit has an associated message which is a description explaining why a particular change was made. | `git commit -m "Your message here"` |
| `git status` | Shows the status of changes as untracked, modified, or staged. This command is helpful for seeing what changes have been added to the staging area and which files are not being tracked by Git. | `git status` |


For students learning Git, understanding how to configure global settings is crucial. These settings simplify the initial setup and ensure that commits and repositories are correctly attributed and organized. Here are summaries of two useful global configurations: setting the user name and email, and setting the default branch name.

### Setting User Name and Email



- **Command to set user name:**
  ```bash
  git config --global user.name "Your Name"
  ```
  Replace `"Your Name"` with your actual name. This name will be associated with all your commits.

- **Command to set user email:**
  ```bash
  git config --global user.email "your_email@example.com"
  ```
  Replace `"your_email@example.com"` with your actual email address. This email is crucial for services like GitHub or GitLab to link commits to your account.

### Setting Default Branch Name

Git historically used `master` as the default branch name for new repositories. However, the community is shifting towards using `main` as the default branch name for new projects. To align with this change and avoid having to manually set the branch name for each new repository, you can change the global default branch name in Git to `main`.

- **Command to set default branch name to `main`:**
  ```bash
  git config --global init.defaultBranch main
  ```
  This command changes the default branch name for all new repositories you create to `main`.

By configuring these settings globally, you streamline your workflow and ensure consistency across all your Git projects. These configurations help maintain a standard naming convention and ensure your identity is correctly attached to your contributions.

