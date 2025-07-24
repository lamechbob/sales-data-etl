# 🧾 sales-etl-lite

**`sales-etl-lite`** is a lightweight Python project that reads sales data from a CSV file, loads it into a SQLite database, and runs basic analytics like total sales and top-selling products. It’s a simple ETL pipeline that demonstrates data ingestion, table creation, and SQL querying with Python.

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

---

## 🛠️ Technologies Used

- Python 3.x
- SQLite3
- Pandas

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sales-etl-lite.git
cd sales-etl-lite
