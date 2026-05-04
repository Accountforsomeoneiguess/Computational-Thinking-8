world = [
    ["-", "-", "-"],
    ["|", ".", "|"],
    ["-", "-", "-"],
]
line = ""

for i in world:
    for j in i:
        line += str(j)
    print (line)
    line = ""