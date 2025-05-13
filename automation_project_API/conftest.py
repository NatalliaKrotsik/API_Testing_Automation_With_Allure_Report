import yaml
import pytest
import os
import json
import shutil

@pytest.fixture(scope="session")
def config():
    with open("config/settings.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """Generate Allure environment.properties automatically."""
    env_path = os.path.join("reports", "allure-results", "environment.properties")
    os.makedirs(os.path.dirname(env_path), exist_ok=True)
    with open(env_path, "w", encoding="utf-8") as f:
        f.write("Environment=Local\n")
        f.write("Base URL=http://127.0.0.1:5000\n")
        f.write("Platform=Windows 11\n")
        f.write("Python=3.11\n")
        f.write("Tester=Natallia\n")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Generate Allure executor.json and copy history for trend tracking."""
    if config.option.collectonly:
        return  # Skip in collect-only mode

    results_dir = os.path.join(os.getcwd(), "reports", "allure-results")
    report_dir = os.path.join(os.getcwd(), "reports", "allure-report")
    history_src = os.path.join(report_dir, "history")
    history_dst = os.path.join(results_dir, "history")

    os.makedirs(results_dir, exist_ok=True)

    # Copy history folder from previous report to enable trend
    if os.path.exists(history_src):
        shutil.copytree(history_src, history_dst, dirs_exist_ok=True)

    # Write executor.json
    executor_data = {
        "name": "Local Machine",
        "type": "manual",
        "buildName": "Local Test Run",
        "buildOrder": "1",
        "reportName": "API Automation by Natallia"
    }

    executor_file = os.path.join(results_dir, "executor.json")
    with open(executor_file, "w", encoding="utf-8") as f:
        json.dump(executor_data, f, indent=2)

    # Write categories.json
    categories_data = [
        {
            "name": "Product defects",
            "matchedStatuses": ["failed"],
            "messageRegex": ".*AssertionError.*"
        },
        {
            "name": "Test defects",
            "matchedStatuses": ["broken"],
            "messageRegex": ".*Exception.*"
        }
    ]

    categories_file = os.path.join(results_dir, "categories.json")
    with open(categories_file, "w", encoding="utf-8") as f:
        json.dump(categories_data, f, indent=2)
