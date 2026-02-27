import subprocess


def main():
    """Optional platform-agnostic script that just checks if uv is installed."""

    try:
        subprocess.run(["uv", "--help"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("""
uv not found. for installation instructions see:
https://docs.astral.sh/uv/getting-started/installation/
""")
    else:
        print("uv is installed and will automatically handle dependency installation. See README.md")


if __name__ == "__main__":
    main()
