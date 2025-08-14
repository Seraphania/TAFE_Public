CREATE DATABASE test; -- PostgreSQL  this has to be done seperately, then manually connect to the new DB.

CREATE TABLE customers (
	given_name VARCHAR(255),
	family_name VARCHAR(255),
	address VARCHAR(255),
	age INT CHECK (age BETWEEN 1 AND 255),
	gender CHAR(1));


INSERT INTO customers (given_name, family_name, address, age, gender) VALUES 
	('Jaques', 'd''Carre', '123, Some Street, Waterdale, 1235', 43, 'M')

INSERT INTO customers (given_name, family_name, address, age, gender) VALUES
   ('Wander', 'Along', '1 Short Lane, Bigtown, 1235', 23,'M'),  
   ('Me-Ann', 'Daring', '34 Long Street, Shortsville, 6543', 17,'F');
