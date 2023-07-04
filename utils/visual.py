import colorama

def painel():
    colorama.init()
    color = {
        'red': colorama.Fore.LIGHTRED_EX,
        'blue': colorama.Fore.CYAN,
        'reset': colorama.Fore.RESET
    }
    text = " ____  __ __  ____  __  ______\n/ __ )/ // / / __ \/ / / / __ \ \n/ __  / // /_/ /_/ / /_/ / / / \n/ /_/ /__  __/ ____/ __  / /_/ /\n/_____/  /_/ /_/   /_/ /_/\____/"
    print(f'{color["red"]}{text}{color["reset"]}')
    print(f'{color["blue"]}         https://github.com/B4PH0{color["reset"]}\n')
    print(f'{color["red"]}  Starting Bruteforce...')
painel()