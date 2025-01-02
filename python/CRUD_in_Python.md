# CRUD OPerations in Python

## Lesson 2: Inserting a Document in Python Applications

### insert_one

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
### insert_many

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

## Lesson 3: Querying a Collection in Python Applications

### find_one

```py
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)
```

### find

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

## Lesson 4: Updating Documents in Python Applications

### update

```py
# Filter
document_to_update = {"_id": ObjectId("62d6e04ecab6d8e130497482")}

# Update
add_to_balance = {"$inc": {"balance": 100}}

# Write an expression that adds to the target account balance by the specified amount.
result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Documents updated: " + str(result.modified_count))
```

### update_many

```py
# Filter
select_accounts = {"account_type": "savings"}

# Update
set_field = {"$set": {"minimum_balance": 100}}

# Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
```

## Lesson 5: Deleting Documents in Python Applications

### delete_one

```py
document_to_delete = {"_id": ObjectId("62d6e04ecab6d8e130497485")}

result = accounts_collection.delete_one(document_to_delete)

print("Documents deleted: " + str(result.deleted_count))
```

### delete_many

```py
documents_to_delete = {"balance": {"$lt": 2000}}

result = accounts_collection.delete_many(document_to_delete)

print("Documents deleted: " + str(result.deleted_count))
```

## Lesson 6: Creating MongoDB Transactions in Python Applications

* Transactions that take longer than 60s will be cancelled
* It any operations fail the transaction won't be completed and no changes will be made

```py
# Step 1: Define the callback that specifies the sequence of operations to perform inside the transactions.
def callback(
    session,
    transfer_id=None,
    account_id_receiver=None,
    account_id_sender=None,
    transfer_amount=None,
):

    # Get reference to 'accounts' collection
    accounts_collection = session.client.bank.accounts

    # Get reference to 'transfers' collection
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount},
    }

    # Transaction operations
    # Important: You must pass the session to each operation

    # Update sender account: subtract transfer amount from balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Update receiver account: add transfer amount to balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Add new transfer to 'transfers' collection
    transfers_collection.insert_one(transfer, session=session)

    print("Transaction successful")

    return


def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR218721873",
        account_id_receiver="MDB343652528",
        account_id_sender="MDB574189300",
        transfer_amount=100,
    )


# Step 2: Start a client session
with client.start_session() as session:
    # Step 3: Use with_transaction to start a transaction, execute the callback, and commit (or cancel on error)
    session.with_transaction(callback_wrapper)
```

Using lambda expression is recommended:


```py
with client.start_session() as session:
    # Step 3: Use with_transaction with a lambda function
    session.with_transaction(
        lambda s: (
            # Transaction operations within the lambda
            s.client.bank.accounts.update_one(
                {"account_id": account_id_sender},
                {
                    "$inc": {"balance": -transfer_amount},
                    "$push": {"transfers_complete": transfer_id},
                },
                session=s,
            ),
            s.client.bank.accounts.update_one(
                {"account_id": account_id_receiver},
                {
                    "$inc": {"balance": transfer_amount},
                    "$push": {"transfers_complete": transfer_id},
                },
                session=s,
            ),
            s.client.bank.transfers.insert_one(
                {
                    "transfer_id": transfer_id,
                    "to_account": account_id_receiver,
                    "from_account": account_id_sender,
                    "amount": {"$numberDecimal": transfer_amount},
                },
                session=s,
            ),
            print("Transaction successful")
        )
    )
```