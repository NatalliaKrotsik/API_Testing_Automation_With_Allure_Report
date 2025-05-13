import requests

class PostClient:
    def __init__(self, base_url):
        self.base_url = base_url 

    def get_post(self, post_id):
        return requests.get(f"{self.base_url}/posts/{post_id}")

    def create_post(self, data):
        return requests.post(f"{self.base_url}/posts", json=data)
    def delete_post(self, post_id):
        return requests.delete(f"{self.base_url}/posts/{post_id}")
    
    def create_post(self, title, body, user_id):
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return requests.post(f"{self.base_url}/posts", json=payload)

    def get_post(self, post_id):
        return requests.get(f"{self.base_url}/posts/{post_id}")
