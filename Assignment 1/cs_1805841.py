#1805841

def virus(filename):
    lineToBeAdded = ' ; print("Virus")'
    newLine = ''
    
    lineList = []

    lineIndex = int(0)

    with open(filename) as file:
        for line in file:
            lineIndex += 1
            
            if lineIndex == 52:
                newLine = line.rstrip() + lineToBeAdded + '\n'
                lineList.append(newLine)
                
            else:
                lineList.append(line)
            
    file = open(filename, "w")
    for line in lineList:
        file.write(line)
    
    file.close()


if __name__ == '__main__':
    
    virus("sfs.py")
