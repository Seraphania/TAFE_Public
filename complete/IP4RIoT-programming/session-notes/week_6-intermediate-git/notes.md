# Contents
- [Contents](#contents)
- [Week 6/Session 7 - Intermediate GIT](#week-6session-7---intermediate-git)
  - [Intermediate Git](#intermediate-git)
    - [Diff](#diff)
    - [Undoing Changes](#undoing-changes)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 6/Session 7 - Intermediate GIT
https://blackboard.northmetrotafe.wa.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_35877_1&content_id=_4134211_1


**Objectives**  
* Produce a diff
* Interpret a diff
* Deal with mistakes

**Curriculum alignment**  
Aligns with the following elements of ICTICT449 Use version control systems in development environments:
>3.3 Locate track of initial version change and confirm new status according to service provider procedures


**Relevance to industry**  
Git is about managing change over time and a diff is a change over time - so it is crucial to read and interpret diffs. Further, mistakes often happen and git is unique in that we can fix mistakes in the history as well as in our files. In industry, you are expected to know how to do both. One thing to consider though is that many use visual tools and integration with issue tracking to provide better visibility to changes and this is beyond the scope for this session.

**Relevance to assessment**  
Relates to using git which is relevant to many assessments in this and other units

**How to use this information**
* Follow the lecture slides and recording if applicable
* Complete the activity outlined 

## Intermediate Git
### Diff
* Crating and interpreting diffs
* Regverting and resetting
* Stashing

Diff standss for difference - standard representation of the difference between text files or sets of text files.

Designed to be human readable but an IDE makes it easier.

They provide enough fidelity to be used as a *patch* 
Patch is enough information to make a change, a patch is a bit like merging a branch, applying the changes is a merge, the patch are the changes. **The patch just contains the differences, not the whole code file.**

When `git status` is run, you're asking what are the changes, same when you merge, it's all about teh deifference (push and pull too).

When running a pull request you see what the changes are, shows what changes exist folder/line/word/character.

diffs can be performed at many levels; between:
files, comits staging (index) and object db (repo) and working copy of any of the above.

git diff is like built in unix diff.

Diff has a header: symbol (+/-) associated with insertion
an insertion in the past is a deletion in the future.

both represent insertions?! 

![alt text](./resources/diff-insertions.png)  
--- is insertions from original_program.py
+++ is insertions from modified_program.py

```
File 1 - Original
A
B
C
___
File 2 - Modification

B
C
D
```
"A" is inserted from original, "D" is inserted from Modification.
Diff just shows differneces (don't worry about resolving conflicts for now).  

 `@@` is the hunk header, it directs where the changes need to be made.

 Fist number where the diff starts, second number is the number of lines showing.

 and it's only a section of the file (a patch), the line numbers above don't relate to lines in the actual files.

### Undoing Changes
Git stores everything, it's not always a good thing.if yo add something you didn't mena to (or committed to the wrong branch), you can revert.

rewrite the history to remove unnescessary commits. Can only do this with a shared history (or permissions.) Subversive changes are a problem if the changes have been distributed.

**Revert vs reset**  
Revert changes by creating anew commit  
Reset changes by removing from history  

![Revert vs Reset](./resources/revert-vs-reset.png)

*For excercise, fork all branches (not just main), which github defaults to.*

## Resources
[Lecture Slides](./resources/civ-ipriot-vcs-intermediate-git-cmds.pptx)  
[Dangit Git!](https://dangitgit.com/en)  

## Activities
[Git Diff and Stash Excercise](https://github.com/NM-TAFE/ipriot-diff-exercise)
