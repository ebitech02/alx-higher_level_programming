-- Lists all cities contained in the datbase hbtn_0d_usa

SELECT cities.id, cities.name, states.name
FROM `cities`
JOIN `states` ON cities.state_id = states_id
ORDER BY cities.id

