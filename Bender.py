l,c = (5, 5)
start_map = [['#', '#', '#', '#', '#'], ['#', '@', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#'], ['#', ' ', ' ', '$', '#'], ['#', '#', '#', '#', '#']]
for line in start_map:
    print(line)
#code goes here
for y_index,line in enumerate(start_map):
    for x_index,row in enumerate(line):
        if start_map[y_index][x_index] == "@":
            x,y = x_index,y_index

class State():
    pass
class Normal_State(State):
    def choose_move(self,x,y):
        if start_map[y+1][x] not in ["X","#"]:
            return "s"
        elif start_map[y][x+1] not in ["X","#"]:
            return "e"
        elif start_map[y-1][x] not in ["X","#"]:
            return "n"
        elif start_map[y][x-1] not in ["X","#"]:
            return "w"
            
class Bender():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = Normal_State()
    def curr_pos(self):
        return start_map[self.y][self.x]
    def check_pos(self):
        position = self.curr_pos()
        if position == " ":
            return False
        if position == "@":
            return False
        if position == '$':
            return "finish"
        else:
            return "error"
    def go_north(self):
        while (start_map[self.y-1][self.x] not in ['#',"X"]) and not self.check_pos():
            self.y += -1
    def go_east(self):
        while (start_map[self.y][self.x+1] not in ['#',"X"]) and not self.check_pos(): 
            self.x += 1
    def go_south(self):
        while (start_map[self.y+1][self.x] not in ['#',"X"]):
            self.y = self.y + 1
    def go_west(self):
        while (start_map[self.y][self.x-1] not in ['#',"X"]) and not self.check_pos():
            self.x -= 1
    def choose_move(self):
        while self.check_pos != "Finish":
            move = self.state.choose_move(self.x,self.y)
            if move == "n":
                self.go_north()
            elif move == "e":
                self.go_east()
            elif move == "s":
                self.go_south()
            elif move == "w":
                self.go_west()
            
bender = Bender(x,y)
bender.choose_move()

    