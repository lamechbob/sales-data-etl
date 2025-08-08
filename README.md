# 📊 Sales ETL – A Serverless AWS Pipeline

## 🧠 Project Goal

This project was built to explore how to implement **cloud-native infrastructure** within an ETL process. 

Up until this point, I had created several ETL pipelines—but only on my local machine. This project represents a leap into cloud architecture by deploying a secure, serverless ETL pipeline that adheres to **enterprise-grade standards** (e.g., private subnets, scoped IAM roles, and S3 triggers).

> **In short:** A CSV of sales data is uploaded to S3, triggering a Lambda function that transforms and inserts the data into a PostgreSQL database hosted in RDS—all inside a private subnet.

---

## 🛠️ Tech Stack

| Tool/Service       | Purpose                                          |
|--------------------|--------------------------------------------------|
| **AWS Lambda**     | Serverless function triggered by S3 upload       |
| **AWS S3**         | Stores CSV files with sales data                 |
| **AWS RDS (PostgreSQL)** | Database to persist sales records          |
| **AWS IAM**        | Scoped role for Lambda S3 access                 |
| **AWS VPC**        | Private subnets, S3 Gateway Endpoints, and route tables |
| **EC2 Bastion Host** | Secure visibility into RDS via port forwarding |
| **Python**         | `boto3`, `pg8000`, `pandas`, `psycopg2`          |
| **DBeaver**        | Local database viewer via SSH tunnel             |

---

## 📁 Folder Structure

```
SalesETL/
├── db/
│   ├── create_database.py        # Create schema in newly launched RDS
│   ├── test_connection.py        # Verifies RDS connection
│   └── upload_s3_app.py          # Uploads CSV to S3 to trigger Lambda
│
├── etl/
│   ├── __init__.py               # Empty (used for Lambda packaging)
│   ├── load.py                   # Handles S3 upload logic
│   └── transform.py              # Creates table and inserts data into RDS
│
├── lambda/
│   ├── lambda_handler.py         # Main Lambda code (runs on trigger)
│   └── test_lambda_handler.py    # Tests Lambda logic locally
│
└── data/
    └── sample_sales.csv          # Example input file
```

---

## 🧪 Sample Data Format

```csv
sale_id,product,quantity,price_per_unit,sale_date
1,Widget A,3,19.99,2025-07-01
2,Widget B,2,24.50,2025-07-01
```

---

## ✅ Features

- ✅ Private subnet for both Lambda and RDS (no public exposure)
- ✅ VPC Endpoint for S3 (no NAT required)
- ✅ Secure IAM roles and scoped permissions
- ✅ Real-time trigger from S3 PUT → Lambda
- ✅ Port-forwarded access to RDS via EC2 Bastion + DBeaver

---

## 🔮 What’s Next?

Week 5 of the bootcamp may build on this project. If so, I’ll extend the functionality for:
- Game stats and player rosters (South Broward App)
- Additional Lambda functions
- Streamlit dashboards or RESTful APIs

---

## 📌 Notes

- DBeaver requires an SSH tunnel through the EC2 instance to reach the private RDS.
- This project is part learning exercise, part portfolio piece.
- All infrastructure was built manually in the AWS Console for practice and deeper understanding.