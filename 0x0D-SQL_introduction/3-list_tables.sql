-- List tables
SET @dbname = '$1';
SELECT table_name
FROM information_schema.tables
WHERE table_schema = @dbname
