#while문

#6의 배수이자 14의 배수인 가장 적은 정수 찾기

i = 1
while True:
    
    if i%6==0 and i%14==0 :
        print(i)
        break
    
    i += 1   # i=i+1
    
