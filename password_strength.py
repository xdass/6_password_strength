import re
import getpass
from string import punctuation


def load_passwords_blacklist(filename):
    try:
        with open(filename) as file:
            bad_passwords = file.read().split('\n')
            return bad_passwords
    except FileNotFoundError:
        return None


def get_password_strength(password, bad_passwords):
    password_strength_points = 1
    if password in bad_passwords:
        return password_strength_points
    if re.search(r'[A-Z]+', password) and re.search(r'[a-z]+', password):
        password_strength_points += 3
    else:
        password_strength_points += 2
    if re.search(r'\d+', password):
        password_strength_points += 3
    if re.search(r'[{}]+'.format(punctuation), password):
        password_strength_points += 3
    return password_strength_points


def print_password_strength(password_strength):
    if password_strength == 1:
        print('Очень слабый пароль')
    if (password_strength > 1) and (password_strength < 6):
        print('Слабый пароль')
    if (password_strength > 6) and (password_strength < 10):
        print('Хороший пароль')
    if password_strength == 10:
        print('Очень крутой пароль')

if __name__ == '__main__':
    user_password = getpass.getpass(prompt='Введите пароль: ')
    blacklist = load_passwords_blacklist('blacklist.txt')
    password_strength = get_password_strength(user_password, blacklist)
    print_password_strength(password_strength)
