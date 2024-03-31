-- Creation of Tables 

CREATE TABLE "WM-WD-KH98-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT,
	turbudity FLOAT,
	ph Float
);

CREATE TABLE "WM-WL-KH98-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    waterlevel FLOAT,
    temperature FLOAT
);

CREATE TABLE "WM-WD-KRB-M1" (
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

CREATE TABLE "WM-WF-KB04-70" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);

CREATE TABLE "WM-WF-KB04-71" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);

CREATE TABLE "WM-WF-KB04-72" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);

CREATE TABLE "WM-WF-KB04-73" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);
 
CREATE TABLE "WM-WD-KH96-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT,
	turbudity FLOAT,
	ph Float
);

CREATE TABLE "WM-WL-KH00-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    waterlevel FLOAT,
    temperature FLOAT
);

CREATE TABLE "WM-WD-KH96-01" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT,
	turbudity FLOAT,
	ph Float
);

CREATE TABLE "WM-WD-KH04-00" (
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

CREATE TABLE "WM-WD-KH01-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE "WM-WD-KH95-00" (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE ro3_wd_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);
