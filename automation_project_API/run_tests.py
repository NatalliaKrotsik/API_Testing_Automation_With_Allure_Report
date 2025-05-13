import subprocess

# Run tests and collect results
subprocess.run(["pytest", "--alluredir=reports/allure-results"], check=True)

# Generate report
subprocess.run(["allure", "generate", "reports/allure-results", "-o", "reports/allure-report", "--clean"], check=True)

# Open report
subprocess.run(["allure", "open", "reports/allure-report"], check=True)
