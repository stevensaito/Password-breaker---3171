	-- Create the pizza_database database
DROP DATABASE IF EXISTS jellies_DATABASE;
CREATE DATABASE jellies_DATABASE;
USE jellies_DATABASE;  -- MySQL command


CREATE TABLE users (
  userID					INT(50)			NOT NULL	AUTO_INCREMENT,
  username					VARCHAR(255)    NOT NULL,
  password					VARCHAR(255)  NOT NULL,
  PRIMARY KEY (userID)
);


INSERT INTO users VALUES
(3171, 'jseanettles', 'japanese');


-- create the users and grant priveleges to those users
GRANT SELECT, INSERT, DELETE, UPDATE
ON jellies_DATABASE.*
TO mgs_user@localhost
IDENTIFIED BY 'pa55word';

GRANT SELECT
ON users
TO mgs_tester@localhost
IDENTIFIED BY 'pa55word';

