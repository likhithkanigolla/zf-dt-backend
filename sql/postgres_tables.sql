-- Creation of Tables 
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
CREATE TABLE IF NOT EXISTS "WM-WD-KH04-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE IF NOT EXISTS "WM-WD-KH03-00" (
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
