# Contents
- [Contents](#contents)
- [Week 8/Session 9 - DevOps and Version Control](#week-8session-9---devops-and-version-control)
  - [What is DevOps](#what-is-devops)
  - [CI/CD Practices](#cicd-practices)
  - [GitHub for Devops:](#github-for-devops)
  - [Before Next session:](#before-next-session)
  - [Resources](#resources)
  - [Activities](#activities)


# Week 8/Session 9 - DevOps and Version Control
https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_35877_1/cl/outline

**Objectives**  
Introduce common industry jargon and associated practices and relate it to Git and GitHub. Specifically, you should be familiar with the following terms:
* DevOps and DevOps Automation Tools
* Continuous Integration and Deployment/Delivery (CI/CD) 

**Curriculum alignment**  
Aligns with knowledge evidence such as web-based DevOps lifecycle tools and DevOps automation tools associated with elements 1-4 in ICTICT449.

**Relevance to industry**  
DevOps as a term is frequently used in industry to mean different things to different people. DevOps itself encompasses advanced tooling and practices. As an organizational role, it is typically associated with significant software development experience. Thus, at this stage, we are more interested in familiarity with the jargon over and above an ability to perform core functions usually associated with DevOps.

**Relevance to assessment**  
Your assessment activity requires you to associate practices identified in a mock organizational standard with DevOps concepts and terms.

**How to use this information**  
*Before the session*

Complete unit 2 and 3 of the following Microsoft training package (include the multiple choice questions):

**unit 2**  
[What is DevOps? - Training What is DevOps? chcomley](https://learn.microsoft.com/en-us/training/modules/get-started-with-devops/2-what-is-devops)


**unit 3**  
[What is Azure DevOps? - Training What is Azure DevOps? chcomley](https://learn.microsoft.com/en-us/training/modules/get-started-with-devops/3-what-is-azure-devops)

 

> During the session


Follow the recording or lecture associated with the slides

> After the session


Familiarize yourself with the organizational standards that will be used in the remaining assessments.
Watch the entertaining video on software development methodologies (that also link to learning material in ICTPRG302)
Start work on your assessment  
https://blackboard.northmetrotafe.wa.edu.au/webapps/assignment/uploadAssignment?content_id=_3663744_1&course_id=_35877_1&group_id=&mode=cpview

___

## What is DevOps
A combination of two term Development and Operations, combining two terms that are generally not ocnnected.  
Links development (coding) and Operations - the environment, networking service provision etc.  

Ops might be might be more involved with networking hardware etc, whereas develoers are creating features, there have historically been some tension between the two. Often get the flack for issues and downtime.  

Ops often slows development (being concerned with security etc.)

Infrasturture has changed a lot given it is common to use cloud computing, so there can be friction with security and who owns what, now you have to consider what hardware it will be run on during development, previously development released cycles were around 6 months long, now they may be as short as a day. Initially operations was resistant to this due to the amount of work that needed to be done/amount of things to be managed.

DevOps tries to combat that by having development and ops being less siloed. Aims to streamline the process od releasing. It's a bit jargony, but is basically about teh need for good tooling to manage and automate software lifecycles.

Bit of a cultural change, this will become more apparent once we have to compile our programs.

GitLab came up with a way of integrating all the DevOps tools, there are others, but GitLab is one of the best examples.

https://roadmap.sh/ is great for working out what kind of skills you need for what job.

## CI/CD Practices
Continuous Integration
- Merging developers work into the "mainline" often
- Sometimes several times per day (this avoids conflicts)
Unit testing is testing that your specific functions work and don't affect anything downstream.

Continuous Delivery/Deployment
- Deployment generally used for cloud based code, whereaas delivery for stand alone, e.g. choromium (hourly updates).
- Ensuring that code is always deploayable  
  
Code coverage means how much of the code is currently covered by tests - code coverage should always be increased, never decreased.

CD requires CI, CI does not always require CD.

Splunk is a way of monitoring logs. 

## GitHub for Devops:
Has lots of tools, wikis, issue tracking etc.
All part of lifecycle tools. 

## Before Next session: 
Read through AT2 KBA Part 1
For final question; don't just say "Github stores source code"!
Don't submit until after class.


## Resources
[Lecture Slides](./resources/civ-ipriot-devops.pptx)  
[DevOps and CI/CD Fundamentals](https://www.youtube.com/watch?v=2qlcY9LkFik&embeds_referring_euri=https%3A%2F%2Fblackboard.northmetrotafe.wa.edu.au%2F&source_ve_path=Mjg2NjY)  
[How GitHub Actions 10x my productivity](https://blackboard.northmetrotafe.wa.edu.au/webapps/blackboard/content/http/x3A/x2F/x2Fwww.youtube.com/x2Fwatch/x3Fv/x3DyfBtjLxn_6k)  


## Activities
[CI/CD exercise](https://coderefinery.github.io/testing/continuous-integration/)  
[GitHub vs. GitLab - Who dominates dev world?](http\x3A\x2F\x2Fwww.youtube.com\x2Fwatch\x3Fv\x3Dm_DcXayqFy8)  