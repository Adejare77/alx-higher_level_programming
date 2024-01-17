-- Active: 1705509733487@@127.0.0.1@3306@hbtn_0d_tvshows
-- lists all shows contained in the database "hbtn_0d_tvshows"
-- Each record should display: tv_shows.title, tv_shows_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show.genres.genre_id
-- If a show doesn't have a genre, display NULL
-- You can only use one SELECT statement
-- The DATABASE name will be passed as an argument of the mysql command
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC
