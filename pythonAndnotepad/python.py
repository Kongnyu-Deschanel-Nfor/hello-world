import requests
url='https://en.wikipedia.org/w/api.php'
params = {
    "action": "query",
    "format": "json",
    "titles": "flood",
    "prop": "extracts",
    "exintro": "disaster",
    "explaintext": "disaster"
}

response=requests.get(url,params=params);
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    page_id = next(iter(data["query"]["pages"]))
    content = data["query"]["pages"][page_id]["extract"]
    print(data)
    print(content)
   
else:
    print("Error: Failed to fetch data from Wikipedia.")


