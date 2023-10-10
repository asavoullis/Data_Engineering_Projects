# Data Engineering Projects Repository

This repository contains distinct data engineering projects, each focusing on different aspects of data analysis, processing, and insights. Below is an overview of each project:

- [Googleplaystore ](https://github.com/asavoullis/Data_Engineering_Projects/tree/main/Googleplaystore "Googleplaystore ")
- [Forex_EURUSD](https://github.com/asavoullis/Data_Engineering_Projects/tree/main/Forex_EURUSD "Forex_EURUSD")
- [Trending_Youtube_Videos](https://github.com/asavoullis/Data_Engineering_Projects/tree/main/Trending_Youtube_Videos "Trending_Youtube_Videos")

---

## 1. Google Play Store Data Engineering Project

### Project Overview

In this comprehensive data engineering project, the goal is to conduct a thorough analysis of the Google Play Store dataset. The primary objective is to transform raw data into a structured and optimized format suitable for downstream analysis and insights. The project encompasses crucial data engineering tasks, including data loading, cleaning, and transformation, ensuring the dataset is prepared for various data analysis or reporting endeavors.

### Project Structure

- **Flask_API.py**: The main file containing the Flask API for interacting with the processed data.
- **process_data.py**: Python script for processing and cleaning the Google Play Store dataset using PySpark.
- **GooglePlayStore_Analysis.ipynb**: Jupyter Notebook with a step-by-step walkthrough of the data engineering project.
- **templates.py**: Module containing templates for the Flask application.

### Flask API

The Flask API provides endpoints for querying the processed Google Play Store data. Example API endpoints include `/get_all_data`, `/filter_one_column`, `/get_data`, `/get_data_tabular`, `/sort_data`, and `/describe_data`.

### PySpark Data Processing

The `process_data.py` script handles PySpark data processing tasks, including loading data, cleaning columns, transforming data types, handling null values, creating new columns, and performing exploratory data analysis.

### Unit Testing

A unit testing file (`test_app.py`) is included to ensure the correctness of the Flask API and data processing functionality.

To run the unit tests:

```bash
python test_app.py
```

---

## 2. Forex EUR/USD Data Engineering Project

### Project Overview

In this data engineering project, the focus is on the analysis and preparation of financial EUR/USD forex data. The project involves tasks such as data loading, cleaning, transformation, and analysis to ensure the dataset is ready for various data analysis, machine learning, or reporting tasks.

### Project Structure

- **eurusd_hour_analysis.ipynb**: Jupyter Notebook with a step-by-step walkthrough of the data engineering project.
- **README.md**: Documentation providing an overview of the project, its structure, and instructions for usage.
- **DataSet**: Directory containing the raw CSV data file (`eurousd.csv`).

### Data Exploration and Analysis

The project provides insights into the EUR/USD forex financial dataset, explaining the significance of each column and addressing anomalies in the data.

---

## 3. YouTube Ad Campaign Data Engineering Project

### Project Overview

This project aims to execute an end-to-end data engineering process, from data acquisition to building a final dashboard using AWS cloud architecture. The objective is to assist a client or company in understanding how to categorize YouTube videos based on comments and stylistic factors and identify the factors that affect a video's popularity. This information will help the client make informed decisions before investing in a YouTube ad campaign.

### Project Goals and Success Criteria

1. Collect data from multiple sources.
2. Design and implement an ETL (Extract, Transform, Load) pipeline.
3. Build a scalable data lake using Amazon S3.
4. Utilize AWS cloud services for data processing.
5. Create a dashboard for data visualization and analysis.

### Services Used

- Amazon S3
- AWS IAM
- Amazon QuickSight
- AWS Glue
- AWS Lambda
- AWS Athena

### Dataset Used

This Kaggle dataset contains statistics on daily popular YouTube videos, including video title, channel title, publication time, tags, views, likes, dislikes, description, and comment count.

### Architecture Diagram

![Architecture Diagram](https://github.com/asavoullis/Data_Engineering_Projects/blob/main/Trending_Youtube_Videos/architecture.jpeg)

---

# Author

**Charilaos A Savoullis**
