import webuiapi
import config

# create API client with custom host, port and https
api = webuiapi.WebUIApi(host=config.host, port=443, use_https=True)

condition = api.txt2img(prompt="cute squirrel",
                    negative_prompt="ugly, out of frame",
                    seed=1003,
                    styles=["anime"],
                    cfg_scale=7,
                    )

# print(api.controlnet_model_list())
unit1 = webuiapi.ControlNetUnit(input_image=condition.images[0], module='inpaint', model='controlnet11Models_inpaint [be8bc0ed]')

output = api.txt2img(prompt="cute squirrel",
                    negative_prompt="ugly, out of frame",
                    seed=1003,
                    styles=["anime"],
                    cfg_scale=7,
                    width=512,
                    height=1024,
                    controlnet_units=[unit1]
                    )


# save the image
condition.images[0].save("input.png")
output.images[0].save("output.png")