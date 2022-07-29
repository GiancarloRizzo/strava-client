
from datetime import datetime, timedelta
import requests
from flask import session, json


# FUNCTIONS ########################################################################################################################
def set_headers(access_token):
    header = {'Authorization': f"Bearer {access_token}"}
    param = {'per_page': 56, 'page': 56}
    data = {'header' : header, 'param' : param}   
    return data

def get_athlete(access_token):
    """
    Returns the currently authenticated athlete. Tokens with profile:read_all scope will receive a detailed athlete representation; all others will receive a summary representation.
    """
    url = f'https://www.strava.com/api/v3/athlete'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_athlete_zones(access_token):
    """
    Returns the the authenticated athlete's heart rate and power zones. Requires profile:read_all.
    """
    url = f'https://www.strava.com/api/v3/athlete/zones'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_athlete_stats(access_token, id):
    """
    Returns the activity stats of an athlete. Only includes data from activities set to Everyone visibilty.
    """
    url = f'https://www.strava.com/api/v3/athletes/{id}/stats'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_activities(access_token, before=datetime.now().timestamp(), after=(datetime.now() -timedelta(days=14)).timestamp()):
    """
    Returns the activities of an athlete for a specific identifier within the last week unless intervall is defined by params "before" and "after".
    "before" and "after" must be epoch-timestamps.
    """
    url = f'https://www.strava.com/api/v3/athlete/activities'
    data = set_headers(access_token)

    # data['param']['before'] = before
    # data['param']['after'] = after
    return requests.get(url, headers=data['header'], params=data['param']).json()
    
def get_activity_by_id(access_token, id):
    """
    Returns the given activity that is owned by the authenticated athlete. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.
    """

    url = f'https://www.strava.com/api/v3/activities/{id}' 
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_activity_zones_by_id(access_token, id):
    """
    Summit Feature. Returns the zones of a given activity. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.
    """

    url = f'https://www.strava.com/api/v3/activities/{id}/zones' 
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()


def get_activity_kudoers_by_id(access_token, id):
    """
    Returns the athletes who kudoed an activity identified by an identifier. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.
    """

    url = f'https://www.strava.com/api/v3/activities/{id}/kudos' 
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()


def get_activity_laps_by_id(access_token, id):
    """
    Returns the laps of an activity identified by an identifier. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.
    """

    url = f'https://www.strava.com/api/v3/activities/{id}/laps' 
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()



def get_activity_comments_by_id(access_token, id):
    """
    Returns the comments on the given activity. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.
    """
    url = f'https://www.strava.com/api/v3/activities/{id}/comments'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_laps_by_activity(id, access_token):
    """
    Returns the laps of an activity identified by an identifier. Requires activity:read for Everyone and Followers activities. Requires activity:read_all for Only Me activities.
    """
    url = f'https://www.strava.com/api/v3/athlete/activities/{id}/laps'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_route_as_gpx(access_token, id):
    """
    Returns a GPX file of the route. Requires read_all scope for private routes.
    """
    url = f'https://www.strava.com/api/v3/routes/{id}/export_gpx'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_route_as_tcx(access_token, id):
    """
    Returns a TCX file of the route. Requires read_all scope for private routes.
    """
    url = f'https://www.strava.com/api/v3/routes/{id}/export_tcx'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_route(access_token, id):
    """
    Returns a route using its identifier. Requires read_all scope for private routes.
    """
    url = f'https://www.strava.com/api/v3/routes/{id}'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

def get_routes_by_athelete(access_token, id):
    """
    Returns a list of the routes created by the authenticated athlete. Private routes are filtered out unless requested by a token with read_all scope.
    """
    url = f'https://www.strava.com/api/v3/athletes/{id}/routes'
    data = set_headers(access_token)
    return requests.get(url, headers=data['header'], params=data['param']).json()

