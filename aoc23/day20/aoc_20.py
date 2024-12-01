import sys
from math import prod
from collections import deque
from numpy import lcm
import numpy as np
f = open(sys.argv[1],'r')

network = {'rx':['rx',[],0]}
for l in f:
    sender, receiver  = l.rstrip().split(' -> ')
    if sender[0] == '%':
        try:
            network[sender[1:]] = ['flipflop',receiver.split(', '),0]
        except:
            network[sender[1:]] = ['flipflop',[receiver],0]
    elif sender[0] == '&':
        try:
            network[sender[1:]] = ['conjunction',receiver.split(', '),{}]
        except:
            network[sender[1:]] = ['conjunction',[receiver],{}]
    else:
        try:
            network[sender] = ['broadcaster',receiver.split(', '),None]
        except:
            network[sender] = ['broadcaster',[receiver],None]

for k in network:
    for r in network[k][1]:
        if network[r][0] == 'conjunction':
            _,_,ins = network[r]
            ins[k] = 0


messages = deque([])
counters = [0,0]
def receive(i,sender,receiver,signal):
    counters[signal] +=1
    ty,re,st = network[receiver]
    if ty == 'flipflop':
        if signal == 0:
            newSt = (st+1)%2
            network[receiver] = [ty,re,newSt]
            for r in re:
                messages.append([receiver,r,newSt])
    elif ty == 'conjunction':
        st[sender] = signal
        m = 1-prod(st.values())
        for r in re:
            messages.append([receiver,r,m])
    elif ty == 'broadcaster':
        for r in re:
             messages.append([receiver,r,signal])

def button():
    messages.append(['button','broadcaster',0])
turnsOn = {}
for n in (network['hf'][2]):
    for nn in network[n][2]:
        turnsOn[nn] = []

for i in range(5000):
    button()
    while len(messages)>0:
        receive(i,*messages[0])
        messages.popleft()
    if i == 999:
        print("part1:", prod(counters))
    for t in turnsOn:
        if sum(network[t][2].values()) == 0:
            turnsOn[t].append(i+1)
#for t in turnsOn:
    #print(t, turnsOn[t],"\n")
    
#Cycles, found by inspection ...
print("part2:",lcm.reduce([4019,3881,3767,3769],dtype = np.int64))