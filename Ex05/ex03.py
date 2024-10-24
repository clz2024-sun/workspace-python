'''
1.최소버전+토큰값
---
2.이전 내용 기억하기
---
3.사용자 질문입력하기
'''

import os       #os모듈을 사용해서 환경변수에 접근
from openai import OpenAI

#이컴퓨터의 환경변수의 키값을 읽어온다
openai_api_key = os.getenv("OPENAI_API_KEY") 

#초기화
client = OpenAI(api_key=openai_api_key)

#system프롬프트
prompt_txt ="""
    #context
    50글자 이내로 답해주세요

    #tone
    친절한 말투로 답변해주세요
"""

#사용자로 부터 질문입력 받기
print("******************************************")
question = input("질문을 입력해 주세요\n(사용자)")

#메세지
message_history =[
    {"role":"system","content": prompt_txt},
    {"role":"user","content": question},
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=message_history,
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
        "type": "text"
    }
)

#print(response.choices[0].message.content)
print(f"[챗_GPT]{response.choices[0].message.content}")
