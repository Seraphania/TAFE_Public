CREATE DATABASE Stocks;

CREATE TABLE current_stock_price (
	stock_ticker VARCHAR(10) PRIMARY KEY,
	company_name VARCHAR(255),
	current_share_price DECIMAL(6,6)
);