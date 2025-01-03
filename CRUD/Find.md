# Find Operations

## Find documents

### Find only one document

```ts
db.collection.findOne({_id:ObjectID("id")})
```

### With equality

```ts
db.collection.find({_id:ObjectID("id")})
```

### With $in operator

```ts
db.collection.find({city : {$in : ["CHICAGO"] }})
```

### Finding Documents by Using Comparison Operators

* `$gt` - Greater than
* `$lt` - Less than
* `$gte` - Greater or equal than 
* `$lte` - Less or equal than

```ts
db.sales.find({ "items.price": { $gt: 50}})
```

## Quering on array elements

### Find Documents with an Array That Contains a Specified Value

Matches any document where the products field is an array and "InvestmentFund" is an element in that array.

```ts
db.accounts.find({ products: "InvestmentFund"})
```

### Find a Document using $elemMatch

Matches any document that contains a item in that field that validates all the conditions.

```ts
db.sales.find({
  items: {
    $elemMatch: { name: "laptop", price: { $gt: 800 }, quantity: { $gte: 1 } },
  },
})
```

## Finding Documents by using Logical Operators

### Implicit $and

```ts
db.routes.find({ "airline.name": "Southwest Airlines", stops: { $gte: 1 } })
```

### $or

```ts
db.routes.find({
  $or: [{ dst_airport: "SEA" }, { src_airport: "SEA" }],
})
```

### $and

```ts
db.routes.find({
  $and: [
    { $or: [{ dst_airport: "SEA" }, { src_airport: "SEA" }] },
    { $or: [{ "airline.name": "American Airlines" }, { airplane: 320 }] },
  ]
})
```