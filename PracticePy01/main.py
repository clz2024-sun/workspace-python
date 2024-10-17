# person_vo.py 파일에서 PersonVo 클래스를 가져옴
from person_vo import PersonVo

p01 = PersonVo(1,"정우성", "010-1111-1111", "02-1111-1111")
print(p01)
print(p01.showInfo())

print("---------------------------------")
p02 = PersonVo()
p02.person_id = 2
p02.name = "박명수"
p02.hp = "010-2222-2222"
p02.company = "02-2222-2222"

print(p02)
print(p02.showInfo())

print("---------------------------------")
p03 = PersonVo("이효리")

print(p03)
print(p03.showInfo())