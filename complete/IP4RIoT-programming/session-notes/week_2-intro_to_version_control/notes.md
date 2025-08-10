# Contents
- [Contents](#contents)
- [Week 2/Session 2/3 - Intro to CLI and Intro to Version Control](#week-2session-23---intro-to-cli-and-intro-to-version-control)
    - [Version Control](#version-control)
    - [Types of version control](#types-of-version-control)
    - [GIT](#git)
    - [Resources](#resources)


# Week 2/Session 2/3 - Intro to CLI and Intro to Version Control

###  Version Control 
Is important, apparently one drive does this.
* Records changes made to files or sets of files/folders.
* Also records who made changes and what (specifically) they changed.
* Allows a user to go back to previous versions.
* Allows multiple people to work on the same project at the same time (even the same file - though it's not ideal)

The most valuable part of a program is the source code. Example the value of a copy of windows is hot much, but the source code represents billions of dollars of investment, and trillions of dollars in value.

Linux kernal is 
* ~27 milion lines of code (100,000 lines in all the Harry Potter books).
* ~70,000 files
* ~75,000 edits/year
* 1000's of contributors

GIT used in many areas, not just software dev.  
GIT Concepts:  
*metadata (also called the **repoository**)*  
*working tree/working copy* (files)  
*commit*  
*branch*  
*clone* only for distributed  
*remote*  

### Types of version control
* Local
* Centralised
  * everything hosted in one place.
  * Still work on a local copy.
* Distributed
  * everyone gets their own repository, including history and metadata (weird).
  * User histories don't interact.
  * GIT is distributed


Examples of different version control systems:
* Subversion: (SVN) Centralised. Open Source
* GIT: Distributed, Open source
* Mercurial: Distributed, Open source
* Bitkeeper: Distributed, Open source

### GIT
*is an asshole, but widely used*
* Is awesome
* Is not GitHub

`git init` initialise to make a folder a git repo

*will need to demonstrate setting up global repo settings, but won't have to actually nuke anything. for assignment*
  
* `git init` Initializes a new Git repository. This creates a new .git directory in your project, which Git uses to track and manage the project's history.
* `git add <file>` Adds changes in the working directory to the staging area. It tells Git you want to include updates to a specific file(s) in the next commit. However, git add does not affect the repository until you commit the changes.
* `git add .` (to add all changes)
* `git commit` Saves the staged changes to the repository. Each commit has an associated message, which is a description explaining why a particular change was made. Remember: if you forget -m, you get the escape room. Usage: `git commit -m "Your message here"`
* `git status` Shows the status of changes as untracked, modified, or staged. This command is helpful for seeing what changes have been added to the staging area and which files are not being tracked by Git.


### Resources
[Command Line Cheet Sheet](./resources/command_line_cheet_sheet.md)  
[Command Line Presentation](./resources/Command-Line-Basics.pptx)  
[Command Line Lecture Slides](./resources/civ-ipriot-command-line.pptx)  

[Intro to Version Control Lecture Slides](./resources/civ-ipriot-vcs-intro.pptx)  
[Basic Git Commands](./resources/command_line_cheet_sheet.md)  
[Chapter 1 of Head First Git](../../Head_First_Git_-_Raju_Gandhi.pdf)  

Git Tutorial: https://www.youtube.com/watch?v=8JJ101D3knE  
Another Git Tutorial: https://www.youtube.com/watch?v=tRZGeaHPoaw  
The Bastard responsible! (Linus Torvalds on Git): https://www.youtube.com/watch?v=4XpnKHJAok8  
