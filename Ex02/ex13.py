#1 이효리    010-2222-3333    031-2323-4441
#2 정우성    010-2323-2323    02-5555-5555

#이효리
#정우성
file_path ="C:\\javaStudy\\workspace-python\\Ex02\\PhoneDB.txt"

#파일 한번에 읽기
print("파일 한번에 읽기====================")
file = open(file_path, "r", encoding="utf-8")
data = file.read()
print(data)
file.close()


#파일 한번에 읽기2
print("파일 한번에 읽기2 with사용====================")
with open(file_path, "r", encoding='utf-8') as file:
    data = file.read()
    print(data)
    




#파일 한줄씩 읽기
print("파일 한줄씩 읽기====================")
file = open(file_path, 'r',  encoding='utf-8')
for line in file:
    print(line.strip())
file.close()


#파일 한줄씩 읽기2
print("파일 한줄씩 읽기2 with사용====================")
with open(file_path, 'r',  encoding='utf-8') as file:
    for line in file:
        print(line.strip())
