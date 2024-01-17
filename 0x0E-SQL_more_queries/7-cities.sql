-- creates the database hbtn_0d_usa and the table cities
-- cat 7-cities.sql | mysql -hlocalhost -uroot -p
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT FOREIGN KEY references states(id),
	name VARCHAR(256) NOT NULL
);
