import sys
f = open(sys.argv[1],'r')

ps = [l.rstrip().split(',') for l in f]
ins = [[p.split('-') for p in pp]  for pp in ps ]
s1 = 0
s2 = 0 
for i in ins:
    if (int(i[0][1])-int(i[1][0])) * (int(i[0][0])-int(i[1][1])) <= 0:
        s2+=1
    if (int(i[0][0])-int(i[1][0])) * (int(i[0][1])-int(i[1][1])) <= 0:
        s1+=1
print(s1,s2)