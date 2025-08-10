import requests
import numpy as np
import pyarrow as pa
from dataclasses import dataclass
from pymilvus.client.types import MetricType
from pymilvus import Collection, CollectionSchema, DataType, FieldSchema, IndexType, connections, utility
from sentence_transformers import SentenceTransformer

DEFAULT_EMBEDDING_FIELD: str = "embedding"


@dataclass
class Index:
    field_name: str
    index_type: IndexType
    metric_type: MetricType


def connect(host: str, port: int) -> None:
    connections.connect(host=host, port=port)


def healthcheck(url: str) -> bool:
    response: requests.Response = requests.get(url=url)
    return response.status_code == 200


def create_collection(name: str, schema: CollectionSchema, index: Index) -> Collection:
    collection: Collection = Collection(name=name, schema=schema)
    collection.create_index(field_name=index.field_name, index_type=index.index_type, metric_type=index.metric_type)
    collection.load()
    return collection


def list_collections() -> list[str]:
    return utility.list_collections()


def insert_data(collection: Collection, data: list[dict]) -> None:
    collection.insert(data=data)
    collection.flush()


def search(collection: Collection, query_vector: list[float], search_field: str, params: dict, limit: int,
           output_fields: list[str]) -> list[dict]:
    return collection.search(
        data=[query_vector], anns_field=search_field, param=params, limit=limit, output_fields=output_fields)


def update_by_id(collection: Collection, id: int, data: dict) -> None:
    collection.delete(expr=f"id == {id}")
    collection.insert(data=[data])
    collection.flush()


def delete_by_id(collection: Collection, ids: list[int]) -> None:
    collection.delete(expr=f"id in {ids}")
    collection.flush()


def delete_collection(collection_name: str) -> None:
    utility.drop_collection(collection_name=collection_name)


def main() -> None:
    print("Starting Milvus client...")
    connect(host="localhost", port=19530)
    print("Healthcheck:", healthcheck(url="http://localhost:9091/healthz"))

    print("Creating collection...")
    schema: CollectionSchema = CollectionSchema(fields=[
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
        FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=100),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384)])
    index: Index = Index(field_name=DEFAULT_EMBEDDING_FIELD, index_type=IndexType.FLAT, metric_type=MetricType.IP)
    collection: Collection = create_collection(name="quotes", schema=schema, index=index)
    print("Collections:", list_collections())

    print("Inserting data...")

    def create_embeddings(texts: list[str]) -> list[list[float]]:
        model: SentenceTransformer = SentenceTransformer(model_name_or_path="all-MiniLM-L6-v2")
        embeddings: np.ndarray = model.encode(texts)
        return embeddings.tolist()

    data = pa.table(data={
        "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "content": [
            "Be the change you wish to see in the world.",
            "The only way to do great work is to love what you do.",
            "Life is what happens when you're busy making other plans.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "The only limit to our realization of tomorrow is our doubts of today.",
            "It does not matter how slowly you go as long as you do not stop.",
            "The journey of a thousand miles begins with one step.",
            "What you get by achieving your goals is not as important as what you become by achieving your goals.",
            "The mind is everything. What you think you become.",
        ]})
    data_with_embeddings: pa.Table = pa.table(data={
        "id": data["id"],
        "content": data["content"],
        "embedding": create_embeddings(data["content"].to_pylist())})
    milvus_data: list[dict] = []
    for i in range(len(data_with_embeddings)):
        row: dict = {
            "id": data_with_embeddings["id"][i].as_py(),
            "content": data_with_embeddings["content"][i].as_py(),
            "embedding": data_with_embeddings["embedding"][i].as_py()
        }
        milvus_data.append(row)
    insert_data(collection=collection, data=milvus_data)

    print("Searching...")
    question: str = "What is the meaning of life?"
    question_embedding: list[float] = create_embeddings([question])[0]
    results: list[dict] = search(
        collection=collection, query_vector=question_embedding, search_field=DEFAULT_EMBEDDING_FIELD,
        params={"params": {"nprobe": 10}}, limit=2, output_fields=["content"])
    print("Search results:", results)


if __name__ == "__main__":
    main()
