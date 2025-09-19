from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkIceberg").getOrCreate()

print('>>> show catalogs <<<')
spark.sql('SHOW CATALOGS;').show()

print('>>> create schema <<<')
spark.sql("CREATE NAMESPACE IF NOT EXISTS hive.iceberg_schema;")
print('>>> show schemas <<<')
spark.sql('SHOW NAMESPACES IN hive;').show()

print('>>> create table <<<')
spark.sql("CREATE TABLE IF NOT EXISTS hive.iceberg_schema.iceberg_table (id INT, name STRING, ts TIMESTAMP);")
print('>>> show tables <<<')
spark.sql('SHOW TABLES IN hive.iceberg_schema;').show()

print('>>> create row <<<')
spark.sql("INSERT INTO hive.iceberg_schema.iceberg_table VALUES (1, 'john doe', current_timestamp());")
print('>>> show rows <<<')
spark.sql('SELECT * FROM hive.iceberg_schema.iceberg_table;').show()

print('>>> delete row <<<')
spark.sql("DELETE FROM hive.iceberg_schema.iceberg_table WHERE id IN (1);")
print('>>> show rows <<<')
spark.sql('SELECT * FROM hive.iceberg_schema.iceberg_table;').show()

print('>>> drop table <<<')
spark.sql('DROP TABLE IF EXISTS hive.iceberg_schema.iceberg_table;')
print('>>> show tables <<<')
spark.sql('SHOW TABLES IN hive.iceberg_schema;').show()

print('>>> drop schema <<<')
spark.sql('DROP NAMESPACE IF EXISTS hive.iceberg_schema CASCADE;')
print('>>> show schemas <<<')
spark.sql('SHOW NAMESPACES IN hive;').show()

print('>>> show catalogs <<<')
spark.sql('SHOW CATALOGS;').show()

spark.stop()
