from openai import OpenAI

client = OpenAI(api_key="BlbkFJ-PMMm_IB-u7EiaDXBQsP4tAKXjxq84NA17BplRwmecIxkRg4h-76m4PHILU4kjTBlDHZr2zb8A")

def ask_dalle(prompt):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return response.data[0].url

prompt = input("Enter Prompt To Generate Image:")
image_url = ask_dalle(prompt)
print("Generate Image Url:", image_url)

