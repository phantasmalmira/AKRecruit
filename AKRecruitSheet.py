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
            'Shift, Defense': 'Croissant',
            'Guard, AOE': 'Specter, Estelle',
            'Guard, Slow': 'Frostleaf',
            'Defender, Healing': 'Nearl, Gummy',
            'Sniper, Survival': 'Jessica',
            'Sniper, Slow': 'ShiraYuki',
            'Sniper, AOE': 'Meteorite, ShiraYuki',
            'Special': 'Projekt Red, Manticore, Cliffheart, FEater, Gravel, Rope, Shaw',
            'Shift': 'Cliffheart, FEater, Croissant, Rope, Shaw',
            'Debuff': 'Meteorite, Pramanix, Haze, Meteor',
            'Fast-Redeploy': 'Projekt Red, Gravel',
            'AOE, Melee': 'Specter, Estelle',
            'AOE, Survival': 'Specter, Estelle',
            'Melee, Slow': 'FEater, Frostleaf',
            'Slow, DPS': 'Istina, Frostleaf',
            'Defense, Healing': 'Nearl, Gummy',
            'Melee, Healing': 'Nearl, Gummy',
            'Survival, Ranged': 'Jesicca',
            'AOE, Slow': 'ShiraYuki',
            'DPS, Support': 'Doberman',
            'Support': '(>= 4 Hours)[Zima, Ptilopsis, Warfarin, Doberman]'
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
                if a_tag == o_tag.upper():
                    matches += 1
        if matches >= len(operator_tags):
            return True
        return False

    def display_tags(self):
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Qualifications' + Color.END)
        for index in range(len(self.qualification)):
            print('{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.qualification[index].upper() not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.qualification[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.qualification) != 5 else ' | ')
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Position' + Color.END)
        for index in range(len(self.position)):
            print('{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.position[index].upper() not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.position[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.position) != 5 else ' | ')
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Classes' + Color.END)
        for index in range(len(self.classes)):
            print('{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.classes[index].upper() not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.classes[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.classes) != 5 else ' | ')
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Affixes' + Color.END)
        for index in range(len(self.affix)):
            print('{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.affix[index].upper() not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.affix[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.affix) != 5 else ' | ')
        print('\n\n')
        
    def get_available_tags(self):
        selected = None
        while selected != '':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Color.UNDERLINE + Color.HEAD['TURQUOISE'] + 'Arknights Recruitment Sheet' + Color.END)
            self.display_tags()
            print(Color.HEAD['BRIGHT_RED'] + 'Leave empty to stop entering' + Color.END)
            selected = input(Color.HEAD['PALE_YELLOW'] + 'Enter tag > ' + Color.END)
            if selected != '':
                selected = self.fuzzy_detection(selected)
                if selected and selected.upper() not in self.tags:
                    self.tags.append(selected.upper())
                elif not selected:
                    continue
                else:
                    self.tags.remove(selected.upper())

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

    def run(self):
        self.get_available_tags()
        self.check_obtainable_wrapper()

    def fuzzy_detection(self, tag):
        _qualification = [qual.upper() for qual in self.qualification]
        _position = [pos.upper() for pos in self.position]
        _classes = [clas.upper() for clas in self.classes]
        _affix = [affx.upper() for affx in self.affix]
        if tag.upper() in _qualification or tag.upper() in _position or tag.upper() in _classes or tag.upper() in _affix:
            return tag
        elif len(tag) >= 3:
            for index in range(len(_qualification)):
                if tag.upper() in _qualification[index]:
                    return self.qualification[index]
            for index in range(len(_position)):
                if tag.upper() in _position[index]:
                    return self.position[index]
            for index in range(len(_classes)):
                if tag.upper() in _classes[index]:
                    return self.classes[index]
            for index in range(len(_affix)):
                if tag.upper() in _affix[index]:
                    return self.affix[index]
        return None


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
        Recruit().run()
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
