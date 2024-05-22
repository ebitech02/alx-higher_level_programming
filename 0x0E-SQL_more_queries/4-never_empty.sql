-- Creates a table that passes as an argument id_not_null
-- Values are id, name

CREATE TABLE IF NOT EXISTS `id_not_null` (
	`id` INT DEFAULT 1,
	`name` VARCHAR(256)
);

