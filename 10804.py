num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start=[]
finish=[]
for i in range(0,10):
    s, f = map(int, input().split(' '))
    start.append(s-1)
    finish.append(f-1)

for i in range(0,10):
    num1 = num[start[i]:finish[i]+1]
    num1.reverse()
    num[start[i]:finish[i]+1] = num1
    
print(num)
    