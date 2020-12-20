def solve1(lines):
    tiles = {}
    for tile in '\n'.join(lines).split("\n\n"):
        id = int(tile.split()[1][:-1])
        l = tile.split("\n")[1:]
        tiles[id] = [l[0],''.join(i[0] for i in l), l[-1], ''.join(i[-1] for i in l)]
    possible = {}
    for i in tiles.keys():
        cur = []
        for j in tiles.keys():
            if i==j:continue
            if len(list(set(tiles[i]).intersection(set(tiles[j]))))!=0 or len(list(set([x[::-1] for x in tiles[i]]).intersection(set(tiles[j]))))!=0:
                    cur.append(j)
        possible[i] = cur
        
    asdf = list(set(i for i in possible.keys() if len(possible[i])==2))
    ret=1
    for i in asdf:ret*=i
    return ret

def solve2(lines):

    # if you're reading this, prepare to feel like you have no idea what the hell my code is doing
    # but hey, it works and I'm happy about that :)

    tiles = {}
    for tile in '\n'.join(lines).split("\n\n"):
        id = int(tile.split()[1][:-1])
        l = tile.split("\n")[1:]
        tiles[id] = [l[0],''.join(i[0] for i in l), l[-1], ''.join(i[-1] for i in l)]
    possible = {}
    for i in tiles.keys():
        cur = []
        for j in tiles.keys():
            if i==j:continue
            if len(list(set(tiles[i]).intersection(set(tiles[j]))))!=0 or len(list(set([x[::-1] for x in tiles[i]]).intersection(set(tiles[j]))))!=0:
                    cur.append(j)
        possible[i] = cur
    
    originalPossible = dict(possible)
    sidelength = int(len(tiles)**0.5)
    grid = [[-1 for j in range(sidelength)] for j in range(sidelength)]
    prevborder = []
    for ring in range(69):

        if len(possible)==0:
            break
        if len(possible)==1:
            grid[sidelength//2][sidelength//2] = list(possible.keys())[0]
            break

        # get corner+edge pieces
        edges = {i:possible[i] for i in possible.keys() if len(possible[i])<4}
        for i in edges.keys():
            new = []
            for j in edges[i]:
                if len(possible[j]) < 4:new.append(j)
            edges[i] = new 
        #build border
        for i in possible.keys():
            if len(possible[i])==2:
                curtile = i
                break
        border = [curtile]
        while True:
            for i in edges[curtile]:
                if i not in border:
                    curtile = i
                    border.append(i)
                    break  
            else: break
        # align ring
        if prevborder!=[]:
            startind = 0
            for i in border:
                if prevborder[1] in originalPossible[i] and prevborder[-1] in originalPossible[i]:
                    startind = border.index(i)
                    break
            border = border[startind:] + border[:startind]
            if prevborder[2] not in originalPossible[border[1]]:
                border = border[::-1]
                border = [border[-1]] + border[:-1]
        prevborder = list(border)
        slength = sidelength - ring*2
        m = [(1,0)]*(slength-1) + [(0,1)]*(slength-1) + [(-1,0)]*(slength-1) + [(0,-1)]*(slength-1)
        curpos = (ring, ring)
        positions = []
        for i in m:
            curpos = (curpos[0] + i[0], curpos[1] + i[1])
            positions.append(curpos)
        positions = [positions[-1]] + positions[:-1]

        for i in range(len(border)):
            grid[positions[i][1]][positions[i][0]] = border[i]

        # remove border pieces
        newpossible = {}
        for i in possible.keys():
            if i not in border:
                toapp=[]
                for j in possible[i]:
                    if j not in border:
                        toapp.append(j)
                newpossible[i] = toapp
        possible = dict(newpossible)


    tileimgs = {} 
    for tile in '\n'.join(lines).split("\n\n"):
        id = int(tile.split()[1][:-1])
        tileimgs[id] = tile.split("\n")[1:]

    # orient rows
    for y in range(len(grid)):
        for x in range(len(grid)-1):
            l = tileimgs[grid[y][x]]
            edges = [l[0],''.join(i[0] for i in l), l[-1], ''.join(i[-1] for i in l)]            
            k = tileimgs[grid[y][x+1]]
            neighbour_edges = [k[0],''.join(i[0] for i in k), k[-1], ''.join(i[-1] for i in k)]            
            matching_pair = None
            for i in range(len(edges)):
                for j in range(len(neighbour_edges)):
                    if edges[i] == neighbour_edges[j] or edges[i] == neighbour_edges[j][::-1]:
                        matching_pair = (i,j)
                        break
                if matching_pair!=None:break
            if matching_pair[0] == 0:
                # rotate clockwise
                tileimgs[grid[y][x]] = [''.join(i[j] for i in tileimgs[grid[y][x]][::-1]) for j in range(10)]
            elif matching_pair[0] == 2:
                # rotate anticlockwise
                tileimgs[grid[y][x]] = [''.join(i[j] for i in tileimgs[grid[y][x]]) for j in range(10)][::-1]
            elif matching_pair[0] == 1:
                # flip x
                tileimgs[grid[y][x]] = [i[::-1] for i in tileimgs[grid[y][x]]]

            if matching_pair[1] == 2:
                # rotate clockwise
                tileimgs[grid[y][x+1]] = [''.join(i[j] for i in tileimgs[grid[y][x+1]][::-1]) for j in range(10)]
            elif matching_pair[1] == 0:
                # rotate anticlockwise
                tileimgs[grid[y][x+1]] = [''.join(i[j] for i in tileimgs[grid[y][x+1]]) for j in range(10)][::-1]
            elif matching_pair[1] == 3:
                # flip x
                tileimgs[grid[y][x+1]] = [i[::-1] for i in tileimgs[grid[y][x+1]]]

    # orient columns
    for y in range(len(grid)-1):
        for x in range(len(grid)):
            l = tileimgs[grid[y][x]]
            edges = [l[0],''.join(i[0] for i in l), l[-1], ''.join(i[-1] for i in l)]            
            k = tileimgs[grid[y+1][x]]
            neighbour_edges = [k[0],''.join(i[0] for i in k), k[-1], ''.join(i[-1] for i in k)]            
            matching_pair = None
            for i in range(len(edges)):
                for j in range(len(neighbour_edges)):
                    if edges[i] == neighbour_edges[j] or edges[i] == neighbour_edges[j][::-1]:
                        matching_pair = (i,j)
                        break
                if matching_pair!=None:break
            if matching_pair[0] == 0:
                # flip y
                tileimgs[grid[y][x]] = tileimgs[grid[y][x]][::-1]

            if matching_pair[1] == 2:
                # flip y
                tileimgs[grid[y+1][x]] = tileimgs[grid[y+1][x]][::-1]

    actualgrid = []
    for t in tileimgs.keys():
        tileimgs[t] = [i[1:-1] for i in tileimgs[t]][1:-1]
    for i in grid:
        for k in range(8):
            actualgrid.append(''.join(tileimgs[j][k] for j in i))
        
    grids = []
    g=actualgrid
    grids.append(g)
    grids.append([g[y] for y in range(len(g)-1,-1,-1)])
    grids.append([g[y][::-1] for y in range(len(g))])
    grids.append([g[y][::-1] for y in range(len(g)-1,-1,-1)])
    k=[''.join(i[j] for i in actualgrid)[::-1] for j in range(len(actualgrid))]
    grids.append(k)
    grids.append([k[y] for y in range(len(k)-1,-1,-1)])
    grids.append([k[y][::-1] for y in range(len(k))])
    grids.append([k[y][::-1] for y in range(len(k)-1,-1,-1)])

    for g in grids:
        mask = ["                  # ","#    ##    ##    ###"," #  #  #  #  #  #   "] 
        count = 0
        asdf = list(list(i) for i in g)
        for y in range(len(actualgrid)-len(mask)):
            for x in range(len(actualgrid[0]) - len(mask[0])):
                foundMonster = True
                for dy in range(len(mask)):
                    for dx in range(len(mask[0])):
                        if mask[dy][dx]=="#" and g[y+dy][x+dx]!="#":
                            foundMonster = False
                            break
                    if not foundMonster:break
                if foundMonster:
                    for dy in range(len(mask)):
                        for dx in range(len(mask[0])):
                            if mask[dy][dx] == "#":
                                asdf[y+dy][x+dx] = "O"
                    count+=1
        if count>0:
            return sum(i.count("#") for i in asdf) 
        

import sys
lines = [l.rstrip('\n') for l in sys.stdin]
print("\033[96m\033[1m[*] PART 1:", solve1(lines), "\033[0m")
print("\033[92m\033[1m[*] PART 2:", solve2(lines), "\033[0m")