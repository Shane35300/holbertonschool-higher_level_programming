-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE NOT EXISTS (
	SELECT 1
	FROM tv_show_genres
	JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_genres.id = tv_show_genres.genre_id
	AND tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
