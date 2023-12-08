import requests

def client():
    # credentials = {"username": "venkatesh", "password": "venkatesh"}

    # response = requests.post("http://127.0.0.1:8000/api/dj-rest-auth/login/",
    #                          data=credentials)

    token_h = "Token dafc774edf6ed1ff7e47acb1b14db1a934feb7be"
    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print("Status Code: ", response.status_code)
    
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()