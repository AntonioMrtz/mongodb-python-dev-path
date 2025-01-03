# Bulk Write Operations

Allows to multiple write operations to be sent in a single query. Useful when handling high volume operations.

```ts
db.collection.bulkWrite(operations, options);
```

```ts
db.products.bulkWrite([
  {
    insertOne: {
      document: { _id: 1, name: "Laptop", price: 999, stock: 50 }
    }
  },
  {
    insertOne: {
      document: { _id: 2, name: "Mouse", price: 25, stock: 150 }
    }
  },])
```

### Supported operations

* insertOne: Inserts a single document.
* updateOne: Updates a single document.
* updateMany: Updates multiple documents.
* deleteOne: Deletes a single document.
* deleteMany: Deletes multiple documents.
* replaceOne: Replaces a document.