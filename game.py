import time


class GameRole:
    # The step distance for each move
    def __init__(self, name):
        self.__name = name
        self.__x = 0
        self.__y = 0
        self.__z = 0

    def leftMove(self):
        self.__x -= 5

    def rightMove(self):
        self.__x += 5

    def upMove(self):
        self.__y += 5

    def downMove(self):
        self.__y -= 5

    def jumpMove(self):
        self.__z += 5

    def squatMove(self):
        self.__z -= 5

    def attack(self):
        print("%slaunched an attack..." % self.__name)

    def showPosition(self):
        print(
            "%sposition：(x:%s, y:%s, z:%s)"
            % (self.__name, self.__x, self.__y, self.__z)
        )


def execute_command(command, role):
    if command == "L":
        role.leftMove()
        role.showPosition()
    elif command == "R":
        role.rightMove()
        role.showPosition()
    elif command == "U":
        role.upMove()
        role.showPosition()
    elif command == "D":
        role.downMove()
        role.showPosition()
    elif command == "JP":
        role.jumpMove()
        role.showPosition()
        time.sleep(0.5)
        role.squatMove()
        role.showPosition()
        time.sleep(0.5)
    elif command == "A":
        role.attack()
    elif command == "LU":
        role.leftMove()
        role.upMove()
        role.showPosition()
    elif command == "LD":
        role.leftMove()
        role.downMove()
        role.showPosition()
    elif command == "RU":
        role.rightMove()
        role.upMove()
        role.showPosition()
    elif command == "RD":
        role.rightMove()
        role.downMove()
        role.showPosition()
    elif command == "LA":
        role.leftMove()
        role.attack()
    elif command == "RA":
        role.rightMove()
        role.attack()
    elif command == "UA":
        role.upMove()
        role.attack()
