import random
class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hp = 100
        self.skill_dict = {'몸통 박치기': 5, '울음소리': 5, '전광석화': 10}

    def attack(self, target, skill_name, skill_level, position):
        print(f'{position}의 {self.name}이(가) {skill_name}(으)로 {position}의 {target.name}을(를) 공격했다!')
        target.hp -= skill_level
        if target.hp <= 0:
            target.hp = 0
        print(f'{position}의 {target.name}의 체력이 {target.hp}로 하락했다!')

    def run(self, target):
        print(f'{self.name}이(가) 야생의 {target.name}과(와)의 대결에서 도망쳤다!')

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp


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
        nemesis_pika = Pikachu()
        nemesis_char = Charmander()
        nemesis_squir = Squirtle()
        nemesis_bul = Bulbasaur()
        self.nemesis_list = [nemesis_pika, nemesis_char, nemesis_squir, nemesis_bul]
        self.mine = self.start()

    def start(self):
        print("포켓몬스터 게임을 시작합니다!")
        self.user = input("당신의 이름은? : ")
        print(f"{self.user}님의 스타팅 포켓몬을 선택해주세요.")

        i = 1
        for pokemon in self.pokemon_list:
            print(f'{i}) {pokemon}')
            i += 1

        while True:
            select = input(f"{self.user}님의 스타팅 포켓몬(1 ~ 4번) : ")

            if select == '1':  # 피카츄
                self.user_pokemon = Pikachu()
                print(f"{self.user_pokemon.get_type()} 속성의 {self.user_pokemon.get_name()}를 선택하셨습니다!")
                break
            elif select == '2':  # 파이리
                self.user_pokemon = Charmander()
                print(f"{self.user_pokemon.get_type()} 속성의 {self.user_pokemon.get_name()}를 선택하셨습니다!")
                break
            elif select == '3':  # 꼬부기
                self.user_pokemon = Squirtle()
                print(f"{self.user_pokemon.get_type()} 속성의 {self.user_pokemon.get_name()}를 선택하셨습니다!")
                break
            elif select == '4':  # 이상해씨
                self.user_pokemon = Bulbasaur()
                print(f"{self.user_pokemon.get_type()} 속성의 {self.user_pokemon.get_name()}를 선택하셨습니다!")
                break
            else:
                print("1 ~ 4번 중에서 골라주세요!")

        # while

        return self.user_pokemon

    def fight(self):
        nemesis = random.choice(self.nemesis_list)
        print(f'야생의 {nemesis.get_name()}이(가) 나타났다!')
        select = input("1) 싸우기  2) 도망가기 : ")
        if select == '2':
            self.mine.run(nemesis)
        elif select == '1':
            print(f'!! {self.user}님의 {self.mine.get_name()} vs 야생의 {nemesis.get_name()} !!\n')
            while True:
                if self.mine.get_hp() <= 0:
                    print(f'야생의 {nemesis.get_name()}과(와)의 대결에서 패배했다!')
                    break
                elif nemesis.get_hp() <= 0:
                    print(f'야생의 {nemesis.get_name()}과(와)의 대결에서 승리했다!')
                    break
                else:
                    # user 포켓몬의 공격
                    i = 1
                    skill_names = list(self.mine.skill_dict.keys())
                    for skill_name in skill_names:
                        print(f'{i}) {skill_name}', end='  ')
                        i += 1
                    select = int(input("/ 공격을 고르세요 : "))
                    if 0 < select <= len(skill_names):
                        my_skill = skill_names[select - 1]
                        self.mine.attack(nemesis, my_skill, self.mine.skill_dict[my_skill], self.user)

                    if nemesis.get_hp() <= 0:
                        print(f'\n야생의 {nemesis.get_name()}과(와)의 대결에서 승리했다!')
                        break

                    print()
                    # 야생 포켓몬의 공격

                    nemesis_skill = random.choice(list(nemesis.skill_dict.keys()))
                    nemesis.attack(self.mine, nemesis_skill, nemesis.skill_dict[nemesis_skill], "야생")
                    if self.mine.get_hp() <= 0:
                        print(f'\n야생의 {nemesis.get_name()}과(와)의 대결에서 패배했다!')
                        break
                    print()
        return

    def menu(self):
        while True:
            select = input("\n* 시작 메뉴 * \n1) 탐험하기 \n2) 체력 충전하기 \n3) 게임 종료하기 \n")
            if select == '1':
                happen = random.randint(0, 2)
                if happen == 0:
                    print("아무것도 발견하지 못했습니다.")
                elif happen == 1:
                    self.fight()
            elif select == '2':
                if self.mine.get_hp() == 100:
                    print("체력이 최대치입니다!")
                else:
                    before = self.mine.get_hp()
                    self.mine.set_hp(100)
                    print(f'{self.mine.get_name()}의 체력이 {before}에서 100으로 회복되었습니다!')
            elif select == '3':
                print("포켓몬스터 게임을 종료하겠습니다.")
                return
            else:
                print("1 ~ 3번 메뉴 중에서 골라주세요!")


game = Game()
game.menu()
