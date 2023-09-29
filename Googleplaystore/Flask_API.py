from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from flask import Flask, request, jsonify
import requests
import threading

# Initialize a SparkSession
spark = SparkSession.builder.appName("PySparkAPI").getOrCreate()

# Read data from a CSV file
data = spark.read.csv("googleplaystore/googleplaystore.csv", header=True, inferSchema=True)

# data.show(5)

# Initialize a Flask web application
app = Flask(__name__)

@app.route("/get_data", methods=["GET"])
def get_data():
    """
    http://localhost:5000/get_data?column_name=App&column_value=Infinite%20Painter
    """
    try:
        # Get query parameters from the request
        filters = request.args.to_dict()

        # Check if any filters are provided
        if not filters:
            return jsonify({"error": "No filter criteria provided."}), 400

        # Initialize a base DataFrame with all the data
        filtered_data = data

        # Apply filters dynamically based on user-provided criteria
        for column, value in filters.items():
            filtered_data = filtered_data.filter(col(column) == value)

        # Convert the filtered data to JSON
        data_json = filtered_data.toJSON().collect()

        # Return the JSON response
        return jsonify({"data": data_json})

    except Exception as e:
        return jsonify({"error": str(e)})




# Function to start the Flask application
def start_flask_app():
    app.run(host="0.0.0.0", port=5000)

# Create a thread to run the Flask app
flask_thread = threading.Thread(target=start_flask_app)



if __name__ == "__main__":
    # Start the Flask app thread
    flask_thread.start()

    # Wait for the Flask app to start (optional)
    # You can remove this if you don't need to wait
    input("Press Enter to continue after the Flask app starts...")

    # Define the API endpoint URL with query parameters
    api_url = "http://127.0.0.1:5000/get_data"
    params = {"column_name": "App", "column_value": "Infinite Painter"}

    # Make a GET request to the API with parameters
    response = requests.get(api_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
