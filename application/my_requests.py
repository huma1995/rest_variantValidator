# import the requests module
import requests


# Create the class
class MyRequests:

    def __init__(self):
        self.base_url = None
        self.url = None

    # method that makes the call to the API using the get method
    def request_data(self):
        return requests.get(self.url)

    # method that assembles the url to request data from the hello endpoint
    def hello(self):
        self.url = f"{self.base_url}hello"
        return self.request_data()


if __name__ == "__main__":
    mrq = MyRequests()
    
    # Set the base url
    mrq.base_url = "http://127.0.0.1:5000/"
    
    # request the data
    response = mrq.hello()
    
    # print the 3 response sections
    print(response.status_code)
    print(response.headers)
    print(response.text)
    print(response.json())

    # Call the "name" endpoint with a specific name
    name_to_request = "Huma"  # Replace with the name you want to request
    response_name = mrq.get_name(name_to_request)

    # Print the response from the "name" endpoint
    print(f"Response from 'name' endpoint for '{name_to_request}':")
    print(response_name.status_code)
    print(response_name.headers)
    print(response_name.text)
    print(response_name.json())