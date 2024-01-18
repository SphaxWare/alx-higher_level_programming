-- lists all cities contained in the database hbtn_0d_usa
-- cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities JOIN states WHERE states.id = cities.state_id
ORDER BY cities.id;
