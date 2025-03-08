# MongoDB `$lookup` - Left Outer Join

## Overview
The **`$lookup`** stage in MongoDB’s aggregation pipeline performs a **left outer join** between two collections. This allows you to **combine related documents** from different collections based on a common field, similar to SQL joins.

In this example, we retrieve an **author** and all the **books written by that author**.

## Sample Collections

### **`authors_collection` (Main Collection)**
Each document represents an **author**:
```json
{
    "_id": 2,
    "name": "J.K. Rowling"
}
```

### **`books_collection` (Joined Collection)**
Each document represents a **book** and contains an `author_id` field linking it to an author:
```json
{
    "_id": 1,
    "author_id": 2,
    "title": "Harry Potter"
}
```


## Aggregation Query
To retrieve an **author and their books**, use the following **MongoDB aggregation pipeline**:

```js
db.authors_collection.aggregate([
  {
    $match: {
      _id: 2 // Filter to get the author with _id: 2
    },
  },
  {
    $lookup: {
      from: "books_collection",  // The collection to join (books)
      localField: "_id",         // Field in authors_collection (_id)
      foreignField: "author_id", // Field in books_collection (author_id)
      as: "books"                // Output field where matched books will be stored
    },
  },
]);
```


## Expected Output
If the author exists and has written books, the output will include the **author’s details** along with a list of their books in the `"books"` array:

```json
[
  {
    "_id": 2,
    "name": "J.K. Rowling",
    "books": [
      { "_id": 1, "author_id": 2, "title": "Harry Potter" }
    ]
  }
]
```

If no matching books are found, the `"books"` array will be **empty (`[]`)**, ensuring that the author record is still returned.

## Key Takeaways

✅ **Performs a left outer join** → All authors are included, even if they have no books.  
✅ **Combines documents using common fields** (`_id` in `authors_collection` and `author_id` in `books_collection`).  
✅ **Results are stored in an array (`as: "books"`)** → If no books exist for an author, `"books": []`.  