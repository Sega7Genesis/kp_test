CREATE ROLE program WITH PASSWORD '123456';
CREATE DATABASE equipment_service;
GRANT ALL PRIVILEGES ON DATABASE equipment_service TO program;
CREATE DATABASE monitor_service;
GRANT ALL PRIVILEGES ON DATABASE monitor_service TO program;
CREATE DATABASE documentation_service;
GRANT ALL PRIVILEGES ON DATABASE documentation_service TO program;
CREATE DATABASE session_service;
GRANT ALL PRIVILEGES ON DATABASE session_service TO program;