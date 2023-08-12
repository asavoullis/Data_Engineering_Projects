# templates.py

# welcome template 

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
        <li><a href="/get_all_data">/get_all_data</a>: Retrieve all processed data.</li>
        <li><a href="/filter_one_column">/filter_one_column</a>: Filter data based on a specified column.</li>
        <li><a href="/get_data">/get_data</a>: Retrieve specific data points.</li>
        <li><a href="/get_data_tabular">/get_data_tabular</a>: Retrieve data in a tabular format.</li>
        <li><a href="/sort_data">/sort_data</a>: Sort the data based on specified criteria.</li>
        <li><a href="/summary_statistics">/summary_statistics</a>: Displays descriptive statistics of the data.</li>
    </ul>
    <p>Feel free to explore and integrate this API into your applications!</p>
    <footer>Credits: Charilaos A Savoullis</footer>
    <h2>Documentation:</h2>
    <p>Explore the API documentation for more details on how to use each endpoint:</p>
    <a href="/documentation">API Documentation</a>
</body>
</html>
"""

# documentation template

DOCUMENTATION_TEMPLATE = """
<html>
<head>
    <title>API Documentation</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            max-width: 800px;
            margin: auto;
        }
        h1 {
            color: #4285f4;
        }
        p {
            line-height: 1.5;
        }
        code {
            background-color: #f2f2f2;
            padding: 2px 4px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>Google Play Store Data API Documentation</h1>
    <p>This API provides access to processed data from the Google Play Store.</p>
    <h2>Endpoints:</h2>
    <ul>
        <li><code>/index</code>: The index function serves as the welcome endpoint for the Google Play Store Data API. Example:<br> <a href="http://localhost:5000/">http://localhost:5000/</a></li>
        <li><code>/get_all_data</code>: Retrieve all processed data. Example:<br> <a href="http://localhost:5000/get_all_data">http://localhost:5000/get_all_data</a></li>
        <li><code>/filter_one_column</code>: Filter data based on a specified column. Example:<br> <a href="http://localhost:5000/filter_one_column?column_name=App&column_value=Infinite%20Painter">http://localhost:5000/filter_one_column?column_name=App&column_value=Infinite%20Painter</a></li>
        <li><code>/get_data</code>: Retrieve specific data points. Example:<br> <a href="http://localhost:5000/get_data?Rating=4.1&Category=ART_AND_DESIGN">http://localhost:5000/get_data?Rating=4.1&Category=ART_AND_DESIGN</a></li>
        <li><code>/get_data_tabular</code>: Retrieve data in a tabular format. Example:<br> <a href="http://localhost:5000/get_data_tabular?Rating=4.1&Category=ART_AND_DESIGN">http://localhost:5000/get_data_tabular?Rating=4.1&Category=ART_AND_DESIGN</a></li>
        <li><code>/sort_data</code>: Sort the data based on specified criteria. Example:<br> <a href="http://localhost:5000/sort_data?sort_column=Rating&sort_order=asc">http://localhost:5000/sort_data?sort_column=Rating&sort_order=asc</a></li>
        <li><code>/summary_statistics</code>: Displays descriptive statistics of the data. Example:<br> <a href="http://localhost:5000/summary_statistics">http://localhost:5000/summary_statistics</a></li>
    </ul>
    <h2>How to Use:</h2>
    <p>To use the API, make HTTP GET requests to the desired endpoint with the required parameters.</p>
    <p>For example, to filter data based on a specific column:</p>
    <code>GET /filter_one_column?column_name=Category&column_value=ART_AND_DESIGN</code>
</body>
</html>
"""
