import random


class Character:
    def __init__(self, name: str, hp: int, mp: int, attks: list) -> None:
        self.name = name
        self.hp = self.max_hp = hp
        self.mp = self.max_mp = mp
        self.attks = attks

    def show_bar(self, base: str, color: str, ticks: int = 50) -> None:
        value = getattr(self, base)
        if value < 0:
            value = 0
        max_value = getattr(self, 'max_' + base)
        bar = f"|{color}{round((value / max_value) * ticks) * '█':{ticks}}\033[m| {value}/{max_value}"
        print('', '_' * ticks)
        print(bar)

    def get_dmg(self, dmg: int) -> None:
        self.hp -= dmg

    def alive(self) -> None:
        if self.hp <= 0:
            return False
        else:
            return True

    def choice_attk(self, auto: bool) -> list:
        if auto:
            while True:
                attk_index = random.randint(0, len(self.attks) - 1)
                attk = self.attks[attk_index]
                if attk['cost'] <= self.mp:
                    break

            low_dmg = attk['dmg'] - 10
            high_dmg = attk['dmg'] + 10
            dmg = random.randrange(low_dmg, high_dmg)
            self.mp -= attk['cost']

        else:
            print('\nAttacks: ')
            c = 1
            for attk in self.attks:
                print(f'{c}. ', end='')
                for key, value in attk.items():
                    print(f'{key:4} = {value:<10}', end='')
                print()
                c += 1
            while True:
                try:
                    attk_index = int(input('\nChoose an attack: ')) - 1
                    attk = self.attks[attk_index]
                    low_dmg = attk['dmg'] - 10
                    high_dmg = attk['dmg'] + 10
                    if self.mp >= attk['cost']:
                        self.mp -= attk['cost']
                        dmg = random.randrange(low_dmg, high_dmg)
                    else:
                        raise ValueError
                except (IndexError, ValueError):
                    print('\nInvalid, try again.')
                except Exception as err:
                    print(err)
                else:
                    break

        return [attk['name'], dmg]
