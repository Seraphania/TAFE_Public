# Contents
- [Contents](#contents)
- [Week 3/Session 4 - Git Branching and Merging](#week-3session-4---git-branching-and-merging)
  - [Branching and Merging](#branching-and-merging)
    - [What are branches](#what-are-branches)
    - [Why Branch](#why-branch)
    - [Branch Lifecycle Fundamentals](#branch-lifecycle-fundamentals)
    - [Branching and Merging Operations](#branching-and-merging-operations)
    - [Resources](#resources)
    - [Activivties](#activivties)

# Week 3/Session 4 - Git Branching and Merging

## Branching and Merging
### What are branches
Example would be adding a suffix to explore a new feature.
different from versions, useful when we don't know which version will be the final one.
Versions are linear, building on an idea, whereas branches are useful when exploring different solutions.

How to tell if branch or version (sort of up to you), but versions are iterations on one idea, whereas if your're working on two versions concurretly, they are probably different branches.

### Why Branch
Experiments
isolate work by different teams
Consolidate, commit graph around a key feature sometimes we want group related changes together - putting them in a branch can help.
For fun - you can play around with ideas.
easy to keep or get rid of a particular branch if not needed.

Branching used to be expensive and error prone (because merging was hard), Git makes this cheap, little cost in disk space, and processing time, easy to remove or merge branches.

### Branch Lifecycle Fundamentals
Might not be known in advance, but if a branch is unsuccessful it can be killed, or it can become main if it *is* successful.

Best practice is to delete useless branches (keeps things tidy).

### Branching and Merging Operations
Two ways to merge:
* Can weave parts of two branches together.
* Or we can *fast forward* - pretend there was never a branch in the first place. Basically rename the experiemts into main. Only possible if no changes were made to the branch.


Commits are always snapshots of the entire project, referring to the parent. it is not reliant on other snapshots.

Current commit matches againts it's parent. These proliferate, and it matches against head... what we're curently working on (the branch, main to begin with)


`$ git config --global init.defaultBranch main`
applies to all repos for the current user, applies to all future repos.

`git branch -M main` renames the current branch (to main)

`git config list` see current username

Handy Link:  
https://learngitbranching.js.org/

Example workflow:
```gitbash
 1  pwd
 2  ls
 3  mkdir -p source/repos
 4  cd /source/repos
 5  mkdir week4-ip4riot
 6  cd week4-ip4riot/
 7  git init
 8  ls -la
 9  git branch -M main
10  touch welcome.md
11  vi welcome.md
12  git config list
13  git log
14  git add welcome.md && git commit -m "first commit"
15  echo "New Line" >> welcome.md
16  git add welcome.md && git commit -m "second commit"
17  git log --oneline
18  echo "Another Line" >> welcome.md
19  git add welcome.md && git commit -m "another commit"
20  git branch experimental
21  git switch experimental
22  cat welcome.md + experiemntal
23  echo "experiemntal branch edit" >> welcome.md
24  git add && git commit -m "commit to experiemntal branch"
25  git log --oneline
26  git switch main
27  cat welcome.md
28  git merge experimental
29  git log --oneline
30  git reflog
```

### Resources
[Lecture Slides](./resources/civ-ipriot-vcs-branch.pptx)  
[Chapter 2 and 3 of Head First Git](../../Head_First_Git_-_Raju_Gandhi.pdf)  
[Learn Git Branching interactive Visualisation tool](https://learngitbranching.js.org/)  
[Git Diff - Atlassian Git Tutorial](https://git-scm.com/docs/git-diff)  
[Adrian's Notes from Friday Online](./resources/Online-QaA-Session-3.pdf)  

### Activivties
[Branching and Merging Activity](./activities/branching-merging-worksheet.md)  
[Branching and Merging Complete](./activities/branching-merging-worksheet-complete.md)  