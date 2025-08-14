# Contents
- [Contents](#contents)
- [Week 1/Session 1 - Database Basics](#week-1session-1---database-basics)
  - [Overview](#overview)
  - [Notes](#notes)
    - [Why learn SQL?](#why-learn-sql)
    - [Tools](#tools)
    - [Data vs. Information](#data-vs-information)
    - [Terminology](#terminology)
      - [DBMS - Database Management System](#dbms---database-management-system)
      - [Client/"Viewer"](#clientviewer)
      - [Database](#database)
      - [Table](#table)
      - [Fields](#fields)
      - [Data Type](#data-type)
      - [Record](#record)
      - [Primary key](#primary-key)
      - [Index](#index)
      - [Query](#query)
    - [Syntax Rules](#syntax-rules)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 1/Session 1 - Database Basics
23/7/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_13866_1/cl/outline)

## Overview
In the first term learning will be SQL, the second term will be about creating  a desktop app with a SQL backend.

## Notes
### Why learn SQL?
The world is dependant on Databases,SQL is the language for interacting with them.
SQL  - Structured Query Language is the language for interacting with databases.

Unlike OOP, data driven programming focuses on data types and their relationships, it is the data itself that controls the program flow.

### Tools
Laragon:  
Recommended by TAFE, designed to run web servers for like PHP and such, but it has DBMS and phpMyAdmin out of the box, so it makes things easier but is fairly bloated. 

**PostgresSQL/DBeaver:  
More complex, should integrate nicely with VSCode and allow extension.**  
[PostgresSQL (Windows)](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)  
[DBeaver CE](https://dbeaver.io/download/)  


MySQL Server/MySQL Workbench:  
Another option, a little simpler to use, less powerful.

Base requirements are a database server and a client to view/interrogate and manage the database.

### Data vs. Information
Data is raw facts  
Information has context

| Data        | Information      |
|-------------|------------------|
| - Tex       | - Name: Tex      |
| - 6         | - Age: 6 Years   |
| - 7.4       | - Weight: 7.4 kg |

**Data** 
- No context
- Values only
- No insight to meaning

**Information**
- Units of measurement
- Context / meaning 

With additional context inferences can be made:  
*Age = 6 -> Tex is an adult cat.*


### Terminology
#### DBMS - Database Management System
An application that provides database management, data/user access and security, querying, reliable storage. The "brain" of the database.   
Examples: *MySQL, PostgreSQL, SQLite, Oracle DB, SQL Server*.  

#### Client/"Viewer"
Connects to the DBMS and provides tools for interactions such as a GUI, visual tools for designing tables, result viewing, server/admin tools.  
Examples: *MySQL Workbench, DBeaver, pgAdmin*.  

#### Database
A database is a storehouse of data that is "organised" and contains 0 or more tables. Databases can be relational, object, document, NoSQL or graph.  

#### Table
Tables are collections of data about one type of thing (cars, clients, pets etc), they should never store data about different types of things.  
For example, if a table contains details about people and also stores next of kin, that’s fine. If it is necessary to also store things about the next of kin, then that should probably be a separate linked table.  

#### Fields
Tables contain one or more fields, these fields help identify the data context.  
Examples: *Name, Age, Weight*.  

#### Data Type
The type of data in a field.  
Examples: *String, Int, Float, Date, Time*.

#### Record
One or more fields containing data which when combined represents a single entity, for example all the information about "Tex"  

#### Primary key
In order for a table to be useful, each record must be unique. The primary key contains this unique identifier, it may be made up by joining multiple fields. The primary key is a field property not a data type.  
Examples: *Tax File Number, Student ID, ISBN*.

#### Index
An index is used by databases to make searching faster at the cost of some storage space. Indexes are built around primary keys, as well as any secondary keys that are specified.  

#### Query
A query is asking a question, this is done using SQL.  
Example: *How many movies were made in 2024 and start with the letter 'A'"*

### Syntax Rules
* **Case-insensitive keywords:** SQL keywords like `SELECT`, `FROM`, `WHERE` are case-insensitive but usually written uppercase for clarity.

* **Semicolon (`;`) terminates statements:** Each SQL statement ends with a semicolon (sometimes optional depending on the tool).

* * **Identifiers (table/column names):** Usually case-insensitive, but quoting (e.g., `"ColumnName"`) makes them case-sensitive. 
  * Avoid spaces or special chars unless quoted.
  * snake_case is commonly used and good practice, though this is not enforced.
  * Table names should be short but descriptive.
  * Consistency is key.  

* **Indentation and formatting:** Not enforced, and there is no official standard, but it is vital for readability and maintenance. Whitespace and newlines are ignored for parsing, but often queries are formatted across multiple lines for readability.
  * Most teams adopt consistent styles.
  * Consistency is more important than the chosen style.

* **Strings:** Use single quotes `'like this'`. To include a single quote inside, double it up `''` or use escape sequences (e.g., PostgreSQL's `E'It\'s'`).

* **Aliases:** Can use `AS` (optional) for tables and columns (`SELECT col AS c FROM table AS t`)  
  - short aliases like `t` are common but descriptive ones help readability.

* **Statement order matters:** The logical order of operations differs from reading order:  
  `FROM` happens before `WHERE`, which happens before `SELECT`, etc.  

* **Avoid `SELECT *` in production:** It fetches all columns which is inefficient and brittle to schema changes.

* **Comments:**
  * Single line:` -- comment`
  * Multi-line: `/* comment */`
___
## Resources
[Lecture Slides](./resources/01-Database-Data-Basics.pptx)  

**Definitions**  
[Data Driven](https://www.techopedia.com/definition/18687/data-driven)  
[Database](https://www.techopedia.com/definition/database-db)  
[Table](https://www.techopedia.com/definition/1247/table)  
[Relational Database](https://www.techopedia.com/definition/1234/relational-database-rdb)  
[Primary Key](https://www.techopedia.com/definition/primary-key)  
[Database Management System](https://www.techopedia.com/definition/24361/database-management-systems-dbms)  

**Video**  
[you need to learn SQL RIGHT NOW!! (SQL Tutorial for Beginners)](https://www.youtube.com/watch?v=xiUTqnI6xk8)


## Activities
Do first assessment:   
https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_13866_1/cl/outline  

[Completed Assessment](./../assessments/test-1-ICTPRG431-KBA-1-Terminology.md)