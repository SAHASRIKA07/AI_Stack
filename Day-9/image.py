from diffusers import DiffusionPipeline
import torch
pipe = DiffusionPipeline.from_pretrained("segmind/tiny-sd",torch_dtype=torch.float32)
pipe = pipe.to("cpu")
prompt= "A cute orange cat sitting in a garden, cinema lighting, 4k, ultra-detailed, photorealistic, trending on artstation"
image = pipe(prompt).images[0]
image.save("images/generated_image1.png")
image.show()