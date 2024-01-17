-- creates the TABLE "unique_id" on local server
-- "unique_id" description:
-- id INT, VARCHAR(256)
-- The DATABASE name will be passed as an argument of the mysql command
-- if the TABLE "unique_id" already exists, your script shouldn't fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
