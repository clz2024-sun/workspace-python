import os  
from openai import OpenAI

#이컴퓨터의 환경변수의 키값을 읽어온다
openai_api_key = os.getenv("OPENAI_API_KEY") 
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)