# Import spark library
from pyspark.sql import SparkSession # type: ignore
import os

# Set some sensible variables
file_name = "yellow_tripdata_2023-01.parquet"

# Create a SparkSession
spark = SparkSession.builder.appName("SparkFuntimes").getOrCreate()

# Read in the Parquet file from the NYC Taxi Data
parquet_file = spark.read.parquet(file_name)

# Write the DataFrame to a CSV file with tab delimiter
output_directory = 'output'
parquet_file.write.csv(output_directory, sep='\t', header=True)