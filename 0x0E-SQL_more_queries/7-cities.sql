-- Create a database and a table with names hbtn_0d_usa and cities

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS cites (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);

