# templates.py

WELCOME_TEMPLATE = """
<html>
<head>
    <title>Google Play Store Data API</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            max-width: 800px;
            margin: auto;
        }
        h1, h2 {
            color: #4285f4;
        }
        pre {
            background-color: #f2f2f2;
            padding: 10px;
            border-radius: 5px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
        }
        p {
            line-height: 1.5;
        }
        footer {
            margin-top: 20px;
            font-size: 0.8em;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Google Play Store Data API</h1>
    <p>Developed by Charilaos A Savoullis!</p>
    <p>This API provides access to processed data from the Google Play Store.</p>
    <p>Explore various endpoints to analyze and retrieve information.</p>
    <h2>Data Schema:</h2>
    <pre>
    root
     |-- App: string (nullable = true)
     |-- Category: string (nullable = true)
     |-- Rating: double (nullable = false)
     |-- Reviews: integer (nullable = true)
     |-- Installs: integer (nullable = true)
     |-- Type: string (nullable = true)
     |-- Price: float (nullable = true)
     |-- Genres: string (nullable = true)
    </pre>
    <h2>Available Endpoints:</h2>
    <ul>
        <li>/get_all_data: Retrieve all processed data.</li>
        <li>/filter_one_column: Filter data based on a specified column.</li>
        <li>/get_data: Retrieve specific data points.</li>
        <li>/get_data_tabular: Retrieve data in a tabular format.</li>
        <li>/sort_data: Sort the data based on specified criteria.</li>
    </ul>
    <p>Feel free to explore and integrate this API into your applications!</p>
    <footer>Credits: Charilaos A Savoullis</footer>
</body>
</html>
"""
