-- creates the MySQL server user user_0d_1
-- creates a new user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- grants privileges
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
