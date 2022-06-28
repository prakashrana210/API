# import requests as req
# import jsonpath as jp
#
# url = "https://reqres.in/api/users"
#
# """opening file and reads the data into variable"""
# with open('post_request.json', 'r') as i:
#     input_content = i.read()
#
# """post request using url and post request content"""
# response = req.post(url, input_content)
#
# """assert for successful posting"""
# assert response.status_code == 201
# print(201)
#
# """taking response as a file for evidence"""
# with open('post_response.json', 'w') as f:
#     f.write(response.text)


import requests as req

url = "https://reqres.in/api/users"

with open('post_request.json', 'r') as i:
    input_content = i.read()

response = req.post(url, input_content)

assert response.status_code == 201

with open('post_response.json', 'w') as f:
    f.write(response.text)

