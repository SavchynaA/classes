


class Human():
    energy = 100
    def __init__(self, name, surname, gender) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
    def __repr__(self):
        return f'Human({self.name}, {self.surname}, {self.gender}, energy: {self.energy})'
    def eat(self):
        self.energy = self.energy + 5
    def sleep(self):
        self.energy = self.energy + 10
    def talk(self):
        self.energy = self.energy - 5
    def walk(self):
        self.energy = self.energy - 10
    def do_homework(self):
        self.energy = self.energy - 90

if __name__ == '__main__':
    man_1 = Human('Misha', 'Rzhavyi', 'man')
   # print(man_1)
    man_2 = Human('Ihor', 'Torosyan', 'man')
   # print(man_2)
    man_3 = Human('Olexiy', "Yallin", 'man')
   # print(man_3)
    woman_1 = Human('Ruslana', 'Mudrats', 'woman')
   # print(woman_1)
    woman_2 = Human('Darya', 'Bobrova', 'woman')
   # print(woman_2)

    man_1.do_homework()
    man_1.talk()


    man_2.do_homework()
    man_2.talk()

    man_3.sleep()
    man_3.talk()
    man_3.walk()

    woman_1.eat()
    woman_1.talk()

    woman_2.sleep()
    woman_2.talk()

    print(man_1)
    print(man_2)
    print(man_3)
    print(woman_1)
    print(woman_2)

    listOfHumans = [man_1, man_2, man_3, woman_1, woman_2]
    listOfEnergy = [man_1.energy, man_2.energy, man_3.energy, woman_1.energy, woman_2.energy]
    max = max(listOfEnergy)
    #print (max)

    for i in range(len(listOfEnergy)):
        if max == listOfEnergy[i]:
            print(f"A Person with the highest level of energy: {listOfHumans[i]}")


