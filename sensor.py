import requests
import time
from datetime import datetime


# set up the Django REST API endpoint
API_ENDPOINT = 'http://localhost:8000/gateway/devices/'

# define the device data
device_data = {
    "name": "Device1",
    "serial_number":"006",
    "location": "Room 101",
    "temperature": 25.5,
    "humidity": 40.2
}
# authenticate and get an access token

username = 'test1'
password='test1234*'
    # add any additional authentication fields here
auth = (username, password)

# send a POST request to create the device
response = requests.post(API_ENDPOINT, data=device_data, auth=auth)

if response.status_code == 201:
    print('Device created successfully')
    device_id = response.json().get('id')
else:
    print(f'Error creating device: {response.text}')
    exit()

# simulate data updates at regular intervals
while True:
    # generate some sample data for the device
    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    device_data = {
        "device": device_id,
         "timestamp": timestamp_str,
        "temperature": 25.5,
        "humidity": 40.2,
    }
    # send a PUT request to update the device data
    update_url = f'{API_ENDPOINT}{device_id}/addvalue/'

    update_response = requests.put(update_url, data=device_data, auth=auth)
    #
    if update_response.status_code == 200:
        print(f'Data update successful: {update_response.json()}')
    else:
        print(f'Error updating data: {update_response.text}')

    # wait for some time before sending the next data update
    time.sleep(5)  # send data update every 60 seconds
