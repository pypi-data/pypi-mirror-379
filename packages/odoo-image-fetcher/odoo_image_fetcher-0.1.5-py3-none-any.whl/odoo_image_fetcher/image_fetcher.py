import os
import logging
import requests
from dotenv import load_dotenv
import urllib3
import io

# Suppress SSL warnings for this test
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ImageFetcher:
    _session = requests.Session()
    _base_url = os.getenv("ODOO_BASE_URL", "").rstrip("/")
    _username = os.getenv("ODOO_USERNAME")
    _password = os.getenv("ODOO_PASSWORD")
    _db = os.getenv("ODOO_DB")

    @staticmethod
    def login():
        """
        Login to Odoo via JSON-RPC and persist session cookies.
        """
        login_url = f"{ImageFetcher._base_url}/web/session/authenticate"

        if not all([ImageFetcher._username, ImageFetcher._password, ImageFetcher._db]):
            logging.error("Missing credentials or DB name in environment variables.")
            return False

        payload = {
            "jsonrpc": "2.0",
            "params": {
                "db": ImageFetcher._db,
                "login": ImageFetcher._username,
                "password": ImageFetcher._password
            }
        }

        try:
            response = ImageFetcher._session.post(login_url, json=payload, verify=False)
            if response.status_code == 200 and response.json().get("result", {}).get("uid"):
                logging.info("Odoo login successful.")
                return True
            else:
                logging.error("Odoo login failed. Status: %s. Response: %s",
                              response.status_code, response.text)
                return False
        except Exception as e:
            logging.error("Login exception: %s", e)
            return False

    @staticmethod
    def fetch_image(image_path):
        """
        Fetch image using Odoo session cookies.
        :param image_path: Path to the image (relative or full URL)
        :return: image bytes or None
        """
        try:
            if not image_path.startswith("http"):
                if not ImageFetcher._base_url:
                    raise ValueError("Base URL not configured.")
                url = f"{ImageFetcher._base_url}/{image_path.lstrip('/')}"
            else:
                url = image_path

            response = ImageFetcher._session.get(url, verify=False)
            if response.status_code == 200:
                logging.info("Fetched image from %s", url)
                return response.content
            else:
                logging.error("Failed to fetch image. Status: %s", response.status_code)
                return None
        except Exception as e:
            logging.error("Error while fetching image: %s", e)
            return None
