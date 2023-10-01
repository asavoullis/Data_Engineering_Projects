from flask import Flask, request, jsonify
from pyspark.sql.functions import col
import threading
import requests
from flask import render_template_string

# importing 
from process_data import DataProcessor
from templates import WELCOME_TEMPLATE


class DataAPI:
    def __init__(self, input_file):
        self.app = Flask(__name__)
        self.processor = DataProcessor(input_file)
        self.processed_df = self.processor.process_data()

        # Set up routes
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/get_all_data', 'get_all_data', self.get_all_data, methods=['GET'])
        self.app.add_url_rule('/filter_one_column', 'filter_one_column', self.filter_one_column, methods=['GET'])
        self.app.add_url_rule('/get_data', 'get_data', self.get_data, methods=['GET'])
        self.app.add_url_rule('/get_data_tabular', 'get_data_tabular', self.get_data_tabular, methods=['GET'])
        self.app.add_url_rule('/sort_data', 'sort_data', self.sort_data, methods=['GET'])


    def index(self):
        """
        The index function serves as the welcome endpoint for the Google Play Store Data API.
        It provides users with a friendly introduction to the API and a quick overview of available endpoints.
        Explore this endpoint to get started and learn about the various functionalities the API offers.
        """
        return render_template_string(WELCOME_TEMPLATE)


    def get_all_data(self):
        """
        Returns all the data available.
        http://localhost:5000/get_all_data
        
        ---
        tags:
            - Data
        responses:
            200:
                description: JSON representation of all data.
        """

        # Convert the PySpark DataFrame to a Pandas DataFrame for easy JSON serialization
        pandas_df = self.processed_df.toPandas()
        # Convert the Pandas DataFrame to a JSON string
        json_data = pandas_df.to_json(orient='records')
        return jsonify(json_data)
    
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

            # Convert the filtered data to JSON
            data_json = filtered_data.toJSON().collect()

            # Return the JSON response
            return jsonify({"data": data_json})

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def get_data(self):
        """
        Allows you to filter multiple columns and retrieve data in json format
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

            # Convert the filtered data to JSON
            data_json = filtered_data.toJSON().collect()

            # Return the JSON response
            return jsonify({"data": data_json})

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def get_data_tabular(self):
        """
        Allows you to filter multiple columns and retrieve data in a tabular format where each result appears in a different dictionary
        http://localhost:5000/get_data_tabular?column1=value1&column2=value2&column3=value3...
        http://localhost:5000/get_data_tabular?Rating=4.1&Category=ART_AND_DESIGN

        The function will return data where both conditions are met: the Rating is equal to "4.1" AND the Category is equal to "ART_AND_DESIGN."
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
        http://localhost:5000/sort_data?sort_column=Price&sort_order=desc
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

            # Return the JSON response
            return jsonify({"data": data_json})

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def run(self):
        # remove use_reloader for non testing environments
        self.app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

def make_api_request(number: int, params):
    try:
        if number in (1, 2, 3):
            # Define the API endpoint URL with query parameters
            if number == 1:
                api_url = "http://127.0.0.1:5000/filter_one_column"
            elif number == 2:
                api_url = "http://127.0.0.1:5000/get_data"
            elif number == 3:
                api_url = "http://127.0.0.1:5000/get_data_tabular"
            elif number == 4:
                api_url = "http://127.0.0.1:5000/sort_data"
            elif number == 5:
                api_url = "http://127.0.0.1:5000/get_all_data"
        else:
            return "Invalid endpoint number. Please choose select a number between 1 and 5 inclusive."
        
        # Make a GET request to the API with parameters
        response = requests.get(api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            print(data)
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    input_file = "googleplaystore/googleplaystore.csv"
    data_api = DataAPI(input_file)
    data_api_thread = threading.Thread(target=data_api.run)

    # Start the Flask app in a separate thread
    data_api_thread.start()

    # Wait for the Flask app thread to finish
    data_api_thread.join()

    # Wait for the Flask app to start (optional)
    input("Press Enter to continue after the Flask app starts...")

    # Example API requests
    make_api_request(1, {"column_name": "Category", "column_value": "ART_AND_DESIGN"})
    make_api_request(2, {"Rating": "4.1", "Category": "ART_AND_DESIGN"})
    make_api_request(3, {"Rating": "4.1", "Category": "ART_AND_DESIGN"})
    make_api_request(4, {"sort_column": "Rating", "sort_order": "desc"})
    # make_api_request(5, {})  # get_all_data

    
