import requests as req

url = "https://reqres.in/api/users/2"

"""read the data"""
with open("put_request.json", "r") as pu:
    input_content = pu.read()

"""convert the data"""
response = req.put(url, input_content)

assert response.status_code == 200

with open("put_response.json", "w") as f:
    f.write(response.text)


