import random

class Tiger:
    def __init__(self, field_size):
        self.field_size = field_size
        self.x = 0
        self.y = 0
        self.state = "Выследить добычу"

    def move(self, hares):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        new_x = max(0, min(self.x + dx, self.field_size - 1))
        new_y = max(0, min(self.y + dy, self.field_size - 1))
        self.x = new_x
        self.y = new_y
        for hare in hares:
            if abs(self.x - hare[0]) <= 1 and abs(self.y - hare[1]) <= 1:
                self.state = "Атаковать добычу"
                return

    def attack(self, hares):
        if random.random() < 0.5:
            print("Тигр успешно атаковал зайца!")
            # Удаление зайца с поля
            for hare in hares:
                if abs(self.x - hare[0]) <= 1 and abs(self.y - hare[1]) <= 1:
                    hares.remove(hare)
                    break
            self.state = "Бежать домой"
        else:
            print("Заяц смог отбежать от тигра!")
            self.state = "Выследить добычу"

    def run_home(self):
        self.x = 0
        self.y = 0
def display_field(field_size, tiger, hares):
    for i in range(field_size):
        row = []
        for j in range(field_size):
            if tiger.x == i and tiger.y == j:
                row.append("T")
            elif (i, j) in hares:
                row.append("З")
            else:
                row.append(".")
        print("".join(row))

def main():
    field_size = 5
    tiger = Tiger(field_size)
    hares = []
    while len(hares) < 2:
        x = random.randint(0, field_size - 1)
        y = random.randint(0, field_size - 1)
        if (x, y) != (0, 0) and (x,y) not in hares:
            hares.append((x, y))

    while tiger.state != "Бежать домой":
        display_field(field_size, tiger, hares)
        print(f"Состояние тигра: {tiger.state}")

        if tiger.state == "Выследить добычу":
            tiger.move(hares)
        elif tiger.state == "Атаковать добычу":
            tiger.attack(hares)
        elif tiger.state == "Бежать домой":
            tiger.run_home()

    display_field(field_size, tiger, hares)
    print("Тигр вернулся домой.")

main()
