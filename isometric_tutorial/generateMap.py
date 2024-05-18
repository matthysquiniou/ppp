
with open("./config/map.txt","w") as f:
    
    for x in range(0,200):
        line = ""
        for y in range(0,200):
                if x > 75 and x < 125:
                    line += "2"
                else:
                     line+= "1"
            
        f.write(line+'\n')
    