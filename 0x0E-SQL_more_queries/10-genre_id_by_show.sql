-- Lists all tv shows in a database hbtn_0d_tvshows that have at least one genres

SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;

