-- Preparint test script for mySQL server

-- Creating test DB
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creaitng new test user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Granting test user all PRVG on hbnb_test_db
GRANT ALL PRIVILEGES ON hbtn_test_db.* TO 'hbnb_test'@'localhost';

-- Granting 'select' PRVG on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- applying changes
FLUSH PRIVILEGES;
