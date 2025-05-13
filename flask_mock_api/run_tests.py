import subprocess
import os
import shutil

base_dir = os.path.abspath(os.path.dirname(__file__))
results_dir = os.path.join(base_dir, "reports", "allure-results")
report_dir = os.path.join(base_dir, "reports", "allure-report")
history_dir = os.path.join(base_dir, "reports", "allure-history")

# 1. Clean old results
for path in [results_dir, report_dir]:
    if os.path.exists(path):
        shutil.rmtree(path)

# 2. Run tests with Allure result output
subprocess.run(["pytest", f"--alluredir={results_dir}"], check=True)

# 3. Copy history if it exists (for trends)
history_source = os.path.join(history_dir, "history")
if os.path.exists(history_source):
    shutil.copytree(history_source, os.path.join(results_dir, "history"), dirs_exist_ok=True)

# 4. Generate the new Allure report
subprocess.run([
    "allure", "generate", results_dir, "-o", report_dir, "--clean"
], check=True)

# 5. Save current report history for the next run
generated_history = os.path.join(report_dir, "history")
if os.path.exists(generated_history):
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)
    shutil.copytree(generated_history, os.path.join(history_dir, "history"), dirs_exist_ok=True)

