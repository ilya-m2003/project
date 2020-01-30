import random

def boundx(n, a=0, b=51):
    if n < a:
        return a
    elif n > b:
        return b
    return n

def boundy(n, a=0, b=27):
    if n < a:
        return a
    elif n > b:
        return b
    return n

def tolist(s):
    aa = [x for x in s]
    return aa

def create_level():
    coords = [['.' for j in range(27)] for i in range(51)]
    listcoords = []
    coords[0][0] = '#'
    coord = [0, 0]
    finish = [51, 27]
    coord = random.choice([[0, 1], [1, 0]])
    coords[coord[0]][coord[1]] = '#'
    listcoords.append([coord[0], coord[1]])
    coord = random.choice([[coord[0] + 1, coord[1]], [coord[0], coord[1] + 1]])
    coords[coord[0]][coord[1]] = '#'
    listcoords.append([coord[0], coord[1]])
    while coord != finish:
        count = 0
        while True:
            newcoord = random.choice([[coord[0] + 1, coord[1]], [coord[0], coord[1] + 1],
                                      [coord[0] - 1, coord[1]], [coord[0], coord[1] - 1]])
            newcoord = [boundx(newcoord[0]), boundy(newcoord[1])]
            
            if ([newcoord[0] + 1, newcoord[1]] not in listcoords[:len(listcoords) - 2]
                                     and [newcoord[0] - 1, newcoord[1]] not in listcoords[:len(listcoords) - 2]
                                      and [newcoord[0], newcoord[1] + 1] not in listcoords[:len(listcoords) - 2]
                                      and [newcoord[0], newcoord[1] - 1] not in listcoords[:len(listcoords) - 2]
                                      and newcoord not in listcoords
                                      and 0 < newcoord[0] <= 51 and 0 < newcoord[1] <= 27):
            #if newcoord not in listcoords:
                coord = newcoord
                #print(coord[0], coord[1])
                coords[coord[0]][coord[1]] = '#'
                listcoords.append([coord[0], coord[1]])
                #print('break')
                break
            if count >= 1:
                coords[listcoords[len(listcoords) - 1][0]][listcoords[len(listcoords) - 1][1]] = '.'
                coord = listcoords[len(listcoords) - 2]
                listcoords = listcoords[:len(listcoords) - 1]
            else:
                count = count + 1
                #print(count)


    #print(len(coords), len(coords[0])

    coords[0][0] = "@"
    coords[51][27] = '*'
                
                
    level = []
    
    for i in range(27):
        s = ''
        for j in range(51):
            s += coords[j][i]
        #print(s)
        level.append(s)
    
    
    return level
            

aa = [tolist(i) for i in create_level()]
bb = [tolist(i) for i in create_level()]
cc = [tolist(i) for i in create_level()]

file = open("data/map1.txt", "w")

for i in range(len(aa)):
    for j in range(len(bb)):
        if aa[i][j] == '#' or bb[i][j] == '#' or cc[i][j] == '#':
            aa[i][j] = '#'
    print(aa[i])
    file.write("".join(aa[i]) + "\n")
file.close()
            
        
            
                                  
    
