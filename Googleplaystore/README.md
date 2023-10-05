# Google Play Store Data Engineering Project

## Project Overview

In this comprehensive data engineering project, I have conducted a thorough analysis of the Google Play Store dataset. The primary objective was to transform raw data into a structured and optimized format suitable for downstream analysis and insights. The project encompassed crucial data engineering tasks, including data loading, cleaning, and transformation, ensuring the dataset is prepared for various data analysis or reporting endeavors.

## Project Structure

- **Flask_API.py**: The main file containing the Flask API for interacting with the processed data.
- **process_data.py**: The Python script for processing and cleaning the Google Play Store dataset using PySpark.
- **GooglePlayStore_Analysis.ipynb**: Jupyter Notebook with code for explaining the process and thinking behind the data loading, exploration, cleaning, transformation and visualization.
- **config.ini**: Configuration file containing settings for the Flask application and data processing tasks.
- **config.py**: Python module responsible for reading and providing access to configuration settings in config.ini.
- **templates.py**: Module containing templates for the Flask application.

## Flask API

The Flask API provides endpoints for querying the processed Google Play Store data. Here are some example API endpoints:

- `/`: Welcome message (index page).
- `/get_all_data`: Get all the processed data.
- `/filter_one_column`: Filter data based on a specific column value.
- `/get_data`: Get data based on specific conditions.
- `/get_data_tabular`: Get data on specific conditions in tabular format.
- `/sort_data`: Allows sorting the data based on a column and order.
- `/describe_data`: Display descriptive statistics of columns.

## PySpark Data Processing

The `process_data.py` script handles the PySpark data processing tasks. It includes loading the data, cleaning columns, transforming data types, handling null values, creating new columns and performing exploratory data analysis.

## Configuration

The project uses configuration files to manage various settings. Here's an overview of the configuration files:

### `config.ini`

The `config.ini` file contains configuration settings for the Flask application and data processing tasks. It includes parameters such as host, port, and debug mode for the Flask application, as well as any other relevant configurations for PySpark.

## config.py

The `config.py` Python module is responsible for reading and providing access to the configuration settings in config.ini

## Jupyter Notebook

The `GooglePlayStore_Analysis.ipynb` notebook provides a step-by-step walkthrough of the data engineering project. It covers data loading, cleaning, exploratory data analysis and data visualisation features.

## Dependencies

- python_version 3.9.7
- pyspark 3.4.1
- Flask 2.3.2
- requests 2.31.0
- matplotlib 3.7.2
- matplotlib-inline 0.1.3
- seaborn 0.12.2
- pandas 2.0.3
- pandas-profiling 3.6.6
- numpy 1.25.2
- jupyter_client 8.3.0
- jupyter_core 5.3.1
- Java JDK v17 or v11 or v8

## Author

- Charilaos A Savoullis

## Usage

Feel free to explore the provided API endpoints and Jupyter Notebook for insights into the Google Play Store dataset. Don't hesitate to reach out with any questions or feedback! To install the necessary dependencies, run:

```
pip install -r requirements.txt
```
