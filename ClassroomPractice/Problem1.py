#!/usr/bin/python
def matrixChainOrder(p):
    le = len(p)
    l = 2
    m = [[0 for col in range(le)] for row in range(le)]
    s = [[0 for col in range(le)] for row in range(le)]
    for i in range(le):
        m[i][i] = 0
    
    for l in range(2,le):
        i = 0
        for i in range(le - l + 1):
            j = i + l - 1
            m[i][j] = 3000000
            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m[1][le-1],s

def printOptimalParens(s,i,j):
    if i == j:
        print('A'+ str(i))
    else:
        print('(')
        printOptimalParens(s,i,s[i][j])
        printOptimalParens(s,s[i][j]+1,j)
        print(')')


if __name__ == '__main__':
    se = [30, 35, 15, 5, 10, 20]
    le = len(se)
    result = matrixChainOrder(se)
    print(str(result[0]))
    printOptimalParens(result[1],1,le-1)