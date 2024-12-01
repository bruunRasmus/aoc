import sys
f = open(sys.argv[1],'r')

winds = [l for l in f][0]
def vis_grid(g):
    for y in range(g.heighest+1):
        for x in range(7):
            if [x,y] in g.occupied:
                print("#",end="")
            else:
                print(".",end = "")
        print()

def add(coords,vector):
    
    return [[c[0]+vector[0],
             c[1]+vector[1]] for c in coords]

    

class grid:
    def __init__(self):
        self.occupied = {0:[i for i in range(7)]}
        self.heighest = 0

    def get_wind(self,i):
        return [1,0] if winds[i%len(winds)] == ">" else [-1,0]
    

    def is_occupied(self,coords):
        for c in coords:
            if c[0]<0 or c[0]>6:
                return True
            if c[1] in self.occupied.keys():
                if c[0] in self.occupied[c[1]]:
                    return True
        return False
        
    
    def blow(self,rock,wind):
        new_pos = add(rock.coords,wind)
        rock.coords = new_pos if not self.is_occupied(new_pos) else rock.coords
        
    def fall(self,rock):
        new_pos = add(rock.coords,[0,-1])
        if self.is_occupied(new_pos):
            rock.is_set = True
            max_y = self.heighest
            for c in rock.coords:
                if c[1] in self.occupied.keys():
                    self.occupied[c[1]].append(c[0])
                else:
                    self.occupied[c[1]] = [c[0]]
                max_y = max(max_y,c[1])
            self.heighest = max_y
        else:
            rock.coords = new_pos
    
    def drop(self,rock,i):
        rock.coords = add(rock.coords,[2,self.heighest+4])
        j = 0
        while not rock.is_set:
            
            self.blow(rock,self.get_wind(i+j))
            self.fall(rock)
            j+=1
        return i+j


class rock:
    def __init__(self,shape_idx):
        self.options = [[[0,0],[1,0],[2,0],[3,0]],
                      [[0,1],[1,0],[1,1],[1,2],[2,1]],
                      [[0,0],[1,0],[2,0],[2,1],[2,2]],
                      [[0,0],[0,1],[0,2],[0,3]],
                      [[0,0],[1,0],[0,1],[1,1]]]
        self.coords = self.options[shape_idx]
        self.is_set = False





N = 2022
g = grid()
k = 0 
for i in range(N):
    if i%100 == 0:
        print(g.heighest)
    r = rock(i%5)
    k = g.drop(r,k)
#print(g.heighest)
    




