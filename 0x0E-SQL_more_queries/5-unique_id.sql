-- Creates a table with the name unique_id
-- Unique default id

CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);

