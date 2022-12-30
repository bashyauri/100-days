import requests
from datetime import *
USERNAME = "bashar"
TOKEN = "agsaddgsdgdggdjshdsj"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.reason)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",

}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
dt = datetime.now()
TODAY = dt.strftime('%Y%m%d')
QUANTITY = "3"


pixel_post_config = {
    "date": TODAY,
    "quantity": QUANTITY,
}


post_pixel_url = f"{graph_endpoint}/{graph_config['id']}"
response = requests.post(
    post_pixel_url, json=pixel_post_config, headers=headers)
print(response.text)
