import requests
import datetime as dt
USERNAME = "zero1"
TOKEN = "abcd1234"
GRAPH_ID = "graph0"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hr",
    "type": "float",
    "color": "kuro"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

day = dt.datetime.now()
day = day.strftime(f'%Y%m%d')
pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_parameters = {
    "date": day,
    "quantity": input("How many hours did you code today?")
}

response = requests.post(url=pixel_create_endpoint, json=pixel_parameters, headers=headers)
print(response.text)

# update_pixel_endpoint = f"{pixel_create_endpoint}/{day}"
# new_pixel_data = {
#     "quantity": "5"
# }
# response = requests.put(url=update_pixel_endpoint,json=new_pixel_data, headers=headers)
# print(response.text)


# delete request
# delete_pixel_endpoint = update_pixel_endpoint
# response = requests.put(url=update_pixel_endpoint,headers=headers)
# print(response.text)