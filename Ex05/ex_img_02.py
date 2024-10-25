
import os       #os모듈을 사용해서 환경변수에 접근
from openai import OpenAI
import uuid
import requests

#이컴퓨터의 환경변수의 키값을 읽어온다
openai_api_key = os.getenv("OPENAI_API_KEY") 

#초기화
client = OpenAI(api_key=openai_api_key)

prompt_txt ="""
A close-up of a woman’s face,
captured in low light with a soft
focus. There is a gentle pink hue
to the image, and the woman’s
features are lightly blurred."""


response = client.images.generate(
  model="dall-e-3",
  prompt=prompt_txt,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)


# 다운로드 받을 경로
download_path = "C:\\javaStudy\\upload_py"

# 파일이름 생성
file_name = str(uuid.uuid4())+".png"

# 이미지 다운로드
response = requests.get(image_url)
if response.status_code == 200:
    file_path = os.path.join(download_path, file_name) 
    with open(file_path, "wb") as file:
        file.write(response.content)
    
    print("다운로드 완료")
else:
    print("url 오류")