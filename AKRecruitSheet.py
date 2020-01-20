import os

class Recruit(object):
    def __init__(self):
        self.operators = {
            'Top Operator': 'Any Recruitable 6*',
            'Senior Operator': 'Any Recruitable 5*',
            'Medic, Support': 'Ptilopsis, Warfarin',
            'Vanguard, Support': 'Zima',
            'Defender, Survival': 'Vulcan',
            'Defender, DPS': 'Liskarm, Vulcan',
            'Defender, Shift': 'Croissant',
            'Supporter, DPS': 'Istina',
            'Supporter, Debuff': 'Pramanix',
            'Special, Slow': 'FEater',
            'Special, Survival': 'Manticore',
            'Special, DPS': 'Manticore, Cliffheart',
            'Summon': 'Mayer',
            'Nuker': 'Firewatch',
            'Crowd-Control': 'Texas, Projekt Red, Mayer',
            'Ranged, Support': 'Ptilopsis, Warfarin',
            'Healing, Support': 'Ptilopsis, Warfarin',
            'DP-Recovery, Support': 'Zima',
            'Defense, Survival': 'Vulcan',
            'Defense, DPS': 'Liskarm, Vulcan',
            'AOE, Debuff': 'Meteorite',
            'DPS, Shift': 'Cliffheart',
            'Shift, Defense': 'Croissant'
                    }
        self.qualification = ['Starter', 'Senior Operator', 'Top Operator']
        self.position = ['Melee', 'Ranged']
        self.classes = ['Vanguard', 'Medic', 'Guard', 'Supporter', 'Caster', 'Defender', 'Sniper', 'Special']
        self.affix = [
        'Debuff', 'Support', 'Slow', 'DPS', 
        'Healing', 'DP-Recovery', 'Survival', 
        'Defense', 'AOE', 'Fast-Redeploy', 'Shift', 
        'Summon', 'Crowd-Control', 'Nuker', 'Robot'
                ]
        self.tags = []

    @staticmethod
    def check_obtainable(operator_tags, available_tags):
        matches = 0
        for a_tag in available_tags:
            for o_tag in operator_tags:
                if a_tag == o_tag:
                    matches += 1
        if matches >= len(operator_tags):
            return True
        return False

    def display_tags(self):
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Qualifications' + Color.END)
        for index in range(len(self.qualification)):
            print('{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.qualification[index] not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.qualification[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.qualification) != 5 else ' | ')
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Position' + Color.END)
        for index in range(len(self.position)):
            print('{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.position[index] not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.position[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.position) != 5 else ' | ')
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Classes' + Color.END)
        for index in range(len(self.classes)):
            print('{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.classes[index] not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.classes[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.classes) != 5 else ' | ')
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Affixes' + Color.END)
        for index in range(len(self.affix)):
            print('{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.affix[index] not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.affix[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.affix) != 5 else ' | ')
        print('\n\n')
        
    def get_available_tags(self):
        selected = None
        while selected != '':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Color.UNDERLINE + Color.HEAD['TURQUOISE'] + 'Arknights Recruitment Sheet' + Color.END)
            self.display_tags()
            print(Color.HEAD['BRIGHT_RED'] + 'Leave empty to stop entering' + Color.END)
            selected = input(Color.HEAD['PALE_YELLOW'] + 'Enter tag > ' + Color.END)
            if selected != '' and (selected in self.qualification or selected in self.position or selected in self.classes or selected in self.affix):
                if selected not in self.tags:
                    self.tags.append(selected)
                else:
                    self.tags.remove(selected)

    def check_obtainable_wrapper(self):
        valid_obtainable = False
        print('\n\n'+ Color.UNDERLINE + Color.HEAD['BRIGHT_BLUE'] + 'Obtainables' + Color.END)
        for key, value in self.operators.items():
            key_list = key.split(', ')
            if self.check_obtainable(key_list, self.tags):
                print(Color.HEAD['BRIGHT_GREEN'] + key + Color.END + Color.HEAD['PALE_YELLOW'] + ' -> ' + Color.END + Color.HEAD['TURQUOISE'] + value + Color.END)
                if not valid_obtainable:
                    valid_obtainable = True
        if not valid_obtainable:
            print(Color.HEAD['BRIGHT_RED'] + 'NONE' + Color.END)


class Color(object):
    HEAD = {
        'BRIGHT_RED': '\033[91m',
        'BRIGHT_GREEN': '\033[92m',
        'PALE_YELLOW': '\033[93m',
        'BRIGHT_BLUE': '\033[94m',
        'BRIGHT_PURPLE': '\033[95m',
        'TURQUOISE': '\033[96m',
        None: '\033[0m'
    }
    UNDERLINE = '\033[4;37;40m'
    END = '\033[0m'

def main():
    while True:
        obj = Recruit()
        obj.get_available_tags()
        obj.check_obtainable_wrapper()
        print('\n\n')
        while True:
            exiting = input(Color.HEAD['PALE_YELLOW'] + 'Continue? (Y/N)' + Color.END + Color.HEAD['TURQUOISE'] + ' -> ' + Color.END + Color.HEAD['BRIGHT_RED'])
            print(Color.END)
            if exiting.upper()[0] == 'Y' or exiting.upper()[0] == 'N':
                break
        if exiting.upper()[0] == 'N':
            break
    print(Color.HEAD['BRIGHT_RED'] + 'Exiting.' + Color.END)

if __name__ == '__main__':
    main()

