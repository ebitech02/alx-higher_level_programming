-- Create a database and a table with names hbtn_0d_usa and states

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);

