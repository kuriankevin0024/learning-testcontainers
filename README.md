# learning-testcontainers

## setup python venv
* activate venv: `python -m venv ./.venv && source .venv/bin/activate`
* install dependencies: `pip install -r requirements.txt`

## delete all installed pip dependencies
`pip freeze | grep -v " @ " | cut -d'=' -f1 | xargs pip uninstall -y`

## Milvus
Doc: https://milvus.io/docs

### Run Milvus Standalone
Docker Compose: https://milvus.io/docs/install_standalone-docker-compose.md
Path: `milvus/docker_compose/docker-compose.yml`
Milvus UI: http://127.0.0.1:9091/webui/
ToDo: Develop Python Code and TestContainer Testcase

## Spark Iceberg
Doc: https://iceberg.apache.org/

### Run Spark Iceberg
Docker Compose: https://iceberg.apache.org/spark-quickstart/#docker-compose
Path: `spark_iceberg/docker-compose.yml`
Run Spark SQL: `spark-submit /home/iceberg/spark_iceberg.py`
Minio UI: http://localhost:9001
