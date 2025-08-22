# Contents
- [Contents](#contents)
- [Week 5/Session 5 - Database Normalisation](#week-5session-5---database-normalisation)
  - [Overview](#overview)
  - [Gathering Data](#gathering-data)
  - [Anomalies](#anomalies)
  - [Normalising Databases](#normalising-databases)
    - [First Normal Form (1NF)](#first-normal-form-1nf)
    - [Second Normal Form (2NF)](#second-normal-form-2nf)
    - [Third Normal Form (3NF)](#third-normal-form-3nf)
    - [Caveat](#caveat)
  - [Entity digrams](#entity-digrams)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 5/Session 5 - Database Normalisation
20/8/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_13866_1/cl/outline)  
[menti.com/alpq7w7kifhd](https://www.menti.com/alpq7w7kifhd)  


## Overview
Gathering Data  
Data anomalies & consistency
what is normalisation

## Gathering Data
Think about the purpose for gathering data, and gather data that is useful for answering a question. Excess non-useful data should not be kept for cost and efficiency reasons. The aim is not to gain data, but to gain knowledge, the difference is organisation.

## Anomalies
anomalies are created when a database is not well planned, for example if classes are only created in a student table, if a student is dropped, so is the reference to that class. 

A table is…
* First normal form if there are no arrays and no fields that store the same type of information as another field.
* Second normal form if it is first normal form and every field directly describes the thing represented by the primary key (not counting foreign keys).
* Third normal form if it is second normal form and no field depends on or is derived from any other field except the primary key.

## Normalising Databases
Normalisation is the process of structuring a database in a way that optimised the database and reduces data redundancy, making the database more efficient. The process is generally done in 3 steps called 'normal forms', and may involve adding fields or even entire tables. 

Collect data
ONF create a big sample - don't work with it.
1NF remove rows that repeat each other.


### First Normal Form (1NF)
A database is considered 1NF if each field contains a single value rather than a list of values. So, arrays or anything like arrays are not permitted. This includes having multiple fields that store the same type of information such as “FirstParent” and “SecondParent”, or “FirstCarNumberPlate” and “SecondCarNumberPlate”.

### Second Normal Form (2NF)
A database is considered 2NF if it’s 1NF and all the columns depend on the primary key. This means that all the fields in the database should describe the thing that the primary key identifies. If you have a table of cars and a field for the owner name, then that is not 2NF since the name of the owner does not describe the car.  

Foreign keys are exempt from this rule. So, if you have a car table and there is a driver’s license number of the owner which allows you to look him or her up in another table, then that’s fine.

### Third Normal Form (3NF)
A database is consider 3NF is it is 2NF and all the columns except the primary key are independent of each other. 

Consider the car example again. If the car table stored both model and manufacturer, then it is not 3NF because the model is dependent on the manufacturer. Ford doesn’t have a Corolla - only Toyota does. What model you have is partially determined by the manufacturer of the car.

As another example, imagine a table of patient data that stores height, weight, body mass index and a boolean for whether they are overweight or not. Whether someone is overweight or not is determined from the BMI, so the boolean is dependent on the BMI value, making the table not 3NF.  
Furthermore, the BMI is calculated from the weight and height, making it dependent as well.

### Caveat
They’re Only Guidelines!  
Although it is ideal, it is not always possible or practical to have a fully 3NF database. Having weight, height and BMI in the same health data table does make sense, after all. However, if you find yourself with a table that does not abide by some of the rules above, make sure you have a good reason not to fix it.

It should also be pointed out that the higher the normal form, the more acceptable it is not to abide by it. There are a good few databases that aren’t 3NF, very few that aren’t 2NF and databases that are not 1NF should basically never happen.

## Entity digrams
https://app.diagrams.net/


___
## Resources
[Lecture Slides](./resources/05-Database-Design-Normalisation.pptx)  
[Class Notes](./resources/Class-Notes-Normalising-Databases.pdf)    

## Activities
[In-class activity](./activities/class-activities.md)  

Questions for Para:
* What should we have covered
* Have we covered "describing tables"
* Week 4 activities - create the databases or just describe them?
* psql connecting to DB's?