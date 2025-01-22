import requests
from app.apis.github import fetch_data_from_github

def build_profile(wallet_address, passport_data, credential_data):
    #passport_credentials_data = result(passport_data["passport"]["passport_id"])
    # Build the profile data
    profile = {
        "display_name": passport_data["passport"]["passport_profile"]["display_name"],
        "bio": passport_data["passport"]["passport_profile"]["bio"],
        "location": passport_data["passport"]["passport_profile"]["location"],
        "image_url": passport_data["passport"]["passport_profile"]["image_url"],
        "socials": passport_data["passport"]["passport_socials"],
        "skills_score": passport_data["passport"]["skills_score"],
        "score": passport_data["passport"]["score"],
        "identity_score": passport_data["passport"]["identity_score"],
        "activity_score": passport_data["passport"]["activity_score"],
        "passport_id": passport_data["passport"]["passport_id"],
        "human_checkmark": passport_data["passport"]["human_checkmark"],
        "abilities": {"skills": []},
        "verified_wallets": passport_data["passport"]["verified_wallets"],
        "credentials": credential_data["passport_credentials"]
    }

    # Check if GitHub exists in passport_socials
    for social in profile['socials']:
        if social["source"] == "github":
            github_username = social["profile_name"]
            skills = fetch_data_from_github(github_username)
            profile["abilities"]["skills"] = skills
            break
        if profile["bio"] == "" and  social['profile_bio'] != "":
            profile["bio"] = social['profile_bio']
    return profile