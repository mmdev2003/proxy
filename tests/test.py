import requests

first_backend = "http://5.35.98.67"


def check_domain():
    body = {
        "public_domain": "gpt",
        "path": "/",
        "request_type": "GET",
        "body": {"key": '3'},
        "headers": {"key": '4'},
        "cookies": {"key": '5'}
    }
    path = "/api/check_domain"
    res = requests.post(f"{first_backend}{path}", json=body)

    print(res.json())


check_domain()
