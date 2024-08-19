import os
import mysql.connector
from itemadapter import ItemAdapter


class TopCVPipeline:
    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
            host=os.getenv("CRAWLER_DATABASE_HOST"),
            user=os.getenv("CRAWLER_DATABASE_USERNAME"),
            password=os.getenv("CRAWLER_DATABASE_PASSWORD"),
            database=os.getenv("CRAWLER_DATABASE_NAME")
        )
        self.cur = self.conn.cursor()

        self.cur.execute("""



CREATE TABLE IF NOT EXISTS jobs (
id INT AUTO_INCREMENT PRIMARY KEY,

job_url VARCHAR(255) NOT NULL,
title VARCHAR(255),

salary_range VARCHAR(255),


min_salary DECIMAL(10,2),
max_salary DECIMAL(10,2),
avg_salary DECIMAL(10,2),




location VARCHAR(255),
region  VARCHAR(255),



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






""")

        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Convert quantity to integer, handle potential conversion issues
        quantity = adapter.get('quantity', '')
        try:
            quantity = int(quantity) if quantity else None
        except ValueError:
            quantity = None

        self.cur.execute(
            """
            INSERT INTO jobs(
                job_url, 
                title,

                salary_range,
                location,
                
                description,
                requirements,
                benefit,
                
                company_url,
                company_name,
                company_avatar,
                company_scale,
                company_address,
                
                
                position,
                experience,
                
                quantity,
                
                type,
                gender,
                
                branch,
                
                

                source
            ) 
            VALUES (
                %s, 
                %s,

                %s,
                %s,

                %s,
                %s,
                %s,

                %s,
                %s,
                %s,
                %s,
                %s,

                %s,

                %s,
                %s,

                %s,

                %s,

                

                %s,
                %s
            )
            """,
            (
                adapter.get('job_url', ''),
                adapter.get('title', ''),

                adapter.get('salary_range', ''),
                adapter.get('location', ''),

                adapter.get('description', ''),
                adapter.get('requirements', ''),
                adapter.get('benefit', ''),

                adapter.get('company_url', ''),
                adapter.get('company_name', ''),
                adapter.get('company_avatar', ''),
                adapter.get('company_scale', ''),
                adapter.get('company_address', ''),

                adapter.get('position', ''),
                adapter.get('experience', ''),

                quantity,

                adapter.get('type', ''),
                adapter.get('gender', ''),

                adapter.get('branch', ''),


                adapter.get('source', '')
            )
        )

        self.conn.commit()

        return item
