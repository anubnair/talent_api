from flask import Blueprint, request, jsonify
from app.apis.talent_protocol import fetch_profile, fetch_credentials
from app.utils import build_profile

# Initialize Blueprint for API routes
bp = Blueprint('api', __name__)

# API endpoint to fetch data from external API and save it
@bp.route('/profile/<wallet_address>', methods=['GET'])
def get_passport(wallet_address):
    try:
        passport_data = fetch_profile(wallet_address)
        credentials = {}
        if 'passport_id' in passport_data['passport']:
            credentials = fetch_credentials(passport_data['passport']['passport_id'])
        profile = build_profile(wallet_address, passport_data, credentials)

        # TODO: Save the data into the database
        # passport = Passport(wallet_address=wallet_address, data=passport_data)
        # db.session.add(passport)
        # db.session.commit()

        return jsonify(profile)

    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Failed to fetch data from API"}), 400