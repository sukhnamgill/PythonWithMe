from typing import List, Tuple

maze = [
    ['S', 0,  1,  0,  0],
    [1,   0, 1,  0,  1],
    [0,   0, 0,  0,  0],
    [0,   0, 1,  1,  1],
    [0,   0, 0,  'E', 0]
]
rows=len(maze)
column=len(maze[0])
is_visited= [[False for _ in range(column)] for _ in range(rows)]
directions=[(0,1),(0,-1),(1,0),(-1,0)]

def is_valid(a,b):
    if (0<=a<rows and 0<=b<column) and (not is_visited[a][b]) and(maze[a][b]!=1) :
        print("valid")
        print(a,b)
        return True
    else:
        print("notvalid")
        return False
   
def main(x,y,path:List[Tuple[int,int]]):
    if not is_valid(x,y):
        return False
    path.append((x,y))
    
    print(x,y,"this items are added in path")
    is_visited[x][y]=True
    

    if maze[x][y]=='E':
        print("goal is founded")
        return True


    for dx,dy in directions:
        if main(x+dx,y+dy,path):
            return True
    print("backtracking")
    path.pop()
    return False

path=[]
start=None
for i in range(rows):
    for j in range(column):
        if maze[i][j]=="S":
            print("start found")
            start=[i,j]
        
main(start[0],start[1],path)
for i in path:
    print(i)
    maze[i[0]][i[1]]="*"
for i in range(len(maze)):
    print(maze[i])



