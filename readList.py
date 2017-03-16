def getList(fileName):
    lines = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
        return lines

#print(getList('users.txt'))
#print(getList('words.txt'))