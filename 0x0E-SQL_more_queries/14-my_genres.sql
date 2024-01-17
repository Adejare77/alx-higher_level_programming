-- use the "hbtn_0d_tvshows" DATABASE to lists all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but id may differ)
-- Each record should display: tv_genres.name
-- Result must be sorted in ASC order by the genre name
-- You can use only one SELECT statement
-- The DATABASE name will be passed as an argument of the mysql command

SELECT name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC
