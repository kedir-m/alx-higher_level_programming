-- lists all records of table without name value.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
