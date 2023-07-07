# Import spark library
from pyspark.sql import SparkSession # type: ignore
import os
import argparse
import time

# Making a function to handle the processing of the file
def process_file(input_file, output_path, file_size_limit=1000000000, accuracy=10000, percentile=0.90):
  # Create a SparkSession
  spark = SparkSession.builder.appName("SparkFuntimes").getOrCreate()

  # Read in the Parquet file from the NYC Taxi Data
  parquet_file = spark.read.parquet(input_file)

  # Let's also get the size of the file too, just in case
  file_size = os.path.getsize(input_file)

  # Parquet files can also be used to create a temporary view (like in a traditional DB) and then used in SQL statements.
  parquet_file.createOrReplaceTempView("parquet_file")

  # Check the file size and if it is larger than file_size_limit (set above), we should to run an approximate
  # This will use the approximate percentile function instead of the exact one if the file is over 1GB
  if file_size > int(file_size_limit):
    print("File size is too large to run exact percentile")
    print("Relative error of approximation: ", 1/int(accuracy))
    percentile_sql = "SELECT percentile_approx(trip_distance, " + str(percentile) + ", " + str(accuracy) + ") FROM parquet_file"
  else:
    print("File size is small enough to run exact percentile")
    percentile_sql = "SELECT percentile(trip_distance, " + str(percentile) + ") FROM parquet_file"

  percentile = spark.sql(percentile_sql)

  # Store the percentile value from the DataFrame in a variable so we can use it both to print and to build another query
  percentile_value = percentile.collect()[0][0]
  print("Finding trip_distance > ", percentile_value)

  # Now we build the actual query to get the data we want using the percentile we just calculated
  data_sql = "SELECT VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance FROM parquet_file WHERE trip_distance > " + str(percentile_value)
  data = spark.sql(data_sql)

  # We likely don't want multipart files as output, so we can coalesce the data to one partition
  data.coalesce(1).write.parquet(output_path, mode='overwrite')

if __name__ == '__main__':
  # Let's make sure we at least have input file and output path and sensible defaults for the rest of the params
  parser = argparse.ArgumentParser(description='Process a parquet file and find the Nth percentile of the trip_distance')
  parser.add_argument('-i', '--input', required=True, help='Input file name')
  parser.add_argument('-o', '--output', required=True, help='Output file path')
  parser.add_argument('-s', '--size', default=1000000000, help='File size limit in bytes (optional)')
  parser.add_argument('-a', '--accuracy', default=10000, help='The approximation accuracy (optional)')
  parser.add_argument('-p', '--percentile', default=0.90, help='The percentile (optional)')

  # Parse the arguments and process the file
  args = parser.parse_args()
  process_file(args.input, args.output, args.size, args.accuracy, args.percentile)