import requests
request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    # print(response.status_code)
    if response.status_code==200:
        json_response=response.json()
        # print(json_response)
        print(json_response["value"])
except requests.exceptions.RequestException as e:
    print("Request couldn't be completed")