-- creates the table "id_not_null" on local server
-- "id_not_null" description:
-- id INT with the default value 1, name VARCHAR(256)
-- The DATABASE name will be passed as an argument in the mysql command
-- if the TABLE "id_not_null" already exists, your script shouldn't fail

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1,
name VARCHAR(256));
