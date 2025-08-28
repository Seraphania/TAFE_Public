CREATE DATABASE IF NOT EXISTS Valuables;
USE Valuables;

CREATE TABLE IF NOT EXISTS Rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    room_name VARCHAR(255)
);

    CREATE TABLE IF NOT EXISTS Items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    room_id INT NOT NULL,
    item_description VARCHAR(255),
    item_type VARCHAR(255) DEFAULT 'Appliance',
    `value` DECIMAL NOT NULL,
    FOREIGN KEY (room_id) REFERENCES Rooms(id) 
);