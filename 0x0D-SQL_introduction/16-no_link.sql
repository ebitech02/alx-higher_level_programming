-- List records with name except records without a name

SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL AND `name` IS != ''
ORDER BY `score` DESC;

