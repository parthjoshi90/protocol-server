SELECT 'CREATE DATABASE ondc_connect_devdb'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'ondc_connect_devdb')\gexec
\connect ondc_connect_devdb;
CREATE SCHEMA ondc_connect;


CREATE TABLE IF NOT EXISTS ondc_connect.ondc_request (
    id SERIAL PRIMARY KEY,
    action VARCHAR(255),
    domain VARCHAR(255),
    message_id VARCHAR(50),
    request JSON,
    created_at TIMESTAMP
);
