import os
import pickle
import pyrebase as pyfbase
import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials

cred = credentials.Certificate("./service_account.json")
firebase_admin.initialize_app(cred)

firebaseConfig = {
    "apiKey": "AIzaSyDj8b00xkTxQnZ_Y_qpgww7xQOKeVf0hvk",
    "authDomain": "fletdemoproject.firebaseapp.com",
    "projectId": "fletdemoproject",
    "storageBucket": "fletdemoproject.appspot.com",
    "messagingSenderId": "297559729859",
    "appId": "1:297559729859:web:4845648d0721ef46efa476",
    "databaseURL": "https://fletdemoproject-default-rtdb.firebaseio.com/"
}


firebase = pyfbase.initialize_app(firebaseConfig)
auth = firebase.auth()


# email = "test@fletdemo.com"
# password = "password@123456"
# name = "Test"

# firebase_auth.create_user(
#     email=email, password=password, display_name=name
# )
def create_user(name, email, password):
    try:
        user = auth.firebase_auth.create_user(
            email=email, password=password, display_name=name
        )
        return user.uid
    except:
        return None


def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user['idToken']
    except:
        return None


def store_token(token):
    if os.path.exists("token.pickle"):
        os.remove("token.pickle")
    with open("token.pickle", "wb") as token_file:
        pickle.dump(token, token_file)


def revoke_token(token):
    firebase_auth.revoke_refresh_tokens(token)

    if os.path.exists("token.pickle"):
        os.remove("token.pickle")
