-- Database setup for Dealership Creative Automation Tool

CREATE DATABASE dealership_automation;

USE dealership_automation;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(100)
);

INSERT INTO users (username, password) VALUES ('admin', 'admin123');