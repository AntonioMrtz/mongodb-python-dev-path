# Aggregation

```ts
db.orders.aggregate([
  { $match: { category: "Stationery" } },
  { 
    $group: { 
      _id: null, 
      totalQuantity: { $sum: "$quantity" }, 
    } 
  }
]);
```

We can get value of a field by using `$fieldName`

```ts
db.collection.aggregate([
  {
    $set: {
      defaultUsername: {
        $concat: ["$first_name", " ", "$last_name"]
      }
    }
  }
]);
```

## $match

Find documents that match certain condition.

```ts
{
  $match: {
     "field_name": "value"
  }
}
```

## $group

Group documents by a field name. It will return one document per unique key. The _id field specifies which field we're using to group the data.

```ts
{
   $group: {
      _id: "$city",
      // group key
      totalZips: { $count : { } }
      // <field>: { <accumulator> : <expression> }
   }
}
```

## $sort

Sort documents in ascending/descending order by fields.

```ts
{
  $sort: {
      "field_name": 1 // 1 for ascending, -1 for descending order
  }
}
```

## $limit

Limit amount of returned documents.

```ts
{
  $limit: 5
}
```

## $project

Select fields for output document.

```ts
{
  $project:{

    field1:0, // do not include
    field2:1, // include
    field3: $field1
  
  }

}
```

## $set

Adds or modify fields on the pipeline.

```ts
{
  $set: {
      place: {
          $concat:["$city",",","$state"]
      },
      pop:10000
    }
  }
```

## $count

Count documents in the pipeline. Returns a document with only one field with the name that we set with the count output of the pipeline.

```ts
{
  $count:"returnField"
}
```

## $out

Writes output documents of pipeline into another collection. Must be the last stage of the pipeline.

### Using same database as the aggregation uses

```ts
{
  $out: "new_collection"
}
```
### Other database

```ts
{
  $out: {db:"new_collection",coll:"new_collection"}
}
```
