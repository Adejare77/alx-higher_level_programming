-- lists all shows contained in "hbtn_0d_tvshows" without a 'genre linked'
-- Each record should display: tv_shows.title, tv_show_genres.genre_id
-- Results mus be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- you can use only one SELECT statement
-- The DATABASEname will b passed as an argument of the mysql command

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC
