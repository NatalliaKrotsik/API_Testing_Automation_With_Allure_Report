import subprocess
import time
import pytest
import requests
import os
import json
import shutil

ALLURE_RESULTS_DIR = "reports/allure-results"
ALLURE_REPORT_DIR = "reports/allure-report"


@pytest.fixture(scope="session", autouse=True)
def flask_app():
    """Start the Flask mock API server before running tests."""
    print("\n🚀 Starting Flask server for testing...")

    proc = subprocess.Popen(["python", "app.py"])

    # Wait until server is ready
    base_url = "http://127.0.0.1:5000/api"
    for _ in range(10):
        try:
            response = requests.get(f"{base_url}/ping")
            if response.status_code in [200, 404]:
                break
        except requests.exceptions.ConnectionError:
            time.sleep(0.5)
    else:
        proc.terminate()
        raise RuntimeError("❌ Flask server did not start in time.")

    yield

    print("\n🧹 Shutting down Flask server...")
    proc.terminate()


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the local Flask API."""
    return "http://127.0.0.1:5000/api"


def pytest_sessionstart(session):
    """Prepare Allure metadata before tests start."""
    os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)

    # Environment metadata
    with open(os.path.join(ALLURE_RESULTS_DIR, "environment.properties"), "w") as f:
        f.write("Environment=Localhost\n")
        f.write("Base URL=http://127.0.0.1:5000/api\n")
        f.write("Platform=Windows 11\n")
        f.write("Python=3.11\n")
        f.write("Tester=Natallia\n")

    # Failure categories
    categories = [
        {
            "name": "Assertion Error",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*AssertionError.*"
        },
        {
            "name": "Connection Error",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*ConnectionError.*"
        },
        {
            "name": "Timeout",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*Timeout.*"
        }
    ]
    with open(os.path.join(ALLURE_RESULTS_DIR, "categories.json"), "w") as f:
        json.dump(categories, f, indent=4)

    # Executor info
    executor = {
        "name": "Localhost",
        "type": "manual",
        "buildName": "Flask Mock API",
        "reportName": "API Test Suite with Flask"
    }
    with open(os.path.join(ALLURE_RESULTS_DIR, "executor.json"), "w") as f:
        json.dump(executor, f, indent=4)

    # Trend history
    if os.path.exists(os.path.join(ALLURE_REPORT_DIR, "history")):
        shutil.copytree(
            os.path.join(ALLURE_REPORT_DIR, "history"),
            os.path.join(ALLURE_RESULTS_DIR, "history"),
            dirs_exist_ok=True
        )
