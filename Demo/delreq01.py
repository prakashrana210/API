import requests as req

response = req.delete("https://reqres.in/api/users/2")

assert response.status_code == 204

