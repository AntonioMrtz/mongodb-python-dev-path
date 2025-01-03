# Modifying query results Operations

## Sorting and Limiting Query Results

### Sort

We specify the query and then a field that contains the parameter to sort with the following flag:

* 1: ascending order
* -1: descending order

```ts
db.collection.find(<query>).sort(<sort>)
```

```ts
db.companies.find({ category_code: "music" }).sort({ name: 1,_id: 1 });
```

### Limit

We specify the maximum results we want to get from a query:

```ts
db.companies.find(<query>).limit(<number>)
```

```ts
db.companies
  .find({ category_code: "music" })
  .sort({ number_of_employees: -1, _id: 1 })
  .limit(3);
```
### Skip

Skips certain number of documents in a query result. Useful por pagination.

```ts
db.products.find().skip(2);
```
If the previous query is runned with the followind dataset:

```ts
[
  { _id: 1, name: "Laptop", price: 1000 },
  { _id: 2, name: "Mouse", price: 20 },
  { _id: 3, name: "Keyboard", price: 50 },
  { _id: 4, name: "Monitor", price: 300 },
  { _id: 5, name: "Headphones", price: 80 }
]
```

We will get:

```ts
[
  { _id: 3, name: "Keyboard", price: 50 },
  { _id: 4, name: "Monitor", price: 300 },
  { _id: 5, name: "Headphones", price: 80 }
]
```


## Returning Specific Data from a Query

### Projections

Projections allow us to determine which fields we want to retrieve from a query result. We cannot exclude and include fields in the same projection, except if the `_id` field.

```ts
db.collection.find( <query>, <projection> )
```


#### Include

We can include fields in the result using a projection `{field_name:1}`:

```ts
db.inspections.find(
  { sector: "Restaurant - 818" },
  { business_name: 1, result: 1 }
)
```

#### Exclude

We can exclude fields in the result using a projection `{field_name:0}`:

```ts
db.inspections.find(
  { result: { $in: ["Pass", "Warning"] } },
  { date: 0, "address.zip": 0 }
)
```

## Counting Documents in a Collection

Count number of documents that match a specify query:

```ts
db.trips.countDocuments({ tripduration: { $gt: 120 }, usertype: "Subscriber" })
```