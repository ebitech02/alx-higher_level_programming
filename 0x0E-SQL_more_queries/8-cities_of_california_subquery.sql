-- Lists all the cities that can be found in a database hbtn_0d_usa

SELECT `id`, `name`
FROM `cities`
WHERE `state_id` = (
	SELECT `id`
	FROM `states`
	WHERE `name` = 'California'
)
ORDER BY `id`;

