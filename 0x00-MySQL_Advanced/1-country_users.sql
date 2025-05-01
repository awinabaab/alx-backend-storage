-- Creates a table named users with the following attributes:
-- id: intger, never null, auto increment and primary key
-- email: string(255 characters), never null and unique
-- name: string(255 characters)
-- country: enumeration of countries [US, CO, TN], never null


CREATE TABLE IF NOT EXISTS users (
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM("US", "CO", "TN") DEFAULT "US"
);
