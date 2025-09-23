class Color:
    def __init__(self):
        self.default = "\033[0m"
        self.darkgrey = "\033[90m"
        self.green = "\033[32m"
        self.purple = "\033[95m"
        self.blue = '\033[94m'
        self.cyan = '\033[96m'
        self.yellow = '\033[93m'
        self.red = '\033[91m'
        self.clear = '\033[0m'
        self.bold = '\033[1m'
        self.underline = '\033[4m'
        self.error = "\033[91;1;4m"
        self.black = '\033[30m'
        self.darkred = '\033[31m'
        self.orange = '\033[33m'
        self.darkblue = '\033[34m'
        self.darkpurple = '\033[35m'
        self.darkcyan = '\033[36m'
        self.lightgrey = '\033[37m'
        self.lightgreen = '\033[92m'

color = Color()


def test_all_colors():
    print(f'{color.default}default')
    print(f'{color.lightgrey}light grey')
    print(f'{color.darkgrey}dark grey')
    print(f'{color.black}black')
    print(f'{color.green}green')
    print(f'{color.lightgreen}light green')
    print(f'{color.purple}purple')
    print(f'{color.darkpurple}dark purple')
    print(f'{color.blue}blue')
    print(f'{color.darkblue}dark blue')
    print(f'{color.cyan}cyan')
    print(f'{color.darkcyan}dark cyan')
    print(f'{color.orange}orange')
    print(f'{color.yellow}yellow')
    print(f'{color.red}red')
    print(f'{color.darkred}dark red')
    print(f'{color.clear}clear formatting')
    print(f'{color.bold}bold{color.clear}')
    print(f'{color.underline}underline{color.clear}')
    print(f'{color.error}error{color.clear}')
test_all_colors()






