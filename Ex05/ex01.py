'''
1.최소버전+토큰값

'''

import os       #os모듈을 사용해서 환경변수에 접근
from openai import OpenAI

#이컴퓨터의 환경변수의 키값을 읽어온다
openai_api_key = os.getenv("OPENAI_API_KEY") 

client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role":"user","content":"자바의 리스트를 100자 이내로 표현해줘"}
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

#토근수 확인
q_token = response.usage.prompt_tokens #질문토근수
a_token = response.usage.completion_tokens  #응답토큰수
t_token = response.usage.total_tokens #전체토큰수
print(f"질문:{q_token}+응답:{a_token}=합계:{t_token}")