end = 1000
n = 1
curr = 0
number_line = [0]
while n < end:
    if (curr - n >= 0 and ((curr - n) not in number_line)):
        number_line.append(curr-n)
        curr = curr-n
        n += 1
    else:
        number_line.append(curr + n)
        curr = curr + n
        n += 1
print(number_line)