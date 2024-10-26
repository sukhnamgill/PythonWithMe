import requests

# URL of the IP-based geolocation service
url = 'https://ipinfo.io/json'

try:
    response = requests.get(url)
    data = response.json()

    # Extract latitude and longitude from location data
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]

    print(f"Latitude: {latitude}, Longitude: {longitude}")
except Exception as e:
    print("Error retrieving location:", e)

