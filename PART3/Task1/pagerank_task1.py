from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

def create_spark_application(input_file_path, output_file_path):
    spark = (SparkSession
	.builder
	.appName("assignment-part3-task1")
	.getOrCreate())

    df_rdd = spark.sparkContext.textFile(input_file_path)

    # Filter out the rows that are comments and start with "#"
    filtered_rdd = df_rdd.filter(lambda line: line[0] != "#")

    # Get the first value from the line and store distinct values as nodes in the page rank algorithm
    node_rdd = filtered_rdd.map(lambda line: line.split("\t")[0]).distinct()

    # Initialize a rank for each node as 1
    rank = node_rdd.map(lambda node: (node, 1))

    # Split every line by tab and get the first and second value as the source and destination nodes
    # Group by key to get the destination nodes for each source node
    links = filtered_rdd.map(lambda line: (line.split("\t")[0],line.split("\t")[1])).groupByKey()

    # Run the page rank algorithm for 10 iterations
    for i in range(10):
        # Calcluate the contributions of each node to the rank of other nodes
        # Join the links and rank rdd to get a tuple of (source_node, (destination_nodes, rank))
        # Calculate the contributions per page by dividing the rank of the source node to the number of destination nodes and map it for every destination node (page)
        contributions_per_page = links.join(rank).flatMap(lambda val: [(page, val[1][1]/len(val[1][0])) for page in val[1][0]])

        # Sum the contributions per page received from other nodes
        sum_contributions_per_page = contributions_per_page.reduceByKey(lambda a, b: a + b)

        # Calculate the new rank for each node by using the formula
        rank = sum_contributions_per_page.mapValues(lambda contribution: 0.15 + 0.85 * contribution)
    
    # Store the final rank in the output file
    rank.saveAsTextFile(output_file_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 PART2-Sorting.py <input_file_path> <output_file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    create_spark_application(input_file_path, output_file_path)

if __name__ == "__main__":
    main()