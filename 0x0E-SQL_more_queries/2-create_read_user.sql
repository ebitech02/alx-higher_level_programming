-- Creates a database hbtn_0d_2 and the user user_0d_02
-- User has SELECT privilege

CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_02_pwd';
GRANT SELECT ON `hbtn_0d_02`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES

