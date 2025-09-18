# learning-testcontainers

## setup python venv
* activate venv: `python -m venv ./.venv && source .venv/bin/activate`
* install dependencies: `pip install -r requirements.txt`

## delete all installed pip dependencies
`pip freeze | grep -v " @ " | cut -d'=' -f1 | xargs pip uninstall -y`

## cursor chat history
`cd ~/Library/Application\ Support/Cursor/User/workspaceStorage`

## Milvus
* Docs:
  * https://milvus.io/docs/install_standalone-docker-compose.md
### Run Milvus
* Install Milvus Venv: `pip install -r milvus/requirements.txt`
* Start Milvus Server: `docker-compose -f milvus/docker-compose.yml up -d`
* Run Milvus Client: `python milvus/milvus_client.py`
* Milvus UI: http://127.0.0.1:9091/webui/

## Spark
* Docs:
  * https://spark.apache.org/docs/latest/api/python/index.html#
* Spark Endpoints:
  * Spark RPC Port: 7077 (used for communication between master and workers) (not exposed as master and worker are part of the same network)
  * Master UI: http://localhost:8080/
  * Driver UI: http://localhost:4040/
  * Worker UI: http://localhost:8081/
  * History UI: http://localhost:18080/ (eventLogs used by history server is only created by driver)
* Run Application:
  * local: driver and executors are run where the application is submitted
    * `spark-submit /opt/spark/work-dir/code/number_stats.py`
  * client: driver is run where the application is submitted and executors are run on the workers
    * `spark-submit --master spark://spark-master:7077 /opt/spark/work-dir/code/number_stats.py`
  * cluster: not supported in pyspark
* Scale Workers:
  * `docker-compose -f spark/master_worker_scale.yml up -d --scale spark-worker=3`
  * navigation from MasterUI to WorkerUI breaks when using scale

## Spark Iceberg
* Docs:
  * https://iceberg.apache.org/spark-quickstart/#docker-compose
* Spark Endpoints:
  * Jupyter UI: http://localhost:8888/
  * Spark Master UI: http://localhost:8080/
  * Spark Driver UI: http://localhost:4040/
  * Spark Worker UI: http://localhost:8081/
  * Spark History UI: http://localhost:18080/
### Run Hadoop Catalog
* Start Spark Iceberg: `docker-compose -f spark_iceberg/hadoop_catalog/docker-compose.yml up -d`
* Run Spark SQL: `spark-submit /home/iceberg/code/spark_iceberg.py`
### Run Hadoop Catalog
* Start Spark Iceberg: `docker-compose -f spark_iceberg/rest_catalog/docker-compose.yml up -d`
* Run Spark SQL: `spark-submit /home/iceberg/code/spark_iceberg.py`
* Minio UI: http://localhost:9001
