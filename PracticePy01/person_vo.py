class PersonVo:
    def __init__(self, person_id="Unknown", name="Unknown", hp="Unknown", company="Unknown"):
        self.person_id = person_id  # 속성: 사람 ID
        self.name = name            # 속성: 이름
        self.hp = hp                # 속성: 전화번호
        self.company = company      # 속성: 회사


    def __str__(self):
        #info_str = "PersonVo(person_id=" + self.person_id +" )" 
        info_str = f"PersonVo(persin_id={self.person_id}), name={self.name}, hp={self.name}, company={self.company} )"

        return info_str
    
    
    def showInfo(self):
        info_str = f"""
PersonVo(
    Persin_id={self.person_id}), 
    name={self.name}, 
    hp={self.name}, 
    company={self.company} 
)
            """
        return info_str


