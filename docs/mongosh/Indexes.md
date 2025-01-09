# Indexes

## Lesson 1: Using Indexes in Collections 

### ✅ Benefits

- Improved reads by only checking documents that match the index, instead of checking every document.

### ❗ Drawbacks 

- Performance on writes descend as indexes need to be updated.
- More storage to store indexes.


### Types of index

- Single field: only one field is used as index.
- Compound: multiple fields of document are used as indexes.
- Multikey: index fields with an array key. llows for improved performance on checking attributes of objects inside an array. Example: given a student check if it has one grade that is less than 5. We can set grades as multikey index.


### Check indexes on collection

Retrieve all indexes of a colelction.

```ts
db.customers.getIndexes()
```

### Check if index is used in a query

Use `explain()` command before the query and if it shows `IXSCAN` on `FETCH` the query is using an index. It will also show which index is being used.

```ts
db.customers.explain().find({
  birthdate: {
    $gt:ISODate("1995-08-01")
    }
  })
``` 


## Lesson 2: Creating a Single Field Index


### Single field index creation

We must set a value for the index key: 1/-1 for ascending, descending order respectively.

```ts
db.customers.createIndex({
    birthdate: 1
})
```

### Single field unique index creation

If `unique` is set to true:

* Cannot create a document with a duplicated field value. It will throw an error upon insertion.

```ts
db.customers.createIndex({
  email: 1
},
{
  unique:true
})
```

## Lesson 3: Creating a Multikey Index

* Only one array field for index.

Given:

```ts
{   
    id: ...,
    accounts: [...]
}
```

We create the index as:

```ts
db.customers.createIndex({
  accounts: 1
})
```

## Lesson 4: Working with Compound Indexes in MongoDB 

Can be turned into `multikey Index` if one index is a field with an array.


```ts
db.customers.createIndex({
  active:1, 
  birthdate:-1,
  name:1
})
```

### Order of Fields in a Compound Index

The order of the fields matters when creating the index and the sort order. It is recommended to list the fields in the following order: Equality, Sort, and Range.

* Equality: field/s that matches on a single field value in a query
* Sort: field/s that orders the results by in a query
* Range: field/s that the query filter in a range of valid values -> $gte, etc. It doesnt mean .limit()

```ts
db.customers.find({
  birthdate: {
    $gte:ISODate("1977-01-01")
    },
    active:true
    }).sort({
      birthdate:-1, 
      name:1
      })
```

Here's an example of an efficient index for this query:

```ts
db.customers.createIndex({
  active:1, 
  birthdate:-1,
  name:1
})
```

If were getting fields from a query and they're not used for sort or filter, we should include them at the end of the query for better performance


## Lesson 5: Deleting MongoDB Indexes

Removing redundant or unused indexes can be useful. Restoring an index is more costly than simply hiding it, so hiding indexes is recommended.


### Hide

If not sure if the index is being used/

```ts
db.collection.hideIndex(<index>)
```

### Delete

An index for a field is redundant if the same field is on another multiple key index.

Example: `keyA_1 and keyA_1_keyB_1`. We can remove the first index.

#### One

```ts
db.customers.dropIndex(
  'active_1_birthdate_-1_name_1'
)
```

#### Multiple

```ts
db.collection.dropIndexes([
  'index1name', 'index2name', 'index3name'
  ])
```

#### All

```ts
db.customers.dropIndexes()
```
