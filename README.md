# Sim Racing Analytics Pipeline

## Overview

This project processes and analyzes personal iRacing race data using a Python-based ETL and analytics pipeline.

The goal of the project is to simulate a realistic data workflow by ingesting raw JSON exports, transforming nested race session data into structured analytical datasets, storing results in SQLite, and generating insights through SQL queries and future dashboard visualizations.

The project focuses on data engineering fundamentals, analytical querying, and pipeline organization while using real-world motorsport telemetry and race session data.


## Tech Stack

- Python
- pandas
- SQLite
- SQL
- JSON / CSV data processing
- Power BI (planned)


## Pipeline Architecture

Raw JSON Export  
→ Python Ingestion & Cleaning Scripts  
→ Structured Analytical CSVs  
→ SQLite Database  
→ SQL Analytics Queries  
→ Power BI Dashboard (planned)


## Features

- Nested JSON ingestion and transformation
- Incremental SQLite loading
- Duplicate prevention using `subsession_id`
- Modular SQL analytics queries
- Track normalization (`track_name`, `track_config`, `track_id`)
- Repeatable ETL workflow structure
- Organized raw vs processed data layers


## Example Analysis Areas

### Incident Analysis
Analyze how incident counts correlate with race finishing position and overall consistency.

### Track Performance
Compare average finishing position and incident rates across tracks and configurations.

### Strength of Field Analysis
Evaluate performance trends across different competition levels (SOF).

### Trend Analysis
Track race consistency and performance changes over time.


## Key Skills Demonstrated

- Data cleaning and transformation
- Working with nested JSON structures
- Building repeatable ETL pipelines
- Relational database loading and querying
- SQL aggregation and analytical querying
- Pipeline organization and workflow management


## Future Improvements

- Power BI dashboard integration
- Expanded trend analysis visualizations
- Automated ingestion workflows
- Additional racecraft and telemetry metrics
- Advanced SQL reporting queries


## Project Structure

```text
sim_racing_data_project/
├── config/
├── data/
│   ├── processed/
│   └── raw/
│       ├── archive/
│       └── incoming/
├── database/
│   └── sim_racing.db
├── docs/
├── powerbi/
├── scripts/
│   ├── analysis/
│   ├── database/
│   ├── ingestion/
│   └── processing/
├── sql/
├── .gitignore
└── README.md
```