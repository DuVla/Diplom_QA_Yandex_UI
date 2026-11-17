import requests
from urls import API_URL
import uuid

def register_user(payload):
    return requests.post(f'{API_URL}/auth/register',
        json=payload,
        timeout=10
    )

def generate_user():
    return {
        'email': f'qa-{uuid.uuid4().hex}@example.com',
        'password': uuid.uuid4().hex,
        'name': 'UI Test'
    }

def delete_user(access_token):
    return requests.delete(f'{API_URL}/auth/user',
                           headers={'Authorization': access_token},
                           timeout=10
    )