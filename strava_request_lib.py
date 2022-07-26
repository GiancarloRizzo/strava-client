
import requests
from flask import session, json


# FUNCTIONS ########################################################################################################################
def set_headers(access_token):
    header = {'Authorization': f"Bearer {access_token}"}
    param = {'per_page': 2, 'page': 1}
    data = {'header' : header, 'param' : param}   
    return data

def get_athlete(access_token):
    url = f'https://www.strava.com/api/v3/athlete'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_activities(access_token):
    url = f'https://www.strava.com/api/v3/athlete/activities'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()
    
def get_activity_by_id(id, access_token):
    url = f'https://www.strava.com/api/v3/athlete/activities/{client_id}'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_laps_by_activity(id, access_token):
    url = f'https://www.strava.com/api/v3/athlete/activities/{client_id}/laps'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()
