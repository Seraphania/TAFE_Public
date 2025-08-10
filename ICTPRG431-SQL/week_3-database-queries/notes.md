# Contents
- [Contents](#contents)
- [Week 3/Session 3 - Database Queries](#week-3session-3---database-queries)
  - [Overview](#overview)
  - [Notes](#notes)
    - [Database Creation](#database-creation)
    - [Creating Tables](#creating-tables)
    - [Table Population](#table-population)
    - [Deleting Tables](#deleting-tables)
    - [Updating Tables](#updating-tables)
    - [BREAD \& CRUD](#bread--crud)
    - [Browsing a Table](#browsing-a-table)
    - [Browsing with filters](#browsing-with-filters)
    - [Grouping](#grouping)
    - [Limiting Results](#limiting-results)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 3/Session 3 - Database Queries
6/8/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_35877_1&content_id=_3663745_1)

[Raf's Lecture materials](https://github.com/NM-TAFE/civ-ipriot-in-class-demos/tree/2025/s1/raf)

## Overview
From Blackboard if available

## Notes
Review:
* Data types
  * Numbers (int, bigint, float, decimal)
  * Strings (char, varchar, text)
  * Dates and times (date, time, datetime)
* Create a simple table
* Add data to the simple table

### Database Creation
Tables must belong to a database, so creating a database before creating tables is necessary.  
The basic syntax to create a new database is:
```sql
CREATE DATABASE database_name;
USE database_name; -- This is a prerequisite for going on to create tables.
```
*see [syntax](../week_1-database-basics/notes.md#syntax-rules) for style*  

### Creating Tables
Tables are created with the syntax:
```sql
USE database_name;
CREATE TABLE table_name (
  field_name data_type(size) other_options,
  -- ... repeat as needed for each field
);
```


Tables should only contain data related to a single subject for example customers, students, lecturers etc, all tables must have a primary key. Below is an example definition of a table:
**Table: Customers**
| Field Name   | Data Type  | Size | Unsigned  | Null  | Zero Fill | Default | Primary Key |
|--------------|------------|------|-----------|-------|-----------|---------|-------------|
| given_name   | varchar    | 255  |           |       |           |         |             |
| family_name  | varchar    | 255  |           |       |           |         |             |
| address      | varchar    | 255  |           |       |           |         |             |
| age          | tinyint    |      |     Y     |       |           |         |             |
| gender       | char       | 1    |           |       |           |         |             |  

*The last 4 columns will be explained in later weeks*

The SQL query to create this table is:
```sql
CREATE TABLE customers (
  customer_id INT PRIMARY KEY, -- this can also be defined later with: PRIMARY KEY(customer_id)  
  given_name VARCHAR (255),
  family_name VARCHAR (255),
  address VARCHAR (255),
  age TINYINT unsigned, -- Postgres has no tinyint, it can be substituted with: age INT CHECK (age BETWEEN 1 AND 255),
  gender CHAR (1)
);
```

### Table Population
Tables can be populated with the syntax:
```sql
INSERT INTO customers 
  (customer_id, given_name, family_name, address, age, gender) -- this part is optional
  VALUES
    (0011, 'Jaques', "d'Carre", '123 Some St, Waterdale, 1235', 43, 'M');
    -- 0011 will be interpreted as binary by PSQL; use quotes or 11
    -- use 'd''Carre' to escape '
```
___
___
___
Up to slide 13 (Exercise 1 creating tables)

### Deleting Tables

### Updating Tables

### BREAD & CRUD

### Browsing a Table

### Browsing with filters

### Grouping

### Limiting Results

___
## Resources
[Lecture Slides](./resources/03-SQL-Queries.pptx)  
[Class Notes - SQL Queries](./resources/Class-Notes-SQL-Queries.pdf)  

## Activities
[In-class activity](./activities/class-activities.md)  
[Database Queries](activities/Database-Queries.pdf)
