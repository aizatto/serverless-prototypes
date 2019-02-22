import json
import boto3
import urllib.request
import urllib.parse as urlparse
import os
from urllib.parse import urlencode
ssm = boto3.client('ssm')

def fetch(url):
    response = urllib.request.urlopen(url).read().decode('utf-8');
    return json.loads(response);

def flaturl(url, params):
    # https://stackoverflow.com/questions/2506379/add-params-to-given-url-in-python
    parts = list(urlparse.urlparse(url))
    parts[4] = urlencode(params)
    return urlparse.urlunparse(parts);

def get_parameter(param):
    parameter = '/build.my/%s/%s' % (os.environ['STAGE'], param)
    return ssm.get_parameter(Name=parameter)['Parameter']['Value']

def login(event, context):
    url = flaturl(
        "https://www.facebook.com/v3.2/dialog/oauth",
        {
            "client_id": get_parameter("FACEBOOK_CLIENT_ID"),
            "redirect_uri": os.environ['REDIRECT_URI'],
            "state": "test",
            "scope": ",".join(["user_events"]),
        }
    );

    response = {
        "statusCode": 301,
        "headers":  {
            "Location": url,
        }
    }
    return response

def callback(event, context):
    code = event["queryStringParameters"]["code"]

    url = flaturl(
        "https://graph.facebook.com/v3.2/oauth/access_token",
        {
            "client_id": get_parameter("FACEBOOK_CLIENT_ID"),
            "client_secret": get_parameter("FACEBOOK_CLIENT_SECRET"),
            "code": code,
            "redirect_uri": os.environ['REDIRECT_URI'],
        }
    )

    try:
        response = fetch(url)
    except urllib.error.URLError as err:
        return {
            "statusCode": err.code,
            "body": err.read().decode('utf-8'),
        }

    parameter = ssm.put_parameter(
        Name='/build.my/%s/FACEBOOK_ACCESS_TOKEN' % (os.environ['STAGE']),
        Value=response['access_token'],
        Type="String",
        Overwrite=True,
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }

def inspect(event, context):
    access_token = get_parameter("FACEBOOK_ACCESS_TOKEN");

    url = flaturl(
        "https://graph.facebook.com/debug_token",
        {
            "input_token": access_token,
            "access_token": access_token,
        }
    );

    response = fetch(url)

    return {
        "statusCode": 200,
        "body": json.dumps(response),
    }
