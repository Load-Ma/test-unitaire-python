from datetime import datetime


def goodby(now):
    if now.hour < 12:
        return "Bonne journée"
    elif now.hour == 12:
        return "Bon appétit"
    elif now.hour > 12:
        return "Au revoir"


def hello(now):
    if now.hour < 12:
        return "good morning world"
    elif now.hour == 12:
        return "Bon appétit"
    elif now.hour > 12:
        return "Bon après-midi"


def invertWord(word):
    if word.lower() == word.lower()[::-1]:
        return "Bien dit !"
    else:
        return word[::-1]


def console():
    now = datetime.now()
    print(hello(now))
    asking = True
    while asking:
        word = str(input(">  "))
        if word == "exit":
            now = datetime.now()
            print(goodby(now))
            asking = False
        else:
            print(invertWord(word))


if __name__ == '__main__':
    console()
