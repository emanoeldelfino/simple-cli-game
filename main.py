from character import Character
import os

os.system('color')  # get colors on cmd

if __name__ == '__main__':
    colors = {
        'red': '\033[1;31m',
        'green': '\033[1;32m',
        'blue': '\033[1;34m'
    }

    player_attacks = [{'name': 'punch', 'cost': 0, 'dmg': 5},
                      {'name': 'kick', 'cost': 5, 'dmg': 15},
                      {'name': 'stab', 'cost': 10, 'dmg': 20},
                      {'name': 'blast', 'cost': 20, 'dmg': 60},
                      {'name': 'tornado', 'cost': 30, 'dmg': 80}]

    enemy_attacks = [{'name': 'sweep kick', 'cost': 0, 'dmg': 10},
                     {'name': 'flying kick', 'cost': 0, 'dmg': 20},
                     {'name': 'storm', 'cost': 0, 'dmg': 50}]

    player = Character(name='Artemis', hp=1000, mp=100, attks=player_attacks)

    enemy = Character(name='Alur', hp=400, mp=0, attks=enemy_attacks)

    print('\n' * 70)

    while True:
        print(f'\n{player.name} (YOU)')
        player.show_bar(base='hp', color=colors['green'], ticks=65)
        player.show_bar(base='mp', color=colors['blue'], ticks=65)

        print(f'\n{enemy.name} (ENEMY)')
        enemy.show_bar(base='hp', color=colors['red'], ticks=30)

        player_attk, player_dmg = player.choice_attk(auto=False)
        print('\n' * 70)
        if player_dmg > 0:
            print(f'{player.name} used {player_attk} dealing {player_dmg} points of damage on {enemy.name}.')
            enemy.get_dmg(dmg=player_dmg)
            if not enemy.alive():
                print('\nYou won.')
                break
        else:
            print(f'{player.name} missed {player_attk}.')

        enemy_attk, enemy_dmg = enemy.choice_attk(auto=True)
        if enemy_dmg > 0:
            print(f'\n{enemy.name} used {enemy_attk} dealing {enemy_dmg} points of damage on {player.name}.')
            player.get_dmg(dmg=enemy_dmg)

            if not player.alive():
                print('\nYou lost.')
                break
        else:
            print(f'{enemy.name} missed {enemy_attk}.')

print(f'\n{player.name} (YOU)')
player.show_bar(base='hp', color=colors['green'], ticks=65)
player.show_bar(base='mp', color=colors['blue'], ticks=65)

print(f'\n{enemy.name} (ENEMY)')
enemy.show_bar(base='hp', color=colors['red'], ticks=30)
print()
