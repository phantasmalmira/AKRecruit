import os
from operator import itemgetter
from itertools import combinations

class Recruit(object):
    def __init__(self):
        self.operators = []
        self.operator_file = 'Operators.txt'
        self.qualification = ['Starter', 'Senior Operator', 'Top Operator']
        self.position = ['Melee', 'Ranged']
        self.classes = ['Vanguard', 'Medic', 'Guard', 'Supporter', 'Caster', 'Defender', 'Sniper', 'Specialist']
        self.affix = [
        'Debuff', 'Support', 'Slow', 'DPS', 
        'Healing', 'DP-Recovery', 'Survival', 
        'Defense', 'AoE', 'Fast-Redeploy', 'Shift', 
        'Summon', 'Crowd Control', 'Nuker', 'Robot'
                ]
        self.tags = []
        self.obtainables = []

    def read_as_dict(self):
        with open(self.operator_file) as f:
            lines = f.readlines()
        rarity = 0
        for line in lines:
            if '# ' in line:
                rarity = int(line[2])
            if not (line[0] == '#' or line[0] == '\n'):
                line = line.strip()
                temp = line.split(' = ')
                operator_name = temp[0]
                operator_tags = temp[1].split(', ')
                operator_exclusive = False
                if 'Exclusive' in operator_tags:
                    operator_exclusive = True
                    operator_tags.remove('Exclusive')
                self.operators.append(Operator(operator_name, operator_tags, rarity, operator_exclusive))

    @staticmethod
    def check_obtainable(operator_tags, available_tags):
        matches = 0
        for index in range(len(available_tags)):
            if available_tags[index] in [x.upper() for x in operator_tags]:
                matches += 1
        if 'TOP OPERATOR' in [x.upper() for x in operator_tags] and 'TOP OPERATOR' not in available_tags:
            return False
        elif matches == len(available_tags):
            return True
        return False

    def display_tags(self):
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Qualifications' + Color.END)
        for index in range(len(self.qualification)):
            print('{}{}'.format(Color.END, '| ' if index % 5 == 0 else ' ') + '{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.qualification[index].upper() not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.qualification[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.qualification) != 5 else ' | ')
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Position' + Color.END)
        for index in range(len(self.position)):
            print('{}{}'.format(Color.END, '| ' if index % 5 == 0 else ' ') + '{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.position[index].upper() not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.position[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.position) != 5 else ' | ')
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Classes' + Color.END)
        for index in range(len(self.classes)):
            print('{}{}'.format(Color.END, '| ' if index % 5 == 0 else ' ') + '{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.classes[index].upper() not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.classes[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.classes) != 5 else ' | ')
        print('\n\n' + Color.UNDERLINE + Color.HEAD['BRIGHT_GREEN'] + 'Affixes' + Color.END)
        for index in range(len(self.affix)):
            print('{}{}'.format(Color.END, '| ' if index % 5 == 0 else ' ') + '{color}'.format(color=Color.HEAD['BRIGHT_BLUE'] if self.affix[index].upper() not in self.tags else Color.HEAD['PALE_YELLOW']) + '{:^15}'.format(self.affix[index]) + Color.END, end=' |\n' if (index + 1) % 5 == 0 and len(self.affix) != 5 else ' | ')
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
        print('\n\n'+ Color.UNDERLINE + Color.HEAD['BRIGHT_BLUE'] + 'Obtainables' + Color.END + ' : ' + Color.HEAD['PALE_YELLOW'] + 'Sorted by average rarity (EX=Exclusive to Recruiting)')
        self.read_as_dict()
        
        for index in range(3, 0, -1):
            for subset in combinations(self.tags, index):
                obtainable_operator = []
                for operator in self.operators:
                    if self.check_obtainable(operator.tags, list(subset)):
                        obtainable_operator.append(operator)
                if obtainable_operator:
                    average_rarity = sum([x.rarity for x in obtainable_operator]) / len(obtainable_operator)
                    self.obtainables.append((subset, obtainable_operator, average_rarity))
        
        self.obtainables.sort(key=itemgetter(2), reverse=True)

        for index in range(len(self.obtainables)):
            print('\n' + '{}'.format(Color.UNDERLINE + Color.HEAD['TURQUOISE'] + ', '.join(self.obtainables[index][0]) + Color.END))
            for index2 in range(len(self.obtainables[index][1])):
                print('{}{}{}{:^33}'.format(Color.END, '| ' if index2 % 5 == 0 else ' ', Color.HEAD['BRIGHT_GREEN'], self.obtainables[index][1][index2].name + ' {}({}*{}{}{})'.format(Color.HEAD['BRIGHT_RED'], str(self.obtainables[index][1][index2].rarity), Color.HEAD['PALE_YELLOW'], 'EX' if self.obtainables[index][1][index2].exclusive else '', Color.HEAD['BRIGHT_RED'])) + Color.END, 
                end=' |\n' if (index2 + 1) % 5 == 0 and index2 + 1 != len(self.obtainables[index][1]) else ' | ')
            print()

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

class Operator(object):
    def __init__(self, name, tags, rarity, exclusive=False):
        self.name = name
        self.tags = tags
        self.rarity = rarity
        self.exclusive = exclusive


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
