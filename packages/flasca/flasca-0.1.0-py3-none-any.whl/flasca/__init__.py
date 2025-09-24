import subprocess


def main() -> None:
    _initialize_uv_project()


def _initialize_uv_project():
    try:
        result = subprocess.run(
            ["uv", "init"], check=True, capture_output=True, text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'uv init': {e.stderr}")
