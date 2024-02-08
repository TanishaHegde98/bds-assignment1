# CS744 Big Data Systems Assignment 1

## Project Team
- Aanandita Dhawan
- Aboli Pai
- Lakshika Rathi
- Tanisha Hegde

## Problem

**Data Sorting:** Given an input CSV file, the task involves organizing the data by specific column/s.

**PageRank Implementation:** The project entails completing four distinct tasks:

- **Task 1 - Algorithm Implementation:** Develop a Spark application in Scala/Python/Java to execute the PageRank algorithm.
- **Task 2 - Custom RDD Partitioning:** Implement customized RDD partitioning and analyze resulting changes.
- **Task 3 - RDD Persistence:** Explore in-memory RDD persistence and assess its impact.
- **Task 4 - Failure Simualtion:** Simulate Worker process failure and monitor the system's response. Trigger the failure when the application is halfway through its lifecycle.

## Project Cloning

```bash
git clone https://github.com/TanishaHegde98/bds-assignment1.git
```

## Data Sorting Spark Application

```bash
./run.sh input_file_path output_file_path

#for example: 
./run.sh /proj/uwmadison744-s24-PG0/data-part3/enwiki-pages-articles/ wiki_output

## PageRank Subparts 1,2,3

```bash
cd PART3
cd Task1
./run.sh input_file_path output_file_path
```

