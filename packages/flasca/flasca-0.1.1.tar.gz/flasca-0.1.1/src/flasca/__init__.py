import argparse
import subprocess


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold Flask project using uv")
    parser.add_argument("name", help="Project name")
    args = parser.parse_args()

    project_name = args.name
    _initialize_uv_project(project_name=project_name)


def _initialize_uv_project(project_name: str):
    try:
        result = subprocess.run(
            ["uv", "init", "--package", project_name],
            check=True,
            capture_output=True,
            text=True,
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'uv init': {e.stderr}")
