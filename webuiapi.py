import webuiapi
import config
import base64


# create API client with custom host, port and https
api = webuiapi.WebUIApi(host=config.url, port=443, use_https=True)

result1 = api.txt2img(prompt="cute squirrel",
                    negative_prompt="ugly, out of frame",
                    seed=1003,
                    styles=["anime"],
                    cfg_scale=7,
                    )
# images contains the returned images (PIL images)
result1.images

# Decode and save the image.
with open("output.png", 'wb') as f:
    f.write(base64.b64decode(result1))