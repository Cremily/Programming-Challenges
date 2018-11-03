width,height = 17,5
count = 1
final_map = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '#', '#', '.', '.', '.', '#', '#', '#', '.', '.', '#', '.', '.', '.'], ['.', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '.'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
for line in final_map:
    print(line)
#code goes here
def count_hash(line):
    x = 0
    for char in line:
        if char == "#":
            x += 1
    return x
def hash_until(hash_map):
    count_list = []
    for line in hash_map:
        count_list.append(count_hash(line))
    return(count_list)
def tumble(width,height,hash_map):
    new_map = [ [] for x in range(width)]
    hash_count = hash_until(hash_map)
    for line_num,line in enumerate(new_map):
        for count in hash_count:
            if count >= width - line_num:
                line.append('#')
            else:
                line.append('.')
    return height,width,new_map
for i in range(count):
    width,height,final_map = tumble(width,height,final_map)
printable_map = []
for line in final_map:
    string = ""
    for char in line:
        string += char
    printable_map.append(string)
for line in printable_map:
    print(line)
