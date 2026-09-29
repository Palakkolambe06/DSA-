'''Print patterns -
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ") # end=" " is used to print in same line.
    print() # we want new line that's why we write print() here. If we don't write this then all the output will be in a single line.

reverse pattern -
5 4 3 2 1
4 3 2 1 
3 2 1
2 1
1

n = 5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()


5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''

n = 5
for i in range(1,n+1):
    for j in range(n, i-1, -1):
        print(j,end=" ")
    print()

'''hw - hollow pyramid pattern
1. * * * 

2.      *
      *   *
    *   *   *
  *   *   *   *
  
3.           *
             *
         * * * * * 
             *
             *
'''