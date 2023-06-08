DROP TABLE IF EXISTS author;
DROP TABLE IF EXISTS book;

CREATE TABLE book (
id SERIAL PRIMARY KEY,
title_first_name VARCHAR(255),
title_last_name VARCHAR(255)
);

CREATE TABLE author (       
id SERIAL PRIMARY KEY,
description VARCHAR(255),
duration INT,
completed BOOLEAN,
book_id INT NOT NULL REFERENCES books(id)
);