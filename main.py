# Import spark library
from pyspark.sql import SparkSession # type: ignore
import os

# Set some sensible variables
file_name = "yellow_tripdata_2023-01.parquet"
file_size_limit = 1000000000 # in bytes aka 1GB here
percentile = 0.90
order_by = "trip_distance DESC"

# Create a SparkSession
spark = SparkSession.builder.appName("SparkFuntimes").getOrCreate()

# Read in the Parquet file from the NYC Taxi Data
parquetFile = spark.read.parquet(file_name)

# Let's also get the size of the file too, just in case
file_size = os.path.getsize(file_name)

# Parquet files can also be used to create a temporary view and then used in SQL statements.
parquetFile.createOrReplaceTempView("parquetFile")

# Check the file size and if it is larger than file_size_limit (set above), we should to run an approximate
# Current size: 47673370 bytes
if file_size > file_size_limit:
    print("File size is too large to run exact percentile")
    percentile_sql = "SELECT percentile_approx(trip_distance, " + str(percentile) + ") FROM parquetFile"
else:
    print("File size is small enough to run exact percentile")
    percentile_sql = "SELECT percentile(trip_distance, " + str(percentile) + ") FROM parquetFile"

percentile = spark.sql(percentile_sql)

# Store the percentile value from the DataFrame in a variable so we can use it both to print and to build another query
percentile_value = percentile.collect()[0][0]
print("90th percentile is: ", percentile_value)

# Now we build the actual query to get the data we want
data_sql = "SELECT VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance FROM parquetFile WHERE trip_distance > " + str(percentile_value) + " ORDER BY " + order_by
data = spark.sql(data_sql)
data.show()