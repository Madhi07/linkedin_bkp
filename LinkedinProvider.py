import requests
import os
from dotenv import load_dotenv
import logging
import traceback

logging.basicConfig(
    filename="user.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s  | %(filename)s:%(lineno)d | %(message)s",
)

load_dotenv(dotenv_path="myenv/.env")
BASE_URL = os.getenv("BASE_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
HOST = os.getenv("HOST")

class LinkedinProvider:
    def __init__(self):
        self.base_url = BASE_URL
        self.access_token = ACCESS_TOKEN
        self.host = HOST

    def url(self, path):
        return f"{self.base_url}{path}"

    def get(self, path, params=None):
        try:
            params = dict(params or {})
            headers = {
                "x-rapidapi-key": self.access_token,
                "x-rapidapi-host": self.host
            }
            response = requests.get(self.url(path), params=params, headers=headers)
            data = response.json()
            if response.status_code != 200:
                logging.error(f"Request error: {response.text}")
            else:
                logging.info(data)
                return data
        except Exception:
            logging.error(f"Generated error: {traceback.format_exc()}")

    def post(self, path, body=None):
        try:
            headers = {
                "x-rapidapi-key": self.access_token,
                "x-rapidapi-host": self.host,
                "Content-Type": "application/json"
            }
            response = requests.post(self.url(path), json=body or {}, headers=headers)
            data = response.json()
            if response.status_code != 200:
                logging.error(f"Request error: {response.text}")
            else:
                logging.info(data)
                return data
        except Exception:
            logging.error(f"Generated error: {traceback.format_exc()}")
