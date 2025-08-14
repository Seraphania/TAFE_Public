# Contents
- [Contents](#contents)
- [Week 3/Session 3 - Database Queries](#week-3session-3---database-queries)
  - [Overview](#overview)
  - [Notes](#notes)
    - [Database Creation](#database-creation)
    - [Table Creation](#table-creation)
    - [Table Population](#table-population)
    - [Deleting Tables](#deleting-tables)
    - [Updating Tables](#updating-tables)
  - [Basic Select Queries](#basic-select-queries)
    - [Comparison Operators](#comparison-operators)
    - [Mathematical Functions](#mathematical-functions)
    - [Ordering Results](#ordering-results)
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
USE database_name; -- This is auto-connects to DB in MySQL, does not work in PG!
```
`USE database_name` does not work in PostgreSQL/DBeaver, connection must be done seperately after database creation. Either run the create seperately -> connect manually to the new DB -> create tables etc. Or use psql:
```sql
-- my_script.sql
CREATE DATABASE e_shop;
\c e_shop
CREATE TABLE customers (...);
INSERT INTO customers (...);
```

```bash
psql -U postgres -f my_script.sql
```
*see [syntax](./../week_1-database-basics/notes.md#syntax-rules) for style*  

### Table Creation
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
*AUTO_INCREMENT is a useful field property; if a NULL value is inserted into an AUTO_INCREMENT field the next record number in sequence will be used.*

### Table Population
Tables can be populated with the syntax:
```sql
INSERT INTO customers 
  (customer_id, given_name, family_name, address, age, gender) -- this part is optional in MySQL, not in PostgreSQL
  VALUES
    (0011, 'Jaques', "d'Carre", '123 Some St, Waterdale, 1235', 43, 'M');
    -- 0011 will be interpreted as binary by PSQL; use quotes or 11
    -- use 'd''Carre' to escape '
```

### Deleting Tables
Deleting tables is performed with the syntax `DROP TABLE table_name`.  
***Dropping tables cannot be undone!***

### Updating Tables
Field names can be added or removed after creation with the basic syntax:
```sql
ALTER TABLE table_name ADD COLUMN -- (or DROP)
field_name data_type(); -- data type is not required if dropping a field
```

`ALTER TABLE` can also be used to update values in a table wit `SET`;
```sql
ALTER TABLE customers 
  ADD COLUMN salary FLOAT(10, 2); -- Adds a new column called salary

UPDATE customers 
  SET salary=5,000; -- Make the salary for all customers 5,000

UPDATE customers 
  SET salary=6,000 WHERE age > 35; -- Change salary to 6,000 for customers over the age of 35
```

## Basic Select Queries
`SELECT` is the basic key word for querying information in a database, the basic syntax for searching for information is `SELECT * FROM table_name;`, this will retrieve all data from all fields in the specified table. It is inadvisable to search using `*` in large datasets.  

To retrieve all data from specified fields from a table the following syntax is used:
```sql
SELECT
  field_name1, field_name2, -- ...
FROM table_name;
```
Results from multiple fields can be combined using the `CONCAT` function, for example:
```sql
SELECT CONCAT (first_name, ' ', last_name) AS name
FROM customers;
```

### Comparison Operators
Select queries can be refined using conditions,  `>` `<` `>=` and `<=` are  the same as in Python or C#, however `=` is used to test equality (not "=="), and  `<>` (not !=) is used to test inequality.

the `LIKE` operator is used in `WHERE` clauses to search for specified patterns. It is often combined with:
* `%` - Wildcard representing any number of characters
* `_` - Wildcard representing only a single character.

The boolean operators `AND`, `OR`, `NOT` and `IN` (multiple `OR`'s)can be included with comparison operators. 

### Mathematical Functions
Mathematical and statistical operations such as `SUM` `AVG` (average) and `MIN`/`MAX` (minimum/maximum) can be performed on numerical results, for example:
```sql
SELECT SUM(age)
  FROM customers;
```
When using multiple fields, `GROUP BY` must be used for these aggregate functions.

### Ordering Results
Retrieved results can be ordered using the `ORDER BY` clarifier, for example:
```sql
SELECT * FROM customers
ORDER BY family_name DESC; --descending order
```
Ordering is done
* Alphanumerically for strings
* Numerically for numbers
* By date for data/time
The default order is ascending, but this can be reversed using the `DESC` switch.

The `DISTINCT` keyword will return only unique results from a query.

### Grouping
Grouping is subtly different from ordering, it is used for
* Gathering related data
* Counting Results
* Totalling values
* Basic statistics
An example is if a table "locations" contained location data that included `ID`, `location_name`, `population` and `country_code` a query could be created to determine how many countries shared the same country code:
```sql
SELECT country_code, COUNT(location_name)
  FROM locations
    GROUP BY country_code
      ORDER BY country_code;
```


### Limiting Results
To select only a certain number of results from a query, `LIMIT` is used:
```sql
SELECT * FROM customers
  WHERE age > 25
  LIMIT 5;
```
This will return only the first 5 matching results. Ranges can also be included, such as `LIMIT 4, 2`, this will start at the 4th matching entry and return the next 2 matches.
___
## Resources
[Lecture Slides](./resources/03-SQL-Queries.pptx)  
[Class Notes - SQL Queries](./resources/Class-Notes-SQL-Queries.pdf)  

## Activities
[In-class activity](./activities/class-activities.md)  
[Database Queries](activities/Database-Queries.pdf)
