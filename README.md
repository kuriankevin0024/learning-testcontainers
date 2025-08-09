# learning-testcontainers

## setup python venv
* activate venv: `python -m venv ./.venv && source .venv/bin/activate`
* install dependencies: `pip install -r requirements.txt`

## delete all installed pip dependencies
`pip freeze | grep -v " @ " | cut -d'=' -f1 | xargs pip uninstall -y`

## cursor chat history
`~/Library/Application Support/Cursor/User/workspaceStorage`

## Spark
* Doc: https://spark.apache.org/docs/latest/api/python/index.html#
* Path: `spark/spark_standalone.yml`
* Run Application:
  * local: driver and executors are run where the application is submitted
    * `spark-submit /opt/spark/work-dir/code/number_stats.py`
  * client: driver is run where the application is submitted and executors are run on the workers
    * `spark-submit --master spark://spark-master:7077 /opt/spark/work-dir/code/number_stats.py`
* Spark Endpoints:
  * Spark RPC Port: 7077
  * Master UI: http://localhost:8080/
  * History UI: http://localhost:18080/
  * Driver UI: http://localhost:4040/
  * Worker UI: http://localhost:8081/
* eventLogs are only created by driver
* Scale Workers:
  * `docker-compose -f spark/master_worker_scale.yml up -d --scale spark-worker=3`
  * navigation from MasterUI to WorkerUI breaks in scale

## Milvus
Doc: https://milvus.io/docs
### Run Milvus Standalone
Docker Compose: https://milvus.io/docs/install_standalone-docker-compose.md
Path: `milvus/docker_compose/docker-compose.yml`
Milvus UI: http://127.0.0.1:9091/webui/

## Spark Iceberg
Doc: https://iceberg.apache.org/spark-quickstart/
### Run Spark Iceberg
Docker Compose: https://iceberg.apache.org/spark-quickstart/#docker-compose
#### Hadoop Catalog
Hadoop Catalog: `spark_iceberg/hadoop_catalog/docker-compose.yml`
Run Spark SQL: `spark-submit /home/iceberg/code/spark_iceberg.py`
Jupyter UI: http://localhost:8888/
Spark Master UI: http://localhost:8080/
Spark Driver UI: http://localhost:4040/
Spark Worker UI: http://localhost:8081/
Spark History UI: http://localhost:18080/

Rest Catalog: `spark_iceberg/rest_catalog/docker-compose.yml`
Hive Catalog: ToDo...

Minio UI: http://localhost:9001
