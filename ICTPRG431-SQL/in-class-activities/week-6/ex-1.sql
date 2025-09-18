CREATE DATABASE IF NOT EXISTS filesystem;

USE filesystem;

CREATE TABLE IF NOT EXISTS folders(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name varchar(255),
    last_accessed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL,
    last_changed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL
);

CREATE TABLE IF NOT EXISTS files(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    folder_id BIGINT NOT NULL,
    name varchar(255),
    last_accessed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL,
    last_changed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP() NOT NULL,
    file_size BIGINT,
    FOREIGN KEY(folder_id) REFERENCES folders(id)
);

INSERT INTO folders (name)
VALUES
('./week_5-normalizing-databases'),
('./week_5-normalizing-databases/activities'),
('./week_5-normalizing-databases/resources'),
('./week_6-join-union-nested-queries'),
('./week_6-join-union-nested-queries/activities'),
('./week_6-join-union-nested-queries/resources'),
('./week_7-calculations-and-functions'),
('./week_7-calculations-and-functions/activities'),
('./week_7-calculations-and-functions/resources'),
('./week_8-view-creation-execution-and-deletion'),
('./week_8-view-creation-execution-and-deletion/activities'),
('./week_8-view-creation-execution-and-deletion/resources'),
('./week_9-procedures-and-triggers'),
('./week_9-procedures-and-triggers/activities'),
('./week_9-procedures-and-triggers/resources')
;

INSERT INTO files (name, file_size, folder_id)
VALUES
('class-activities.md', 4, 2),
('Exercise-Normalsing Databases-Part-2.pdf', 28, 2),
('notes.md', 8, 1),
('05-Database-Design-Normalisation.pptx', 1572, 3),
('Class-Notes-Normalising-Databases.pdf', 28, 3),
('class-activities.md', 4, 5),
('Exercise - Joining Tables.pdf', 24, 5),
('notes.md', 8, 4),
('Class-Notes-SQL-Joins.pdf', 104, 6),
('joins.png', 156, 6),
('Session-6-join-union-all-nested-queries.pptx', 2020, 6),
('class-activities.md', 4, 8),
('Exercise-Calculations-in-SQL.pdf', 24, 8),
('notes.md', 8, 7),
('Class-Notes-Calculations.pdf', 36, 9),
('Session-7-calculations-functions.pptx', 480, 9),
('traffic_cop_2.sql', 4, 9),
('class-activities.md', 1, 11),
('notes.md', 4, 10),
('Session8-View-in-SQL.pptx', 772, 12),
('class-activities.md', 1, 14),
('notes.md', 4, 13),
('Session-9-Procedures-and-Triggers-in-SQL.pptx', 1652, 15)
;

-- 1. Display all the names of all the files in a given folder.
-- Subquery
SELECT fi.name FROM files fi
WHERE fi.folder_id IN (
    SELECT id 
    FROM folders fo 
    WHERE fo.name LIKE "%week_6%"
);

-- Join
SELECT fi.name
FROM files fi
LEFT JOIN folders fo
ON fo.id = fi.folder_id 
WHERE fo.name LIKE "%week_6%";

-- 2. Display all the names of all the files in a given folder ordered by creation date.
-- Subquery
SELECT fi.name, fi.created_date 
FROM files fi
WHERE fi.folder_id IN (
    SELECT fo.id 
    FROM folders fo 
    WHERE fo.name LIKE "%week_6%"
)
ORDER BY fi.created_date ASC;

-- Join
SELECT fi.name, fi.created_date 
FROM files fi
LEFT JOIN folders fo
ON fo.id = fi.folder_id 
WHERE fo.name LIKE '%week_6%'
ORDER BY fi.created_date;

--    3. Display the folder name and file names for files in a given folder.
-- Subquery (gross)
SELECT 
    (SELECT fo.name AS Folder_Name
    FROM folders fo
    WHERE fo.id = fi.folder_id AND fo.name LIKE "%week_6%") AS Folder_Name,
    fi.name AS File_Name
FROM files fi
WHERE fi.folder_id IN (
    SELECT fo.id 
    FROM folders fo 
    WHERE fo.name LIKE "%week_6%");

-- Join
SELECT  fo.name AS Folder_Name, fi.name AS File_Name  
FROM files fi
LEFT JOIN folders fo
ON fo.id = fi.folder_id 
WHERE fo.name LIKE "%week_6%";

--    4. Display the folder name and file names for files in a given folder if they haven’t been accessed this year.
SELECT  fo.name AS Folder_Name, fi.name AS File_Name, fi.last_accessed_date AS Last_Accessed
FROM files fi
LEFT JOIN folders fo
ON fo.id = fi.folder_id 
WHERE fo.name LIKE "%week_6%" AND fi.last_accessed_date < '2025-01-01';

--    5. Display all folders and what files they contain, even if they contain none.
SELECT  fo.name AS Folder_Name, fi.name AS File_Name
FROM files fi
RIGHT JOIN folders fo
ON fo.id = fi.folder_id;

--    6. Display all folders and what files they contain, even if they contain none. Sort by file size.
SELECT  fo.name AS Folder_Name, fi.name AS File_Name, fi.file_size AS File_Size
FROM files fi
RIGHT JOIN folders fo
ON fo.id = fi.folder_id
ORDER BY fi.file_size;

--    7. Display all the files and what folders they are in.
SELECT fi.name AS File_Name, fo.name AS Folder_Name
FROM files fi
LEFT JOIN folders fo
ON fo.id = fi.folder_id;

--    8. Display all the files and what folders they are in. Sort alphabetically by folder name and then file size.

SELECT fi.name AS File_Name, fo.name AS Folder_Name, fi.file_size AS File_Size
FROM files fi
LEFT JOIN folders fo
ON fo.id = fi.folder_id
ORDER BY fo.name, fi.file_size;
