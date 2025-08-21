CREATE TABLE locations(
    id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL DEFAULT '--ERROR--',
    population BIGINT DEFAULT -1,
    country_code CHAR(2) NOT NULL DEFAULT '--');

INSERT INTO locations(id, name, country_code, population) VALUES
    (1, 'Palikir - National Government Center', 'FM', 0),
    (2, 'Burg Unter-Falkenstein', 'DE', 0),
    (3, 'Guam Government House', 'GU', 0),
    (4, 'bishopric of Perugia', 'IT', 0), 
    (5, 'Linton Military Camp', 'NZ', 0), 
    (6, 'Chasse Royale', 'BE', 0),
    (7, 'Haselbachtal', 'DE', 0),
    (8, 'RMI Capitol', 'MH', 0), 
    (9, 'Ngerulmud', 'PW', 0),
    (10, 'Riverlea', 'ZA', 0),
    (11, 'Plymouth', 'MS', 0),
    (12, 'Cambebba', 'BR', 0),
    (13, 'Grytviken', 'GS', 2),
    (14, 'Port-aux-Francais (Port-aux-Français)', 'TF', 45),
    (15, 'Adamstown', 'PN', 46),
    (16, 'West Island', 'CC', 120),
    (17, 'Flying Fish Cove', 'CX', 500),
    (18, 'Alofi', 'NU', 624),
    (19, 'Jamestown', 'SH', 637),
    (20, 'Vatican City', 'VA', 829),
    (21, 'Kingston', 'NF', 880),
    (22, 'Amato', 'IT', 895),
    (23, 'Hamilton', 'BM', 902),
    (24, 'Brades', 'MS', 1000),
    (25, 'Hagatna (Hagåtña)', 'GU', 1051),
    (26, 'Yaren', 'NR', 1100),
    (27, 'Mata-Utu', 'WF', 1200),
    (28, 'Philipsburg', 'SX', 1400),
    (29, 'The Valley', 'AI', 2035), 
    (30, 'Longyearbyen', 'SJ', 2060),
    (31, 'Stanley', 'FK', 2213),
    (32, 'Iron River', 'US', 2904),
    (33, 'Kralendijk', 'BQ', 3081),
    (34, 'Cockburn Town', 'TC', 3720),
    (35, 'Funafuti', 'TV', 4492),
    (36, 'San Marino', 'SM', 4500),
    (37, 'Lobamba', 'SZ', 4557),
    (38, 'Vaduz', 'LI', 5197),
    (39, 'Marigot', 'MF', 5700),
    (40, 'Gustavia', 'BL', 5988);

-- Ex 7.1
SELECT country_code, population FROM locations
	ORDER BY population DESC;

-- Ex 7.2
SELECT name, AVG(population) AS avg_population FROM locations
	GROUP BY name
	ORDER BY AVG(population);

-- Ex 7.3
SELECT name, population FROM locations
	WHERE population=0 
	LIMIT 5;