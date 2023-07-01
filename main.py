# import spark libraries
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("SparkFuntimes").getOrCreate()

# Read in the Parquet file from the NYC Taxi Data
parquetFile = spark.read.parquet("yellow_tripdata_2023-01.parquet")

# Parquet files can also be used to create a temporary view and then used in SQL statements.
parquetFile.createOrReplaceTempView("parquetFile")
data = spark.sql("SELECT * FROM parquetFile LIMIT 10")
data.show()