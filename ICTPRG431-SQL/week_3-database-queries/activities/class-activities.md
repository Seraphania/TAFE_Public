# Overview

## Exercise 1
Create database and table and insert values.  
1. Create and use new database called E_Shop; Create the following table "customers" within the database:
2. **Table: Customers**
    | Field Name   | Data Type  | Size | Unsigned  | Null  | Zero Fill | Default | Primary Key |
    |--------------|------------|------|-----------|-------|-----------|---------|-------------|
    | given_name   | varchar    | 255  |           |       |           |         |             |
    | family_name  | varchar    | 255  |           |       |           |         |             |
    | address      | varchar    | 255  |           |       |           |         |             |
    | age          | tinyint    |      |     Y     |       |           |         |             |
    | gender       | char       | 1    |           |       |           |         |             | 

3. Insert the following entry into the customers table:  
   `('Jaques', “d'Carre”, '123 Some St, Waterdale, 1235', 43,'M')`
4. Insert the following into the table (multiple inserts):  
   ```
   ('Wander', “Along”, “1 Short Lane, Bigtown, 1235”, 23,'M'),  
   ('Me-Ann', 'Daring', '34 Long Street, Shortsville, 6543', 17,'F');
   ```

## Exercise 2
Create table and insert values.  
1. Create the following table "employees" and insert the values using single row inserts:
   | Given      | Family        | Address                                       | Age |
   |------------|---------------|-----------------------------------------------|-----|
   | Robyn      | Banks         | 8 Secure Road, Bankstown, Nevada, 123456      | 54  |
   | Eileen     | Dover         | 'The Lighthouse', Endstown, Somerset, EZ1 1AA | 23  |
   | Russell    | Leaves        | 1970 Forrest Street, Pinewood, 9873           | 48  |
   | May-Jorre  | Rhode-Werks   | 21 D'Toure Street, Ringswood, QLD, 4392       | 19  |

## Exercise 3
Create table.  
1. Create the following table "books":
   | Field      | Field Name | Data Type | Size | Unsigned  |
   |------------|------------|-----------|------|-----------|
   | ID         | id         | bigint    |      | Y         |
   | ISBN       | isbn       | varchar   | 16   |           |
   | Title      | title      | varchar   | 255  |           |
   | Subject    | subject    | varchar   | 32   |           |
   | Pages      | pages      | integer   |      | Y         |
   | Media type | media_type | char      | 1    |           |
   | Author     | author     | varchar   | 255  |           |
   
## Exercise 4
Create table.  
1. Create the following table "pens":
   | Field Name | Data Type | Size | Unsigned |
   |------------|-----------|------|----------|
   | Name       | varchar   | 128  |          |
   | EAN        | varchar   | 24   |          |
   | Type       | varchar   | 16   |          |
   | Colour     | varchar   | 32   |          |
   | Notes      | text      |      |          |

## Exercise 5
Practice deleting tables
1. Create and then delete the following two tables:  
   **Dummy:**
   | Field Name | Data Type | Size |
   |------------|-----------|------|
   | Name       | varchar   | 255  |
   | Age        | tinyint   |      |
   | Gender     | char      | 1    |

   **Another Dummy:**
   | Field Name  | Data Type | Size |
   |-------------|-----------|------|
   | Given Name  | varchar   | 255  |
   | Family Name | varchar   | 255  |

## Exercise 6
Update Columns
1. Add a column "amount_to_be_paid" to the "customers" table with float data type.
2. Set different values for "amount_to_be_paid" using `UPDATE` and `SET` commands.
3. Add a column "discount" with float data type in the table "customers".
4. Set different values of "discount" into each record using `UPDATE` and `SET` commands.
5. Add a column "paid_amount".
6. Set "paid_amount" by subtracting "discount" from "amount_to_be_paid" using update `UPDATE` and `SET` commands.

## Exercise 7
Using the dataset below, create the following queries:
1. Show the total population for each country code in reverse order of total.
2. Show the average population of each country in increasing  order of the average.
3. Show the first FIVE countries with zero total population.

```sql
CREATE TABLE locations(
    id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL DEFAULT '--ERROR--',
    population BIGINT DEFAULT -1,
    country_code CHAR(2) NOT NULL DEFAULT '--');

INSERT INTO locations(id, name, country_code, population) VALUES
    (1, 'Palikir - National Government Center', 'FM', 0),
    (2, 'Burg Unter-Falkenstein', 'DE', 0),
    (3, 'Guam Government House', 'GU', 0),
    (4, 'bishopric of Perugia', 'IT', 0), 
    (5, 'Linton Military Camp', 'NZ', 0), 
    (6, 'Chasse Royale', 'BE', 0),
    (7, 'Haselbachtal', 'DE', 0),
    (8, 'RMI Capitol', 'MH', 0), 
    (9, 'Ngerulmud', 'PW', 0),
    (10, 'Riverlea', 'ZA', 0),
    (11, 'Plymouth', 'MS', 0),
    (12, 'Cambebba', 'BR', 0),
    (13, 'Grytviken', 'GS', 2),
    (14, 'Port-aux-Francais (Port-aux-Français)', 'TF', 45),
    (15, 'Adamstown', 'PN', 46),
    (16, 'West Island', 'CC', 120),
    (17, 'Flying Fish Cove', 'CX', 500),
    (18, 'Alofi', 'NU', 624),
    (19, 'Jamestown', 'SH', 637),
    (20, 'Vatican City', 'VA', 829),
    (21, 'Kingston', 'NF', 880),
    (22, 'Amato', 'IT', 895),
    (23, 'Hamilton', 'BM', 902),
    (24, 'Brades', 'MS', 1000),
    (25, 'Hagatna (Hagåtña)', 'GU', 1051),
    (26, 'Yaren', 'NR', 1100),
    (27, 'Mata-Utu', 'WF', 1200),
    (28, 'Philipsburg', 'SX', 1400),
    (29, 'The Valley', 'AI', 2035), 
    (30, 'Longyearbyen', 'SJ', 2060),
    (31, 'Stanley', 'FK', 2213),
    (32, 'Iron River', 'US', 2904),
    (33, 'Kralendijk', 'BQ', 3081),
    (34, 'Cockburn Town', 'TC', 3720),
    (35, 'Funafuti', 'TV', 4492),
    (36, 'San Marino', 'SM', 4500),
    (37, 'Lobamba', 'SZ', 4557),
    (38, 'Vaduz', 'LI', 5197),
    (39, 'Marigot', 'MF', 5700),
    (40, 'Gustavia', 'BL', 5988);
```

## Notes
### Exercise 6
Part 6 -  `COALESCE(discount, 0)` is useful for handling the calculation where NULL is present; it treats all NULL values as 0 (other values can also be used). Otherwise any calculation involving a NULL value will result in NULL.

### Exercise 7
Part 2 - When using aggregates (AVG, SUM, MIN), a GROUP BY must be used.

## Tips


