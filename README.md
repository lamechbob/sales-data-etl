# 🧾 sales-data-etl

**`sales-data-etl`** is a lightweight Python project that reads sales data from a CSV file, loads it into a SQLite database, and runs basic analytics like total sales and top-selling products. It’s a simple ETL pipeline that demonstrates data ingestion, table creation, and SQL querying with Python.

---

## 📌 Features

- Reads structured sales data from CSV
- Creates and manages a local SQLite database
- Builds a `sales` table with schema definition
- Inserts transaction data row-by-row
- Runs SQL queries to:
  - Calculate total sales per transaction
  - Identify the highest single sale
  - Display top 3 transactions by quantity sold
- Modular project structure (`main.py` + `etl/transform.py`)
- Git-tracked with clean `.gitignore` and `requirements.txt`

---

## 🛠️ Technologies Used

- Python 3.x
- SQLite3
- Pandas

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sales-data-etl.git
cd sales-data-etl
