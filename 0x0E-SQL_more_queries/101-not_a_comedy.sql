-- lists all `SHOWS WITHOUT the GENRE Comedy` in the DATABASE "hbtn_0d_tvshows"
-- The tv_genres table contains only one record where name = Comedy (but id may differ)
-- Each record should display: tv_shows.title
-- Results must be sorted in ASC order by the show title
-- You can use a maximum of two SELECT statement
-- The DATABASE name will be passed as an argument of the mysql command
WITH my_table AS (
    SELECT tv_shows.id, tv_shows.title
    FROM tv_genres
    JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_genres.name = 'Comedy'
) -- Gives only movies with genre = 'Comedy' to get their show_id
SELECT tv_shows.title
FROM my_table
RIGHT JOIN tv_shows ON my_table.id = tv_shows.id
WHERE my_table.id IS NULL -- OPPOSITE of tables that contain Comedy
ORDER BY tv_shows.title ASC

