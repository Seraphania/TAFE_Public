# Contents
- [Contents](#contents)
- [Week 5/Session 6 - GitHub and Remotes(Part 2)](#week-5session-6---github-and-remotespart-2)
    - [Forking](#forking)
    - [Pull requests](#pull-requests)
    - [Git ignore](#git-ignore)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 5/Session 6 - GitHub and Remotes(Part 2)

### Forking
forking and cloning are basically the same, but forking is a github feature
a fork is a clone that is yours, but can't be merged back to the original.
GitHub maintains a link?

to create a fork, you don't need write permissions

fork vs branch
forking makes it so that someone can do what they want, but the changes may not be accepted by the repo owner.

if you fork you can make changes, and the repo owner can decide to merge them into the main branch or not.

Caveat:  
Can be hard to control in an enterprise situation.

Go ahead and fork!

### Pull requests
Pull requests are a github feature   
main git features are "clone, push pull" but pull is actually fetch and merge.

If a repo is public then (except for commercial) it's free to be forked.  
Attribution is expected (otherwise it's frowned on like plagiarism)  

If you think your changes are good enough for the main repo, you can try to merge into main, but it will be up to the repo owner whether the changes are accepted.  

Wikipedia edits are not controlled, but git prevents changes without permissions being set.  
Not just anyone can edit a repo because otherwise it introduces bugs and mistakes. This is also to keep the history clean. don't want it to be a free for all.

Repo owners generally want to review changes before merging.

Part of this is psychological: If people lose ownership (or feel they do), they may not care about quality, review allows a sense of ownership.

github allows pull requests which take the place of pushing.  
so if Raf wants to make changes to my stuff, he requests I pull from his repo (pull request).
Push/pull is relative.  

pull requests can happen between any two forks or branches with a shared history.  

Common in enterprise, it is one of a few strategies for code review.  
however a chat might be more appropriate depending on the situation.  

GitLab uses the term merge request, but it's the same thing (possibly a better description)

make changes, push to own repo... then look in github shows ahead of origin
then create pull request.

### Git ignore
add a git ignore (choose languages)
(python for python)
list of string patterns that ignores certain things (for example the metadata from vscode/vis studio or private info)

whne you run a python program it creates a "pythonc" which is a cache file, because we don't compile. you only want source, not source control.

`echo top-secret.shh >> .gitignore` will ignore certain thing including pattern matching/folders/files
play with it.  
useful for keeping out extra stuff, particularly if you `git add .` a lot.

## Resources
[Lecture Slides](./resources/civ-ipriot-vcs-remotes-p2-github-workflow.pptx)  
[Intro to Pull Requests](./resources/README.md)  
[Video: Getting started with branching workflows, Git Flow and GitHub Flow](https://www.youtube.com/watch?v=gW6dFpTMk8s)  
[Video: create Pull Request from fork](https://www.youtube.com/watch?v=rgbCcBNZcdQ)  
[Video: Writing and Approving Pull Requests in GitHub](https://www.youtube.com/watch?v=1XrP6POUPD0)  
[Video: How to Push Code to Github](https://www.youtube.com/watch?v=wrb7Gge9yoE)  
[Pushing a project to GitHub](https://circleci.com/blog/pushing-a-project-to-github/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--japac-en-dsa-maxConv-auth-brand&utm_term=g_-_c__dsa_&utm_content=)  
[How to delete a repository in GitHub](https://zapier.com/blog/github-delete-repository/)  
[Git Delete Branch](https://www.cloudbees.com/blog/git-delete-branch-how-to-for-both-local-and-remote)  
[Pull Requests](./resources/Pull-Requests.pdf)

## Activities
[Git Excercise - Password Generator](./activities/AppProgPython-Git-Exercises.pptx)  

