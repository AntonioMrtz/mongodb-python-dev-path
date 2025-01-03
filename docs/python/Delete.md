# Delete Operations

## delete_one

```py
document_to_delete = {"_id": ObjectId("62d6e04ecab6d8e130497485")}

result = accounts_collection.delete_one(document_to_delete)

print("Documents deleted: " + str(result.deleted_count))
```

## delete_many

```py
documents_to_delete = {"balance": {"$lt": 2000}}

result = accounts_collection.delete_many(document_to_delete)

print("Documents deleted: " + str(result.deleted_count))
```