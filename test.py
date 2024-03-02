import requests
import base64

import config

# Define the URL and the payload to send.
url = config.url

payload = {
    "prompt": "puppy dog",
    "steps": 5,
    "seed":1,
    "cfg_scale":2,
}

# Send said payload to said URL through the API.
response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
r = response.json()
# Decode and save the image.
with open("output.png", 'wb') as f:
    f.write(base64.b64decode(r['images'][0]))