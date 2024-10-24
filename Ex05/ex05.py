'''
1.최소버전+토큰값
---
2.이전 내용 기억하기
---
3.사용자 질문입력하기
---
4.반복해서 질문입력하기, 종료가능, *대화내용이 누적되지 않음
---
5.대화내용 누적  -> 토큰(비용)이 많이 사용해야한다
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

message_history =[
    {"role":"system","content": prompt_txt},
]


#사용자로 부터 질문입력 받기
print("******************************************")
print("***반갑습니다. 질문을 입력해 주세요*******")
print("******************************************")

while True:
    question = input("(사용자)")

    if question == "\q":
        break
    
    else:
        #질문추가
        message_history.append({"role":"user","content": question})

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
        message_history.append({"role":"assistant","content": response.choices[0].message.content})

        print(message_history)
    #//if

print("******************************************")
print("***갑사합니다. 이용해 주셔서 감사합니다.**")
print("******************************************")

    
