-- this is comment 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
--this is using for use db 
USE hbtn_0d_usa;
--table creating
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
    name VARCHAR(256) NOT NULL
);
