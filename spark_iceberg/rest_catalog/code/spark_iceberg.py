from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkIceberg").getOrCreate()

print('>>> show catalogs <<<')
spark.sql('SHOW CATALOGS;').show()

print('>>> create schema <<<')
spark.sql("CREATE NAMESPACE IF NOT EXISTS iceberg_catalog.iceberg_schema "
          "LOCATION 's3://warehouse/iceberg_schema';")
print('>>> show schemas <<<')
spark.sql('SHOW NAMESPACES IN iceberg_catalog;').show()

print('>>> create table <<<')
spark.sql("CREATE TABLE IF NOT EXISTS iceberg_catalog.iceberg_schema.iceberg_table (id INT, name STRING, ts TIMESTAMP) "
          "USING iceberg LOCATION 's3://warehouse/iceberg_schema/iceberg_table';")
print('>>> show tables <<<')
spark.sql('SHOW TABLES IN iceberg_catalog.iceberg_schema;').show()

print('>>> create row <<<')
spark.sql("INSERT INTO iceberg_catalog.iceberg_schema.iceberg_table VALUES (1, 'john doe', current_timestamp());")
print('>>> show rows <<<')
spark.sql('SELECT * FROM iceberg_catalog.iceberg_schema.iceberg_table;').show()

print('>>> delete row <<<')
spark.sql("DELETE FROM iceberg_catalog.iceberg_schema.iceberg_table WHERE id IN (1);")
print('>>> show rows <<<')
spark.sql('SELECT * FROM iceberg_catalog.iceberg_schema.iceberg_table;').show()

print('>>> drop table <<<')
spark.sql('DROP TABLE IF EXISTS iceberg_catalog.iceberg_schema.iceberg_table;')
print('>>> show tables <<<')
spark.sql('SHOW TABLES IN iceberg_catalog.iceberg_schema;').show()

print('>>> drop schema <<<')
spark.sql('DROP NAMESPACE IF EXISTS iceberg_catalog.iceberg_schema CASCADE;')
print('>>> show schemas <<<')
spark.sql('SHOW NAMESPACES IN iceberg_catalog;').show()

print('>>> show catalogs <<<')
spark.sql('SHOW CATALOGS;').show()

spark.stop()
