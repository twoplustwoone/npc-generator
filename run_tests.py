import os
import subprocess

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))
    pytest_command = ["pytest", "tests/"]

    env = os.environ.copy()
    env["PYTHONPATH"] = project_root

    # Run pytest
    result = subprocess.run(pytest_command, env=env)
    exit(result.returncode)

if __name__ == "__main__":
    main()
