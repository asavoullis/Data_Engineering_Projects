# process_data.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, length
from pyspark.sql.types import  IntegerType, FloatType
from pyspark.ml.feature import StringIndexer

from config import Config  # Importing the Config class from config.py

class DataProcessor:
    """
    This class processes a CSV file using PySpark.
    It loads the data, performs cleaning operations and further processesed/transformed the data.
    The explanation of the processing of the GooglePlayStore.csv file is in: PySpark_ML_GooglePlayStore.ipynb.
    """

    def __init__(self, config):
        self.input_path = config.get_data_processing_config()['INPUT_FILE']
        self.spark = self._create_spark_session()

    def _create_spark_session(self):
        """ Creates and return a Spark session. """
        return SparkSession.builder \
            .appName("DataProcessing") \
            .config("spark.ui.reverseProxy", "true") \
            .config("spark.ui.reverseProxyUrl", "http://your-proxy-url:4041") \
            .getOrCreate()

    def _load_data(self):
        """ Loads and returns the CSV data into a PySpark DataFrame. """
        return self.spark.read.load('googleplaystore/googleplaystore.csv', format='csv', sept=',', escape ='"' , header=True, inferSchema=True)

    def process_data(self):
        """ Cleaning and Processesing the Dataframe. """
        # Load the data
        df = self._load_data()

        # Dropping Unnecessary columns
        df_cleaned = df.drop("Size", "Content Rating", "Last Updated", "Android Ver", "Current Ver")

        # Transforming the data into the correct data type
        df_cleaned = df_cleaned.withColumn("Reviews", col("Reviews").cast(IntegerType())) \
                    .withColumn("Installs", regexp_replace(col("Installs"), "[^0-9]", "").cast(IntegerType())) \
                    .withColumn("Price", regexp_replace(col("Price"), "\\$", "").cast(FloatType())) 

        # Droping Unnecessary rows
        df_cleaned = df_cleaned.filter(~(col("Reviews").isNull() & col("Installs").isNull() & col("Price").isNull()))
        df_cleaned = df_cleaned.filter(col("App") != "Command & Conquer: Rivals")

        # Replace NaN values in the "Rating" column with 0
        df_cleaned = df_cleaned.fillna(0, subset=["Rating"])
        
        # Handle Categorical Data 
        indexer = StringIndexer(inputCol="Category", outputCol="CategoryIndex")
        df_cleaned2 = indexer.fit(df_cleaned).transform(df_cleaned)

        # Feature Engineering - creataed a new column representing the length of the "App" column
        df_cleaned2 = df_cleaned2.withColumn("AppNameLength", length("App"))

        df_cleaned2.createOrReplaceTempView("df_cleaned2")
        # print("DataFrame names:", self.spark.catalog.listTables())
        return df_cleaned2

if __name__ == "__main__":
    config = Config()
    processor = DataProcessor(config)
    processed_df = processor.process_data()

    # Wait for the Spark Session to start 
    input("Press Enter to continue after the Spark app starts...")

    # Testing

    # processed_df.show(10)

    processed_df.printSchema()

    # result_df = processed_df.filter((col("CategoryIndex") != "28.0") & (col("CategoryIndex") != "25.0"))
    # result_df.show()

    # Show the distinct values ordered by Price in descending order
    distinct_prices = processed_df.select("Price").distinct().orderBy(col("Price").desc())    
    distinct_prices.show()

    # Wait for the Spark Session to start 
    input("Press Enter to continue after the Spark app starts...")

    print("")

    filtered_df = processed_df.select("Rating").distinct().orderBy(col("Rating").desc())
    filtered_df.show()
