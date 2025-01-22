import os
import unittest
from unittest.mock import patch
from app import create_app

class TestProfileAPI(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client and environment variables."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.wallet_address = "0x0914543c9716d8a4811187a78606a50ca81b9c14"
        os.environ["API_KEY"] = "test_api_key"

    def test_get_profile_invalid_api_key(self):
        """Test the /profile/<wallet_address> API endpoint with invalid API key."""
        os.environ["API_KEY"] = ""  # Simulate missing API key

        # Send GET request to the API
        response = self.client.get(f"/profile/{self.wallet_address}")

        # Assertions
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()