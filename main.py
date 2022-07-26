from flask import json
from flask import Flask, request, redirect, session, url_for

import os
import requests
import strava_request_lib as api
from utils import load_config, save_config
app = Flask(__name__)

config = load_config('credentials.yml')
client_id = config['client_id']
client_secret = config['client_secret']
base_url = 'http://www.strava.com/oauth/authorize'
website_domain = 'http://127.0.0.1'
port = '5000'
redirect_uri = f'{website_domain}:{port}/callback'
response_type = 'code'
scope = 'activity:read_all,read_all,read' #no writing permissions until yet
grant_type = "authorization_code"
token_url = "https://www.strava.com/oauth/token"
authorization_url = f'{base_url}?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}&scope={scope}'



# AUTH ########################################################################################################################
def get_authorization_code():
    return request.args.get('code')

def get_access():
    params = {
        'client_id': client_id,
        'client_secret': client_secret, 
        'code': get_authorization_code(),
        'redirect_uri': f'{redirect_uri}',
        'grant_type': "authorization_code"
    }
    
    res = requests.post(f'{token_url}', params=params, verify=True)

    session['access_token'] = res.json()['access_token']
    session['refresh_token'] = res.json()['refresh_token']

    # save_config(session['access_token'], 'credentials.yml')
    # save_config(session['refresh_token'], 'credentials.yml')
    return

# APP  ########################################################################################################################

@app.route("/")
def start():
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.

@app.route("/callback", methods=["GET"])
def callback():
    get_access()

    print(api.get_athlete(session['access_token']))
    print('\n')
    print(api.get_activities(session['access_token']))


    return redirect(url_for('.profile'))


@app.route("/profile", methods=["GET"])
def profile():
    
    return ''

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=5000, debug=True)








