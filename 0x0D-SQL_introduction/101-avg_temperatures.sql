-- displays the average temperature (Fahrenheit) 
-- by city ordered by temperature (descending)
SELECT city, AVG(*) AS avg_temp FROM temperatures ORDER BY temperature DESC;
