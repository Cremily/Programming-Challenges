start_map = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', ' ', '@', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', 'X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', 'B', 'X', 'X', '$', '#'], ['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
for line in start_map:
    print(line)
#code goes here
for y_index,line in enumerate(start_map):
    for x_index,row in enumerate(line):
        if start_map[y_index][x_index] == "@":
            x,y = x_index,y_index
obstacles = ['#','X']
class Default_Movement():
    def choose_move(self,x,y):
        if start_map[y+1][x] not in obstacles:
            return "s"
        elif start_map[y][x+1] not in obstacles:
            return "e"
        elif start_map[y-1][x] not in obstacles:
            return "n"
        elif start_map[y][x-1] not in obstacles:
            return "w"
class Class():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.move_state = Default_Movement()
        self.breaker = False
    def change_breaker(self):
        global obstacles
        if self.breaker == False:
            obstacles = ['#']
            self.breaker = True
        else:
            obstacles = ['#','X']
            self.breaker = False
    def curr_pos(self):
        return start_map[self.y][self.x]
    def check_pos(self):
        position = self.curr_pos()
        if position == "B":
            self.change_breaker()
            position = " "
        if position == "X" and self.breaker == True:
            start_map[self.y][self.x] = ' '
            position = " "
        if position == " ":
            return False
        if position == "@":
            return False
        if position == '$':
            return "finish"
        else:
            return "error"
    def go_south(self):
            while (start_map[self.y+1][self.x] not in obstacles):
                self.y = self.y + 1
                print("SOUTH")
                if self.check_pos():
                    break
    def go_north(self):
        while (start_map[self.y-1][self.x] not in obstacles):
            self.y += -1
            print("NORTH")
            if self.check_pos():
                break
    def go_east(self):
        while (start_map[self.y][self.x+1] not in obstacles): 
            self.x += 1
            print("EAST")
            if self.check_pos():
                break
    def go_west(self):
        while (start_map[self.y][self.x-1] not in obstacles):
            self.x -= 1
            print("WEST")
            if self.check_pos():
                break
    def choose_move(self):
        position = self.curr_pos()
        if position == 'E':
            self.go_east()
        elif position == "N":
            self.go_north()
        elif position == "W":
            self.go_west()
        elif position == "S":
            self.go_south()
        else:
            direction = self.move_state.choose_move(self.x,self.y)
            if direction == "s":
                self.go_south()
            elif direction == "e":
                self.go_east()
            elif direction == "n":
                self.go_north()
            elif direction == "w":
                self.go_west()
    def move_loop(self):
        while self.check_pos() != "finish":
            self.choose_move()
c = Class(x,y)
c.move_loop()
