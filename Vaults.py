import sys
r = 5
v = 20
vaults = [[3, 3], [1, 6], [4, 0], [4, 4], [0, 3], [3, 1], [1, 7], [3, 0], [5, 0], [6, 1], [2, 4], [3, 2], [4, 1], [0, 7], [0, 7], [4, 4], [0, 6], [5, 1], [2, 1], [2, 2]]
#start of program
def calc_times(digits,vowels):
    return ((10 ** digits) * (5 ** vowels))
times = []
for vault in vaults:
    times.append(calc_times(vault[0],vault[1]))
in_prog = times[:r]
times = times[r:]
total_time = 0
while in_prog:
    non_empty_vaults = []
    rob_count = 0
    in_prog.sort()
    removed_vault = in_prog[0]
    total_time += removed_vault
    for index,vault in enumerate(in_prog):
        in_prog[index] -= removed_vault
        if in_prog[index] != 0:
            non_empty_vaults.append(in_prog[index])
        else:
            rob_count += 1
    in_prog = non_empty_vaults
    if times:
        for _ in range(rob_count):
            in_prog.append(times[0])
            del(times[0])
print(total_time)