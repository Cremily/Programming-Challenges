means = """3.13 3.37 2.93 3.03 3.19 3.02 2.87 2.56
2.76
2.79
3.04
2.39
2.39
2.22
2.39
2.98
"""
SDs= """1.030 .967 1.108 1.061 1.121 1.185 .989 1.183 .990 1.134 1.081 1.139 1.058 1.082 1.133 1.130 1.125 1.165 1.090 .800 .966 1.051 1.050 1.053"""
new_means = means.split(" ")
new_sd = SDs.split(" ")
results = []
for x in range(0,24):
    try:
        results.append("%s (%s)" % (new_means[x],new_sd[x]))
    except Exception as e:
        print("out of bounds! %s" % (e))
print(results)

file = open("results.txt","w")
for x in range(0,24):
    file.write(results[x])
    file.write("\n")
file.close()
    