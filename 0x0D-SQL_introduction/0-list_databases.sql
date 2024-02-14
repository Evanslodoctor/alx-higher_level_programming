-- 0-list_databases.sql

-- Connect to MySQL server
-- Replace 'your_username' and 'your_password' with your MySQL username and password
-- You may also need to replace 'localhost' with your MySQL server address if it's different
mysql -u your_username -p your_password -h localhost <<EOF

-- Lists all databases
SHOW DATABASES;

-- End of script
EOF
