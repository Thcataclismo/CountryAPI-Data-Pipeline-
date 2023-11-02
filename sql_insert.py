import pymongo

def insert_data_into_mongodb(data):
    try:
        client = pymongo.MongoClient("")
        db = client[""]
        collection = db[""]

        for item in data:
            collection.insert_one(item)

        print("Data successfully inserted into MongoDB!")

    except pymongo.errors.ConnectionFailure as e:
        print(f"MongoDB connection error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    data_to_insert = [
        {'name': 'Saint Vincent and the Grenadines', 'capital': 'Kingstown', 'code': 'VC', 'currency': 'XCD'},
        {'name': 'Venezuela', 'capital': 'Caracas', 'code': 'VE', 'currency': 'VES'},
    ]

    insert_data_into_mongodb(data_to_insert)
