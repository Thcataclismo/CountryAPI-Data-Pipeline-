import pymongo

def connect_to_mongodb(uri):
    try:
        client = pymongo.MongoClient(uri)
        db = client["mydatabase"]
        return db
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

if __name__ == "__main__":
    db = connect_to_mongodb()
    if db:
        print("Successfully connected to MongoDB!")
        db.client.close()
    else:
        print("Failed to connect to MongoDB. Please check the configuration.")
