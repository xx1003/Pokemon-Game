import addskill

class Pokemon:
    hp = 100
    xp = 0

    # swim = addskill.Noswim()

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.skill_dict = {'몸통 박치기': 5, '울음소리': 5, '전광석화': 10}
        self.can_fly = False
        self.fly_skill = addskill.Nofly()

    def attack(self, target, skill_name, skill_level, position, target_position):
        print(f'{position}의 {self.name}이(가) {skill_name}(으)로 {target_position}의 {target.name}을(를) 공격했다!')
        target.hp -= skill_level
        if target.hp <= 0:
            target.hp = 0
        print(f'{target_position}의 {target.name}의 체력이 {target.hp}로 하락했다!')

    def run(self, target, user):
        print(f'{user}의 {self.name}이(가) 야생의 {target.name}과(와)의 대결에서 도망쳤다!')

    def evolve(self, new_name):
        print(f'{self.name}이(가) {new_name}으로 진화했다!')
        self.name = new_name
        print(f'{self.name}의 특수공격의 위력이 5씩 증가했다!\n')
        self.fly_skill = addskill.FlyingSkill()
        self.can_fly = True
        self.fly_skill.fly(self.name)

    def inventory(self):
        print(f"<< {self.name}의 보유 공격 >>")
        for key in self.skill_dict.keys():
            print(f'공격 : {key}   위력 : {self.skill_dict[key]}')
        print()
        print(f"<< {self.name}의 특수 능력 >>")
        if self.can_fly:
            print(f'플라잉 능력')
        else:
            print('없음')

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_xp(self):
        return self.xp

    def set_xp(self, xp):
        self.xp = xp

    def add_xp(self, xp):
        self.xp += xp


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('피카츄', '전기')
        self.pikachu_skill_dict = {'전기쇼크': 20, '10만 볼트': 30, '번개': 50}
        self.skill_dict.update(self.pikachu_skill_dict)
        self.evolve_name = '라이츄'

    def evolve(self):
        super().evolve(self.evolve_name)
        self.pikachu_skill_dict = {'전기쇼크': 25, '10만 볼트': 35, '번개': 55}
        self.skill_dict.update(self.pikachu_skill_dict)


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__('꼬부기', '물')
        self.squirtle_skill_dict = {'거품': 20, '물대포': 30, '하이드로 펌프': 50}
        self.skill_dict.update(self.squirtle_skill_dict)
        self.evolve_name = '어니부기'

    def evolve(self):
        super().evolve(self.evolve_name)
        self.squirtle_skill_dict = {'거품': 25, '물대포': 35, '하이드로 펌프': 55}
        self.skill_dict.update(self.squirtle_skill_dict)


class Charmander(Pokemon):
    def __init__(self):
        super().__init__('파이리', '불')
        self.charmander_skill_dict = {'불꽃세례': 20, '화염방사': 30, '연옥': 50}
        self.skill_dict.update(self.charmander_skill_dict)
        self.evolve_name = '리자드'

    def evolve(self):
        super().evolve(self.evolve_name)
        self.charmander_skill_dict = {'불꽃세례': 25, '화염방사': 35, '연옥': 55}
        self.skill_dict.update(self.charmander_skill_dict)


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__('이상해씨', '풀')
        self.bulbasaur_skill_dict = {'덩굴채찍': 20, '앞날가르기': 30, '씨폭탄': 50}
        self.skill_dict.update(self.bulbasaur_skill_dict)
        self.evolve_name = '이상해풀'

    def evolve(self):
        super().evolve(self.evolve_name)
        self.bulbasaur_skill_dict = {'덩굴채찍': 25, '앞날가르기': 35, '씨폭탄': 55}
        self.skill_dict.update(self.bulbasaur_skill_dict)

