from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

def create_spark_application(input_file_path, output_file_path):
    spark = (SparkSession
	.builder
	.appName("assignment-part2")
	.getOrCreate())

    df = spark.read.csv(input_file_path, header=True, inferSchema=True)
    
    # Filter out the rows with null values
    df_filtered = df.filter(col("cca2").isNotNull() & col("timestamp").isNotNull())
    df_sorted = df_filtered.orderBy(col("cca2"), col("timestamp"))

    df_sorted.write.csv(output_file_path, header=True, mode="overwrite")
    spark.stop()

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 PART2-Sorting.py <input_file_path> <output_file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    create_spark_application(input_file_path, output_file_path)

if __name__ == "__main__":
    main()


    

