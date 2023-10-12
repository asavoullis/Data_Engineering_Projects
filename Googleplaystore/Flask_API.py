from flask import Flask, request, jsonify
from pyspark.sql.functions import col
import requests
import threading
from flask import render_template_string

# importing functions and configurations from files I created
from process_data import DataProcessor
from templates import WELCOME_TEMPLATE, DOCUMENTATION_TEMPLATE
from config import Config



class DataAPI:
    def __init__(self, config):
        self.app = Flask(__name__)
        self.config = config
        self.processor = DataProcessor(config)
        self.processed_df = self.processor.process_data()

        # Set up routes
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/get_all_data', 'get_all_data', self.get_all_data, methods=['GET'])
        self.app.add_url_rule('/filter_one_column', 'filter_one_column', self.filter_one_column, methods=['GET'])
        self.app.add_url_rule('/get_data', 'get_data', self.get_data, methods=['GET'])
        self.app.add_url_rule('/get_data_tabular', 'get_data_tabular', self.get_data_tabular, methods=['GET'])
        self.app.add_url_rule('/sort_data', 'sort_data', self.sort_data, methods=['GET'])
        self.app.add_url_rule('/summary_statistics', 'summary_statistics', self.summary_statistics, methods=['GET'])
        self.app.add_url_rule('/documentation', 'documentation', self.documentation)

    def index(self):
        """ The index function serves as the welcome endpoint for the Google Play Store Data API. """
        return render_template_string(WELCOME_TEMPLATE)
    
    def documentation(self):
        """ Displays documentation on how to use the Google Play Store Data API. """
        return render_template_string(DOCUMENTATION_TEMPLATE)
    
    def filter_one_column(self):
        """
        Allows filtering of 1 column
        http://localhost:5000/filter_one_column?column_name=App&column_value=Infinite%20Painter
        """
        try:
            # Get query parameters from the request
            column_name = request.args.get("column_name")
            column_value = request.args.get("column_value")

            # If 1 of the parameters is missing return 400
            if not column_name or not column_value:
                return jsonify({"error": "Both 'column_name' and 'column_value' query parameters are required."}), 400

            # Pulling data from filter
            filtered_data = self.processed_df.filter(col(column_name) == column_value)

            data_json = filtered_data.toJSON().collect()

            return jsonify({"data": data_json})

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def get_data(self):
        """
        Allows you to filter multiple columns and retrieve data in json format.
        http://localhost:5000/get_data?column1=value1&column2=value2&column3=value3...
        http://localhost:5000/get_data?Rating=4.1&Category=ART_AND_DESIGN
        """
        try:
            # Get query parameters from the request
            filters = request.args.to_dict()

            # Check if any filters are provided
            if not filters:
                return jsonify({"error": "No filter criteria provided."}), 400

            # Initialize a base DataFrame with all the data
            filtered_data = self.processed_df

            # Apply filters dynamically based on user-provided criteria
            for column, value in filters.items():
                filtered_data = filtered_data.filter(col(column) == value)

            data_json = filtered_data.toJSON().collect()

            return jsonify({"data": data_json})

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def get_data_tabular(self):
        """
        Allows you to filter multiple columns and retrieve data in a tabular format where each result appears in a different dictionary.
        http://localhost:5000/get_data_tabular?column1=value1&column2=value2&column3=value3...
        http://localhost:5000/get_data_tabular?Rating=4.1&Category=ART_AND_DESIGN
        """
        try:
            # Get query parameters from the request
            filters = request.args.to_dict()

            # Check if any filters are provided
            if not filters:
                return jsonify({"error": "No filter criteria provided."}), 400

            # Initialize a base DataFrame with all the data
            filtered_data = self.processed_df

            # Apply filters dynamically based on user-provided criteria
            for column, value in filters.items():
                filtered_data = filtered_data.filter(col(column) == value)

            # Display the data in a tabular format where each result appears in a different column
            # Convert the filtered data to a list of dictionaries
            data_dict_list = []
            for row in filtered_data.collect():
                data_dict_list.append(row.asDict())

            # Return the list of dictionaries as JSON
            return jsonify({"data": data_dict_list})

        except Exception as e:
            return jsonify({"error": str(e)}), 400    
    
    def sort_data(self):
        """
        Allows sorting the data based on a column and order.
        http://localhost:5000/sort_data?sort_column=Rating&sort_order=asc
        """
        try:
            # Get query parameters from the request
            sort_column = request.args.get("sort_column")
            sort_order = request.args.get("sort_order", "asc")  # Default to ascending order if not provided

            # If the sort column is not provided, return 400
            if not sort_column:
                return jsonify({"error": "'sort_column' query parameter is required."}), 400

            # Apply sorting to the data
            sorted_data = self.processed_df.orderBy(col(sort_column).asc() if sort_order == "asc" else col(sort_column).desc())

            # Convert the sorted data to JSON
            data_json = sorted_data.toJSON().collect()

            return jsonify({"data": data_json})

        except Exception as e:
            return jsonify({"error": str(e)}), 400
    
    def get_all_data(self):
        """ Returns all the data available. """

        # Convert the PySpark DataFrame to a Pandas DataFrame for easy JSON serialization
        pandas_df = self.processed_df.toPandas()
        # Convert the Pandas DataFrame to a JSON list
        json_data = pandas_df.to_json(orient='records')
        return jsonify(json_data)
        
    def summary_statistics(self):
        """ Displays descriptive statistics of the data. """
        try:
            describe_stats = self.processed_df.describe().toPandas().to_dict()

            return jsonify({"data": describe_stats})

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def run(self):
        # remove use_reloader for non testing environments
        flask_config = self.config.get_flask_config()
        self.app.run(host=flask_config['HOST'], port=flask_config['PORT'], debug=flask_config.getboolean('DEBUG'),
                     use_reloader=False)
        # self.app.run(host=flask_config['HOST'], port=flask_config['PORT'], use_reloader=True)


class APIClient:
    @staticmethod
    def make_request(endpoint_number: int, params: dict) -> dict:
        """
        Make a request to a specified API endpoint.

        Parameters:
        - endpoint_number (int): The number corresponding to the desired API endpoint.
        - params (dict): Query parameters for the API request.

        Returns:
        - dict: The JSON response from the API.
        """
        base_url = "http://127.0.0.1:5000"

        # Define the valid endpoint numbers and their corresponding paths
        endpoints = {
            1: "/filter_one_column",
            2: "/get_data",
            3: "/get_data_tabular",
            4: "/sort_data",
            5: "/get_all_data",
            6: "/summary_statistics"
        }

        # Check if the provided endpoint number is valid
        if endpoint_number not in endpoints:
            raise ValueError("Invalid endpoint number. Please choose a number between 1 and 6 inclusive.")

        # Construct the complete API URL
        api_url = f"{base_url}{endpoints[endpoint_number]}"

        try:
            # Make the API request
            response = requests.get(api_url, params=params)
            response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)

            return response.json()

        except requests.exceptions.RequestException as e:
            # Handle request exceptions (e.g., connection error, timeout)
            return {"error": f"Failed to make API request: {str(e)}"}


if __name__ == '__main__':
    config = Config()
    data_api = DataAPI(config)

    # for production use only
    # data_api.run()

    # for testing
    data_api_thread = threading.Thread(target=data_api.run)

    # initiates the execution of the run method in a separate thread.
    data_api_thread.start()


    # Wait for the Flask app thread to finish
    input("Press Enter to continue after the Flask app starts...")

    # Example Spark SQL query
    try:
        sql_query = "SELECT App, Rating, Installs FROM df_cleaned2 WHERE Rating > 4.5 ORDER BY Installs DESC LIMIT 10"
        result_sql_df = data_api.processor.spark.sql(sql_query)
        print("\nResult of SQL Query:")
        result_sql_df.show()

    except Exception as e:
        print(f"Error executing SQL query: {str(e)}")

    # # Example API requests
    print(APIClient.make_request(1, {"column_name": "Category", "column_value": "ART_AND_DESIGN"}))   
    # print(APIClient.make_request(2, {"Rating": "4.1", "Category": "ART_AND_DESIGN"})
    # print(APIClient.make_request(3, {"Rating": "4.1", "Category": "ART_AND_DESIGN"})
    # print(APIClient.make_request(4, {"sort_column": "Rating", "sort_order": "desc"})
    # print(APIClient.make_request(5, {})  # get_all_data
    # print(APIClient.make_request(6, {})  # describe_data
    data_api_thread.join()