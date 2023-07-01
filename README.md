# Spark Funtimes!

## Index
- [What is this?](#what-is-this)
- [How does it all work?](#how-does-it-all-work)
    - [Installation](#installation)
        - [Mac/Linux](#maclinux)
        - [Windows](#windows)
    - [Running the script](#running-the-script)
    - [Coding?](#coding)
- [But... why?](#but-why)

## What is this?

In this repo we'll be installing Python 3.X, installing the Java runtime (JRE), and attempting to dissect a parquet file. All before I finish this espresso, if I can help it. :P

## How does it all work?

The main idea is that if we install Python and the associated pyspark library, we *should* be able to create a temporary view (yes, like a database view), and run SQL commands on a flat file (rather than a database). Unfortunately the pyspark library also requires us to install the Java Runtime Environment (JRE) so... we have to have Java as well.

### Installation

First, click this link: [Install Python3.X](https://www.python.org/downloads/) in order to download and install python on your computer. Follow the on-screen instructions to install it.

#### Mac/Linux

If you're running this on MacOS or Linux, open your `Terminal` app and run the following command to ensure that python is intalled on your system:
```bash
python3 --version
```

#### Windows

You should get a response that looks something like this:
```bash
Python 3.11.4
```

If you're not getting that message, either check the [python forums](https://discuss.python.org/) or reach out to me and we'll troubleshoot your install together. Otherwise, continue reading this document.

Next we want to ensure `pip` is all up to date by running the following:
```bash
python3 -m pip install --upgrade pip
```

`python3 -m pip install pyspark `

[Install Java Runtime](https://www.java.com/en/)

### Running the script

`python3 main.py`

### Coding

[Read the docs](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html)

## But... why?

FOR FUN! And for an interview.