'''
1.최소버전+토큰값
---
2.이전 내용 기억하기

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

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role":"system","content": prompt_txt},
        {"role":"user","content":"제이름은 황일영입니다."},
        {"role":"assistant","content":"황일영님 반갑습니다."},
        {"role":"user","content":"대한민국의 수도는?"},
        {"role":"assistant","content":"대한민국의 수도는 서울입니다. 혹시 더 궁금한 것이 있으시면 또 물어보세요"},
        {"role":"user","content":"그곳의 인구수는?"},
        {"role":"assistant","content":"1000만명입니다."},
        {"role":"user","content":"내이름은?"},
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
        "type": "text"
    }
)

print(response.choices[0].message.content)

