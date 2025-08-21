# What I learned about branching and merging

> Use the attached worksheet to practice the concepts of branching and merging. 

Actions you need to perform are marked with `- [ ]` replace the space with an `x` when you complete the action.

- [x] Before you start, create a new git repo and add the worksheet to it:

```bash
cd source/repos
mkdir branching-merging
cd branching-merging
git init
cp ~/Downloads/branching-merging-worksheet.md .
git add .
git commit -m "Add branching-merging-worksheet.md"
```


## Branching

### Definition

- [x] In your own words define what is branching

> Branching is creating a copy of a main repository called a branch,, that can be edited seperately, and completely independantly. It may or may not be merged later.

- [x] Commit your changes:

```bash
git add .
git commit -m "Define what is branching"
```


### Why branch

- [x] List at least three reasons why you would use branches in a project

> Your list goes here
> 1. Branching allows a place to work without affecting main, so parts of a project ca be worked on independantly.
> 2. Because a branch is isolated, new features can be experimented with, potentially taking the project in new directions. This doesn't require the original programmer's accceptance of the changes into their project.
> 3. Branches allow a safe place to tinker, the changes can be completely discarded if they aren't good, or addeed to the main branch if desired.

- [x] Commit your changes - remember to use a descriptive message

### How to create a branch

To create a branch we run the following commands: 

```bash
git branch <branch-name>
git switch <branch-name>
```


- [x] Briefly describe what each command does:

> `git branch <branch-name>` creates a new branch called \<branch-name>
> `git switch <branch-name>` moves into the branch called \<branch-name>

- [x] Create a new branch called `feature-1` and switch to it
- [x] Did your working copy change? Why or why not?

> No, my working copy has not changed, I have not committed any changes to the new branch yet.

- [x] Commit your changes
- [x] Switch back to main
- [x] Did you notice any changes in the working copy after the commit? Why or why not?
> My changes to the last question disappeared, they were mde in the branch feature-1, not in main. But I'll write this here anyway!
 
**Oh no!** 
If you did everything correctly, your answer to the previous question is gone! Haha.

Don't worry, we can get it back. But first:

- [x] Commit your changes to the main branch


### Merging changes

- [x] What is merging?
> Merging is the combining of changes to two seperate branches (hopefully main and feature-1 in my case!)

- [x] What is a merge conflict?
> A merge conflict is when changes between 2 branches clash with eachother

When there is a merge conflict, you need to resolve it before you can merge the changes. Git will mark the conflicted files, and you need to manually resolve the conflicts – that is, edit the files to remove the conflict markers and make the changes you want to keep. Here's an example of a file with a merge conflict:

```text
<<<<<<< HEAD
Text from the version in the HEAD (main) branch
=======
Text from the version in the feature-1 branch
>>>>>>> feature-1
```


- [x] How do you resolve a merge conflict?
> Edit the files to remove the conflict markers; make the changes you want to keep.

- [x] Attempt to merge the `feature-1` branch into `main`:

```bash
git merge feature-1
```

- [x] Did it work? Why or why not?

> Yes, though I forgot to add a commit message, so it asked for that.

Before you can merge, you need to commit any changes in your working copy (or stash, but we'll talk about that later)

- [x] Commit your changes
- [x] Attempt to merge the `feature-1` branch into `main` again
- [x] Did it work? Why or why not? If a merge succeeded, what was the merge strategy used? If there was a merge conflict, resolve it.
  
> It said "Already up to date."

- [x] Commit your changes and/or resolve the merge conflict

### Deleting branches

- [x] Delete the `feature-1` branch:
```bash
git branch -d feature-1
```

### Looking back

We can look into the past and see the evolution of our project using the git log command. There are several useful options to the git log command, such as --oneline, --graph, --decorate, --all, --since, --until, --author, --grep, --no-merges, --reverse, and many others.

We'll use a couple of popular options to see the history of our project.

- [x] Run the following commands:

```bash 
git log
git log --oneline
git log --oneline --graph --decorate --all
```
- [x] Briefly describe the output of each command

> `git log` shows the commit history for the current branch, incluing who did it, when (date and time), the commit ID (SHA-1) and the commit message.  
> `git log --oneline` shows a shorter version, only the start of the hash, and the commit messaage, no committer or time info:
 ```
    $ git log --oneline
    a031dc2 (HEAD -> main) Merge branch 'feature-1'
    0fab37b Final main commit before attempting to merge feature-1
    d0420dd Changes to main ater chanegs to feature-1 branch
    e5b6b60 Change branch to feature-1
    98dffb8 Describe why branching is good
    873263b Define what is branching
    409b407 Add branching-merging-worksheet.md
```
> `git log --oneline --graph --decorate --all` same as `git log --oneline` but with a pretty graph!:
```
$ git log --oneline --graph --decorate --all
*   a031dc2 (HEAD -> main) Merge branch 'feature-1'
|\
| * e5b6b60 Change branch to feature-1
* | 0fab37b Final main commit before attempting to merge feature-1
* | d0420dd Changes to main ater chanegs to feature-1 branch
|/
* 98dffb8 Describe why branching is good
* 873263b Define what is branching
* 409b407 Add branching-merging-worksheet.md
```

- [x] Commit your changes
- [x] Reflect on what you learned about branching and merging. What was the most challenging part? What was the most interesting part?

> I jumped ahead, I added and committed the changes to main, before attempting to merge feature-1, so I encountered no issues (I tried to go back to before that commit, but I don't think it worked.)
>
> I enjoyed the git log, especially with the graph, it's a nice visual representation.
>
> I think knowing IRL, when to branch and when to merge will be a challenge (and I didin't get a chance to see conflicts, so those will be fun.)

**Done!**
Or are you? There are always new changes to commit ;) 

```
$ git log --oneline --graph --decorate --all
* 9d1d519 (HEAD -> main) Final Commit Assignment complete
*   a031dc2 Merge branch 'feature-1'
|\
| * e5b6b60 Change branch to feature-1
* | 0fab37b Final main commit before attempting to merge feature-1
* | d0420dd Changes to main ater chanegs to feature-1 branch
|/
* 98dffb8 Describe why branching is good
* 873263b Define what is branching
* 409b407 Add branching-merging-worksheet.md
```