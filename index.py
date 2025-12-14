import base64
import requests
from dotenv import load_dotenv
import os 
load_dotenv('.env')
CLIENT_ID=os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')

# creating a token for spotify verification
def access_token():
    try:
         credentials=f"{CLIENT_ID}:{CLIENT_SECRET}"
         encoded_credentials=base64.b64encode(credentials.encode()).decode()
         response = requests.post(
            'https://accounts.spotify.com/api/token',
            headers={"Authorization":f'Basic {encoded_credentials}'},
            data={'grant_type':'client_credentials'})
         # print(response.json())
         # print(response.json()['access_token'])

         print("Token Generated Successfully...")
         return response.json()['access_token']
    except Exception as e:
         print("Error in Token Generation...",e)
# print(access_token())