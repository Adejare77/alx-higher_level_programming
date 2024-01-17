-- lists all genres from "hbtn_0d_tvshows" and displays the `number of shows`
-- linked to each
-- Each record should display: <TV Show genre>, <Number of shows linked to this genre>
-- First column must be called genre, while second column must be
-- called number_of_shows
-- Don't display a genre that doesn't have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The DATABASE name will be passed as an argument of the mysql command

SELECT tv_genres.name AS genre, count(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
