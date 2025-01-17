#time-m*n,space-m*n
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        q=deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    mat[i][j]=-1
                else:
                    q.append((i,j))
        dist=1
        while q:
            size=len(q)
            for i in range(size):
                curr=q.popleft()
                for j in dirs:
                    x=curr[0]+j[0]
                    y=curr[1]+j[1]
                    if x>=0 and x<len(mat) and y>=0 and y<len(mat[0]) and mat[x][y]==-1:
                        mat[x][y]=dist
                        q.append((x,y))
            dist+=1
            
        return mat
                
        
        
