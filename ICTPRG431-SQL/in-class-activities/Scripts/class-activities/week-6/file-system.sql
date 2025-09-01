CREATE DATABASE IF NOT EXISTS FileSystem;
USE FileSystem;

DROP TABLE IF EXISTS folders;
CREATE TABLE IF NOT EXISTS folders (
    `name` VARCHAR (255) NOT NULL PRIMARY KEY,
    last_accessed TIMESTAMP,
    last_modified TIMESTAMP,
    created_date TIMESTAMP
);

DROP TABLE IF EXISTS files;
CREATE TABLE IF NOT EXISTS files (
    folder_name BIGINT NOT NULL PRIMARY KEY,
    `name` VARCHAR (255) NOT NULL,
    last_accessed TIMESTAMP,
    last_modified TIMESTAMP,
    created_date TIMESTAMP,
    file_size BIGINT,
    FOREIGN KEY(folder_name) REFERENCES folders(name)
);

INSERT INTO folders (name, last_accessed, last_modified, created_date)
VALUES
    ('resources', NOW(), NOW(), NOW()),
    ('activities', NOW(), NOW(), NOW())
;

INSERT INTO folders (file_size, folder_name, name, last_accessed, last_modified, created_date)
VALUES
    (4, 'activities', 'class-activities.md',  NOW(), NOW(), NOW())
    (24, 'activities', 'Exercise - Joining Tables.pdf', NOW(), NOW(), NOW())
    (8, '.', 'notes.md',  NOW(), NOW(), NOW())
    (104, 'resources', 'Class-Notes-SQL-Joins.pdf',  NOW(), NOW(), NOW())
    (156, 'resources', 'joins.png',  NOW(), NOW(), NOW())
    (2020, 'resources', 'Session-6-join-union-all-nested-queries.pptx',  NOW(), NOW(), NOW())
;

-- Display all the names of all the files in a given folder.
SELECT `name` from files
    INNER JOIN folders
    WHERE folders.name = files.folder_name

-- Display all the names of all the files in a given folder ordered by creation date.


-- Display the folder name and file names for files in a given folder.


-- Display the folder name and file names for files in a given folder if they haven’t been accessed this year.


-- Display all folders and what files they contain, even if they contain none.


-- Display all folders and what files they contain, even if they contain none. Sort by file size.


-- Display all the files and what folders they are in.


-- Display all the files and what folders they are in. Sort alphabetically by folder name and then file size.