import requests

# endpoint = "https://httpbin.org/#/Status_codes"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/leave/" # local django server endpoint http://127.0.0.1:8000/

get_response = requests.post(endpoint, data={
    "employee_id": 123,
    "leave_type": "sick",
    "start_date": "2023-10-01",
    "end_date": "2023-10-05",
    "reason": "Flu"
})
print(get_response.text) # print the response text

# print(get_response.json()) # print the response json
#print(get_response.status_code)  # print the status code