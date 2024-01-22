import random
import PokemonClass as pc

class Game:
    def __init__(self):
        self.pokemon_list = ['피카츄', '파이리', '꼬부기', '이상해씨']
        nemesis_pika = pc.Pikachu()
        nemesis_char = pc.Charmander()
        nemesis_squir = pc.Squirtle()
        nemesis_bul = pc.Bulbasaur()
        # self.nemesis_list = [nemesis_pika, nemesis_char, nemesis_squir, nemesis_bul]
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
                self.user_pokemon = pc.Pikachu()
                print(f"{self.user_pokemon.get_type()} 속성의 {self.user_pokemon.get_name()}를 선택하셨습니다!")
                break
            elif select == '2':  # 파이리
                self.user_pokemon = pc.Charmander()
                print(f"{self.user_pokemon.get_type()} 속성의 {self.user_pokemon.get_name()}를 선택하셨습니다!")
                break
            elif select == '3':  # 꼬부기
                self.user_pokemon = pc.Squirtle()
                print(f"{self.user_pokemon.get_type()} 속성의 {self.user_pokemon.get_name()}를 선택하셨습니다!")
                break
            elif select == '4':  # 이상해씨
                self.user_pokemon = pc.Bulbasaur()
                print(f"{self.user_pokemon.get_type()} 속성의 {self.user_pokemon.get_name()}를 선택하셨습니다!")
                break
            else:
                print("1 ~ 4번 중에서 골라주세요!")

        # while

        return self.user_pokemon

    def fight(self):
        num = random.randint(0, 3)
        if num == 0:
            nemesis = pc.Pikachu()
        elif num == 1:
            nemesis = pc.Charmander()
        elif num ==2:
            nemesis = pc.Squirtle()
        elif num ==3:
            nemesis = pc.Bulbasaur()

        print(f'야생의 {nemesis.get_name()}이(가) 나타났다!')
        while True:
            select = input("1) 싸우기  2) 도망가기 : ")
            if select == '2':
                self.mine.run(nemesis, self.user)
                break
            elif select == '1':
                print(f'!! {self.user}님의 {self.mine.get_name()} vs 야생의 {nemesis.get_name()} !!\n')
                while True:
                    if self.mine.get_hp() <= 0:
                        print(f'야생의 {nemesis.get_name()}과(와)의 대결에서 패배했다!')
                        self.mine.add_xp(-5)
                        if self.mine.get_xp() <= 0: self.mine.set_xp(0)
                        print(f'{self.user}의 {self.mine.get_name()}의 경험치가 {self.mine.get_xp()}로 떨어졌습니다.')
                        break
                    elif nemesis.get_hp() <= 0:
                        print(f'야생의 {nemesis.get_name()}과(와)의 대결에서 승리했다!')
                        self.mine.add_xp(10)
                        print(f'{self.user}의 {self.mine.get_name()}의 경험치가 {self.mine.get_xp()}로 올랐습니다!')
                        if self.mine.get_xp() == 100:
                            self.mine.evolve()
                        break
                    else:
                        # user 포켓몬의 공격
                        i = 1
                        skill_names = list(self.mine.skill_dict.keys())
                        for skill_name in skill_names:
                            print(f'{i}) {skill_name}', end='  ')
                            i += 1
                        while True:
                            try:
                                select = int(input("\n공격을 고르세요 : "))
                            except ValueError:
                                print(f'1 ~ {len(skill_names)}번 중에서 골라주세요!')
                                continue
                            if 0 < select <= len(skill_names):
                                my_skill = skill_names[int(select) - 1]
                                self.mine.attack(nemesis, my_skill, self.mine.skill_dict[my_skill], self.user, "야생")
                                break
                            else:
                                print(f'1 ~ {len(skill_names)}번 중에서 골라주세요!')

                        if nemesis.get_hp() <= 0:
                            print(f'\n야생의 {nemesis.get_name()}과(와)의 대결에서 승리했다!')
                            self.mine.add_xp(10)
                            print(f'{self.user}의 {self.mine.get_name()}의 경험치가 {self.mine.get_xp()}로 올랐습니다!')
                            if self.mine.get_xp() == 100:
                                self.mine.evolve()
                            break

                        print()
                        # 야생 포켓몬의 공격
                        nemesis_skill = random.choice(list(nemesis.skill_dict.keys()))
                        nemesis.attack(self.mine, nemesis_skill, nemesis.skill_dict[nemesis_skill], "야생", self.user)
                        if self.mine.get_hp() <= 0:
                            print(f'\n야생의 {nemesis.get_name()}과(와)의 대결에서 패배했다!')
                            self.mine.add_xp(-5)
                            if self.mine.get_xp() <= 0:
                                self.mine.set_xp(0)
                            print(f'{self.user}의 {self.mine.get_name()}의 경험치가 {self.mine.get_xp()}로 떨어졌습니다.')
                            break
                        print()
                break
            else:
                print("1 ~ 2번 중에서 골라주세요!")

    def menu(self):
        while True:
            select = input("\n* 게임 메뉴 * \n1) 탐험하기 \n2) 체력 충전하기 \n3) 게임 종료하기 \n")
            if select == '1':
                happen = random.randint(0, 1)
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