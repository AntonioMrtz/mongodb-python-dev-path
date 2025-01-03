# Update Operations

## Replacing a Document

Select the document to replace and insert all the new fields that it will have. The fields not inserted will stay the same. In the example `_id` will not change in the new document. It only works with one document, there's no `replace` or `replaceMany` method.

```ts
db.books.replaceOne(
  {
    _id: ObjectId("6282afeb441a74a98dbbec4e"),
  },
  {
    title: "Data Science Fundamentals for Python and MongoDB",
    isbn: "1484235967",
    publishedDate: new Date("2018-5-10"),
    thumbnailUrl:
      "https://m.media-amazon.com/images/I/71opmUBc2wL._AC_UY218_.jpg",
    authors: ["David Paper"],
    categories: ["Data Science"],
  }
)
```

## Updating Documents by Using updateOne()

The `updateOne()` method accepts a filter document, an update document, and an optional options object. MongoDB provides update operators and options to help you update documents. In this section, we'll cover three of them: `$set`, `upsert`, and `$push`.

### $set

Replaces field with a value

```ts
db.podcasts.updateOne(
  {
    _id: ObjectId("5e8f8f8f8f8f8f8f8f8f8f8"),
  },

  {
    $set: {
      subscribers: 98562,
    },
  }
)
```

### $upsert

If no document matches the filter a new one will be created

```ts
db.podcasts.updateOne(
  { title: "The Developer Hub" },
  { $set: { topics: ["databases", "MongoDB"] } },
  { upsert: true }
)
```

### $push

Add item to an array

```ts
db.podcasts.updateOne(
  { _id: ObjectId("5e8f8f8f8f8f8f8f8f8f8f8") },
  { $push: { hosts: "Nic Raboy" } }
)
```

## Updating Documents by Using findAndModify()

New option is specified if want to return the modified document. This query is useful because:

* Only one query instead of two
* Thread protecting if the field changed while finding and modifying the document. A value could be modified between our queries.

```ts
db.podcasts.findAndModify({
  query: { _id: ObjectId("6261a92dfee1ff300dc80bf1") },
  update: { $inc: { subscribers: 1 } },
  new: true,
})
```

## Updating Documents by Using updateMany()

* There's no rollback if some document update fails

```ts
db.books.updateMany(
  { publishedDate: { $lt: new Date("2019-01-01") } },
  { $set: { status: "LEGACY" } }
)
```