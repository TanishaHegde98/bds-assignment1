# CS744 Big Data Systems Assignment 1

## Project Team
- Aanandita Dhawan (dhawan6@wisc.edu)
- Aboli Pai (apai7@wisc.edu)
- Lakshika Rathi (lrathi@wisc.edu)
- Tanisha Hegde (tghegde@wisc.edu)

## Problem

**Data Sorting:** Given an input CSV file, the task involves organizing the data by specific column/s.

**PageRank Implementation:** The project entails completing four distinct tasks:

- **Task 1 - Algorithm Implementation:** Develop a Spark application in Scala/Python/Java to execute the PageRank algorithm.
- **Task 2 - Custom RDD Partitioning:** Implement customized RDD partitioning and analyze resulting changes.
- **Task 3 - RDD Persistence:** Explore in-memory RDD persistence and assess its impact.
- **Task 4 - Failure Simualtion:** Simulate Worker process failure and monitor the system's response. Trigger the failure when the application is 25% and 75% through its lifecycle.

## Clone Cmd

```bash
git clone https://github.com/TanishaHegde98/bds-assignment1.git
```

## Data Sorting Spark Application

```bash
cd src/data_sorting/

./run.sh input_file_path output_file_path

#for example: 
./run.sh /proj/uwmadison744-s24-PG0/data-part3/enwiki-pages-articles/ wiki_output
```

## PageRank Subparts 1,2,3

```bash
#for subpart1:
cd src/pagerank/Subpart1

./run.sh input_file_path output_file_path

#for example:
./run.sh web-BerkStan.txt rank.txt
```

## Project Structure

The project repository is organized as follows:

- `README.md`: This README file providing an overview of the assignment and project structure.
- `src/`: Contains the source code for implementing the data sorting and PageRank tasks.
  - `data_sorting/`: Directory for data sorting-related code and scripts.
  - `pagerank/`: Directory for PageRank algorithm implementation and related tasks.
- `report.pdf`: Detailed report documenting the methodology, experimentation, and analysis conducted during the assignment.

For any inquiries or assistance, please reach out to the project team members listed above.
