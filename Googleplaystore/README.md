# Google Play Store Data Engineering Project

## Project Overview

In this data engineering project, I have worked on a comprehensive analysis of the Google Play Store dataset. The goal was to transform raw data into a structured and optimized format for downstream analysis and insights. The project covered data loading, cleaning, and transformation tasks, ensuring that the dataset is ready for various data analysis, machine learning, or reporting tasks.

## Project Structure

- **Flask_API.py**: The main file containing the Flask API for interacting with the processed data.
- **process_data.py**: The Python script for processing and cleaning the Google Play Store dataset using PySpark.
- **PySpark_ML_GooglePlayStore.ipynb**: Jupyter Notebook with code for data loading, exploration, cleaning and machine learning features.

## Flask API

The Flask API provides endpoints for querying the processed Google Play Store data. Here are some example API endpoints:

- `/`: Welcome message.
- `/get_all_data`: Get all the processed data.
- `/filter_one_column`: Filter data based on a specific column value.
- `/get_data`: Get data based on specific conditions.
- `/get_data_tabular`: Get data in tabular format.
- `/sort_data`: Allows sorting the data based on a column and order.
- `/describe_data`: Descriptive statistics of numerical columns.

## PySpark Data Processing

The `process_data.py` script handles the PySpark data processing tasks. It includes loading the data, cleaning columns, transforming data types, handling null values, creating new columns and performing exploratory data analysis.

## Configuration

The project uses configuration files to manage various settings. Here's an overview of the configuration files:

### `config.ini`

The `config.ini` file contains configuration settings for the Flask application and data processing tasks.

## config.py

The `config.py` Python module is responsible for reading and providing access to the configuration settings in config.ini

## Jupyter Notebook

The `PySpark_ML_GooglePlayStore.ipynb` notebook provides a step-by-step walkthrough of the data engineering project. It covers data loading, cleaning, exploratory data analysis, data visualisation and machine learning feature preparation.

Numerous features of the PySpark library were leveraged during the project, including:

- **StringIndexer and OneHotEncoder:** For handling categorical variables.
- **VectorAssembler:** For assembling feature vectors.
- **LinearRegression:** Utilized for machine learning tasks.

## Dependencies

- Python 3.10
- Flask
- PySpark
- Matplotlib
- Seaborn
- Requests
- Jsonify
- Threading
- Java JDK v17 or v11 or v8

## Author

- Charilaos A Savoullis

## Usage

Feel free to explore the provided API endpoints and Jupyter Notebook for insights into the Google Play Store dataset and reach out with any questions or feedback!
