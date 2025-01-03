# Bulk Write Operation

```py
requests = [
    InsertOne({"name": "John", "age": 30}),
    InsertOne({"name": "Alice", "age": 25}),
    UpdateOne({"name": "John"}, {"$set": {"age": 31}}),
    DeleteOne({"name": "Alice"})
]

try:
    result = collection.bulk_write(requests)
    print(f"Bulk write result: {result.bulk_api_result}")
except BulkWriteError as bwe:
    print(f"Bulk write error: {bwe.details}")
```