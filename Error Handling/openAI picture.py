import openai

openai.api_key = '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'

response = openai.Image.create(
    prompt="frog with a tiny hat, sitting on a leaf and eating a hotdog while watching the sun set over the lake",
    n=1,
    size="256x256"
)

image_url = response['data'][0]['url']

print(image_url)