CREATE TABLE employees (
	given_name VARCHAR(255), 
	family_name VARCHAR(255), 
	address VARCHAR(255), 
	age INT CHECK (age BETWEEN 1 AND 255));

INSERT INTO employees (given_name, family_name, address, age) VALUES 
	('Robyn', 'Banks', '8 Secure Road Bankstown, Nevada, 123456', 54);

INSERT INTO employees (given_name, family_name, address, age) VALUES 
	('Eileen', 'Dover', '''The Lighthouse'', Endstown, Somerset, EZ1 1AA', 23);
;
INSERT INTO employees (given_name, family_name, address, age) VALUES 
	('Russell', 'Leaves', '1970 Forrest Street, Pinewood, 9873', 48);

INSERT INTO employees(given_name, family_name, address, age) VALUES
	('May-Jorre', 'Rhode-Werks', '1 D''Toure Street, Ringswood, QLD, 4392', 19);
