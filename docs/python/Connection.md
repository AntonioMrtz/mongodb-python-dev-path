# Database Connection

## URI format

### Localhost

```
MONGODB_URI= mongodb://root:root@127.0.0.1:27017/
```

### Atlas

```
MONGODB_URI= mongodb+srv://user:password@cluster0.mongodb.net/
```

## Connect to database

```py
import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)
```

## List databases

```py
# List all the databases in the cluster:
for db_info in client.list_database_names():
   print(db_info)
```

## Get reference to database and list its collections

```py
# Get a reference to the 'sample_mflix' database:
db = client['sample_mflix']

# List all the collections in 'sample_mflix':
collections = db.list_collection_names()
for collection in collections:
   print(collection)
```