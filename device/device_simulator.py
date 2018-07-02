import requests
import base64
import datetime
import json
import time
import jwt
import argparse
import os

current_jwt_exp = None
def get_or_renew_jwt(current_jwt, private_key, project_id):
    global current_jwt_exp
    if current_jwt:
        if current_jwt_exp > datetime.datetime.utcnow():
            return current_jwt

    print("JWT is expired or does not exist, renewing")
    jwt_iat = datetime.datetime.utcnow()
    current_jwt_exp = jwt_iat + datetime.timedelta(minutes=60)
    token = {
        'iat': jwt_iat,
        'exp': current_jwt_exp,
        'aud': project_id
    }
    return jwt.encode(token, private_key, algorithm='RS256').decode('ascii')

def publish_telemetry(jwt, device_path, message):
    # Encode message as utf-8
    binary_data = message.encode('utf-8')

    # Encode utf-8 message as base64 binary
    b64_binary_data = base64.urlsafe_b64encode(binary_data)

    # Decode base64 binary into base64 string
    b64_data = b64_binary_data.decode('ascii')

    # Set message body, headers, and url
    body = {'binary_data': b64_data }
    headers = {
      'authorization': 'Bearer {}'.format(jwt),
      'content-type': 'application/json'
    }
    publish_url = 'https://cloudiotdevice.googleapis.com/v1/{}:publishEvent'.format(device_path)

    # Attempt to publish
    print('Publishing {} to {} using headers {}'.format(body, publish_url, headers))
    response = requests.post(publish_url, data=json.dumps(body), headers=headers)

    if response.status_code is not 200:
      print('Bad response {}'.format(response))
      print(response.reason)
      print(response.text)

    return response

def main():
    # Environmental variable values below can be set in linux by typing the following in your shell:
    # export PROJECT_ID="foo"
    project_id = os.environ["PROJECT_ID"]
    region = os.environ["REGION"]
    device_id = os.environ["DEVICE_ID"]
    registry_id = os.environ["REGISTRY_ID"]
    path_to_key = os.environ["PATH_TO_KEY"]
    device_path = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(project_id, region, registry_id, device_id)

    # Read the private key pem file
    path_to_key = os.path.join(os.path.dirname(__file__), path_to_key)
    with open(path_to_key, 'r') as f:
        private_key = f.read()

    # jwt is kept outside of the loop to check for renewals
    current_jwt = None

    # Data is completely arbitrary for button press
    data = "1"

    # Loop forever, listening for button presses
    while True:
        # Check for JWT renewal
        current_jwt = get_or_renew_jwt(current_jwt, private_key, project_id)

        # Publish data every 10 seconds
        # TODO: run publish code if button press occurs, not on timer like below
        publish_telemetry(current_jwt, device_path, data)
        time.sleep(10)

# Pythonic way of running main function if module run as script and not import
if __name__ == "__main__":
    main()
