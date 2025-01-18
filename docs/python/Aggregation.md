# Aggregation

```py
# Create an aggegation pipeline using 'stage_match_balance' and 'stage_group_account_type'.
pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance,
]

results = accounts_collection.aggregate(pipeline)
```

## Match

```py
select_by_balance = {"$match": {"balance": {"$lt": 1000}}}
```

## Group

```py
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}
```

## Sort

```py
# Organize documents in order from highest balance to lowest.
organize_by_original_balance = {"$sort": {"balance": -1}}
```

## Project

```py
# Return only the account type & balance fields, plus a new field containing balance in Great British Pounds (GBP).
return_specified_fields = {
    "$project": {
        "account_type": 1,
        "balance": 1,
        "gbp_balance": {"$divide": ["$balance", conversion_rate_usd_to_gbp]},
        "_id": 0,
    }
}
```