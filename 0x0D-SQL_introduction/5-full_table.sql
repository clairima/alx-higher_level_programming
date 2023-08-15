-- a script that prints the full description of the table first_table
SELECT column_name, column_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'first_table';

