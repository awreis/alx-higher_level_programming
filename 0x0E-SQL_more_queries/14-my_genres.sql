-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- tv_shows table contains only one record where title = Dexter (but the id can be different)
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
-- can use only one SELECT statement
-- the database name will be passed as an argument of the mysql command

SELECT g.`name`
	FROM `tv_genres` AS g
		INNER JOIN `tv_show_genres` AS s
		ON g.`id` = s.`genre_id`
		INNER JOIN `tv_shows` AS t
		ON t.`id` = s.`show_id`
		WHERE t.`title` = "Dexter"
	ORDER BY g.`name`;
