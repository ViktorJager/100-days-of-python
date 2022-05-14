from email import header
import requests
from datetime import datetime


USERNAME = "groteskovilja"
TOKEN = "asdyugf89s7fghs23rasdfsd"
headers = {"X-USER-TOKEN": TOKEN}

# Create user
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Kindle Reading Tracker",
    "unit": "pages",
    "type": "int",
    "color": "momiji",
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post a pixel entry
todays_date = datetime.today().strftime("%Y%m%d")
post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
post_pixel_config = {
    "date": "20220512",
    "quantity": "150",
}
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(response.text)

# Update pixel entry
update_pixel_endpoint = f"{post_pixel_endpoint}/{todays_date}"
update_pixel_config = {
    "quantity": "100",
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# Delete a pixel entry
delete_endpoint = update_pixel_endpoint
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
