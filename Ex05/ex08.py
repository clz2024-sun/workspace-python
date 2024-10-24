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
---
6.배경(1)+질+답(5*2) ==> 11개만 보관 --> 우리의사이트의 정보가 없다
---
7.system 사이트정보 추가
---
8.사이트정보 함수로 호출하기
'''

import os       #os모듈을 사용해서 환경변수에 접근
from openai import OpenAI
import chat_dao
#메세지 갯수
n=7

#이컴퓨터의 환경변수의 키값을 읽어온다
openai_api_key = os.getenv("OPENAI_API_KEY") 

#초기화
client = OpenAI(api_key=openai_api_key)

#system프롬프트
prompt_txt = chat_dao.get_data()

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
            temperature=0,         #엉뚱한 단어 
            max_tokens=800,
            top_p=1,               #다양한문장형식 1~5형식 
            frequency_penalty=0,   #중복단어 제한
            presence_penalty=0,    #다른 주제까지 확장
            response_format={
                "type": "text"
            }
        )

        #print(response.choices[0].message.content)
        print(f"[챗_GPT]{response.choices[0].message.content}")
        message_history.append({"role":"assistant","content": response.choices[0].message.content})

        #총5개의 데이타만 유지
        if len(message_history) > n:
            message_history = [message_history[0]] + message_history[-(n-1):]
            #print(message_history)

        
    #//if

print("******************************************")
print("***갑사합니다. 이용해 주셔서 감사합니다.**")
print("******************************************")

    
