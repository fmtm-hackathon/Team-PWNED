import requests

def download_overpass_turbo_geojson(query):
    url = 'https://overpass-api.de/api/interpreter'
    payload = {
        'data': query,
        'output': 'json'
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f'Request failed with status code {response.status_code}')
        return None

# Example Overpass Turbo query
query = '''
[out:json];
(
  way["building"="yes"](27.667276861070913,85.41924834251402,27.671775114740015,85.42418360710143);
);
out body;
>;
out skel qt;
'''

data = download_overpass_turbo_geojson(query)
if data:
    # Save the data to a GeoJSON file
    with open('output.geojson', 'w') as file:
        file.write(data)
    print('GeoJSON file downloaded successfully.')
else:
    print('Data download failed.')
