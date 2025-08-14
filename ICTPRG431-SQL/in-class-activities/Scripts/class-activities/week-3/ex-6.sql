ALTER TABLE customers ADD COLUMN amount_to_be_paid FLOAT;

UPDATE customers
	SET amount_to_be_paid=5000;
	
UPDATE customers
	SET amount_to_be_paid=5500 WHERE age>30;

ALTER TABLE customers ADD COLUMN discount FLOAT;

UPDATE customers
	SET discount=13.37 WHERE given_name LIKE '%a%';

ALTER TABLE customers ADD COLUMN paid_amount FLOAT;

UPDATE customers
	SET paid_amount=(amount_to_be_paid - COALESCE(discount, 0));