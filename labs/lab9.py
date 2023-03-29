import requests
URL = requests.get('http://localhost:3000/')
widgets = URL.json()
for i in widgets :
    print(f"{i['name']} - {i['color']}")
