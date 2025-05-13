import requests

class AuthClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        return requests.post(f"{self.base_url}/login", json=payload)
