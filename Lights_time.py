import sys
speed,light_count = 200, 1
lights = [[1000, 15], [3000, 10], [4000, 30], [5000, 30], [6000, 5], [7000, 10]] 
for trial_speed in range(speed,0,-1):
    for light in lights:
        time = round(light[0] / (trial_speed / 3.6),3)
        if ((time // light[1]) % 2) > 0:
            break
    else:
        print(trial_speed)
        break
    