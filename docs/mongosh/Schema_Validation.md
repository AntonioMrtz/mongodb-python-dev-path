# Schema validation

MongoDB schema validation allows us to enforce rules on documents within a collection, ensuring data consistency.

* Skipping validation during the **early stages** of development can speed up the process..
* Once our data model is **established**, we can enforce validations to ensure data consistency.

## Validator

Based on [json schema](https://json-schema.org/).

### Applied validator on creation

```json
db.createCollection("sales", {
    validator: {
      "$and": [
        {
          "$expr": {
            "$lt": ["$items.discountedPrice", "$items.price"]
          }
        },
        {
          "$jsonSchema": {
            "properties": {
              "items": { "bsonType": "array" }
            }
           }
         }
       ]
     }
   }
 )
```
### Applied validator after creation

Objects created before enforcing the validator won't be affected by new validations.

```js
db.runCommand({
    collMod: "reviews", // collection to modify
    validator: bookstore_reviews_default, // validator specified in the example below
    validationLevel: "strict",
    validationAction: "error", // rejects operation
});
```

### Check non validated documents

```js
db.collection.find( { $nor: [ validator ] } )
```


## Validation mode

Specifies when rules are applied.

* **Strict**: rejects any document that do not match the validation.
* **Moderate**: only validate fields that match the schema but not extra fields.

## Validation actions

What needs to be done after validation fails.

* **Warn**. Logs a warning but the operation is resolved.
* **Error**. Rejects operation.

## Validator example

```js
const bookstore_reviews_default = {
    $jsonSchema:{
        bsonType: "object", // type of the field
        required: [“_id”, "review_id", "user_id", "timestamp", "review", "rating"], // required fields
        additionalProperties: false, // can't add new properties that are not listed
        properties: {
            _id: { bsonType: "objectId" },
            review_id: { bsonType: "string" },
            user_id: { bsonType: "string" },
            timestamp: { bsonType: "date" },
            review: { bsonType: "string" },
            rating: {
                bsonType: "int",
                minimum: 0,
                maximum: 5,
            },
            comments: {
                bsonType: "array",
                maxItems: 3,
                items: {
                    bsonType: "object",
                },
            },
        },
    }
};
```

