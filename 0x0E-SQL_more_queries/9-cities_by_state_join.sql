-- lists all cities contained in the database hbtn_0d_usa
-- cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
SELECT cities.id, cities.name,(SELECT name FROM states WHERE states.id = state_id) as name FROM cities
ORDER BY cities.id;
