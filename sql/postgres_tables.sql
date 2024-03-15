-- Creation of Tables 

CREATE TABLE sump1_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT,
	turbudity FLOAT,
	ph Float
);

CREATE TABLE sump1_waterlevel (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    distance FLOAT
);

CREATE TABLE motor1_status (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    status FLOAT,
    current FLOAT
);
 
CREATE TABLE oht1_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT,
	turbudity FLOAT,
	ph Float
);

CREATE TABLE oht1_waterlevel (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    distance FLOAT
);

CREATE TABLE roplant1_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE roplant1_tds (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    tds FLOAT
);

CREATE TABLE ro1_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE ro2_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE ro3_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

-- Inserting Random data for the past 1 month 
-- sump1_data
INSERT INTO sump1_data (timestamp, creationtime, temperature, voltage, uncompensated_tds, compensated_tds, turbudity, ph)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (50 - 10) + 10,  -- temperature between 10 and 50
    RANDOM() * (40 - 20) + 20, -- voltage between 200 and 400
    RANDOM() * (500 - 100) + 100, -- uncompensated_tds between 100 and 500
    RANDOM() * (500 - 100) + 100, -- compensated_tds between 100 and 500
    RANDOM() * (20 - 0) + 10,    -- turbudity between 0 and 20
    RANDOM() * (14 - 6) + 6       -- pH between 6 and 14
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);


INSERT INTO oht1_data (timestamp, creationtime, temperature, voltage, uncompensated_tds, compensated_tds, turbudity, ph)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (50 - 10) + 10,  -- temperature between 10 and 50
    RANDOM() * (40 - 20) + 20, -- voltage between 200 and 400
    RANDOM() * (500 - 100) + 100, -- uncompensated_tds between 100 and 500
    RANDOM() * (500 - 100) + 100, -- compensated_tds between 100 and 500
    RANDOM() * (20 - 0) + 10,    -- turbudity between 10 and 20
    RANDOM() * (14 - 6) + 6       -- pH between 6 and 14
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);

INSERT INTO roplant1_data (timestamp, creationtime, temperature, voltage, uncompensated_tds, compensated_tds)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (50 - 10) + 10,  -- temperature between 10 and 50
    RANDOM() * (40 - 20) + 20, -- voltage between 200 and 400
    RANDOM() * (500 - 100) + 100, -- uncompensated_tds between 100 and 500
    RANDOM() * (500 - 100) + 100 -- compensated_tds between 100 and 500
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);

INSERT INTO ro1_data (timestamp, creationtime, temperature, voltage, uncompensated_tds, compensated_tds)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (50 - 10) + 10,  -- temperature between 10 and 50
    RANDOM() * (40 - 20) + 20, -- voltage between 200 and 400
    RANDOM() * (500 - 100) + 100, -- uncompensated_tds between 100 and 500
    RANDOM() * (500 - 100) + 100 -- compensated_tds between 100 and 500
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);

INSERT INTO ro2_data (timestamp, creationtime, temperature, voltage, uncompensated_tds, compensated_tds)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (50 - 10) + 10,  -- temperature between 10 and 50
    RANDOM() * (40 - 20) + 20, -- voltage between 200 and 400
    RANDOM() * (500 - 100) + 100, -- uncompensated_tds between 100 and 500
    RANDOM() * (500 - 100) + 100 -- compensated_tds between 100 and 500
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);

INSERT INTO ro3_data (timestamp, creationtime, temperature, voltage, uncompensated_tds, compensated_tds)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (50 - 10) + 10,  -- temperature between 10 and 50
    RANDOM() * (40 - 20) + 20, -- voltage between 200 and 400
    RANDOM() * (500 - 100) + 100, -- uncompensated_tds between 100 and 500
    RANDOM() * (500 - 100) + 100 -- compensated_tds between 100 and 500
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);

-- sump1_waterlevel
INSERT INTO sump1_waterlevel (timestamp, creationtime, temperature, distance)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (50 - 10) + 10,  -- temperature between 10 and 50
    RANDOM() * (1000 - 100) + 100 -- distance between 100 and 1000
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);

INSERT INTO oht1_waterlevel (timestamp, creationtime, temperature, distance)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (50 - 10) + 10,  -- temperature between 10 and 50
    RANDOM() * (1000 - 100) + 100 -- distance between 100 and 1000
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);

-- motor1_status
INSERT INTO motor1_status (timestamp, creationtime, status, current)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (1 - 0) + 0,     -- status either 0 or 1
    RANDOM() * (20 - 5) + 5      -- current between 5 and 20
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);



INSERT INTO roplant1_tds (timestamp, creationtime, tds)
SELECT 
    gs.timestamp,
    CURRENT_TIMESTAMP,
    RANDOM() * (50 - 10) + 10 -- uncompensated_tds between 10 and 50
FROM 
    GENERATE_SERIES(NOW() - INTERVAL '1 month', NOW(), INTERVAL '1 hour') AS gs(timestamp);
