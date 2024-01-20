class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hp = 100
        self.skill_dict = {'몸통 박치기': 5, '울음소리': 5, '전광석화': 10}

    def attack(self, target, skill_name, skill_level):
        print(f'{self.name}이(가) {skill_name}(으)로 {target.name}을(를) 공격했다!')
        target.hp -= skill_level
        print(f'{target.name}의 체력이 {target.hp}로 하락했다!')

    def run(self, target):
        print(f'{self.name}이(가) {target.name}과의 대결에서 도망쳤다!')

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_hp(self):
        return self.hp


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('피카츄', '전기')
        self.pikachu_skill_dict = {'전기쇼크': 20, '10만 볼트': 30, '번개': 50}
        self.skill_dict.update(self.pikachu_skill_dict)


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__('꼬부기', '물')
        self.squirtle_skill_dict = {'거품': 20, '물대포': 30, '하이드로 펌프': 50}
        self.skill_dict.update(self.squirtle_skill_dict)


class Charmander(Pokemon):
    def __init__(self):
        super().__init__('파이리', '불')
        self.charmander_skill_dict = {'불꽃세례': 20, '화염방사': 30, '연옥': 50}
        self.skill_dict.update(self.charmander_skill_dict)


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__('이상해씨', '풀')
        self.charmander_skill_dict = {'덩굴채찍': 20, '앞날가르기': 30, '씨폭탄': 50}
        self.skill_dict.update(self.charmander_skill_dict)


class Game:
    def __init__(self):
        self.pokemon_list = ['피카츄', '파이리', '꼬부기', '이상해씨']

    def start(self):
        print("포켓몬스터 게임을 시작합니다!")
        user = input("당신의 이름은? : ")
        print(f"{user}님의 스타팅 포켓몬을 선택해주세요.")
        i = 1
        while i <= len(self.pokemon_list):
            print(f'{i}) {self.pokemon_list[i-1]}')
            i += 1

        while True:
            num = input(f"{user}님의 스타팅 포켓몬(1 ~ 4번) : ")

            if num == '1':  # 피카츄
                user_pokemon = Pikachu()
                print(f"{user_pokemon.get_type()} 속성의 {user_pokemon.get_name()}를 선택하셨습니다!")
                break
            elif num == '2':  # 파이리
                user_pokemon = Charmander()
                print(f"{user_pokemon.get_type()} 속성의 {user_pokemon.get_name()}를 선택하셨습니다!")
                break
            elif num == '3':  # 꼬부기
                user_pokemon = Squirtle()
                print(f"{user_pokemon.get_type()} 속성의 {user_pokemon.get_name()}를 선택하셨습니다!")
                break
            elif num == '4':  # 이상해씨
                user_pokemon = Bulbasaur()
                print(f"{user_pokemon.get_type()} 속성의 {user_pokemon.get_name()}를 선택하셨습니다!")
                break
            else:
                print("1 ~ 4번 중에서 골라주세요!")

        # while

        return user_pokemon


game = Game()
game.start()

