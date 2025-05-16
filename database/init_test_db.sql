-- PostgreSQL IT projects schema v1

-- Drop tables if they exist to avoid conflicts
DROP TABLE IF EXISTS project_technologies;
DROP TABLE IF EXISTS technologies;
DROP TABLE IF EXISTS projects;

-- Table: projects
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    client_name VARCHAR(100),
    start_date DATE,
    end_date DATE,
    status VARCHAR(30) CHECK (status IN ('Planned', 'Ongoing', 'Completed', 'On Hold'))
);

-- Table: technologies
CREATE TABLE technologies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Association table: many-to-many between projects and technologies
CREATE TABLE project_technologies (
    project_id INT REFERENCES projects(id) ON DELETE CASCADE,
    technology_id INT REFERENCES technologies(id) ON DELETE CASCADE,
    PRIMARY KEY (project_id, technology_id)
);

-- Insert test data into technologies
INSERT INTO technologies (name) VALUES 
    ('Python'),
    ('JavaScript'),
    ('React'),
    ('Node.js'),
    ('Django'),
    ('PostgreSQL'),
    ('AWS'),
    ('Docker'),
    ('Kubernetes');

-- Insert test data into projects
INSERT INTO projects (name, client_name, start_date, end_date, status) VALUES
    ('E-commerce Backend', 'Acme Corp', '2023-01-15', '2023-06-30', 'Completed'),
    ('Mobile Banking App', 'FinTech Ltd', '2024-03-01', NULL, 'Ongoing'),
    ('Cloud Migration', 'DataSecure Inc', '2024-05-10', NULL, 'Planned'),
    ('Internal CRM Tool', 'InHouse', '2022-08-01', '2023-02-28', 'Completed');

-- Associate technologies with projects
INSERT INTO project_technologies (project_id, technology_id) VALUES
    (1, 1), -- Python
    (1, 5), -- Django
    (1, 6), -- PostgreSQL
    (2, 2), -- JavaScript
    (2, 3), -- React
    (2, 4), -- Node.js
    (2, 6), -- PostgreSQL
    (2, 7), -- AWS
    (3, 7), -- AWS
    (3, 8), -- Docker
    (3, 9), -- Kubernetes
    (4, 1), -- Python
    (4, 6); -- PostgreSQL
