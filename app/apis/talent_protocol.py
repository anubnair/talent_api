import os
import requests

def fetch_profile(wallet_address):
    # Get the API_KEY, URL from environment variables
    api_key = os.getenv('TALENT_API_KEY')
    talent_api_url = os.getenv('TALENT_API_URL')

    # Check if the API_KEY is None or empty
    if not api_key or not talent_api_url:
        return jsonify({"error": "Invalid or missing API_KEY in .env"}), 400

    passport_api = f"{talent_api_url}/passports/{wallet_address}"

    headers = {'X-API-KEY': api_key}

    passport_response = requests.get(passport_api, headers=headers)

    if passport_response.status_code == 200:
        passport_data = passport_response.json()
        return passport_data
    else:
        return {"error": "Failed to fetch data from API"}

def fetch_credentials(passport_id):
    # Get the API_KEY, URL from environment variables
    api_key = os.getenv('TALENT_API_KEY')
    talent_api_url = os.getenv('TALENT_API_URL')

    # Check if the API_KEY is None or empty
    if not api_key or not talent_api_url:
        return jsonify({"error": "Invalid or missing API_KEY in .env"}), 400
    headers = {'X-API-KEY': api_key}

    # Now fetch the credentials
    credential_api = f"{talent_api_url}/passport_credentials"
    # Define the query parameters
    params = {
        'passport_id': passport_id
    }
    credential_response = requests.get(credential_api, headers=headers, params=params)
    if credential_response.status_code == 200:
        credential_data = credential_response.json()
        return credential_data
    else:
        return {"error": "Failed to fetch data from API"}