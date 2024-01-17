-- creates DATABASE "hbtn_0d_usa" and TABLE "cities" on your local server
-- "cities" description:
-- id INT, unique, auto generated, not-null and is PK
-- state_id INT, not-null, FK referencing id of states table
-- if both DATABASE and TABLE does not exist, your script shouldn't fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);

