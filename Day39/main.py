import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
user_name = os.getenv("USERNAME")
token = os.getenv("TOKEN")
endpoint = os.getenv("ENDPOINT")
parameters = {
    "token": token,
    "username":user_name,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


GRAPH_ENDPOINT = f"{endpoint}/{user_name}/graphs"
graph_header ={
    "X-USER-TOKEN":token
}
graph_id = "abcd1234"
graph_parameters = {
    "id":graph_id,
    "name":"Learning",
    "unit":"time",
    "type":"int",
    "color":"shibafu"
    # "timezone":"Asia/Tokyo",
    # "description":"This is a graph for test."
}

present = datetime.now()
pixel_update ={
    "quantity":"4"
}
pixel_data = {
    "date":present.strftime("%Y%m%d"),
    "quantity":input("How much time did you spend on learning today?: ")
}

graph_update = f"{GRAPH_ENDPOINT}/{graph_id}"
graph_response = requests.post(url=graph_update,json=pixel_data,headers=graph_header)
# graph_response = requests.post(url=graph_update,json=pixel_data,headers=graph_header)
# graph_response = requests.put(url=f"{GRAPH_ENDPOINT}/{graph_id}/{today}",json=pixel_update,headers=graph_header)
# graph_response = requests.delete(url=f"{GRAPH_ENDPOINT}/{graph_id}/{today}",headers=graph_header)
print(graph_response.text)
print(f'LOOK AT THE OUTPUT AT: https://pixe.la/v1/users/junior009/graphs/abcd1234.html ')



