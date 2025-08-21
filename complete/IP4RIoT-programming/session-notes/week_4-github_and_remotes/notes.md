# Contents
- [Contents](#contents)
- [Week 4/Session 5 - GitHub and Remotes](#week-4session-5---github-and-remotes)
  - [Session overview](#session-overview)
    - [Relevance to industry](#relevance-to-industry)
    - [Relevance to assessment](#relevance-to-assessment)
  - [Github and Remotes](#github-and-remotes)
    - [Cloning](#cloning)
    - [Push](#push)
    - [Fetch](#fetch)
    - [Pull](#pull)
    - [Git vs. Github](#git-vs-github)
    - [Notes on Assessments](#notes-on-assessments)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 4/Session 5 - GitHub and Remotes

## Session overview
**Objectives**
* Understand the concept of remote repositories
* Clone a repository
* Understand the relationship between git and GitHub
* Set up a GitHub account

**Curriculum alignment**  
Aligns with the following elements of ICTICT449 Use version control systems in development environments:
* 1.4 Install VCS and create personal account and push changes from branch according to VCS service provider and organisational requirements
* 1.5 Configure tools and user interface of VCS according to organisational requirements
* 2.4 Create and access files in the repository according to service provider procedures

### Relevance to industry
In order to use git for collaborative workflows - its core use case - we must work with remote repositories. In industry, we usually have an enterprise repository that is the "source of truth". Such remote repositories are usually hosted internally (tools such as Bitbucket) or externally (GitLab, GitHub, and Bitbucket).

### Relevance to assessment
Creating a GitHub account and repository is a prerequisite for the first portfolio activity.

**How to use this information**  
* Follow the lecture slides and recording if applicable
* Create a GitHub account using the attached instructions or your own research - you do not have to create an account with your TAFE account.

___
## Github and Remotes
Today is where we learn industry useful knowledge.
The primary purpose of git is collaboration, that's where github comes in.

Tthe opposite of `git init` is `rm -rf`, there is nothing keeping the .git folder safe.
some repos you may wish to keep private, if so you can use github.


### Cloning
Copies the repo in its last committed state and maintains a link to the origin repo as a remote.

creates a new repository with all its history. This can then be worked with locally (commit/branch/merge), but you can also push to and fetch from the remote.

### Push
pushes commits to a remote. by default the remte will b e called origin.

### Fetch
Creates a branch locally, is a a bit like clone, but only with the last commit instead of full history. Does not create the repo however.
It operates in the opposite order to clone: fetches the changes into a local branch (a remote tracking branch) - is different from pull. a remote tracking branch only points at the last commit you fetched, but you can merge from it.

### Pull
is a fetch, creates local tracking branch and merges locally, pull tends to be used more often as typically we want to fetch and merge at the same time.

One person's push is another person's pull.

### Git vs. Github
git on it's own is a utility, it's not a server (most version control systems are backed by hosting to make them collaborative), there are a bunch of different hosting servicees that specialise in git bitbucket and Git Lab being common examples besides GitHub.

Git hub is not the main one used for enterprise, github is the biggest for small/open source type projects.
core functions are all to host git repos remotely.

Bitbucket owned by atlassian (Sydney)

Git Lab Owned by Git Labs

GitHub owned by Microsoft

git and github are things an employer expect you to know, it demonstrates that you have collaborated, and that you have worked on something worth sharing. (fine if you've used bitbucket or similar.)

git has no inherant hosting capability, was initially considered brilliant, but hard to use.
Making it hostable and easy to use was important, GitHub launched 3 years after git (git was launched in 2004) emphasis was put on collaboration and ease of use.

### Notes on Assessments
1. screenshot github profile
screenshot git init username/pw with tafe e-mail/student no(don't hit enter)

2. pay attention to Q.2  
b. be detailed, not every repo in the universe (all users/repos/??)  
c. what goes wrong if people use ramndom names for repo (conflicts)  
d. why setup yourself (distributed nature of git) instead of having it set up?  
justify which flag you use.  
type don't copy/paste (smart quotes are a problem)

3. switch or checkout is fine (switch is fine)

4. screenshot e-mail, don't send, do it in-character.

**Assessment 1 is due**

## Resources
[Lecture Slides](./resources/civ-ipriot-vcs-remotes.pptx)  
[Create a GitHub account (presentation)](./resources/AppProgPython-Create-GitHub-Account.pptx)  
[Chapter 5 of Head First Git](../../Head_First_Git_-_Raju_Gandhi.pdf)  
[Git - Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)  
[Git vs Github Video](https://www.youtube.com/watch?v=wpISo9TNjfU)

## Activities

**Revision Session 4**  
Branch over brunch:
1. In a new git repo, create a file called brunch.txt
2. In the file, enter the text "This is what I had for brunch:" <include what you had for brunch!>
3. Commit the changes
4. Create a new branch called brunch-branch. 
5. In the branch you created, add what you would have liked to have for brunch.
6. Merge the changes into the main branch.
7. Now branch out at brunch! 

<details>
<summary>
Solution (actual editing is up to you - vim is not recommended if you don't know how to use it):
</summary>

```
   62  cd source/repos/
   63  mkdir brunch
   64  cd brunch/
   65  git init
   66  vim brunch.txt
   67  git add brunch.txt
   68  git commit -m "what I had for lunch"
   69  git branch brunch-branch
   70  git switch brunch-branch
   71  vim brunch.txt
   72  git add brunch.txt
   73  git commit -m "what I'd like to have for lunch"
   74  git switch main
   75  git merge brunch-branch
   76  git log --oneline --decorate
```
</details>


