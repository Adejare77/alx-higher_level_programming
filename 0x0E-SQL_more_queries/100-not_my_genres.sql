-- Active: 1705509733487@@127.0.0.1@3306@hbtn_0d_tvshows
-- uses the "hbtn_0d_tvshows" DATABASE to list all genres `not linked to the show` `Dexter`
-- tv_shows table contains only one record where title = Dexter (but id may differ)
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The DATABASE name will be passed as an argument of the mysql command

WITH my_table AS (
    SELECT id, genre_id AS my_genre_id
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    WHERE title = 'Dexter'
)
SELECT DISTINCT name
FROM tv_show_genres
LEFT JOIN my_table ON my_table.my_genre_id = tv_show_genres.genre_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE my_genre_id IS NULL
ORDER BY name
