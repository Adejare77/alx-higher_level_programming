-- creates the table "force_name" on local server
-- "force_name" description:
-- id INT, name VARCHAR(256) can't be null
-- The database will be passed as an argument. If "force_name" exist,
-- your script shouldn't fail
CREATE TABLE IF NOT EXISTS force_name (id INT,
name VARCHAR(256) NOT NULL)
