-- Create or use the hbnb_test_db database
CREATE DATABASE IF NOT EXISTS solysis_test_db;

-- Create or use the hbnb_test user with the password 'hbnb_test_pwd' on localhost
CREATE USER IF NOT EXISTS 'solysis_test'@'localhost' IDENTIFIED BY 'solysis_test_pwd';

-- Grant all privileges on the hbnb_test_db database to the hbnb_test user
GRANT ALL PRIVILEGES ON solysis_test_db.* TO 'solysis_test'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the hbnb_test user
GRANT SELECT ON performance_schema.* TO 'solysis_test'@'localhost';
