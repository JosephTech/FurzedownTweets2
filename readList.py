def getList(fileName):
    lines = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
        return lines

if __name__ == "__main__":
    print(getList('/home/pi/jules/retweeter/furzedown/config/users.txt'))
    print(getList('/home/pi/jules/retweeter/furzedown/config/words.txt'))