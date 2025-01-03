# Delete Operations

## Delete One Document

```ts
db.podcasts.deleteOne({ _id: Objectid("6282c9862acb966e76bbf20a") })
```

## Delete Many Documents

```ts
db.podcasts.deleteMany({category: “crime”})
```

## Find one and delete

```ts
db.collection.findOneAndDelete({city : {$in : ["CHICAGO"] }})
```