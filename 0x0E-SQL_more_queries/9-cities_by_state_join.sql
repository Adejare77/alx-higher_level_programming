-- list all cities contained in the DATABASE "hbtn_0d_usa"
-- Each record should display: cities.id, cities.name, states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
-- The DATABASE name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
