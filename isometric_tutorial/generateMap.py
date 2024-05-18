
with open("./config/map.txt","w") as f:
    
    for x in range(0,200):
        line = ""
        for y in range(0,200):
                line += "1"
            
        f.write(line+'\n')
    