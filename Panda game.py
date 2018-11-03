w,h = 7,7
diagram = [['A', ' ', ' ', 'B', ' ', ' ', 'C'], ['|', ' ', ' ', '|', ' ', ' ', '|'], ['|', '-', '-', '|', ' ', ' ', '|'], ['|', ' ', ' ', '|', '-', '-', '|'], ['|', ' ', ' ', '|', '-', '-', '|'], ['|', ' ', ' ', '|', ' ', ' ', '|'], ['1', ' ', ' ', '2', ' ', ' ', '3']]
for line in diagram:
    print(line)
def position(x,y):
    global diagram
    if x < 0 or y < 0 or x > w-1 or y > h-1 :
        return("ERROR")
    return diagram[y][x]
for index,start in enumerate(diagram[0]):
    if start != " ":
        x,y = index,1
        while position(x,y) == '|' or position(x,y) == '-':
            if position(x-1,y) == '-':
                x -= 3
                if position(x-1,y) == '-':
                    x-= 3
            elif position(x+1,y) == '-':
                x += 3
                if position(x+1,y) == '-':
                    x+= 3
            if position(x,y) == '|':
                y+= 1
        else:
            print(start + str(position(x,y)))
    