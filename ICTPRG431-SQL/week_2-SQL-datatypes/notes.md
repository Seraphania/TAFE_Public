# Contents
- [Contents](#contents)
- [Week 2/Session 2 - SQL Datatypes and Creating Tables](#week-2session-2---sql-datatypes-and-creating-tables)
  - [Overview](#overview)
  - [Data Types](#data-types)
    - [DBMS Data Type Comparison](#dbms-data-type-comparison)
      - [Numeric](#numeric)
      - [Binary](#binary)
      - [String](#string)
      - [Date and Time](#date-and-time)
      - [Quick Comparison Reference (GPT)](#quick-comparison-reference-gpt)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 2/Session 2 - SQL Datatypes and Creating Tables
30/7/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_13866_1/cl/outline)

## Overview
This session covers SQL Data Types.  
**Database and table creation are covered in session 3 also, so the notes are contained in the [week 3 notes](./../week_3-database-queries/notes.md).**

## Data Types
There are many data types in SQL, broadly speaking these are:
* Numeric
  * INT, DECIMAL, FLOAT, NUMERIC
* Binary
  * BINARY, BLOB
* String
  * CHAR, VARCHAR, TEXT
* Boolean
  * BOOLEAN
* Date/Time
  * DATE, TIME, DATETIME
* Special
  * UUID
  * AON
  * XML
  * JSON

Every field in an SQL table must have a data type.
Different DBMS will have different specific data types which expand on the standard SQL Types. The reason for this specificity is to provide accuracy and also save on memory space.

Documentation:  
[MySQL](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)  
[MariaDB](https://mariadb.com/docs/server/reference/data-types)  
[PostgreSQL](https://www.postgresql.org/docs/current/datatype.html)  
[SQL Server (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver15)  

### DBMS Data Type Comparison
#### Numeric
| MySQL            | MariaDB          | PostgreSQL       | SQL Server       |
|------------------|------------------|------------------|------------------|
| bit, tinyint, smallint, integer, bigint| bit, tinyint, smallint, int, bigint, boolean | smallint, integer, bigint | bit, tinyint, smallint, int, bigint |
| decimal, numeric | decimal, numeric | decimal, numeric | decimal, numeric |
| flaot, double, real | float, double, real | float, double, precision | real, float |
|                  | money            |                  | money, smallmoney |

Floating point numbers sacrifice precision for space saving, large numbers are stored as exponents.  
`123,456,789.12345` is stored in a float as 1.2345678912345 x 10<sup>8</sup>, this may be truncated if the storage allocated to store the number isn't large enough:  
For example with 6 characters it becomes 1.23456 x 10<sup>8</sup>.  
Once translated back into a non-exponent, it becomes `123,456,000` which is very different from the original.  
This, combined with addition/subtraction causes *error propagation*.

***For large numbers or numbers where precision is required decimal should be used.***

#### Binary
| MySQL            | MariaDB          | PostgreSQL       | SQL Server       |
|------------------|------------------|------------------|------------------|
| binary           | binary           | bytea            |  binary          |
| varbinary        | varbinary        |                  | varbinary        |
| blob             | tinyblob         |                  | image            |
|                  | blob             |                  |                  |
|                  | longblob         |                  |                  |

BLOB is Binary Large Object. It describes a large file of graphics, Video or audio.

#### String
| MySQL            | MariaDB          | PostgreSQL       | SQL Server       |
|------------------|------------------|------------------|------------------|
| char             | char             | char             | char             |
| varchar          | varchar          | varchar          | varchar          |
| text             | text             | text             | text             |
|                  |                  |                  | nchar            |
|                  |                  |                  | nvarchar         |
|                  |                  |                  | ntext            |

In PostgreSQL, `CHAR(n)` always stores exactly `n` characters, padding with spaces if the value is shorter. For example, a `CHAR(7)` column storing `'Male'` will still take space for 7 characters (plus minor overhead).  
`VARCHAR(n)` stores up to `n` characters, but only uses as much space as needed for the actual value, plus a few bytes of length overhead. For example a `VARCHAR(20)` column storing `'Male'` will take space for 4 characters (plus minor overhead).  
`TEXT` can store very large strings (up to around 1GB) and has no fixed limit. In PostgreSQL, `VARCHAR` without a length limit behaves the same as `TEXT`.


#### Date and Time
| MySQL            | MariaDB          | PostgreSQL       | SQL Server       |
|------------------|------------------|------------------|------------------|
| date             | date             | timestamp        | date             |
| time             | time             | date             | time             |
| datetime         | datetime         | time             | datetime         |
| timestamp        | timestamp        | interval         | datetimeoffset   |
| year             | year             |                  | smalldatetime    |

Date and time formats:
* DATE - YYYY-MM-DD
* DATETIME - YYYY-MM-DD HH:MI:SS
* TIMESTAMP - YYYY-MM-DD HH:MI:SS
* YEAR - YYYY or YY


#### Quick Comparison Reference (GPT)


| MySQL / MariaDB         | PostgreSQL       | Size (bytes) | Notes |
|-------------------------|------------------|--------------|-------|
| TINYINT                 | SMALLINT         | 2            | PG min is 2 bytes; MySQL's 1‑byte type doesn't exist in PG |
| SMALLINT                | SMALLINT         | 2            | Same size |
| MEDIUMINT               | INTEGER          | 4            | PG skips 3‑byte ints |
| INT / INTEGER           | INTEGER          | 4            | Same size |
| BIGINT                  | BIGINT           | 8            | Same size |
| DECIMAL(p,s) / NUMERIC  | NUMERIC          | ~2 bytes/4 digits + overhead | Variable size; depends on precision |
| FLOAT                   | REAL             | 4            | MySQL float = PG real |
| DOUBLE / DOUBLE PRECISION | DOUBLE PRECISION | 8          | Same size |
| CHAR(n)                 | CHAR(n)          | n + 1        | Fixed width; n padded with spaces, +1 for length byte |
| VARCHAR(n)              | VARCHAR(n)       | length + 1   | Only stores actual chars used, +1 for length byte |
| TEXT                    | TEXT             | var          | No length limit; stored out‑of‑row if large |
| BLOB / VARBINARY        | BYTEA            | var          | PG just uses bytea for all binary data |
| DATE                    | DATE             | 4            | Stores as days since epoch |
| DATETIME / TIMESTAMP    | TIMESTAMP (no tz)| 8            | Stores microseconds since epoch |
| TIME                    | TIME             | 8            | Stores microseconds since midnight |
| YEAR                    | SMALLINT         | 2            | PG has no YEAR type; use smallint or date constraints |

___
## Resources
[Lecture Slides](./resources/02-Database-Data-Types.pptx)  
[Data Types in SQL (Web Link)](https:www.w3schools.com/sql/sql_datatypes.asp)  
[SQL Tutorial (Web Link)](https://www.w3schools.com/sql/sql_select.asp)  
[Class Notes - Data Types in SQL](resources/Class-Notes-Data-types-in-SQL.pdf)

## Activities
~~[In-class activity: Portfolio Exercise - Creating Tables](./../week_3-database-queries/activities/portfolio-excercise/Portfolio-Exercise-Creating-Tables.md)~~  In Blackboard under Session 2, but fits better with week 3.  
Do second assessment:   
https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_13866_1/cl/outline  

[Completed Assessment](./../assessments/test-2-ICTPRG431-KBA-2-SQL-Datatypes.md)
