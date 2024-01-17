-- lists all the cities of California that can be found in the DATABASE "hbtn_0d_usa"
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
-- The DATABASE name will be passed as an argument of the mysql command
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE states.name = 'California'
)
ORDER BY cities.name ASC;
