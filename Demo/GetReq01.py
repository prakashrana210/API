

import requests as req
import json
import jsonpath as jp

"""using get method and saving response"""
response = req.get("https://reqres.in/api/user?page=2")

"""converting response content into json"""
json_text = json.loads(response.content)

"""using JSON path to get specific value"""
result_list = jp.jsonpath(json_text, 'data[0].id')

print('response is', response.content, '\nFirst ID is ', result_list)

"""assert on the extracted value"""
assert result_list[0] == 7


# import requests as req
# import json
# import jsonpath as jp
#
# """getting response and saving"""
# response = req.get("https://reqres.in/api/users?page=2")
#
# """converted response into json format"""
# json_text = json.loads(response.content)
#
# """using jsonpath to get the specific value"""
# result_list = jp.jsonpath(json_text, 'data[0].id')
#
# print('response is', response.content, '\nFirst id is', result_list)


# assert result_list[0] == 7
# #or we can also use
# assert response.status_code == 200


