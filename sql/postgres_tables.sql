-- Creation of Tables 

CREATE TABLE sump1_wd_data (
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

CREATE TABLE oht_krbadm_wf_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    flowrate FLOAT,
    totalflow FLOAT
);
 
CREATE TABLE oht1_wd_data (
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

CREATE TABLE oht_rop1_wd_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT,
	turbudity FLOAT,
	ph Float
);

CREATE TABLE roplant1_wd_data (
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

CREATE TABLE ro1_wd_data (
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	creationtime TIMESTAMP WITH TIME ZONE,
    temperature FLOAT,
    voltage FLOAT,
    uncompensated_tds FLOAT,
    compensated_tds FLOAT
);

CREATE TABLE ro2_wd_data (
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
