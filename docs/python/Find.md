# Find Operations

## find_one

```py
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)
```

## find

```py
# Query
documents_to_find = {"balance": {"$gt": 4700}}

# Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
print("# of documents found: " + str(num_docs))
```