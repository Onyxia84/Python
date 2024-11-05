from caracters import allcaracters
import time
from fight import fight


def game() :
    print("There is a skeleton, be ready to fight")
    time.sleep(1)
    print(allcaracters[1].name, 'is attacking you, get ready to fight now !')
    time.sleep(1)
    fight(allcaracters[1])