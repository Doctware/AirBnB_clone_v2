-- Preparing MySQL server

-- Creating my Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating a new use
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting user hbnb_dev all privileges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Granting 'SELECT' privilege to user hbnb_dev on perfomance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- apply changes
FLUSH PRIVILEGES;
