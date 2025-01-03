# Insert Operations

## insert_one

```python
new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": "MDB829001337",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.datetime.utcnow(),
}

# Write an expression that inserts the 'new_account' document into the 'accounts' collection.
result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id
```
## insert_many

```python
new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": "MDB829001337",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.datetime.utcnow(),
}

other_acc = {
    "test":1
}

# Write an expression that inserts the 'new_account' document into the 'accounts' collection.
result = accounts_collection.insert_many([new_account,other_acc])

document_ids = result.inserted_ids
print(f"_ids of inserted documents: {document_ids}")
```