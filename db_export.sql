-- Esempi utilizzati nell'elaborato per l'esame di maturità 2020
--	   Copyright (C) 2020  Michele Viotto
create schema if not exists tesina collate utf8mb4_0900_ai_ci;

create table if not exists posts
(
	id int auto_increment
		primary key,
	author varchar(255) not null,
	body varchar(255) not null
);

create table if not exists users
(
	user_id int auto_increment
		primary key,
	username varchar(255) not null,
	password varchar(255) not null,
	constraint username
		unique (username)
);


INSERT INTO tesina.users (user_id, username, password) VALUES (1, 'admin', 'abc123!');
INSERT INTO tesina.users (user_id, username, password) VALUES (2, 'marco', 'password');
INSERT INTO tesina.users (user_id, username, password) VALUES (3, 'giovanni', 'giovanni123');

INSERT INTO tesina.posts (id, author, body) VALUES (1, 'Michele', 'Questo blog è così bello');
INSERT INTO tesina.posts (id, author, body) VALUES (10, 'Gatto', 'Gattini!!<script>alert("persistent script")</script>');
INSERT INTO tesina.posts (id, author, body) VALUES (11, 'asd', 'Gattini!!&lt;script&gt;alert(&quot;persistent script&quot;)&lt;/script&gt;');
