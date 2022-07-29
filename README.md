# strava-client
A simple strava client to fetch activity-data in json-format provided by [strava-api](https://developers.strava.com/docs/reference/).

## Prerequisites
- [Stava](https://www.strava.com/) account

## Get started

#### 1. Register API client 
  
Navigate to https://www.strava.com/settings/api. Log in with your Strava-account and create a new client.

Use `localhost:5000?callback` as the authorization callback domain for this example.


#### 2. Install the client & add credentials

```bash
git clone https://github.com/GiancarloRizzo/strava-client.git

# make your virtual-env ready
cd strava-client
source bin/activate
pip install -r requirements

# replace your client-id and client-secret from [https://www.strava.com/settings/api](https://www.strava.com/settings/api) in credentials.yml:
nano credentials.yml
# client_id: example-id-743b34
# client_secret: example-secret-832-dshdfsk-234r89hfdfj34-c663je
```

#### 3. Link user & run

User account needs to be linked to client application before client can get any user data. User is asked for authorization 
in Strava, and user is redirected back to application callback url with authorization code once user has accepted the request.

```bash
# run webserver and call in webserver your url: localhost:5000 and login with your strava-login-credentials
python main.py
```
