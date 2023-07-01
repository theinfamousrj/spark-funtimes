# Spark Funtimes!

## What is this?

In this repo we'll be installing Python 3.X, installing the Java runtime (JRE), and attempting to dissect a parquet file. All before I finish this espresso, if I can help it. :P

## How does it all work?

The main idea is that if we install Python and the associated pyspark library, we *should* be able to create a temporary view (yes, like a database view), and run SQL commands on a flat file (rather than a database). Unfortunately the pyspark library also requires us to install the Java Runtime Environment (JRE) so... we have to have Java as well.

### Installation

[Install Python3.X](https://www.python.org/downloads/)
`python3 --version`
`python3 -m pip install --upgrade pip`
`python3 -m pip install pyspark `

[Install Java Runtime](https://www.java.com/en/)

### Running the script

`python3 main.py`

### Coding

[Read the docs](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html)

## 

## But... why?

FOR FUN! And for an interview.