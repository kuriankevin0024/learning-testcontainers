import time
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark_Delay").getOrCreate()
    print(f'>>> Mode: {spark.sparkContext.master}')

    duration = 60
    for sec in range(duration, 0, -1):
        print(f"Time remaining: {sec}s")
        time.sleep(1)

    count = spark.sparkContext.parallelize(range(1_000_000)).count()
    print(f"Final count: {count}")

    spark.stop()
