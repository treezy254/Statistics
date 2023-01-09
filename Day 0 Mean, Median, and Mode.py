# Enter your code here. Read input from STDIN. Print output to STDOUT
N= int(input())
array = list(map(int,input().split()))
array = sorted(array,reverse=True)
print(round(sum(array)/N,1))
if len(array) % 2 == 1:
    print(round(array[len(array)//2 +1],1))
else:
    print(round(sum(array[len(array)//2 -1: len(array)//2 +1])/2,1))
mode = dict()
for i in range(len(array)):
    if array[i] in mode.keys():
        mode[array[i]]+= 1
    else:
        mode[array[i]] = 1
mode =min([key for key,value in mode.items() if value ==max(mode.values())])
print(mode)