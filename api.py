import requests

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

def make_graphql_request(url, query):
    try:
        # Create a dictionary with the GraphQL query
        data = {
            'query': query
        }

        # Perform a POST request to the GraphQL API
        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()
            return result
        else:
            print(f"Request failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    result = make_graphql_request(API_URL, QUERY)
    if result:
        print(result)
