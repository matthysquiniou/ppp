import random

MapSize = (75,75)

with open("./config/map.txt","w") as f:
    
    for x in range(0,MapSize[0]):
        line = ""
        for y in range(0,MapSize[1]):
                
                if (x > MapSize[0] // 4 and x < (MapSize[0] // 4) *3) or (y > MapSize[1] // 4 and y < (MapSize[1] // 4) *3):
                    line += "2"
                elif (x > MapSize[0] // 4 -5 and x < (MapSize[0] // 4) *3 +5) or (y > MapSize[1] // 4 -5 and y < (MapSize[1] // 4) *3 +5):
                    line += "3"
                else:
                    if random.randint(0,10) == 5:
                        line+= "0"
                    else:
                        line+= "1"
        f.write(line+'\n')
    