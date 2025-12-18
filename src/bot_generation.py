import random

size = 10
empty = " ~ "
ship = " ▲ "
ships = [4,3,3,2,2,2,1,1,1,1]

class SeaBattleBot:
    def __init__(self):
        self.field = [[empty for column in range(size)] for row in range(size)]
        self.place_all_ships()

    def place_all_ships(self):
        for length in ships:
            placed = False
            while not placed:
                placed = self.place_ship(length)

    def place_ship(self,length):
        x = random.randint(0,size-1)
        y = random.randint(0,size-1)
        horizontal = random.choice([True,False])

        cells=[]
        for i in range(length):
            neighbor_x = x+i if horizontal else x
            neighbor_y = y if horizontal else y+i
            if not self.can_place(neighbor_x,neighbor_y):
                return False
            cells.append((neighbor_x,neighbor_y))

        for current_x,current_y in cells:
            self.field[current_x][current_y] = ship
        return True

    def can_place(self,x,y):
        if not (0<=x<size and 0<=y<size):
            return False
        if self.field[x][y] != empty:
            return False
        for direction_x in [-1,0,1]:
            for direction_y in [-1,0,1]:
                neighbor_x,neighbor_y=x+direction_x,y+direction_y
                if 0<=neighbor_x<size and 0<=neighbor_y<size:
                    if self.field[neighbor_x][neighbor_y] == ship:
                        return False
        return True
