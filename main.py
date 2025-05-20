import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 1000
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.2
        self.gladness -= 1
        self.money -= 200
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.progress +=0.1
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 300
    def to_work(self):
        print("Work time")
        self.money += 1000
        self.progress -= 0.4
        self.gladness -=2
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.money < 0:
            print("Poorest…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress ={round(self.progress, 2)}")
        print(f"Money = {self.money}")
    def live(self, day):
        day = "Day" + str(day) + "of" +self.name + "life"
        print(f"{day:=^50}")
        if self.progress <= 0.8:
            live_cube = 1
        elif self.money >= 3000:
            live_cube = random.randint(1, 3)
        elif self.gladness <= 1:
            live_cube = random.randint(2, 3)
        elif self.money<=1000:
            live_cube = 4
        else :
            live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive ()
nick = Student(name="Nick")
for day in range(366):
    if nick.alive == False:
        break
    nick.live(day)