# Contents
- [Contents](#contents)
- [Week 5/Session 5 - Database Normalisation](#week-5session-5---database-normalisation)
	- [Overview](#overview)
	- [Gathering Data](#gathering-data)
	- [Anomalies](#anomalies)
	- [Data Normalisation](#data-normalisation)
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
When gathering data it is important to think about the purpose for gathering the data, and gather data that is useful for answering a question. Excess non-useful data should not be kept for cost and efficiency reasons. The aim is not to gain data, but to gain knowledge, the difference is organisation.

## Anomalies
anomalies are created when a database is not well planned, for example if classes are only created in a student table, if a student is dropped, so is the reference to that class. 

A table is…
* First normal form if there are no arrays and no fields that store the same type of information as another field.
* Second normal form if it is first normal form and every field directly describes the thing represented by the primary key (not counting foreign keys).
* Third normal form if it is second normal form and no field depends on or is derived from any other field except the primary key.

## Data Normalisation
Normalisation is the process of structuring a database in a way that optimises the database and reduces data redundancy, making the database more efficient. The process is generally done in 3 steps called 'normal forms', and may involve adding fields or even entire tables. 

1. Collect data - Import raw data, use forms or other processes.
2. ONF - create a big sample - don't work with it.
3. 1NF - Fields that duplicate other fields.
4. 2NF - Ensure fields describe only what is represented by the primary key.
5. 3NF - Fields only depend on the primary key.


### First Normal Form (1NF)
A database is considered 1NF if:
* Each field contains a single value rather than a list of values. No arrays (all data values are atomic). Remove multiple fields that store the same type of information such as “FirstParent”,“SecondParent”.
* Each field has a unique name.
* There is a primary key.

This may involve changing the schema, this can be done using raw SQL commands.

### Second Normal Form (2NF)
A database is considered 2NF if 
* It is 1NF
* All non key attributes depend on all parts of the primary key. - This means that all the fields in the database should describe the thing that the primary key identifies. If a table of cars has a field for the owner name, this is not 2NF since the name of the owner does not describe the car.  

Foreign keys are exempt from this rule. So, if you have a car table and there is a driver’s license number of the owner which allows you to look him or her up in another table, then that’s fine. However ideally join tables will be used instead.

**Example Database in 2NF:**
```sql
DROP DATABASE tafe;
CREATE DATABASE tafe;

USE tafe;

CREATE TABLE if NOT EXISTS students (
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
	student_number VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	address VARCHAR(255));

CREATE TABLE if NOT EXISTS classes (
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
	`name` VARCHAR(255),
	`code` VARCHAR(255));

CREATE TABLE if NOT EXISTS enrolments (
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
	class_id BIGINT NOT null,
	student_id BIGINT NOT NULL,
	FOREIGN KEY(class_id) REFERENCES classes(id),
	FOREIGN KEY(student_id) REFERENCES students(id));

DESCRIBE students;
DESCRIBE classes;
DESCRIBE enrolments;

INSERT INTO students 
	(student_number, first_name, last_name, address)

VALUES
	('J123', 'Mila', 'Maxwell', 'The plain of spirits'),
	('2032', 'Jude', 'Mathis', 'Fennmont'),
	('0123', 'Lloyd','Irving', 'Iselia');

INSERT INTO classes
 (`name`, `code`)

VALUES
	('Version Control and Object Oriented', 'RIoT'),
	('Data Driven Applications', 'DDA');

SELECT * FROM students;
SELECT * FROM classes;

INSERT INTO enrolments
	(student_id, class_id)

VALUES
	(1,1),
	(1,2),
	(2,1),
	(3,1);

SELECT * FROM students;
SELECT * FROM classes;
SELECT * FROM enrolments;
```

### Third Normal Form (3NF)
A database is considered 3NF if:
* It is 2NF
* All non-key attributes do not depend on any other non-key attributes.

If a car table stored both model and manufacturer, then it is not 3NF because the model is dependent on the manufacturer. Ford doesn’t have a Corolla - only Toyota does. What model you have is partially determined by the manufacturer of the car.

As another example, imagine a table of patient data that stores height, weight, body mass index and a boolean for whether they are overweight or not. Whether someone is overweight or not is determined from the BMI, so the boolean is dependent on the BMI value, making the table not 3NF.  
Furthermore, the BMI is calculated from the weight and height, making it dependent as well.

### Caveat
They’re Only Guidelines!  
Although it is ideal, it is not always possible or practical to have a fully 3NF database. Having weight, height and BMI in the same health data table does make sense, after all. However, if you find yourself with a table that does not abide by some of the rules above, make sure you have a good reason not to fix it.

It should also be pointed out that the higher the normal form, the more acceptable it is not to abide by it. There are a few good databases that aren’t 3NF, very few that aren’t 2NF and databases that are not 1NF should basically never happen.


## Entity digrams
https://app.diagrams.net/


___
## Resources
[Lecture Slides](./resources/05-Database-Design-Normalisation.pptx)  
[Class Notes](./resources/Class-Notes-Normalising-Databases.pdf)    

## Activities
[In-class activity](./activities/class-activities.md)  