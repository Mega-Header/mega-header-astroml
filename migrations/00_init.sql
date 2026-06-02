-- AstroML Database Initialization Script
-- This script runs on PostgreSQL startup to create initial tables and extensions

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
CREATE EXTENSION IF NOT EXISTS "hstore";

-- Create schema
CREATE SCHEMA IF NOT EXISTS mega-header-astroml;

-- Set search path
SET search_path TO mega-header-astroml, public;

-- Log initialization completion
SELECT now() as "Database initialized at";
