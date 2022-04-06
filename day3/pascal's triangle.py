class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l= []
        if numRows==1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            l=[[1],[1,1]]
            for i in range(2, numRows):
                for j in range(0, i+1):
                    if j==0:
                        l.append([1])
                    elif i==j:
                        l[i].append(1)
                    else:
                        l[i].append(l[i-1][j-1] + l[i-1][j])
            return l
