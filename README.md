# Spark Funtimes!

## Index
- [What is this?](#what-is-this)
- [How does it all work?](#how-does-it-all-work)
    - [Installation](#installation)
        - [Mac/Linux](#maclinux)
        - [Windows](#windows)
    - [Updating](#updating)
    - [Downloading this repo](#downloading-this-repo)
    - [Working with this repo](#working-with-this-repo)
    - [Installing PySpark](#installing-pyspark)
    - [Running the script](#running-the-script)
    - [Coding?](#coding)
- [But... why?](#but-why)

## What is this?

In this repo we'll be installing Python 3.X, installing the Java runtime (JRE), and attempting to dissect a parquet file. All before I finish this espresso, if I can help it. :P

## How does it all work?

The main idea is that if we install Python and the associated pyspark library, we *should* be able to create a temporary view (yes, like a database view), and run SQL commands on a flat file (rather than a database). Unfortunately the pyspark library also requires us to install the Java Runtime Environment (JRE) so... we have to have Java as well.

### Installation

#### Mac/Linux

First, click this link: [Install Python3.X](https://www.python.org/downloads/) in order to download and install python on your computer. Double-click the downloaded file and follow the on-screen instructions to install it.

If you're running this on MacOS or Linux, open your `Terminal` app and run the following command to ensure that python is intalled on your system:
```bash
python3 --version
```

#### Windows

First, click this link: [Get started using Python on Windows for beginners](https://learn.microsoft.com/en-us/windows/python/beginners) and follow the instructions in order to get python installed on your windows computer.

If you're running this on Windows, open your `cmd` app or `PowerShell` and run the following command to ensure that python is intalled on your system:
```bash
python3 --version
```

You *may* have to do some PATH editing on a windows machine to get this to work correctly. Here is a [quick tutorial on adding Python to your PATH](https://www.youtube.com/watch?v=3J96_vyfx8Y) in Windows.

Regardless of which OS you are running you should get a response that looks something like this:
```bash
Python 3.11.4
```

If you're not getting that message, either check the [python forums](https://discuss.python.org/) or reach out to me and we'll troubleshoot your install together. Otherwise, continue reading this document.

Next we need to [Install the Java Runtime](https://www.java.com/en/) (JRE). Download the file, double-click it, and follow the on-screen instructions in order to get the JRE installed on your computer.

### Updating

Next we want to ensure `pip` is all up to date by running the following:
```bash
python3 -m pip install --upgrade pip
```

### Downloading this repo

If you're reading this README, you're either at my github repo page on the internet, or you've already downloaded it to your local machine. If you're on the github page, just [click here to download](https://github.com/theinfamousrj/spark-funtimes/archive/refs/heads/main.zip) the repo. 

### Working with this repo

Once you've downloaded it, unzip it and open either the `Terminal` app or `cmd` or `PowerShell`, same as we did earlier, depending on your OS. More than likely you'll have downloaded it to your `Downloads` folder.

On Mac/Linux you can get there via the `Terminal` app by typing:
```bash
cd ~/Downloads/spark-funtimes
```

And on Windows you can get there via `cmd` or `PowerShell` typing:
```PWSH
cd %HOMEPATH%\Downloads\spark-funtimes
```

### Installing PySpark

Technically you can run this anywhere (after you install python), since it will install globally, but it makes sense to me to put it here. Run this in your `Terminal` or `cmd` or `PowerShell`:
```bash
python3 -m pip install pyspark
```

### Running the script

All that's left is to run the script. Run this in your `Terminal` or `cmd` or `PowerShell`:
```bash
python3 main.py
```

### Coding

First I went straight to the docs here: [Apache Spark + Parquet](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html). After that I messed with the code a little to get a `SELECT *` to work. After that I created a [reference file](reference.txt) so that I wouldn't have to swap back and forth in my `main.py` file a bunch. I know I could have used args to flip between SQL statements but it felt very unnecessary and would have bloated the code a little.

## But... why?

FOR FUN! And for an interview.