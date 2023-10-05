--recipe directory sql
-- recipe_directory
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    cook_time INT,
    rating INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (title, cook_time, rating) VALUES ('Cola Ham', 120, 5);
INSERT INTO recipes (title, cook_time, rating) VALUES ('BimBimBap', 20, 4);
INSERT INTO recipes (title, cook_time, rating) VALUES ('Omelette', 5, 2);
INSERT INTO recipes (title, cook_time, rating) VALUES ('Boiled Egg', 5, 1);
INSERT INTO recipes (title, cook_time, rating) VALUES ('Cheese Toasty',4, 3);
