-- Creation of Tables 
-- Authenticaltion Users Table 
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(2550) NOT NULL
);

-- Alarm and Notification Tables

CREATE TABLE IF NOT EXISTS notifications (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    node_id VARCHAR(255),
    notification_type VARCHAR(255),
    notification_value TEXT,
    read_status BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS alarms (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    node_id VARCHAR(255) NOT NULL,
    alarm_type VARCHAR(255) NOT NULL,
    alarm_value TEXT,
    alarm_status BOOLEAN DEFAULT TRUE,
    resolved_remarks TEXT
);


--Added IF Not Exists to avoid errors when creating tables that already exist
-- Motor Node SQL Statements
CREATE TABLE IF NOT EXISTS "DM-KH98-60" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    status FLOAT,
    voltage FLOAT,
    current FLOAT,
    power FLOAT,
    energy FLOAT,
    frequency FLOAT,
    power_factor FLOAT
);

-- Status and Actuation
CREATE TABLE IF NOT EXISTS "DM-KH98-80" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    node_type VARCHAR,
    status VARCHAR
);

CREATE TABLE IF NOT EXISTS "DM-KH95-80" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    node_type VARCHAR,
    status VARCHAR
);

CREATE TABLE IF NOT EXISTS "DM-KH96-80" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    node_type VARCHAR,
    status VARCHAR
);

CREATE TABLE IF NOT EXISTS "DM-KH03-80" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    node_type VARCHAR,
    status VARCHAR
);



-- Water Flow Node SQL Statements
CREATE TABLE IF NOT EXISTS "WM-WF-KB04-70" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WF-KB04-71" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WF-KB04-72" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WF-KB04-73" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);

-- Water Level Nodes 
CREATE TABLE IF NOT EXISTS "WM-WL-KH00-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    waterlevel FLOAT,
    temperature FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WL-KH98-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    waterlevel FLOAT,
    temperature FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WF-KH98-40" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);
CREATE TABLE IF NOT EXISTS "WM-WF-KH95-40" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);


-- Water Quality / Water Distribution
-- Nodes with pH and turbidity
CREATE TABLE IF NOT EXISTS "WM-WD-KH98-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT,
    turbidity FLOAT,
    ph FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WD-KH96-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT,
    turbidity FLOAT,
    ph FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WD-KH96-01" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT,
    turbidity FLOAT,
    ph FLOAT
);

-- Nodes without pH and turbidity
CREATE TABLE IF NOT EXISTS "WM-WD-KH96-02" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WD-KH04-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WD-KH95-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE IF NOT EXISTS ro3_wd_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE IF NOT EXISTS roplant1_tds (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    tds FLOAT
);

-- Test Setup Tables
CREATE TABLE IF NOT EXISTS "WM-WD-NODE-1" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WD-NODE-2" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WD-NODE-3" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);
