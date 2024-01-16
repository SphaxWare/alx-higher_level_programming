-- displays the number of records with id = 89
-- Execute: cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
SELECT COUNT(id) FROM first_table WHERE id=89;
