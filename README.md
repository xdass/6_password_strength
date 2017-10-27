# Password Strength Calculator

It's program that check password strength and print it level.<br>

Program check password by such parameters:
* use of both upper-case and lower-case letters (case sensitivity)
* inclusion of one or more numerical digits
* inclusion of special characters, such as @, #, $ and etc.
* prohibition of words found in a password blacklist

# How to start program
To start the script you need a blacklist.txt file, you'll find it on [blacklist.txt](https://github.com/xdass/6_password_strength/blob/master/blacklist.txt) <br>

**On linux:**
```bash
$ python password_strength.py
```
**On windows:**<br>
The same as linux

# Examples of the program
```
$ python password_strength.py
Введите пароль: qwerty
Очень слабый пароль
```

```
$ python password_strength.py
Введите пароль: Dmitry
Слабый пароль
```

```
$ python password_strength.py
Введите пароль: Dmitry123
Хороший пароль
```

```
$ python password_strength.py
Введите пароль: Dmitry123@
Очень крутой пароль
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
