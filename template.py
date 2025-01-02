from pymongo import MongoClient

MONGODB_URI = "mongodb://root:root@127.0.0.1:27017/"

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

## List databases

# List all the databases in the cluster:
for db_info in client.list_database_names():
    print(db_info)
