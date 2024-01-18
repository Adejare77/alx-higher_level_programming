-- lists all genres in the DATABASE "hbtn_0d_tvshows_rate" by their rating
-- Each record should display: tv_genres.name, rating sum
-- Results must be sorted in DESC order by their rating
-- You can use only one SELECT statement
-- The DATABASE name will be passed as an argument of the mysql command

SELECT name, SUM(rate) AS rating
FROM tv_show_ratings
JOIN tv_show_genres ON tv_show_genres.show_id = tv_show_ratings.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY rating DESC
