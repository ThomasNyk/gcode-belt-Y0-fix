import sys
import re

def main():
    file = open(sys.argv[1])
    
    pattern = re.compile(r'(?<=Y)([-+]?\d*\.\d+|\d+)(?= |$)')
    lowestY = 1000.0

    lines = file.readlines()

    validPart = False
    
    for i, line in enumerate(lines):
        if ";end of Start GCode" in line:
            validPart = True
            continue
        if ";end of Gcode" in line:
            validPart = False
            continue
        if "G1" in line and "Y" in line:
            match = float(re.findall(pattern, line)[0])
            if lowestY > match and validPart:
                print("New lowest at line " + str(i+1) + " equals: " + str(match))
                lowestY = match
    if lowestY == 1000.0:
        print("Error")
        return
    else:
        print("lowestY: " + str(lowestY))

    for i, line in enumerate(lines):
        if ";end of Start GCode" in line:
            validPart = True
            continue
        if ";end of Gcode" in line:
            validPart = False
            continue
        if "G1" in line and "Y" in line and validPart:
            match = float(re.findall(pattern, line)[0])
            newY = round(match - lowestY, 4)
            lines[i] = re.sub(pattern, str(newY), line)
    
    with open(sys.argv[1], 'w') as file:
        file.writelines(lines)

main()