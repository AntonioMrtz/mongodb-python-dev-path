# Insert Operations

## Insert one document

```ts
db.collection.insertOne({
  student_id: 654321,
  products: [
    {
      type: "exam",
      score: 90,
    },
    {
      type: "homework",
      score: 59,
    },
    {
      type: "quiz",
      score: 75,
    },
    {
      type: "homework",
      score: 88,
    },
  ],
  class_id: 550,
})
```

## Insert many documents

```ts
db.collection.insertMany([{student_id: 654321},{student_id: 777,}])
```