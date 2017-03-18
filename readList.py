def getList(fileName):
    lines = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
        return lines

if __name__ == "__main__":
    print(getList('./config/users.txt'))
    print(getList('./config/words.txt'))