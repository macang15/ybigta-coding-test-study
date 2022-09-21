n = list(map(int, input().split(' ')))
maxScore = [100, 100, 200, 200, 300, 300, 400, 400, 500]

sumn = 0
hacker = False
for i in range(0,len(n)):
    sumn += n[i]
    if n[i] > maxScore[i]:
        hacker = True   
    
if hacker == True :
    print('hacker')
elif sumn >= 100 :
    print('draw')
else:
    print('none')
