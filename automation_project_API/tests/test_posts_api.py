import allure
import pytest
from api.clients.post_client import PostClient

@allure.epic("Post - Get - Delete - Get")
@allure.feature("POST")
@allure.title("Post")
def test_create_post(config):
    client = PostClient(config["api_base_url2"])
    new_post = {
        "title": "Automated Post",
        "body": "This is a test post created during automated testing.",
        "userId": 1
    }

    response = client.create_post(new_post)

    with allure.step("Verify post creation response"):
        assert response.status_code == 201
        assert response.json()["title"] == new_post["title"]
@allure.feature("GET /posts/{id}")
@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_post_by_id(config, post_id):
    client = PostClient(config["api_base_url2"])
    response = client.get_post(post_id)

    with allure.step(f"Verify post {post_id} exists"):
        assert response.status_code == 200
        assert response.json()["id"] == post_id

@allure.feature("Negative Test - GET /posts/{invalid_id}")
@pytest.mark.parametrize("invalid_id", [0, 101, "no-id"])
def test_get_invalid_post(config, invalid_id):
    client = PostClient(config["api_base_url2"])
    response = client.get_post(invalid_id)

    with allure.step(f"Verify 404 for invalid post ID: {invalid_id}"):
        assert response.status_code == 404
        assert response.text == "{}"
@pytest.mark.parametrize("post_id", [1, 5, 10])
@allure.feature("DELETE /posts/{post_id}")
@allure.title("Delete existing post by ID")
def test_delete_post(config, post_id):
    client = PostClient(config["api_base_url2"])
    response = client.delete_post(post_id)

    with allure.step(f"Delete existing post with ID: {post_id}"):
        assert response.status_code == 200
        assert response.text == "{}"
@pytest.mark.parametrize("invalid_id", [9999, "abc", -1])
@allure.feature("DELETE /posts/{invalid_id} - Simulated invalid deletes")
@allure.title("Attempt to delete non-existent or invalid posts")
def test_delete_invalid_post(config, invalid_id):
    client = PostClient(config["api_base_url2"])
    response = client.delete_post(invalid_id)

    with allure.step(f"Simulate deletion of non-existent post ID: {invalid_id}"):
        assert response.status_code == 200
        assert response.text == "{}"

@allure.feature("E2E: Create → Delete → (Optional) Verify Delete")
@allure.title("Simulate full flow of POST then DELETE a blog post")
def test_create_and_delete_post(config):
    client = PostClient(config["api_base_url"])

    # Step 1: Create a post
    with allure.step("Create a new post"):
        response_create = client.create_post("QA Automation Post", "This post is for delete testing.", 1)
        assert response_create.status_code == 201
        post_id = response_create.json().get("id")
        assert post_id is not None

    # Step 2: Delete the post
    with allure.step(f"Delete the created post with ID {post_id}"):
        response_delete = client.delete_post(post_id)
        assert response_delete.status_code == 200
        assert response_delete.text == "{}"

    # Step 3 (Optional): Try to retrieve the post
    with allure.step("Try to fetch deleted post (note: JSONPlaceholder does not persist deletes)"):
        response_get = client.get_post(post_id)
        assert response_get.status_code == 200
        # In a real API: assert response_get.status_code == 404