import os

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {os.getenv('BASIC_TOKEN')}",
}