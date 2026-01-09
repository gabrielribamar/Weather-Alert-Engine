import requests

url = "https://api.sportmonks.com/v3/football/players"
params = {
    "locale": "pt"
}
eaders = {
    53
    }

response = requests.get(url, params=params, headers=eaders)
data = response.json()
print(data.keys())
print(data['data'])



