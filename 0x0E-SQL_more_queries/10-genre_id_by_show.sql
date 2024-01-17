-- lists all shows contained in "hbtn_0d_tvshows" that have at lease
-- one 'genre linked'.
-- Each record should display: tv_shows.title, tv_show_genres.genre_id
-- Result must be in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can only use one SELECT statement
-- DATABASE name will be passed as argument on mysql command

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC
