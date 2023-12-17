import sys
f = open(sys.argv[1],'r')
heatmap = f.read().strip().split('\n')
heatmap = [[[[int(c),1e10,0,-1] for _ in range (3)] for c in l ] for l in heatmap]
heatmap[0][0] = [[heatmap[0][0][0][0],0,0,-1] for _ in range (3)]
print(heatmap[0][0])


def neighbour(x):
    c,r = x
    if c == 0:
        if r == 0:
            return [[c+1,r,1],[c,r+1,0]]
        else:
            return [[c+1,r,1],[c,r+1,0],[c,r-1,2]]
    elif r == 0:
        return [[c+1,r,1],[c-1,r,3],[c,r+1,0]]
    else:
        return [[c+1,r,1],[c-1,r,3],[c,r+1,0],[c,r-1,2]]
def step (c,r,d,l):
    print('c,r,d,l:',c,r,d,l)
    mindist = 1e10
    next = [-1,-1,-1,-1]
    for i in range(l-1,3):
        heatmap[r][c][i][2] = 1
    for nc,nr,nd in neighbour([c,r]):
        #print('nc,nr,nd:',nc,nr,nd)
        curdist = heatmap[r][c][0][1]
        #print("curdist = ", curdist)
        nl = (nd==d)*(1+l)+(nd!=d)*1
        #print('nl =',nl)
        for i in range(nl-1,3):
           #print('i= ',i)
            #print(heatmap[nr][nc][i][1])
            olddist =  heatmap[nr][nc][i][1]

            w = heatmap[nr][nc][i][0]
            print("w",w)
            print("curdist",curdist)
            alt = curdist+w

            if alt < olddist:
                heatmap[nr][nc][i][1] = alt
                print("setting new dist value, at ", nr,nc,i)
                heatmap[nr][nc][i][3] = [r,c]
            print("visited?",heatmap[nr][nc][i][2])
            print("newlength:", nl)
            print("newVal:", heatmap[nr][nc][i][1])
            if heatmap[nr][nc][i][1] < mindist and nl<3 and heatmap[nr][nc][i][2] == 0:
                mindist = heatmap[nr][nc][i][1]
                next = [nr,nc,nd,nl]
    if d == 0:
        return
    step(*next)
    

step(0,0,1,1)
  
        
        
            
                

            
            