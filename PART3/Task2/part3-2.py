from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

def create_spark_application(input_file_path, output_file_path):
    spark = (SparkSession
	.builder
	.appName("assignment-part3-task2")
	.getOrCreate())
    
    numPartitions = 10
    df_rdd = spark.sparkContext.textFile(input_file_path)
    print("Initial Number of Partions: ", df_rdd.getNumPartitions())
    #df_rdd = df_rdd.repartition(numPartitions)
    #df.printSchema()

    # Filter out the rows that are comments and start with "#"
    filtered_rdd = df_rdd.filter(lambda line: line[0] != "#")

    # Split every line by tab and get the first and second value as the source and destination nodes
    # Group by key to get the destination nodes for each source node
    links = filtered_rdd.map(lambda line: (line.split("\t")[0],line.split("\t")[1])).groupByKey().repartition(numPartitions)

    rank = links.map(lambda node: (node[0], 1))

    print(links.getNumPartitions())
    for i in range(10):
        contributions_per_page = links.join(rank).flatMap(lambda val: [(page, val[1][1]/len(val[1][0])) for page in val[1][0]])
        sum_contributions_per_page = contributions_per_page.reduceByKey(lambda a, b: a + b)
        rank = sum_contributions_per_page.mapValues(lambda contribution: 0.15 + 0.85 * contribution)
    

    rank.coalesce(1).saveAsTextFile(output_file_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 part3-1.py <input_file_path> <output_file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    create_spark_application(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
