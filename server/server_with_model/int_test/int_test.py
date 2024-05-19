import requests
import json

url = "http://localhost:8000/find_code"

payload = json.dumps({
    "code": "3f52bb3e-6f30-4e32-a1684-320d8dd6b209"
})
headers = {
    'username': 'admin',
    'password': 'Dinara06052002@',
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46RGluYXJhMDYwNTIwMDJA'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
