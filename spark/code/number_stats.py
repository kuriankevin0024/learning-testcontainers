from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NumberStats").getOrCreate()
print(f'>>> Mode: {spark.sparkContext.master}')
sc = spark.sparkContext

nums = sc.parallelize(list(range(1, 1_000_001)))

_count = nums.count()
_total = nums.sum()
_avg = _total / _count
_min = nums.min()
_max = nums.max()

squares = nums.map(lambda x: x * x).collect()

print(f"Count: {_count}")
print(f"Sum: {_total}")
print(f"Average: {_avg}")
print(f"Min: {_min}, Max: {_max}")
print(f"First 10 Squares: {squares[:10]}")

spark.stop()
