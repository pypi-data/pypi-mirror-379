"""Test data insertion utilities for E2E tests."""

from typing import Any

from pymongo import MongoClient
from pymongo.database import Database


def generate_nested(level: int, base_value: int = 100) -> dict[str, Any]:
    """
    Recursively generate a nested document to the specified depth.

    Parameters
    ----------
    level : int
        Nesting depth to generate
    base_value : int, optional
        Base value to use for calculations, by default 100

    Returns
    -------
    dict[str, Any]
        A nested dictionary with predictable values at the deepest level.
    """
    if level <= 0:
        return {"value": base_value + (level * 10)}
    return {"level": level, "child": generate_nested(level - 1, base_value)}


def insert_test_data(
    uri: str = "mongodb://admin:password@localhost:27017/mongoex_integration_test?authSource=admin",
    db_name: str = "mongoex_integration_test",
    collection_name: str = "complex_data",
) -> None:
    """
    Insert predictable test data into MongoDB for E2E tests.

    Parameters
    ----------
    uri : str
        MongoDB connection URI
    db_name : str
        Database name to use
    collection_name : str
        Collection name to write data to
    """
    client: MongoClient[dict[str, Any]] = MongoClient(uri)
    db: Database[dict[str, Any]] = client[db_name]
    collection = db[collection_name]

    # Clean existing data
    collection.drop()

    # Generate predictable test data
    documents: list[dict[str, Any]] = []
    for level in range(1, 4):  # 3 levels of complexity
        for idx in range(5):  # 5 documents per level
            base_value = 100 + (level * 50) + (idx * 10)
            nested_doc = generate_nested(level, base_value)

            document: dict[str, Any] = {
                "complexity_level": level,
                "nested": nested_doc,
                "index": idx,
                "category": f"category_{level}",
                "active": idx % 2 == 0,  # Alternating boolean
                "score": float(base_value + idx),
            }
            documents.append(document)

    collection.insert_many(documents)
    print(
        f"✅ Inserted {len(documents)} test documents into {db_name}.{collection_name}"
    )
    client.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Insert test data into MongoDB")
    parser.add_argument(
        "--uri",
        default="mongodb://admin:password@localhost:27017/mongoex_integration_test?authSource=admin",
    )
    parser.add_argument("--db", default="mongoex_integration_test")
    parser.add_argument("--collection", default="complex_data")

    args = parser.parse_args()
    insert_test_data(args.uri, args.db, args.collection)
