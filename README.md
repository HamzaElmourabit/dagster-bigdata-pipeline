# Big Data Pipeline Orchestration with Dagster

## 📖 Overview

This project demonstrates the implementation of an **ETL (Extract–Transform–Load) data pipeline** orchestrated using **Dagster**, a modern and flexible data orchestration framework.

The main objective is to showcase how orchestration tools can be used to **structure, monitor, and manage data workflows** efficiently within a **Big Data ecosystem**, improving reliability, observability, and scalability compared to standalone scripts.

---

## 🏗 Architecture

The pipeline is organized into **three main stages**, following standard ETL architecture principles:

### 🔹 Extract
- Reads structured data from a **CSV file**
- Loads the data into a **Pandas DataFrame**

### 🔹 Transform
- Applies data processing and aggregation
- Example operations:
  - Grouping data
  - Computing statistical metrics (e.g., averages)

### 🔹 Load
- Writes the transformed data into an **output file**
- Prepares the data for **downstream analytics or reporting**

---

## ⚙️ Orchestration with Dagster

Dagster is used to manage and orchestrate the pipeline by providing:

- Execution order control
- Dependency management between steps
- Step-level monitoring and logging
- Interactive pipeline visualization via **Dagster UI**

This demonstrates how orchestration enhances **visibility, reliability, and maintainability** of data pipelines.

---

## 🛠 Technologies Used

- **Python**
- **Pandas**
- **Dagster**
- **ETL Architecture**
- **Data Pipeline Orchestration**

---

## ▶ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install dagster dagster-webserver pandas

