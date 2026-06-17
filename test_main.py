from fastapi.testclient import TestClient
from main import app

# Create a test client to interact with the API without running the server
client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Learn CI/CD", "done": False},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Learn CI/CD"
    assert data["done"] is False


def test_get_tasks_grows():
    # Check initial number of tasks
    initial_response = client.get("/tasks")
    initial_count = len(initial_response.json())

    # Add a new task
    client.post("/tasks", json={"title": "Write Tests"})

    # Check tasks again and ensure the list has grown by 1
    new_response = client.get("/tasks")
    new_count = len(new_response.json())
    assert new_count == initial_count + 1


def test_create_task_empty_title_fails():
    # Send a request with an empty title
    response = client.post("/tasks", json={"title": "   "})

    # Assert that it returns a 400 Bad Request error
    assert response.status_code == 400
    assert response.json()["detail"] == "Title cannot be empty"
