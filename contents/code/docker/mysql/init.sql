CREATE DATABASE IF NOT EXISTS crawler;

USE crawler;

CREATE TABLE IF NOT EXISTS jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_url VARCHAR(255) NOT NULL,
    title VARCHAR(255),
    salary_range VARCHAR(255),
    min_salary DECIMAL(10,2),
    max_salary DECIMAL(10,2),
    avg_salary DECIMAL(10,2),
    location VARCHAR(255),
    region VARCHAR(255),
    description TEXT,
    requirements TEXT,
    benefit TEXT,
    company_url VARCHAR(255),
    company_name VARCHAR(255),
    company_avatar VARCHAR(255),
    company_scale VARCHAR(255),
    company_address VARCHAR(255),
    position VARCHAR(255),
    experience VARCHAR(255),
    quantity INT,
    type VARCHAR(255),
    gender VARCHAR(255),
    branch TEXT,
    crawl_data_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    source VARCHAR(255),
    UNIQUE (job_url)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
