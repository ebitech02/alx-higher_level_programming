-- USES A DATABASE TO LIST ALL GENRES

SELECT tv_genre.name
FROM tv_genres tg
JOIN tv_show_genres tsh
ON tv_genre.id = tsh.genre_id
JOIN tv_shows ts
ON ts.id = tsh.show_id
WHERE ts.tile = 'Dexter'
ORDER BY tv_genre.name;

