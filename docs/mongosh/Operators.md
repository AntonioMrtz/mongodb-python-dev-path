# Operators

## $expr

Allows comparisons between fields of the same document.

```json
{
  "$expr": {
    "<aggregationOperator>": [ "<field1>", "<field2>" ]
  }
}
```

## $exists

Checks if a field exists

```json
{
  "field":{"$exists" : true}
}
```

## $rename

Rename a field

```json
{
  "$rename" : {"old_name":"new_name"}
}
```

## $set

Sets a field

```json
{
  "$set" : {"field":"value","field2":"value"}
}
```

## $unset

Removes a field

```json
{
  "$unset" : ["field1","field2"]
}
```
