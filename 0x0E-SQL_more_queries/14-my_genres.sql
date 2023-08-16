-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT s.title, g.genre_id
	FROM tv_shows AS S
		LEFT JOIN tv_show_genres AS g
		ON s.id = g.show_id
		WHERE g.genre_id IS NULL
	ORDER BY s.title, g.genre_id;

