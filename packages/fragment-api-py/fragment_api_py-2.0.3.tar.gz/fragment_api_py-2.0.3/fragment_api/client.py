import requests
import json
import os
import logging
from typing import Dict, Optional
from datetime import datetime

# Инициализация логгера
logger = logging.getLogger(__name__)

class FragmentAPI:
    """Client for interacting with the Fragment API."""
    
    def __init__(self, base_url: str = "https://fragment.s1qwy.ru"):
        """Initialize the Fragment API client.
        
        Args:
            base_url (str): Base URL of the Fragment API (default: https://fragment.s1qwy.ru)
        """
        self.base_url = base_url.rstrip('/')
        self.auth_key: Optional[str] = None
        self.session = requests.Session()
        self.session_file = "fragment_session.json"

    def _print_response(self, response: requests.Response, method: str, url: str) -> None:
        """Helper method to print full server response details."""
        logger.debug(f"--- API Request: {method} {url} ---")
        logger.debug(f"Status Code: {response.status_code}")
        logger.debug(f"Headers: {response.headers}")
        try:
            logger.debug(f"Response Body: {json.dumps(response.json(), indent=2)}")
        except ValueError:
            logger.debug(f"Response Body (raw): {response.text}")
        logger.debug("--- End of Response ---")

    def _handle_request(self, method: str, url: str, **kwargs) -> Dict:
        """Helper method to make HTTP requests and handle responses."""
        try:
            response = getattr(self.session, method)(url, **kwargs)
            self._print_response(response, method.upper(), url)
            response.raise_for_status()
            return {"ok": True, "result": response.json()}
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error occurred: {e}")
            self._print_response(e.response, method.upper(), url)
            return {"ok": False, "error": e.response.json() if e.response else {"error": str(e)}}
        except requests.exceptions.RequestException as e:
            logger.error(f"Request Error occurred: {e}")
            return {"ok": False, "error": {"error": str(e)}}

    def create_auth(self, wallet_mnemonic: str, cookies: str, hash_value: str) -> Dict:
        """Create a new authentication session."""
        payload = {
            "wallet_mnemonic": wallet_mnemonic,
            "cookies": cookies,
            "hash": hash_value
        }
        url = f"{self.base_url}/create_auth"
        result = self._handle_request("post", url, json=payload)
        
        if result.get("ok") and result.get("result", {}).get("auth_key"):
            self.auth_key = result["result"]["auth_key"]
            self.save_session()
            
        return result

    def save_session(self, filename: Optional[str] = None) -> bool:
        """Save current session to file."""
        if not self.auth_key:
            return False
            
        session_data = {
            "auth_key": self.auth_key,
            "base_url": self.base_url,
            "saved_at": datetime.now().isoformat()
        }
        
        try:
            file_path = filename or self.session_file
            with open(file_path, 'w') as f:
                json.dump(session_data, f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Error saving session: {e}")
            return False

    def load_session(self, filename: Optional[str] = None) -> bool:
        """Load session from file."""
        try:
            file_path = filename or self.session_file
            if not os.path.exists(file_path):
                return False
                
            with open(file_path, 'r') as f:
                session_data = json.load(f)
                
            self.auth_key = session_data.get("auth_key")
            if "base_url" in session_data:
                self.base_url = session_data["base_url"]
                
            return self.auth_key is not None
            
        except Exception as e:
            logger.error(f"Error loading session: {e}")
            return False

    def delete_session(self, filename: Optional[str] = None) -> bool:
        """Delete saved session file."""
        try:
            file_path = filename or self.session_file
            if os.path.exists(file_path):
                os.remove(file_path)
                self.auth_key = None
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting session: {e}")
            return False

    def has_valid_session(self) -> bool:
        """Check if there's a valid session available."""
        return self.auth_key is not None

    def get_balance(self) -> Dict:
        """Get wallet balance."""
        if not self.auth_key:
            return {"ok": False, "error": {"error": "Authentication key not set. Please create_auth first."}}
            
        url = f"{self.base_url}/balance/{self.auth_key}"
        return self._handle_request("get", url)

    def buy_stars(self, username: str, quantity: Optional[int] = 50, show_sender: Optional[bool] = False) -> Dict:
        """Buy Telegram Stars for a specified user."""
        if not self.auth_key:
            return {"ok": False, "error": {"error": "Authentication key not set. Please create_auth first."}}
            
        payload = {
            "username": username,
            "quantity": quantity,
            "show_sender": show_sender
        }
        
        url = f"{self.base_url}/buy_stars/{self.auth_key}"
        return self._handle_request("post", url, json=payload)

    def gift_premium(self, username: str, months: Optional[int] = 3, show_sender: Optional[bool] = False) -> Dict:
        """Gift Telegram Premium to a specified user."""
        if not self.auth_key:
            return {"ok": False, "error": {"error": "Authentication key not set. Please create_auth first."}}
            
        payload = {
            "username": username,
            "months": months,
            "show_sender": show_sender
        }
        
        url = f"{self.base_url}/gift_premium/{self.auth_key}"
        return self._handle_request("post", url, json=payload)

    def topup_ton(self, username: str, amount: int, show_sender: Optional[bool] = False) -> Dict:
        """Top up TON for a specified user."""
        if not self.auth_key:
            return {"ok": False, "error": {"error": "Authentication key not set. Please create_auth first."}}
            
        payload = {
            "username": username,
            "amount": amount,
            "show_sender": show_sender
        }
        
        url = f"{self.base_url}/topup_ton/{self.auth_key}"
        return self._handle_request("post", url, json=payload)

    def get_user_stars(self, username: str) -> Dict:
        """Search user for Telegram Stars transactions."""
        if not self.auth_key:
            return {"ok": False, "error": {"error": "Authentication key not set. Please create_auth first."}}
            
        payload = {"username": username}
        url = f"{self.base_url}/get_user_stars/{self.auth_key}"
        return self._handle_request("post", url, json=payload)

    def get_user_premium(self, username: str) -> Dict:
        """Search user for Telegram Premium transactions."""
        if not self.auth_key:
            return {"ok": False, "error": {"error": "Authentication key not set. Please create_auth first."}}
            
        payload = {"username": username}
        url = f"{self.base_url}/get_user_premium/{self.auth_key}"
        return self._handle_request("post", url, json=payload)

    def health_check(self) -> Dict:
        """Check API health status."""
        url = f"{self.base_url}/health"
        return self._handle_request("get", url)

    def close(self):
        """Close the session."""
        self.session.close()
        self.auth_key = None