from connection import connect_to_mongodb
from sql_insert import insert_data_into_mongodb
from api import make_graphql_request
#from api import QUERY, API_URL

# URL of the Countries GraphQL API
API_URL = 'https://countries.trevorblades.com/'

# Define your GraphQL query
QUERY = '''
{
  countries {
    name
    capital
    code
    currency
  }
}
'''

def main():
    # Make a GraphQL request
    result = make_graphql_request(API_URL, QUERY)

    # Check if the GraphQL request was successful
    if result:
        # Connect to MongoDB
        db = connect_to_mongodb()

        if db:
            print("Connection to MongoDB successful!")

            # Insert data into MongoDB
            insert_data_into_mongodb(db, result)

            # Close the MongoDB connection
            db.client.close()
        else:
            print("Failed to connect to MongoDB. Check the configuration.")

if __name__ == "__main__":
    main()
 




