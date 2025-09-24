import requests
import os

def download_package(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    data = response.json()

    # Find the first wheel file
    for file in data["urls"]:
        if file["filename"].endswith(".whl"):
            download_url = file["url"]
            filename = file["filename"]
            break
    else:
        raise Exception("No wheel file found.")

    # Download the wheel
    response = requests.get(download_url)
    with open(filename, "wb") as f:
        f.write(response.content)

    return os.path.abspath(filename)