#!/bin/bash

# This assumes that the file is already present in HDFS
# If not, you can use the following command to copy the file to HDFS
# hdfs dfs -put {local_path_to_file} /{hdfs_path_to_file}

# Get input file path from user
DEFAULT_INPUT_FILE="hdfs://10.10.1.1:9000/web-BerkStan.txt"
DEFAULT_OUTPUT_FILE="hdfs://10.10.1.1:9000/persistence_output.txt"

read -p "Enter the input file path [default: $DEFAULT_INPUT_FILE]: " INPUT_FILE
INPUT_FILE=${INPUT_FILE:-$DEFAULT_INPUT_FILE}

read -p "Enter the output file path [default: $DEFAULT_OUTPUT_FILE]: " OUTPUT_FILE
OUTPUT_FILE=${OUTPUT_FILE:-$DEFAULT_OUTPUT_FILE}

# Install pip3 and pyspark for application to work
sudo apt install python3-pip
pip3 install pyspark

spark-3.3.4-bin-hadoop3/bin/spark-submit \
    --master spark://10.10.1.1:7077 \
    part3-3.py $INPUT_FILE $OUTPUT_FILE
