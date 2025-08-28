CREATE TABLE dummy (
	name VARCHAR(255),
	age SMALLINT,
	gender CHAR(1));
	
CREATE TABLE another_dummy (
	given_name VARCHAR(255),
	familly_name VARCHAR(255));

DROP TABLE dummy;

DROP TABLE IF EXISTS another_dummy;
